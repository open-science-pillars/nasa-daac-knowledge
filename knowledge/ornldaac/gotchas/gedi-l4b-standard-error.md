---
type: dataset-gotcha
spheres: [biosphere]
title: "The L4B standard error is the hybrid estimator's standard error of the cell mean, built from the L4A model parameter covariance and the footprint clusters in the cell: a cell with few tracks carries a large one, at two tracks the estimator itself runs low, and the percent layer is capped at 100"
description: "Every L4B cell mean comes with SE, the standard error of the mean under hybrid inference, and the product splits it into V1 (the model covariance of the L4A field-to-GEDI model) and V2 (GEDI's sampling of the cell). The size of SE follows the sample: the density of footprints and ground tracks in the cell sets V2, at least two tracks are needed for any variance, and in the estimator's own simulations the variance was under-estimated by about 20 percent when only two clusters were available. PE, the percent standard error, is truncated at 100 with 255 as no data; QF equal to 2 marks only the cells inside the mission's Level 1 requirement (20 Mg/ha or 20 percent). A cell mean quoted without SE, an SE read as the error of a single footprint, a PE of 100 read as exactly 100 percent, or a two-track cell treated as if its SE were as sound as a ten-track cell's, mis-states the uncertainty, and the files do not object."
tags: [gedi, l4b, standard-error, hybrid-inference, variance, sampling, quality-flag, ornldaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T14:02:24Z }
severity: medium
# medium: a wrong reading mis-states an uncertainty rather than the
# cell mean itself, the SE, PE, NC, NS and QF layers are in the same
# dataset and documented on the product page, and the Level 1
# requirement flag gives a ready screen; no eval case is required.
dataset: ../datasets/gedi-l4b-gridded-biomass.md
status: draft
stale_after: 2027-03-15
sources:
  - id: ornl-l4b-v2-guide
    resource: https://daac.ornl.gov/GEDI/guides/GEDI_L4B_Gridded_Biomass.html
    title: "ORNL DAAC user guide, GEDI L4B Version 2 (documentation revision 2022-04-26): the SE, V1, V2, PE, NC, NS and QF layer definitions with units, no-data values and the PE truncation; the two variance components and their decomposition; the two-cluster requirement; the standard error depending on the fit of the L4A models and on the density of observations and ground tracks; the Level 1 requirement and the quality flag value that marks it"
  - id: ornl-l4b-v21-landing
    resource: https://daac.ornl.gov/cgi-bin/dsviewer.pl?ds_id=2299
    title: "ORNL DAAC landing page for GEDI L4B Version 2.1 (Earthdata catalog redirect): the abstract's statement that corresponding 1 km estimates of the standard error of the mean are provided and that uncertainty is due to both sampling and the modeled L4A values"
  - id: cmr-l4b-v21
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2792577683-ORNL_CLOUD.umm_json
    title: "CMR collection record for GEDI L4B Version 2.1: the same abstract, and the ten granules with the SE, PE, V1, V2, NC, NS and QF layer suffixes read through the granule search"
  - id: crossref-patterson-2019
    resource: https://api.crossref.org/works/10.1088/1748-9326/ab18df
    title: "Crossref registry record for Patterson and others 2019, Environmental Research Letters 14, 065007: the abstract on hybrid estimators being unbiased, the variance estimators asymptotically unbiased with under-estimation of about 20 percent at two clusters, sampling error the larger component and the design-based component the source of the small-sample bias"
  - id: ornl-l4a-v3-guide
    resource: https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V3.html
    title: "ORNL DAAC user guide, GEDI L4A Version 3 (documentation revision 2026-09-02): agbd_se as the per-footprint prediction standard error, and the model_data variance-covariance matrix required as input to the L4B algorithm"
  - id: dataset
    resource: ../datasets/gedi-l4b-gridded-biomass.md
    title: "This bundle's GEDI L4B dataset concept, which lists this trap among the known issues"
---

# The L4B standard error is the hybrid estimator's

