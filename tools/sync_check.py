#!/usr/bin/env python3
"""Snapshot sync check (SPEC v0.6 §5.7): verify a plugin's pinned
snapshot is byte-identical to this canonical bundle.

Usage: python tools/sync_check.py <plugin-knowledge-dir> [--map SUB=SUB ...]
Exit 0 if every overlapping concept file is byte-identical; 1 otherwise.
"""
import sys
from pathlib import Path

canon = Path(__file__).resolve().parent.parent / "podaac"
target = Path(sys.argv[1])
bad, checked = [], 0
for f in canon.rglob("*.md"):
    rel = f.relative_to(canon)
    if rel.name in ("index.md", "log.md"):
        continue
    for cand in (target / rel, target / "snapshot-podaac" / rel):
        if cand.exists():
            checked += 1
            if cand.read_bytes() != f.read_bytes():
                bad.append(str(rel))
            break
print(f"sync_check: {checked} snapshot files checked against canonical")
if bad:
    print("STALE:", *bad, sep="\n  ")
    sys.exit(1)
print("all byte-identical")
