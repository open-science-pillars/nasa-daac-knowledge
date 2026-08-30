#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "numpy",
#     "xarray",
#     "netcdf4",
#     "dask",
# ]
# ///
"""Sanctioned computation for the attested regional sea level partition.

Contract: podaac/computations/ecco-regional-sea-level.md. ECCO-internal
v1 scope: over a REGISTERED region and a month period, area-mean monthly
anomaly series of total sea level (the SSH variant, stated in the
receipt), the manometric piece (OBP), and an INDEPENDENT steric piece
from the model's own density anomaly (RHOAnoma integrated over depth
with partial cells), all on the native llc90 grid. The receipt carries
the three trends, the maximum monthly partition residual, and the
convention-bound bookkeeping fields. Consumers bind values for the
declared parameters and MUST NOT edit this file; the attester hashes it.
"""

import argparse
import datetime
import hashlib
import json
import re
import sys
import uuid
from pathlib import Path

import numpy as np
import xarray as xr

RHO0 = 1029.0            # kg m-3, the model's Boussinesq reference density
SSH_VARIANT = "SSH"      # one variant, stated, never mixed (ssh-ib-variants)

# The region registry: part of the sanctioned file by design, so an
# unregistered region fails attestation (A2) instead of improvising a
# mask. Bounds are (lon_min, lon_max, lat_min, lat_max), degrees east.
REGIONS = {
    "us-northeast-coast": (-75.0, -65.0, 35.0, 45.0),
    "gulf-of-mexico": (-98.0, -81.0, 18.0, 31.0),
    "north-sea": (-2.0, 9.0, 51.0, 60.0),
}

SPAN = ("1992-01", "2017-12")   # ECCO v4r4; briefings state this boundary


def parse_period(period: str):
    m = re.fullmatch(r"(\d{4}-\d{2}):(\d{4}-\d{2})", period)
    if not m:
        raise SystemExit(f"period must be YYYY-MM:YYYY-MM, got {period!r}")
    a, b = m.group(1), m.group(2)
    if not (SPAN[0] <= a <= b <= SPAN[1]):
        raise SystemExit(f"period {period} outside the v4r4 span {SPAN}")
    return a, b


def monthly(root: Path, short_name: str, a: str, b: str) -> xr.Dataset:
    ds = xr.open_mfdataset(str(root / short_name / "*.nc"), combine="by_coords")
    ds = ds.sel(time=slice(a, b))
    return ds


def compute(region: str, period: str, root: Path) -> dict:
    lon0, lon1, lat0, lat1 = REGIONS[region]
    a, b = parse_period(period)

    grid = xr.open_dataset(root / "geometry" / "GRID_GEOMETRY_ECCO_V4r4_native_llc0090.nc")
    ssh = monthly(root, "ECCO_L4_SSH_LLC0090GRID_MONTHLY_V4R4", a, b)
    obp = monthly(root, "ECCO_L4_OBP_LLC0090GRID_MONTHLY_V4R4", a, b)
    dens = monthly(root, "ECCO_L4_DENS_STRAT_PRESS_LLC0090GRID_MONTHLY_V4R4", a, b)
    n_months = int(ssh.sizes["time"])
    assert n_months == int(obp.sizes["time"]) == int(dens.sizes["time"]), \
        "matching-period rule violated: the three inputs cover different months"
    assert n_months >= 2, "need at least two months"

    xc, yc = grid.XC.values, grid.YC.values                  # (13, 90, 90)
    wet = grid.maskC.values[0] > 0                            # surface wet
    inbox = (yc >= lat0) & (yc <= lat1) & (xc >= lon0) & (xc <= lon1) & wet
    w = grid.rA.values * inbox                                # area weights
    wsum = float(w.sum())
    assert wsum > 0, f"region {region} selects no wet cells"

    def area_mean(field2d):                                   # (t, 13, 90, 90)
        v = np.nan_to_num(field2d)
        return (v * w[None]).sum(axis=(1, 2, 3)) / wsum

    total = area_mean(ssh[SSH_VARIANT].values)                # m
    mass = area_mean(obp["OBP"].values)                       # m (equiv. sea level)

    # Independent steric: -(1/rho0) * integral of RHOAnoma over depth,
    # partial cells in (hFacC * drF); model-consistent density, never a
    # foreign equation of state.
    hfac_drf = grid.hFacC.values * grid.drF.values[:, None, None, None]  # (50,13,90,90)
    rho = np.nan_to_num(dens["RHOAnoma"].values)              # (t, 50, 13, 90, 90)
    steric_h = -(rho * hfac_drf[None]).sum(axis=1) / RHO0     # (t, 13, 90, 90), m
    steric = area_mean(steric_h)

    def anom(s):
        return s - s.mean()

    ta, ma, sa = anom(total), anom(mass), anom(steric)
    resid = ta - ma - sa
    months_ax = np.arange(n_months, dtype=float)

    def trend_mm_yr(s):
        slope = np.polyfit(months_ax, s, 1)[0]                # m / month
        return float(slope * 12.0 * 1000.0)

    return {
        "ssh_variant": SSH_VARIANT,
        "months": n_months,
        "cells_evaluated": int(inbox.sum()),
        "trend_total_mm_yr": round(trend_mm_yr(ta), 4),
        "trend_mass_mm_yr": round(trend_mm_yr(ma), 4),
        "trend_steric_mm_yr": round(trend_mm_yr(sa), 4),
        "partition_residual_max": float(np.abs(resid).max()),
        "residual_series_mm": [round(float(r) * 1000.0, 4) for r in resid],
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--region", required=True, choices=sorted(REGIONS),
                    help="registered region name (declared parameter)")
    ap.add_argument("--period", required=True,
                    help="YYYY-MM:YYYY-MM within 1992-01..2017-12 (declared parameter)")
    ap.add_argument("--data-root", type=Path, default=Path.home() / "ECCO_V4r4",
                    help="cache root (execution plumbing, not a parameter)")
    ap.add_argument("--receipt", type=Path, default=None)
    args = ap.parse_args()

    stats = compute(args.region, args.period, args.data_root)
    series = stats.pop("residual_series_mm")
    print(f"region {args.region}, {stats['months']} months, "
          f"{stats['cells_evaluated']} cells", file=sys.stderr)
    print(f"trends mm/yr: total {stats['trend_total_mm_yr']}, "
          f"mass {stats['trend_mass_mm_yr']}, steric {stats['trend_steric_mm_yr']}",
          file=sys.stderr)
    print(f"partition residual max {stats['partition_residual_max']:.3e} m; "
          f"monthly series (mm): {series}", file=sys.stderr)

    receipt = {
        "run_id": (datetime.datetime.now(datetime.timezone.utc)
                   .strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:8]),
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "bound_parameters": {"region": args.region, "period": args.period},
        **stats,
    }
    text = json.dumps(receipt, indent=2)
    if args.receipt:
        args.receipt.write_text(text + "\n", encoding="utf-8")
        print(f"receipt written: {args.receipt}", file=sys.stderr)
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