**Mechanism.** The L4B mean for a 1 km cell is inferred from the
L4A footprints inside it by hybrid inference, and the SE layer is the
standard error of that mean, combining sampling and modeling
uncertainty; the guide splits it into V1, the model covariance due to
the L4A field-to-GEDI biomass model, and V2, the uncertainty due to
GEDI's sampling of the cell (or, under the generalized hierarchical
mode, the second model's fit), so that a user can decompose SE into
its two components.[^ornl-l4b-v2-guide][^ornl-l4b-v21-landing] The
sampling component is where the sample size enters: the guide states
that the standard error of the mean depends on the fit of the L4A
footprint models, reflected in V1, and on the density of observations
and ground tracks, reflected in V2, and NC (the number of ground
tracks with at least one high-quality waveform in the cell) and NS
(the number of such waveforms) record that
density.[^ornl-l4b-v2-guide] The tracks are the clusters of a cluster
sample, at least two are required to calculate a variance, and cells
with fewer hold no estimate.[^ornl-l4b-v2-guide] The estimator's
statistical properties are Patterson and others 2019's subject: in
simulations calibrated with lidar and field data from six United
States sites, hybrid estimators of the mean were unbiased and the
variance estimators appeared asymptotically unbiased, with the
variance under-estimated by approximately 20 percent when data from
only two clusters were available; sampling error contributed more to
the variance than model variability, and the design-based component
was the source of the bias at small sample
sizes.[^crossref-patterson-2019] Two layers summarize SE: PE, the
standard error as a percentage of the mean, truncated to 100 where it
exceeds 100 and 255 where there is no data, and QF, which is 2 where
a land cell meets the mission's Level 1 requirement of a percent
standard error below 20 or a standard error below 20 Mg/ha, the
requirement being that 80 percent of cells reach one of those
bounds.[^ornl-l4b-v2-guide]

**Wrong-result mode.** A cell mean quoted alone, or a sum of cell
means over a region quoted alone, drops the uncertainty the product
ships for every estimated cell; a regional standard error assembled
by treating the cells as independent ignores that the same tracks
run through neighbouring cells. SE read as the error of an individual
footprint confuses the standard error of a 1 km mean with the L4A
per-footprint prediction standard error agbd_se, which is a different
quantity in a different product.[^ornl-l4a-v3-guide] A map of SE, or
of the ratio SE to MU, that treats a two-track cell and a ten-track
cell alike reads a number that the estimator under-states by about a
fifth in the first case and a number close to nominal in the second,
and a threshold on SE selects preferentially the cells whose few
tracks happened to agree.[^crossref-patterson-2019] PE read as a
continuous percentage reports 100 for every cell whose true percent
error is 100 or more, and 255 read as a percentage is a no-data
value.[^ornl-l4b-v2-guide] Zero read as a mean with zero error is a
cell with no estimate.[^ornl-l4b-v2-guide]

**Correct approach.** The uncertainty of a cell is SE, stated with
the cell's NC and NS so that a reader sees the sample it rests on;
the V1 and V2 layers say whether the model or the sample dominates
it.[^ornl-l4b-v2-guide] QF equal to 2 is the product's own screen for
cells inside the Level 1 requirement, and NC is the screen for the
small-sample regime that Patterson and others 2019
characterize.[^ornl-l4b-v2-guide][^crossref-patterson-2019] An
uncertainty for a region larger than a cell is a design question,
not a sum of cell standard errors: the tracks are the clusters, and
the estimator with the L4A model_data covariance applies at the
region's scale.[^ornl-l4b-v2-guide][^ornl-l4a-v3-guide] A percent
error is taken from SE and MU rather than from PE where the cap
matters.[^ornl-l4b-v2-guide]

**Verification.** The layer definitions, the truncation, the
no-data values and the two-cluster rule are in the Version 2 guide's
file table and application section, and the Version 2.1 granule
names in CMR carry the same layer suffixes.[^ornl-l4b-v2-guide][^cmr-l4b-v21]
The estimator's properties are in the abstract on the Patterson and
others 2019 registry record; the article page was not
read.[^crossref-patterson-2019] On the files the check is direct: PE
never exceeds 100 except at 255, MI is 0 wherever NC is below 2, and
MU is 0 there. No GEDI file was opened for this concept. The dataset
concept lists this trap among the known issues.[^dataset]

[^ornl-l4b-v2-guide]: ORNL DAAC user guide, GEDI L4B Version 2, revision 2022-04-26, read 2026-09-15
[^ornl-l4b-v21-landing]: ORNL DAAC landing page for GEDI L4B Version 2.1 (ds_id 2299), read at its Earthdata catalog redirect 2026-09-15
[^cmr-l4b-v21]: CMR collection C2792577683-ORNL_CLOUD and its granule search, read 2026-09-15
[^crossref-patterson-2019]: Crossref record for doi:10.1088/1748-9326/ab18df, read 2026-09-15
[^ornl-l4a-v3-guide]: ORNL DAAC user guide, GEDI L4A Version 3, revision 2026-09-02, read 2026-09-15
[^dataset]: This bundle's GEDI L4B dataset concept
