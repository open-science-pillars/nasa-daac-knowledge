---
type: dataset
spheres: [biosphere, geosphere]
title: "MOD17A2H and MOD17A3HGF version 6.1: Terra MODIS gross primary productivity summed over eight days and gap-filled annual net primary production from a radiation use efficiency model driven by MOD15 FPAR and LAI, GMAO reanalysis weather and a fixed biome parameter table, on 500 m sinusoidal tiles"
description: "MOD17A2H is the Terra MODIS eight-day gross primary productivity product at 500 m on the sinusoidal grid, a Level 4 model output: daily GPP is the product of a biome maximum light use efficiency, attenuated by linear ramps in daily minimum temperature and daytime vapour pressure deficit from GMAO reanalysis, and the absorbed PAR from MOD15 FPAR and 0.45 times the reanalysis shortwave radiation; the file holds the eight-day sums of GPP and of net photosynthesis (GPP less leaf and fine root maintenance respiration computed from MOD15 LAI) as int16 times 0.0001 kg C per square metre, with a quality byte inherited from MOD15. MOD17A3HGF is the year-end product built after the year's MOD15A2H has been screened by its quality label and gap-filled by linear interpolation: annual GPP, annual NPP as 0.8 times (GPP minus maintenance respiration), and a quality layer that is the percentage of growing-season days on which filled LAI and FPAR were used. Since Collection 6.1 a five-year FPAR and LAI climatology replaces contaminated inputs in the eight-day product, and the Collection 6.1 MOD17A2H record begins on 2021-01-01."
tags: [mod17, mod17a2h, mod17a3hgf, modis, terra, gpp, npp, primary-productivity, light-use-efficiency, bplut, sinusoidal, lpdaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T17:50:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-15T18:34:53Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/172 }
resource: https://lpdaac.usgs.gov/products/mod17a2hv061/
version: "Collection 6.1 (MOD17A2H DOI 10.5067/MODIS/MOD17A2H.061, CMR C2565791027-LPCLOUD; MOD17A3HGF DOI 10.5067/MODIS/MOD17A3HGF.061, CMR C2565791034-LPCLOUD; provider LPCLOUD), verified 2026-09-15: MOD17A2H temporal extent 2021-01-01 to present and MOD17A3HGF 2001-01-01 to present, both with the ends-at-present flag set and collection progress ACTIVE, 92,343 and 7,250 granules on the product pages that day; the user guide read is version 1.1 of March 11 2021"
status: stable
stale_after: 2027-03-15
citation:
  access_date_required: true
  authority: https://lpdaac.usgs.gov/
  data: "Running, S., Mu, Q., and Zhao, M. (2021). MODIS/Terra Gross Primary Productivity 8-Day L4 Global 500m SIN Grid V061 [Dataset]. NASA Land Processes Distributed Active Archive Center, accessed {access_date}, 10.5067/MODIS/MOD17A2H.061"
  doi: "10.5067/MODIS/MOD17A2H.061"
  note: "the citation text is the one the LP DAAC product page renders on 2026-09-15; the annual product is cited as Running, S., and Zhao, M. (2021), MODIS/Terra Net Primary Production Gap-Filled Yearly L4 Global 500m SIN Grid V061, DOI 10.5067/MODIS/MOD17A3HGF.061; both are DataCite DOIs, for which the Crossref API returns no record, verified by their resolution at doi.org; the access date matters because both collections are in forward processing"
