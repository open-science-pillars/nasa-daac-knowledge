---
type: dataset
spheres: [biosphere, geosphere]
title: "MOD15A2H version 6.1: Terra MODIS leaf area index and FPAR retrieved by a biome look-up table inversion of red and near-infrared reflectance, composited over eight days by maximum FPAR, with retrieval standard deviations and two quality bytes, on 500 m sinusoidal tiles"
description: "MOD15A2H is the Terra MODIS eight-day leaf area index and fraction of absorbed photosynthetically active radiation product at 500 m on the sinusoidal grid, a Level 4 product: for each pixel the main algorithm compares the observed red (648 nm) and near-infrared (858 nm) reflectances with a look-up table of three-dimensional radiative transfer solutions for the pixel's biome type and reports the mean of the acceptable solutions as LAI and FPAR and their dispersion as the standard deviation layers; when no solution is found, a backup regression on NDVI is used, and the algorithm path is recorded in the FparLai_QC byte. Values are uint8 with LAI times 0.1 and FPAR times 0.01, and the codes 249 to 255 above the valid range encode the land cover class of pixels without a retrieval. Collection 6.1 keeps the Collection 6 algorithm and format and differs by the Level-1B calibration."
tags: [mod15, mod15a2h, modis, terra, lai, fpar, leaf-area-index, look-up-table, sinusoidal, lpdaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T17:50:00Z }
resource: https://lpdaac.usgs.gov/products/mod15a2hv061/
version: "Collection 6.1 (DOI 10.5067/MODIS/MOD15A2H.061, CMR C2218777082-LPCLOUD, provider LPCLOUD), verified 2026-09-15: temporal extent 2000-02-18 to present with the ends-at-present flag set and collection progress ACTIVE, 349,578 granules listed on the product page that day; the user guide read is the Collection 6.1 guide updated April 21 2020"
status: draft
stale_after: 2027-03-15
citation:
  access_date_required: true
  authority: https://lpdaac.usgs.gov/
  data: "Myneni, R., Knyazikhin, Y., and Park, T. (2021). MODIS/Terra Leaf Area Index/FPAR 8-Day L4 Global 500m SIN Grid V061 [Dataset]. NASA Land Processes Distributed Active Archive Center, accessed {access_date}, 10.5067/MODIS/MOD15A2H.061"
  doi: "10.5067/MODIS/MOD15A2H.061"
  note: "the citation text is the one the LP DAAC product page renders on 2026-09-15; a DataCite DOI, for which the Crossref API returns no record, verified by its resolution at doi.org; the access date matters because the collection is in forward processing"
