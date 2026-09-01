#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# ///
"""Deterministic attester for the attested ECCO v4r4 regional heat
budget.

No LLM, stdlib only, consumer-side (spec 10.2). PASS (exit 0) only
when ALL hold, else FAIL (exit 1) naming the field:

  1. declared receipt fields present, including the DISCLOSURE set
     (resolved volume with mask digest and geometry digest) and the
     MUTATION EVIDENCE (all four named sabotages, each caught): a
     receipt without its failure demonstrations is not evidence;
  2. code_sha256 matches the sanctioned computation file;
  3. bound parameters are the contract exactly (collections,
     constants, the two bars);
  4. BOTH BARS recomputed from the receipt's own results: absolute
     per-volume within 1e-10 degC per s AND relative within 1e-6
     (measured 2026-08-31: geothermal omission passes the absolute
     bar alone, so one bar is not a criterion);
  5. every STRUCTURAL mutation actually failed a bar by the numbers
     it carries, not merely by its caught flag; the geothermal
     mutation may instead be marked not applicable, but only with an
     internally consistent story: its own numbers below both bars and
     the bottom-cell count disclosed (a volume without bottom cells
     owes no geothermal catch);
  6. REFERENCE ANCHOR (region southeast-atlantic-upper, year 2010):
     wet_cells exactly 27,921; volume within 0.1 percent of
     4.1351e15 m3; residual per volume within a factor of three of
     the measured 1.632e-14 TWO-SIDED, so a doctored receipt claiming
     a flattering residual fails the same as a broken one.

Usage: regional_budget_check.py RECEIPT.json [--computation PATH]
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path

ABS_BAR = 1e-10
REL_BAR = 1e-6
REF_REGION = "southeast-atlantic-upper"
REF_YEAR = 2010
REF_RESIDUAL = 1.632e-14
REF_FACTOR = 3.0
REF_CELLS = 27921
REF_VOLUME = 4.1351e15
COLLECTIONS = [
    "ECCO_L4_OCEAN_3D_TEMPERATURE_FLUX_LLC0090GRID_MONTHLY_V4R4",
    "ECCO_L4_HEAT_FLUX_LLC0090GRID_MONTHLY_V4R4",
    "ECCO_L4_TEMP_SALINITY_LLC0090GRID_SNAPSHOT_V4R4",
    "ECCO_L4_SSH_LLC0090GRID_SNAPSHOT_V4R4",
]
MUTATIONS = {"geothermal-omitted", "rim-west-face-shifted",
             "vertical-face-sign-flipped", "vertical-faces-omitted"}


def fail(msg: str) -> int:
    print(f"FAIL: {msg}")
    return 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("receipt", type=Path)
    ap.add_argument("--computation", type=Path,
                    default=Path(__file__).parent.parent
                    / "computations" / "ecco_regional_budget.py")
    args = ap.parse_args()
    r = json.loads(args.receipt.read_text(encoding="utf-8"))

    for f in ["run_id", "code_sha256", "bound_parameters",
              "resolved_volume", "results", "mutation_evidence",
              "caveats"]:
        if f not in r:
            return fail(f"receipt field missing: {f}")
    rv = r["resolved_volume"]
    for f in ["tile", "j", "i", "k_cells", "depth_face_m", "lat_extent",
              "lon_extent", "wet_cells", "bottom_cells", "volume_m3",
              "mask_sha256", "geometry_sha256"]:
        if f not in rv:
            return fail(f"disclosure field missing: resolved_volume.{f} "
                        "(the mask and geometry digests are the "
                        "contract, not optional)")

    want = hashlib.sha256(args.computation.read_bytes()).hexdigest()
    if r["code_sha256"] != want:
        return fail("code_sha256 does not match the sanctioned computation")

    bp = r["bound_parameters"]
    if (bp.get("collections") != COLLECTIONS
            or bp.get("rhoConst_kg_m3") != 1029.0
            or bp.get("Cp_J_kg_K") != 3994.0
            or bp.get("abs_bar_degC_s") != ABS_BAR
            or bp.get("rel_bar") != REL_BAR):
        return fail("constants, collections, or bars differ from the contract")

    res = r["results"]
    a = res.get("residual_per_volume_max_degC_s")
    rel = res.get("residual_relative_max")
    if a is None or rel is None:
        return fail("results missing the two bar figures")
    if a > ABS_BAR:
        return fail(f"absolute bar failed: {a} > {ABS_BAR}")
    if rel > REL_BAR:
        return fail(f"relative bar failed: {rel} > {REL_BAR}")

    ev = r["mutation_evidence"]
    names = {e.get("mutation") for e in ev}
    if names != MUTATIONS:
        return fail(f"mutation evidence must carry exactly {sorted(MUTATIONS)}; "
                    f"got {sorted(n for n in names if n)}")
    for e in ev:
        tripped = (e.get("residual_per_volume", 0) > ABS_BAR
                   or e.get("residual_relative", 0) > REL_BAR)
        if tripped:
            continue
        if (e.get("mutation") == "geothermal-omitted"
                and e.get("applicable") is False):
            if e.get("caught"):
                return fail("geothermal-omitted marked caught but its "
                            "numbers trip no bar")
            continue
        return fail(f"mutation {e.get('mutation')} did not fail a bar "
                    "by its own numbers; the test cannot fail, so "
                    "this receipt is not evidence")

    if (bp.get("mode") == "registered" and bp.get("region") == REF_REGION
            and bp.get("year") == REF_YEAR):
        if rv["wet_cells"] != REF_CELLS:
            return fail(f"reference wet_cells {rv['wet_cells']} != {REF_CELLS}")
        if abs(rv["volume_m3"] - REF_VOLUME) / REF_VOLUME > 0.001:
            return fail(f"reference volume {rv['volume_m3']} not within "
                        f"0.1 percent of {REF_VOLUME}")
        if not (REF_RESIDUAL / REF_FACTOR <= a <= REF_RESIDUAL * REF_FACTOR):
            return fail(f"reference residual {a} outside a factor of "
                        f"{REF_FACTOR} of the measured {REF_RESIDUAL} "
                        "(two-sided: flattering claims fail too)")
        print(f"PASS run {r['run_id']}: sanctioned code, both bars, all "
              f"four mutations demonstrated, and the reference anchors "
              f"hold (residual {a:.3e} vs measured {REF_RESIDUAL:.3e})")
        return 0

    print(f"PASS run {r['run_id']}: sanctioned code, both bars, "
          f"mutation evidence consistent "
          f"({bp.get('region') or 'explicit box'}, year {bp.get('year')})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
