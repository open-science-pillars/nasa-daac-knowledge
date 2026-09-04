---
type: convention
title: "Loading state estimate fields on the native grid"
description: "Tutorial-companion facts: cloud-distributed NetCDF since March 2023, one granule per time, open_mfdataset for multiples, Dask for the very large."
tags: [ecco, tutorial-companion, access, loading]
generated: { by: claude-code/fable-5, at: 2026-08-30T21:40:00Z }
status: draft
stale_after: 2027-01-04
sources:
  - id: tut-load-fields
    resource: https://ecco-v4-python-tutorial.readthedocs.io/ECCO_v4_Loading_the_ECCOv4_state_estimate_fields_on_the_native_model_grid.html
    title: "ECCO v4 Python Tutorial: Loading the ECCOv4 state estimate fields on the native model grid"
    author: team:ecco-consortium
---

# Loading state estimate fields on the native grid

As of March 2023 the v4r4 state estimate fields are distributed
through PO.DAAC in the NASA Earthdata Cloud as NetCDF, one file per
time step per dataset; the chapter's load routes are `open_dataset`
for a single granule, `open_mfdataset` for multiples, `xarray.merge`
for combining, a preprocess function for spatial subsetting at open
time, and Dask for very large requests.[^tut-load-fields] The
exact-ShortName discipline and the access peculiarities are owned by
[the dataset concept](../datasets/ecco-v4r4.md); dataset-to-variable
lookup by [the fields layer](../fields/ecco-v4r4/index.md).

[^tut-load-fields]: ECCO v4 Python Tutorial: Loading the ECCOv4 state estimate fields on the native model grid
