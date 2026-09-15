---
type: dataset
spheres: [biosphere]
title: "GEDI L4A footprint aboveground biomass density (Version 3): a modeled biomass density and its prediction standard error for every 25 m laser footprint the mission sampled within about 51.6 degrees of the equator"
description: "Level 4A of the Global Ecosystem Dynamics Investigation, the waveform lidar on the International Space Station: for each geolocated laser footprint (about 25 m across, 60 m apart along track, on eight tracks about 600 m apart) a prediction of aboveground biomass density in megagrams per hectare and its prediction standard error, with the quality and degrade flags, the scaled relative height metrics that were the model inputs, and the model parameters and covariance that Level 4B needs. The biomass is a model output: linear models of Level 2A relative height metrics, calibrated on simulated waveforms and field plots and stratified by plant functional type and world region. The current version is Version 3 (published 2026-06-08) with updated models and new quality flags; Version 2.1 remains a complete, separately identified collection. The footprints are a sample, not a map, and the band ends near 51.6 degrees north and south."
tags: [gedi, biomass, agbd, footprint, lidar, iss, plant-functional-type, relative-height, ornldaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T14:02:24Z }
resource: https://doi.org/10.3334/ORNLDAAC/2508
version: "GEDI L4A Version 3 (DOI 10.3334/ORNLDAAC/2508, CMR short name GEDI_L4A_AGB_Density_V3_2508, concept C4212593885-ORNL_CLOUD, published 2026-06-08, user guide revision 2026-09-02), CMR-verified 2026-09-15 as an active collection with 96,275 sub-orbit granules whose latest acquisition starts 2025-07-09; Version 2.1 (DOI 10.3334/ORNLDAAC/2056, GEDI_L4A_AGB_Density_V2_1_2056, C2237824918-ORNL_CLOUD) is listed complete the same day with 96,318 granules covering 2019-04-17 through 2025-07-09"
sources:
  - id: ornl-l4a-v3-guide
    resource: https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V3.html
    title: "ORNL DAAC user guide, GEDI L4A Footprint Level Aboveground Biomass Density, Version 3 (documentation revision 2026-09-02): the summary, the instrument geometry, the file naming and groups, the variable tables, the model stratification by plant functional type and world region, the calibration dataset, the quality assessment, the frequently asked questions on geolocation, quality flags, xvar and prediction intervals, and the dataset revisions table"
  - id: ornl-l4a-v3-landing
    resource: https://daac.ornl.gov/cgi-bin/dsviewer.pl?ds_id=2508
    title: "ORNL DAAC landing page for GEDI L4A Version 3 (DOI 10.3334/ORNLDAAC/2508): the publication date 2026-06-08, the bounding rectangle, the temporal coverage 2019-04-04 to 2025-07-10, the citation and the three companion files"
  - id: ornl-l4a-v21-landing
    resource: https://daac.ornl.gov/cgi-bin/dsviewer.pl?ds_id=2056
    title: "ORNL DAAC landing page for GEDI L4A Version 2.1 (DOI 10.3334/ORNLDAAC/2056), which redirects to the Earthdata catalog page: the publication date 2022-03-17, the last update 2026-04-21, the data state complete, the granule count and the temporal extent"
  - id: cmr-l4a-v3
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C4212593885-ORNL_CLOUD.umm_json
    title: "CMR collection record for GEDI L4A Version 3: the abstract, the DOI, the bounding rectangle 56 north to 53 south, the temporal extent beginning 2019-04-04 with the ends-at-present flag, the active collection progress, the HDF5 format and the 15.352 TB collection size, and the granule search read through the granule listing sorted by start date"
  - id: cmr-l4a-v21
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2237824918-ORNL_CLOUD.umm_json
    title: "CMR collection record for GEDI L4A Version 2.1: the abstract (six algorithm setting groups), the temporal extent 2019-04-17 through 2025-07-09, the complete collection progress, the bounding rectangle 55.8 north to 53 south, and the granule count read through the granule search"
  - id: cmr-gedi-collections
    resource: https://cmr.earthdata.nasa.gov/search/collections.json?provider=ORNL_CLOUD&keyword=GEDI&page_size=100
    title: "CMR collection search for GEDI at provider ORNL_CLOUD: the concept ids, short names and versions of the L4A Version 2.1, L4A Version 3, L4A golden weeks, L4B Version 2.1 and L4B country summary collections"
  - id: doi-handle-2508
    resource: https://doi.org/api/handles/10.3334/ORNLDAAC/2508
    title: "The doi.org handle record for 10.3334/ORNLDAAC/2508, resolving to the Earthdata catalog page for GEDI L4A Version 3; the DataCite metadata service behind doi.org content negotiation was not reachable from the drafting environment"
  - id: crossref-kellner-2023
    resource: https://api.crossref.org/works/10.1029/2022EA002516
    title: "Crossref registry record for Kellner, Armston and Duncanson, Algorithm Theoretical Basis Document for GEDI Footprint Aboveground Biomass Density, Earth and Space Science 10, e2022EA002516, issued 2023-04: the title, the three authors, the journal and the abstract (13 linear models in 32 combinations of plant functional type and world region; 8,587 simulated waveforms in 21 countries for releases 1 and 2; under-represented regions); the article page was not read"
  - id: crossref-dubayah-2022
    resource: https://api.crossref.org/works/10.1088/1748-9326/ac8694
    title: "Crossref registry record for Dubayah and others 2022, GEDI launches a new era of biomass inference from space, Environmental Research Letters 17, 095001, issued 2022-08-18: the title, the 19 authors, the journal and the abstract; the article page at the publisher was not read"
  - id: l4b-dataset
    resource: ./gedi-l4b-gridded-biomass.md
    title: "This bundle's GEDI L4B dataset concept, the 1 km product built from these footprints"
