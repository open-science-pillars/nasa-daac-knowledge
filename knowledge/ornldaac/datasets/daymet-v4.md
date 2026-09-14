---
type: dataset
spheres: [atmosphere, geosphere]
title: "Daymet Version 4 (release R1): daily surface weather on a 1 km grid for North America, Hawaii and Puerto Rico"
description: "Daily minimum and maximum temperature, precipitation, shortwave radiation, vapor pressure, snow water equivalent and day length interpolated from weather stations onto a 1 km Lambert conformal conic grid, one netCDF file per variable, region and year, on a 365-day calendar; the current release is Version 4 R1, whose only change to existing Version 4 files was a rerun of 2020 and 2021 with corrected station inputs; later years are appended under R1. Uncertainty ships as a separate station-level cross-validation dataset, not as a field in the grids."
tags: [daymet, surface-weather, temperature, precipitation, gridded, lambert-conformal-conic, ornldaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:40:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-14T12:17:15Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/143 }
resource: https://doi.org/10.3334/ORNLDAAC/2129
version: "Daymet Version 4 R1 (ORNL DAAC version 4.1, DOI 10.3334/ORNLDAAC/2129, CMR short name Daymet_Daily_V4R1_2129, concept C2532426483-ORNL_CLOUD), CMR-verified 2026-09-14 with 1,176 granules covering 1950-01-01 through 2025-12-31; Version 4 (DOI 10.3334/ORNLDAAC/1840) is superseded and its landing page marks access restricted"
sources:
  - id: ornl-v4-guide
    resource: https://daac.ornl.gov/DAYMET/guides/Daymet_Daily_V4.html
    title: "ORNL DAAC user guide, Daymet Daily Surface Weather Data on a 1-km Grid for North America, Version 4 (documentation revision 2024-06-17): the variables and units, the file naming, the three regions and their extents, the projection parameters, the Daymet calendar, the station inputs, the cross-validation protocol and the release record"
  - id: ornl-v4-landing
    resource: https://daac.ornl.gov/cgi-bin/dsviewer.pl?ds_id=1840
    title: "ORNL DAAC landing page for Daymet Version 4 (DOI 10.3334/ORNLDAAC/1840): the notice that Version 4 R1 supersedes it as of 2022-11-01, the version history and the restricted-access notice"
  - id: cmr-daily-v4r1
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2532426483-ORNL_CLOUD.umm_json
    title: "CMR collection record for Daymet Daily Version 4 R1 (Daymet_Daily_V4R1_2129, version 4.1): the abstract with the R1 statement, the temporal and spatial extents, and the granule listing read through the granule search"
  - id: cmr-collections
    resource: https://cmr.earthdata.nasa.gov/search/collections.json?keyword=Daymet&page_size=50
    title: "CMR collection search for Daymet: the concept ids and short names of the four Version 4 R1 collections at ORNL_CLOUD"
  - id: cmr-xval-v4r1
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2531991823-ORNL_CLOUD.umm_json
    title: "CMR collection record for Daymet Station-Level Inputs and Cross-Validation, Version 4 R1 (Daymet_xval_V4R1_2132, DOI 10.3334/ORNLDAAC/2132)"
  - id: ornl-v4-xval-guide
    resource: https://daac.ornl.gov/DAYMET/guides/Daymet_V4_Stn_Level_CrossVal.html
    title: "ORNL DAAC user guide, Daymet Station-Level Inputs and Cross-Validation Result for North America, Version 4: what the cross-validation files hold and what can be derived from them"
  - id: daymet-overview
    resource: https://daymet.ornl.gov/overview
    title: "Daymet project site, description page: the inputs, the 2-degree processing tiles and their TileID, the mosaics the DAAC builds from them, the calendar and the projection"
  - id: daymet-getdata
    resource: https://daymet.ornl.gov/getdata
    title: "Daymet project site, get data page: the direct download, THREDDS, single pixel, web service, tiled subset and climatology access paths"
  - id: daymet-web-services
    resource: https://daymet.ornl.gov/web_services.html
    title: "Daymet project site, web services page: the netCDF subset service and its projection note, and the single pixel extraction service with its stated latitude and longitude limits"
  - id: daymet-citations
    resource: https://daymet.ornl.gov/citations
    title: "Daymet project site, citations page: the DOIs of the Version 4 R1 daily, monthly, annual and cross-validation datasets and the method references"
  - id: thornton-2021
    resource: https://doi.org/10.1038/s41597-021-00973-0
    title: "Thornton and others, 2021, Gridded daily weather data for North America with comprehensive uncertainty quantification, Scientific Data 8, article 190: the Version 4 methods, the cross-validation results and the usage notes"
  - id: crossref-thornton-2021
    resource: https://api.crossref.org/works/10.1038/s41597-021-00973-0
    title: "Crossref registry record for Thornton and others 2021: title, authors, journal, volume and publication date"