sources:
  - id: page
    resource: https://lpdaac.usgs.gov/products/mod15a2hv061/
    title: "LP DAAC product page for MOD15A2H v061, read 2026-09-15 (the lpdaac.usgs.gov address redirects to the NASA Earthdata data catalog page for C2218777082-LPCLOUD): description with the LAI and FPAR definitions, version description, DOI, CMR concept id, temporal extent, granule count, the six-layer variables table with data type, fill, valid range and scale, the file name convention, the citation, the documents it links and the validation stage statement"
  - id: lai-guide
    resource: https://lpdaac.usgs.gov/documents/926/MOD15_User_Guide_V61.pdf
    title: "MODIS Collection 6.1 (C6.1) LAI/FPAR Product User's Guide, updated April 21 2020, with the Collection 6.1 cover note, read in full 2026-09-15: sections 1 (definitions), 2 (changes in Collection 6), 3 (the algorithm, Figure 1 and Table 1), 4 (the products, Tables 2 and 3, the tiling and the metadata), 6 (Table 4, the two quality bytes in the two tables both numbered 5, the fill legends of Tables 6 and 7) and 9 (the related papers)"
  - id: lai-atbd
    resource: https://lpdaac.usgs.gov/documents/90/MOD15_ATBD.pdf
    title: "MODIS Leaf Area Index and FPAR Product (MOD15) Algorithm Theoretical Basis Document, version 4.0, April 30 1999 (Myneni, Knyazikhin and others), read 2026-09-15 in its overview (the eight-day product produced by compositing using maximum FPAR), section 2.9 (the saturation domain) and section 2.12 (the backup algorithm as biome-dependent regression curves of LAI and FPAR on NDVI)"
  - id: gpp-guide
    resource: https://lpdaac.usgs.gov/documents/972/MOD17_User_Guide_V61.pdf
    title: "MOD17 User's Guide for Collection 6.1, version 1.1, March 11 2021 (Running and Zhao), read 2026-09-15 for section 2.3: the eight-day MOD15A2H compositing selects the maximum FPAR across the eight days and the same day supplies the LAI, and section 1.3.4: reflectance has low sensitivity to LAI above 3, and section 2.4.2 (the Terra MOD15A2H start date used for gap filling)"
  - id: cmr
    resource: https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=MOD15A2H&version=061
    title: "CMR collection record for MOD15A2H v061 (concept C2218777082-LPCLOUD, revision 52 of 2026-04-16), read 2026-09-15: DOI, platform Terra and instrument MODIS, temporal extent with ends-at-present, processing level 4, the sinusoidal tiling system and 500 m resolution, HDF-EOS2 at 3.5 MB average over HTTPS and the Earthdata Cloud, the S3 buckets and credentials endpoint, and the related documents including the LDOPE quality site and the file specification"
  - id: cmr-vars
    resource: https://cmr.earthdata.nasa.gov/search/variables.umm_json?concept_id[]=V3144112793-LPCLOUD&concept_id[]=V3144112802-LPCLOUD&concept_id[]=V3144112836-LPCLOUD&concept_id[]=V3144112838-LPCLOUD&concept_id[]=V3144112811-LPCLOUD&concept_id[]=V3144112833-LPCLOUD
    title: "CMR variable records associated with the MOD15A2H v061 collection (V3144112793, V3144112802, V3144112836, V3144112838, V3144112811 and V3144112833, all LPCLOUD, revisions of August 2024), read 2026-09-15: Fpar_500m and Lai_500m carry the seven science fill values 249 to 255 with their land cover descriptions, the two standard deviation layers 248 to 255 with 248 as the backup method code, the two quality bytes 255, and the valid ranges and scales of Table 4"
  - id: doi
    resource: https://doi.org/10.5067/MODIS/MOD15A2H.061
    title: "The MOD15A2H DOI, resolved 2026-09-15 to the Earthdata catalog page; a DataCite DOI, for which the Crossref API holds no record"
  - id: myneni-2002
    resource: https://doi.org/10.1016/S0034-4257(02)00074-3
    title: "Myneni, Hoffman, Knyazikhin, Privette, Glassy, Tian, Wang, Song, Zhang, Smith, Lotsch, Friedl, Morisette, Votava, Nemani and Running (2002), Global products of vegetation leaf area and fraction absorbed PAR from year one of MODIS data, Remote Sensing of Environment 83, 214 to 231: the paper the guide lists first for the product; the DOI resolves to an Elsevier page on a domain outside this seed's reading list, so the paper is cited on its registry record"
  - id: myneni-2002-crossref
    resource: https://api.crossref.org/works/10.1016/S0034-4257(02)00074-3
    title: "Crossref record for 10.1016/S0034-4257(02)00074-3, read 2026-09-15: title, the sixteen authors, journal, volume 83 issues 1 to 2, pages 214 to 231, issued November 2002, ISSN 0034-4257; the record carries no abstract"
  - id: mod13
    resource: mod13-vegetation-indices.md
    title: "This bundle's MOD13 concept, for the indices the backup algorithm regresses on and the sinusoidal grid statements shared by the two products"
  - id: mod11
    resource: mod11-land-surface-temperature.md
    title: "This bundle's MOD11 concept, whose Collection 6.1 statement lists the same Level-1B calibration changes"
  - id: model-gotcha
    resource: ../gotchas/lai-and-gpp-are-model-outputs.md
    title: "This bundle's gotcha on LAI, FPAR, GPP and NPP as model outputs gated by their quality layers"
  - id: index-gotcha
    resource: ../gotchas/index-is-not-a-state-variable.md
    title: "This bundle's gotcha on NDVI and EVI as indices rather than state variables, which names this product as the retrieved state variable"
  - id: grid-gotcha
    resource: ../gotchas/sinusoidal-grid-cell-area.md
    title: "This bundle's gotcha on the sinusoidal cell size, tile footprint and reprojection"
---

# MOD15A2H version 6.1

