#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Assemble and stamp the data root of the ice sheet mass balance
closure's firn and surface mass balance terms: the two term files the
loaders wrote and the RECORD.json a computation reads before the CSVs.

The stamp carries the record name, the SHA-256 manifest of the two CSV
files, the time of stamping, the two loaders' own stamps (what each
read, from where, when, with which hash, and how it aggregated), and
the bookkeeping table: per term the product and its version, the GEMB
version, the forcing, the grid, the mask and aggregation, the units,
the sign convention, the uncertainty basis and the alternates not
read, plus the statement of what the ITS_LIVE distribution does not
carry (no Greenland surface mass balance, no grounded Antarctic term),
so a computation that expects a grounded Antarctic term finds the gap
here rather than in an empty query. The statements are read from the
loaders' stamps where the loader determined them and written down
here so a reader auditing a closure residual starts in one file.

Usage:
  isb_data_root.py --root DIR --record NAME
      DIR holds firn.csv, smb.csv and the loaders' stamps
      firn-stamp.json and smb-stamp.json
  --check   verify an existing RECORD.json against the files (exit 1 on drift)
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import sys
from pathlib import Path

TERMS = ("firn", "smb")


def sha256(p: Path) -> str:
    return "sha256:" + hashlib.sha256(p.read_bytes()).hexdigest()


def manifest(root: Path) -> dict:
    out = {}
    for t in TERMS:
        p = root / f"{t}.csv"
        if not p.is_file():
            sys.exit(f"{root} lacks {t}.csv")
        out[p.name] = sha256(p)
    return out


def per_series(stamp: dict, key: str) -> dict:
    return {name: s.get(key, "") for name, s in stamp.get("series", {}).items()}


def bookkeeping(stamps: dict) -> dict:
    table = {}
    for term in TERMS:
        st = stamps[term]
        table[term] = {
            "product_and_version": {name: f"{s.get('product', '')} (product version "
                                          f"{s.get('product_version', '')}, doi {s.get('doi', '')})"
                                    for name, s in st.get("series", {}).items()},
            "gemb_version": per_series(st, "gemb_version"),
            "forcing": per_series(st, "forcing"),
            "grid": per_series(st, "grid"),
            "mask": per_series(st, "mask"),
            "aggregation": per_series(st, "aggregation"),
            "reference": per_series(st, "reference"),
            "sampling": per_series(st, "sampling"),
            "coverage": {name: {"months": s.get("months"), "n_steps": s.get("n_steps"),
                                "cells": s.get("cells"), "area_km2": s.get("area_km2")}
                         for name, s in st.get("series", {}).items()},
            "units": st.get("units", ""),
            "sign_convention": st.get("sign_convention", ""),
            "uncertainty_basis": per_series(st, "uncertainty_basis"),
            "not_in_the_distribution": st.get("not_in_the_distribution", []),
            "alternates_not_read": st.get("alternates_not_read", []),
        }
    table["domains"] = {
        "greenland/ice_sheet": "the grounded Greenland Ice Sheet (mask 1 of the Greenland product); "
                               "firn only",
        "greenland/peripheral_glaciers": "the peripheral glaciers of Greenland (mask 2); firn only",
        "antarctica/ice_shelves": "the floating Antarctic ice shelves (ID 1 to 182 of the ice shelf "
                                  "product); firn and surface mass balance; not the grounded ice "
                                  "sheet",
    }
    table["reading_rule"] = ("a computation reads rows by ice_sheet and domain and by the sampling "
                             "column; a quarterly row is one product time step labelled by the "
                             "month of its time value, not a monthly value, and no month is ever "
                             "filled")
    return table


def build(root: Path, record: str):
    stamps = {}
    for t in TERMS:
        p = root / f"{t}-stamp.json"
        if not p.is_file():
            sys.exit(f"{root} lacks {t}-stamp.json (the loader's stamp)")
        stamps[t] = json.loads(p.read_text(encoding="utf-8"))
    files = manifest(root)
    mh = hashlib.sha256("\n".join(f"{k} {v}" for k, v in sorted(files.items())).encode()).hexdigest()
    stamp = {
        "record": record,
        "manifest": files,
        "manifest_sha256": "sha256:" + mh,
        "verified_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "terms": stamps,
        "bookkeeping": bookkeeping(stamps),
    }
    (root / "RECORD.json").write_text(json.dumps(stamp, indent=2) + "\n", encoding="utf-8")
    print(f"RECORD.json written for {record}: manifest sha256:{mh[:16]}, "
          + ", ".join(f"{t} {stamps[t]['months'][0]} to {stamps[t]['months'][1]}" for t in TERMS))


def check(root: Path):
    p = root / "RECORD.json"
    if not p.is_file():
        sys.exit(f"{root} lacks RECORD.json")
    stamp = json.loads(p.read_text(encoding="utf-8"))
    files = manifest(root)
    if files != stamp.get("manifest"):
        sys.exit("RECORD.json manifest does not match the files")
    for t in TERMS:
        if t not in stamp.get("terms", {}) or t not in stamp.get("bookkeeping", {}):
            sys.exit(f"RECORD.json lacks the {t} stamp or its bookkeeping row")
    print("RECORD.json matches the files")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--root", type=Path, required=True)
    ap.add_argument("--record")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    if a.check:
        check(a.root); return
    if not a.record:
        ap.error("--record is required to build")
    build(a.root, a.record)


if __name__ == "__main__":
    main()
