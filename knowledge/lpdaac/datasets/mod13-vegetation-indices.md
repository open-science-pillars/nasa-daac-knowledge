---
type: dataset
spheres: [biosphere, geosphere]
title: "MOD13Q1 and MOD13A1 version 6.1: Terra MODIS NDVI and EVI composited over 16 days by a constrained-view maximum value rule, with the input reflectances, the view geometry, the composite day of year and two quality layers, on 250 m and 500 m sinusoidal tiles"
description: "MOD13Q1 and MOD13A1 are the Terra MODIS vegetation index products at 250 m and 500 m on the sinusoidal grid: for each 16-day period and each pixel, one observation is selected from the eight-day precomposited MOD09 surface reflectance by the constrained-view maximum value rule (the two highest NDVI candidates compared, the smaller view angle kept) and its NDVI and EVI are stored as int16 times 0.0001 with fill -3000, beside the red, NIR, blue and mid-infrared reflectances that produced them, the view zenith, sun zenith and relative azimuth angles, the day of year the selected observation was acquired, a summary pixel reliability rank and a 16-bit quality field. EVI switches to a two-band form over bright surfaces. Collection 6.1 keeps the Collection 6 algorithm and format and differs by the Level-1B calibration."
tags: [mod13, mod13q1, mod13a1, modis, terra, ndvi, evi, vegetation-index, composite, sinusoidal, lpdaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T17:50:00Z }
resource: https://lpdaac.usgs.gov/products/mod13q1v061/
version: "Collection 6.1 (MOD13Q1 DOI 10.5067/MODIS/MOD13Q1.061, CMR C1748066515-LPCLOUD; MOD13A1 DOI 10.5067/MODIS/MOD13A1.061, CMR C2565788901-LPCLOUD; provider LPCLOUD), verified 2026-09-15: both with temporal extent 2000-02-18 to present, the ends-at-present flag set and collection progress ACTIVE, 177,776 granules listed on each product page that day; the user guide read is version 3.10 of September 2019 with its Collection 6.1 cover note"
status: draft
stale_after: 2027-03-15
citation:
  access_date_required: true
  authority: https://lpdaac.usgs.gov/
  data: "Didan, K. (2021). MODIS/Terra Vegetation Indices 16-Day L3 Global 250m SIN Grid V061 [Dataset]. NASA Land Processes Distributed Active Archive Center, accessed {access_date}, 10.5067/MODIS/MOD13Q1.061"
  doi: "10.5067/MODIS/MOD13Q1.061"
  note: "the citation text is the one the LP DAAC product page renders on 2026-09-15; the 500 m product is cited the same way with its own title and DOI 10.5067/MODIS/MOD13A1.061; both are DataCite DOIs, for which the Crossref API returns no record, and both were verified by their resolution at doi.org; the access date matters because the collections are in forward processing"
