# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Verify a data tree against its manifest, and stamp the tree.

Three checks, each reported per collection and in total:
  presence   every manifest row is a file in the tree
  size       bytes match the manifest size (the archive's catalog
             sizes are approximate at the 1e-5 level; the bar here
             is 1e-3, and the checksum is the real integrity check)
  checksum   the file hashes to the manifest checksum, using the
             manifest's own algorithm (the archive publishes SHA-512)
and, with --exact, a fourth: the tree holds nothing the manifest does
not declare (the property a pinned fixture cache must keep).

Coverage is derived from the granule names: months present, months
missing inside the span, and per budget the window over which its
tendency can be closed: every monthly input present for month m AND
both snapshot inputs at the start of m and of m+1. The input lists
mirror the attested regional budget executor.

On success the tree is stamped with RECORD.json: the manifest's
name and sha256, the verification time, and the report's sha256.
Sanctioned computations copy that stamp into their receipts, so a
receipt says which tree fed it and that the tree was verified.
Stdlib only; credentials are used for nothing here.
"""
import argparse
import datetime as dt
import hashlib
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

SIZE_BAR = 1e-3
BUDGET_INPUTS = {   # mirrors ecco_regional_budget.py
    "heat": (["ECCO_L4_OCEAN_3D_TEMPERATURE_FLUX_LLC0090GRID_MONTHLY_V4R4",
              "ECCO_L4_HEAT_FLUX_LLC0090GRID_MONTHLY_V4R4"],
             ["ECCO_L4_TEMP_SALINITY_LLC0090GRID_SNAPSHOT_V4R4",
              "ECCO_L4_SSH_LLC0090GRID_SNAPSHOT_V4R4"]),
    "salt": (["ECCO_L4_OCEAN_3D_SALINITY_FLUX_LLC0090GRID_MONTHLY_V4R4",
              "ECCO_L4_FRESH_FLUX_LLC0090GRID_MONTHLY_V4R4"],
             ["ECCO_L4_TEMP_SALINITY_LLC0090GRID_SNAPSHOT_V4R4",
              "ECCO_L4_SSH_LLC0090GRID_SNAPSHOT_V4R4"]),
    "volume": (["ECCO_L4_OCEAN_3D_VOLUME_FLUX_LLC0090GRID_MONTHLY_V4R4"],
               ["ECCO_L4_TEMP_SALINITY_LLC0090GRID_SNAPSHOT_V4R4",
                "ECCO_L4_SSH_LLC0090GRID_SNAPSHOT_V4R4"]),
}
EXTRAS_OK = {"RECORD.json", "fetch.log", "manifest_rebuild.log"}


def row_path(root, short_name, row):
    return root / row.get("path", f"{short_name}/{row['granule']}")


def digest(path, algorithm):
    h = hashlib.new(algorithm.lower().replace("-", ""))
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 22), b""):
            h.update(chunk)
    return h.hexdigest().lower()


def month_of(name):
    m = re.search(r"_(\d{4}-\d{2})(?:-\d{2}T\d{6})?_ECCO", name)
    return m.group(1) if m else None


def months_between(a, b):
    y, m = map(int, a.split("-"))
    out = []
    while f"{y:04d}-{m:02d}" <= b:
        out.append(f"{y:04d}-{m:02d}")
        m += 1
        if m == 13:
            y, m = y + 1, 1
    return out


def next_month(ym):
    y, m = map(int, ym.split("-"))
    return f"{y + 1:04d}-01" if m == 12 else f"{y:04d}-{m + 1:02d}"


def coverage(manifest):
    cov = {}
    for sn, coll in manifest["collections"].items():
        months = sorted({mm for mm in (month_of(r["granule"])
                                       for r in coll["files"]) if mm})
        if not months:
            cov[sn] = {"granules": len(coll["files"]), "dated": 0}
            continue
        span = months_between(months[0], months[-1])
        cov[sn] = {"granules": len(coll["files"]), "first": months[0],
                   "last": months[-1], "months": len(months),
                   "missing_inside_span": sorted(set(span) - set(months))}
    have = {sn: {month_of(r["granule"]) for r in coll["files"]}
            for sn, coll in manifest["collections"].items()}
    windows = {}
    for budget, (monthly, snaps) in BUDGET_INPUTS.items():
        absent = [sn for sn in monthly + snaps if sn not in have]
        if absent:
            windows[budget] = {"months": 0, "absent_collections": absent}
            continue
        months = sorted(set.intersection(*(have[sn] for sn in monthly)))
        closable = [m for m in months
                    if all(m in have[sn] and next_month(m) in have[sn]
                           for sn in snaps)]
        windows[budget] = ({"first": closable[0], "last": closable[-1],
                            "months": len(closable)} if closable
                           else {"months": 0})
    cov["budget_closable_windows"] = {
        "rule": "every monthly input present for the month and both "
                "snapshot inputs at its start and at the start of the "
                "next month; inputs mirror the regional budget executor",
        **windows}
    return cov


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--data-root", type=Path, required=True)
    ap.add_argument("--checksum", default="all",
                    help="all | none | a substring of collection names "
                         "(comma-separated) to restrict hashing")
    ap.add_argument("--exact", action="store_true",
                    help="fail if the tree holds files the manifest "
                         "does not declare")
    ap.add_argument("--report", type=Path, help="write the report here")
    ap.add_argument("--stamp", action="store_true",
                    help="write RECORD.json into the tree on success")
    ap.add_argument("--jobs", type=int, default=4)
    args = ap.parse_args()
    root = args.data_root.expanduser().resolve()
    mbytes = args.manifest.read_bytes()
    manifest = json.loads(mbytes)
    manifest_sha = hashlib.sha256(mbytes).hexdigest()
    want_ck = (lambda sn: True) if args.checksum == "all" else \
              (lambda sn: False) if args.checksum == "none" else \
              (lambda sn: any(s in sn for s in args.checksum.split(",")))

    report = {"verified_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
              "manifest": str(args.manifest), "manifest_sha256": manifest_sha,
              "record": manifest.get("record"), "data_root": str(root),
              "tool_sha256": hashlib.sha256(
                  Path(__file__).read_bytes()).hexdigest(),
              "collections": {}, "failures": []}
    declared = set()
    to_hash = []
    for sn, coll in manifest["collections"].items():
        c = {"declared": len(coll["files"]), "present": 0, "size_ok": 0,
             "size_max_rel_dev": 0.0, "checksum_planned": 0}
        for row in coll["files"]:
            p = row_path(root, sn, row)
            declared.add(p)
            if not p.exists():
                report["failures"].append({"collection": sn, "granule":
                                           row["granule"], "check": "presence"})
                continue
            c["present"] += 1
            want = row["size_mb"] * 1048576
            dev = abs(p.stat().st_size - want) / want if want else 1.0
            c["size_max_rel_dev"] = max(c["size_max_rel_dev"], dev)
            if dev <= SIZE_BAR:
                c["size_ok"] += 1
            else:
                report["failures"].append({"collection": sn, "granule":
                                           row["granule"], "check": "size",
                                           "rel_dev": dev})
            if row.get("checksum") and want_ck(sn):
                to_hash.append((sn, row, p))
                c["checksum_planned"] += 1
        report["collections"][sn] = c

    def check(item):
        sn, row, p = item
        got = digest(p, row["checksum"]["algorithm"])
        return sn, row, got == row["checksum"]["value"].lower()
    algos = sorted({r["checksum"]["algorithm"] for _, r, _ in to_hash})
    with ThreadPoolExecutor(args.jobs) as ex:
        for sn, row, ok in ex.map(check, to_hash):
            c = report["collections"][sn]
            c["checksum_ok"] = c.get("checksum_ok", 0) + int(ok)
            if not ok:
                report["failures"].append({"collection": sn, "granule":
                                           row["granule"], "check": "checksum"})
    report["checksum"] = {"algorithms": algos, "hashed": len(to_hash),
                          "ok": sum(c.get("checksum_ok", 0)
                                    for c in report["collections"].values())}

    extras = sorted(str(p.relative_to(root)) for p in root.rglob("*")
                    if p.is_file() and p not in declared
                    and p.name not in EXTRAS_OK)
    report["undeclared_files"] = extras
    if args.exact and extras:
        report["failures"].append({"check": "exact", "undeclared": extras})
    report["coverage"] = coverage(manifest)
    report["ok"] = not report["failures"]

    out = json.dumps(report, indent=1) + "\n"
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(out)
    tot = {k: sum(c[k] for c in report["collections"].values())
           for k in ("declared", "present", "size_ok")}
    print(f"record {report['record']!r} at {root}")
    print(f"present {tot['present']}/{tot['declared']}, size ok "
          f"{tot['size_ok']}, checksum ok {report['checksum']['ok']}/"
          f"{report['checksum']['hashed']} ({','.join(algos) or 'none'}), "
          f"undeclared files {len(extras)}")
    for c, v in report["coverage"].items():
        if c == "budget_closable_windows":
            for b, w in v.items():
                if b != "rule":
                    print(f"  {b} budget closable: {w}")
        elif "first" in v:
            gap = v["missing_inside_span"]
            print(f"  {c}: {v['first']}..{v['last']} {v['months']} months"
                  f"{', MISSING ' + ','.join(gap) if gap else ''}")
    for f in report["failures"][:20]:
        print("FAIL", json.dumps(f))
    if report["ok"] and args.stamp:
        stamp = {"record": report["record"], "manifest_sha256": manifest_sha,
                 "verified_utc": report["verified_utc"],
                 "report_sha256": hashlib.sha256(out.encode()).hexdigest(),
                 "granules": tot["declared"]}
        (root / "RECORD.json").write_text(json.dumps(stamp, indent=1) + "\n")
        print(f"stamped {root / 'RECORD.json'}")
    print("VERIFIED" if report["ok"] else f"FAILED ({len(report['failures'])})")
    sys.exit(0 if report["ok"] else 1)


if __name__ == "__main__":
    main()