sources:
  - id: a2h-page
    resource: https://lpdaac.usgs.gov/products/mod17a2hv061/
    title: "LP DAAC product page for MOD17A2H v061, read 2026-09-15 (the lpdaac.usgs.gov address redirects to the NASA Earthdata data catalog page for C2565791027-LPCLOUD): description, version description with the climatology backup, DOI, CMR concept id, temporal extent 2021-01-01 to present, granule count, the three-layer variables table with data type, fill, valid range and scale, the file name convention, the citation, the documents it links and the validation stage statement"
  - id: a3hgf-page
    resource: https://lpdaac.usgs.gov/products/mod17a3hgfv061/
    title: "LP DAAC product page for MOD17A3HGF v061, read 2026-09-15 (redirects to the Earthdata catalog page for C2565791034-LPCLOUD): description of the year-end gap filling, known issues pointer to section 2 of the guide, DOI, concept id, temporal extent 2001-01-01 to present, granule count, the three-layer variables table, the file name convention and the citation"
  - id: gpp-guide
    resource: https://lpdaac.usgs.gov/documents/972/MOD17_User_Guide_V61.pdf
    title: "User's Guide, Daily GPP and Annual NPP (MOD17A2H/A3H) and Year-end Gap-Filled (MOD17A2HGF/A3HGF) Products, Collection 6.1, version 1.1, March 11 2021 (Running and Zhao), read 2026-09-15: the cover note, the synopsis, sections 1.1 to 1.3 (the algorithm logic, equations 1.1 to 1.13, Tables 1.1 to 1.3), 2.1 to 2.5 (the land cover dependence, the BPLUT of Table 2.2, the LAI and FPAR input, the climatology backup and year-end gap filling, the GMAO meteorology), 3 (validation), 4.1 and 4.2 (Tables 4.1 and 4.2, the fill legends and the quality layers) and 5"
  - id: gpp-atbd
    resource: https://lpdaac.usgs.gov/documents/95/MOD17_ATBD.pdf
    title: "MODIS Daily Photosynthesis (PSN) and Annual Net Primary Production (NPP) Product (MOD17) Algorithm Theoretical Basis Document, version 3.0, April 29 1999 (Running, Nemani, Glassy and Thornton), read 2026-09-15 in section 3 (the algorithm overview and the daily GPP logic with the BPLUT parameters of Table 3.1) and section 5 (the integerized sinusoidal grid at 1 km and the DAO climatology inputs at launch)"
  - id: cmr-a2h
    resource: https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=MOD17A2H&version=061
    title: "CMR collection record for MOD17A2H v061 (concept C2565791027-LPCLOUD, revision 45 of 2026-03-18), read 2026-09-15: DOI, platform Terra and instrument MODIS, temporal extent beginning 2021-01-01 with ends-at-present, processing level 4, the sinusoidal tiling system and 500 m resolution, HDF-EOS2 at 3.4 MB average over HTTPS and the Earthdata Cloud, the S3 buckets and credentials endpoint, and the related documents including the LDOPE quality site and the file specification"
  - id: cmr-a3hgf
    resource: https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=MOD17A3HGF&version=061
    title: "CMR collection record for MOD17A3HGF v061 (concept C2565791034-LPCLOUD, revision 46 of 2026-03-18), read 2026-09-15: the same fields for the annual product, temporal extent beginning 2001-01-01 at a one year resolution, HDF-EOS2 at 7 MB average, with the total collection file size beginning 2000-01-01"
  - id: cmr-a2hgf
    resource: https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=MOD17A2HGF&version=061
    title: "CMR collection record for the gap-filled eight-day product MOD17A2HGF v061 (concept C2565791029-LPCLOUD), read 2026-09-15 for one field: its temporal extent begins 2000-01-01, so it is the collection that carries the Collection 6.1 eight-day record before 2021; that product is not otherwise described here"
  - id: cmr-a3hgf-granules
    resource: https://cmr.earthdata.nasa.gov/search/granules.json?collection_concept_id=C2565791034-LPCLOUD&temporal=2000-01-01T00:00:00Z,2000-12-31T23:59:59Z&page_size=1
    title: "CMR granule search on C2565791034-LPCLOUD for the calendar year 2000, read 2026-09-15: zero hits, against 290 for 2001, with the earliest granules by start date named MOD17A3HGF.A2001001"
  - id: cmr-vars
    resource: https://cmr.earthdata.nasa.gov/search/variables.umm_json?concept_id[]=V3151335752-LPCLOUD&concept_id[]=V3151335789-LPCLOUD&concept_id[]=V3151335815-LPCLOUD&concept_id[]=V3151347144-LPCLOUD&concept_id[]=V3151347163-LPCLOUD&concept_id[]=V3151347206-LPCLOUD
    title: "CMR variable records associated with the MOD17A2H and MOD17A3HGF v061 collections (V3151335752, V3151335789, V3151335815, V3151347144, V3151347163 and V3151347206, all LPCLOUD, revisions of August 2024), read 2026-09-15: Gpp_500m, PsnNet_500m and Npp_500m carry the seven science fill values 32761 to 32767, the annual Gpp_500m 65529 to 65535 and Npp_QC_500m 249 to 255, each with its land cover description, and the valid ranges and scales of Tables 4.1 and 4.2"
  - id: doi-a2h
    resource: https://doi.org/10.5067/MODIS/MOD17A2H.061
    title: "The MOD17A2H DOI, resolved 2026-09-15 to the Earthdata catalog page; a DataCite DOI, for which the Crossref API holds no record"
  - id: doi-a3hgf
    resource: https://doi.org/10.5067/MODIS/MOD17A3HGF.061
    title: "The MOD17A3HGF DOI, resolved 2026-09-15 to the Earthdata catalog page; a DataCite DOI, for which the Crossref API holds no record"
  - id: running-2004
    resource: https://doi.org/10.1641/0006-3568(2004)054[0547:ACSMOG]2.0.CO;2
    title: "Running, Nemani, Heinsch, Zhao, Reeves and Hashimoto (2004), A Continuous Satellite-Derived Measure of Global Terrestrial Primary Production, BioScience 54(6), 547 to 560: the paper the guide's synopsis quotes for the product's purpose; the DOI resolves to an Oxford University Press page on a domain outside this seed's reading list, so the paper is cited on its registry record"
  - id: running-2004-crossref
    resource: https://api.crossref.org/works/10.1641/0006-3568(2004)054[0547:ACSMOG]2.0.CO;2
    title: "Crossref record for 10.1641/0006-3568(2004)054[0547:ACSMOG]2.0.CO;2, read 2026-09-15: title, the six authors, journal BioScience, volume 54 issue 6, first page 547, issued 2004, ISSN 0006-3568; the record carries no abstract"
  - id: mod15
    resource: mod15-lai-fpar.md
    title: "This bundle's MOD15 concept, the source of the FPAR and LAI inputs and of the FparLai_QC byte this product inherits"
  - id: mod13
    resource: mod13-vegetation-indices.md
    title: "This bundle's MOD13 concept, for the sinusoidal grid statements shared by the land products"
  - id: model-gotcha
    resource: ../gotchas/lai-and-gpp-are-model-outputs.md
    title: "This bundle's gotcha on LAI, FPAR, GPP and NPP as model outputs gated by their quality layers"
  - id: grid-gotcha
    resource: ../gotchas/sinusoidal-grid-cell-area.md
    title: "This bundle's gotcha on the sinusoidal cell size, tile footprint and reprojection"