sources:
  - id: q1-page
    resource: https://lpdaac.usgs.gov/products/mod13q1v061/
    title: "LP DAAC product page for MOD13Q1 v061, read 2026-09-15 (the lpdaac.usgs.gov address redirects to the NASA Earthdata data catalog page for C1748066515-LPCLOUD): description, version description, DOI, CMR concept id, temporal extent, granule count, the twelve-layer variables table with data type, fill, valid range and scale, the file name convention, the citation, the documents it links and the validation stage statement"
  - id: a1-page
    resource: https://lpdaac.usgs.gov/products/mod13a1v061/
    title: "LP DAAC product page for MOD13A1 v061, read 2026-09-15 (redirects to the Earthdata catalog page for C2565788901-LPCLOUD): the same fields for the 500 m product, with its own variables table and file name example"
  - id: vi-guide
    resource: https://lpdaac.usgs.gov/documents/621/MOD13_User_Guide_V61.pdf
    title: "MODIS Vegetation Index User's Guide (MOD13 Series), version 3.10, September 2019, Collection 6.1 (Didan and Barreto Munoz, University of Arizona), with the Collection 6.1 cover note, read in full 2026-09-15: sections 1.1 and 1.2 (the indices, their equations and the two-band EVI backup), 2 (what changed in Collection 6), 3 and 4 (the file format and the product suite), 5 (the MOD13Q1 and MOD13A1 algorithm, Table 1, the QA metadata of Tables 2, 3 and 6, the pixel reliability of Table 4, the quality bit field of Table 5, the usefulness scoring of Table 7), 6 to 9 (the 1 km, monthly and climate modeling grid products), 11 (the FAQ) and Figure 4"
  - id: vi-atbd
    resource: https://lpdaac.usgs.gov/documents/104/MOD13_ATBD.pdf
    title: "MODIS Vegetation Index (MOD 13) Algorithm Theoretical Basis Document, version 3, April 30 1999 (Huete, Justice and van Leeuwen), read 2026-09-15 in its sections 2.2.3 (the influences inherent to canopies), 2.2.7 (canopy background), 2.2.8 (NDVI saturation), 2.2.9 (canopy structure), 3 (the algorithm description opening) and the production section on the projection and tiling (36 by 18 tiles, 648 in all, about 290 with land, 4800 by 4800 pixels at 250 m)"
  - id: cmr-q1
    resource: https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=MOD13Q1&version=061
    title: "CMR collection record for MOD13Q1 v061 (concept C1748066515-LPCLOUD, revision 63 of 2026-04-16), read 2026-09-15: DOI, platform Terra and instrument MODIS, temporal extent with ends-at-present, processing level 3, the sinusoidal tiling system and 250 m resolution, HDF-EOS2 at 92.6 MB average over HTTPS and the Earthdata Cloud, the S3 buckets and credentials endpoint, and the related documents including the LDOPE quality site and the file specification"
  - id: cmr-a1
    resource: https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=MOD13A1&version=061
    title: "CMR collection record for MOD13A1 v061 (concept C2565788901-LPCLOUD, revision 43 of 2026-03-19), read 2026-09-15: the same fields for the 500 m product, HDF-EOS2 at 28.7 MB average"
  - id: doi-q1
    resource: https://doi.org/10.5067/MODIS/MOD13Q1.061
    title: "The MOD13Q1 DOI, resolved 2026-09-15 to the Earthdata catalog page; a DataCite DOI, for which the Crossref API holds no record"
  - id: doi-a1
    resource: https://doi.org/10.5067/MODIS/MOD13A1.061
    title: "The MOD13A1 DOI, resolved 2026-09-15 to the Earthdata catalog page; a DataCite DOI, for which the Crossref API holds no record"
  - id: huete-2002
    resource: https://doi.org/10.1016/S0034-4257(02)00096-2
    title: "Huete, Didan, Miura, Rodriguez, Gao and Ferreira (2002), Overview of the radiometric and biophysical performance of the MODIS vegetation indices, Remote Sensing of Environment 83, 195 to 213: the product's overview paper; the DOI resolves to an Elsevier page on a domain outside this seed's reading list, so the paper is cited on its registry record"
  - id: huete-2002-crossref
    resource: https://api.crossref.org/works/10.1016/S0034-4257(02)00096-2
    title: "Crossref record for 10.1016/S0034-4257(02)00096-2, read 2026-09-15: title, the six authors, journal, volume 83 issues 1 to 2, pages 195 to 213, issued November 2002, ISSN 0034-4257; the record carries no abstract"
  - id: lai-guide
    resource: https://lpdaac.usgs.gov/documents/926/MOD15_User_Guide_V61.pdf
    title: "MODIS Collection 6.1 LAI/FPAR Product User's Guide, updated April 21 2020, read 2026-09-15 for section 4 and Table 3: the sinusoidal tile of a 500 m product is 2400 rows by 2400 columns and the projection sphere measures 6371007.181 m"
  - id: mod11
    resource: mod11-land-surface-temperature.md
    title: "This bundle's MOD11 concept, whose tile, file name and Collection 6.1 statements describe the same sinusoidal grid and the same Level-1B calibration changes at 1 km"
  - id: index-gotcha
    resource: ../gotchas/index-is-not-a-state-variable.md
    title: "This bundle's gotcha on NDVI and EVI as empirical indices rather than state variables"
  - id: doy-gotcha
    resource: ../gotchas/composite-day-of-year-layer.md
    title: "This bundle's gotcha on the composite day of the year layer and the selection rule"
  - id: grid-gotcha
    resource: ../gotchas/sinusoidal-grid-cell-area.md
    title: "This bundle's gotcha on the sinusoidal cell size, tile footprint and reprojection"