status: stable
stale_after: 2027-03-14
---

# Daymet Version 4 (release R1)

**Identity.** Daymet is a gridded estimate of daily surface weather
produced by interpolating and extrapolating ground station
observations: daily minimum and maximum temperature, precipitation,
shortwave radiation, water vapor pressure, snow water equivalent and
day length on a 1 km by 1 km grid over continental North America
(Canada, the United States and Mexico), Hawaii and Puerto Rico, from
1980 for North America and Hawaii and from 1950 for Puerto Rico,
through the most recent full calendar year; each new year is processed
at the close of the calendar year.[^ornl-v4-guide][^cmr-daily-v4r1]
The core inputs are daily observations of minimum temperature, maximum
temperature and precipitation from the Global Historical Climatology
Network daily dataset, assembled as three separate station files for
the three regions, which are run through the algorithm
independently.[^ornl-v4-guide][^thornton-2021] The other four
variables are derived: day length from location and date, and
shortwave radiation, vapor pressure and snow water equivalent from the
interpolated temperature and precipitation by theory and empirical
relationships.[^ornl-v4-guide][^thornton-2021] The Version 4 methods
are the subject of Thornton and others 2021 in Scientific Data, whose
registry record names six authors, the journal and the 2021
publication.[^thornton-2021][^crossref-thornton-2021]

**Variables and units.** Seven variables, each in its own file:
tmin and tmax (daily minimum and maximum 2 m air temperature, degrees
Celsius), prcp (daily total precipitation as water-equivalent depth,
millimeters), srad (incident shortwave radiation flux density in watts
per square meter, an average over the daylight period, so the daily
total in megajoules per square meter is srad times dayl divided by one
million), vp (daily average water vapor pressure, pascals), swe (snow
water equivalent, kilograms per square meter) and dayl (day length,
seconds per day, the period the sun is above a flat
horizon).[^ornl-v4-guide]

**Structure.** One CF-compliant netCDF file per variable, region and
year, named daymet_v4_daily_<region>_<variable>_<year>.nc with region
na, hi or pr; the three regions are separate files with separate
extents: continental North America from 178.13 W to 53.06 W and from
14.07 N to 82.91 N, Hawaii from 160.31 W to 154.77 W and 17.95 N to
23.52 N, Puerto Rico from 67.99 W to 64.12 W and 16.84 N to 19.94
N.[^ornl-v4-guide] The grid is a Lambert conformal conic projection
in meters (standard parallels 25 N and 60 N, central meridian 100 W,
latitude of origin 42.5 N, WGS 84 spheroid) with a stated PROJ
definition in the guide.[^ornl-v4-guide][^daymet-overview] Every
Daymet year has 365 days: leap years keep February 29 and drop
December 31.[^ornl-v4-guide][^daymet-overview] The algorithm runs on
2-degree by 2-degree tiles identified by a TileID that is the same in
every year, and the DAAC mosaics the tiles into the seamless per-region
files; the tiles remain available as smaller subsets through the
THREDDS server, and the single pixel service extracts one cell's
series for a point.[^daymet-overview][^daymet-getdata][^daymet-web-services]
The CMR collection for the daily product holds 1,176 granules, one per
variable, region and year, with the Puerto Rico granules starting in
1950 and the collection's temporal extent ending 2025-12-31 on the
verification date; no granule is a tile.[^cmr-daily-v4r1] Version and
software version are recorded in each file's global attributes
Version_software and Version_data, and the DAAC's versioning practice
keeps the version number when a release only appends a new
year.[^ornl-v4-guide]

**Releases and identifiers.** Version 4 was published 2020-12-15
under DOI 10.3334/ORNLDAAC/1840; Version 4 R1 was published 2022-11-01
under DOI 10.3334/ORNLDAAC/2129 and supersedes it, and the Version 4
landing page marks its files as access
restricted.[^ornl-v4-landing] R1 re-derived every 2020 and 2021 file
with corrected station inputs, after a large share of Canadian
stations were found to lack January readings in the inputs used for
those two years; files for other years are unchanged from Version
4.[^cmr-daily-v4r1] The four Version 4 R1 collections in CMR, all at
provider ORNL_CLOUD and version 4.1: daily
C2532426483-ORNL_CLOUD (Daymet_Daily_V4R1_2129), annual climate
summaries C2531982907-ORNL_CLOUD (Daymet_Annual_V4R1_2130), monthly
climate summaries C2532007210-ORNL_CLOUD (Daymet_Monthly_V4R1_2131)
and station-level inputs and cross-validation C2531991823-ORNL_CLOUD
(Daymet_xval_V4R1_2132).[^cmr-collections][^daymet-citations] The
project site also lists a monthly-latency daily product under DOI
10.3334/ORNLDAAC/1904, a separate collection not described
here.[^daymet-citations] Version 4 shifted the timing of precipitation
relative to Version 3 by moving whole-day station totals to the
previous day where the station reported before noon, so a given
calendar day in Version 3 corresponds best to the previous day in
Version 4 during an event.[^thornton-2021]

