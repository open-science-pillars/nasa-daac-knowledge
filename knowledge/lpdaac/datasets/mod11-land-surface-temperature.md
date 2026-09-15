---
type: dataset
spheres: [geosphere, biosphere]
title: "MOD11A1 and MOD11A2 version 6.1: Terra MODIS clear-sky land surface temperature and classified emissivity, daily and eight-day, on 1 km sinusoidal tiles"
description: "MOD11A1 is the daily Terra MODIS land surface temperature and emissivity product at 1 km on the sinusoidal grid, gridded from the MOD11_L2 swath retrievals of the generalized split-window algorithm on bands 31 and 32 under the MOD35 clear-sky test; MOD11A2 is the simple average of the MOD11A1 values over eight days. Each carries separate daytime and nighttime temperature fields (uint16 kelvin times 0.02, fill 0) with their own quality bytes, local solar view times, signed view zenith angles and clear-sky coverage counts, plus band 31 and 32 emissivities assigned from land cover class rather than retrieved. Collection 6.1 keeps the Collection 6 algorithm and format and differs by the Level-1B calibration. Only clear-sky observations exist in the files, so every mean built from them is a clear-sky mean."
tags: [mod11, mod11a1, mod11a2, modis, terra, land-surface-temperature, lst, emissivity, sinusoidal, lpdaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T13:40:00Z }
resource: https://lpdaac.usgs.gov/products/mod11a1v061/
version: "Collection 6.1 (MOD11A1 DOI 10.5067/MODIS/MOD11A1.061, CMR C1748058432-LPCLOUD; MOD11A2 DOI 10.5067/MODIS/MOD11A2.061, CMR C2269056084-LPCLOUD; provider LPCLOUD), verified 2026-09-15: MOD11A1 temporal extent 2000-02-24 to present and MOD11A2 2000-02-18 to present, both with the ends-at-present flag set and collection progress ACTIVE, 3,042,160 and 386,325 granules on the product pages that day; the user guide read is the Collection 6 guide of June 2019 with its Collection 6.1 cover note"
status: draft
stale_after: 2027-03-15
citation:
  access_date_required: true
  authority: https://lpdaac.usgs.gov/
  data: "Wan, Z., Hook, S., and Hulley, G. (2021). MODIS/Terra Land Surface Temperature/Emissivity Daily L3 Global 1km SIN Grid V061 [Dataset]. NASA Land Processes Distributed Active Archive Center, accessed {access_date}, 10.5067/MODIS/MOD11A1.061"
  doi: "10.5067/MODIS/MOD11A1.061"
  note: "the citation text is the one the LP DAAC product page renders on 2026-09-15; the eight-day product is cited the same way with its own title and DOI 10.5067/MODIS/MOD11A2.061; both are DataCite DOIs, for which the Crossref API returns no record, and both were verified by their resolution at doi.org; the access date matters because the collection is in forward processing and the guide says further reprocessing is anticipated"
