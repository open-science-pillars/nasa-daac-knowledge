#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml"]
# ///
"""Check ECCO fields concepts against the family manifest and the OSP
fields-layer rules. Runs offline; pair with check_okf_v02.py (generic OKF
v0.2 conformance) and verify_cmr.py (live ground truth). Errors fail the
gate; warnings are review flags. Exit 1 on errors, or warnings with --strict.

ERRORS
  F1  type is not `Data Collection`
  F2  resource is not a podaac.jpl.nasa.gov/dataset/<ShortName> URL for a
      ShortName the concept claims
  F3  no `# Schema` table with at least one variable row
  F4  Variants names a ShortName the manifest does not know
  F5  a ShortName is claimed by more than one concept
  F6  concept slug not in the manifest (unknown family)

WARNINGS
  F7  Schema variable not in the manifest for this family (NEW: needs
      granule verification and a manifest update in the same PR)
  F8  manifest variable missing from the Schema table (incomplete)
  F9  status stable without a human: verified event (promotion ladder:
      stable requires human-reviewed; see fields-authoring doc)
  F10 manifest family has no concept yet (coverage meter)
  F11 no sources entry pointing at the PO.DAAC landing page or CMR
  F12 Variants missing the harvested DOI for a claimed ShortName (fires
      only once tools/ecco_v4r4_dois.yaml exists; DOIs are harvested by
      tools/ecco_cite.py, never hand-typed)

Usage: check_fields.py FIELDS_DIR data/ecco_v4r4_families.yaml [--strict]
"""

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("pyyaml required: python3 -m pip install pyyaml", file=sys.stderr)
    sys.exit(2)

SN_RE = re.compile(r"^https://podaac\.jpl\.nasa\.gov/dataset/(ECCO_L4_[A-Z0-9_]+)$")


def split_frontmatter(text: str):
    if not text.startswith("---"):
        return None, text
    lines = text.split("\n")
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[1:i]), "\n".join(lines[i + 1:])
    return None, text


def schema_vars(body: str) -> list:
    """Backticked names in the first column of the table under # Schema."""
    m = re.search(r"^#\s+Schema\s*$(.*?)(?=^#\s|\Z)", body, re.M | re.S)
    if not m:
        return []
    out = []
    for line in m.group(1).split("\n"):
        cell = re.match(r"^\|\s*`([A-Za-z0-9_]+)`\s*\|", line)
        if cell:
            out.append(cell.group(1))
    return out


def human_reviewed(fm: dict) -> bool:
    ver = fm.get("verified")
    events = ver if isinstance(ver, list) else [ver] if ver else []
    return any(isinstance(e, dict) and str(e.get("by", "")).startswith("human:")
               for e in events)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("fields_dir", type=Path)
    ap.add_argument("manifest", type=Path)
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--dois", type=Path, default=None,
                    help="shortname-to-DOI mapping (default: "
                         "<manifest dir>/ecco_v4r4_dois.yaml when present)")
    args = ap.parse_args()

    manifest = yaml.safe_load(args.manifest.read_text(encoding="utf-8"))
    dois_path = args.dois or (args.manifest.parent / "ecco_v4r4_dois.yaml")
    dois = {}
    if dois_path.exists():
        dois = (yaml.safe_load(dois_path.read_text(encoding="utf-8")) or {}).get("dois", {})
    fam_by_slug = {f["slug"]: f for f in manifest["families"]}
    known_sns = {sn: f["slug"] for f in manifest["families"] for sn in f["shortnames"]}

    out, claims, covered = [], {}, set()
    for path in sorted(args.fields_dir.glob("*.md")):
        if path.name in ("index.md", "log.md"):
            continue
        slug = path.stem
        text = path.read_text(encoding="utf-8")
        raw_fm, body = split_frontmatter(text)
        fm = (yaml.safe_load(raw_fm) or {}) if raw_fm else {}

        fam = fam_by_slug.get(slug)
        if fam is None:
            out.append(("F6", path, "slug not in the manifest; add the family "
                        "there first (single source of truth)"))
            continue
        covered.add(slug)

        if fm.get("type") != "Data Collection":
            out.append(("F1", path, f"type is '{fm.get('type')}', expected Data Collection"))

        concept_sns = set(re.findall(r"`(ECCO_L4_[A-Z0-9_]+)`", text))
        res = str(fm.get("resource") or "")
        rm = SN_RE.match(res)
        if not rm or rm.group(1) not in concept_sns:
            out.append(("F2", path, f"resource '{res}' is not a PO.DAAC landing "
                        "URL for a claimed ShortName"))

        for sn in sorted(concept_sns):
            if sn not in known_sns:
                out.append(("F4", path, f"ShortName {sn} unknown to the manifest"))
            elif known_sns[sn] != slug:
                out.append(("F4", path, f"ShortName {sn} belongs to family "
                            f"'{known_sns[sn]}' per the manifest"))
            if sn in claims and claims[sn] != path:
                out.append(("F5", path, f"{sn} also claimed by {claims[sn].name}"))
            claims[sn] = path

        svars = schema_vars(body)
        if not svars:
            out.append(("F3", path, "no # Schema table with variable rows"))
        mvars = {v["name"] for v in fam.get("variables", [])}
        for v in sorted(set(svars) - mvars):
            out.append(("F7", path, f"variable `{v}` not in manifest: granule-verify "
                        "and update the manifest in this PR"))
        for v in sorted(mvars - set(svars)):
            out.append(("F8", path, f"manifest variable `{v}` missing from Schema"))

        if fm.get("status") == "stable" and not human_reviewed(fm):
            out.append(("F9", path, "stable without a human: verified event; "
                        "the steward signs promotion"))

        sources = fm.get("sources") or []
        res_urls = " ".join(str(e.get("resource", "")) for e in sources
                            if isinstance(e, dict))
        if "podaac.jpl.nasa.gov" not in res_urls and "cmr.earthdata" not in res_urls:
            out.append(("F11", path, "no sources entry for the PO.DAAC landing "
                        "page or the CMR sweep"))

        for sn in sorted(concept_sns & set(dois)):
            doi = str((dois[sn] or {}).get("doi", ""))
            if doi and doi not in text:
                out.append(("F12", path, f"Variants missing harvested DOI "
                            f"{doi} for {sn}"))

    for slug in sorted(set(fam_by_slug) - covered):
        out.append(("F10", args.fields_dir / f"{slug}.md", "family not yet authored"))

    errors = [x for x in out if x[0] in {"F1", "F2", "F3", "F4", "F5", "F6"}]
    warns = [x for x in out if x[0] not in {"F1", "F2", "F3", "F4", "F5", "F6"}]
    for code, path, msg in errors + warns:
        print(f"{code:<4} {path}: {msg}")
    print(f"\ncoverage: {len(covered)}/{len(fam_by_slug)} families authored; "
          f"{len(claims)}/{len(known_sns)} ShortNames claimed")
    print(f"errors: {len(errors)}  warnings: {len(warns)}")
    if errors or (args.strict and warns):
        return 1
    if len(covered) == len(fam_by_slug) and not warns:
        print("fields layer complete: every family authored, every ShortName "
              "claimed once, all Schemas reconciled with the manifest")
    return 0


if __name__ == "__main__":
    sys.exit(main())
