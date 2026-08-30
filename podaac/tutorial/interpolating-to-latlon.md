---
type: convention
title: "Interpolating llc90 fields to regular lat-lon grids"
description: "Tutorial-companion facts: tiles 7-12 are rotated 90 degrees counter-clockwise relative to tiles 0-5; resample_to_latlon handles scalars; vectors have their own section and their own trap."
tags: [ecco, tutorial-companion, regridding, llc90]
generated: { by: claude-code/fable-5, at: 2026-08-30T21:45:00Z }
status: draft
stale_after: 2027-01-04
sources:
  - id: tut-interp
    resource: https://ecco-v4-python-tutorial.readthedocs.io/ECCO_v4_Interpolating_Fields_to_LatLon_Grid.html
    title: "ECCO v4 Python Tutorial: Interpolating fields from the model llc grid to a regular lat lon grid"
    author: team:ecco-consortium
---

# Interpolating llc90 fields to regular lat-lon grids

The chapter's load-bearing geometry fact: **tiles 7-12 of the llc90
grid are rotated 90 degrees counter-clockwise relative to tiles
0-5**.[^tut-interp] Scalar fields map to regular lat-lon grids of
arbitrary resolution with `resample_to_latlon` (nearest-neighbor and
bin-average demonstrated, each with its own tradeoffs); vector fields
get their own section because the rotation makes component-wise
treatment wrong.[^tut-interp] The traps this chapter walks past are
owned by their concepts: interpolated fields do not conserve and close
no budgets
([ecco-native-vs-regridded](../gotchas/ecco-native-vs-regridded.md)),
and native velocity components are grid-relative until rotated
([ecco-vector-orientation](../gotchas/ecco-vector-orientation.md)).

[^tut-interp]: ECCO v4 Python Tutorial: Interpolating fields from the model llc grid to a regular lat lon grid