**Identity.** MOD15A2H is "MODIS/Terra Leaf Area Index/FPAR 8-Day L4
Global 500m SIN Grid V061", CMR collection C2218777082-LPCLOUD
(provider LPCLOUD, short name MOD15A2H, version 061, DOI
10.5067/MODIS/MOD15A2H.061), platform Terra, instrument MODIS,
processing level 4 (model output rather than a gridded measurement),
temporal extent 2000-02-18 to the present with the ends-at-present
flag set.[^cmr][^page] The DOI resolves at doi.org to the Earthdata
catalog page.[^doi] On 2026-09-15 the product page listed 349,578
granules.[^page] Each granule is one tile of the sinusoidal grid, 2400
rows by 2400 columns at 500 m, named like
`MOD15A2H.A2025209.h35v09.061.2025218040352.hdf`: short name, the day
of year the product page calls the acquisition date, tile, collection,
production time.[^page][^lai-guide] The guide's Table 2 lists the Aqua
product MYD15A2H, the combined eight-day MCD15A2H and the combined
four-day MCD15A3H beside it; only the Terra eight-day product is
described here.[^lai-guide] The guide gives the Terra temporal coverage
as February 18, 2000 onward, and the MOD17 guide, describing the
inputs to its own gap filling, says MOD15A2H of Terra starts from
2000-02-28; both are recorded as read.[^lai-guide][^gpp-guide]

Collection 6.1 is identical in format to Collection 6 and contains no
change to the science algorithm; the differences come from the
Level-1B calibration and polarization changes that this bundle's MOD11
and MOD13 concepts list.[^lai-guide][^page][^mod11][^mod13] Collection 6
itself moved the product from 1 km to 500 m, replaced the 1 km
aggregated reflectance input with the 500 m MOD09GA daily surface
reflectance (through an intermediate daily product, MOD15IP, that is
not archived) and took up an improved multi-year land cover
product.[^lai-guide]

## Definitions

Leaf area index is the one-sided green leaf area per unit ground area
in broadleaf canopies and one half the total needle surface area per
unit ground area in coniferous canopies, dimensionless. FPAR is the
fraction of incident photosynthetically active radiation, 400 to 700
nm, absorbed by the green elements of a vegetation canopy. STD LAI and
STD FPAR are the estimated retrieval uncertainties: the true value can
differ from the retrieval by plus or minus that amount.[^lai-guide][^page]

## How the retrieval is made

The algorithm has a main path and a backup. The main path is a
look-up table generated with a three-dimensional radiative transfer
equation (Knyazikhin and others 1998): for each pixel it compares the
observed bidirectional reflectance factors at red (648 nm) and
near-infrared (858 nm) with modelled ones for a suite of canopy and
soil patterns representing the expected range of conditions for the
pixel's biome type, given the sun-sensor geometry and the assumed
reflectance uncertainties. Every canopy and soil pattern whose
modelled reflectances fall within the uncertainty of the observed ones
is an acceptable solution; the mean LAI and FPAR over the acceptable
solutions are reported as the retrievals and their dispersions as the
standard deviation layers.[^lai-guide] The inputs are the vegetation
structural type from the MODIS land cover product MCD12Q1, the
sun-sensor geometry, the two reflectances from MOD09GA and their
uncertainties, which the guide's Table 1 sets at 20 per cent in the
red and 5 per cent in the near-infrared for the four non-forest biomes
(grasses and cereal crops, shrubs, broadleaf crops, savanna) and 30
and 15 per cent for the four forest biomes (evergreen broadleaf,
deciduous broadleaf, evergreen needleleaf, deciduous
needleleaf).[^lai-guide]

In dense canopies the reflectances saturate and are weakly sensitive
to canopy properties, so the dispersion of the solution distribution
is large and the reliability of the retrieval is low; such retrievals
are flagged in the quality byte. The algorithm document develops this
as the saturation domain, where a measured reflectance is consistent
with any LAI from a saturation point up to the biome maximum with
equal probability, illustrated by a case where any value from 3.6 to
9.85 is a solution, and the MOD17 guide says reflectance has low
sensitivity to LAI above 3.[^lai-guide][^lai-atbd][^gpp-guide] When the
look-up table fails to localize a solution, the backup path estimates
LAI and FPAR from biome-dependent regression curves on NDVI; the guide
says the best quality, high precision retrievals come from the main
algorithm and that the algorithm path is therefore a key quality
indicator.[^lai-guide][^lai-atbd] The guide also states that the
algorithm is executed irrespective of input quality, so the quality
layers are the means of selecting reliable retrievals ([the model
outputs gotcha](../gotchas/lai-and-gpp-are-model-outputs.md)).[^lai-guide][^model-gotcha]