status: draft
stale_after: 2027-03-15
---

# GEDI L4A footprint aboveground biomass density (Version 3)

**Identity.** GEDI L4A is the footprint-level aboveground biomass
density product of the Global Ecosystem Dynamics Investigation, a
multibeam waveform lidar on the International Space Station: for every
geolocated laser footprint whose waveform the algorithm could process,
a prediction of aboveground biomass density (AGBD) in megagrams per
hectare and the standard error of that prediction, with quality
flags, the model inputs and the parameters and covariance of the model
that made it.[^ornl-l4a-v3-guide][^cmr-l4a-v3] The instrument has
three lasers producing eight beam ground transects, which sample
footprints of about 25 m diameter spaced about 60 m along track, with
the transects about 600 m apart across track for a swath about 4.2 km
wide; the footprints lie within the latitude band the station
overflies, nominally 51.6 degrees north and
south.[^ornl-l4a-v3-guide][^cmr-l4a-v3] GEDI was launched on
2018-12-05, completed its initial orbit checkout in April 2019, and
the Version 3 record starts 2019-04-04; no acquisitions occurred while
the instrument was in storage on the station from March 2023 to April
2024.[^ornl-l4a-v3-guide][^cmr-l4a-v3] The biomass is a model output,
not a measurement: linear parametric models relate the Level 2A (L2A)
waveform relative height (RH) metrics to field plot estimates of
AGBD, calibrated on simulated GEDI waveforms derived from airborne
lidar co-located with field plots and stratified by plant functional
type (PFT) and world region.[^ornl-l4a-v3-guide][^crossref-kellner-2023]
The Version 3 product is derived from the Version 3 L2A product and
has the same geolocation, the ground position of each shot (the
lowest mode: elev_lowestmode, lat_lowestmode,
lon_lowestmode).[^ornl-l4a-v3-guide]

