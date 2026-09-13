---
type: dataset
spheres: [hydrosphere]
title: "SMAP sea surface salinity, JPL CAP Level 3 (with the RSS product as the alternative producer)"
description: "The JPL Combined Active-Passive version 5.0 Level 3 sea surface salinity from the SMAP L-band radiometer: 8-day running means in daily files and monthly means on a 0.25-degree grid at about 60 km resolution from April 2015 onward, with a predicted uncertainty field, HYCOM reference salinity, and land and ice fractions; Remote Sensing Systems produces the alternative SMAP salinity (version 6.0) with a different algorithm, smoothing and flags."
tags: [smap, salinity, sss, l-band, radiometer, level3, jpl, cap, rss, podaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-13T21:00:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-13T21:10:06Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/128 }
resource: https://podaac.jpl.nasa.gov/dataset/SMAP_JPL_L3_SSS_CAP_8DAY-RUNNINGMEAN_V5
version: "JPL CAP V5.0 (user's guide dated 2020-11-12, PO.DAAC release date 2020-12-11), CMR-verified 2026-09-13 (provider POCLOUD) with granule ranges from a first-and-last granule search the same day: SMAP_JPL_L3_SSS_CAP_8DAY-RUNNINGMEAN_V5 (C2208422957-POCLOUD, DOI 10.5067/SMP50-3TPCS, daily files; the first granule record spans 2015-04-30T12 to 2015-05-08T12 and the last SMAP_L3_SSS_20260905_8DAYS_V5.0 spans 2026-09-01T12 to 2026-09-09T12) and SMAP_JPL_L3_SSS_CAP_MONTHLY_V5 (C2208423975-POCLOUD, DOI 10.5067/SMP50-3TMCS, first granule 2015-04, last 2026-08); the RSS alternative is identified in the body"
status: stable
stale_after: 2027-03-13
sources:
  - id: podaac-jpl-8day
    resource: https://podaac.jpl.nasa.gov/dataset/SMAP_JPL_L3_SSS_CAP_8DAY-RUNNINGMEAN_V5
    title: "PO.DAAC collection page, SMAP_JPL_L3_SSS_CAP_8DAY-RUNNINGMEAN_V5: description, DOI, release date, granule span and documentation links (read 2026-09-13)"
  - id: podaac-jpl-monthly
    resource: https://podaac.jpl.nasa.gov/dataset/SMAP_JPL_L3_SSS_CAP_MONTHLY_V5
    title: "PO.DAAC collection page, SMAP_JPL_L3_SSS_CAP_MONTHLY_V5: description, DOI, the variable table and the documentation links, one of which (the ATBD directory) returned 404 (read 2026-09-13)"
  - id: cmr-jpl-8day
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2208422957-POCLOUD.umm_json
    title: "CMR collection record for the JPL 8-day product: abstract, DOI, open-ended temporal extent from 2015-04-30T12:00 and documentation links (read 2026-09-13)"
  - id: cmr-jpl-monthly
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2208423975-POCLOUD.umm_json
    title: "CMR collection record for the JPL monthly product: abstract, DOI, open-ended temporal extent from 2015-04-01 and documentation links (read 2026-09-13)"
  - id: cmr-granules-jpl
    resource: https://cmr.earthdata.nasa.gov/search/granules.json?collection_concept_id=C2208422957-POCLOUD&page_size=1&sort_key=start_date
    title: "CMR granule searches run 2026-09-13 for the JPL 8-day (C2208422957) and monthly (C2208423975) collections, page_size=1 with sort_key=start_date and again sort_key=-start_date: first 8-day granule SMAP_L3_SSS_20150504_8DAYS_V5.0 (time_start 2015-04-30T12:00, time_end 2015-05-08T12:00), last SMAP_L3_SSS_20260905_8DAYS_V5.0; first monthly SMAP_L3_SSS_201504_MONTHLY_V5.0, last SMAP_L3_SSS_202608_MONTHLY_V5.0"
  - id: cmr-granules-rss
    resource: https://cmr.earthdata.nasa.gov/search/granules.json?collection_concept_id=C2832227567-POCLOUD&page_size=1&sort_key=start_date
    title: "CMR granule searches run 2026-09-13 for the RSS 8-day (C2832227567) and monthly (C2832226365) collections, the same parameters: first 8-day granule RSS_smap_SSS_L3_8day_running_2015_091_FNL_v06.0 (time_start 2015-03-28T12:00), last 2026_250 (2026-09-03 to 2026-09-11); first monthly 2015_04, last 2026_05"
  - id: jpl-guide
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/docs/JPL-CAP_V5/SMAP-SSS_JPL_V5.0_Documentation.pdf
    title: "SMAP Salinity and Wind Speed Data User's Guide, Version 5.0, Fore, Yueh, Tang and Hayashi, JPL, 12 November 2020 (42 pages, read in full 2026-09-13): version history, algorithm, land correction, uncertainty, L3 gridding, validation and the L2B and L3 data definitions"
  - id: granule
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-protected/SMAP_JPL_L3_SSS_CAP_MONTHLY_V5/2026/SMAP_L3_SSS_202608_MONTHLY_V5.0.nc
    title: "One monthly granule (August 2026, created 2026-09-03), opened with an Earthdata token on 2026-09-13 to read its variable names and attributes, then deleted; the file is behind Earthdata login"
  - id: podaac-rss-8day
    resource: https://podaac.jpl.nasa.gov/dataset/SMAP_RSS_L3_SSS_SMI_8DAY-RUNNINGMEAN_V6
    title: "PO.DAAC collection page, SMAP_RSS_L3_SSS_SMI_8DAY-RUNNINGMEAN_V6: description, DOI, release date and the variable table (read 2026-09-13)"
  - id: podaac-rss-monthly
    resource: https://podaac.jpl.nasa.gov/dataset/SMAP_RSS_L3_SSS_SMI_MONTHLY_V6
    title: "PO.DAAC collection page, SMAP_RSS_L3_SSS_SMI_MONTHLY_V6, with the variable table (read 2026-09-13)"
  - id: cmr-rss
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2832226365-POCLOUD.umm_json
    title: "CMR collection record for the RSS monthly product (the RSS 8-day record is C2832227567-POCLOUD): abstracts, DOIs and temporal extents, read 2026-09-13 with a short-name pattern search that showed the older RSS V4, V5 and V5.3 collections still catalogued (V5.3 with a stated end at the start of 2024)"
  - id: rss-release
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/docs/V6/Release_V6.0.pdf
    title: "Remote Sensing Systems SMAP Salinity Version 6.0 release notes and technical report (RSS Technical Report 011624, 73 pages; the summary, version changes, resolution, known issues, land and sea-ice sections, flags, L3 processing, formal uncertainty and data format sections read 2026-09-13)"
  - id: rss-readme
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/L3/RSS/README.txt
    title: "RSS SMAP-SSS known issues README at PO.DAAC: the bad-orbit and missing-ancillary lists on the producer's site, whose orbits are excluded from the L3 (read 2026-09-13)"
  - id: aquarius-readme
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/README.KnownIssues.txt
    title: "The file the JPL and RSS collections link as their anomalies and known issues: it is the Aquarius known-issues README and says nothing about SMAP (read 2026-09-13)"
  - id: fore-2016
    resource: https://doi.org/10.1109/TGRS.2016.2601486
    title: "Fore, Yueh, Tang, Stiles and Hayashi, 2016, Combined active/passive retrievals of ocean vector wind and sea surface salinity with SMAP, IEEE Transactions on Geoscience and Remote Sensing 54, 7396 to 7404: the CAP algorithm paper the guide and the files cite (registry record verified 2026-09-13; the record carries no abstract and the article was not read)"
  - id: tang-2017
    resource: https://doi.org/10.1016/j.rse.2017.08.021
    title: "Tang and others, 2017, Validating SMAP SSS with in situ measurements, Remote Sensing of Environment 200, 326 to 340: the validation paper the guide and the files cite (registry record verified 2026-09-13; the record carries no abstract and the article was not read)"
  - id: meissner-2018
    resource: https://doi.org/10.3390/rs10071121
    title: "Meissner, Wentz and Le Vine, 2018, The salinity retrieval algorithms for the NASA Aquarius version 5 and SMAP version 3 releases, Remote Sensing 10, 1121: the RSS algorithm line (registry record verified and abstract read there 2026-09-13; the article was not read)"
