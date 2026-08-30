---
type: convention
title: "Coordinates and dimensions of ECCO v4 NetCDF files"
description: "Tutorial-companion facts: coordinate labels place every field on the Arakawa C-grid; the dimension coordinates are i, j, k, tile, and time."
tags: [ecco, tutorial-companion, grid, netcdf]
generated: { by: claude-code/fable-5, at: 2026-08-30T21:40:00Z }
status: draft
stale_after: 2027-01-04
sources:
  - id: tut-coords
    resource: https://ecco-v4-python-tutorial.readthedocs.io/ECCO_v4_Coordinates_and_Dimensions_of_ECCOv4_NetCDF_files.html
    title: "ECCO v4 Python Tutorial: Coordinates and Dimensions of ECCOv4 NetCDF files"
    author: team:ecco-consortium
---

# Coordinates and dimensions of ECCO v4 NetCDF files

ECCO v4 fields carry coordinate labels that state where each field
sits on the Arakawa C-grid; the dimension coordinates are `i`, `j`,
`k`, `tile`, and `time`, with staggered-grid variants (the `_g` and
`_l`/`_p1` flavors) marking face and interface positions, which is how
a consumer tells a center quantity from an edge flux without reading
code.[^tut-coords] The granule-verified placement of every authored
variable is recorded per family in
[the fields layer](../fields/ecco-v4r4/index.md) (the Schema grid-point
columns), and the geometry inventory on
[the geometry concept](../fields/ecco-v4r4/geometry.md); this
companion carries the chapter's naming convention itself.

[^tut-coords]: ECCO v4 Python Tutorial: Coordinates and Dimensions of ECCOv4 NetCDF files
