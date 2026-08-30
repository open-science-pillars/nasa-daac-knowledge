---
type: convention
title: "Combining ECCO datasets centered on different grid points"
description: "Tutorial-companion facts: c-, u-, and v-centered variables merge into one Dataset with xarray.merge, the grid parameters alongside."
tags: [ecco, tutorial-companion, loading, grid]
generated: { by: claude-code/fable-5, at: 2026-08-30T21:45:00Z }
status: draft
stale_after: 2027-01-04
sources:
  - id: tut-combine
    resource: https://ecco-v4-python-tutorial.readthedocs.io/ECCO_v4_Combining_Multiple_Datasets.html
    title: "ECCO v4 Python Tutorial: Combining multiple Datasets"
    author: team:ecco-consortium
---

# Combining ECCO datasets centered on different grid points

ECCO state estimate variables arrive in datasets centered on different
C-grid coordinates (the chapter's example merges c-centered SSH with
the u- and v-centered advective fluxes) and combine into one Dataset
via `xarray.merge`, with the model grid dataset merged in the same
way; the merged object keeps each variable's own dimension coordinates
side by side.[^tut-combine] The placement vocabulary is
[the coordinates companion](coordinates-and-dimensions.md); geometry
merging as standing practice is recorded on
[the geometry concept](../fields/ecco-v4r4/geometry.md).

[^tut-combine]: ECCO v4 Python Tutorial: Combining multiple Datasets
