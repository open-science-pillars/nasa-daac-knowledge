#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml"]
# ///
"""release_delta: reconcile a new ECCO release's CMR sweep against the
V4r4 family manifest and draft the day-one migration artifacts.

Pairs collections across releases by stem (the ShortName with its release
token removed), then reports three sets: CONTINUED (stem present in both
releases), NEW (no prior-release counterpart: candidate new family or new
variant), DISCONTINUED (prior-release stem with no successor). With
--draft-dir it writes: the delta report, a v<new> manifest skeleton
(families carried over with successor ShortNames, provenance reset to
release-pending), and a migration-gotcha stub for steward review.

Inputs: the v4r4 manifest, and either --sweep-file (one ShortName per
line, e.g. saved from verify_cmr.py --sweep output) or --live (query CMR
for ECCO_L4_*<TOKEN>* directly).

Usage:
  release_delta.py data/ecco_v4r4_families.yaml --new-token V4R5 \
      (--sweep-file v4r5_names.txt | --live) [--draft-dir out/]
  release_delta.py ... --selftest
"""

import argparse
import datetime
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

try:
    import yaml
except ImportError:
    print("pyyaml required", file=sys.stderr)
    sys.exit(2)

CMR = "https://cmr.earthdata.nasa.gov/search/collections.json"

SELFTEST_OLD = [
    "ECCO_L4_TEMP_SALINITY_LLC0090GRID_MONTHLY_V4R4",
    "ECCO_L4_TEMP_SALINITY_LLC0090GRID_SNAPSHOT_V4R4",
    "ECCO_L4_OBP_LLC0090GRID_MONTHLY_V4R4B",
    "ECCO_L4_GMSL_TIME_SERIES_MONTHLY_V4R4",
]
SELFTEST_NEW = [
    "ECCO_L4_TEMP_SALINITY_LLC0090GRID_MONTHLY_V4R5",
    "ECCO_L4_TEMP_SALINITY_LLC0090GRID_SNAPSHOT_V4R5",
    "ECCO_L4_OBP_LLC0090GRID_MONTHLY_V4R5",
    "ECCO_L4_SEA_LEVEL_COMPONENTS_LLC0090GRID_MONTHLY_V4R5",
]


def stem(shortname: str, tokens: tuple) -> str:
    s = shortname
    for t in tokens:
        s = re.sub(rf"_{t}B?$", "", s)
    return s


