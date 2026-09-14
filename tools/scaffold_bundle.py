#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Scaffold a new provider bundle under knowledge/ so that a seed session
can add concepts to it without touching anything the gate reads outside
the bundle: the root index.md with its intro and empty type sections, the
change log, the DIGEST.md rendered by tools/digest.py for the empty
bundle, the four check lines in
tools/run_checks.sh, and the CODEOWNERS line for the bundle's steward
team. The team must already be declared in build-kit osp/teams.yaml or
the plugin gates refuse the CODEOWNERS line.

Usage:
  scaffold_bundle.py NAME --title "GES DISC" --team gesdisc-stewards
      --intro intro.txt [--sections datasets,gotchas]

The intro file holds the hand-written paragraph of the index (what the
bundle covers, who confirms it). Idempotent: an existing file is left
alone and reported.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SECTIONS = ("datasets", "gotchas", "recipes")

INDEX = """---
okf_version: "0.2"
---

# {name} bundle ({title})

{intro}

What this bundle claims, for the people who know the data: [DIGEST.md](DIGEST.md).
"""

LOG = """# {name} bundle: change log

Newest first. One line per change: date, concept path, what changed, who.

- {date} · bundle scaffolded empty by tools/scaffold_bundle.py: the index
  with its sections, this log, the check lines and the CODEOWNERS line
  for {team}; no concepts yet. (maintainer)
"""

CHECK_LINES = (
    "run uv run tools/check_okf_v02.py knowledge/{name} --provider nasa-daac-knowledge",
    "run uv run tools/check_negative.py knowledge/{name}",
    "run uv run tools/signature_check.py knowledge/{name} $sig",
    "run uv run tools/digest.py knowledge/{name} --check",
)


def write(path: Path, text: str, made: list, kept: list):
    if path.exists():
        kept.append(str(path.relative_to(ROOT)))
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    made.append(str(path.relative_to(ROOT)))


def add_check_lines(name: str, made: list, kept: list):
    p = ROOT / "tools" / "run_checks.sh"
    text = p.read_text(encoding="utf-8")
    wanted = [line.format(name=name) for line in CHECK_LINES]
    if all(w in text for w in wanted):
        kept.append("tools/run_checks.sh"); return
    lines = text.split("\n")
    out, inserted = [], {w: False for w in wanted}
    for line in lines:
        out.append(line)
        for w in wanted:
            tool = w.split()[3]
            # after the last existing line that runs the same tool on another bundle
            if not inserted[w] and line.startswith(f"run uv run {tool} knowledge/") and \
               not any(nxt.startswith(f"run uv run {tool} knowledge/") for nxt in lines[lines.index(line) + 1:]):
                out.append(w); inserted[w] = True
    if not all(inserted.values()):
        sys.exit("run_checks.sh: could not place every check line; add them by hand")
    p.write_text("\n".join(out), encoding="utf-8")
    made.append("tools/run_checks.sh")


def add_codeowners(name: str, team: str, made: list, kept: list):
    p = ROOT / "CODEOWNERS"
    text = p.read_text(encoding="utf-8")
    line = f"/knowledge/{name}/   @open-science-pillars/{team}"
    if re.search(rf"^/knowledge/{name}/\s", text, re.M):
        kept.append("CODEOWNERS"); return
    anchor = re.search(r"^/knowledge/\S+\s+@\S+\n(?!/knowledge/)", text, re.M)
    if not anchor:
        sys.exit("CODEOWNERS: no bundle block to extend")
    text = text[:anchor.end()] + line + "\n" + text[anchor.end():]
    p.write_text(text, encoding="utf-8")
    made.append("CODEOWNERS")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("name")
    ap.add_argument("--title", required=True)
    ap.add_argument("--team", required=True)
    ap.add_argument("--intro", type=Path, required=True)
    ap.add_argument("--sections", default=",".join(DEFAULT_SECTIONS))
    ap.add_argument("--date", default=None)
    a = ap.parse_args()
    if not re.fullmatch(r"[a-z][a-z0-9-]*", a.name):
        sys.exit("bundle name: lowercase letters, digits and hyphens")
    import datetime as dt
    date = a.date or dt.date.today().isoformat()
    bundle = ROOT / "knowledge" / a.name
    made, kept = [], []
    intro = a.intro.read_text(encoding="utf-8").strip()
    index = INDEX.format(name=a.name, title=a.title, intro=intro)
    for s in [s.strip() for s in a.sections.split(",") if s.strip()]:
        index += f"\n## {s}\n\n(none yet)\n"
    write(bundle / "index.md", index, made, kept)
    write(bundle / "log.md", LOG.format(name=a.name, date=date, team=a.team), made, kept)
    if not (bundle / "DIGEST.md").exists():
        import subprocess
        subprocess.run([sys.executable, str(ROOT / "tools" / "digest.py"), f"knowledge/{a.name}"],
                       check=True, cwd=ROOT, stdout=subprocess.DEVNULL)
        made.append(f"knowledge/{a.name}/DIGEST.md")
    else:
        kept.append(f"knowledge/{a.name}/DIGEST.md")
    add_check_lines(a.name, made, kept)
    add_codeowners(a.name, a.team, made, kept)
    print("made: " + ", ".join(made) if made else "made: nothing")
    if kept:
        print("kept: " + ", ".join(kept))


if __name__ == "__main__":
    main()