---

# MOD17A2H and MOD17A3HGF version 6.1

**Identity.** MOD17A2H is "MODIS/Terra Gross Primary Productivity
8-Day L4 Global 500m SIN Grid V061", CMR collection
C2565791027-LPCLOUD (provider LPCLOUD, short name MOD17A2H, version
061, DOI 10.5067/MODIS/MOD17A2H.061), platform Terra, instrument
MODIS, processing level 4, temporal extent 2021-01-01 to the present
with the ends-at-present flag set.[^cmr-a2h][^a2h-page] MOD17A3HGF is
"MODIS/Terra Net Primary Production Gap-Filled Yearly L4 Global 500m
SIN Grid V061", C2565791034-LPCLOUD (short name MOD17A3HGF, version
061, DOI 10.5067/MODIS/MOD17A3HGF.061), one file per tile and year,
temporal extent 2001-01-01 to the present; a CMR granule query on the
collection for the year 2000 returns no granules, the earliest are
named A2001001, and the record's total collection file size begin
date of 2000-01-01 is the only trace of the earlier year in the
metadata.[^cmr-a3hgf][^a3hgf-page][^cmr-a3hgf-granules]
Both DOIs resolve at doi.org to the Earthdata catalog pages.[^doi-a2h][^doi-a3hgf]
On 2026-09-15 the product pages listed 92,343 and 7,250
granules.[^a2h-page][^a3hgf-page] Granules are sinusoidal tiles at
500 m, named like `MOD17A2H.A2025209.h05v11.061.2025218043205.hdf` and
`MOD17A3HGF.A2024001.h17v10.061.2025011052834.hdf`: short name, the
day of year the product pages call the acquisition date, tile,
collection, production time; the guide says the eight-day sums are
named for the first day of their period, and the annual example
carries day 001.[^a2h-page][^a3hgf-page][^gpp-guide]

