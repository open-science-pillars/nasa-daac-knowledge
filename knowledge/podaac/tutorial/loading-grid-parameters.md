---
type: convention
title: "Loading the native model grid parameters"
description: "Tutorial-companion facts: the grid is one NetCDF file under ECCO_L4_GEOMETRY_LLC0090GRID_V4R4, opened with plain open_dataset."
tags: [ecco, tutorial-companion, grid, access]
generated: { by: claude-code/fable-5, at: 2026-08-30T21:40:00Z }
status: draft
stale_after: 2027-01-04
sources:
  - id: tut-load-grid
    resource: https://ecco-v4-python-tutorial.readthedocs.io/ECCO_v4_Loading_the_ECCOv4_native_model_grid_parameters.html
    title: "ECCO v4 Python Tutorial: Loading the ECCOv4 native model grid parameters"
    author: team:ecco-consortium
---

# Loading the native model grid parameters

The model grid parameters are provided as a single NetCDF file under
ShortName `ECCO_L4_GEOMETRY_LLC0090GRID_V4R4`, downloadable via the
ecco_access package and opened with xarray's plain `open_dataset`
(single file, no multi-file machinery needed).[^tut-load-grid] The
granule-verified variable inventory, the coordinate note, and the
static-collection fetch quirk are owned by
[the geometry concept](../fields/ecco-v4r4/geometry.md); this
companion records the chapter's route.

[^tut-load-grid]: ECCO v4 Python Tutorial: Loading the ECCOv4 native model grid parameters
