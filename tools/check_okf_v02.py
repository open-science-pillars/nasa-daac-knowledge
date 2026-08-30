#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml"]
# ///
"""OKF v0.2 conformance checker for OSP knowledge bundles.

Checks a bundle directory against OKF v0.2 (GoogleCloudPlatform/
knowledge-catalog, okf/SPEC.md) plus the OSP conventions layered on it.
Errors are conformance failures (spec 11); warnings are spec SHOULDs and
OSP house rules. Exit 1 on any error, or on warnings too with --strict.

ERRORS (spec 11 conformance)
  E1  concept has no parseable YAML frontmatter
  E2  frontmatter missing a non-empty `type`
  E3  `generated` present but malformed (needs mapping with `by`)
  E4  `verified` present but malformed (mapping or list of {by, at})
  E5  `status` outside draft | stable | deprecated
  E6  `stale_after` not YYYY-MM-DD
  E7  `sources` entry missing `resource`
  E8  actor value violates the convention (spec 7)
  E9  non-root index.md carries frontmatter (spec 8, 12)

WARNINGS (SHOULDs and OSP rules)
  W1  body footnote ref has no matching sources id (spec 5.1 join)
  W2  sources id never referenced by a body footnote
  W3  root index.md missing okf_version
  W4  concept unverified or machine-confirmed only (tier report)
  W5  stale: today >= stale_after (spec 5.5)
  W6  log.md date heading not ISO YYYY-MM-DD (spec 9)
  W7  legacy v0.1/v0.6 key present (timestamp, verified_by, evidence,
      or a v0.6 status value): migration incomplete

Usage: check_okf_v02.py BUNDLE_DIR [--strict]
"""

import argparse
import datetime
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("pyyaml required: python3 -m pip install pyyaml", file=sys.stderr)
    sys.exit(2)

ACTOR_RE = re.compile(r"^(human:|process:|team:)\S+$|^[\w.-]+/[\w.@-]+$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
STATUSES = {"draft", "stable", "deprecated"}
LEGACY_STATUSES = {"verified", "stale", "superseded", "disputed"}
FOOT_REF = re.compile(r"\[\^([\w-]+)\](?!:)")
FOOT_DEF = re.compile(r"^\[\^([\w-]+)\]:", re.M)


def split_frontmatter(text: str):
    if not text.startswith("---"):
        return None, text
    lines = text.split("\n")
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[1:i]), "\n".join(lines[i + 1:])
    return None, text


def check_actor(value, where, out, path):
    if not isinstance(value, str) or not ACTOR_RE.match(value):
        out.append(("E8", path, f"{where}: '{value}' violates the actor convention"))


def tier(verified) -> str:
    events = verified if isinstance(verified, list) else [verified] if verified else []
    bys = [e.get("by", "") for e in events if isinstance(e, dict)]
    if any(isinstance(b, str) and b.startswith("human:") for b in bys):
        return "human-reviewed"
    return "machine-confirmed" if bys else "unverified"