sources:
  - id: a1-page
    resource: https://lpdaac.usgs.gov/products/mod11a1v061/
    title: "LP DAAC product page for MOD11A1 v061, read 2026-09-15 (the lpdaac.usgs.gov address redirects to the NASA Earthdata data catalog page for C1748058432-LPCLOUD): description, version description, DOI, CMR concept id, temporal extent, granule count, the twelve-layer variables table with data type, fill, valid range, scale and offset, the file name convention, the citation, the documents it links and the validation stage statement"
  - id: a2-page
    resource: https://lpdaac.usgs.gov/products/mod11a2v061/
    title: "LP DAAC product page for MOD11A2 v061, read 2026-09-15 (redirects to the Earthdata catalog page for C2269056084-LPCLOUD): description, the simple average statement, the eight-day period rationale, DOI, concept id, temporal extent, granule count, the variables table and the citation"
  - id: user-guide
    resource: https://lpdaac.usgs.gov/documents/715/MOD11_User_Guide_V61.pdf
    title: "Collection-6 MODIS Land Surface Temperature Products Users' Guide (Wan, June 2019) with the Collection 6.1 cover note, read 2026-09-15: sections 1, 2 (MOD11_L2, Tables 2, 3 and 8), 3 (MOD11A1, Tables 9 and 13), 4 (MOD11A2, Tables 14 and 18), the MOD11B1 description in section 5, section 10.1 (the monthly product's clear-sky day flags, one per bit), and the publications list"
  - id: atbd
    resource: https://lpdaac.usgs.gov/documents/119/MOD11_ATBD.pdf
    title: "MODIS Land-Surface Temperature Algorithm Theoretical Basis Document, version 3.3, April 1999 (Wan), read 2026-09-15 in its sections 2.1 (the 1 K accuracy specification), 2.2 (thermal infrared LST exists only in clear sky), 3.1.1.1 (the classification-based emissivity table) and 3.1.5.3 (emissivity knowledge base uncertainty)"
  - id: cmr-a1
    resource: https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=MOD11A1&version=061
    title: "CMR collection record for MOD11A1 v061 (concept C1748058432-LPCLOUD, revision 64 of 2026-04-16), read 2026-09-15: DOI, platform Terra and instrument MODIS, temporal extent with ends-at-present, the sinusoidal description, HDF-EOS2 at 2 MB average, distribution over HTTPS and the Earthdata Cloud, the S3 buckets and credentials endpoint, and the related documents including the LDOPE quality site and the file specification"
  - id: cmr-a2
    resource: https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=MOD11A2&version=061
    title: "CMR collection record for MOD11A2 v061 (concept C2269056084-LPCLOUD, revision 52 of 2026-04-16), read 2026-09-15: the same fields for the eight-day product, HDF-EOS2 at 3.6 MB average"
  - id: doi-a1
    resource: https://doi.org/10.5067/MODIS/MOD11A1.061
    title: "The MOD11A1 DOI, resolved 2026-09-15 to the Earthdata catalog page; a DataCite DOI, for which the Crossref API holds no record"
  - id: doi-a2
    resource: https://doi.org/10.5067/MODIS/MOD11A2.061
    title: "The MOD11A2 DOI, resolved 2026-09-15 to the Earthdata catalog page; a DataCite DOI, for which the Crossref API holds no record"
  - id: wan-2014
    resource: https://doi.org/10.1016/j.rse.2013.08.027
    title: "Wan (2014), New refinements and validation of the collection-6 MODIS land-surface temperature/emissivity product, Remote Sensing of Environment 140, 36 to 45: the paper the user guide cites for the Collection 6 algorithm refinements; the DOI resolves to an Elsevier page on a domain outside this seed's reading list, so the paper is cited on its registry record and on what the user guide reports of it"
  - id: wan-2014-crossref
    resource: https://api.crossref.org/works/10.1016/j.rse.2013.08.027
    title: "Crossref record for 10.1016/j.rse.2013.08.027, read 2026-09-15: title, the one author Zhengming Wan, journal, volume 140, pages 36 to 45, issued January 2014, ISSN 0034-4257; the record carries no abstract"
  - id: l30
    resource: hls-l30.md
    title: "This bundle's HLS L30 concept, whose layer table carries the two TIRS bands as top-of-atmosphere brightness temperature, not atmospherically corrected"
  - id: clear-sky-gotcha
    resource: ../gotchas/mod11-clear-sky-and-view-time.md
    title: "This bundle's gotcha on the clear-sky sampling and the varying view time"
  - id: day-night-gotcha
    resource: ../gotchas/mod11-day-and-night-are-different.md
    title: "This bundle's gotcha on the separate daytime and nighttime fields"
  - id: emissivity-gotcha
    resource: ../gotchas/mod11-emissivity-is-classified.md
    title: "This bundle's gotcha on the classified emissivity layers"
---

# MOD11A1 and MOD11A2 version 6.1

**Identity.** MOD11A1 is "MODIS/Terra Land Surface Temperature/Emissivity
Daily L3 Global 1km SIN Grid V061", CMR collection C1748058432-LPCLOUD
(provider LPCLOUD, short name MOD11A1, version 061, DOI
10.5067/MODIS/MOD11A1.061), platform Terra, instrument MODIS, temporal
extent 2000-02-24 to the present with the ends-at-present flag set,
processing level 3.[^cmr-a1][^a1-page] MOD11A2 is the eight-day
product, "MODIS/Terra Land Surface Temperature/Emissivity 8-Day L3
Global 1km SIN Grid V061", C2269056084-LPCLOUD (short name MOD11A2,
version 061, DOI 10.5067/MODIS/MOD11A2.061), temporal extent
2000-02-18 to the present.[^cmr-a2][^a2-page] Both DOIs resolve at
doi.org to the Earthdata catalog pages.[^doi-a1][^doi-a2] On 2026-09-15
the product pages listed 3,042,160 and 386,325 granules.[^a1-page][^a2-page]
Each granule is one tile of the MODIS sinusoidal grid, 1200 rows by
1200 columns, named like `MOD11A1.A2025222.h17v10.061.2025223235730.hdf`:
short name, acquisition day of year, tile, collection, production
time.[^a1-page] The nominal 1 km cell is 0.928 km on the
ground.[^user-guide] The Aqua equivalents are MYD11A1 and MYD11A2 and
are not described here.[^user-guide]

