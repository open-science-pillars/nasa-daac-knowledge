---
type: dataset-gotcha
spheres: [atmosphere, geosphere]
title: "Daymet values are interpolated from stations, and the error is not the domain average: station-sparse and high-relief regions carry larger error, which the cross-validation files quantify and the derived variables lack"
description: "Every Daymet cell is an estimate from surrounding weather stations, weighted by distance and elevation, and the station network is dense over most of the contiguous United States and very sparse over Arctic Alaska and Canada, northern Mexico and mountainous terrain. The product's uncertainty is a cross-validation statistic per station, and the paper's domain-wide daily mean absolute errors (about 1.8 degrees Celsius for tmin and 1.5 for tmax) are averages over that uneven network; the error in a sparse region is read from the cross-validation files for that region, and the derived variables (shortwave radiation, vapor pressure, snow water equivalent) have no cross-validation at all."
tags: [daymet, uncertainty, cross-validation, station-density, interpolation, terrain, mean-absolute-error, ornldaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:40:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-14T12:17:15Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/143 }
severity: low
# low: the interpolated nature of the product and the cross-validation
# record are on every product page, and a wrong reading of the error
# mis-states an uncertainty rather than a value; no eval case is
# required.
dataset: ../datasets/daymet-v4.md
status: stable
stale_after: 2027-03-14
sources:
  - id: thornton-2021
    resource: https://doi.org/10.1038/s41597-021-00973-0
    title: "Thornton and others, 2021, Scientific Data 8, 190: station density varying greatly over the domain, the pre-calculated search radius adopted for robustness where stations are very sparse, the lapse-rate and warm-cap constraints written for sparse and skewed networks, the domain-wide cross-validation error summary, and the statement that station density, terrain and atmospheric patterns drive spatial heterogeneity in the cross-validation statistics"
  - id: crossref-thornton-2021
    resource: https://api.crossref.org/works/10.1038/s41597-021-00973-0
    title: "Crossref registry record for Thornton and others 2021: title, authors, journal, volume and publication date"
  - id: ornl-v4-guide
    resource: https://daac.ornl.gov/DAYMET/guides/Daymet_Daily_V4.html
    title: "ORNL DAAC user guide, Daymet Daily V4 (documentation revision 2024-06-17): the interpolation and extrapolation method, the search radius, the derived secondary variables, and the quality assessment section on the leave-one-out cross-validation protocol"
  - id: ornl-v4-xval-guide
    resource: https://daac.ornl.gov/DAYMET/guides/Daymet_V4_Stn_Level_CrossVal.html
    title: "ORNL DAAC user guide, Daymet Station-Level Inputs and Cross-Validation Result, Version 4: one file per variable, region and year for tmin, tmax and prcp with observed and predicted values and station metadata, provided so that regional accuracy can be assessed"
  - id: cmr-xval-v4r1
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2531991823-ORNL_CLOUD.umm_json
    title: "CMR collection record for the Version 4 R1 station-level inputs and cross-validation dataset (DOI 10.3334/ORNLDAAC/2132): the current release of the cross-validation record"
  - id: dataset
    resource: ../datasets/daymet-v4.md
    title: "This bundle's Daymet dataset concept, whose Uncertainty section rests on the same record"
---

# Station-sparse regions carry larger error