The Collection 6.1 eight-day record of MOD17A2H begins on 2021-01-01
on both the product page and the CMR record, while the guide
describes eight-day products beginning in 2000; the CMR record of the
gap-filled eight-day collection MOD17A2HGF begins 2000-01-01, so the
years before 2021 exist in Collection 6.1 as the gap-filled eight-day
product, which this concept does not otherwise describe.[^a2h-page][^cmr-a2h][^gpp-guide][^cmr-a2hgf]
The guide's family is four products: MOD17A2H and MOD17A3H, the
operational eight-day and annual products, and MOD17A2HGF and
MOD17A3HGF, their year-end gap-filled versions; the annual product
described here is the gap-filled one, which is the one the LP DAAC
product page and the brief name.[^gpp-guide][^a3hgf-page] The Aqua
products MYD17 are not described here.[^gpp-guide]

Collection 6.1 is identical in format to Collection 6 except that a
new annual total GPP field, Gpp_500m, was added to the annual product;
the science algorithm is unchanged and the differences come from the
Level-1B calibration and polarization changes, plus one input change
stated on the product pages and in the guide: a climatology of FPAR
and LAI is used as backup to the operational MOD15A2H.[^gpp-guide][^a2h-page][^a3hgf-page]
The guide's synopsis quotes Running and others (2004) for the
product's purpose, a regular global estimate of daily GPP and annual
NPP for every land cell; the paper is cited here on its registry
record.[^gpp-guide][^running-2004][^running-2004-crossref]

## The model

The algorithm is a radiation use efficiency model. Daily GPP is
epsilon times APAR, where APAR is the incident PAR times the MOD15
FPAR and the incident PAR is 0.45 times the incident shortwave
radiation from the GMAO reanalysis (equations 1.2 and 1.3); epsilon is
a biome maximum light use efficiency, epsilon max, times two scalars
that ramp linearly from 1 to 0 as the daily minimum temperature falls
between two thresholds and as the daytime vapour pressure deficit
rises between two thresholds (equation 1.1, Table 1.1).[^gpp-guide][^gpp-atbd]
GPP is truncated on days with air temperature below 0 degrees C and
progressively limited above a vapour pressure deficit of the order of
2000 Pa, the guide's global generalization of stomatal
closure.[^gpp-guide] The five parameters and the respiration
coefficients come from the biome properties look-up table (BPLUT), one
column per University of Maryland land cover class read from the
MCDLCHKM land cover product; the guide prints the table (Table 2.2)
with epsilon max from 0.000841 kg C per MJ for open shrubland to
0.001281 for closed shrubland, minimum temperature ramps from -8 to
-6 degrees C (-8 for most classes, -7 for mixed forest, -6 for
deciduous broadleaf forest) up to between 8.31 and 12.02 degrees C, and vapour pressure deficit
ramps from 650 or 800 Pa to between 1650 and 5300 Pa.[^gpp-guide] The
guide calls the assumption that these biome parameters do not vary in
space or time arguably the most significant in the logic: a
semi-desert grassland in Mongolia is treated the same as a tallgrass
prairie in the Midwestern United States.[^gpp-guide] The land cover
maps are stated to be accurate to within 65 to 80 per cent, higher
where pixels are homogeneous.[^gpp-guide]

