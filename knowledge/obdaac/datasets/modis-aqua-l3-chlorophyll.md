---
type: dataset
spheres: [biosphere, hydrosphere]
title: "MODIS-Aqua Level 3 mapped chlorophyll-a (OB.DAAC, reprocessing R2022)"
description: "The Ocean Biology Processing Group's Level 3 mapped chlorophyll-a concentration from MODIS on Aqua: one variable, chlor_a, from the blended OCI algorithm (color index below 0.25 mg per cubic metre, OC3M band ratio above 0.35, a weighted transition between), on 4 km and 9 km equidistant cylindrical grids, as daily, 8-day, monthly, rolling 32-day, seasonal and annual composites plus monthly, seasonal and cumulative climatologies, from 4 July 2002 onward, in the R2022 reprocessing (files carry processing_version R2022.0.3); a separate near-real-time collection runs ahead of the refined record."
tags: [modis, aqua, chlorophyll, chlor_a, ocean-color, level3, mapped, obdaac, obpg, r2022, oci-algorithm]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:30:00Z }
resource: https://cmr.earthdata.nasa.gov/search/concepts/C3380709133-OB_CLOUD.umm_json
version: "Reprocessing R2022 (collection version 2022.0; the files opened on 2026-09-14 carry processing_version R2022.0.3), CMR-verified 2026-09-14: MODISA_L3m_CHL (C3380709133-OB_CLOUD, DOI 10.5067/AQUA/MODIS/L3M/CHL/2022.0, 27028 granule records, temporal extent from 2002-07-04 with no end), its binned companion MODISA_L3b_CHL (C3380708988-OB_CLOUD, DOI 10.5067/AQUA/MODIS/L3B/CHL/2022.0) and the near-real-time collection MODISA_L3m_CHL_NRT (C3380709124-OB_CLOUD); on 2026-09-14 the last refined daily granule was 2026-05-30 and the last near-real-time daily granule was 2026-09-12"
status: draft
stale_after: 2027-03-14
sources:
  - id: cmr-modis
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C3380709133-OB_CLOUD.umm_json
    title: "CMR collection record for MODISA_L3m_CHL version 2022.0 (read 2026-09-14): entry title, DOI, temporal extent from 2002-07-04 ending at present, platform and instrument, the abstract with its coastal and inland water caveat, the additional attributes CompositingPeriod, SpatialResolution and Product, and the related links to the OPeNDAP service, the direct data access directory, the reprocessing history page and the chlorophyll ATBD"
  - id: cmr-modis-l3b
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C3380708988-OB_CLOUD.umm_json
    title: "CMR collection record for the binned companion MODISA_L3b_CHL version 2022.0 (read 2026-09-14): DOI 10.5067/AQUA/MODIS/L3B/CHL/2022.0, the same abstract and temporal extent"
  - id: cmr-collections
    resource: https://cmr.earthdata.nasa.gov/search/collections.json?short_name=MODISA_L3m_C*&options[short_name][pattern]=true&page_size=100
    title: "CMR collection searches run 2026-09-14: the short-name pattern MODISA_L3m_C* returns only MODISA_L3m_CHL and MODISA_L3m_CHL_NRT, both version 2022.0 under provider OB_CLOUD; a keyword search for MODIS Aqua chlorophyll under provider OB_DAAC returns no satellite collection"
  - id: cmr-granules
    resource: https://cmr.earthdata.nasa.gov/search/granules.json?collection_concept_id=C3380709133-OB_CLOUD&temporal=2024-06-15T12:00:00Z,2024-06-15T12:00:01Z&page_size=500
    title: "CMR granule searches run 2026-09-14 on C3380709133-OB_CLOUD: every granule whose period contains 2024-06-15 (the 4 km and 9 km files of the DAY, 8D, MO, R32, YR, SNSP, SCSP, SCSU, SCAU, SCWI, MC and CU periods, some climatology files listed under two record names), the granules of calendar 2025 counted by period code and grid, the first granules by start date and the last by descending start date (2026-05-30, daily), and the CMR-Hits header (27028); the same searches on the near-real-time collection C3380709124-OB_CLOUD (last daily granule 2026-09-12)"
  - id: modis-file
    resource: https://oceandata.sci.gsfc.nasa.gov/opendap/MODISA/L3SMI/2024/0601/AQUA_MODIS.20240601_20240630.L3m.MO.CHL.chlor_a.4km.nc.das
    title: "The attribute listing (OPeNDAP .das, metadata only, no data read) of the June 2024 monthly 4 km file, read 2026-09-14 through the OPeNDAP service the CMR record lists: the chlor_a variable attributes (long name, units, fill, valid range, the reference attribute citing Hu and others 2019 and O'Reilly and Werdell 2019), the grid attributes, temporal_range month, measure Mean, processing_version R2022.0.3, date_created 2026-07-10, the l2_flag_names list, the id naming the binned source file, the product DOI and data_minimum and data_maximum; the same listing read for the daily file of 2026-05-30 (created 2026-07-08), the 9 km cumulative climatology ending 2025-11-30 (temporal_range 24-year, created 2026-07-13) and the 9 km January monthly climatology ending 2026-01-31 (temporal_range 23-year)"
  - id: catalog-modis
    resource: https://doi.org/10.5067/AQUA/MODIS/L3M/CHL/2022.0
    title: "The product DOI, which resolved on 2026-09-14 to the Earthdata catalog page for MODISA_L3m_CHL version 2022.0 (read there): the description, the concept id, the granule count 27028, netCDF-4 format, the temporal extent 2002-07-04 to present, data state ACTIVE, processing level 3 and the published and updated dates 2025-01-23"
  - id: atbd
    resource: https://oceancolor.gsfc.nasa.gov/files/atbd/atbd-obdaac-chlorophyll-a.pdf
    title: "Chlorophyll a, Algorithm Theoretical Basis Document version 1.1, 6 November 2023, Werdell, O'Reilly, Hu, Feng, Lee, Franz, Bailey, Proctor and Wang, DOI 10.5067/JCQB8QALDOYD, 18 pages, read in full 2026-09-14 (the OB.DAAC URL redirects to the same file on the OB.DAAC data host): the R2022 implementation of the blended OCI algorithm, the CI and OCx equations, the sensor coefficient table (MODIS OC3M), the 0.25 to 0.35 transition, the earlier 0.15 to 0.2 transition, the validation method and criteria, the accuracy goals and the reference list"
  - id: obdaac-site
    resource: https://oceancolor.gsfc.nasa.gov/data/reprocessing/
    title: "The reprocessing history page the CMR record links, requested 2026-09-14: the OB.DAAC website (this page, the product pages, the algorithm pages and the R2022 validation pages the ATBD cites) redirects to the Ocean Biology DAAC landing page on the Earthdata site, so none of them was read; only the /files/ paths on that host still serve documents, by redirect to the OB.DAAC data host"
  - id: ancillary
    resource: https://oceancolor.gsfc.nasa.gov/files/obdaac-ancillary-data-sources.pdf
    title: "Ancillary Data at OB.DAAC (8 pages, read 2026-09-14): the two-step processing, near-real-time with the best ancillary data available at the time and refined processing once the optimal ancillary data exist"
  - id: alerts
    resource: https://www.earthdata.nasa.gov/data/alerts-outages/aqua-safe-mode-alert
    title: "Earthdata data alert, Aqua Safe Mode Alert, issued 2022-03-31 and resolved 2022-04-17 (an LP DAAC alert about the instrument, read 2026-09-14): Aqua entered safe mode on 2022-03-31, MODIS produced no science data until it returned to science mode on 2022-04-15, and usable day data resumed on 2022-04-17; the Earthdata alerts list read the same day also names Aqua MODIS data losses on 22, 27 and 28 July 2023 and 22 to 25 March 2024 (titles only)"
  - id: aqua-project
    resource: https://aqua.nasa.gov/
    title: "The Aqua Project Science home page (read 2026-09-14): the statement that, because of fuel limitations, Aqua completed the last of its drag make-up maneuvers in December 2021 and is in a free-drift mode, descending below the A-Train and drifting to later equatorial crossing times and lower altitudes, with a weekly-updated chart of the mean local equator crossing time and altitude through 2027; the page says nothing about the effect on the ocean color products"
  - id: hu-2019
    resource: https://doi.org/10.1029/2019JC014941
    title: "Hu, Feng, Lee, Franz, Bailey, Werdell and Proctor, 2019, Improving satellite global chlorophyll a data products through algorithm refinement and data recovery, Journal of Geophysical Research: Oceans 124, 1524 to 1543 (registry record verified on Crossref and abstract read there 2026-09-14; the publisher page returned 403 to this environment and the article was not read): the OCI2 coefficients and transition, the cross-sensor consistency and the relaxed straylight masking"
  - id: oreilly-werdell-2019
    resource: https://doi.org/10.1016/j.rse.2019.04.021
    title: "O'Reilly and Werdell, 2019, Chlorophyll algorithms for ocean color sensors, OC4, OC5 and OC6, Remote Sensing of Environment 229, 32 to 47 (registry record verified on Crossref 2026-09-14; the record carries no abstract, the publisher page was not reachable and the article was not read): the OCx coefficients the ATBD adopts"
  - id: hu-2012
    resource: https://doi.org/10.1029/2011JC007395
    title: "Hu, Lee and Franz, 2012, Chlorophyll a algorithms for oligotrophic oceans, a novel approach based on three-band reflectance difference, Journal of Geophysical Research: Oceans 117, C01011 (registry record verified on Crossref and abstract read there 2026-09-14; the publisher page returned 403 and the article was not read): the color index, its range and its tolerance to noise and atmospheric correction error"
