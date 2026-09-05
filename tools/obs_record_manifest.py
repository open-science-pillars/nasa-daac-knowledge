# /// script
# requires-python = ">=3.10"
# dependencies = ["netcdf4", "numpy"]
# ///
"""Manifest and verify an observational data tree, and stamp it.

The science record's manifest vouches for ECCO granules with the
archive's own checksums. An observational record may have no CMR
behind it: the programme that made it serves the files, revises them
in place, and identifies the release inside the files (a version and a
DOI in the netCDF global attributes). So the tree is hashed locally at
retrieval, the identity is READ FROM THE FILES rather than declared,
and the fetch record the retriever left in the tree (SOURCE.json:
URLs, server timestamps or archive checksums, retrieval time) is
carried into the manifest. An archived record fetched through CMR by
obs_record_fetch.py is treated the same way: the archive's checksums
are verified at fetch, and the identity is still read from the files.

  build   --data-root TREE --out MANIFEST [--version V --doi D]
          hashes every file (SHA-256), reads version and DOI from every
          netCDF file's attributes, refuses if two files disagree or
          if --version/--doi were given and the files say otherwise
  verify  --manifest MANIFEST --data-root TREE [--stamp]
          re-hashes the tree against the manifest, refuses any missing
          or changed file and any undeclared file, and with --stamp
          leaves RECORD.json (record name, manifest sha256, time,
          report sha256) for sanctioned computations to copy into
          their receipts, exactly as for the science record.

Credentials are used for nothing here; nothing is fetched.
"""
import argparse
import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path

SKIP = {"SOURCE.json", "RECORD.json", "SHA256SUMS", ".DS_Store"}


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def nc_identity(p: Path) -> dict:
    """Version and DOI as the file states them, plus its time axis."""
    import netCDF4 as nc
    import numpy as np
    ds = nc.Dataset(p)
    attrs = {a.lower(): str(getattr(ds, a)).strip() for a in ds.ncattrs()}
    # Producers name these differently: RAPID writes version and doi,
    # PO.DAAC's NASA-SSH grids write product_version and put the DOI in
    # id. Read every name that means the same thing, in that order.
    version = (attrs.get("version") or attrs.get("dataset_version")
               or attrs.get("product_version"))
    doi = attrs.get("doi", "")
    if not doi and re.match(r"^(doi:)?\s*10\.\d{4,}/", attrs.get("id", ""), re.I):
        doi = attrs["id"]
    doi = re.sub(r"^doi:\s*", "", doi, flags=re.I).strip()
    out = {"version": version, "doi": doi}
    if "time" in ds.variables:
        t = ds.variables["time"]
        vals = np.atleast_1d(t[:])        # a scalar time is one epoch
        d = nc.num2date(vals[[0, -1]], t.units,
                        getattr(t, "calendar", "standard"))
        out["time"] = {"n": int(len(vals)), "first": str(d[0]),
                       "last": str(d[1]), "units": t.units}
    out["variables"] = sorted(v for v in ds.variables if v != "time")
    ds.close()
    return out


def norm_version(v):
    return (v or "").lower().replace("-", ".")


def build(args) -> int:
    root = args.data_root.expanduser().resolve()
    source = json.loads((root / "SOURCE.json").read_text()) \
        if (root / "SOURCE.json").exists() else None
    if source is None:
        sys.exit(f"{root} has no SOURCE.json: the retriever must leave the "
                 f"fetch record (urls, server timestamps, retrieval time) "
                 f"before the tree can be manifested")
    files, ident = [], {}
    for p in sorted(x for x in root.rglob("*") if x.is_file()
                    and x.name not in SKIP):
        row = {"path": str(p.relative_to(root)), "bytes": p.stat().st_size,
               "sha256": sha256(p)}
        if p.suffix == ".nc":
            row["identity"] = nc_identity(p)
            ident[row["path"]] = row["identity"]
        files.append(row)
    versions = {norm_version(i["version"]) for i in ident.values()}
    dois = {i["doi"] for i in ident.values()}
    if len(versions) != 1 or len(dois) != 1:
        sys.exit(f"the netCDF files do not agree on one release: versions "
                 f"{sorted(versions)}, dois {sorted(dois)}")
    version, doi = versions.pop(), dois.pop()
    if args.version and norm_version(args.version) != version:
        sys.exit(f"files say version {version!r}, not {args.version!r}")
    if args.doi and args.doi.lower() != doi.lower():
        sys.exit(f"files say DOI {doi!r}, not {args.doi!r}")
    manifest = {"record": source.get("record") or args.record,
                "generated_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
                "identity": {"version": version, "doi": doi,
                             "read_from": sorted(ident)},
                "source": source, "files": files,
                "total_bytes": sum(f["bytes"] for f in files)}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(manifest, indent=1) + "\n")
    print(f"{manifest['record']}: {len(files)} files, "
          f"{manifest['total_bytes'] / 1048576:.1f} MB, version {version}, "
          f"doi {doi} -> {args.out}")
    return 0


def verify(args) -> int:
    root = args.data_root.expanduser().resolve()
    mbytes = args.manifest.read_bytes()
    manifest = json.loads(mbytes)
    msha = hashlib.sha256(mbytes).hexdigest()
    report = {"verified_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
              "record": manifest["record"], "manifest_sha256": msha,
              "data_root": str(root), "declared": len(manifest["files"]),
              "present": 0, "checksum_ok": 0, "failures": [],
              "tool_sha256": sha256(Path(__file__))}
    declared = set()
    for row in manifest["files"]:
        p = root / row["path"]
        declared.add(p)
        if not p.exists():
            report["failures"].append({"path": row["path"],
                                       "check": "presence"})
            continue
        report["present"] += 1
        if sha256(p) == row["sha256"]:
            report["checksum_ok"] += 1
        else:
            report["failures"].append({"path": row["path"],
                                       "check": "checksum"})
    extras = sorted(str(p.relative_to(root)) for p in root.rglob("*")
                    if p.is_file() and p not in declared
                    and p.name not in SKIP)
    if extras:
        report["failures"].append({"check": "exact", "undeclared": extras})
    report["ok"] = not report["failures"]
    out = json.dumps(report, indent=1) + "\n"
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(out)
    print(f"record {report['record']!r} at {root}: present "
          f"{report['present']}/{report['declared']}, checksum ok "
          f"{report['checksum_ok']}/{report['declared']}, undeclared "
          f"{len(extras)}")
    for f in report["failures"]:
        print("FAIL", json.dumps(f))
    if report["ok"] and args.stamp:
        stamp = {"record": report["record"], "manifest_sha256": msha,
                 "verified_utc": report["verified_utc"],
                 "report_sha256": hashlib.sha256(out.encode()).hexdigest(),
                 "files": report["declared"]}
        (root / "RECORD.json").write_text(json.dumps(stamp, indent=1) + "\n")
        print(f"stamped {root / 'RECORD.json'}")
    return 0 if report["ok"] else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build")
    b.add_argument("--data-root", type=Path, required=True)
    b.add_argument("--out", type=Path, required=True)
    b.add_argument("--record", help="record name if SOURCE.json has none")
    b.add_argument("--version", help="refuse unless the files say this")
    b.add_argument("--doi", help="refuse unless the files say this")
    v = sub.add_parser("verify")
    v.add_argument("--manifest", type=Path, required=True)
    v.add_argument("--data-root", type=Path, required=True)
    v.add_argument("--report", type=Path)
    v.add_argument("--stamp", action="store_true")
    args = ap.parse_args()
    return build(args) if args.cmd == "build" else verify(args)


if __name__ == "__main__":
    sys.exit(main())
