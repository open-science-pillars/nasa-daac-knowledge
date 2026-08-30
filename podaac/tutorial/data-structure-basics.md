---
type: convention
title: "ECCO NetCDF structure: datasets, granules, and the xarray objects"
description: "Tutorial-companion facts: each dataset carries a few variables, one file per time coordinate is a granule, and the Dataset/DataArray objects are the working structures."
tags: [ecco, tutorial-companion, netcdf, structure]
generated: { by: claude-code/fable-5, at: 2026-08-30T21:40:00Z }
status: draft
stale_after: 2027-01-04
sources:
  - id: tut-structure
    resource: https://ecco-v4-python-tutorial.readthedocs.io/ECCO_v4_data_structure_basics.html
    title: "ECCO v4 Python Tutorial: The Dataset and DataArray objects"
    author: team:ecco-consortium
---

# ECCO NetCDF structure: datasets, granules, and the xarray objects

The v4r4 files are NetCDF; output is organized as datasets that each
contain a few variables, each dataset consists of files corresponding
to a single time coordinate (monthly mean, daily mean, or snapshot),
and each single-time file is called a granule.[^tut-structure] The
working structures are xarray's Dataset and DataArray, whose anatomy
(dimensions, coordinates, data variables, attributes) the chapter
walks in detail.[^tut-structure] The collection inventory itself lives
in [the fields layer](../fields/ecco-v4r4/index.md) and the product
identity on [the dataset concept](../datasets/ecco-v4r4.md); this
companion carries only the chapter's structural vocabulary.

[^tut-structure]: ECCO v4 Python Tutorial: The Dataset and DataArray objects