---

# MODIS-Aqua Level 3 mapped chlorophyll-a

**Identity.** The Ocean Biology Processing Group's standard Level 3
mapped chlorophyll-a from the Moderate Resolution Imaging
Spectroradiometer on Aqua, distributed by the Ocean Biology DAAC as
the collection MODISA_L3m_CHL, version 2022.0, with a temporal extent
from 4 July 2002 and no end date, DOI
10.5067/AQUA/MODIS/L3M/CHL/2022.0 and concept id
C3380709133-OB_CLOUD; the binned Level 3 product it is mapped from is
the collection MODISA_L3b_CHL (C3380708988-OB_CLOUD, DOI
10.5067/AQUA/MODIS/L3B/CHL/2022.0), and a near-real-time mapped
collection MODISA_L3m_CHL_NRT (C3380709124-OB_CLOUD) runs ahead of the
refined record.[^cmr-modis][^cmr-modis-l3b][^cmr-collections] The
version is the OB.DAAC's multi-mission reprocessing R2022: the files
opened on 2026-09-14 carry processing_version R2022.0.3, and the ATBD
describes the chlorophyll algorithm as implemented in that
reprocessing.[^modis-file][^atbd] The retrieval is the blended OCI
algorithm: the three-band color index of Hu, Lee and Franz for
retrievals below 0.25 mg per cubic metre, the OC3M band ratio (the
greater of the 443 and 488 nm reflectances over the 547 nm
reflectance, a fourth-order polynomial in log space with
MODIS-specific coefficients) above 0.35, and a weighted blend of the
two in between; the coefficients are those of Hu and others 2019 and
O'Reilly and Werdell 2019, and the file's chlor_a variable cites both
papers in its reference attribute.[^atbd][^hu-2012][^hu-2019][^oreilly-werdell-2019][^modis-file]
CMR catalogues no other version of the collection: a short-name
pattern search on 2026-09-14 returned only the 2022.0 refined and
near-real-time collections.[^cmr-collections]