def check_concept(path: Path, out: list, tiers: dict):
    text = path.read_text(encoding="utf-8")
    raw_fm, body = split_frontmatter(text)
    if raw_fm is None:
        out.append(("E1", path, "no frontmatter block"))
        return
    try:
        fm = yaml.safe_load(raw_fm) or {}
    except yaml.YAMLError as e:
        out.append(("E1", path, f"frontmatter does not parse: {e}"))
        return
    if not isinstance(fm, dict):
        out.append(("E1", path, "frontmatter is not a mapping"))
        return

    if not str(fm.get("type") or "").strip():
        out.append(("E2", path, "missing non-empty `type` (the one required key)"))

    for legacy in ("timestamp", "verified_by", "evidence"):
        if legacy in fm:
            out.append(("W7", path, f"legacy key `{legacy}` present: migration incomplete"))

    gen = fm.get("generated")
    if gen is not None:
        if not isinstance(gen, dict) or "by" not in gen:
            out.append(("E3", path, "`generated` must be a mapping with `by`"))
        else:
            check_actor(gen["by"], "generated.by", out, path)

    ver = fm.get("verified")
    if ver is not None:
        events = ver if isinstance(ver, list) else [ver]
        for e in events:
            if not isinstance(e, dict) or "by" not in e or "at" not in e:
                out.append(("E4", path, "`verified` events need `by` and `at`"))
            else:
                check_actor(e["by"], "verified.by", out, path)
    t = tier(ver)
    tiers[t] = tiers.get(t, 0) + 1
    if t != "human-reviewed":
        out.append(("W4", path, f"trust tier: {t}"))

    status = fm.get("status")
    if status is not None and status not in STATUSES:
        code = "W7" if status in LEGACY_STATUSES else "E5"
        out.append((code, path, f"status '{status}' outside draft|stable|deprecated"))

    sa = fm.get("stale_after")
    if sa is not None:
        s = sa.isoformat() if isinstance(sa, datetime.date) else str(sa)
        if not DATE_RE.match(s):
            out.append(("E6", path, f"stale_after '{sa}' is not YYYY-MM-DD"))
        elif datetime.date.today().isoformat() >= s:
            out.append(("W5", path, f"stale since {s}"))

    src_ids = set()
    sources = fm.get("sources")
    if sources is not None:
        for entry in sources if isinstance(sources, list) else []:
            if not isinstance(entry, dict) or "resource" not in entry:
                out.append(("E7", path, "sources entry missing `resource`"))
            elif "id" in entry:
                src_ids.add(str(entry["id"]))
            if isinstance(entry, dict) and "author" in entry:
                check_actor(entry["author"], "sources[].author", out, path)

    refs = set(FOOT_REF.findall(body)) | set(FOOT_DEF.findall(body))
    for r in sorted(refs - src_ids):
        if sources is not None:
            out.append(("W1", path, f"footnote [^{r}] has no matching sources id"))
    for s in sorted(src_ids - refs):
        out.append(("W2", path, f"sources id '{s}' never cited by a footnote"))


def check_index(path: Path, is_root: bool, out: list):
    text = path.read_text(encoding="utf-8")
    raw_fm, _ = split_frontmatter(text)
    if is_root:
        if raw_fm is None:
            out.append(("W3", path, 'root index missing okf_version: "0.2"'))
        else:
            fm = yaml.safe_load(raw_fm) or {}
            if "okf_version" not in fm:
                out.append(("W3", path, "root index frontmatter lacks okf_version"))
    elif raw_fm is not None:
        out.append(("E9", path, "non-root index.md must not carry frontmatter"))


def check_log(path: Path, out: list):
    for line in path.read_text(encoding="utf-8").split("\n"):
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m and not DATE_RE.match(m.group(1)):
            out.append(("W6", path, f"log heading '{m.group(1)}' not ISO YYYY-MM-DD"))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("bundle", type=Path)
    ap.add_argument("--strict", action="store_true", help="warnings fail too")
    args = ap.parse_args()

    out: list = []
    tiers: dict = {}
    for path in sorted(args.bundle.rglob("*.md")):
        if path.name == "index.md":
            check_index(path, path.parent == args.bundle, out)
        elif path.name == "log.md":
            check_log(path, out)
        else:
            check_concept(path, out, tiers)

    errors = [x for x in out if x[0].startswith("E")]
    warns = [x for x in out if x[0].startswith("W")]
    for code, path, msg in errors + warns:
        print(f"{code}  {path}: {msg}")
    total = sum(tiers.values())
    print(f"\nconcepts: {total}  tiers: " +
          ", ".join(f"{k} {v}" for k, v in sorted(tiers.items())))
    print(f"errors: {len(errors)}  warnings: {len(warns)}")
    if errors or (args.strict and warns):
        return 1
    print("conformant with OKF v0.2 (spec 11)" +
          ("" if not warns else "; warnings above are SHOULDs, not failures"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
