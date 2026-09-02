# /// script
# requires-python = ">=3.10"
# dependencies = ["earthaccess"]
# ///
"""Fetch a data tree FROM ITS MANIFEST, resumably.

Reads the manifest (never a fresh search, so what was declared is
what is fetched), skips granules already present and verified,
downloads the rest through an authenticated Earthdata session, and
verifies each file after download against the manifest checksum
(whatever algorithm the manifest carries; the archive publishes
SHA-512), falling back to size only for a row with no checksum.
Progress goes to a log file, one line per granule naming the check
it passed, so a background run can be watched with tail. Credentials
come from earthaccess (environment token or netrc); nothing is
embedded here. Rerunning after any interruption continues where it
stopped.

The default root is the science record's tree, deliberately separate
from the pinned fixture cache: the fixtures are verified against
their own manifest with --exact, and a fetch must never grow them.
Rows without a URL (the tutorial's geothermal file) are not fetched;
their absence is reported so the operator can place them.
"""
import argparse
import datetime as dt
import hashlib
import json
import sys
from pathlib import Path

import earthaccess

SIZE_BAR = 1e-3


def check(path, row):
    """Return the name of the check the file passes, or None."""
    if not path.exists():
        return None
    cs = row.get("checksum")
    if cs:
        algo = cs["algorithm"].lower().replace("-", "")
        h = hashlib.new(algo)
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(1 << 22), b""):
                h.update(chunk)
        return algo if h.hexdigest().lower() == cs["value"].lower() else None
    want = row["size_mb"] * 1048576
    ok = want > 0 and abs(path.stat().st_size - want) / want <= SIZE_BAR
    return "size" if ok else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--data-root", type=Path,
                    default=Path.home() / "ECCO_V4r4_record")
    ap.add_argument("--log", type=Path, required=True)
    args = ap.parse_args()
    m = json.loads(args.manifest.read_text())
    root = args.data_root.expanduser()
    log = open(args.log, "a", buffering=1)

    def note(msg):
        log.write(f"{dt.datetime.now(dt.timezone.utc).isoformat()} {msg}\n")

    todo, unfetchable = [], []
    for sn, coll in m["collections"].items():
        for row in coll["files"]:
            target = root / row.get("path", f"{sn}/{row['granule']}")
            if check(target, row):
                continue
            (unfetchable if not row.get("url") else todo).append((row, target))
    for row, target in unfetchable:
        note(f"ABSENT {target} has no URL in the manifest; place it from "
             f"its origin: {row.get('origin', 'unknown')}")
    total_gb = sum(r["size_mb"] for r, _ in todo) / 1024
    note(f"START {len(todo)} granules to fetch, {total_gb:.1f} GB "
         f"(manifest total {m['total_gb']} GB) into {root}")
    if not todo:
        print(f"nothing to fetch; {len(unfetchable)} rows absent without URL")
        sys.exit(0 if not unfetchable else 1)
    earthaccess.login()
    session = earthaccess.get_requests_https_session()
    done_gb, fails = 0.0, 0
    for n, (row, target) in enumerate(todo, 1):
        target.parent.mkdir(parents=True, exist_ok=True)
        tmp = target.with_suffix(".part")
        try:
            with session.get(row["url"], stream=True, timeout=120) as r:
                r.raise_for_status()
                with open(tmp, "wb") as f:
                    for chunk in r.iter_content(1 << 20):
                        f.write(chunk)
            tmp.rename(target)
            passed = check(target, row)
            if not passed:
                target.unlink()
                raise RuntimeError("verification failed after download")
            done_gb += row["size_mb"] / 1024
            note(f"OK {n}/{len(todo)} {row['granule']} ({passed}) "
                 f"({done_gb:.1f}/{total_gb:.1f} GB)")
        except Exception as e:
            fails += 1
            tmp.unlink(missing_ok=True)
            note(f"FAIL {row['granule']}: {e}")
    note(f"DONE fetched {len(todo) - fails}/{len(todo)}, {fails} failures, "
         f"{len(unfetchable)} rows absent without URL")
    print(f"fetched {len(todo) - fails}/{len(todo)}, {fails} failures")
    sys.exit(0 if fails == 0 and not unfetchable else 1)


if __name__ == "__main__":
    main()