---

# SMAP sea surface salinity, JPL CAP Level 3

**Identity.** The Soil Moisture Active Passive observatory carries an
L-band (1.41 GHz) radiometer in a sun-synchronous 685 km orbit with a
1000 km swath; the collection description states global coverage in
about three days and an exact eight-day repeat, and that the radar
failed on 7 July 2015, so the salinity retrieval is radiometer-only
with an ancillary wind for the roughness
correction.[^podaac-jpl-8day][^jpl-guide] Two groups produce sea
surface salinity from it and PO.DAAC archives both. This concept's
product is the JPL line: the Combined Active-Passive (CAP) retrieval
developed for Aquarius and extended to SMAP, version 5.0, built on
version 5 of the SMAP Level 1B brightness temperatures with a
recalibration that reduces ascending versus descending
biases.[^podaac-jpl-8day][^fore-2016] The Level 3 comes in two
collections: an 8-day running mean written as one file per day, and
a monthly mean, both on a 0.25-degree grid with an approximate
spatial resolution the collection descriptions give as 60 km, and
with latencies the descriptions give as seven days and one month; the
Level 2B swath products (standard and two near-real-time variants) are
separate collections.[^podaac-jpl-8day][^podaac-jpl-monthly][^cmr-jpl-8day]
The Level 2B retrieval is a maximum-likelihood fit of salinity and
wind speed to the four brightness-temperature looks (fore and aft, H
and V), the wind constrained near the NCEP ancillary value and the
salinity free between 0 and 45; the Level 3 grids the L2B cells with
Gaussian weights of 30 km half-power radius and 45 km search radius
after filtering on three L2B quality bits (high ancillary wind, land,
ice), and the guide states that the L3 quality criteria are
deliberately relaxed to let the most data in.[^jpl-guide]