**Structure.** HDF5, one file per sub-orbit granule, named
GEDI04_A_YYYYDDDHHMMSS_O<orbit>_<granule>_T<track>_<PPDS type>_<release>_<production version>_V003.h5,
where the PPDS type is 00 for predicted, 01 for rapid and 02 or higher
for final pointing, the release number (004) is the science data
system software release and the version number (003) is the DAAC
dataset version.[^ornl-l4a-v3-guide] Each file holds a METADATA
group, one BEAMXXXX group for each of the eight beams with valid data
(0000, 0001, 0010, 0011, 0101, 0110, 1000, 1011) and ANCILLARY
compound datasets: model_data with the model parameters, the
variance-covariance matrix of the parameters, the degrees of freedom,
the residual standard error, the transforms and the bias correction
for each prediction stratum, plus look-up tables for the PFT, region,
phenology and WorldCover codes.[^ornl-l4a-v3-guide] The BEAMXXXX root
carries the selected prediction: agbd (Mg/ha), agbd_se (the
prediction standard error, Mg/ha), agbd_pi_lower and agbd_pi_upper
(the prediction interval at the level in the alpha attribute, 90
percent by default), agbd_t and agbd_t_se (the prediction and its
standard error in transform space), xvar (the scaled and transformed
RH metrics that were the predictors), predict_stratum,
selected_algorithm, shot_number, sensitivity, the geolocation of the
lowest mode and the flags described below.[^ornl-l4a-v3-guide] Three
subgroups repeat the prediction for each of the four algorithm
setting groups (1, 2, 5 and 10, where 10 means group 5 with a higher
mode used because the lowest detected mode is likely noise):
geolocation, agbd_prediction (agbd_aN, agbd_se_aN and their
companions) and land_cover_data (Landsat tree cover and water
persistence, the MCD12Q1-derived pft_class and pft_infilled_class,
region_class, urban_proportion from the TanDEM-X urban footprint,
leaf_off_flag and phenology_phase from VIIRS phenology, and
worldcover_class).[^ornl-l4a-v3-guide] The CMR record gives the
collection 15.352 TB in HDF5, and the granule search on 2026-09-15
returned 96,275 granules with the latest acquisition starting
2025-07-09.[^cmr-l4a-v3]

**Models and strata.** Five PFTs from an error-corrected and infilled
1 km grid derived from the Type 5 classification of MODIS MCD12Q1
Version 006 (deciduous broadleaf trees, class 4; deciduous needleleaf
trees, class 3; evergreen broadleaf trees, class 2; evergreen
needleleaf trees, class 1; grasses, shrubs and woodlands, classes 5
and 6) and seven world regions (Africa; Australia and Oceania, east
of the Wallace line; Europe; North America north of southern Mexico;
North Asia; South America with Central America, the Caribbean and
southern Mexico; South Asia) define the prediction strata, named like
DBT_Af in predict_stratum.[^ornl-l4a-v3-guide] Version 3 predicts
AGBD in 32 prediction strata with 14 linear models (13 in Version
2.1); five types by seven regions make 35 combinations, and the L4B
stratum code table lists all 35, so three combinations carry no model
of their own, and which three the sources read do not
say.[^l4b-dataset] The models are fitted on a quality-filtered calibration dataset of 11,687
simulated waveforms from 24 countries (8,587 for Version 2.1, in 21
countries per the algorithm
document).[^ornl-l4a-v3-guide][^crossref-kellner-2023] The models
carry a square root or natural logarithm transform on the response
and predictors, a predictor offset added before the transform because
RH metrics can be negative, and a back-transform bias correction
(Snowdon or Baskerville) recorded in model_data; the guide's worked
example shows how par, predictor_id and rh_index reconstruct the
estimator, so a prediction is reproducible from L2A metrics and the
file's own model_data.[^ornl-l4a-v3-guide] Important regions are
under-represented in the calibration data: the forests of continental
Asia, the evergreen broadleaf forests of the islands of Southeast Asia
and north of Australia, and savannas and deciduous tropical forests
worldwide.[^ornl-l4a-v3-guide][^crossref-kellner-2023]