Net photosynthesis subtracts daily leaf and fine root maintenance
respiration from GPP: leaf mass is the MOD15 LAI divided by the
biome's specific leaf area, fine root mass is leaf mass times a biome
ratio, and each respires at a base rate at 20 degrees C scaled by a
Q10 function of the daily average temperature, with Q10 fixed at 2.0
for fine roots and live wood and, for leaves, the temperature
acclimated form 3.22 minus 0.046 times the average temperature
(equations 1.4 to 1.8, 1.11).[^gpp-guide] The eight-day file holds
the sums of daily GPP and of daily net photosynthesis over eight
consecutive days; 46 periods make a year and the last one holds five
days, or six in a leap year, so the guide says a daily estimate is the
stored sum divided by eight for the first 45 periods and by five or
six for the last.[^gpp-guide] Live wood maintenance respiration and
growth respiration are not in the eight-day product.[^gpp-guide]

The annual product adds live wood maintenance respiration from the
annual maximum leaf mass and then growth respiration, which since the
Collection 6 logic is parameterized as 25 per cent of NPP rather than
from the annual maximum LAI, because the retrieved LAI is mostly
saturated above 3 and the forest maximum is set to 6.8; annual NPP is
therefore 0.8 times (GPP minus maintenance respiration) where that
difference is positive and 0 where it is not (equations 1.12 and
1.13).[^gpp-guide]

## The inputs and their treatment

FPAR and LAI come from the eight-day MOD15A2H, whose compositing
selects the maximum FPAR across the eight days with the LAI of the
same day, so the model assumes leaf area and FPAR constant within
each period although productivity is computed daily ([this bundle's
MOD15 concept](mod15-lai-fpar.md)).[^gpp-guide][^mod15] Cloud and
aerosol contaminated FPAR and LAI introduce substantial error, and the
collection handles them in two ways. In the operational eight-day
product, since Collection 6.1, the climatology MCD15A2HCL, the average
of the best FPAR and LAI for each eight-day period over the past five
years from both Terra and Aqua (five years chosen as about the length
of an ENSO cycle, a longer span obscuring disturbance and land use
change), replaces contaminated MOD15A2H values for the corresponding
period; the guide shows the effect as higher FPAR and GPP in a cloudy
Amazon tile and almost none in a clear Mongolian tile, and notes that
the climatology can bias the result because it smooths out
interannual variability, disturbance and recovery.[^gpp-guide] In the
year-end gap-filled products, once all 46 periods of the year's
MOD15A2H exist, poor quality FPAR and LAI are removed by their quality
label and filled by linear interpolation between the previous and next
periods that pass, and the productivity is recomputed; the guide notes
that some periods have low FPAR and LAI with good quality labels and
that the label is nonetheless the only source of quality control, and
that the filling generally raises FPAR and so GPP.[^gpp-guide][^a3hgf-page]
For the first mission year the gap filling had no data from the start
of the year to the first MOD15A2H, which the guide dates 2000-02-28
for Terra, and the RANGEBEGINNINGDATE metadata of that year's annual
file reflects the mission start rather than January 1.[^gpp-guide] That
caution concerns the year 2000, while the Collection 6.1 MOD17A3HGF
extent begins 2001-01-01 and no 2000 granule exists in the collection,
so the year the guide warns about is not in this collection as
read.[^cmr-a3hgf][^cmr-a3hgf-granules]

The meteorology is the GMAO GEOS-5 reanalysis at hourly time step and
about 0.5 by 0.67 degrees, aggregated to daily minimum and average
temperature, incident shortwave radiation and specific humidity, with
the vapour pressure deficit computed for daytime hours (those with
downward solar radiation above zero); the fields are interpolated to
the 500 m pixel from the four nearest reanalysis cells with a modified
cosine weighting, which removes the cell boundary lines visible in
Collection 4 but leaves the reanalysis's own errors, which the guide
says are larger in the tropics and where weather stations are
sparse.[^gpp-guide] The algorithm document describes the launch-era
version of the same design on the integerized sinusoidal grid at 1 km
with Data Assimilation Office fields.[^gpp-atbd] The tiles follow the
sinusoidal tiling system described in this bundle's MOD13 concept
([the grid gotcha](../gotchas/sinusoidal-grid-cell-area.md)).[^cmr-a2h][^mod13][^grid-gotcha]

## Layers

The guide's Tables 4.1 and 4.2 and the product page variables tables
give three scientific data sets in each product:[^gpp-guide][^a2h-page][^a3hgf-page]

