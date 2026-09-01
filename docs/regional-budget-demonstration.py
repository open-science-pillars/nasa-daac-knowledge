# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy", "xarray", "netCDF4", "dask", "ecco_v4_py"]
# ///
"""Demonstration behind section 1 of regional-budget-design.md.

NOT A SANCTIONED COMPUTATION. No receipt, no attester, no signature.
This exists so the measured numbers in the design document can be
reproduced and disputed.

It closes a heat budget over a control volume by comparing THREE
INDEPENDENT collections, so that agreement is evidence rather than
arithmetic:
  tendency   from the temperature/salinity and sea-surface-height
             SNAPSHOTS (THETA, ETAN)
  transport  from the three-dimensional flux collection, read as RAW
             FACE FLUXES at the volume's six boundary faces and never
             derived from the divergence field
  forcing    from the surface flux collection (TFLUX, oceQsw) plus
             geothermal at bottom wet cells

The mutation controls at the end sabotage the implementation four ways
and report whether each is caught. A test that cannot fail is not
evidence. The geothermal case is the instructive one: it passes an
absolute tolerance and is caught only by a relative one.

Formulation mirrors the signed pointwise heat budget exactly.
Requires the local fixture cache; retrieval is a separate step.
"""
import numpy as np, xarray as xr, ecco_v4_py as ecco
from pathlib import Path

RHOCONST, C_P = 1029.0, 3994.0
R_SW, ZETA1, ZETA2 = 0.62, 0.6, 20.0
root = Path.home() / "ECCO_V4r4"
TILE, YEAR = 1, 2010
J0, J1, I0, I1, K = 20, 60, 20, 60, 20      # the control volume

grid = xr.open_dataset(root/"geometry/GRID_GEOMETRY_ECCO_V4r4_native_llc0090.nc").isel(tile=TILE)
def monthly(s):
    d = xr.open_mfdataset(str(root/s/"*.nc"), combine="by_coords").isel(tile=TILE)
    return d.sel(time=slice(f"{YEAR}-01-01", f"{YEAR}-12-31"))
def snaps(s):
    d = xr.open_mfdataset(str(root/s/"*.nc"), combine="by_coords").isel(tile=TILE)
    return d.sel(time=slice(f"{YEAR}-01-01", f"{YEAR+1}-01-01T23:59"))
flux = monthly("ECCO_L4_OCEAN_3D_TEMPERATURE_FLUX_LLC0090GRID_MONTHLY_V4R4")
hf   = monthly("ECCO_L4_HEAT_FLUX_LLC0090GRID_MONTHLY_V4R4")
sts  = snaps("ECCO_L4_TEMP_SALINITY_LLC0090GRID_SNAPSHOT_V4R4")
sssh = snaps("ECCO_L4_SSH_LLC0090GRID_SNAPSHOT_V4R4")

hfacc = grid.hFacC.values
vol = grid.rA.values[None]*grid.drF.values[:,None,None]*hfacc
mskc = (hfacc > 0).astype(np.float64)
mskc_dn = np.concatenate([mskc[1:], np.zeros_like(mskc[:1])], axis=0)
mskb = mskc - mskc_dn                                   # bottom wet cell
print(f"bottom cells inside the volume: {int(mskb[:K, J0:J1, I0:I1].sum())} "
      f"(0 means geothermal contributes nothing here)")

dt = ((sts.time.values[1:]-sts.time.values[:-1])/np.timedelta64(1,"s")).astype(np.float64)
depth = grid.Depth.values
with np.errstate(divide="ignore", invalid="ignore"):
    sfac = np.where(depth > 0, 1.0 + sssh.ETAN.values/depth, 1.0)
stheta = sts.THETA.values * sfac[:, None, :, :]
g_total = (stheta[1:]-stheta[:-1])/dt[:,None,None,None]
g_total = np.nan_to_num(np.where(hfacc[None] > 0, g_total, 0.0))   # land -> 0, not NaN

# --- LHS: volume-integrated tendency, from SNAPSHOTS
lhs = (g_total[:, :K, J0:J1, I0:I1]*vol[None,:K,J0:J1,I0:I1]).sum(axis=(1,2,3))

# --- RHS part 1: transport through the control volume's SIX faces, from FLUX
fx = np.nan_to_num(flux.ADVx_TH.values)+np.nan_to_num(flux.DFxE_TH.values)
fy = np.nan_to_num(flux.ADVy_TH.values)+np.nan_to_num(flux.DFyE_TH.values)
fr = np.nan_to_num(flux.ADVr_TH.values)+np.nan_to_num(flux.DFrE_TH.values)+np.nan_to_num(flux.DFrI_TH.values)
fr = np.where(hfacc[None] > 0, fr, 0.0)
frp = np.concatenate([fr, np.zeros_like(fr[:,:1])], axis=1)      # pad bottom
rim = (fx[:, :K, J0:J1, I0].sum(axis=(1,2)) - fx[:, :K, J0:J1, I1].sum(axis=(1,2))
     + fy[:, :K, J0, I0:I1].sum(axis=(1,2)) - fy[:, :K, J1, I0:I1].sum(axis=(1,2)))
