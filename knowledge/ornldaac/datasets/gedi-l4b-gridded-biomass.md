---
type: dataset
spheres: [biosphere]
title: "GEDI L4B gridded mean aboveground biomass density (Version 2.1): 1 km cell means inferred from the L4A footprint sample by hybrid estimation, with a standard error of the mean, the sample counts, a quality flag and the prediction stratum in ten GeoTIFF layers"
description: "Level 4B of the Global Ecosystem Dynamics Investigation: for every 1 km cell of the global EASE-Grid 2.0 (EPSG 6933) an estimate of mean aboveground biomass density in megagrams per hectare, inferred by hybrid model-based estimation from the quality-filtered L4A footprints inside the cell, for mission weeks 19 through 223 (2019-04-18 to 2023-03-16) in Version 2.1. Ten cloud-optimized GeoTIFF layers: the mean, two variance components, the standard error of the mean, the percent standard error, the numbers of ground tracks and of footprints, a quality flag, the prediction stratum that links to the L4A model, and the mode of inference. A cell mean covers the whole cell, forest and non-forest; a cell needs at least two ground tracks for a hybrid estimate, and cells without one hold zero. Valid cells lie nominally within 52 degrees of the equator."
tags: [gedi, biomass, agbd, gridded, 1km, ease-grid, hybrid-inference, standard-error, ornldaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T14:02:24Z }
resource: https://doi.org/10.3334/ORNLDAAC/2299
version: "GEDI L4B Version 2.1 (DOI 10.3334/ORNLDAAC/2299, CMR short name GEDI_L4B_Gridded_Biomass_V2_1_2299, concept C2792577683-ORNL_CLOUD, published 2023-10-29), CMR-verified 2026-09-15 as a complete collection of 10 granules named GEDI04_B_MW019MW223_02_002_02_R01000M_<layer>.tif covering 2019-04-18 through 2023-03-16; Version 2 (DOI 10.3334/ORNLDAAC/2017, mission weeks 19 through 138, 2019-04-18 to 2021-08-04) is the version whose HTML user guide (revision 2022-04-26) documents the layers"
sources:
  - id: ornl-l4b-v21-landing
    resource: https://daac.ornl.gov/cgi-bin/dsviewer.pl?ds_id=2299
    title: "ORNL DAAC landing page for GEDI L4B Version 2.1 (DOI 10.3334/ORNLDAAC/2299), which redirects to the Earthdata catalog page: the abstract (mission week 19 starting 2019-04-18 to mission week 223 ending 2023-03-16), the publication date 2023-10-29, the 10 files, the 2.326 GB size, the extent 52 north to 52 south, the citation with 11 authors, and the three documents listed (the Version 2.0 ATBD, the excluded granules list and the Version 2.1 user guide, all PDFs on the data host)"
  - id: ornl-l4b-v2-guide
    resource: https://daac.ornl.gov/GEDI/guides/GEDI_L4B_Gridded_Biomass.html
    title: "ORNL DAAC user guide, GEDI L4B Gridded Aboveground Biomass Density, Version 2 (documentation revision 2022-04-26, DOI 10.3334/ORNLDAAC/2017): the file naming convention, the ten layers with units, no-data values and data types, the grid properties, the prediction stratum codes, the user notes on coverage, the hybrid inference and its two-cluster requirement, the mode of inference, the whole-cell meaning of the mean, the Level 1 requirement and the quality flag, the two variance components and the non-response pattern"
  - id: cmr-l4b-v21
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2792577683-ORNL_CLOUD.umm_json
    title: "CMR collection record for GEDI L4B Version 2.1: the abstract, the DOI, the temporal extent 2019-04-18 through 2023-03-16, the bounding rectangle 52 north to 52 south, the complete collection progress, the related URLs (the Version 2.0 ATBD and the Version 2.1 user guide as PDFs on data.ornldaac.earthdata.nasa.gov), and the ten granules with their layer suffixes read through the granule search"
  - id: cmr-gedi-collections
    resource: https://cmr.earthdata.nasa.gov/search/collections.json?provider=ORNL_CLOUD&keyword=GEDI&page_size=100
    title: "CMR collection search for GEDI at provider ORNL_CLOUD: the concept ids and short names of the L4B Version 2.1 collection and of the L4B country-level summaries collection (C2813390180-ORNL_CLOUD, GEDI_L4B_Country_Biomass_2321)"
  - id: doi-handle-2299
    resource: https://doi.org/api/handles/10.3334/ORNLDAAC/2299
    title: "The doi.org handle record for 10.3334/ORNLDAAC/2299, resolving to the Earthdata catalog page for GEDI L4B Version 2.1; the DataCite metadata service behind doi.org content negotiation was not reachable from the drafting environment"
  - id: crossref-patterson-2019
    resource: https://api.crossref.org/works/10.1088/1748-9326/ab18df
    title: "Crossref registry record for Patterson and others 2019, Statistical properties of hybrid estimators proposed for GEDI, Environmental Research Letters 14, 065007, issued 2019-06-01: the title, the 13 authors, the journal and the abstract (hybrid estimators of mean biomass unbiased, variance estimators asymptotically unbiased with about 20 percent under-estimation at two clusters, sampling error the larger component in the study areas); the article page was not read"
  - id: crossref-dubayah-2022
    resource: https://api.crossref.org/works/10.1088/1748-9326/ac8694
    title: "Crossref registry record for Dubayah and others 2022, GEDI launches a new era of biomass inference from space, Environmental Research Letters 17, 095001, issued 2022-08-18: the title, the 19 authors, the journal and the abstract (1 km mean biomass densities and national and sub-national aggregates from two years of observations, each with a standard error); the article page was not read"
  - id: cmr-l4a-v21
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2237824918-ORNL_CLOUD.umm_json
    title: "CMR collection record for GEDI L4A Version 2.1 (DOI 10.3334/ORNLDAAC/2056): the footprint product the Version 2 L4B guide names as its input, created 2022-03-17"
  - id: cmr-l4a-v3
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C4212593885-ORNL_CLOUD.umm_json
    title: "CMR collection record for GEDI L4A Version 3: the creation date 2026-06-08, later than the L4B Version 2.1 publication"
  - id: ornl-l4a-v3-guide
    resource: https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V3.html
    title: "ORNL DAAC user guide, GEDI L4A Version 3 (documentation revision 2026-09-02): the statement that the footprint quality flags use beam sensitivity thresholds of 0.98 over tropical evergreen forests, 0.95 over other land and 0.5 over water, matching what the Level 2, 4B and 4C products use, and the revisions table naming degrade_include_flag and elev_highestreturn_outlier_flag as new in Version 3"
  - id: l4a-dataset
    resource: ./gedi-l4a-footprint-biomass.md
    title: "This bundle's GEDI L4A dataset concept, the footprint product family this grid is inferred from"