| Product | Layer | Content | Type | Valid range | Fill (product page) | Fill codes (guide) | Scale | Unit after scaling |
|---|---|---|---|---|---|---|---|---|
| MOD17A2H | Gpp_500m | eight-day total GPP | int16 | 0 to 30000 | 32761 | 32767 fill, 32766 to 32761 land cover codes | 0.0001 | kg C per square metre per eight days |
| MOD17A2H | PsnNet_500m | eight-day total net photosynthesis | int16 | -30000 to 30000 | 32761 | the same | 0.0001 | kg C per square metre per eight days |
| MOD17A2H | Psn_QC_500m | quality control, bit field | uint8 | 0 to 254 | 255 | | none | |
| MOD17A3HGF | Gpp_500m | annual sum of GPP | uint16 | 0 to 65500 | 65529 | 65535 fill, 65534 to 65529 land cover codes | 0.0001 | kg C per square metre per year |
| MOD17A3HGF | Npp_500m | annual NPP | int16 | -30000 to 32700 | 32761 | 32767 fill, 32766 to 32761 land cover codes | 0.0001 | kg C per square metre per year |
| MOD17A3HGF | Npp_QC_500m | percentage of growing-season days with filled inputs | uint8 | 0 to 100 | 249 | 255 fill, 254 to 249 land cover codes | none | per cent |

The guide says that although the file attributes list one fill value,
there are seven for the non-vegetated pixels for which GPP and net
photosynthesis were not computed: on the int16 layers 32767 is the
fill proper, 32766 perennial salt or water bodies, 32765 barren or
sparse vegetation, 32764 perennial snow or ice, 32763 permanent
wetlands, 32762 urban or built-up and 32761 unclassified; the uint16
annual GPP uses 65535 down to 65529 in the same order and the uint8
quality layer 255 down to 249, with 253 on the non-gap-filled annual
product also used for data gaps from cloud and snow over vegetated
pixels.[^gpp-guide] The product pages render only the lowest code of
each range as the fill, while the CMR variable records for the two
collections, from which the catalog's layer tables are rendered, list
all seven codes with their land cover meanings.[^a2h-page][^a3hgf-page][^cmr-vars] All the codes lie inside
their data types above the valid ranges, so the valid range is the
test that separates data from code ([the model outputs
gotcha](../gotchas/lai-and-gpp-are-model-outputs.md)).[^gpp-guide][^model-gotcha]
The guide's text under Table 4.1 gives the net photosynthesis range as
-3000 to 3000 where the table gives -30000 to 30000, and the product
page agrees with the table; the text is read here as a copying
slip.[^gpp-guide][^a2h-page]

## Quality

Psn_QC_500m on the eight-day product directly inherits FparLai_QC
from the MOD15A2H of the same period, with the same bit layout: bit 0
the MODLAND quality, bit 1 the sensor, bit 2 the dead detector flag,
bits 3 to 4 the cloud state and bits 5 to 7 the SCF_QC algorithm path,
as this bundle's MOD15 concept tabulates.[^gpp-guide][^mod15] For the
operational eight-day product the guide suggests at least excluding
cloud-contaminated cells; for the year-end gap-filled products it says
the quality layer only denotes whether filled inputs were used, so a
reader may ignore it and keep the pixels within the valid
range.[^gpp-guide] Npp_QC_500m on the annual product is not a bit field
but 100 times the number of growing-season days on which filled LAI
and FPAR had to be used divided by the number of growing-season days,
the growing season being the days with minimum temperature above the
BPLUT stomatal closure threshold; a value of 85 means filled inputs on
85 per cent of the growing days, and the guide expects humid forests
to be high and dry grasslands and shrublands low.[^gpp-guide] The
product pages state that validation at stage 3 has been achieved for
the gross and net primary productivity products and point to the
LDOPE site for known issues, and the annual page adds that operational
and uncertainty issues are in section 2 of the guide; the LDOPE site
and the LAADS file specifications are on domains outside this seed's
reading list.[^a2h-page][^a3hgf-page][^cmr-a2h]

## Access