**Quality flags.** AGBD is predicted for every shot where the
algorithm could run (l2_algrunflag); the file removes nothing, and
the flags gate use.[^ornl-l4a-v3-guide] l2a_quality_flag_rel3 marks
land surface shots with waveforms of sufficient fidelity for AGBD
estimation; l4a_quality_flag_rel3 marks shots that are samples of the
population the applied models represent (in the guide's own
spelling, l2a_quality_flag == 1 and is_land_rel3 == 1,
urban_proportion below 50, a prediction stratum assigned, leaf_off_flag
not 1 unless the model uses RH98 alone, and RH100 below 150 m); both use a beam sensitivity threshold of 0.98
over tropical evergreen forests, 0.95 over other land and 0.5 over
water, as the Level 2, 4B and 4C products
do.[^ornl-l4a-v3-guide] degrade_flag from L2A marks degraded
pointing or positioning; degrade_include_flag names the degrade codes
(attitude codes 0, 1, 2, 3, 4 and 6; trajectory codes 0, 3 and 8)
accepted into the Level 4B sample, chosen from GEDI-to-airborne-lidar
crossovers as the codes without higher systematic geolocation error;
elev_highestreturn_outlier_flag marks segments of sub-orbit granules
whose highest-return elevations are outliers against the TanDEM-X
digital elevation model, often low fog or cloud, for gridding and
fusion where the shot-level flags are not
enough.[^ornl-l4a-v3-guide] predictor_limit_flag and
response_limit_flag mark shots whose RH metrics or whose prediction
fall outside the range of the training data.[^ornl-l4a-v3-guide]

**Releases and identifiers.** Version 3 is DOI 10.3334/ORNLDAAC/2508,
CMR concept C4212593885-ORNL_CLOUD, short name
GEDI_L4A_AGB_Density_V3_2508, published 2026-06-08, active in CMR
with a temporal extent beginning 2019-04-04 and a bounding rectangle
of 56 north to 53 south; the landing page gives the coverage as
2019-04-04 to 2025-07-10 and the doi.org handle resolves to its
Earthdata catalog page.[^ornl-l4a-v3-landing][^cmr-l4a-v3][^doi-handle-2508]
The guide's revisions table for Version 3 lists a 2026-06-05 entry
for the model update and an entry dated 2025-09-02 on the page that
adds files for mission weeks 281 through 343 (2024-04-26 through
2025-07-09), a date earlier than the collection's publication; the
documentation revision date is 2026-09-02.[^ornl-l4a-v3-guide] The
Version 3 model update reduced bias, in United States deciduous
broadleaf forest in particular, while the global root mean square
error within forested PFTs weighted by land area moved from 50.0
percent for Version 2.1 to 50.7 percent for Version 3, both from the
geographic transferability estimates; it introduced consistent
quality flags and algorithm setting group selection across the Level
2 and Level 4 footprint products, added l4a_quality_flag_rel3,
degrade_include_flag and elev_highestreturn_outlier_flag, fixed bugs
in the limit flags and leaf_off_flag, added phenology_phase,
phenology_year, pft_infilled_class and worldcover_class, and removed
the unused algorithm setting groups 3, 4 and 6, leaving 1, 2, 5 and
10 where the Version 2.1 abstract names six.[^ornl-l4a-v3-guide][^cmr-l4a-v21]
Version 2.1 (DOI 10.3334/ORNLDAAC/2056, C2237824918-ORNL_CLOUD,
GEDI_L4A_AGB_Density_V2_1_2056) was published 2022-03-17, last
updated 2026-04-21 when files for mission weeks 328 through 343
(2025-03-20 through 2025-07-09) were added, and is a complete
collection of 96,318 granules over 2019-04-17 through
2025-07-09.[^ornl-l4a-v21-landing][^cmr-l4a-v21][^ornl-l4a-v3-guide]
Version 2.0 (2021-12-15) moved to sub-orbit granules and a changed
shot_number format, so Version 1 and Version 2 granules are not
straightforward to link; Version 1 (2019-09-09) is superseded and
available on request, and its golden weeks (mission weeks 19, 32, 34
and 38) are a separate collection, C2734289572-ORNL_CLOUD, version
1.1.[^ornl-l4a-v3-guide][^cmr-gedi-collections] The footprint product
is the input to the L4B gridded product, and the model_data group
carries what the L4B algorithm needs; the L4B Version 2.1 grid that
ships was published 2023-10-29, before Version 3, and rests on the
earlier footprint models.[^ornl-l4a-v3-guide][^l4b-dataset]
Dubayah and others 2022 in Environmental Research Letters, whose
registry record names 19 authors, presents the mission's biomass
inference and the first pan-tropical and temperate estimates from two
years of observations.[^crossref-dubayah-2022]

## Uncertainty