---

# MOD13Q1 and MOD13A1 version 6.1

**Identity.** MOD13Q1 is "MODIS/Terra Vegetation Indices 16-Day L3
Global 250m SIN Grid V061", CMR collection C1748066515-LPCLOUD
(provider LPCLOUD, short name MOD13Q1, version 061, DOI
10.5067/MODIS/MOD13Q1.061), platform Terra, instrument MODIS,
processing level 3, temporal extent 2000-02-18 to the present with the
ends-at-present flag set.[^cmr-q1][^q1-page] MOD13A1 is the same
product at 500 m, "MODIS/Terra Vegetation Indices 16-Day L3 Global
500m SIN Grid V061", C2565788901-LPCLOUD (short name MOD13A1, version
061, DOI 10.5067/MODIS/MOD13A1.061), with the same temporal
extent.[^cmr-a1][^a1-page] Both DOIs resolve at doi.org to the
Earthdata catalog pages.[^doi-q1][^doi-a1] On 2026-09-15 each product
page listed 177,776 granules, the same figure for both; it is recorded
here as read.[^q1-page][^a1-page] Each granule is one tile of the MODIS
sinusoidal grid, named like `MOD13Q1.A2025193.h31v08.061.2025209132825.hdf`:
short name, the day of year the product page calls the acquisition
date, tile, collection, production time; the MOD13A1 example is
`MOD13A1.A2025193.h29v07.061.2025209132759.hdf`.[^q1-page][^a1-page]
The guide places the two products in a suite of six, with MOD13A2 at
1 km, MOD13A3 monthly at 1 km and the MOD13C1 and MOD13C2 climate
modeling grid products at 0.05 degrees; only the first two are
described here, and the Aqua products MYD13Q1 and MYD13A1 are their
counterparts eight days out of phase.[^vi-guide]

Collection 6.1 is identical in format to Collection 6 and contains no
change to the science algorithm; the changes are in the Level-1B
inputs, the response versus scan angle calibration, the optical
crosstalk correction in the Terra infrared bands, the Terra forward
look-up table for 2012 to 2017 and a polarization correction on the
reflective solar bands, the same list this bundle's MOD11 concept
carries.[^vi-guide][^q1-page][^cmr-q1][^mod11] The cover note of the
guide opens by naming the C61 MCD12 product as identical in format to
its C6 version; MCD12 is the land cover product, and the sentence is
read here as a copying slip in the vegetation index guide's note. The
guide is a live document last updated September 2019 and points to
the algorithm theoretical basis document for the theory; the product's
overview paper is Huete and others (2002), cited here on its registry
record.[^vi-guide][^vi-atbd][^huete-2002][^huete-2002-crossref]

## The indices

NDVI is the normalized difference of the near-infrared and red
surface reflectances, (NIR minus red) over (NIR plus red), a
normalized transform of the NIR to red ratio confined to -1 to +1,
which the guide calls the continuity index to the NOAA-AVHRR record
that began in 1981.[^vi-guide] EVI is (NIR minus red) over (NIR plus
C1 times red minus C2 times blue plus L), times a gain G, with L equal
to 1, C1 to 6, C2 to 7.5 and G to 2.5: the blue term is an aerosol
resistance built on the wavelength dependence of aerosol scattering,
and L a canopy background adjustment.[^vi-guide] Over bright targets,
where the blue reflectance is at or above about 0.2 (snow, ice, cloud,
heavy aerosol), the three-band EVI becomes unstable and produces
extreme values, so since Collection 5 it is replaced there by a
two-band EVI that does not use the blue band, 2.5 times (NIR minus red)
over (NIR plus 2.4 times red plus 1); because the three-band values
usually stay inside -1 to 1, the guide says these problems are usually
undetected.[^vi-guide] The indices are empirical measures of vegetation
activity, integrative functions of canopy structure and physiology
rather than any one of them; the ratio form of NDVI reduces
band-correlated noise but is non-linear and asymptotic, losing
sensitivity over dense vegetation, and the guide's own FAQ says EVI is
superior at high vegetation density where NDVI tends to saturate ([the
index gotcha](../gotchas/index-is-not-a-state-variable.md)).[^vi-guide][^vi-atbd][^index-gotcha]

