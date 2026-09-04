#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml"]
# ///
"""Migrate an OSP knowledge bundle from OKF v0.1 (plus SPEC v0.6 trust
extensions) to OKF v0.2 frontmatter.

Line-surgical by design: only the keys being migrated are touched; every
other byte, including YAML comments inside frontmatter, is preserved so
review diffs stay minimal. Idempotent: a file already carrying a
`generated:` key is reported and skipped.

Transforms (spec references are OKF v0.2, GoogleCloudPlatform/knowledge-catalog):
  timestamp: X                 ->  generated: { by: <--generated-by>, at: X }   (spec 13.1)
  status: verified             ->  status: stable                               (spec 5.4)
  status: stale                ->  status: stable  (+ stale_after today)        (spec 5.5)
  status: superseded           ->  status: deprecated                           (spec 5.4)
  status: disputed             ->  left in place, WARN (manual call)
  verified: DATE
  verified_by: STR             ->  verified: { by: <--steward>, at: DATE }      (spec 5.2, 7)
  evidence:                    ->  sources: (id + resource per entry)           (spec 5.1)
    - URL
  (root index.md)              ->  prepend okf_version: "0.2" frontmatter       (spec 12)
  (all concepts)               ->  add stale_after if --stale-after given       (spec 5.5)

Usage:
  migrate_okf_v02.py BUNDLE_DIR --steward human:ID --generated-by ACTOR
      [--stale-after YYYY-MM-DD] [--write]

Dry run by default. --write applies changes in place. Exit 0 on success.
"""

import argparse
import datetime
import re
import sys
from pathlib import Path

RESERVED = {"index.md", "log.md"}
ACTOR_RE = re.compile(r"^(human:|process:|team:)\S+$|^[\w.-]+/[\w.@-]+$")


def iso_at(value: str) -> str:
    """Normalize a bare date or datetime string to ISO 8601 with time."""
    v = value.strip().strip("'\"")
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", v):
        return v + "T00:00:00Z"
    return v


def slug_for(url: str, taken: set) -> str:
    """Derive a stable, readable sources id from a URL."""
    u = url.strip().rstrip("/")
    m = re.match(r"https?://([^/]+)(?:/(.*))?", u)
    if m:
        host = m.group(1).split(".")
        host_part = host[-2] if len(host) >= 2 else host[0]
        tail = (m.group(2) or "").split("/")[-1]
        tail = re.sub(r"\.\w+$", "", tail)
        base = "-".join(p for p in (host_part, tail) if p) or "source"
    else:
        base = re.sub(r"\.\w+$", "", u.split("/")[-1]) or "source"
    base = re.sub(r"[^a-zA-Z0-9-]+", "-", base).strip("-").lower()[:48] or "source"
    cand, n = base, 2
    while cand in taken:
        cand, n = f"{base}-{n}", n + 1
    taken.add(cand)
    return cand


def split_frontmatter(text: str):
    """Return (fm_lines, body_text) or (None, text) when no frontmatter."""
    if not text.startswith("---"):
        return None, text
    lines = text.split("\n")
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return lines[: i + 1], "\n".join(lines[i + 1:])
    return None, text


