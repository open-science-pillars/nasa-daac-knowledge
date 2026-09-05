---
type: recipe
title: "Reconstruct the current from density alone: thermal wind from a level of no motion"
description: "The route from a density field to a current: thermal-wind shear in the tile frame, integrated from a 3000 m level of no motion on the model's own levels, then scored two ways against the model's real current so the cost of the assumption is part of the answer."
tags: [ecco, thermal-wind, geostrophy, level-of-no-motion, recipe, native-grid]
inputs: "ECCO_L4_DENS_STRAT_PRESS_LLC0090GRID_MONTHLY_V4R4 (RHOAnoma); ECCO_L4_OCEAN_VEL_LLC0090GRID_MONTHLY_V4R4 (UVEL, VVEL) for the same month; the geometry granule (dxC, dyC, Depth, YC, Z, hFacC, hFacW, hFacS)"
expected: "Month 2009-12 (measured 2026-09-05): over the open-ocean interior (10-55 deg, seafloor deeper than 3000 m, wet at the reference level, 19,315 columns), 100-1000 m absolute r = 0.9900 with RMS error 15 percent of the model current, relative r = 0.9989 with 5 percent; shear r = 0.9757; below the reference level absolute r = 0.152 with RMS error 108 percent against relative r = 0.978; median model speed at the reference level 3.6 mm/s"
expected_uncertainty: "Two scores, never one for the other: the absolute score is the reconstruction's skill, the relative score is the shear's skill, and their gap is the cost of assuming no motion at 3000 m. The deep band is where that cost lands (absolute r 0.15); quoting the relative 0.98 there answers a question nobody asked. The top 100 m has no thermal-wind skill (shear r 0.03) because mixed-layer shear is not geostrophic; where the winter mixed layer is deeper than about 100 m the failure follows it down. A fill value read as a number, or a face-masked velocity averaged without its own mask, ruins the gradient silently: r near zero with no error"
generated: { by: claude-code/fable-5, at: 2026-09-05T16:20:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-05T16:39:22Z }
status: stable
stale_after: 2027-03-05
sources:
  - id: attested-computation
    resource: ../computations/ecco-thermal-wind-reconstruction.md
    title: "The attested computation this recipe walks: two-score contract, reference run, where the shear is density-controlled"
  - id: geostrophic-balance
    resource: ecco-geostrophic-balance.md
    title: "Recipe, geostrophic balance: the shear identity between two depths that this recipe integrates through the whole column"
  - id: tutorial-thermal-wind
    resource: https://ecco-v4-python-tutorial.readthedocs.io/Thermal_wind.html
    title: "ECCO v4 Python tutorial, thermal wind: the construction on the Atlantic 26N transect and the level-of-no-motion caveat"
  - id: density-factor
    resource: ../gotchas/ecco-geostrophic-density-factor.md
    title: "Gotcha: rho is rho0 plus RHOAnoma, and the anomaly is small enough that float32 arithmetic on the sum rounds it"
  - id: vector-orientation
    resource: ../gotchas/ecco-vector-orientation.md
    title: "Gotcha: velocities and gradients live in each tile's local frame; east and north need the CS, SN rotation"
---

# Reconstruct the current from density alone: thermal wind from a level of no motion

The geostrophic-balance recipe checks a shear identity between two
depths.[^geostrophic-balance] This recipe integrates that identity
through the whole column and asks the question a density field can be
asked: how much of the current does it recover? The construction is
the tutorial's, on every open-ocean column instead of one
transect.[^tutorial-thermal-wind]

**Build the shear in the tile frame.** Density is rho0 plus RHOAnoma,
promoted to float64 before the sum, because the horizontal gradient of
the anomaly is the whole signal and float32 on 1029 plus a small
number rounds it sixty times coarser than the granule
stores.[^density-factor] Centered differences at tracer points with the
tile's own dxC and dyC give drho/dx and drho/dy; du/dz is g over f rho
times drho/dy, dv/dz is minus g over f rho times drho/dx. Stay in the
tile frame for the whole calculation and compare the model's current
in the same frame; rotate to east and north only for a map, with CS
and SN.[^vector-orientation]

**Read every granule through a fill-aware loader.** ECCO marks land
and dry faces with a fill value near 1E+37, not NaN, and a plain array
conversion of the netCDF4 masked array keeps it. One fill reaching a
difference does not raise; it produces a gradient of 1E+37 that the
integration carries into every level above and below, and the score
collapses to zero with no error message. Mask UVEL with hFacW and VVEL
with hFacS before averaging them to tracer points; masking with hFacC
leaves fill at wet cells whose face is dry.

**Integrate from the level of no motion.** Set the current to zero at
the model level nearest 3000 m (level 41, 2990 m in ECCO v4r4) and
integrate the shear upward and downward with the trapezoid rule on the
model's own level spacing. Columns that are dry at the reference level
are out of the domain, not zero-filled: the assumption has no meaning
where there is no water to be at rest.

**Score it twice, and report the reference speed.** The absolute score
compares the reconstruction with the model's current; the relative
score compares it with the model's current minus the model's own
current at the reference level. The first is the answer to the
question; the second is the shear's skill with the assumption removed;
the gap between them, and the model's median speed at the reference
level (3.6 mm/s in the reference month, 11 mm/s at the 90th
percentile), is what assuming no motion at 3000 m cost. Report all
four depth bands. In the reference month the thermocline band
(100-1000 m) reaches absolute r 0.99 with 15 percent RMS error, and
the band below the reference reaches absolute r 0.15 with 108 percent:
density alone recovers the thermocline current and not the deep one,
and the second half of that sentence is the required part. The
attested form refuses a receipt that drops either score, any band, or
the reference speed.[^attested-computation]

**Where it fails, and why.** The top 100 m has no thermal-wind skill
(shear r 0.03): mixed-layer shear is wind-driven and convective, not
geostrophic. Ask for the per-cell shear-skill field (`--fields`) and
the failure is not a fixed surface layer but the winter mixed layer:
a coherent band of zero skill across the winter North Pacific and
North Atlantic near 30 to 45 degrees where the mixed layer reaches
past 100 m, and near-perfect skill across the subtropical gyres and
the whole summer hemisphere. A "where does density control the shear"
map is that field, and it changes with the season.

**Run the sanctioned form.** `uv run
references/computations/ecco_thermal_wind_reconstruction.py --month
YYYY-MM --receipt tw.json --fields tw_fields.npz`, then `uv run
references/attesters/thermal_wind_check.py tw.json`. Every script in
this bundle carries its own dependencies in its header, so `uv run`
on the script file resolves netCDF4 and numpy by itself; `python
script.py` or `uv run python script.py` skips that header and fails on
the first import.

[^attested-computation]: computations/ecco-thermal-wind-reconstruction.md, contract, reference run, and the mixed-layer finding
[^geostrophic-balance]: recipes/ecco-geostrophic-balance.md, the two-depth shear identity
[^tutorial-thermal-wind]: ECCO v4 Python tutorial, Thermal_wind chapter
[^density-factor]: gotchas/ecco-geostrophic-density-factor.md
[^vector-orientation]: gotchas/ecco-vector-orientation.md