## How the composite is made

The inputs are the MOD09 surface reflectances, corrected for
molecular scattering, ozone absorption and aerosols.[^vi-guide] Since
Collection 6 the algorithm no longer ingests daily reflectance: it
ingests the eight-day precomposited Level-2G surface reflectance, in
which the surface reflectance algorithm has already applied filters on
quality, cloud and viewing geometry (cloud-contaminated pixels and
extreme off-nadir views count as lower quality, and a minimum blue
band approach limits aerosol), so that a 16-day period offers at most
two candidate observations per pixel, as the guide's data flow figure
labels it.[^vi-guide] The compositing then extracts one value per
pixel for the period. The main rule is the constrained-view maximum
value composite: the n observations with the highest NDVI, n being 2,
are compared and the one with the smaller view zenith angle, closest
to nadir, is chosen, to limit directional reflectance effects; the
backup is the plain maximum value composite of the AVHRR tradition,
the pixel with the highest NDVI.[^vi-guide] The product page states the
criteria as low clouds, low view angle and the highest NDVI or
EVI.[^q1-page][^a1-page] The guide states the consequence for the map:
all compositing methods result in spatial discontinuities, because
disparate days can be chosen for adjacent pixels, which then carry
different sun-pixel-sensor geometries and different residual
contamination; the day chosen is recorded per pixel in the composite
day of the year layer ([the day of year
gotcha](../gotchas/composite-day-of-year-layer.md)).[^vi-guide][^doy-gotcha]
Since Collection 5 the Terra and Aqua streams are processed eight
days out of phase, so the two together give a quasi eight-day
series.[^vi-guide] In the section covering both products, the guide
says the red and NIR bands, whose native resolution is 250 m, are
aggregated to 500 m before the indices are computed, and the mixed
cloud quality bit is set if any 250 m pixel in the aggregation was
cloud contaminated; the statement describes the 500 m product.[^vi-guide] Indices are
not computed over the ocean and inland water classes of the land/water
mask.[^vi-guide]

Tiles are approximately 1200 by 1200 km at the equator (1,111.95 km
in projection metres on the guide's sphere; the grid gotcha derives
it), 10 by 10 degrees, in the sinusoidal projection, which the guide calls an equal
area projection; only tiles with land are processed.[^vi-guide] The
algorithm document describes the production grid as 36 by 18 tiles,
648 in all of which about 290 hold land, each tile 4800 by 4800 pixels
at 250 m or 1200 by 1200 at 1 km, every pixel keeping its geolocation
through time; the 500 m tile of a MODIS land product is 2400 by 2400,
and the projection sphere measures 6371007.181 m ([the grid
gotcha](../gotchas/sinusoidal-grid-cell-area.md)).[^vi-atbd][^lai-guide][^grid-gotcha]

## Layers

The guide's Table 1 and the product pages' variables tables agree on
twelve scientific data sets, named with the resolution prefix `250m`
on MOD13Q1 and `500m` on MOD13A1:[^vi-guide][^q1-page][^a1-page]

