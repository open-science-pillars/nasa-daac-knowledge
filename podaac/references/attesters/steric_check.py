#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# ///
"""Deterministic attester for the attested ECCO v4r4 steric height.

No LLM, stdlib only, consumer-side (spec 10.2). PASS (exit 0) only
when ALL hold, else FAIL (exit 1) naming the field:

  1. declared receipt fields present (run_id, code_sha256,
     bound_parameters, steric_mean_m_by_month, cells_in_region);
  2. code_sha256 matches the sanctioned computation file;
  3. bound parameters are the contract exactly: a registered region,
     months as YYYY-MM strings, rho0 1029.0, the density collection;
  4. THE CROSS-COMPUTATION ANCHOR: when the run is the reference
     configuration (region us-northeast-coast, months 2010-01 through
     2010-12), steric_trend_mm_yr must match the steric trend the
     attested sea-level partition's receipt records, +135.7772 mm/yr,
     within 0.05 mm/yr (measured agreement 2026-09-01: identical to
     four decimals), and cells_in_region must be exactly 102, the
     registered box's wet-cell count;
  5. sanity everywhere: every area-mean steric height within -60 to 0
     m (measured: -19.6 regional, -30.9 global);
  6. a global run must carry the Boussinesq caveat field, so no
     consumer can quote a global-mean steric change as modeled
     sea-surface rise.

Usage: steric_check.py RECEIPT.json [--computation PATH]
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path

REF_REGION = "us-northeast-coast"
REF_MONTHS = [f"2010-{m:02d}" for m in range(1, 13)]
REF_TREND = 135.7772
REF_TREND_TOL = 0.05
REF_CELLS = 102
RHO0 = 1029.0
COLLECTION = "ECCO_L4_DENS_STRAT_PRESS_LLC0090GRID_MONTHLY_V4R4"
REGIONS = {"us-northeast-coast", "gulf-of-mexico", "north-sea", "global"}
FIELDS = ["run_id", "code_sha256", "bound_parameters",
          "steric_mean_m_by_month", "cells_in_region"]


def fail(msg: str) -> int:
    print(f"FAIL: {msg}")
    return 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("receipt", type=Path)
    ap.add_argument("--computation", type=Path,
                    default=Path(__file__).parent.parent
                    / "computations" / "ecco_steric_height.py")
    args = ap.parse_args()
    r = json.loads(args.receipt.read_text(encoding="utf-8"))

    for f in FIELDS:
        if f not in r:
            return fail(f"receipt field missing: {f}")
    want = hashlib.sha256(args.computation.read_bytes()).hexdigest()
    if r["code_sha256"] != want:
        return fail("code_sha256 does not match the sanctioned computation")

    data = r.get("data")
    if (not isinstance(data, dict)
            or not isinstance(data.get("record"), dict)):
        return fail("receipt names no verified data tree: data.record must "
                    "be the RECORD.json stamp the verify tool leaves in "
                    "a tree checked against its manifest; nothing is "
                    "attested against unmanifested data")

    bp = r["bound_parameters"]
    if bp.get("region") not in REGIONS:
        return fail(f"region {bp.get('region')!r} is not registered")
    months = bp.get("months")
    if (not isinstance(months, list) or not months
            or not all(isinstance(m, str) and len(m) == 7 and m[4] == "-"
                       for m in months)):
        return fail("months is not a list of YYYY-MM")
    if bp.get("rho0_kg_m3") != RHO0 or bp.get("collection") != COLLECTION:
        return fail("constants or collection differ from the contract")

    for m, s in r["steric_mean_m_by_month"].items():
        if not (-60.0 <= s <= 0.0):
            return fail(f"steric mean {s} m outside [-60, 0] for {m}")

    if bp["region"] == REF_REGION and months == REF_MONTHS:
        t = r.get("steric_trend_mm_yr")
        if t is None or abs(t - REF_TREND) > REF_TREND_TOL:
            return fail(f"reference trend {t} mm/yr not within "
                        f"{REF_TREND_TOL} of the sea-level partition's "
                        f"signed {REF_TREND}")
        if r["cells_in_region"] != REF_CELLS:
            return fail(f"cells_in_region {r['cells_in_region']} != {REF_CELLS}")
        print(f"PASS run {r['run_id']}: sanctioned code, contract "
              f"parameters, and the cross-computation anchor holds "
              f"(steric trend {t:+.4f} mm/yr vs the signed partition's "
              f"{REF_TREND:+.4f})")
        return 0

    if bp["region"] == "global" and "boussinesq_caveat" not in r:
        return fail("global run without the Boussinesq caveat field")

    print(f"PASS run {r['run_id']}: sanctioned code, contract parameters, "
          f"and sanity bounds hold ({bp['region']}, {len(months)} months)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