- **A prediction standard error per footprint.** agbd_se is the
  standard error of the model prediction for that footprint, and
  agbd_pi_lower and agbd_pi_upper bound it at the level in the alpha
  attribute (90 percent by default); an interval at another level is
  agbd_t plus or minus agbd_t_se times the t multiplier for the
  model's degrees of freedom in model_data, back-transformed with the
  recorded bias correction.[^ornl-l4a-v3-guide]
- **The error is the model's.** Footprint AGBD is a linear model of
  RH metrics, so its error is a model error assessed by geographic
  transferability: candidate models were tested by holding out
  5-degree grid cells with coincident field data, and the global root
  mean square error within forested PFTs weighted by land area is
  50.7 percent for Version 3 (50.0 percent for Version
  2.1).[^ornl-l4a-v3-guide]
- **The stratum is a 1 km land cover class.** The PFT that picks the
  model comes from an infilled 1 km grid derived from MCD12Q1, and
  the region from a world region grid, looked up at the lowest mode
  position; a footprint's model is set by that cell's class, not by
  the footprint's own vegetation, and regions under-represented in
  the calibration data carry models fitted elsewhere.[^ornl-l4a-v3-guide]
- **Out-of-range predictions are flagged, not removed.**
  predictor_limit_flag and response_limit_flag mark RH metrics or
  predictions outside the training range.[^ornl-l4a-v3-guide]
- **Geolocation.** The Version 3 geolocation is that of the Version 3
  L2A product; degrade_flag, degrade_include_flag and
  elev_highestreturn_outlier_flag mark the shots and segments whose
  position or elevation is not trusted for gridding or
  fusion.[^ornl-l4a-v3-guide]
- **No area estimate ships here.** Aggregation of footprints to an
  area is the Level 4B hybrid inference, which uses the sample within
  a cell and the model parameter covariance from model_data; the L4A
  standard error is per footprint.[^ornl-l4a-v3-guide][^l4b-dataset]

## Known issues

- [gedi-footprint-is-not-a-pixel](../gotchas/gedi-footprint-is-not-a-pixel.md):
  a footprint is a 25 m sample on a sparse track pattern, and a mean
  of footprints is a sample mean of a model output, not the area's
  biomass density.
- [gedi-quality-and-degrade-flags](../gotchas/gedi-quality-and-degrade-flags.md):
  every shot the algorithm could run on carries a prediction, and the
  quality and degrade flags gate which are fit for use.
- [gedi-biomass-is-a-model-output](../gotchas/gedi-biomass-is-a-model-output.md):
  the value is a stratified model of height metrics that changes with
  the version's models and the stratum grid.
- [gedi-l4b-standard-error](../gotchas/gedi-l4b-standard-error.md):
  the L4B cell standard error is the hybrid estimator's, and a cell
  with few tracks carries a large one.
- [gedi-latitude-limits](../gotchas/gedi-latitude-limits.md): the
  band ends near 51.6 degrees, so the boreal forest is absent from
  both products.

[^ornl-l4a-v3-guide]: ORNL DAAC user guide, GEDI L4A Version 3, revision 2026-09-02, read 2026-09-15
[^ornl-l4a-v3-landing]: ORNL DAAC landing page for GEDI L4A Version 3 (ds_id 2508), read 2026-09-15
[^ornl-l4a-v21-landing]: ORNL DAAC landing page for GEDI L4A Version 2.1 (ds_id 2056), read at its Earthdata catalog redirect 2026-09-15
[^cmr-l4a-v3]: CMR collection C4212593885-ORNL_CLOUD and its granule search, read 2026-09-15
[^cmr-l4a-v21]: CMR collection C2237824918-ORNL_CLOUD and its granule search, read 2026-09-15
[^cmr-gedi-collections]: CMR collection search for GEDI at ORNL_CLOUD, read 2026-09-15
[^doi-handle-2508]: doi.org handle record for 10.3334/ORNLDAAC/2508, read 2026-09-15
[^crossref-kellner-2023]: Crossref record for doi:10.1029/2022EA002516, read 2026-09-15
[^crossref-dubayah-2022]: Crossref record for doi:10.1088/1748-9326/ac8694, read 2026-09-15
[^l4b-dataset]: This bundle's GEDI L4B dataset concept
