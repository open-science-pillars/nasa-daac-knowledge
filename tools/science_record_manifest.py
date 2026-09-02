# /// script
# requires-python = ">=3.10"
# dependencies = ["earthaccess"]
# ///
"""Generate a data-tree manifest: every granule with its size, the
archive's checksum, and its download URL. A manifest is the citable
statement of exactly what a tree holds; the fetch tool downloads FROM
a manifest, never from a fresh search, so what was declared is what
is fetched, and the verify tool checks a tree AGAINST its manifest.

Two ways to build one:
  declared   (default) the full 1992-2017 record of the core
             collections, enumerated from CMR. The science record.
  --from-tree ROOT
             the granules already in a tree, each matched to its CMR
             record for the checksum. The pinned fixture cache is
             built this way, so the manifest states what the fixtures
             ARE and CMR vouches for every byte of them. An on-disk
             file with no CMR match is an error, not a silent gap.

Both include the grid geometry granule (computations read it from
geometry/ under the root; CMR publishes no checksum for it, so with
--data-root it is hashed locally and the manifest says so) and, when
--data-root holds one, the tutorial's geothermal flux file, which is
not a PO.DAAC product and is checksummed locally. CMR metadata
queries are anonymous; credentials are used for nothing here.
"""
import argparse
import datetime as dt
import hashlib
import json
import re
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore", category=FutureWarning,
                        message=".*DataGranule.size.*")
import earthaccess  # noqa: E402

MONTHLY = [
    "ECCO_L4_TEMP_SALINITY_LLC0090GRID_MONTHLY_V4R4",
    "ECCO_L4_DENS_STRAT_PRESS_LLC0090GRID_MONTHLY_V4R4",
    "ECCO_L4_SSH_LLC0090GRID_MONTHLY_V4R4",
    "ECCO_L4_OBP_LLC0090GRID_MONTHLY_V4R4",
    "ECCO_L4_OCEAN_VEL_LLC0090GRID_MONTHLY_V4R4",
    "ECCO_L4_OCEAN_3D_VOLUME_FLUX_LLC0090GRID_MONTHLY_V4R4",
    "ECCO_L4_OCEAN_3D_TEMPERATURE_FLUX_LLC0090GRID_MONTHLY_V4R4",
    "ECCO_L4_HEAT_FLUX_LLC0090GRID_MONTHLY_V4R4",
    "ECCO_L4_STRESS_LLC0090GRID_MONTHLY_V4R4",
]
SNAPSHOT = [
    "ECCO_L4_TEMP_SALINITY_LLC0090GRID_SNAPSHOT_V4R4",
    "ECCO_L4_SSH_LLC0090GRID_SNAPSHOT_V4R4",
]
GEOMETRY = "ECCO_L4_GEOMETRY_LLC0090GRID_V4R4"
SNAPSHOT_POLICY = (
    "month-boundary snapshots only, 311 per collection: the archive "
    "has no 1992-01-01 and no 2018-01-01 snapshot (verified against "
    "CMR 2026-09-01), so the budget-closable window is 1992-02 "
    "through 2017-11. Daily snapshots exist and are excluded by "
    "policy: the budget tendency needs bracketing month boundaries, "
    "not days")


def cmr_rows(short_name, temporal):
    rows = []
    for g in earthaccess.search_data(short_name=short_name,
                                     temporal=temporal):
        umm = g["umm"]
        url = next((u["URL"] for u in umm.get("RelatedUrls", [])
                    if u.get("Type") == "GET DATA"
                    and u["URL"].startswith("https")), None)
        # the URL basename is the definitive filename; GranuleUR is the
        # bare identifier without the extension
        name = url.rsplit("/", 1)[-1] if url else \
            umm.get("GranuleUR", "").split(":")[-1] + ".nc"
        csum = None
        for a in umm["DataGranule"].get(
                "ArchiveAndDistributionInformation", []):
            if "Checksum" in a:
                csum = {"algorithm": a["Checksum"]["Algorithm"],
                        "value": a["Checksum"]["Value"]}
                break
        assert name.endswith(".nc") and url, \
            f"unresolvable granule: {umm.get('GranuleUR')}"
        rows.append({"granule": name, "size_mb": float(g.size()),
                     "url": url, "checksum": csum})
    rows.sort(key=lambda r: r["granule"])
    return rows


