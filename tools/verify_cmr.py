#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml"]
# ///
"""Verify ECCO ShortNames against NASA's Common Metadata Repository (CMR)
and reconcile the family manifest against the live collection sweep.

Three modes, combinable:

  --names       verify every ShortName in the manifest exists in CMR,
                exactly once (default mode when nothing else is given)
  --sweep       pull all ECCO_L4_*V4R4* collections from CMR (POCLOUD) and
                reconcile: names in CMR but unclaimed by any manifest
                family, and manifest names absent from CMR
  --sign DIR    for each fields concept in DIR whose Variants ShortNames
                all verified FOUND, append a verified event
                { by: process:cmr-shortname-sweep, at: <now> } to its
                frontmatter (OKF v0.2 spec 5.2, 7): the machine-confirmed
                rung of the promotion ladder. Line-surgical; skipped when
                the event already exists.

  --selftest    run the parser and reconciler against a bundled fixture,
                no network: proves the tooling without Earthdata access.

CMR collection search is public (no auth). Usage:
  verify_cmr.py data/ecco_v4r4_families.yaml [--sweep] [--sign knowledge/podaac/fields/ecco-v4r4]
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
    print("pyyaml required: python3 -m pip install pyyaml", file=sys.stderr)
    sys.exit(2)

CMR = "https://cmr.earthdata.nasa.gov/search/collections.json"
UA = {"User-Agent": "osp-ecco-fields-kit/1.0 (verify_cmr)"}

SELFTEST_FIXTURE = {
    "feed": {"entry": [
        {"short_name": "ECCO_L4_TEMP_SALINITY_LLC0090GRID_MONTHLY_V4R4"},
        {"short_name": "ECCO_L4_GEOMETRY_LLC0090GRID_V4R4"},
        {"short_name": "ECCO_L4_FAKE_NEW_COLLECTION_V4R4"},
    ]}
}


def cmr_get(params: dict) -> dict:
    url = CMR + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def entries(payload: dict) -> list:
    return payload.get("feed", {}).get("entry", []) or []


def load_manifest(path: Path):
    m = yaml.safe_load(path.read_text(encoding="utf-8"))
    claims = {}  # shortname -> family slug
    for fam in m.get("families", []):
        for sn in fam.get("shortnames", []):
            if sn in claims:
                print(f"MANIFEST ERROR: {sn} claimed by both "
                      f"'{claims[sn]}' and '{fam['slug']}'")
            claims[sn] = fam["slug"]
    return m, claims


def check_names(claims: dict) -> dict:
    """Return shortname -> FOUND | MISSING | AMBIGUOUS from per-name queries."""
    status = {}
    for sn in sorted(claims):
        try:
            hits = entries(cmr_get({"short_name": sn, "page_size": 2}))
        except Exception as e:
            status[sn] = f"ERROR ({e})"
            continue
        status[sn] = {0: "MISSING", 1: "FOUND"}.get(len(hits), "AMBIGUOUS")
        print(f"{status[sn]:<9} {sn}")
    return status


def sweep(claims: dict, payload: dict | None = None):
    if payload is None:
        payload = cmr_get({
            "short_name": "ECCO_L4_*V4R4*",
            "options[short_name][pattern]": "true",
            "provider": "POCLOUD",
            "page_size": 500,
        })
    cmr_names = {e.get("short_name", "") for e in entries(payload)} - {""}
    unclaimed = sorted(cmr_names - set(claims))
    absent = sorted(set(claims) - cmr_names)
    print(f"\nsweep: {len(cmr_names)} ECCO_L4_*V4R4* collections in CMR, "
          f"{len(claims)} claimed by the manifest")
    if unclaimed:
        print("IN CMR, UNCLAIMED BY ANY FAMILY (new or missed; assign or open an issue):")
        print("\n".join("  " + n for n in unclaimed))
    if absent:
        print("IN MANIFEST, ABSENT FROM CMR (typo or retired; fix the manifest):")
        print("\n".join("  " + n for n in absent))
    if not unclaimed and not absent:
        print("coverage complete: every CMR collection is claimed by exactly one family")
    return unclaimed, absent


def sign_concepts(fields_dir: Path, status: dict):
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    event = f"{{ by: process:cmr-shortname-sweep, at: {now} }}"
    for path in sorted(fields_dir.glob("*.md")):
        if path.name in ("index.md", "log.md"):
            continue
        text = path.read_text(encoding="utf-8")
        sns = set(re.findall(r"`(ECCO_L4_[A-Z0-9_]+)`", text))
        if not sns:
            print(f"SKIP  {path.name}: no ShortNames found")
            continue
        bad = sorted(sn for sn in sns if status.get(sn) != "FOUND")
        if bad:
            print(f"HOLD  {path.name}: not signing, unverified names: {', '.join(bad)}")
            continue
        if "process:cmr-shortname-sweep" in text:
            print(f"OK    {path.name}: already carries a sweep event")
            continue
        lines = text.split("\n")
        closing = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
        if closing is None or not text.startswith("---"):
            print(f"SKIP  {path.name}: no frontmatter")
            continue
        vi = next((i for i in range(closing) if re.match(r"^verified:", lines[i])), None)
        if vi is None:
            lines.insert(closing, f"verified: {event}")
        elif re.match(r"^verified:\s*\{", lines[vi]):
            existing = lines[vi].split(":", 1)[1].strip()
            lines[vi] = "verified:"
            lines.insert(vi + 1, f"  - {existing}")
            lines.insert(vi + 2, f"  - {event}")
        else:  # already a list: append after its last "  - " line
            j = vi + 1
            while j < closing and re.match(r"^\s+-\s", lines[j]):
                j += 1
            lines.insert(j, f"  - {event}")
        path.write_text("\n".join(lines), encoding="utf-8")
        print(f"SIGN  {path.name}: machine-confirmed ({len(sns)} names FOUND)")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("manifest", type=Path)
    ap.add_argument("--names", action="store_true")
    ap.add_argument("--sweep", action="store_true")
    ap.add_argument("--sign", type=Path, default=None, metavar="FIELDS_DIR")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    _, claims = load_manifest(args.manifest)

    if args.selftest:
        print("selftest: reconciling manifest against the bundled fixture "
              "(expect one UNCLAIMED fake, many ABSENT since the fixture is tiny)")
        unclaimed, absent = sweep(claims, payload=SELFTEST_FIXTURE)
        ok = ("ECCO_L4_FAKE_NEW_COLLECTION_V4R4" in unclaimed
              and "ECCO_L4_TEMP_SALINITY_LLC0090GRID_MONTHLY_V4R4" not in absent)
        print("selftest:", "PASS" if ok else "FAIL")
        return 0 if ok else 1

    status = {}
    if args.names or not (args.sweep or args.sign):
        status = check_names(claims)
    if args.sweep:
        sweep(claims)
    if args.sign:
        if not status:
            status = check_names(claims)
        sign_concepts(args.sign, status)

    missing = [k for k, v in status.items() if v != "FOUND"]
    if missing:
        print(f"\n{len(missing)} name(s) not cleanly FOUND")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