| Layer (after the prefix `250m 16 days` or `500m 16 days`) | Content | Type | Valid range | Fill | Scale |
|---|---|---|---|---|---|
| NDVI | 16-day NDVI | int16 | -2000 to 10000 | -3000 | 0.0001 |
| EVI | 16-day EVI | int16 | -2000 to 10000 | -3000 | 0.0001 |
| VI Quality | detailed quality bit field | uint16 | 0 to 65534 | 65535 | none |
| red reflectance | surface reflectance band 1 | int16 | 0 to 10000 | -1000 | 0.0001 |
| NIR reflectance | surface reflectance band 2 | int16 | 0 to 10000 | -1000 | 0.0001 |
| blue reflectance | surface reflectance band 3 | int16 | 0 to 10000 | -1000 | 0.0001 |
| MIR reflectance | surface reflectance band 7 | int16 | 0 to 10000 | -1000 | 0.0001 |
| view zenith angle | of the selected observation, degrees | int16 | 0 to 18000 | -10000 | 0.01 |
| sun zenith angle | of the selected observation, degrees | int16 | 0 to 18000 | -10000 | 0.01 |
| relative azimuth angle | of the selected observation, degrees | int16 | -18000 to 18000 | -4000 | 0.01 |
| composite day of the year | day of year of the selected observation | int16 | 1 to 366 | -1 | none |
| pixel reliability | summary quality rank | int8 | 0 to 3 | -1 | none |

The indices are the stored integer times 0.0001, so the valid range
is -0.2 to 1.0 and the fill -3000 is a number inside the int16 range
that would scale to -0.3.[^vi-guide] The relative azimuth angle took a
new dynamic range of -180 to 180 degrees in Collection 6 with the new
input stream.[^vi-guide] The monthly MOD13A3 product lacks the composite
day of the year layer because it is built from composites, and the
climate modeling grid products carry NDVI and EVI standard deviations
and counts of contributing pixels that the tiles do not.[^vi-guide]

## Quality

Two per-pixel layers and a set of tile-level metadata objects carry the
quality. The pixel reliability rank is a single summary for both
indices, combined since Collection 5 because the two indices' quality
assignments did not differ significantly:[^vi-guide]

| Rank | Key | Meaning |
|---|---|---|
| -1 | fill, no data | not processed |
| 0 | good data | use with confidence |
| 1 | marginal data | useful, but look at other QA information |
| 2 | snow or ice | target covered with snow or ice |
| 3 | cloudy | target not visible, covered with cloud |

The VI Quality layer packs the conditions of acquisition and
processing, bit 0 the least significant (Table 5):[^vi-guide]

| Bits | Field | Values |
|---|---|---|
| 0 to 1 | VI quality (MODLAND mandatory) | 00 produced, good quality; 01 produced, check other QA; 10 produced but most probably cloudy; 11 not produced for reasons other than cloud |
| 2 to 5 | VI usefulness | 0000 highest quality down to 1100 lowest quality in thirteen levels; 1101 quality so low it is not useful; 1110 L1B data faulty; 1111 not useful for any other reason or not processed |
| 6 to 7 | aerosol quantity | 00 climatology; 01 low; 10 intermediate; 11 high |
| 8 | adjacent cloud detected | 0 no; 1 yes |
| 9 | atmosphere BRDF correction | 0 no; 1 yes |
| 10 | mixed clouds | 0 no; 1 yes |
| 11 to 13 | land/water mask | 000 shallow ocean; 001 land; 010 ocean coastlines and lake shorelines; 011 shallow inland water; 100 ephemeral water; 101 deep inland water; 110 moderate or continental ocean; 111 deep ocean |
| 14 | possible snow/ice | 0 no; 1 yes |
| 15 | possible shadow | 0 no; 1 yes |

The usefulness index is a sum of scores for aerosol quantity,
atmospheric correction conditions, mixed cloud, shadow and view and
sun zenith angles above 40 and 60 degrees (Table 7); a pixel with
usefulness 0000 always has MODLAND bits 00 and one with 1111 always
11.[^vi-guide] The guide says that although bits 8 and 9 are listed, in
practice no adjacency correction and no BRDF correction is applied,
so both are always 0.[^vi-guide] The tile-level metadata carry
QAPercentGoodQuality, QAPercentOtherQuality,
QAPercentNotProducedCloud and QAPercentNotProducedOther, which are the
percentages of the four MODLAND bit combinations over the tile, plus
product-specific objects giving the percentage of good NDVI and EVI
pixels and a sixteen-number histogram of the usefulness index summing
to 100.[^vi-guide] The product pages state that validation at stage 3
has been achieved for the vegetation index suite and point to the
LDOPE land product quality assessment site for known issues; that site
and the LAADS file specification are on domains outside this seed's
reading list and their contents are not represented here.[^q1-page][^cmr-q1]