The eight-day product is a composite of the daily retrievals. The
product page says the algorithm chooses the best pixel from the eight
days of Terra acquisitions; the algorithm document says the eight-day
product is produced by compositing using maximum FPAR, and the MOD17
guide, describing its own input, says the compositing selects the
maximum FPAR across the eight days and the same day contributes the
LAI value.[^page][^lai-atbd][^gpp-guide] Unlike MOD13, the product
carries no layer recording which day was chosen ([this bundle's MOD13
concept](mod13-vegetation-indices.md)).[^lai-guide][^mod13] The tiles
follow the sinusoidal tiling system of the other MODIS land products,
36 by 18 tiles of 10 by 10 degrees at the equator on a sphere of
6371007.181 m; the guide notes that the UpperLeftPointMtrs and
LowerRightMtrs projection coordinates are the only metadata that
accurately reflect the corners of the gridded image, while the
BOUNDINGRECTANGLE and GRINGPOINT fields give the latitude and
longitude of the geographic tile ([the grid
gotcha](../gotchas/sinusoidal-grid-cell-area.md)).[^lai-guide][^grid-gotcha]

## Layers

The guide's Table 4 and the product page variables table give six
scientific data sets, all 8-bit unsigned:[^lai-guide][^page]

| Layer | Content | Type | Valid range | Fill (guide) | Fill (product page) | Scale |
|---|---|---|---|---|---|---|
| Fpar_500m | fraction of absorbed PAR | uint8 | 0 to 100 | 249 to 255 | 249 | 0.01 |
| Lai_500m | leaf area index | uint8 | 0 to 100 | 249 to 255 | 249 | 0.1 |
| FparLai_QC | quality for LAI and FPAR, bit field | uint8 | 0 to 254 | 255 | 255 | none |
| FparExtra_QC | extra quality detail, bit field | uint8 | 0 to 254 | 255 | 255 | none |
| FparStdDev_500m | standard deviation of FPAR | uint8 | 0 to 100 | 248 to 255 | 248 | 0.01 |
| LaiStdDev_500m | standard deviation of LAI | uint8 | 0 to 100 | 248 to 255 | 248 | 0.1 |

LAI is the stored byte times 0.1, so the valid range runs to 10.0, and
FPAR the byte times 0.01, to 1.0.[^lai-guide] The guide's fill legend
(Tables 6 and 7) gives the codes above the valid range a meaning: 255
is the fill proper, assigned when the MOD09GA red or near-infrared
reflectance was fill or the land cover pixel was fill; 254 is land
cover perennial salt or inland fresh water; 253 barren or sparse
vegetation (rock, tundra, desert); 252 perennial snow or ice; 251
permanent wetlands or inundated marshland; 250 urban or built-up; 249
unclassified; and on the two standard deviation layers 248 means no
standard deviation is available because the pixel was produced by the
backup method.[^lai-guide] The product page renders only the lowest
code of each range as the fill, while the CMR variable records for the
collection, from which the catalog's layer table is rendered, list
all seven codes with the same land cover meanings the guide
gives.[^page][^cmr-vars] The guide's Table 4 spells the second
standard deviation layer with a doubled underscore,
`LaiStdDev__500m`, where the product page has `LaiStdDev_500m`; the
product page spelling is used here.[^lai-guide][^page]

## Quality

