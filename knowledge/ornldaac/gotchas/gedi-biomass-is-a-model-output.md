---
type: dataset-gotcha
spheres: [biosphere]
title: "GEDI biomass is a model output, not a measurement: L4A AGBD is a linear model of L2A relative height metrics, calibrated on simulated waveforms and field plots and stratified by plant functional type and world region, so a footprint's value changes with the version's models and with the 1 km stratum it falls in"
description: "The lidar measures a waveform; the biomass is predicted from that waveform's relative height metrics by one of 14 linear models (Version 3) chosen by the combination of plant functional type and world region at the footprint's ground position, the type coming from an infilled 1 km grid derived from MODIS MCD12Q1. The models were fitted on 11,687 simulated waveforms from 24 countries, and their geographic transferability error, stated as one global figure (the root mean square error within forested types weighted by land area, 50.7 percent for Version 3) and not per stratum; continental Asia, the evergreen forests of the Southeast Asian islands and north of Australia, and the world's savannas and deciduous tropical forests are under-represented in the calibration. Version 3 refitted the models and changed predictions even where the calibration data did not change, and the L4B Version 2.1 grid was built before that refit. A footprint value read as a measured stock, a difference between versions or across a stratum boundary read as a change on the ground, or a comparison with a field plot that ignores the model error, mis-reads a prediction as an observation."
tags: [gedi, biomass, model, calibration, plant-functional-type, world-region, relative-height, version, ornldaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T14:02:24Z }
severity: medium
# medium: the guide, the abstract and the algorithm document all say
# the value is a model prediction with a stated standard error and
# stratification, and a wrong reading over-trusts the value rather
# than producing a different number; the version and stratum
# mechanisms are documented in the file's own model_data group; no
# eval case is required.
dataset: ../datasets/gedi-l4a-footprint-biomass.md
status: draft
stale_after: 2027-03-15
sources:
  - id: ornl-l4a-v3-guide
    resource: https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V3.html
    title: "ORNL DAAC user guide, GEDI L4A Version 3 (documentation revision 2026-09-02): footprint AGBD derived from linear parametric models of L2A relative height metrics and field plot estimates; the calibration on simulated waveforms from airborne lidar because GEDI will not intersect most field plots; the stratification by plant functional type and world region with the MCD12Q1-derived 1 km grid and the region definitions; the transforms, offset and bias correction; the under-represented regions; the geographic transferability assessment; the Version 3 revision entry with the training data, model count and root mean square error changes and the note that predictions differ even where data changed little; the frequently asked question on applying an alternative model"
  - id: crossref-kellner-2023
    resource: https://api.crossref.org/works/10.1029/2022EA002516
    title: "Crossref registry record for Kellner, Armston and Duncanson, Algorithm Theoretical Basis Document for GEDI Footprint Aboveground Biomass Density, Earth and Space Science 10, e2022EA002516 (issued 2023-04): the abstract on 13 linear models in 32 combinations of plant functional type and world region, 8,587 simulated waveforms in 21 countries for releases 1 and 2, the under-represented regions and the assumption of generalization beyond training data; the article page was not read"
  - id: cmr-l4a-v3
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C4212593885-ORNL_CLOUD.umm_json
    title: "CMR collection record for GEDI L4A Version 3: the abstract's statement that footprint AGBD was derived from parametric models relating simulated L2A relative height metrics to field plot estimates, compiled by world region and plant functional type"
  - id: cmr-l4a-v21
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2237824918-ORNL_CLOUD.umm_json
    title: "CMR collection record for GEDI L4A Version 2.1: a complete, separately identified collection with its own DOI whose files carry the Version 2.1 models"
  - id: cmr-l4b-v21
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2792577683-ORNL_CLOUD.umm_json
    title: "CMR collection record for GEDI L4B Version 2.1: the creation date 2023-10-29, earlier than L4A Version 3"
  - id: dataset
    resource: ../datasets/gedi-l4a-footprint-biomass.md
    title: "This bundle's GEDI L4A dataset concept, which lists this trap among the known issues"
---

# GEDI biomass is a model output

