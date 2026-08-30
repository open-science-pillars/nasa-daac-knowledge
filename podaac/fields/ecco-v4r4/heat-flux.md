---
type: Data Collection
title: Ocean and sea-ice surface heat fluxes
description: "The surface heat-flux family of the V4r4 estimate: TFLUX and the shortwave component that force the heat budget, with net flux and forcing components."
tags: [ecco, v4r4, ocean-heat-budget]
resource: https://podaac.jpl.nasa.gov/dataset/ECCO_L4_HEAT_FLUX_LLC0090GRID_MONTHLY_V4R4
status: draft
generated: { by: claude-code/fable-5, at: 2026-08-30T20:15:00Z }
stale_after: 2027-01-04
sources:
  - id: podaac-landing
    resource: https://podaac.jpl.nasa.gov/dataset/ECCO_L4_HEAT_FLUX_LLC0090GRID_MONTHLY_V4R4
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

# Ocean and sea-ice surface heat fluxes

Ocean and sea-ice surface heat fluxes from the ECCO V4r4 estimate on
the native llc90 grid and the interpolated 0.5 degree grid, monthly and
daily means.[^podaac-landing] `TFLUX` and `oceQsw` are the heat-budget
forcing terms; EXF forcing components ride in this family and are
enumerated at granule verification (manifest
note).[^variable-catalog] The geothermal flux is not in this family or
any PO.DAAC gridded collection; it is a static model input in the
ancillary data, and deep heat budgets fail without it
(see Known issues).[^variable-catalog]

# Schema

| Variable | Units | Grid point | Description | Provenance |
|---|---|---|---|---|
| `TFLUX` | W m-2 | c center | Total heat flux into the ocean surface; heat-budget forcing term | user guide (verify at first load) |
| `oceQsw` | W m-2 | c center | Net shortwave radiative flux; penetrates with the two-band profile | user guide (verify at first load) |
| `oceQnet` | W m-2 | c center | Net surface heat flux | user guide (verify at first load) |

# Variants

All four ShortNames verified in CMR by the 2026-08-30 sweep.[^cmr-sweep]

- `ECCO_L4_HEAT_FLUX_LLC0090GRID_MONTHLY_V4R4`: native llc90, monthly mean.
- `ECCO_L4_HEAT_FLUX_LLC0090GRID_DAILY_V4R4`: native llc90, daily mean.
- `ECCO_L4_HEAT_FLUX_05DEG_MONTHLY_V4R4`: 0.5 degree interpolated, monthly mean; display and comparison, not budgets.
- `ECCO_L4_HEAT_FLUX_05DEG_DAILY_V4R4`: 0.5 degree interpolated, daily mean; display and comparison, not budgets.

# Known issues

Deep and full-depth heat budgets need the geothermal flux, which no
PO.DAAC collection carries
([ecco-geothermal-flux](../../gotchas/ecco-geothermal-flux.md)).

[^podaac-landing]: PO.DAAC dataset landing page
[^cmr-sweep]: CMR ShortName sweep, tools/verify_cmr.py
[^variable-catalog]: OSP ECCO variable catalog (sweep of 2026-07-04)