Collection 6.1 is identical in format to Collection 6 and contains no
change to the science algorithm; what changed are the Level-1B inputs,
with calibration changes to the response versus scan angle approach,
corrections for optical crosstalk in the Terra infrared bands, a
correction to the Terra forward look-up table for 2012 to 2017 and a
polarization correction on the reflective bands.[^user-guide][^a1-page][^cmr-a1]
The user guide is therefore the Collection 6 guide of June 2019 with
a Collection 6.1 cover note, and it points to Wan (2014) for the
Collection 6 refinements.[^user-guide][^wan-2014][^wan-2014-crossref]

## How the daily product is made

The chain starts in the swath product MOD11_L2, retrieved by the
generalized split-window algorithm (Wan and Dozier 1996) from the
Level-1B radiances in bands 31 (11.03 micrometres) and 32 (12.02
micrometres), with the MOD03 geolocation and land/water mask, the
MOD35_L2 cloud mask, the MOD07_L2 atmospheric profile, the MCDLC1KM
land cover and the MOD10_L2 snow cover as inputs.[^user-guide] A pixel
is retrieved only if it has nominal radiances in both bands, is on
land or inland water, and is clear by MOD35 at 95 per cent confidence
or better in the Level-2 product; the Level-3 daily products admit a
looser clear-sky rule, 95 per cent over land at or below 2000 m,
66 per cent over land above 2000 m and 66 per cent over lakes, and
remove cloud-contaminated values afterwards with constraints on the
temporal variation of clear-sky LST over 32 days (Wan 2008), a step
the guide says has no easy equivalent in the Level-2
product.[^user-guide] The algorithm theoretical basis document states
the consequence in one sentence: the MODIS LST product based on
thermal infrared data will only be available in clear sky
conditions.[^atbd]

MOD11A1 maps every valid clear-sky LST of the day's swaths onto the
sinusoidal grid, averaging overlapping pixels with their overlap areas
as weights.[^user-guide] Above 30 degrees latitude there can be several
clear-sky observations of one cell in a day; the guide says that in
Collection 6 the value at every grid cell comes from a single
observation, chosen as the clear-sky LST at the smaller view zenith
angle unless the one at the larger angle is warmer by at least 2 K,
while the product page says the cell value is the average of all
qualifying observations. The two statements differ and both are
recorded here as read ([the clear-sky and view time
gotcha](../gotchas/mod11-clear-sky-and-view-time.md)).[^user-guide][^a1-page][^clear-sky-gotcha]
The daytime and nighttime fields are produced separately, each with
its own quality byte, view time and view angle
([the day and night gotcha](../gotchas/mod11-day-and-night-are-different.md)).[^user-guide][^day-night-gotcha]
The split-window coefficients are two sets for hot and warm bare soil
between 38 degrees south and 49.5 degrees north, one for daytime and
one for nighttime, and the Collection 6 algorithm adds a quadratic
term in the band 31 minus band 32 brightness temperature
difference.[^user-guide]

Emissivity in bands 31 and 32 is estimated by the classification-based
method (Snyder and others 1998) from the land cover class and the
daily snow cover, not retrieved from the radiances; Collection 6 adds
a prototype adjustment of up to 0.0063 in band 31, and the same amount
the other way in band 32, for arid and semi-arid areas ([the
emissivity gotcha](../gotchas/mod11-emissivity-is-classified.md)).[^user-guide][^atbd][^emissivity-gotcha]
Retrieved emissivities exist in the 6 km MOD11B1 product from the
day/night algorithm, a different product.[^user-guide]

## Layers

The guide's Table 9 and the product page variables table agree on the
twelve scientific data sets of MOD11A1:[^user-guide][^a1-page]