## Uncertainty

- **No uncertainty variable ships in the gridded files.** The daily
  files carry the seven weather variables and nothing else; the
  product's uncertainty statement is a separate dataset, the
  station-level inputs and cross-validation results, one file per
  variable, region and year for tmin, tmax and prcp, holding each
  station's observations beside the prediction made with that station
  withheld, with a station metadata file for every
  combination.[^ornl-v4-guide][^ornl-v4-xval-guide][^cmr-xval-v4r1]
- **The cross-validation covers the three primary variables only.**
  Prediction errors exist for temperature and precipitation; srad,
  vp, swe and dayl are derived from them and have no cross-validation
  of their own in the product.[^thornton-2021][^ornl-v4-xval-guide]
- **Domain-wide daily error levels, from the paper.** Averaged over
  the 40 years and all stations, the mean daily absolute error is
  about 1.78 degrees Celsius for tmin and 1.52 degrees Celsius for
  tmax (1.75 for tmax in Version 3; tmin unchanged); the daily precipitation error is lower in
  recent years than early in the record as the station networks
  grew.[^thornton-2021]
- **The error is not uniform.** Station density, terrain and
  large-scale atmospheric patterns all contribute to spatial
  heterogeneity in the cross-validation statistics, and the algorithm
  carries constraints written for regions of very sparse and
  horizontally skewed station networks; the regional error for an
  application is read from the cross-validation files, not from the
  domain average.[^thornton-2021][^ornl-v4-xval-guide]
- **All Daymet data are provisional and subject to revision**, per
  the guide, and the R1 release is the live example: two whole years
  changed under a new DOI.[^ornl-v4-guide][^cmr-daily-v4r1]

## Known issues

- [daymet-365-day-year](../gotchas/daymet-365-day-year.md): every
  year has 365 days and December 31 is dropped in leap years, so a
  positional or generated-date join misaligns after February in a
  leap year.
- [daymet-lcc-projection-and-cell-area](../gotchas/daymet-lcc-projection-and-cell-area.md):
  the grid is Lambert conformal conic meters, and a cell's ground
  area is one square kilometer only on the standard parallels.
- [daymet-tiles-mosaics-regions](../gotchas/daymet-tiles-mosaics-regions.md):
  tiles and mosaics are the same estimates in different files, and
  the three region files differ in extent and start year.
- [daymet-v4-r1-correction](../gotchas/daymet-v4-r1-correction.md):
  R1 changed every 2020 and 2021 file and no earlier year.
- [daymet-station-sparse-error](../gotchas/daymet-station-sparse-error.md):
  the values are interpolated from stations, and station-sparse
  terrain carries larger error that the cross-validation files
  quantify.

[^ornl-v4-guide]: ORNL DAAC user guide, Daymet Daily V4, revision 2024-06-17, read 2026-09-14
[^ornl-v4-landing]: ORNL DAAC landing page for Daymet Daily V4 (ds_id 1840), read 2026-09-14
[^cmr-daily-v4r1]: CMR collection C2532426483-ORNL_CLOUD and its granule search, read 2026-09-14
[^cmr-collections]: CMR collection search for Daymet, read 2026-09-14
[^cmr-xval-v4r1]: CMR collection C2531991823-ORNL_CLOUD, read 2026-09-14
[^ornl-v4-xval-guide]: ORNL DAAC user guide, Daymet V4 station-level cross-validation, read 2026-09-14
[^daymet-overview]: Daymet project site, description page, read 2026-09-14
[^daymet-getdata]: Daymet project site, get data page, read 2026-09-14
[^daymet-web-services]: Daymet project site, web services page, read 2026-09-14
[^daymet-citations]: Daymet project site, citations page, read 2026-09-14
[^thornton-2021]: Thornton and others, 2021, Scientific Data 8, 190, doi:10.1038/s41597-021-00973-0, read at nature.com 2026-09-14
[^crossref-thornton-2021]: Crossref record for doi:10.1038/s41597-021-00973-0, read 2026-09-14
