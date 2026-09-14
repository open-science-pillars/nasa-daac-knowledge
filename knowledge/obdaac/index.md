---
okf_version: "0.2"
---

# obdaac bundle (OB.DAAC ocean color)

The OB.DAAC knowledge bundle: the Ocean Biology Distributed Active
Archive Center's ocean color products (the level 3 chlorophyll-a grids
from MODIS-Aqua and PACE OCI first), as reviewable concepts with
sources, statuses and steward sign-off. OKF v0.2 conformant
(okf_version: "0.2"; the vendored spec text lives in marketplace
docs/upstream). Every concept is a draft until the steward promotes it
after review, and a confirmation from the OB.DAAC or the Ocean Biology
Processing Group is invited on each and never required.

What this bundle claims, for the people who know the data: [DIGEST.md](DIGEST.md).

## datasets

- [MODIS-Aqua Level 3 mapped chlorophyll-a (OB.DAAC, reprocessing R2022)](datasets/modis-aqua-l3-chlorophyll.md), status: draft
- [PACE OCI Level 3 mapped chlorophyll-a (OB.DAAC, the BGC suite, version 3.2)](datasets/pace-oci-l3-chlorophyll.md), status: draft

## gotchas

- [The standard chlor_a is two algorithms blended between 0.25 and 0.35 mg per cubic metre: a threshold, histogram, gradient or front inside that range measures the switch between the color index and the band ratio, and the transition itself moved between reprocessings](gotchas/chlor-a-blended-ocx-and-ci.md), severity high, status: draft
- [A Level 3 chlorophyll composite is the mean of the observations that survived the flags in the period, with no count in the mapped file: a monthly mean is a mean of the sampled days, high latitudes have no winter value, cloudy seasons have few, and a climatology is re-cut every month](gotchas/chlor-a-composite-sampling-gaps.md), severity medium, status: draft
- [A reprocessing rewrites the whole chlorophyll record and the catalogue keeps one version: a series comes from one reprocessing, files fetched before and after a reprocessing are two products, and the near-real-time tail is a third](gotchas/chlor-a-one-reprocessing-per-series.md), severity medium, status: draft
- [chlor_a is a near-surface pigment concentration that the producer calls a proxy for phytoplankton biomass: it is not biomass, not carbon and not primary production, which the same producer distributes as separate products with their own algorithms](gotchas/chlor-a-is-not-biomass.md), severity medium, status: draft

## recipes

(none yet)