## Access

Cloud-hosted: the product pages mark both collections cloud enabled,
and the CMR records distribute them over HTTPS and the Earthdata Cloud
in HDF-EOS2 at 92.6 MB (250 m) and 28.7 MB (500 m) per file from the
buckets `s3://lp-prod-protected/MOD13Q1.061` and
`s3://lp-prod-protected/MOD13A1.061` with public counterparts, region
us-west-2, temporary credentials at
data.lpdaac.earthdatacloud.nasa.gov/s3credentials.[^q1-page][^cmr-q1][^cmr-a1]
The data links are Earthdata Search on the collection concept ids and
AppEEARS.[^cmr-q1][^cmr-a1]

## Uncertainty

The tiles carry no per-pixel uncertainty on either index. What stands
in:

- **The pixel reliability rank and the usefulness index.** Ordinal
  classes, not error values: the rank says good, marginal, snow or
  cloud, and the usefulness index places the pixel in one of thirteen
  quality levels by summing condition scores.[^vi-guide]
- **The aerosol, cloud and shadow bits.** The conditions the algorithm
  document lists as external influences on the index (atmosphere,
  clouds, sun-target-sensor geometry) are recorded per pixel as flags
  and angles, so a reader can stratify by them but not correct for
  them.[^vi-atbd][^vi-guide]
- **The index's own non-linearity.** The algorithm document reports
  NDVI insensitive to leaf area above about 2 or 3 and background
  sensitivity of 0.30 NDVI units at a leaf area index of 1 for
  background red reflectances from 0.06 to 0.33; these are properties
  of the index, not errors the product can flag.[^vi-atbd]
- **The two-band EVI substitution.** Where the blue band saturates the
  EVI is computed by a different formula, and the quality table read
  here carries no field that says which formula produced a
  pixel.[^vi-guide]
- **The selection.** Each value is one observation chosen by the
  maximum value rule, so the composite is not a period mean and its
  date varies by pixel; the day of year and angle layers say which
  observation it was.[^vi-guide]
- **Validation.** Stage 3 on the product page; the overview paper of
  Huete and others (2002) is the reference the guide names for the
  radiometric and biophysical performance, cited here on its registry
  record without its text.[^q1-page][^huete-2002][^huete-2002-crossref]

The climate modeling grid products MOD13C1 and MOD13C2 do carry
standard deviation layers for the indices, computed over the 1 km
pixels aggregated into each 0.05 degree cell, and fill cloudy cells
from a historical record; those are different products with their own
pixel reliability value 4 for estimated cells.[^vi-guide]

[^q1-page]: LP DAAC product page, MOD13Q1 v061, read 2026-09-15
[^a1-page]: LP DAAC product page, MOD13A1 v061, read 2026-09-15
[^vi-guide]: MODIS Vegetation Index User's Guide, version 3.10, September 2019, with the Collection 6.1 cover note
[^vi-atbd]: MODIS Vegetation Index Algorithm Theoretical Basis Document, version 3, April 1999
[^cmr-q1]: CMR collection record C1748066515-LPCLOUD, read 2026-09-15
[^cmr-a1]: CMR collection record C2565788901-LPCLOUD, read 2026-09-15
[^doi-q1]: the MOD13Q1 DOI resolved at doi.org, 2026-09-15
[^doi-a1]: the MOD13A1 DOI resolved at doi.org, 2026-09-15
[^huete-2002]: Huete and others 2002, Remote Sensing of Environment 83, doi:10.1016/S0034-4257(02)00096-2, cited on its Crossref record
[^huete-2002-crossref]: Crossref record for 10.1016/S0034-4257(02)00096-2, read 2026-09-15
[^lai-guide]: MODIS Collection 6.1 LAI/FPAR Product User's Guide, April 2020, section 4 and Table 3
[^mod11]: this bundle's MOD11 concept
[^index-gotcha]: this bundle's gotcha on indices as empirical measures
[^doy-gotcha]: this bundle's gotcha on the composite day of the year layer
[^grid-gotcha]: this bundle's gotcha on the sinusoidal grid
