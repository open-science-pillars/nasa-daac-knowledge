# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy", "xarray", "netCDF4", "dask", "ecco_v4_py"]
# ///
"""Attested regional heat budget over a control volume on the ECCO
V4r4 native llc90 grid.

WHAT IT COMPUTES
A closed heat budget over a control volume, comparing THREE
INDEPENDENT collections so agreement is evidence rather than
arithmetic: the tendency from temperature and sea-surface-height
SNAPSHOTS, the transport from the three-dimensional flux collection
read as RAW FACE FLUXES at the volume's boundary faces (never derived
from the divergence field; the telescoping identity is algebra, not
evidence), and the forcing from the surface flux collection plus
geothermal at bottom wet cells. Formulation mirrors the signed
pointwise heat budget exactly (constants, shortwave penetration,
free-surface scaling from bracketing snapshots).

TWO BARS, both required (measured 2026-08-31: omitting geothermal
passes an absolute bar of 1e-10 and is caught only by the relative
bar):
  absolute: max monthly |residual| / volume <= 1e-10 degC per s, the
            signed pointwise tolerance;
  relative: max monthly |residual| / largest term <= 1e-6.

MUTATION EVIDENCE IN THE RECEIPT. The executor reruns four sabotaged
variants (geothermal omitted, rim west face shifted one cell,
vertical face sign flipped, vertical faces omitted) and records that
each failed a bar. If a STRUCTURAL mutation passes, or the correct
run fails, NO RECEIPT IS WRITTEN: a test that cannot fail is not
evidence. The geothermal mutation alone is applicability-aware: a
volume containing few or no bottom cells has a genuinely negligible
geothermal term (measured: a 300 m open-ocean box leaves the omission
at 2.1e-7 relative, below the bar), so there the entry records
applicable false with its measured numbers and the bottom-cell count
in the disclosure, and the attester checks that story for internal
consistency instead of demanding a catch that physics does not owe.

CONTROL VOLUMES, two tiers:
  registered: a name from the KEYED registry below (keyed, never
              positional; the tuple-order defect is in the log);
  explicit:   --box LAT0 LAT1 LON0 LON1 --depth-m D, resolved to the
              smallest index rectangle containing every cell whose
              center falls in the box, on ONE tile, with the depth
              snapped to the nearest stored cell face.
Either way the receipt disclosed: the resolved index bounds, tile,
depth face, latitude and longitude extent, wet-cell count, volume, a
sha256 DIGEST OF THE RESOLVED WET MASK, and the sha256 of the
geometry granule, because no oracle can check that a mask is the
water the user meant; disclosure is the answer, and the digest makes
the mask the attester's business rather than the executor's word.

V1 LIMIT, stated: the volume must lie within one tile's interior
(faces 1 through 89). A box crossing a tile seam is refused with a
clear message; seam-crossing volumes arrive with the seam-calibrated
section machinery, not before.

INPUTS (local files only; retrieval is a separate, credentialed step)
  ECCO_L4_OCEAN_3D_TEMPERATURE_FLUX_..._MONTHLY   ADV*_TH, DF*_TH
  ECCO_L4_HEAT_FLUX_..._MONTHLY                   TFLUX, oceQsw
  ECCO_L4_TEMP_SALINITY_..._SNAPSHOT              THETA
  ECCO_L4_SSH_..._SNAPSHOT                        ETAN
  geometry granule; geothermalFlux.bin (tutorial distribution, NOT a
  PO.DAAC collection; a budget without it fails the relative bar)
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import uuid
from pathlib import Path

import numpy as np
import xarray as xr
import ecco_v4_py as ecco

RHOCONST, C_P = 1029.0, 3994.0
R_SW, ZETA1, ZETA2 = 0.62, 0.6, 20.0
ABS_BAR = 1e-10      # degC per s per m3 of volume; the signed pointwise bar
REL_BAR = 1e-6       # against the largest regional term
FLUX = "ECCO_L4_OCEAN_3D_TEMPERATURE_FLUX_LLC0090GRID_MONTHLY_V4R4"
HF = "ECCO_L4_HEAT_FLUX_LLC0090GRID_MONTHLY_V4R4"
SNP_TS = "ECCO_L4_TEMP_SALINITY_LLC0090GRID_SNAPSHOT_V4R4"
SNP_SSH = "ECCO_L4_SSH_LLC0090GRID_SNAPSHOT_V4R4"
GEOM = "geometry/GRID_GEOMETRY_ECCO_V4r4_native_llc0090.nc"

REGIONS = {
    # KEYED index boxes, never positional tuples. j and i are half-open
    # cell ranges on the named tile; k_cells is the number of levels
    # from the surface.
    "southeast-atlantic-upper": {
        "tile": 1, "j": (20, 60), "i": (20, 60), "k_cells": 20,
        "note": "eastern South Atlantic, roughly 44S to 10S and 18W "
                "to 22E, upper 323 m; the design note's reference "
                "volume",
    },
}

MUTATIONS = ["geothermal-omitted", "rim-west-face-shifted",
             "vertical-face-sign-flipped", "vertical-faces-omitted"]


def resolve_box(grid_all, lat0, lat1, lon0, lon1, depth_m):
    """Explicit tier: geographic box to one tile's index rectangle."""
    yc = grid_all.YC.values
    xc = grid_all.XC.values
    inbox = (yc >= lat0) & (yc <= lat1) & (xc >= lon0) & (xc <= lon1)
    tiles = np.unique(np.where(inbox.any(axis=(1, 2)))[0])
    if len(tiles) == 0:
        raise SystemExit("explicit box selects no cells")
    if len(tiles) > 1:
        raise SystemExit(
            f"explicit box spans tiles {tiles.tolist()}; volumes "
            "crossing a tile seam need the seam-calibrated section "
            "machinery and are refused here by design")
    t = int(tiles[0])
    jj, ii = np.where(inbox[t])
    j0, j1 = int(jj.min()), int(jj.max()) + 1
    i0, i1 = int(ii.min()), int(ii.max()) + 1
    if not (1 <= j0 and j1 <= 89 and 1 <= i0 and i1 <= 89):
        raise SystemExit(
            f"resolved rectangle j {j0}-{j1}, i {i0}-{i1} touches the "
            "tile edge; the rim would need cross-seam faces, refused "
            "here by design")
    zp1 = grid_all.Zp1.values
    k_cells = int(np.argmin(np.abs(-zp1[1:] - depth_m))) + 1
    return t, j0, j1, i0, i1, k_cells


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--region", choices=sorted(REGIONS))
    ap.add_argument("--box", nargs=4, type=float,
                    metavar=("LAT0", "LAT1", "LON0", "LON1"))
    ap.add_argument("--depth-m", type=float)
    ap.add_argument("--year", type=int, default=2010)
    ap.add_argument("--data-root", type=Path,
                    default=Path.home() / "ECCO_V4r4")
    ap.add_argument("--receipt", type=Path, required=True)
    args = ap.parse_args()
    if bool(args.region) == bool(args.box):
        raise SystemExit("exactly one of --region or --box")
    if args.box and args.depth_m is None:
        raise SystemExit("--box requires --depth-m")

    geom_path = args.data_root / GEOM
    grid_all = xr.open_dataset(geom_path)
    if args.region:
        r = REGIONS[args.region]
        tile, (j0, j1), (i0, i1), K = (r["tile"], r["j"], r["i"],
                                       r["k_cells"])
        mode = {"mode": "registered", "region": args.region}
    else:
        lat0, lat1, lon0, lon1 = args.box
        tile, j0, j1, i0, i1, K = resolve_box(
            grid_all, lat0, lat1, lon0, lon1, args.depth_m)
        mode = {"mode": "explicit",
                "requested_box_lat_lon": [lat0, lat1, lon0, lon1],
                "requested_depth_m": args.depth_m}

    grid = grid_all.isel(tile=tile)

    def monthly(s):
        d = xr.open_mfdataset(str(args.data_root / s / "*.nc"),
                              combine="by_coords").isel(tile=tile)
        d = d.sel(time=slice(f"{args.year}-01-01", f"{args.year}-12-31"))
        assert d.sizes["time"] == 12, f"{s}: want 12 months"
        return d

    def snaps(s):
        d = xr.open_mfdataset(str(args.data_root / s / "*.nc"),
                              combine="by_coords").isel(tile=tile)
        d = d.sel(time=slice(f"{args.year}-01-01",
                             f"{args.year + 1}-01-01T23:59"))
        assert d.sizes["time"] == 13, f"{s}: want 13 snapshots"
        return d

    flux, hf = monthly(FLUX), monthly(HF)
    sts, sssh = snaps(SNP_TS), snaps(SNP_SSH)

    hfacc = grid.hFacC.values
    vol = grid.rA.values[None] * grid.drF.values[:, None, None] * hfacc
    mskc = (hfacc > 0).astype(np.float64)
    mskc_dn = np.concatenate([mskc[1:], np.zeros_like(mskc[:1])], axis=0)
    mskb = mskc - mskc_dn

    dts = ((sts.time.values[1:] - sts.time.values[:-1])
           / np.timedelta64(1, "s")).astype(np.float64)
    depth = grid.Depth.values
    with np.errstate(divide="ignore", invalid="ignore"):
        sfac = np.where(depth > 0, 1.0 + sssh.ETAN.values / depth, 1.0)
    stheta = sts.THETA.values * sfac[:, None, :, :]
    g_total = (stheta[1:] - stheta[:-1]) / dts[:, None, None, None]
    g_total = np.nan_to_num(np.where(hfacc[None] > 0, g_total, 0.0))
    lhs = (g_total[:, :K, j0:j1, i0:i1]
           * vol[None, :K, j0:j1, i0:i1]).sum(axis=(1, 2, 3))

    fx = np.nan_to_num(flux.ADVx_TH.values) + np.nan_to_num(flux.DFxE_TH.values)
    fy = np.nan_to_num(flux.ADVy_TH.values) + np.nan_to_num(flux.DFyE_TH.values)
    fr = (np.nan_to_num(flux.ADVr_TH.values)
          + np.nan_to_num(flux.DFrE_TH.values)
          + np.nan_to_num(flux.DFrI_TH.values))
    fr = np.where(hfacc[None] > 0, fr, 0.0)
    frp = np.concatenate([fr, np.zeros_like(fr[:, :1])], axis=1)

    def rim_flux(iw):
        return (fx[:, :K, j0:j1, iw].sum(axis=(1, 2))
                - fx[:, :K, j0:j1, i1].sum(axis=(1, 2))
                + fy[:, :K, j0, i0:i1].sum(axis=(1, 2))
                - fy[:, :K, j1, i0:i1].sum(axis=(1, 2)))

    rim = rim_flux(i0)
    vert = (frp[:, K, j0:j1, i0:i1].sum(axis=(1, 2))
            - frp[:, 0, j0:j1, i0:i1].sum(axis=(1, 2)))

    Z = grid.Z.values
    RF = np.concatenate([grid.Zp1.values[:-1], [np.nan]])
    q1 = R_SW * np.exp(RF[:-1] / ZETA1) + (1 - R_SW) * np.exp(RF[:-1] / ZETA2)
    q2 = R_SW * np.exp(RF[1:] / ZETA1) + (1 - R_SW) * np.exp(RF[1:] / ZETA2)
    zcut = int(np.where(Z < -200)[0][0])
    q1[zcut:] = 0
    q2[zcut - 1:] = 0
    tfl = np.nan_to_num(hf.TFLUX.values)
    qsw = np.nan_to_num(hf.oceQsw.values)
    forc_sub = (q1[None, :, None, None] * (mskc[None] == 1)
                - q2[None, :, None, None] * (mskc_dn[None] == 1)) * qsw[:, None]
    forc_surf = (tfl - (1 - (q1[0] - q2[0])) * qsw) * mskc[0][None]
    forch = np.concatenate([forc_surf[:, None], forc_sub[:, 1:]], axis=1)
    hfac_drf = hfacc * grid.drF.values[:, None, None]
    with np.errstate(divide="ignore", invalid="ignore"):
        g_forc = np.where(hfac_drf[None] > 0,
                          (forch / (RHOCONST * C_P)) / hfac_drf[None], 0.0)
    geo = np.asarray(ecco.read_llc_to_tiles(
        str(args.data_root), "geothermalFlux.bin", less_output=True))[tile]
    with np.errstate(divide="ignore", invalid="ignore"):
        g_geo = np.where(hfac_drf[None] > 0,
                         ((geo[None, None] * mskb[None])
                          / (RHOCONST * C_P)) / hfac_drf[None], 0.0)
    vw = vol[None, :K, j0:j1, i0:i1]
    forc = ((g_forc + g_geo)[:, :K, j0:j1, i0:i1] * vw).sum(axis=(1, 2, 3))
    geo_int = (g_geo[:, :K, j0:j1, i0:i1] * vw).sum(axis=(1, 2, 3))

    V = float(vol[:K, j0:j1, i0:i1].sum())
    largest = float(np.abs(np.vstack([lhs, rim, vert, forc])).max())
    res = lhs - (rim + vert + forc)

    def bars(r):
        return (float(np.abs(r).max() / V), float(np.abs(r).max() / largest))

    a_ok, rel_ok = bars(res)
    if a_ok > ABS_BAR or rel_ok > REL_BAR:
        raise SystemExit(
            f"correct formulation FAILED its own bars (abs {a_ok:.2e}, "
            f"rel {rel_ok:.2e}); no receipt written")

    wet = hfacc[:K, j0:j1, i0:i1] > 0
    bottom_cells = int(mskb[:K, j0:j1, i0:i1].sum())

    evidence = []
    rim_shift = rim_flux(i0 + 1)
    for name, r in [
        ("geothermal-omitted", res + geo_int),
        ("rim-west-face-shifted", lhs - (rim_shift + vert + forc)),
        ("vertical-face-sign-flipped", lhs - (rim - vert + forc)),
        ("vertical-faces-omitted", lhs - (rim + forc)),
    ]:
        a, rel = bars(r)
        caught = a > ABS_BAR or rel > REL_BAR
        entry = {"mutation": name, "residual_per_volume": a,
                 "residual_relative": rel, "caught": bool(caught)}
        if not caught:
            if name == "geothermal-omitted":
                entry["applicable"] = False
                entry["note"] = (
                    f"volume contains {bottom_cells} bottom cells; the "
                    "geothermal term is below both bars here, so its "
                    "omission is not demonstrable in this volume")
            else:
                raise SystemExit(
                    f"structural mutation {name} was NOT caught (abs "
                    f"{a:.2e}, rel {rel:.2e}); the test cannot fail, "
                    "so it is not evidence; no receipt written")
        evidence.append(entry)
    yc = grid.YC.values[j0:j1, i0:i1]
    xc = grid.XC.values[j0:j1, i0:i1]
    code = Path(__file__).read_bytes()
    receipt = {
        "run_id": (dt.datetime.now(dt.timezone.utc)
                   .strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:8]),
        "computation": "ecco-regional-heat-budget",
        "code_sha256": hashlib.sha256(code).hexdigest(),
        "generated_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "bound_parameters": {
            **mode, "year": args.year,
            "collections": [FLUX, HF, SNP_TS, SNP_SSH],
            "geothermal_source": "geothermalFlux.bin, ECCO tutorial "
                                 "distribution, not a PO.DAAC collection",
            "rhoConst_kg_m3": RHOCONST, "Cp_J_kg_K": C_P,
            "sw_R": R_SW, "sw_zeta1_m": ZETA1, "sw_zeta2_m": ZETA2,
            "abs_bar_degC_s": ABS_BAR, "rel_bar": REL_BAR,
        },
        "resolved_volume": {
            "tile": tile, "j": [j0, j1], "i": [i0, i1], "k_cells": K,
            "depth_face_m": float(-grid.Zp1.values[K]),
            "lat_extent": [float(yc.min()), float(yc.max())],
            "lon_extent": [float(xc.min()), float(xc.max())],
            "wet_cells": int(wet.sum()),
            "bottom_cells": bottom_cells,
            "volume_m3": V,
            "mask_sha256": hashlib.sha256(
                wet.astype(np.uint8).tobytes()).hexdigest(),
            "geometry_sha256": hashlib.sha256(
                geom_path.read_bytes()).hexdigest(),
        },
        "results": {
            "months": int(res.size),
            "residual_per_volume_max_degC_s": a_ok,
            "residual_relative_max": rel_ok,
            "largest_term_degC_m3_s": largest,
            "monthly_residual_per_volume_degC_s":
                [float(x) for x in np.abs(res) / V],
        },
        "mutation_evidence": evidence,
        "caveats": {
            "free_surface": "s* scaling from bracketing snapshots, "
                            "inherited from the signed pointwise budget",
            "single_tile_v1": "the volume lies within one tile "
                              "interior; seam-crossing volumes are "
                              "refused until the seam-calibrated "
                              "section machinery lands",
            "mask_disclosure": "no oracle checks that this mask is the "
                               "water the user meant; the resolved "
                               "extent above is the disclosure",
        },
    }
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.write_text(json.dumps(receipt, indent=2) + "\n")
    label = mode.get("region") or "explicit box"
    print(f"run {receipt['run_id']}: {label}, year {args.year}")
    print(f"  volume tile {tile}, j {j0}-{j1}, i {i0}-{i1}, "
          f"0-{-grid.Zp1.values[K]:.0f} m; {int(wet.sum()):,} wet cells, "
          f"{V:.4e} m3")
    print(f"  residual per volume max {a_ok:.3e} degC/s "
          f"(bar {ABS_BAR:.0e}); relative max {rel_ok:.3e} "
          f"(bar {REL_BAR:.0e})")
    ncaught = sum(1 for e in evidence if e["caught"])
    na = [e["mutation"] for e in evidence if not e.get("caught")]
    print(f"  mutations caught: {ncaught}/4"
          + (f" ({', '.join(na)} not applicable here)" if na else ""))
    print(f"  receipt -> {args.receipt}")


if __name__ == "__main__":
    main()