**Structure.** A monthly granule opened on 2026-09-13 holds, on
720 by 1440 cells: `smap_sss` (units written as 1e-3, valid 0 to 45),
`smap_sss_uncertainty`, `anc_sss` (HYCOM), `anc_sst` (kelvin),
`smap_spd` and `smap_high_spd` (10 m wind speed, the second with the
salinity fixed at the ancillary value, meant for storms), `weight`
(the sum of the Gaussian weights), `land_fraction`, `ice_fraction`,
`latitude`, `longitude` and one `time` (seconds since 2015-01-01, the
midpoint of the window); the fill value is -9999 and the file's
`references` attribute cites the CAP algorithm and validation
papers.[^granule][^fore-2016][^tang-2017] There is no quality-flag
variable at Level 3: the flags live in the L2B `quality_flag` and the
L3 is the filtered result.[^jpl-guide] The guide's L3 table names the
ice variable `ice_concentration`; the file names it `ice_fraction`,
which the collection page's variable table also
shows.[^jpl-guide][^granule][^podaac-jpl-monthly] File names are
`SMAP_L3_SSS_<date>_<N>DAYS_V5.0.nc`, with N the window in days
(8 or MONTHLY); the first 8-day granule record in CMR spans
2015-04-30T12:00 to 2015-05-08T12:00 and the first monthly record is
April 2015.[^jpl-guide][^cmr-granules-jpl]

**The alternative producer.** Remote Sensing Systems produces the
other SMAP salinity line for the NASA Ocean Salinity Science Team,
now version 6.0 (validated release 18 January 2024), as an 8-day
running mean and a monthly Level 3 on the same 0.25-degree grid, from
an algorithm that follows the Aquarius version 5 retrieval: a
Backus-Gilbert optimal interpolation to 40 km on the grid
(`sss_smap_40km`), then a nine-cell average to about 70 km
(`sss_smap`), which the producer names the standard product for open
ocean and coastal use, both with formal uncertainty fields
(`sss_smap_unc`, `sss_smap_40km_unc` and their nine components),
rain-filtered variants, the HYCOM reference, the gain-weighted and
footprint land fractions `gland` and `fland`, the estimated sea-ice
fraction `gice_est`, the ancillary SST and CCMP wind, and in the
8-day files the sea-ice zones and
flags.[^rss-release][^podaac-rss-8day][^podaac-rss-monthly][^meissner-2018]
Its collections are SMAP_RSS_L3_SSS_SMI_8DAY-RUNNINGMEAN_V6
(C2832227567-POCLOUD, DOI 10.5067/SMP60-3SPCS) and
SMAP_RSS_L3_SSS_SMI_MONTHLY_V6 (C2832226365-POCLOUD, DOI
10.5067/SMP60-3SMCS), released at PO.DAAC on 2024-03-26 per the
collection pages.[^podaac-rss-8day][^podaac-rss-monthly][^cmr-rss]
A granule search on 2026-09-13 found its first 8-day granule
starting 2015-03-28T12:00 and its first monthly granule in April
2015, and its last archived monthly file was May 2026, three months
behind the JPL monthly; the older RSS versions 4, 5 and the 5.3
evaluation set (with a stated end at the start of 2024) remain
catalogued.[^cmr-granules-rss][^cmr-rss] The two lines are not interchangeable; the
gotcha on the two producers carries the differences.

## Uncertainty

- **`smap_sss_uncertainty` is the product's own estimate.** At L2B it
  is the full width at half maximum of the likelihood in salinity
  space after the fit, so it includes the effects of cold water, radio
  frequency interference, model-function error and measurement noise
  together; at L3 it is propagated by variance with an approximate
  correction for the correlation of cells from the same orbit. The
  guide shows its zonal average tracking the RMS difference to HYCOM
  and offers a threshold on it as an alternative to the quality
  flag.[^jpl-guide]