status: draft
stale_after: 2027-03-15
---

# GEDI L4B gridded mean aboveground biomass density (Version 2.1)

**Identity.** GEDI L4B provides 1 km by 1 km estimates of mean
aboveground biomass density (AGBD): the L4A footprint product
converts each high-quality waveform to an AGBD prediction, and L4B
uses the sample of those predictions present within the borders of
each 1 km cell to statistically infer the cell's mean, by the hybrid
model-based mode of inference that Patterson and others 2019
describe, with a corresponding 1 km estimate of the standard error of
the mean.[^ornl-l4b-v21-landing][^cmr-l4b-v21][^crossref-patterson-2019]
Version 2.1 covers mission week 19, starting 2019-04-18, through
mission week 223, ending 2023-03-16; the uncertainty is due both to
GEDI's sampling of the 1 km area, as opposed to wall-to-wall
observation, and to the L4A values being modeled rather than
measured.[^ornl-l4b-v21-landing][^cmr-l4b-v21] The estimate covers
the entire area of the cell whether it is forested or not: no
high-resolution forest mask was applied, and a forest-only density is
the cell mean divided by the forest fraction from the user's own
forest map.[^ornl-l4b-v2-guide] Dubayah and others 2022 in
Environmental Research Letters present the pan-tropical and temperate
estimates from the first two years of observations at 1 km and
aggregated to countries and to United States sub-national units, each
with a standard error.[^crossref-dubayah-2022]

