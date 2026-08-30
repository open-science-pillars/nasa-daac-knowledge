---
type: Data Collection
title: Ocean velocity
description: "The velocity family of the V4r4 estimate: UVEL, VVEL, and the mass-weighted vertical component on native and interpolated grids."
tags: [ecco, v4r4, ocean-circulation]
resource: https://podaac.jpl.nasa.gov/dataset/ECCO_L4_OCEAN_VEL_LLC0090GRID_MONTHLY_V4R4
status: draft
generated: { by: claude-code/fable-5, at: 2026-08-30T20:15:00Z }
stale_after: 2027-01-04
sources:
  - id: podaac-landing
    resource: https://podaac.jpl.nasa.gov/dataset/ECCO_L4_OCEAN_VEL_LLC0090GRID_MONTHLY_V4R4
    title: PO.DAAC dataset landing page
  - id: cmr-sweep
    resource: all ECCO_L4_*V4R4* collections in CMR (provider POCLOUD)
    title: CMR ShortName sweep, tools/verify_cmr.py
  - id: variable-catalog
    resource: https://github.com/open-science-pillars/ocean-science/blob/main/skills/ecco/references/variable-catalog.md
    title: OSP ECCO variable catalog (sweep of 2026-07-04)
    author: human:PaulMRamirez
verified: { by: process:cmr-shortname-sweep, at: 2026-08-30T20:07:19Z }
---

# Ocean velocity

Ocean velocity from the ECCO V4r4 ocean and sea-ice state estimate on
the native llc90 grid and the interpolated 0.5 degree grid, monthly and
daily means.[^podaac-landing] This is the velocity ShortName family; the
OBP collections are ocean bottom pressure, a different product (the
naming confusion this distinction exists to prevent).[^variable-catalog]
The interpolated collections carry east/north velocity components whose
exact variable names are confirmed at granule verification (manifest
note).

# Schema

| Variable | Units | Grid point | Description | Provenance |
|---|---|---|---|---|
| `UVEL` | m s-1 | w face | Ocean velocity, model x component | user guide (verify at first load) |
| `VVEL` | m s-1 | s face | Ocean velocity, model y component | user guide (verify at first load) |
| `WVELMASS` | m s-1 | vertical face | Mass-weighted vertical velocity | user guide (verify at first load) |

# Variants

All four ShortNames verified in CMR by the 2026-08-30 sweep.[^cmr-sweep]

- `ECCO_L4_OCEAN_VEL_LLC0090GRID_MONTHLY_V4R4`: native llc90, monthly mean.
- `ECCO_L4_OCEAN_VEL_LLC0090GRID_DAILY_V4R4`: native llc90, daily mean.
- `ECCO_L4_OCEAN_VEL_05DEG_MONTHLY_V4R4`: 0.5 degree interpolated, monthly mean; display and comparison, not budgets.
- `ECCO_L4_OCEAN_VEL_05DEG_DAILY_V4R4`: 0.5 degree interpolated, daily mean; display and comparison, not budgets.

[^podaac-landing]: PO.DAAC dataset landing page
[^cmr-sweep]: CMR ShortName sweep, tools/verify_cmr.py
[^variable-catalog]: OSP ECCO variable catalog (sweep of 2026-07-04)