**Structure.** Each file holds one variable, `chlor_a` (float32, mg
per cubic metre, fill value -32767, valid range 0.001 to 100, long
name "Chlorophyll Concentration, OCI Algorithm"), with `lat`, `lon`
and a `palette`, on an equidistant cylindrical grid: 4320 by 8640
cells at 0.0416667 degrees (the file states 4.638 km) for the 4 km
files and 2160 by 4320 for the 9 km files (9.277 km).[^modis-file]
The global attributes carry `temporal_range` (day, month, 24-year),
`measure` "Mean", `processing_version`, `date_created`, the
`l2_flag_names` list (ATMFAIL, LAND, HILT, HISATZEN, STRAYLIGHT,
CLDICE, COCCOLITH, LOWLW, CHLWARN, CHLFAIL, NAVWARN, MAXAERITER,
ATMWARN, HISOLZEN, NAVFAIL, FILTER, HIGLINT), a `data_bins` count, the
data minimum and maximum, the product DOI and an `id` naming the
binned file the map was made from (for June 2024,
R2022.0.3/L3/AQUA_MODIS.20240601_20240630.L3b.MO.CHL.nc); there is no
count, weight or uncertainty layer in the mapped
file.[^modis-file] File names read
AQUA_MODIS.<start>_<end>.L3m.<period>.CHL.chlor_a.<4km or 9km>.nc,
and the granule records for a single date on 2026-09-14 show the
periods the collection carries at both grids: DAY, 8D (8-day), MO
(monthly), R32 (a rolling 32-day window issued every eight days), YR
(annual), SNSP, SNSU, SNAU and SNWI (the four seasons of one year),
SCSP, SCSU, SCAU and SCWI (seasonal climatologies over the record), MC
(monthly climatologies) and CU (the cumulative climatology over the
whole record).[^cmr-granules] In calendar 2025 the catalogue held, per
grid, 699 daily, 87 8-day, 92 rolling 32-day and 23 monthly records
(the monthly and daily counts include records listed under two naming
styles), plus the climatology files whose end date falls in
2025.[^cmr-granules] The climatology files are re-cut as the record
extends and are named by their span: monthly climatologies ending in
2024, 2025 and 2026 coexist in the catalogue, the cumulative
climatology ending 2025-11-30 carries temporal_range "24-year" and
was created on 2026-07-13, and the January climatology ending
2026-01-31 carries "23-year".[^cmr-granules][^modis-file] The
collection counted 27028 granule records on 2026-09-14; the last
refined daily granule was 2026-05-30 (created 2026-07-08), while the
near-real-time collection's last daily granule was 2026-09-12, so the
refined record trails by about three and a half
months.[^cmr-granules][^catalog-modis][^modis-file] Near-real-time
files are processed with the best ancillary data available at the
time and are later replaced by the refined processing once the
optimal ancillary data exist.[^ancillary]