FparLai_QC packs five fields, read from bit 0 as the least significant
(the guide's Table 5):[^lai-guide]

| Bits | Field | Values |
|---|---|---|
| 0 | MODLAND QC | 0 good quality (main algorithm with or without saturation); 1 other quality (backup algorithm or fill values) |
| 1 | sensor | 0 Terra; 1 Aqua |
| 2 | dead detector | 0 detectors apparently fine for up to 50 per cent of channels 1 and 2; 1 dead detectors caused more than 50 per cent adjacent detector retrieval |
| 3 to 4 | cloud state, inherited from the MOD09GA aggregate QC | 00 significant clouds not present (clear); 01 significant clouds were present; 10 mixed cloud present in pixel; 11 cloud state not defined, assumed clear |
| 5 to 7 | SCF_QC, the algorithm path | 000 main method, best result possible, no saturation; 001 main method with saturation, good and very usable; 010 main method failed due to bad geometry, empirical algorithm used; 011 main method failed for problems other than geometry, empirical algorithm used; 100 pixel not produced, value could not be retrieved (bad L1B data, unusable MOD09GA data) |

The guide's worked example is the byte 64, binary 01000000, whose bits
5 to 7 read 010: the main method failed for geometry and the backup
was used, with the cloud, detector and MODLAND bits all zero.[^lai-guide]
The guide calls SCF_QC the key indicator of retrieval quality and
notes that several fields are passed through from the MOD09GA surface
reflectance quality rather than assessed by this algorithm.[^lai-guide]
FparExtra_QC carries the pass-through land/sea class in bits 0 to 1
(land, shore, freshwater, ocean), snow or ice in bit 2, average or
high aerosol in bit 3, cirrus in bit 4, the internal cloud mask in
bit 5, cloud shadow in bit 6 and in bit 7 whether the biome is in the
interval 1 to 4 (the non-forest biomes).[^lai-guide] Tile-level quality
appears as the standard ECS metadata fields.[^lai-guide] The product page
states that the LAI product has attained stage 2 validation and the
FPAR product stage 1, and points to the LDOPE land product quality
assessment site for known issues; that site and the LAADS file
specification are on domains outside this seed's reading list and
their contents are not represented here.[^page][^cmr]

## Access

Cloud-hosted: the product page marks the collection cloud enabled, and
the CMR record distributes it over HTTPS and the Earthdata Cloud in
HDF-EOS2 at 3.5 MB per file from the bucket
`s3://lp-prod-protected/MOD15A2H.061` with a public counterpart, region
us-west-2, temporary credentials at
data.lpdaac.earthdatacloud.nasa.gov/s3credentials; the guide's file
size of about 0.8 MB compressed describes the same product at its
writing.[^page][^cmr][^lai-guide] The data links are Earthdata Search on
the collection concept id and AppEEARS, and each granule also has two
low resolution browse images.[^cmr][^page]

## Uncertainty

This product carries a per-pixel uncertainty layer for each
variable, and its meaning is specific:

- **LaiStdDev_500m and FparStdDev_500m.** The dispersion of the
  acceptable solutions of the look-up table inversion, the measure of
  solution accuracy the main algorithm provides; the guide defines
  them as the amount by which the true value can differ from the
  retrieval. They exist only for main-algorithm pixels: a backup
  pixel carries 248.[^lai-guide]
- **The assumed input uncertainties.** The inversion accepts every
  solution within 20 or 30 per cent in the red and 5 or 15 per cent in
  the near-infrared by biome (Table 1), so the standard deviations
  express that assumed tolerance propagated through the model, not a
  comparison with the ground.[^lai-guide]
- **Saturation.** Under saturation the dispersion is large by
  construction and the retrieval is flagged (SCF_QC 001); the
  algorithm document's saturation domain means any LAI above the
  saturation point is equally consistent with the
  reflectances.[^lai-guide][^lai-atbd]
- **The backup path.** Regression curves of LAI and FPAR on NDVI by
  biome, which the guide rates below the main algorithm in quality and
  precision; these pixels inherit the index's own limits ([the index
  gotcha](../gotchas/index-is-not-a-state-variable.md)).[^lai-guide][^lai-atbd][^index-gotcha]
- **The biome map.** Every retrieval is conditioned on the land cover
  class assigned to the pixel, which selects the look-up table and the
  backup curve; a misclassified pixel is inverted against the wrong
  canopy model.[^lai-guide]
- **Validation.** Stage 2 for LAI and stage 1 for FPAR on the product
  page; the guide's related papers list the year-one product paper of
  Myneni and others (2002), cited here on its registry record without
  its text, and the Collection 6 evaluation papers of Yan and others
  (2016).[^page][^myneni-2002][^myneni-2002-crossref][^lai-guide]

[^page]: LP DAAC product page, MOD15A2H v061, read 2026-09-15
[^lai-guide]: MODIS Collection 6.1 LAI/FPAR Product User's Guide, April 2020
[^lai-atbd]: MODIS LAI and FPAR Algorithm Theoretical Basis Document, version 4.0, April 1999
[^gpp-guide]: MOD17 User's Guide for Collection 6.1, version 1.1, March 2021, sections 1.3.4, 2.3 and 2.4.2
[^cmr]: CMR collection record C2218777082-LPCLOUD, read 2026-09-15
[^cmr-vars]: CMR variable records for the MOD15A2H v061 collection, read 2026-09-15
[^doi]: the MOD15A2H DOI resolved at doi.org, 2026-09-15
[^myneni-2002]: Myneni and others 2002, Remote Sensing of Environment 83, doi:10.1016/S0034-4257(02)00074-3, cited on its Crossref record
[^myneni-2002-crossref]: Crossref record for 10.1016/S0034-4257(02)00074-3, read 2026-09-15
[^mod13]: this bundle's MOD13 concept
[^mod11]: this bundle's MOD11 concept
[^model-gotcha]: this bundle's gotcha on model outputs and their quality layers
[^index-gotcha]: this bundle's gotcha on indices as empirical measures
[^grid-gotcha]: this bundle's gotcha on the sinusoidal grid