def migrate_concept(path: Path, args, report: list) -> str | None:
    text = path.read_text(encoding="utf-8")
    fm, body = split_frontmatter(text)
    if fm is None:
        report.append(f"SKIP  {path}: no frontmatter block")
        return None
    if any(re.match(r"^generated:", ln) for ln in fm):
        report.append(f"SKIP  {path}: already migrated (generated: present)")
        return None

    out, actions = [], []
    verified_at, saw_verified_by = None, False
    sources_ids: set = set()
    i = 0
    while i < len(fm):
        line = fm[i]

        m = re.match(r"^timestamp:\s*(.+?)\s*$", line)
        if m:
            out.append(f"generated: {{ by: {args.generated_by}, at: {iso_at(m.group(1))} }}")
            actions.append("timestamp -> generated")
            i += 1
            continue

        m = re.match(r"^status:\s*(\S+)\s*$", line)
        if m:
            old = m.group(1)
            new = {"verified": "stable", "stale": "stable",
                   "superseded": "deprecated", "draft": "draft"}.get(old)
            if new is None:
                out.append(line)
                actions.append(f"WARN status '{old}' left as-is (manual call)")
            else:
                out.append(f"status: {new}")
                if old != new:
                    actions.append(f"status {old} -> {new}")
                if old == "stale" and not args.stale_after:
                    today = datetime.date.today().isoformat()
                    out.append(f"stale_after: {today}")
                    actions.append(f"stale -> stale_after {today}")
            i += 1
            continue

        m = re.match(r"^verified:\s*(.+?)\s*$", line)
        if m:
            verified_at = iso_at(m.group(1))
            i += 1  # emitted later, once verified_by is known
            continue

        m = re.match(r"^verified_by:\s*(.+?)\s*$", line)
        if m:
            saw_verified_by = True
            raw = m.group(1).strip().strip("'\"")
            actor = raw if ACTOR_RE.match(raw) else args.steward
            if actor != raw:
                actions.append(f"verified_by '{raw}' -> {actor}")
            at = verified_at or iso_at(datetime.date.today().isoformat())
            out.append(f"verified: {{ by: {actor}, at: {at} }}")
            actions.append("verified/verified_by -> verified event")
            i += 1
            continue

        if re.match(r"^evidence:\s*$", line):
            urls = []
            i += 1
            while i < len(fm) and re.match(r"^\s+-\s+\S", fm[i]):
                urls.append(re.sub(r"^\s+-\s+", "", fm[i]).strip())
                i += 1
            out.append("sources:")
            for u in urls:
                sid = slug_for(u, sources_ids)
                out.append(f"  - id: {sid}")
                out.append(f"    resource: {u}")
            actions.append(f"evidence -> sources ({len(urls)} entries: "
                           + ", ".join(sorted(sources_ids)) + ")")
            continue

        out.append(line)
        i += 1

    if verified_at and not saw_verified_by:
        # A verified date with no verified_by line: sign as the steward.
        out.insert(len(out) - 1, f"verified: {{ by: {args.steward}, at: {verified_at} }}")
        actions.append("verified date (no verified_by) -> steward event")

    if args.stale_after and not any(re.match(r"^stale_after:", ln) for ln in out):
        out.insert(len(out) - 1, f"stale_after: {args.stale_after}")
        actions.append(f"stale_after {args.stale_after}")

    if not actions:
        report.append(f"OK    {path}: nothing to migrate")
        return None
    report.append(f"EDIT  {path}\n        " + "\n        ".join(actions))
    if sources_ids:
        report.append(f"TODO  {path}: footnote pass, join body claims to sources ids "
                      f"[{', '.join(sorted(sources_ids))}] (spec 5.1)")
    return "\n".join(out) + "\n" + body


def migrate_root_index(path: Path, report: list) -> str | None:
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        report.append(f"OK    {path}: root index already carries frontmatter")
        return None
    report.append(f"EDIT  {path}\n        prepend okf_version 0.2 frontmatter (spec 12)")
    return '---\nokf_version: "0.2"\n---\n\n' + text


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("bundle", type=Path, help="bundle directory, e.g. knowledge/podaac/")
    ap.add_argument("--steward", required=True,
                    help="steward actor for verified events, e.g. human:PaulMRamirez")
    ap.add_argument("--generated-by", required=True,
                    help="actor for generated.by, e.g. knowledge-seeder/claude; "
                         "review per file, hand-authored concepts want a human: actor")
    ap.add_argument("--stale-after", default=None,
                    help="YYYY-MM-DD applied to concepts lacking stale_after")
    ap.add_argument("--write", action="store_true",
                    help="apply changes (default is a dry run)")
    args = ap.parse_args()

    if not args.steward.startswith("human:"):
        print("--steward must be a human: actor; the human-reviewed trust tier "
              "keys on that prefix (spec 5.3, 7)", file=sys.stderr)
        return 2
    if not ACTOR_RE.match(args.generated_by):
        print("--generated-by must follow the actor convention (spec 7)", file=sys.stderr)
        return 2

    report: list = []
    edits: list[tuple[Path, str]] = []
    for path in sorted(args.bundle.rglob("*.md")):
        if path.name == "log.md":
            continue
        if path.name == "index.md":
            if path.parent == args.bundle:
                new = migrate_root_index(path, report)
                if new is not None:
                    edits.append((path, new))
            continue
        new = migrate_concept(path, args, report)
        if new is not None:
            edits.append((path, new))

    print("\n".join(report))
    print(f"\n{len(edits)} file(s) to change; mode: {'WRITE' if args.write else 'dry run'}")
    if args.write:
        for path, new in edits:
            path.write_text(new, encoding="utf-8")
        print("written. Next: review generated.by per file, run the footnote pass, "
              "then tools/check_okf_v02.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
