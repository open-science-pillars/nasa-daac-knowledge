#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# ///
"""Every script resolves its own dependencies, or the gate says which
one does not.

The tools, computations, attesters and skill scripts in these plugins
run as `uv run <script>`: uv reads the PEP 723 block at the top of the
file (`# /// script` ... `# ///`), builds an environment with exactly
the packages it declares, and runs the script in it. Nothing is
installed by hand, so a user of the plugins never sees
`ModuleNotFoundError: netCDF4` as long as every script that imports a
third-party package declares it. This check is that guarantee, run
offline before any PR: it parses each script's imports, discards the
standard library and modules that sit beside the script, and fails
naming any script whose block does not declare a package it imports,
or that has no block at all.

Import names and distribution names differ for a few packages (yaml is
pyyaml, netCDF4 is netcdf4 once normalized, ecco_v4_py is ecco-v4-py);
the table below carries the ones these plugins use. A declared package
that is never imported is not a failure: xarray's netCDF engine and
dask are pulled in by name, not by import.

  check_script_deps.py ROOT [ROOT ...]   scan every .py under the roots
  check_script_deps.py --selftest
"""

import argparse
import ast
import re
import sys
import tempfile
from pathlib import Path

STDLIB = set(getattr(sys, "stdlib_module_names", ())) | {
    "__future__", "_thread", "typing_extensions_stub"}
IMPORT_TO_DIST = {
    "yaml": "pyyaml", "PIL": "pillow", "netCDF4": "netcdf4",
    "ecco_v4_py": "ecco-v4-py", "sklearn": "scikit-learn",
    "dateutil": "python-dateutil", "cv2": "opencv-python",
    "matplotlib": "matplotlib", "mpl_toolkits": "matplotlib",
}
BLOCK = re.compile(r"^# /// script\s*$(.*?)^# ///\s*$", re.M | re.S)
SKIP_DIRS = {"__pycache__", ".git", ".venv", "node_modules"}


def normalize(name: str) -> str:
    return re.sub(r"[-_.]+", "-", name).lower()


def declared(text: str):
    """The distributions a script's PEP 723 block declares, normalized;
    None when the file has no block."""
    m = BLOCK.search(text)
    if not m:
        return None
    body = "\n".join(line[2:] if line.startswith("# ") else line[1:]
                     for line in m.group(1).splitlines())
    deps = re.search(r"^dependencies\s*=\s*\[(.*?)\]\s*$", body, re.M | re.S)
    if not deps:
        return set()
    out = set()
    for spec in re.findall(r"[\"']([^\"']+)[\"']", deps.group(1)):
        out.add(normalize(re.split(r"[\[<>=!~; @]", spec.strip(), 1)[0]))
    return out


def imported(path: Path, text: str):
    """Top-level names of third-party imports: not stdlib, not a module
    or package that sits beside the script."""
    try:
        tree = ast.parse(text)
    except SyntaxError as e:
        return None, f"does not parse: {e}"
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(a.name.split(".")[0] for a in node.names)
        elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
            names.add(node.module.split(".")[0])
    here = path.parent
    third = set()
    for n in names:
        if n in STDLIB or n == path.stem:
            continue
        if (here / f"{n}.py").exists() or (here / n).is_dir():
            continue
        third.add(n)
    return third, None


def check_file(path: Path):
    """Failure messages for one script; empty when it resolves itself."""
    text = path.read_text(encoding="utf-8", errors="replace")
    third, err = imported(path, text)
    if err:
        return [f"{path}: {err}"]
    if not third:
        return []
    decl = declared(text)
    if decl is None:
        return [f"{path}: imports {', '.join(sorted(third))} and has no "
                "PEP 723 block (uv run cannot resolve it)"]
    missing = sorted(n for n in third
                     if normalize(IMPORT_TO_DIST.get(n, n)) not in decl)
    if missing:
        return [f"{path}: imports {', '.join(missing)} not declared in its "
                "dependencies (uv run will fail on the import)"]
    return []


def scan(roots):
    problems, count = [], 0
    for root in roots:
        root = Path(root)
        files = [root] if root.is_file() else sorted(
            p for p in root.rglob("*.py")
            if not (set(p.parts) & SKIP_DIRS))
        for p in files:
            count += 1
            problems.extend(check_file(p))
    return count, problems


def selftest() -> int:
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        cases = {
            "ok.py": ("# /// script\n# dependencies = [\"numpy\", \"netCDF4>=1.6\"]\n# ///\n"
                      "import numpy\nimport netCDF4\nimport json\n", 0),
            "mapped.py": ("# /// script\n# dependencies = ['pyyaml']\n# ///\nimport yaml\n", 0),
            "local.py": ("# /// script\n# ///\nimport helper\nimport os\n", 0),
            "helper.py": ("x = 1\n", 0),
            "stdlib_only.py": ("import sys, pathlib\nfrom collections import Counter\n", 0),
            "undeclared.py": ("# /// script\n# dependencies = [\"numpy\"]\n# ///\n"
                              "import numpy\nfrom netCDF4 import Dataset\n", 1),
            "noblock.py": ("import numpy\n", 1),
            "extras.py": ("# /// script\n# dependencies = [\"xarray[io]\", \"dask\"]\n# ///\n"
                          "import xarray\n", 0),
        }
        for name, (src, _) in cases.items():
            (d / name).write_text(src)
        bad = 0
        for name, (_, want) in cases.items():
            got = 1 if check_file(d / name) else 0
            if got != want:
                print(f"selftest FAIL: {name} expected {want} got {got}")
                bad += 1
        if bad:
            return 1
    print("check_script_deps selftest: OK (declared, mapped names, local "
          "modules, stdlib, undeclared, missing block, extras)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("roots", nargs="*", type=Path)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    if not args.roots:
        ap.error("give at least one ROOT or --selftest")
    count, problems = scan(args.roots)
    for p in problems:
        print(f"FAIL  {p}")
    print(f"check_script_deps: {count} scripts scanned, {len(problems)} "
          f"cannot resolve their own dependencies")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