- **Validation numbers, with their scope.** Against gridded Argo
  (Scripps and APDRC optimal interpolations), monthly, April 2015 to
  October 2020, averaged between 40S and 40N: bias below 0.03 and RMS
  difference below 0.3 (practical salinity). Against 102 tropical
  moored buoys at 1 m depth: RMS difference 0.2614 with a 7-day moving
  average and 0.2202 with a 30-day one (bias 0.08 in both).[^jpl-guide]
  These are low-latitude, open-ocean figures; the coastal, sea-ice and
  cold-water gotchas carry what happens outside that scope.
- **Land and ice fractions are the only contamination indicators at
  L3.** `land_fraction` and `ice_fraction` are the weighted averages
  of the L2B observations that survived filtering, so a cell with a
  value already passed the producer's relaxed criteria, and the
  fraction says how much of the antenna's view was land or ice in what
  remained.[^jpl-guide][^granule]
- **The RSS uncertainty is a different quantity.** It is a formal
  error budget built by perturbing nine inputs with random and
  systematic propagation rules, not a likelihood width; the two
  products' uncertainty fields do not compare directly.[^rss-release]

## Known issues

- [smap-sss-coastal-and-sea-ice-contamination](../gotchas/smap-sss-coastal-and-sea-ice-contamination.md):
  land and sea ice inside the antenna's view bias the retrieval by
  amounts up to several practical salinity units, the products' own
  corrections and exclusions define where a value exists, and a
  coastal or ice-edge series is a series of those decisions.
- [smap-sss-two-producers-differ](../gotchas/smap-sss-two-producers-differ.md):
  JPL CAP and RSS differ in input calibration, algorithm, smoothing,
  ancillary data, coverage and uncertainty definition; a series does
  not mix them and an anomaly uses its own product's climatology.
- [smap-sss-cold-water-sensitivity](../gotchas/smap-sss-cold-water-sensitivity.md):
  the radiometer's salinity sensitivity falls with SST, both producers
  flag SST below 5 C, and high-latitude values carry errors several
  times the tropical figures.
- The collections' "anomalies" link at PO.DAAC points to the Aquarius
  known-issues README, which documents Aquarius and not SMAP; the JPL
  guide lists no outages, and the RSS release notes list SMAP
  safeholds (17 June to 25 July 2019, no July 2019 monthly; 6 August
  to 21 September 2022, no August or September 2022 monthly), days
  without sea-ice masks or CCMP winds, and suspected undetected radio
  frequency interference near Japan, China and Taiwan, in the Arabian
  Sea and in the Mediterranean.[^aquarius-readme][^rss-release][^rss-readme]
- The JPL monthly collection's "ATBD, validation analysis" link is a
  directory that returned 404 on 2026-09-13; the user's guide link
  works and is the documentation of record here.[^podaac-jpl-monthly]
- The JPL guide is dated November 2020 and its revision history ends
  at version 5.0; the archive's files created in 2026 still carry
  `product_version` V5.0.[^jpl-guide][^granule]

[^podaac-jpl-8day]: PO.DAAC collection page, SMAP_JPL_L3_SSS_CAP_8DAY-RUNNINGMEAN_V5
[^podaac-jpl-monthly]: PO.DAAC collection page, SMAP_JPL_L3_SSS_CAP_MONTHLY_V5
[^cmr-jpl-8day]: CMR collection record, C2208422957-POCLOUD
[^cmr-jpl-monthly]: CMR collection record, C2208423975-POCLOUD
[^cmr-granules-jpl]: CMR granule searches, first and last granule, JPL 8-day and monthly collections, 2026-09-13
[^cmr-granules-rss]: CMR granule searches, first and last granule, RSS 8-day and monthly collections, 2026-09-13
[^jpl-guide]: SMAP Salinity and Wind Speed Data User's Guide, Version 5.0, JPL, November 2020
[^granule]: One JPL monthly granule, August 2026, opened and deleted on 2026-09-13
[^podaac-rss-8day]: PO.DAAC collection page, SMAP_RSS_L3_SSS_SMI_8DAY-RUNNINGMEAN_V6
[^podaac-rss-monthly]: PO.DAAC collection page, SMAP_RSS_L3_SSS_SMI_MONTHLY_V6
[^cmr-rss]: CMR collection records for the RSS products
[^rss-release]: RSS SMAP Salinity Version 6.0 release notes, RSS Technical Report 011624
[^rss-readme]: RSS SMAP-SSS known issues README, PO.DAAC
[^aquarius-readme]: Aquarius known-issues README, PO.DAAC
[^fore-2016]: Fore and others, 2016, IEEE Transactions on Geoscience and Remote Sensing, doi:10.1109/TGRS.2016.2601486
[^tang-2017]: Tang and others, 2017, Remote Sensing of Environment, doi:10.1016/j.rse.2017.08.021
[^meissner-2018]: Meissner, Wentz and Le Vine, 2018, Remote Sensing, doi:10.3390/rs10071121