**Structure.** Ten cloud-optimized GeoTIFF files, one per layer,
named GEDI04_B_<start week><end week>_<PPDS>_<release>_<production version>_R01000M_<layer>.tif;
the Version 2.1 granules in CMR are
GEDI04_B_MW019MW223_02_002_02_R01000M_ followed by MU, V1, V2, SE,
PE, NC, NS, QF, PS or MI, each spanning 2019-04-18 to 2023-03-16, and
the collection is 2.326 GB.[^cmr-l4b-v21][^ornl-l4b-v21-landing] The
Version 2 guide, which documents the same ten layers under the same
convention, gives them as: MU, the estimated mean AGBD for the cell
including forest and non-forest (Mg/ha, float32, no data -9999); V1,
variance component 1, the uncertainty due to the field-to-GEDI model
used in L4A; V2, variance component 2, the uncertainty due to GEDI's
sampling of the cell under hybrid inference (or, under the
generalized hierarchical mode, the second model's uncertainty); SE,
the standard error of the mean combining sampling and modeling
uncertainty (Mg/ha); PE, the standard error as a percentage of the
mean, truncated to 100 (uint8, no data 255); NC, the number of
clusters, meaning unique GEDI ground tracks with at least one
high-quality waveform in the cell; NS, the total number of
high-quality waveforms in the cell; QF, a quality flag (0 outside the
GEDI domain, 1 land surface, 2 land surface meeting the mission Level
1 requirement of percent standard error below 20 or standard error
below 20 Mg/ha); PS, the prediction stratum, a code from 1 to 35 for
the PFT and world region combination (DBT_Af is 1, GSW_NAm is 35)
that is also the row of the L4A model_data dataset whose parameters
and covariance the cell used, the 35 codes being every combination of
the five types and seven regions where the L4A guide counts 32
prediction strata with models, and which three combinations carry no
model of their own is not stated in the sources read; and MI, the mode of inference (0 none,
1 hybrid model-based, 2 generalized hierarchical
model-based).[^ornl-l4b-v2-guide] The grid is the global EASE-Grid
2.0 (EPSG 6933, WGS 84, meters), one band per file, 34,704 columns by
14,616 rows with the outer edge of the upper-left pixel at
-17367530.45, 7314540.83 m; the files span 85 to -85 degrees
latitude, the full grid, and cells with valid values fall nominally
within 52 to -52.[^ornl-l4b-v2-guide] The L4A footprints are assigned
to cells by their center point.[^ornl-l4b-v2-guide]

**Inference and coverage.** The primary algorithm is hybrid inference,
in which mean biomass is estimated from an incomplete sample of
modeled biomass values and the variance accounts for both the model
and the sample design; GEDI's linear observations are treated as a
cluster sample with each ground track a cluster, and since at least
two clusters are required for a variance, the hybrid estimate exists
only in cells with samples from at least two intersecting ground
tracks.[^ornl-l4b-v2-guide][^crossref-patterson-2019] At the end of
the mission, cells without sufficient clusters are to be estimated
by generalized hierarchical model-based inference, a second-level
model extending biomass to a surface predicted from wall-to-wall
imagery; until then only cells where hybrid inference is possible
hold a mean, and the other cells hold zero.[^ornl-l4b-v2-guide] The
zero cells are not uniform: non-response is higher earlier in the
mission, closer to the equator where the station's overpass pattern
is sparser, in cloudy areas, and where reference ground tracks were
not sampled because of the mission's second-year orbital resonance
problem, an unscheduled change in station altitude that repeated
some tracks at the expense of others.[^ornl-l4b-v2-guide] The
Version 2 guide names L4A Version 2.1 (DOI 10.3334/ORNLDAAC/2056) as
the footprint product whose predictions it grids and whose user guide
describes them.[^ornl-l4b-v2-guide][^cmr-l4a-v21] The Version 2.1
guide could not be read, so the L4A version behind the Version 2.1
grid is not stated in a source read; by the dates, L4B Version 2.1
(published 2023-10-29) predates L4A Version 3 (created 2026-06-08),
so the shipped grid cannot rest on the Version 3 models or on the
flags Version 3 introduced (degrade_include_flag and
elev_highestreturn_outlier_flag), and a Version 3 footprint mean and
a Version 2.1 cell mean at the same place rest on different model
sets; this is reasoning from the publication dates, not a statement
read.[^cmr-l4b-v21][^cmr-l4a-v3][^ornl-l4a-v3-guide] The L4A Version
3 guide states that the footprint quality flags use a beam
sensitivity threshold of 0.98 over tropical evergreen forests, 0.95
over other land and 0.5 over water, matching what the Level 2, 4B and
4C products use.[^ornl-l4a-v3-guide]

**Releases and identifiers.** Version 2.1 is DOI
10.3334/ORNLDAAC/2299, CMR concept C2792577683-ORNL_CLOUD, short
name GEDI_L4B_Gridded_Biomass_V2_1_2299, published 2023-10-29, a
complete collection with the doi.org handle resolving to its Earthdata
catalog page; its citation names 11 authors (Dubayah, Armston,
Healey, Yang, Patterson, Saarela, Stahl, Duncanson, Kellner, Bruening
and Pascual, 2023).[^ornl-l4b-v21-landing][^cmr-l4b-v21][^doi-handle-2299]
Version 2 (DOI 10.3334/ORNLDAAC/2017) covered mission weeks 19
through 138, 2019-04-18 to 2021-08-04, and its HTML user guide is the
readable layer documentation; the Version 2.1 user guide and the
Version 2.0 algorithm theoretical basis document are PDFs on the
DAAC's data host, listed on the landing page and in CMR, and were not
readable from the drafting environment.[^ornl-l4b-v2-guide][^cmr-l4b-v21]
A country-level summary product, GEDI_L4B_Country_Biomass_2321
(C2813390180-ORNL_CLOUD), is a separate collection not described
here.[^cmr-gedi-collections]

## Uncertainty

- **SE is the standard error of the cell mean under hybrid
  inference.** It combines V1, the model covariance due to the L4A
  field-to-GEDI model, with V2, the sampling component from the
  number and variance of the footprint clusters in the cell, and the
  two layers let the user decompose it.[^ornl-l4b-v2-guide]
- **The estimator's own properties.** In the simulations of
  Patterson and others 2019, calibrated with lidar and field data
  from six United States sites, hybrid estimators of mean biomass
  were unbiased and the variance estimators appeared asymptotically
  unbiased, with variance under-estimated by about 20 percent when
  only two clusters were available; in those study areas sampling
  error contributed more to the variance than model variability, and
  the design-based component was the source of the small-sample
  bias.[^crossref-patterson-2019]
- **A cell with few tracks carries a large standard error.** The
  standard error depends on the fit of the L4A models (V1) and on the
  density of observations and ground tracks (V2); NC and NS record
  the sample behind each cell, and PE is truncated at 100
  percent.[^ornl-l4b-v2-guide]
- **The Level 1 requirement is a mission target, tracked per cell.**
  The requirement is that 80 percent of 1 km cells be estimated
  within a standard error of 20 Mg/ha or 20 percent, whichever is
  greater; QF equal to 2 marks the cells that meet it.[^ornl-l4b-v2-guide]
- **The mean is a whole-cell mean.** Forest and non-forest area are
  both in it, so the value for a partly forested cell is below the
  forest's own density.[^ornl-l4b-v2-guide]
- **Zero is not an estimate, and -9999 is no data.** The guide states
  that until the end-of-mission inference all grid cells without a
  valid hybrid mean hold zero, with MI equal to 0, and QF separates
  cells outside the GEDI domain from land cells; the file table gives
  -9999 as the no-data value of MU, V1, V2 and SE and 255 for PE
  without naming which cells carry it, so which cells hold -9999
  rather than zero is not stated in the sources read.[^ornl-l4b-v2-guide]

## Known issues

- [gedi-l4b-standard-error](../gotchas/gedi-l4b-standard-error.md):
  SE is the hybrid estimator's standard error of the mean, and a cell
  with few tracks carries a large one that runs low at two tracks.
- [gedi-footprint-is-not-a-pixel](../gotchas/gedi-footprint-is-not-a-pixel.md):
  the cell mean is inferred from a sparse footprint sample, and a
  footprint mean is not an area estimate.
- [gedi-quality-and-degrade-flags](../gotchas/gedi-quality-and-degrade-flags.md):
  the sample behind each cell is the flag-gated one.
- [gedi-biomass-is-a-model-output](../gotchas/gedi-biomass-is-a-model-output.md):
  the cell means inherit the L4A models of the version they were
  built from, which predates Version 3, so a Version 3 footprint mean
  and a Version 2.1 cell rest on different model sets.
- [gedi-latitude-limits](../gotchas/gedi-latitude-limits.md): the
  files span 85 degrees of latitude, and valid cells stop near 52.

[^ornl-l4b-v21-landing]: ORNL DAAC landing page for GEDI L4B Version 2.1 (ds_id 2299), read at its Earthdata catalog redirect 2026-09-15
[^ornl-l4b-v2-guide]: ORNL DAAC user guide, GEDI L4B Version 2, revision 2022-04-26, read 2026-09-15
[^cmr-l4b-v21]: CMR collection C2792577683-ORNL_CLOUD and its granule search, read 2026-09-15
[^cmr-gedi-collections]: CMR collection search for GEDI at ORNL_CLOUD, read 2026-09-15
[^doi-handle-2299]: doi.org handle record for 10.3334/ORNLDAAC/2299, read 2026-09-15
[^crossref-patterson-2019]: Crossref record for doi:10.1088/1748-9326/ab18df, read 2026-09-15
[^crossref-dubayah-2022]: Crossref record for doi:10.1088/1748-9326/ac8694, read 2026-09-15
[^cmr-l4a-v21]: CMR collection C2237824918-ORNL_CLOUD, read 2026-09-15
[^cmr-l4a-v3]: CMR collection C4212593885-ORNL_CLOUD, read 2026-09-15
[^ornl-l4a-v3-guide]: ORNL DAAC user guide, GEDI L4A Version 3, revision 2026-09-02, read 2026-09-15
[^l4a-dataset]: This bundle's GEDI L4A dataset concept