def live_sweep(token: str) -> list:
    params = {"short_name": f"ECCO_L4_*{token}*",
              "options[short_name][pattern]": "true",
              "provider": "POCLOUD", "page_size": 500}
    req = urllib.request.Request(CMR + "?" + urllib.parse.urlencode(params),
                                 headers={"User-Agent": "osp-release-delta/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        payload = json.loads(r.read().decode("utf-8"))
    return sorted({e.get("short_name", "")
                   for e in payload.get("feed", {}).get("entry", [])} - {""})


def reconcile(old_names, new_names, old_token, new_token):
    old_by_stem, new_by_stem = {}, {}
    for n in old_names:
        old_by_stem.setdefault(stem(n, (old_token,)), []).append(n)
    for n in new_names:
        new_by_stem.setdefault(stem(n, (new_token,)), []).append(n)
    continued = sorted(set(old_by_stem) & set(new_by_stem))
    new = sorted(set(new_by_stem) - set(old_by_stem))
    discontinued = sorted(set(old_by_stem) - set(new_by_stem))
    return continued, new, discontinued, old_by_stem, new_by_stem


def draft(outdir: Path, manifest: dict, continued, new, discontinued,
          new_by_stem, old_token, new_token):
    outdir.mkdir(parents=True, exist_ok=True)
    today = datetime.date.today().isoformat()

    lines = [f"# {new_token} release delta (generated {today})", "",
             f"Continued stems: {len(continued)}; new: {len(new)}; "
             f"discontinued: {len(discontinued)}", ""]
    if new:
        lines += ["## New in this release (assign to a family or create one)",
                  *(f"- {sn}" for s in new for sn in new_by_stem[s]), ""]
    if discontinued:
        lines += [f"## No {new_token} successor found (verify before deprecating)",
                  *(f"- {s}_{old_token}*" for s in discontinued), ""]
    (outdir / f"delta-{new_token.lower()}.md").write_text("\n".join(lines) + "\n",
                                                          encoding="utf-8")

    skel = {"meta": {"product": f"ECCO {new_token} (skeleton generated {today}; "
                     "verify period, grids, variables at release)",
                     "derived_from": "ecco_v4r4_families.yaml"},
            "families": []}
    for fam in manifest.get("families", []):
        sns = []
        for sn in fam.get("shortnames", []):
            st = stem(sn, (old_token,))
            sns += [n for n in new_by_stem.get(st, [])]
        if sns:
            skel["families"].append({
                "slug": fam["slug"], "title": fam["title"],
                "tags": fam.get("tags", []),
                "primary": sorted(sns)[0],
                "shortnames": sorted(set(sns)),
                "variables": [],
                "note": "release-pending; granule-verify variables and confirm "
                        "period before authoring",
            })
    (outdir / f"ecco_{new_token.lower()}_families.skeleton.yaml").write_text(
        yaml.safe_dump(skel, sort_keys=False), encoding="utf-8")

    gotcha = f"""---
type: gotcha
title: {old_token} to {new_token} migration
description: What changes between releases and where mixing them silently misleads.
tags: [ecco, releases]
status: draft
severity: high
generated: {{ by: release-delta/{new_token.lower()}, at: {today}T00:00:00Z }}
sources:
  - id: delta-report
    resource: delta-{new_token.lower()}.md (this sweep)
    title: Generated release delta
---

# {old_token} to {new_token} migration

STUB for steward completion at release: the period extension, any renamed
or restructured collections, baseline changes affecting trends, and the
rule for mixing releases in one analysis. Continued: {len(continued)}
stems; new: {len(new)}; discontinued: {len(discontinued)}.
"""
    (outdir / f"gotcha-{new_token.lower()}-migration.stub.md").write_text(
        gotcha, encoding="utf-8")
    print(f"drafted: delta report, manifest skeleton "
          f"({len(skel['families'])} families carried), migration-gotcha stub -> {outdir}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("manifest", type=Path)
    ap.add_argument("--new-token", default="V4R5")
    ap.add_argument("--old-token", default="V4R4")
    ap.add_argument("--sweep-file", type=Path)
    ap.add_argument("--live", action="store_true")
    ap.add_argument("--draft-dir", type=Path)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    manifest = yaml.safe_load(args.manifest.read_text(encoding="utf-8"))
    old_names = [sn for f in manifest.get("families", [])
                 for sn in f.get("shortnames", [])]

    if args.selftest:
        c, n, d, _, nbs = reconcile(SELFTEST_OLD, SELFTEST_NEW, "V4R4", "V4R5")
        ok = (len(c) == 3 and n == ["ECCO_L4_SEA_LEVEL_COMPONENTS_LLC0090GRID_MONTHLY"]
              and d == ["ECCO_L4_GMSL_TIME_SERIES_MONTHLY"])
        print(f"selftest: continued={len(c)} new={n} discontinued={d}")
        print("selftest:", "PASS" if ok else "FAIL")
        return 0 if ok else 1

    if args.sweep_file:
        new_names = [ln.strip() for ln in args.sweep_file.read_text().split("\n")
                     if ln.strip()]
    elif args.live:
        new_names = live_sweep(args.new_token)
    else:
        print("need --sweep-file, --live, or --selftest", file=sys.stderr)
        return 2

    c, n, d, _, nbs = reconcile(old_names, new_names, args.old_token, args.new_token)
    print(f"{args.new_token}: {len(new_names)} collections; continued stems {len(c)}, "
          f"new {len(n)}, discontinued {len(d)}")
    for s in n:
        print(f"NEW           {', '.join(nbs[s])}")
    for s in d:
        print(f"DISCONTINUED  {s}_{args.old_token}*")
    if args.draft_dir:
        draft(args.draft_dir, manifest, c, n, d, nbs, args.old_token, args.new_token)
    return 0


if __name__ == "__main__":
    sys.exit(main())