## Uncertainty

- **No uncertainty field in the mapped product.** The Level 3 mapped
  file carries `chlor_a` alone; there is no per-pixel uncertainty,
  no count of contributing observations and no flag layer, only the
  list of Level 2 flag names in the global attributes.[^modis-file]
- **The stated accuracy goal is a community figure, not a
  measurement of this product.** The ATBD quotes the generally
  accepted goals of plus or minus 5 percent for water-leaving
  radiance and plus or minus 35 percent for open-ocean chlorophyll,
  states that overall validation results indicate good performance,
  and states that regional differences can be large and that
  validation for a local study area may be necessary.[^atbd]
- **Validation is by SeaBASS match-ups against Level 2, not Level 3.**
  The ATBD's validation uses satellite-to-in-situ pairs within 3 hours
  at sensor zenith below 60 degrees and solar zenith below 75 degrees,
  the mean of a 5 by 5 pixel box with a homogeneity test and at least
  half the pixels unflagged, and it recommends native-resolution
  products for validation rather than sub-sampled data; the per-mission
  R2022 match-up statistics it points to are on OB.DAAC web pages that
  now redirect to the Earthdata landing page and were not
  read.[^atbd][^obdaac-site]
- **The collection's own caveat.** The collection description states
  that retrievals in optically complex coastal and inland waters may
  carry higher uncertainty and refers to the algorithm
  documentation.[^cmr-modis][^catalog-modis]
