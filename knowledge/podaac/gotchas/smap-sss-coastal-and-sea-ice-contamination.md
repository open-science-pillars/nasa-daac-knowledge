---
type: dataset-gotcha
spheres: [hydrosphere, cryosphere]
title: "SMAP salinity near coasts and the sea-ice edge: land and ice inside the antenna's view bias the retrieval by up to several salinity units, and a coastal or ice-edge series is a series of the product's own exclusion decisions"
description: "An L-band radiometer integrates emission from the whole visible disk weighted by the antenna pattern, so land or sea ice in the sidelobes or the footprint contaminates an ocean cell: land alone can bias SMAP salinity by about one practical salinity unit before correction, and sea ice by several after it. Both producers correct and then exclude: the JPL CAP product removes land- and ice-flagged observations and grids the rest with a relaxed filter, keeping only average land and ice fractions at Level 3; the RSS product retrieves within 30 to 40 km of land, sets missing values above hard thresholds and drops moderately contaminated cells from its 70 km smoothing, and classifies sea-ice zones whose residual errors reach 7.5 salinity units. A salinity series for a shelf, an estuary or the marginal ice zone built from the nearest valid cells therefore samples a changing set of cells whose contamination and coverage vary with season and geometry, and its variability and trend are partly the product's flagging, not the ocean's."
tags: [smap, salinity, sss, coast, land-contamination, sea-ice, marginal-ice-zone, sidelobe, flags, arctic, antarctic, river-plume]
generated: { by: knowledge-seeder/claude, at: 2026-09-13T21:00:00Z }
verified:
  - { by: human:PaulMRamirez, at: 2026-09-13T21:10:06Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/128 }
  - { by: human:PaulMRamirez, at: 2026-09-14T12:26:34Z, role: maintainer, source: https://claude.ai/code/session_01DVKYxSeRJWncZVsmaxC4p4 }
severity: high
dataset: ../datasets/smap-sss-jpl.md
eval_case: smap-sss-coastal-and-sea-ice-contamination
status: stable
stale_after: 2027-03-13
sources:
  - id: jpl-guide
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/docs/JPL-CAP_V5/SMAP-SSS_JPL_V5.0_Documentation.pdf
    title: "SMAP Salinity and Wind Speed Data User's Guide, Version 5.0, JPL, November 2020 (read in full 2026-09-13): the land correction (section 3.2.1), land and ice flagging at L2A (3.3.2), the L3 filter (3.5 and 5.2), the quality flag bits (6.2.24) and the L3 land and ice fields (7.2)"
  - id: granule
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-protected/SMAP_JPL_L3_SSS_CAP_MONTHLY_V5/2026/SMAP_L3_SSS_202608_MONTHLY_V5.0.nc
    title: "One JPL monthly granule (August 2026) opened with an Earthdata token on 2026-09-13 and deleted: the L3 carries land_fraction and ice_fraction and no flag variable"
  - id: rss-release
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/docs/V6/Release_V6.0.pdf
    title: "RSS SMAP Salinity Version 6.0 release notes, RSS Technical Report 011624 (read 2026-09-13): the land sidelobe correction and exclusion (section 5.1), sea-ice detection, zones and the residual-error table (5.3), the quality flags (6), the L3 processing (7) and the early-mission shelf bias removed in V6 (2.7)"
  - id: podaac-rss-8day
    resource: https://podaac.jpl.nasa.gov/dataset/SMAP_RSS_L3_SSS_SMI_8DAY-RUNNINGMEAN_V6
    title: "PO.DAAC collection page, SMAP_RSS_L3_SSS_SMI_8DAY-RUNNINGMEAN_V6: the variable table with gland, fland, gice_est, anc_sea_ice_flag and sea_ice_zones (read 2026-09-13)"
  - id: meissner-2021
    resource: https://doi.org/10.3390/rs13245120
    title: "Meissner and Manaster, 2021, SMAP salinity retrievals near the sea-ice edge using multi-channel AMSR2 brightness temperatures, Remote Sensing 13, 5120: sea-ice contamination as a large error source, the discriminant flagging and correction the RSS product uses, and undetected icebergs as a cause of spurious retrievals (registry record verified and abstract read there 2026-09-13; the article was not read)"
  - id: tang-2018
    resource: https://doi.org/10.3390/rs10060869
    title: "Tang and others, 2018, The potential and challenges of using SMAP sea surface salinity to monitor Arctic Ocean freshwater changes, Remote Sensing 10, 869: the JPL group's 2018 assessment of the algorithm of that time, which retrieved in ice-free regions to within 35 km of the coast with the improved land and ice correction, found Arctic retrievals varying with sea-ice coverage, and an RMS difference to in situ north of 50N under about one salinity unit (registry record verified and abstract read there 2026-09-13; the article was not read; the V5 guide states no coastal reach of its own)"
  - id: dataset
    resource: ../datasets/smap-sss-jpl.md
    title: "This bundle's SMAP salinity dataset concept: the L3 structure, the relaxed L3 filter and the alternative producer"
---

# SMAP salinity near coasts and the sea-ice edge

**Mechanism.** The SMAP antenna receives energy from the entire
visible disk of the Earth weighted by its gain pattern, so even when
the main lobe is over water a portion of the signal comes from land,
and the JPL guide states that this bias on the retrieved salinity can
be as large as one practical salinity unit (negative, because land is
warmer at L-band than the sea).[^jpl-guide] Both producers correct
for it and then exclude what the correction cannot handle, and the
two sets of rules differ. In the JPL CAP product a look-up table of
gain-weighted land fraction by position and antenna azimuth, with a
monthly climatology of nearby land brightness temperature, corrects
every ocean observation within 1000 km of land; after correction the
bias is nearly flat in land fraction and the RMS is much reduced, but
the residual is not zero.[^jpl-guide] At Level 2A every observation
flagged as land or ice is removed and the cell is flagged (bits 7 and
8 of the L2B quality flag, with bit 0 the overall usability flag); at
Level 3 the guide filters on bits 5, 7 and 8 only (high ancillary
wind, land, ice), states that the criteria are deliberately relaxed,
and keeps as the only trace the weighted-average `land_fraction` and
`ice_fraction` of the observations that
survived.[^jpl-guide][^granule] The V5 guide states no coastal reach;
the JPL group's 2018 Arctic assessment of the algorithm of that time
reported retrievals in ice-free regions to within 35 km of the coast
with the improved land and ice correction, and Arctic retrievals
existing only where and when the ice allows.[^tang-2018] In the RSS product two land fractions are carried,
`gland` (gain-weighted) and `fland` (within the 3 dB footprint), with
a sidelobe correction from land tables; a cell with either above 0.1
gets no value (strong contamination); a cell with `gland` above 0.04
or `fland` above 0.005 is retrieved but excluded from the nine-cell
average that makes the standard 70 km product (moderate
contamination); `gland` above 0.001 is flagged light; since version
4 the product reaches 30 to 40 km from land.[^rss-release] For sea
ice the RSS product classifies each cell into zones from AMSR2
brightness temperatures by discriminant analysis, applies a sidelobe
correction, and reports for its 40 km Level 2 product, against HYCOM
in the Antarctic over a year, residual RMS errors of 2.2 practical
salinity units in zone 0 (cold open water inside the climatological
ice mask), 2.6 in zone 1, 3.1 in zone 2, 5.4 in zone 3 and 7.5 in zone
4 (25.4 before correction), with no retrieval in zone 5; cells in
zones 3 and 4 are excluded from the 70 km smoothing, and the producer
states that spatial, fore-aft and temporal averaging typically does
not reduce sea-ice error.[^rss-release][^meissner-2021] Where ice and
land meet, or where AMSR2 has no usable observation, neither
correction applies and no salinity is retrieved.[^rss-release]
Drifting icebergs go undetected in standard ice products and produce
spurious retrievals, which is part of what the discriminant method
exists to catch.[^meissner-2021] The JPL Level 3 carries an ancillary
ice concentration as `ice_fraction` but no zone or flag.[^granule]

**Wrong-result mode.** A salinity series for a river plume, a shelf, an
estuary or the marginal ice zone that averages the valid cells nearest
the coast or the ice edge is a series of whichever cells passed the
producer's exclusion in each window: the set changes with the
observation geometry, with the month (the JPL land climatology is
monthly) and with the ice season, so the series' variance and its
seasonal cycle contain the flagging, the coverage and the residual
contamination beside any ocean signal, and a trend across years of
changing ice cover is fitted to a changing sample. Residual land
contamination is a fresh bias whose size varies with distance and
direction from the coast, so a cross-shelf salinity gradient built
from the nearest cells is partly the correction's residual. A fresh
anomaly at the ice edge in the melt season can be sea-ice
contamination: several salinity units of residual error in the outer
zones, which averaging does not remove.[^rss-release][^meissner-2021]
Comparing the JPL and RSS products near a coast compares two
exclusion rules (different land-fraction thresholds, different
smoothing, and a reach the JPL group put at 35 km in its 2018
assessment against 30 to 40 km stated for RSS), so their
disagreement there is not an uncertainty for
either.[^tang-2018][^rss-release] A coastal analysis
that reads the L3 without the land and ice fields sees a complete
looking field with no flag, because the JPL Level 3 has none and the
RSS 70 km product has already dropped the flagged
cells.[^granule][^rss-release] In the RSS record the early months of
the mission (until 11 August 2015) carried a salty bias near the
continental shelves from the radiometer's two data-rate modes, removed
only in version 6.0.[^rss-release]

**Correct approach.** A coastal or ice-edge salinity series from
SMAP is defined on a fixed set of cells chosen with a stated
contamination threshold, read from the product's own fields
(`land_fraction` and `ice_fraction` in the JPL Level 3; `gland`,
`fland`, `gice_est` and, in the 8-day files, `sea_ice_zones` in the
RSS Level 3), with the number of contributing cells or observations
carried beside each value and the product's retrieval limit stated
as the inner edge of what it can say: 30 to 40 km from land for the
RSS product by its release notes, and for the JPL product the reach
the group reported in 2018 (35 km in ice-free conditions), since the
V5 guide states none.[^jpl-guide][^granule][^rss-release][^tang-2018]
A series in the marginal ice zone is read with the ice season as its
sampling, the cells' ice fraction or zone reported, and the residual
errors the producer quotes per zone beside the value; the RSS
producer's own recommendation for its near-real-time product, zone 0
only, is the conservative reading for any ice-edge
statement.[^rss-release] The products' L3 uncertainty fields carry
part of this (the RSS budget allocates half the land correction as
residual error and treats sea-ice contamination as a systematic term
that does not average down), so they are quoted, not replaced by a
root-N reduction.[^rss-release] What a coastal salinity series from
SMAP therefore is: the salinity of the product's retrievable cells,
corrected for the land the antenna sees and screened for the ice it
detects, at a resolution of 60 to 70 km, with the coast itself and
the ice-covered water outside it.[^dataset]

**Verification.** The JPL guide's land-correction, flagging, L3 and
data-definition sections are the producer's own statement of the
correction, the flags and the relaxed L3 filter, read in full on
2026-09-13; one monthly granule opened the same day confirms that the
Level 3 carries `land_fraction` and `ice_fraction` and no flag
variable.[^jpl-guide][^granule] The RSS release notes' land and
sea-ice sections, flag table and L3 section were read the same day
and are the source of every threshold and residual error quoted
above; the collection page's variable table shows the same fields in
the archived files.[^rss-release][^podaac-rss-8day] The two papers'
records were verified against the Crossref registry the same day
(title, authors, journal, year) and their abstracts read there: the
2021 paper states sea-ice contamination as a large error source and
icebergs as a cause of spurious retrievals, and the 2018 paper states
the 35 km coastal reach of the algorithm it assessed, the dependence
of Arctic retrievals on ice cover and the high-latitude RMS
difference; the publisher pages themselves were not
read.[^meissner-2021][^tang-2018]

[^jpl-guide]: SMAP Salinity and Wind Speed Data User's Guide, Version 5.0, JPL, November 2020
[^granule]: One JPL monthly granule, August 2026, opened and deleted on 2026-09-13
[^rss-release]: RSS SMAP Salinity Version 6.0 release notes, RSS Technical Report 011624
[^podaac-rss-8day]: PO.DAAC collection page, SMAP_RSS_L3_SSS_SMI_8DAY-RUNNINGMEAN_V6
[^meissner-2021]: Meissner and Manaster, 2021, Remote Sensing, doi:10.3390/rs13245120
[^tang-2018]: Tang and others, 2018, Remote Sensing, doi:10.3390/rs10060869
[^dataset]: This bundle's SMAP salinity dataset concept