def declared_rows(short_name):
    rows = cmr_rows(short_name, ("1992-01-01", "2018-01-02"))
    if short_name in SNAPSHOT:
        # day-01 at any hour: the record's first snapshot is at noon
        rows = [r for r in rows if "-01T" in r["granule"]]
    return rows


def tree_rows(root, short_name):
    """Rows for the files present under root/short_name, each matched
    to CMR over the window the filenames span."""
    names = sorted(p.name for p in (root / short_name).glob("*.nc"))
    if not names:
        return []
    dates = [re.search(r"_(\d{4}-\d{2}(?:-\d{2})?)", n).group(1)
             for n in names]
    lo, hi = min(dates), max(dates)
    lo = lo if len(lo) == 10 else lo + "-01"
    hi = (hi if len(hi) == 10 else hi + "-28")
    hi = (dt.date.fromisoformat(hi) + dt.timedelta(days=4)).isoformat()
    by_name = {r["granule"]: r for r in cmr_rows(short_name, (lo, hi))}
    missing = [n for n in names if n not in by_name]
    if missing:
        sys.exit(f"{short_name}: {len(missing)} on-disk files have no "
                 f"CMR record, first {missing[0]}; a manifest cannot "
                 f"vouch for them")
    return [by_name[n] for n in names]


def local_checksum(path):
    return {"algorithm": "SHA-256", "source": "local",
            "value": hashlib.sha256(path.read_bytes()).hexdigest()}


def geometry_rows(root):
    rows = cmr_rows(GEOMETRY, None)
    keep = [r for r in rows if r["granule"].startswith("GRID_GEOMETRY")]
    assert len(keep) == 1, [r["granule"] for r in rows]
    row = keep[0]
    row["path"] = f"geometry/{row['granule']}"
    if root is not None:
        if not (root / row["path"]).exists():
            sys.exit(f"geometry granule absent from {root}")
        if not row["checksum"]:
            row["checksum"] = local_checksum(root / row["path"])
            row["checksum_note"] = ("CMR publishes no checksum for this "
                                    "granule; hashed locally")
    return keep


def geothermal_row(path):
    return {"granule": path.name, "path": path.name,
            "size_mb": path.stat().st_size / 1048576, "url": None,
            "origin": "ECCO tutorial distribution (geothermalFlux.bin); "
                      "not a PO.DAAC collection; checksummed locally",
            "checksum": local_checksum(path)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--record", default="ecco-v4r4-science-record",
                    help="the record's name; receipts carry it")
    ap.add_argument("--from-tree", type=Path,
                    help="manifest the granules present in this tree")
    ap.add_argument("--data-root", type=Path,
                    help="tree holding the locally checksummed inputs "
                         "(geometry, geothermalFlux.bin); implied by "
                         "--from-tree")
    args = ap.parse_args()
    root = args.from_tree.expanduser().resolve() if args.from_tree else None
    local = root or (args.data_root.expanduser().resolve()
                     if args.data_root else None)
    manifest = {"record": args.record,
                "generated_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
                "derived_from": f"tree {root}" if root else
                                "CMR, 1992-01 through 2017-12",
                "collections": {}}
    if root:
        names = sorted(p.name for p in root.glob("ECCO_L4_*")
                       if p.is_dir() and p.name != GEOMETRY
                       and any(p.glob("*.nc")))
        plan = [(sn, tree_rows(root, sn)) for sn in names]
    else:
        manifest["temporal"] = ["1992-01", "2017-12"]
        manifest["snapshot_policy"] = SNAPSHOT_POLICY
        plan = [(sn, declared_rows(sn)) for sn in MONTHLY + SNAPSHOT]
    plan.append((GEOMETRY, geometry_rows(local)))
    if local and (local / "geothermalFlux.bin").exists():
        plan.append(("tutorial-distribution",
                     [geothermal_row(local / "geothermalFlux.bin")]))
    total = 0.0
    for sn, rows in plan:
        sz = sum(r["size_mb"] for r in rows)
        total += sz
        with_cs = sum(1 for r in rows if r["checksum"])
        manifest["collections"][sn] = {
            "granules": len(rows), "size_mb": round(sz, 1),
            "with_checksum": with_cs, "files": rows}
        print(f"{sn:60s} {len(rows):4d} granules {sz/1024:7.2f} GB "
              f"({with_cs} with checksums)")
    manifest["total_gb"] = round(total / 1024, 2)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(manifest, indent=1) + "\n")
    print(f"TOTAL {manifest['total_gb']} GB -> {args.out}")


if __name__ == "__main__":
    main()