vert = (frp[:, K, J0:J1, I0:I1].sum(axis=(1,2)) - frp[:, 0, J0:J1, I0:I1].sum(axis=(1,2)))

# --- RHS part 2: surface forcing, from HEAT FLUX
Z = grid.Z.values; RF = np.concatenate([grid.Zp1.values[:-1],[np.nan]])
q1 = R_SW*np.exp(RF[:-1]/ZETA1)+(1-R_SW)*np.exp(RF[:-1]/ZETA2)
q2 = R_SW*np.exp(RF[1:]/ZETA1)+(1-R_SW)*np.exp(RF[1:]/ZETA2)
zcut = int(np.where(Z < -200)[0][0]); q1[zcut:] = 0; q2[zcut-1:] = 0
tflux = np.nan_to_num(hf.TFLUX.values); qsw = np.nan_to_num(hf.oceQsw.values)
forc_sub = (q1[None,:,None,None]*(mskc[None]==1) - q2[None,:,None,None]*(mskc_dn[None]==1))*qsw[:,None]
forc_surf = (tflux-(1-(q1[0]-q2[0]))*qsw)*mskc[0][None]
forch = np.concatenate([forc_surf[:,None], forc_sub[:,1:]], axis=1)
hfac_drf = hfacc*grid.drF.values[:,None,None]
with np.errstate(divide="ignore", invalid="ignore"):
    g_forc = np.where(hfac_drf[None] > 0, (forch/(RHOCONST*C_P))/hfac_drf[None], 0.0)
geo = np.asarray(ecco.read_llc_to_tiles(str(root), "geothermalFlux.bin", less_output=True))[TILE]
geo3d = geo[None, None]*mskb[None]
with np.errstate(divide="ignore", invalid="ignore"):
    g_geo = np.where(hfac_drf[None] > 0, (geo3d/(RHOCONST*C_P))/hfac_drf[None], 0.0)
g_forc = g_forc + g_geo
forc = (g_forc[:, :K, J0:J1, I0:I1]*vol[None,:K,J0:J1,I0:I1]).sum(axis=(1,2,3))

V = vol[:K, J0:J1, I0:I1].sum()
res = lhs - (rim + vert + forc)
print(f"\ncontrol volume: tile {TILE}, j {J0}-{J1}, i {I0}-{I1}, k 0-{K}")
print(f"volume {V:.4e} m3, wet cells {(hfacc[:K,J0:J1,I0:I1]>0).sum():,}\n")
print(f"{'month':>6s} {'tendency':>13s} {'rim':>13s} {'top/bot':>12s} {'forcing':>12s} {'residual':>11s} {'per m3 (degC/s)':>17s}")
for m in range(12):
    print(f"{m+1:6d} {lhs[m]:13.5e} {rim[m]:13.5e} {vert[m]:12.4e} {forc[m]:12.4e} {res[m]:11.3e} {res[m]/V:17.3e}")
norm = np.abs(res/V)
print(f"\nregional residual normalized by volume: max {norm.max():.3e} degC/s")
print(f"the signed POINTWISE bar for this budget: 1e-10 degC/s")
print(f"VERDICT: {'CLOSES within the signed bar' if norm.max() <= 1e-10 else 'DOES NOT CLOSE'}")

print("\n=== MUTATION CONTROLS: can this test fail? ===")
largest = np.abs(np.vstack([lhs, rim, vert, forc])).max()
def verdict(r, label):
    a = np.abs(r/V).max(); rel = np.abs(r).max()/largest
    print(f"{label:34s} abs {a:9.2e} degC/s  rel {rel:9.2e}   "
          f"{'passes both' if (a<=1e-10 and rel<=1e-6) else 'CAUGHT'}")
verdict(res, "correct implementation")
geo_int = (g_geo[:, :K, J0:J1, I0:I1]*vol[None,:K,J0:J1,I0:I1]).sum(axis=(1,2,3))
verdict(res + geo_int, "geothermal omitted")
rim_shift = (fx[:, :K, J0:J1, I0+1].sum(axis=(1,2)) - fx[:, :K, J0:J1, I1].sum(axis=(1,2))
           + fy[:, :K, J0, I0:I1].sum(axis=(1,2)) - fy[:, :K, J1, I0:I1].sum(axis=(1,2)))
verdict(lhs-(rim_shift+vert+forc), "rim west face shifted one cell")
verdict(lhs-(rim-vert+forc), "vertical face sign flipped")
verdict(lhs-(rim+forc), "vertical faces omitted")
