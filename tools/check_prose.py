#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# ///
"""The wording rules these repositories keep, as a gate instead of a
sweep.

Three rules hold in everything a reader meets (concepts, indexes,
tool docstrings, READMEs, guides, skills, specs), and each of them has
drifted often enough to cost a sweep across every repository:

  citation    specification rules are cited by name, never by section
              number: the specification's numbering has moved several
              times, so "the merge-then-sign rule" stays true where
              "SPEC" followed by a section number goes stale. Name the
              rule and the document (docs/SPECIFICATION.md in
              open-science-pillars/marketplace); build-harness rule
              numbers follow the same rule. External standards keep the
              numbers their authors publish (OKF v0.2 and CF sections
              are fine) and are not flagged.
  scaffolding program bookkeeping stays out of artifacts: kit, session
              and wave numbers belong in tracking issues, runbooks and
              commit messages, never in a file a user reads.
  dash        no em or en dashes; a colon, comma, parenthesis or period
              does the work.

Scanned: .md .py .yaml .yml .json .sh .txt .cff .toml .js under the
roots, skipping .git, node_modules, __pycache__, .venv, and the
vendored docs/upstream. Skipped by name everywhere: SPECIFICATION.md
(the numbering's own home) and log.md (dated entries keep the text as
written). --exclude adds glob patterns matched against the path
relative to the root and against the basename, for a repository's
dated records.

  check_prose.py ROOT [ROOT ...] [--exclude GLOB ...]
  check_prose.py --selftest

One line per finding, path:line: rule: the text; exit 1 when anything
is found.
"""

import argparse
import fnmatch
import re
import sys
import tempfile
from pathlib import Path

EXTS = {".md", ".py", ".yaml", ".yml", ".json", ".sh", ".txt", ".cff",
        ".toml", ".js"}
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv"}
SKIP_NAMES = {"SPECIFICATION.md", "log.md"}
SECTION = "§"
RULES = {
    # SPEC or SPECIFICATION.md, an optional version, then a section sign
    # or a bare section number; the harness numbering too.
    "citation": re.compile(
        r"\bSPEC(IFICATION\.md)?( v?0\.[0-9](\.[0-9]+)?)? ?" + SECTION
        + r"|\bSPEC [0-9]+\.[0-9]"
        + r"|\(spec [0-9]+\.[0-9]"
        + r"|\bharness rule [0-9]"),
    "scaffolding": re.compile(r"\b(kit|session|wave) [0-9]+\b", re.I),
    "dash": re.compile("[\u2013\u2014]"),
}


def excluded(rel: Path, patterns) -> bool:
    if rel.name in SKIP_NAMES:
        return True
    parts = rel.parts
    if "upstream" in parts and "docs" in parts:
        return True
    return any(fnmatch.fnmatch(rel.as_posix(), p) or fnmatch.fnmatch(rel.name, p)
               for p in patterns)


def scan_file(path: Path):
    """(line number, rule, line text) for every finding in one file."""
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return []
    out = []
    for i, line in enumerate(text.splitlines(), 1):
        for rule, pat in RULES.items():
            if pat.search(line):
                out.append((i, rule, line.strip()))
    return out


def scan(root: Path, patterns):
    """Findings under one root as (path, line, rule, text); the count of
    files read comes second."""
    findings, files = [], 0
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix not in EXTS:
            continue
        rel = path.relative_to(root)
        if SKIP_DIRS & set(rel.parts) or excluded(rel, patterns):
            continue
        files += 1
        for line, rule, text in scan_file(path):
            findings.append((path, line, rule, text))
    return findings, files


def selftest() -> int:
    sect = SECTION
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "docs" / "upstream").mkdir(parents=True)
        (root / "knowledge").mkdir()
        (root / "reviews").mkdir()
        (root / "clean.md").write_text(
            "The merge-then-sign rule (the specification, docs/SPECIFICATION.md\n"
            "in open-science-pillars/marketplace) and OKF v0.2 " + sect + "10.2 are\n"
            "both cited the right way; CF " + sect + "2.5.1 too. A session in Claude\n"
            "Code, a kit of parts, and a wave breaking are all fine words.\n",
            encoding="utf-8")
        (root / "drift.md").write_text(
            "Per SPEC " + sect + "5.4 the edit merges (SPEC " + "5.1 says so).\n"
            "This came from " + "kit " + "12, " + "Session " + "3 of "
            + "wave " + "4.\nA dash " + "\u2014" + " here, and one " + "\u2013"
            + " there.\nAlso (spec " + "10.3) and harness rule " + "9.\n",
            encoding="utf-8")
        (root / "knowledge" / "log.md").write_text(
            "- 2026-01-01 " + "\u2014" + " SPEC " + sect + "5.4 kept as written\n",
            encoding="utf-8")
        (root / "docs" / "SPECIFICATION.md").write_text(
            "See " + sect + "5.4 and SPEC " + sect + "5.1 above.\n", encoding="utf-8")
        (root / "docs" / "upstream" / "okf.md").write_text(
            "vendored " + "\u2014" + " text\n", encoding="utf-8")
        (root / "reviews" / "pr-1-verdict.md").write_text(
            "the " + "kit " + "15 attribution\n", encoding="utf-8")
        (root / "notes.bin").write_bytes(b"\xff\xfe kit " + b"1")

        findings, files = scan(root, [])
        rules = sorted(r for _, _, r, _ in findings)
        by_file = {p.name for p, _, _, _ in findings}
        assert by_file == {"drift.md", "pr-1-verdict.md"}, by_file
        assert rules.count("citation") == 2, rules
        assert rules.count("scaffolding") == 2, rules
        assert rules.count("dash") == 1, rules
        assert files == 3, files
        findings, _ = scan(root, ["reviews/*"])
        assert {p.name for p, _, _, _ in findings} == {"drift.md"}
        findings, _ = scan(root, ["pr-*-verdict.md"])
        assert {p.name for p, _, _, _ in findings} == {"drift.md"}
    print("check_prose selftest: ok")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("roots", nargs="*", type=Path)
    ap.add_argument("--exclude", action="append", default=[], metavar="GLOB",
                    help="skip paths matching GLOB (relative path or basename)")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    if not args.roots:
        ap.error("give at least one ROOT or --selftest")
    total, files = 0, 0
    for root in args.roots:
        findings, n = scan(root, args.exclude)
        files += n
        for path, line, rule, text in findings:
            print(f"{path}:{line}: {rule}: {text[:120]}")
        total += len(findings)
    if total:
        print(f"check_prose: {total} finding(s) in {files} files scanned")
        return 1
    print(f"check_prose: clean ({files} files scanned)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
