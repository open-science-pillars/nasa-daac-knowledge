#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# ///
"""Deterministic attester for the attested regional sea level partition.

Stdlib only, consumer-side. Checks A1 through A5 from the contract
(podaac/computations/ecco-regional-sea-level.md). Exit 0 PASS, 1 FAIL
with the failing check named.

A4's tolerance is MEASURED, never assumed: TOLERANCE_M below is set from
the first sanctioned fixture run and recorded in the concept in the same
change; while it is None, every run fails A4 by design.
"""

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

RECEIPT_FIELDS = ("run_id", "code_sha256", "bound_parameters", "ssh_variant",
                  "months", "cells_evaluated", "trend_total_mm_yr",
                  "trend_mass_mm_yr", "trend_steric_mm_yr",
                  "partition_residual_max")
REGIONS = {"us-northeast-coast", "gulf-of-mexico", "north-sea"}
SPAN = ("1992-01", "2017-12")
TOLERANCE_M = 1.0e-3   # m; measured 2026-08-30 on us-northeast-coast
# 2010-01:2010-12 (max monthly area-mean residual 5.085e-04 m over 102
# cells); recorded with ~2x headroom, per the measured-not-assumed rule.
DEFAULT_COMPUTATION = (Path(__file__).resolve().parent.parent
                       / "computations" / "ecco_regional_sea_level.py")


def fail(check: str, msg: str) -> int:
    print(f"FAIL {check}: {msg}")
    return 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("receipt", type=Path)
    ap.add_argument("--computation", type=Path, default=DEFAULT_COMPUTATION)
    args = ap.parse_args()

    try:
        r = json.loads(args.receipt.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        return fail("receipt", f"unreadable or not JSON: {e}")
    for f in RECEIPT_FIELDS:
        if f not in r:
            return fail(f, "missing from receipt")

    want = hashlib.sha256(args.computation.read_bytes()).hexdigest()
    if r["code_sha256"] != want:
        return fail("A1", f"receipt {str(r['code_sha256'])[:12]}... does not match "
                    f"sanctioned computation {want[:12]}...")

    bound = r["bound_parameters"]
    if not isinstance(bound, dict) or set(bound) != {"region", "period"}:
        return fail("A2", "bound_parameters must bind exactly region and period")
    if bound["region"] not in REGIONS:
        return fail("A2", f"region '{bound['region']}' is not in the registry")
    m = re.fullmatch(r"(\d{4}-\d{2}):(\d{4}-\d{2})", str(bound["period"]))
    if not m or not (SPAN[0] <= m.group(1) <= m.group(2) <= SPAN[1]):
        return fail("A2", f"period '{bound['period']}' malformed or outside "
                    f"{SPAN[0]}..{SPAN[1]}")

    if r["ssh_variant"] != "SSH":
        return fail("A3", f"ssh_variant '{r['ssh_variant']}' is not the stated "
                    "convention (exactly SSH; one variant, never mixed)")

    if TOLERANCE_M is None:
        return fail("A4", "no tolerance recorded yet: the pass bar is measured "
                    "on the sanctioned fixture run and written into the concept "
                    "and this attester together; until then nothing attests")
    resid = float(r["partition_residual_max"])
    if resid > TOLERANCE_M:
        return fail("A4", f"partition_residual_max {resid:.3e} m exceeds the "
                    f"recorded tolerance {TOLERANCE_M:.1e} m")

    if int(r["months"]) <= 0 or int(r["cells_evaluated"]) <= 0:
        return fail("A5", "months and cells_evaluated must be positive")

    print(f"PASS run {r['run_id']}: region {bound['region']} period "
          f"{bound['period']}, residual_max {resid:.3e} m within "
          f"{TOLERANCE_M:.1e}, variant {r['ssh_variant']}, "
          f"{r['months']} months, {r['cells_evaluated']} cells")
    return 0


if __name__ == "__main__":
    sys.exit(main())