Cloud-hosted: the product pages mark both collections cloud enabled,
and the CMR records distribute them over HTTPS and the Earthdata Cloud
in HDF-EOS2 at 3.4 MB (eight-day) and 7 MB (annual) per file from the
buckets `s3://lp-prod-protected/MOD17A2H.061` and
`s3://lp-prod-protected/MOD17A3HGF.061` with public counterparts,
region us-west-2, temporary credentials at
data.lpdaac.earthdatacloud.nasa.gov/s3credentials.[^a2h-page][^cmr-a2h][^cmr-a3hgf]
The data links are Earthdata Search on the collection concept ids and
AppEEARS.[^cmr-a2h][^cmr-a3hgf]

## Uncertainty

The files carry no per-pixel uncertainty on GPP, net photosynthesis
or NPP. What stands in, as the guide's section 2 states it:

- **The fixed biome parameters.** One BPLUT column per land cover
  class, invariant in space and season, the assumption the guide
  calls arguably the most significant; the class itself is 65 to 80
  per cent accurate.[^gpp-guide]
- **The reanalysis weather.** Coarse GMAO fields interpolated to
  500 m; the guide says the uncertainties of GMAO and of the resulting
  GPP and NPP are higher in the tropics than elsewhere.[^gpp-guide]
- **The FPAR and LAI inputs.** The MOD15 retrieval's own quality
  (algorithm path, saturation, its standard deviation layers) enters
  the model unweighted, held constant over each eight-day period, and
  where contaminated is replaced by a five-year climatology in the
  eight-day product or an interpolation in the year-end product; the
  quality layers say which, not by how much the value
  changed.[^gpp-guide][^mod15]
- **The respiration terms.** Allometric ratios and base rates from
  the BIOME-BGC parameter lists, growth respiration fixed at 25 per
  cent of NPP; the eight-day product omits live wood and growth
  respiration entirely.[^gpp-guide]
- **Validation.** Stage 3 on the product pages; the guide describes
  the strategy of substituting tower meteorology, ground FPAR and
  process models into the algorithm to isolate error sources, and
  names the flux tower comparisons and the global NPP reviews by Ito
  (2011) and Pan and others (2014).[^a2h-page][^gpp-guide]

The hydrology plugin's MOD16 evapotranspiration concept, at
knowledge/datasets/mod16a2gf.md in that plugin's own bundle, covers
the sibling product built on the same MOD15 inputs, the same land
cover dependence and the same GMAO forcing; it is named here and not
repeated.

[^a2h-page]: LP DAAC product page, MOD17A2H v061, read 2026-09-15
[^a3hgf-page]: LP DAAC product page, MOD17A3HGF v061, read 2026-09-15
[^gpp-guide]: MOD17 User's Guide for Collection 6.1, version 1.1, March 2021
[^gpp-atbd]: MOD17 Algorithm Theoretical Basis Document, version 3.0, April 1999
[^cmr-a2h]: CMR collection record C2565791027-LPCLOUD, read 2026-09-15
[^cmr-a3hgf]: CMR collection record C2565791034-LPCLOUD, read 2026-09-15
[^cmr-a2hgf]: CMR collection record C2565791029-LPCLOUD, read 2026-09-15 for its temporal extent
[^cmr-a3hgf-granules]: CMR granule search on C2565791034-LPCLOUD for 2000, read 2026-09-15
[^cmr-vars]: CMR variable records for the MOD17A2H and MOD17A3HGF v061 collections, read 2026-09-15
[^doi-a2h]: the MOD17A2H DOI resolved at doi.org, 2026-09-15
[^doi-a3hgf]: the MOD17A3HGF DOI resolved at doi.org, 2026-09-15
[^running-2004]: Running and others 2004, BioScience 54(6), doi:10.1641/0006-3568(2004)054[0547:ACSMOG]2.0.CO;2, cited on its Crossref record
[^running-2004-crossref]: Crossref record for the Running and others 2004 DOI, read 2026-09-15
[^mod15]: this bundle's MOD15 concept
[^mod13]: this bundle's MOD13 concept
[^model-gotcha]: this bundle's gotcha on model outputs and their quality layers
[^grid-gotcha]: this bundle's gotcha on the sinusoidal grid