| Layer | Content | Type | Valid range | Fill | Scale | Offset |
|---|---|---|---|---|---|---|
| LST_Day_1km | daytime land surface temperature, kelvin | uint16 | 7500 to 65535 | 0 | 0.02 | 0 |
| QC_Day | quality control for daytime LST and emissivity, bit field | uint8 | 0 to 255 | none | | |
| Day_view_time | local solar time of the daytime observation, hours | uint8 | 0 to 240 | 255 | 0.1 | 0 |
| Day_view_angl | view zenith angle of the daytime observation, degrees | uint8 | 0 to 130 | 255 | 1.0 | -65 |
| LST_Night_1km | nighttime land surface temperature, kelvin | uint16 | 7500 to 65535 | 0 | 0.02 | 0 |
| QC_Night | quality control for nighttime LST and emissivity, bit field | uint8 | 0 to 255 | none | | |
| Night_view_time | local solar time of the nighttime observation, hours | uint8 | 0 to 240 | 255 | 0.1 | 0 |
| Night_view_angl | view zenith angle of the nighttime observation, degrees | uint8 | 0 to 130 | 255 | 1.0 | -65 |
| Emis_31 | band 31 emissivity | uint8 | 1 to 255 | 0 | 0.002 | 0.49 |
| Emis_32 | band 32 emissivity | uint8 | 1 to 255 | 0 | 0.002 | 0.49 |
| Clear_day_cov | day clear-sky coverage | uint16 | 1 to 65535 | 0 | 0.0005 | 0 |
| Clear_night_cov | night clear-sky coverage | uint16 | 1 to 65535 | 0 | 0.0005 | 0 |

The temperature is the stored integer times 0.02, so the valid range
starts at 150 K; the emissivity is the stored integer times 0.002 plus
0.49, so it runs from 0.492 to 1.0.[^user-guide] The view time is local
solar time, defined as UTC plus the cell's longitude in degrees divided
by 15, wrapped into 0 to 24 hours; the data day in the file name is
UTC, so the local solar data day of a cell can differ from it by one
day.[^user-guide] The view angle offset of -65 was introduced in
Collection 6 so that a negative sign means MODIS viewed the cell from
the east; the zenith angle itself is the magnitude, and the guide says
the side matters for the view angle effect on temporal variations in
rugged terrain.[^user-guide]

MOD11A2 has the same twelve layer names with two differences: the
temperatures are the eight-day averages, the view time and view angle
are the averages over the days used, and the coverage layers are
Clear_sky_days and Clear_sky_nights, uint8 with valid range 1 to 255,
fill 0 and no scale, described by the guide as the days in clear-sky
conditions with valid LSTs and by the product page as bit
fields.[^user-guide][^a2-page] They are not counts: the guide says of
the monthly MOD11C3 product that the days and nights in clear-sky
conditions with validated LSTs are flagged in each bit of two 32-bit
unsigned integers, and the eight-day layer's byte with a range to 255
holds one flag per day of the period in the same design, so the
number of days that contributed is the number of set bits, not the
stored value. Which bit stands for the first day of the period is not
stated in the sources read here, and the file specification the CMR
record links is on a domain outside this seed's reading list.[^user-guide][^a2-page][^cmr-a2]
The guide's Table 14 gives Night_view_time the long name "Average view
zenith angle of nighttime Land-surface Temperature", in hours; the
name is read here as a copying slip for the average nighttime view
time, since the units, range and scale are those of the time
layer.[^user-guide] The eight-day period was chosen because twice
eight days is the ground track repeat period of Terra, and the
compositing is a simple average of the MOD11A1 values that exist in
the period.[^user-guide][^a2-page]

## Quality

QC_Day and QC_Night pack four two-bit fields, bit 0 the least
significant (Table 13 for MOD11A1, Table 18 with the same layout for
MOD11A2):[^user-guide]

| Bits | Field | Values |
|---|---|---|
| 1 and 0 | mandatory QA | 00 LST produced, good quality; 01 LST produced, other quality, examine the detailed QA; 10 LST not produced due to cloud; 11 LST not produced for reasons other than cloud |
| 3 and 2 | data quality | 00 good; 01 other quality; 10 and 11 to be defined |
| 5 and 4 | emissivity error | 00 at most 0.01; 01 at most 0.02; 10 at most 0.04; 11 above 0.04 |
| 7 and 6 | LST error | 00 at most 1 K; 01 at most 2 K; 10 at most 3 K; 11 above 3 K |