- **Algorithm-level uncertainty.** The color index was designed for
  low-chlorophyll water (0.25 mg per cubic metre and below, about 78
  percent of the ocean area) and is less sensitive than band ratios to
  instrument noise and imperfect atmospheric correction; the 2019
  retuning reports the mean cross-sensor difference in monthly
  oligotrophic chlorophyll falling from about 10 percent with OCx to 1
  to 2 percent with OCI2. Those are statements about the algorithm's
  consistency, not a per-pixel error.[^hu-2012][^hu-2019]

## Known issues

- [chlor-a-blended-ocx-and-ci](../gotchas/chlor-a-blended-ocx-and-ci.md):
  chlor_a is the output of two algorithms blended between 0.25 and
  0.35 mg per cubic metre, so a threshold, histogram or gradient
  inside that range measures the blend, and coastal and inland values
  carry the collection's own higher-uncertainty caveat.
- [chlor-a-composite-sampling-gaps](../gotchas/chlor-a-composite-sampling-gaps.md):
  a composite is the mean of the flagged-and-binned observations that
  existed in the period, with no count in the mapped file; cloud, sun
  angle, glint, ice and outages set the sampling.
- [chlor-a-one-reprocessing-per-series](../gotchas/chlor-a-one-reprocessing-per-series.md):
  a reprocessing changes the whole record, the catalogue keeps one
  version, and the refined record trails the near-real-time one.
- [chlor-a-is-not-biomass](../gotchas/chlor-a-is-not-biomass.md):
  the product is a near-surface pigment concentration that the
  producer calls a proxy for biomass; carbon and primary production
  are separate products.
- The OB.DAAC website (product pages, algorithm pages, the
  reprocessing history and the R2022 validation pages) redirected to
  the Ocean Biology DAAC landing page on the Earthdata site on
  2026-09-14; the ATBD and the ancillary-data document remain
  reachable at their /files/ paths by redirect to the data host, and
  the product DOI resolves to an Earthdata catalog page. The R2022
  reprocessing notes for MODIS-Aqua were therefore not
  read.[^obdaac-site][^catalog-modis]
- Instrument outages leave holes in the daily record: Aqua was in
  safe mode from 2022-03-31 and MODIS produced usable day data again
  from 2022-04-17, and the Earthdata alerts list names Aqua MODIS data
  losses on 22, 27 and 28 July 2023 and 22 to 25 March 2024.[^alerts]
- The platform is drifting. The Aqua Project Science page states
  that, because of fuel limitations, Aqua completed the last of its
  drag make-up maneuvers in December 2021 and is in a free-drift mode,
  descending below the A-Train and drifting to later equatorial
  crossing times and lower altitudes, with the crossing time and
  altitude charted month by month through 2027. No producer source
  read for this concept states the effect of the drift on this
  chlorophyll record, so it is recorded here as a platform fact, not
  as a gotcha.[^aqua-project]

[^cmr-modis]: CMR collection record, C3380709133-OB_CLOUD
[^cmr-modis-l3b]: CMR collection record, C3380708988-OB_CLOUD
[^cmr-collections]: CMR collection searches, 2026-09-14
[^cmr-granules]: CMR granule searches on the refined and near-real-time collections, 2026-09-14
[^modis-file]: Attribute listings of four MODIS-Aqua L3m CHL files, read through OPeNDAP on 2026-09-14
[^catalog-modis]: The product DOI and the Earthdata catalog page it resolves to, 2026-09-14
[^atbd]: Chlorophyll a ATBD version 1.1, OB.DAAC, 6 November 2023
[^obdaac-site]: The OB.DAAC website redirect observed on 2026-09-14
[^ancillary]: Ancillary Data at OB.DAAC
[^alerts]: Earthdata data alert, Aqua Safe Mode Alert, and the alerts list, 2026-09-14
[^aqua-project]: Aqua Project Science home page, read 2026-09-14
[^hu-2019]: Hu and others, 2019, Journal of Geophysical Research: Oceans, doi:10.1029/2019JC014941
[^oreilly-werdell-2019]: O'Reilly and Werdell, 2019, Remote Sensing of Environment, doi:10.1016/j.rse.2019.04.021
[^hu-2012]: Hu, Lee and Franz, 2012, Journal of Geophysical Research: Oceans, doi:10.1029/2011JC007395