**Mechanism.** Daymet estimates each grid cell's primary variables
(tmax, tmin, prcp) by interpolation and extrapolation from
surrounding weather stations, with weights that reflect each station's
spatial and temporal relationship to the cell, and the approximate
number of stations used per cell is a parameter of the
algorithm.[^ornl-v4-guide][^thornton-2021] The density of stations
varies greatly over the domain and shifts over time as networks
change; Version 4 replaced the earlier iterative station density
calculation with a pre-calculated search radius per cell, sized to
capture the average number of stations, a change made for robustness
in regions of very low station density such as Arctic Alaska and
Canada, where it removed artifacts and reduced mean cross-validation
error, while over most of the contiguous United States the two
approaches are nearly identical.[^thornton-2021] Two constraints in
the temperature regression exist for the same reason: the vertical
temperature gradient is bounded to limit spurious estimates in regions
of strong relief and very sparse networks, named for the far northern
Canadian Rocky Mountains, and any daily estimate is capped relative to
the warmest station in the list to stop spurious horizontal gradients
in very sparse and horizontally skewed networks, named for the
southern Baja peninsula.[^thornton-2021] The product's uncertainty is
a leave-one-out cross-validation: each station is withheld in turn,
predicted from the others and compared with its observation, and the
per-station results ship as the station-level cross-validation
dataset, one file per variable, region and year for tmin, tmax and
prcp with station metadata, so that regression statistics and mean
absolute error can be derived for a region and
period.[^ornl-v4-guide][^ornl-v4-xval-guide][^cmr-xval-v4r1] The
paper's summary numbers are domain-wide: a mean daily absolute error
of about 1.78 degrees Celsius for tmin and 1.52 for tmax over the
40-year record, a precipitation error lower in recent years as the
networks grew, and the statement that variation in station density,
terrain and large-scale atmospheric patterns all contribute to
spatial heterogeneity in the cross-validation
statistics.[^thornton-2021] The derived variables, srad, vp and swe,
are computed from the interpolated temperature and precipitation and
are not cross-validated; the cross-validation covers the three primary
variables.[^ornl-v4-guide][^thornton-2021]

**Wrong-result mode.** An uncertainty quoted for a Daymet series in
the Yukon, the Alaskan interior, northern Mexico or a mountain
catchment from the paper's domain-wide mean absolute error
under-states the local error, because that mean is dominated by the
dense networks of the contiguous United States and the cross-validation
statistics are heterogeneous with station density and terrain. A
comparison of Daymet against an independent record in such a region
that treats the domain-wide error as the expected disagreement flags
ordinary interpolation error as a discrepancy, or, in the other
direction, a fitted trend in a sparse region is reported with a
confidence the local error does not support. A snow water equivalent,
radiation or humidity statement given with a cross-validation error
attaches an error the product does not have for that variable. A
Daymet value at a cell is read as a measurement at that location when
it is a model estimate whose nearest inputs may be far away and at
different elevations.

**Correct approach.** The cross-validation files for the region,
period and variable are the product's uncertainty statement, and the
error quoted for an application is derived from the stations within
that region and period (the paper's authors state that users are
encouraged to consult them to assess suitability for the region,
period and variables of interest); the domain-wide numbers serve as
context, labeled as domain averages.[^thornton-2021][^ornl-v4-xval-guide]
An uncertainty statement for srad, vp or swe names the absence of a
cross-validation for them and rests on the primary variables' errors
and the derivation.[^ornl-v4-guide][^thornton-2021] The current
cross-validation record is the Version 4 R1 collection.[^cmr-xval-v4r1]

**Verification.** The paper's methods section carries the station
density statement, the search radius change and the two constraints,
and its technical validation section carries the error summary and
the heterogeneity statement; its registry record was verified against
Crossref on 2026-09-14 (title, six authors, Scientific Data, volume
8, published 2021) and the article was read in full at
nature.com.[^thornton-2021][^crossref-thornton-2021] The guide's
quality assessment section states the cross-validation protocol, and
the cross-validation guide states what the files hold and what they
are for.[^ornl-v4-guide][^ornl-v4-xval-guide] The CMR record names the
current release of that record.[^cmr-xval-v4r1] No cross-validation
file was opened for this concept, so no regional error is stated
here. The dataset concept's Uncertainty section rests on the same
sources.[^dataset]

[^thornton-2021]: Thornton and others, 2021, Scientific Data 8, 190, doi:10.1038/s41597-021-00973-0, read at nature.com 2026-09-14
[^crossref-thornton-2021]: Crossref record for doi:10.1038/s41597-021-00973-0, read 2026-09-14
[^ornl-v4-guide]: ORNL DAAC user guide, Daymet Daily V4, revision 2024-06-17, read 2026-09-14
[^ornl-v4-xval-guide]: ORNL DAAC user guide, Daymet V4 station-level cross-validation, read 2026-09-14
[^cmr-xval-v4r1]: CMR collection C2531991823-ORNL_CLOUD, read 2026-09-14
[^dataset]: This bundle's Daymet dataset concept