The guide notes that a QC value of 0 means good quality only when the
LST is valid: where the LST is fill, the mandatory bits read 10 or 11,
and the two layers are read together.[^user-guide] The Level-2 product
carries a sixteen-bit QC with more fields, among them an emissivity
flag whose value 00 is "inferred from land cover type", and a
per-pixel Error_LST layer that the guide calls conservative and blind
to cloud contamination; neither is carried into the daily and
eight-day tiles.[^user-guide] Granule metadata carry QAPercentGoodQuality,
QAPercentOtherQuality, QAPercentNotProducedCloud and
QAPercentNotProducedOther, computed over all pixels of the
tile.[^user-guide] The product page states that validation at stage 2
has been achieved for all MODIS land surface temperature and
emissivity products and points to the LDOPE land product quality
assessment site for known issues; that site is on a domain outside
this seed's reading list and its contents are not represented
here.[^a1-page][^cmr-a1]

## Access

Cloud-hosted: both product pages mark the collections cloud enabled,
and the CMR records distribute them over HTTPS and the Earthdata Cloud
in HDF-EOS2 at 2 MB (daily) and 3.6 MB (eight-day) per file from the
buckets `s3://lp-prod-protected/MOD11A1.061` and
`s3://lp-prod-protected/MOD11A2.061` with public counterparts, region
us-west-2, temporary credentials at
data.lpdaac.earthdatacloud.nasa.gov/s3credentials.[^a1-page][^cmr-a1][^cmr-a2]
The data links are Earthdata Search on the collection concept ids and
AppEEARS.[^cmr-a1][^cmr-a2] The CMR records link the file
specifications on the LAADS site; those were not read.[^cmr-a1]

## Uncertainty

The tiles carry no per-pixel temperature uncertainty. What stands in:

- **The accuracy specification.** The algorithm document sets 1 K at
  1 km under clear-sky conditions for LST and 0.02 for the band 31
  and 32 emissivities, and says the generalized split-window
  algorithm is better than 1 K in most cases for land cover types
  with known emissivities.[^atbd]
- **The QC error classes.** Bits 6 and 7 place each pixel's average
  LST error in one of four classes up to and beyond 3 K, and bits 4
  and 5 the emissivity error up to and beyond 0.04; they are classes,
  not values.[^user-guide]
- **The Level-2 Error_LST layer.** An estimated value per swath pixel,
  conservative in real clear-sky conditions, that does not account
  for cloud contamination, and that is not in the tiles.[^user-guide]
- **The emissivity knowledge base.** The algorithm document expects
  the uncertainty of the classified emissivity for most land cover
  types to be about 0.005, and the guide says a large uncertainty may
  exist in arid and semi-arid areas, which is what the Collection 6
  adjustment of up to 0.0063 addresses.[^atbd][^user-guide]
- **Residual cloud.** The daily product's looser clear-sky threshold
  and the 32 day temporal screening mean that cloud contamination is
  removed statistically rather than excluded by the mask
  alone.[^user-guide]
- **Sampling.** Every value is a clear-sky observation at its own
  local solar time; a mean over days or over the eight-day period is
  a mean of the clear observations that exist, and the coverage
  layers say which days contributed, as flags.[^user-guide][^atbd]

This bundle's HLS L30 concept carries the Landsat TIRS bands as
top-of-atmosphere brightness temperature that is not atmospherically
corrected, so those layers are not a land surface temperature and are
not comparable to these fields without an atmospheric and emissivity
correction of their own.[^l30]

[^a1-page]: LP DAAC product page, MOD11A1 v061, read 2026-09-15
[^a2-page]: LP DAAC product page, MOD11A2 v061, read 2026-09-15
[^user-guide]: Collection-6 MODIS LST Products Users' Guide, June 2019, with the Collection 6.1 cover note
[^atbd]: MODIS LST Algorithm Theoretical Basis Document, version 3.3, April 1999
[^cmr-a1]: CMR collection record C1748058432-LPCLOUD, read 2026-09-15
[^cmr-a2]: CMR collection record C2269056084-LPCLOUD, read 2026-09-15
[^doi-a1]: the MOD11A1 DOI resolved at doi.org, 2026-09-15
[^doi-a2]: the MOD11A2 DOI resolved at doi.org, 2026-09-15
[^wan-2014]: Wan 2014, Remote Sensing of Environment 140, doi:10.1016/j.rse.2013.08.027, cited on its Crossref record
[^wan-2014-crossref]: Crossref record for 10.1016/j.rse.2013.08.027, read 2026-09-15
[^l30]: this bundle's HLS L30 concept
[^clear-sky-gotcha]: this bundle's gotcha on clear-sky sampling and view time
[^day-night-gotcha]: this bundle's gotcha on the day and night fields
[^emissivity-gotcha]: this bundle's gotcha on classified emissivity