**Mechanism.** Footprint AGBD is derived from linear parametric
models that relate L2A waveform relative height metrics to
aboveground biomass estimates from co-located field plots; because
few places have field estimates and GEDI, a sampling mission, will
not intersect most of them, the models were fitted on simulated GEDI
waveforms derived from discrete-return airborne lidar over field
plots, processed to L2A-equivalent RH metrics.[^ornl-l4a-v3-guide][^cmr-l4a-v3]
The models are stratified: the algorithm looks up the plant
functional type at the lowest-mode position in an error-corrected and
infilled 1 km grid derived from the Type 5 classification of MODIS
MCD12Q1 Version 006 (deciduous broadleaf, deciduous needleleaf,
evergreen broadleaf, evergreen needleleaf, and grasses, shrubs and
woodlands) and the world region in a region grid (Africa, Australia
and Oceania, Europe, North America, North Asia, South America, South
Asia), takes the estimator for that combination, and predicts AGBD
from the scaled and transformed RH metrics, with a square root or
logarithm transform, a predictor offset and a back-transform bias
correction recorded in the file's model_data
group.[^ornl-l4a-v3-guide] The algorithm document describes 13 linear
models over 32 combinations of type and region fitted on 8,587
quality-filtered simulated waveforms in 21 countries for releases 1
and 2; Version 3 uses 14 models over the 32 strata fitted on 11,687
simulated waveforms from 24 countries, and the guide records that the
refit reduced bias, in United States deciduous broadleaf forest in
particular, while the global root mean square error within forested
types weighted by land area moved from 50.0 percent (Version 2.1) to
50.7 percent (Version 3), and that even regions with little change
in data, South America and Europe among them, see different
predictions where type-wide models
apply.[^crossref-kellner-2023][^ornl-l4a-v3-guide] Important regions
are under-represented in the calibration: the forests of continental
Asia, the evergreen broadleaf forests of the Southeast Asian islands
and north of Australia, and savannas and deciduous tropical forests
worldwide, so their predictions rest on models fitted
elsewhere.[^ornl-l4a-v3-guide][^crossref-kellner-2023]

**Wrong-result mode.** A footprint value read as a measured stock
carries no visible sign that it is a prediction with a standard
error of its own (agbd_se) and, for the models as a whole, a global
land-area-weighted root mean square error over forested types near
half the value, a figure the guide gives globally and not per
stratum.[^ornl-l4a-v3-guide] Version 2.1 and Version 3 footprints
mixed in one analysis, or a Version 3 value compared with a Version
2.1 value at the same place, register the model refit as a change in
the forest, and the two collections are separately identified with
their own DOIs for that reason.[^ornl-l4a-v3-guide][^cmr-l4a-v21]
The same holds across products: the L4B Version 2.1 grid (published
2023-10-29) predates L4A Version 3 (created 2026-06-08), so its cell
means rest on the earlier model set, and a Version 3 footprint mean
compared with a Version 2.1 cell mean at the same place differs by
the refit before anything else; this is reasoning from the
publication dates, not a statement read.[^cmr-l4b-v21][^cmr-l4a-v3] A
step in biomass across a boundary of the 1 km type or region grid,
where the vegetation is continuous, is the boundary between two
estimators, and a footprint whose 1 km class does not match its own
25 m vegetation is predicted with the wrong model; the guide's
example is Indonesian forest east of the Wallace line, where the
Australia and Oceania estimator applies and a type-wide model may be
preferred.[^ornl-l4a-v3-guide] A field plot compared with a
footprint without the prediction interval, or a validation that
treats the calibration regions as representative of Southeast Asia
or the savannas, mis-states what was tested.[^ornl-l4a-v3-guide][^crossref-kellner-2023]

**Correct approach.** The value is a prediction, and the file says
so in full: agbd comes with agbd_se and a prediction interval, xvar
holds the predictors, predict_stratum names the estimator, and the
model_data group holds the coefficients, the covariance, the
transforms and the bias correction that reproduce the prediction from
L2A metrics, or apply an alternative type-wide model to the same
footprints.[^ornl-l4a-v3-guide] A series or a comparison is built on
one version, named with its DOI, and a difference between versions is
a model difference until the revisions table says
otherwise.[^ornl-l4a-v3-guide][^cmr-l4a-v21] A stratum boundary is
read from pft_infilled_class and region_class beside the biomass, and
an under-represented region is reported with the guide's
caveat.[^ornl-l4a-v3-guide]

**Verification.** The model description, the strata, the calibration
counts and the revision entry are in the Version 3 guide's methods
and revisions sections; the release 1 and 2 counts are in the
algorithm document's abstract on its registry
record.[^ornl-l4a-v3-guide][^crossref-kellner-2023] On any Version 3
granule, model_data lists the estimators with their strata and
parameters, and the same shot in a Version 2.1 and a Version 3
granule carries different agbd values where the stratum's model was
refitted. No GEDI file was opened for this concept. The dataset
concept lists this trap among the known issues.[^dataset]

[^ornl-l4a-v3-guide]: ORNL DAAC user guide, GEDI L4A Version 3, revision 2026-09-02, read 2026-09-15
[^crossref-kellner-2023]: Crossref record for doi:10.1029/2022EA002516, read 2026-09-15
[^cmr-l4a-v3]: CMR collection C4212593885-ORNL_CLOUD, read 2026-09-15
[^cmr-l4a-v21]: CMR collection C2237824918-ORNL_CLOUD, read 2026-09-15
[^cmr-l4b-v21]: CMR collection C2792577683-ORNL_CLOUD, read 2026-09-15
[^dataset]: This bundle's GEDI L4A dataset concept
