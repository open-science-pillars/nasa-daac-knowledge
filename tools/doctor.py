#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# ///
"""Is this machine ready to run the plugins' scripts? Say so, and make
it so.

Every script in these plugins carries its dependencies in a PEP 723
block and runs as `uv run <script>`; uv builds the script's environment
on first run and caches it. Two things can still go wrong on a fresh
machine, and this tool names both: uv is not installed (nothing runs),
or the first run of a script has to resolve and download its packages
(netCDF4, numpy, matplotlib) and looks like a hang or, offline, fails.

  doctor.py [ROOT ...]          check uv, list every script with a block
  doctor.py --warm [ROOT ...]   also build each script's environment now
                                (uv sync --script), so later runs start
                                at once and work offline

ROOT defaults to the directory above tools/ (this plugin). Give the
other plugins' install paths too (`claude plugin list` shows them) to
warm everything at once. Exit 1 when uv is missing or a warm-up fails.
This file needs nothing beyond the standard library, so if uv is the
thing that is missing, `python3 tools/doctor.py` still tells you.
"""

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

BLOCK = re.compile(r"^# /// script\s*$(.*?)^# ///\s*$", re.M | re.S)
SKIP_DIRS = {"__pycache__", ".git", ".venv", "node_modules"}
INSTALL = ("install uv: https://docs.astral.sh/uv/getting-started/installation/ "
           "(macOS and Linux: curl -LsSf https://astral.sh/uv/install.sh | sh)")


def scripts_with_blocks(roots):
    for root in roots:
        root = Path(root)
        files = [root] if root.is_file() else sorted(
            p for p in root.rglob("*.py") if not (set(p.parts) & SKIP_DIRS))
        for p in files:
            text = p.read_text(encoding="utf-8", errors="replace")
            m = BLOCK.search(text)
            if not m:
                continue
            deps = re.search(r"^#\s*dependencies\s*=\s*\[(.*?)\]\s*$", m.group(1), re.M | re.S)
            names = re.findall(r"[\"']([^\"']+)[\"']", deps.group(1)) if deps else []
            yield p, names


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("roots", nargs="*", type=Path,
                    default=[Path(__file__).resolve().parent.parent])
    ap.add_argument("--warm", action="store_true",
                    help="build every script's environment now (uv sync --script)")
    args = ap.parse_args()

    uv = shutil.which("uv")
    if not uv:
        print("FAIL  uv is not on PATH; nothing here runs without it.")
        print(f"      {INSTALL}")
        return 1
    ver = subprocess.run([uv, "--version"], capture_output=True, text=True).stdout.strip()
    print(f"ok    {ver} at {uv}")

    found = list(scripts_with_blocks(args.roots))
    with_deps = [(p, d) for p, d in found if d]
    print(f"ok    {len(found)} scripts carry a dependency block under "
          f"{', '.join(str(r) for r in args.roots)}; {len(with_deps)} need packages")
    if not args.warm:
        packages = sorted({re.split(r"[\[<>=!~; @]", n)[0] for _, d in with_deps for n in d})
        print(f"      packages they resolve on first run: {', '.join(packages)}")
        print("      run with --warm to build every environment now")
        return 0

    failed = 0
    for p, deps in with_deps:
        r = subprocess.run([uv, "sync", "--script", str(p)], capture_output=True, text=True)
        if r.returncode == 0:
            print(f"warm  {p}  ({', '.join(deps)})")
        else:
            failed += 1
            last = (r.stderr.strip().splitlines() or ["no output"])[-1]
            print(f"FAIL  {p}: {last}")
    print(f"doctor: {len(with_deps) - failed} environments ready, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
