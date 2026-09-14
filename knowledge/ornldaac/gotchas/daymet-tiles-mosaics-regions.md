---
type: dataset-gotcha
spheres: [atmosphere, geosphere]
title: "Tiles, mosaics and region files are three cuts of one estimate: the 2-degree tiles are mosaicked into the per-region files, and the three regions differ in extent, start year and service coverage"
description: "Daymet is computed on 2-degree by 2-degree tiles with a fixed TileID, and the ORNL DAAC mosaics those tiles into one seamless netCDF per variable and year for each of three separately processed regions, continental North America, Hawaii and Puerto Rico. A tile and the mosaic that contains it are the same estimate in different files, not two products or versions. The region files have different extents and start years (Puerto Rico from 1950, the others from 1980), a point in Hawaii lies inside the North America bounding box yet only in the Hawaii file, the CMR collection holds mosaics only, and the single pixel service covers a narrower latitude and longitude window than the North America file and none of Puerto Rico before 1980."
tags: [daymet, tiles, mosaics, regions, thredds, subsetting, extent, ornldaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:40:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-14T12:17:15Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/143 }
severity: medium
# medium: the tile, mosaic and region structure is documented on the
# project site and in the guide, and a wrong choice usually shows as a
# missing file or an empty subset rather than a plausible number; no
# eval case is required.
dataset: ../datasets/daymet-v4.md
status: stable
stale_after: 2027-03-14
sources:
  - id: daymet-overview
    resource: https://daymet.ornl.gov/overview
    title: "Daymet project site, description page: the 2-degree processing tiles identified by a TileID consistent across the record, the DAAC's mosaicking of the tiles into seamless per-variable per-year files, and the note that Puerto Rico before 1980 is not available through the single pixel tool"
  - id: daymet-getdata
    resource: https://daymet.ornl.gov/getdata
    title: "Daymet project site, get data page: tiled subsets as 2-degree netCDF subsets of the North American extent through THREDDS, the TileID convention, and the other access paths"
  - id: daymet-tst-retirement
    resource: https://daymet.ornl.gov/tile-selection-tool-retirement
    title: "Daymet project site, tile selection tool retirement notice: the tool released in 2012 was retired on a July 6 (the page names no year), and tiled data continue through THREDDS with scripted download examples"
  - id: daymet-web-services
    resource: https://daymet.ornl.gov/web_services.html
    title: "Daymet project site, web services page: THREDDS instances for the North American dataset, the 2-degree tiles and the climatologies, and the single pixel service's stated latitude (14.5 N to 52.0 N) and longitude (131.0 W to 53.0 W) limits"
  - id: ornl-v4-guide
    resource: https://daac.ornl.gov/DAYMET/guides/Daymet_Daily_V4.html
    title: "ORNL DAAC user guide, Daymet Daily V4 (documentation revision 2024-06-17): the three region files and their bounding boxes, the file naming with region na, hi or pr, the start years, and the release record naming 2-degree tiles from 2012 and mosaics from 2014"
  - id: cmr-daily-v4r1
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2532426483-ORNL_CLOUD.umm_json
    title: "CMR collection record for Daymet Daily Version 4 R1 and its granule search: 1,176 granules named by region, variable and year with per-region bounding boxes, and no granule named as a tile"
  - id: thornton-2021
    resource: https://doi.org/10.1038/s41597-021-00973-0
    title: "Thornton and others, 2021, Scientific Data 8, 190: the three sub-domains processed independently with identical methods, and the usage notes listing the access services"
  - id: dataset
    resource: ../datasets/daymet-v4.md
    title: "This bundle's Daymet dataset concept, which lists this trap among the known issues"
---

# Tiles, mosaics and region files

**Mechanism.** The Daymet algorithm manages its domain as a system
of 2-degree by 2-degree tiles, each processed individually and
identified by a TileID that is derived within the algorithm and is
the same in every year of the record.[^daymet-overview][^daymet-getdata]
The ORNL DAAC mosaics the tiles into a seamless gridded netCDF file
per variable and year, and those mosaics are what the landing page,
the CMR collection and the netCDF subset service serve: the CMR
collection's 1,176 granules are named by region, variable and year,
and none is a tile.[^daymet-overview][^cmr-daily-v4r1] The tiles
remain available as smaller subsets of the North American extent
through the THREDDS server, after the tile selection tool that first
served them (released in 2012) was retired.[^daymet-getdata][^daymet-tst-retirement]
The mosaics come in three region files, na, hi and pr, because
continental North America, Hawaii and Puerto Rico are processed
independently with identical methods from three separate station
files; the region files have separate extents (North America 178.13 W
to 53.06 W and 14.07 N to 82.91 N, Hawaii 160.31 W to 154.77 W and
17.95 N to 23.52 N, Puerto Rico 67.99 W to 64.12 W and 16.84 N to
19.94 N) and separate start years, 1980 for North America and Hawaii
and 1950 for Puerto Rico.[^ornl-v4-guide][^thornton-2021] The single
pixel service, a separate access path that returns one cell's daily
series for a point, states its own limits: latitude between 14.5 N
and 52.0 N and longitude between 131.0 W and 53.0 W, and Puerto Rico
before 1980 is not available through it.[^daymet-web-services][^daymet-overview]

**Wrong-result mode.** A tile read beside the mosaic that contains
it, or two tiles read beside each other, is one estimate read twice,
not an ensemble or a version pair; an analysis that treats them as
independent (averaging them, differencing them for a "change",
counting them as separate samples) reports agreement or a zero
difference that says nothing. A region chosen by bounding box goes
wrong at Hawaii, whose longitudes and latitudes fall inside the North
America box while its cells exist only in the hi file: a subset of the
na file over Hawaii is empty or water, and a workflow that requests
the na file for a Hawaiian site reports no data or the wrong cells. A
Puerto Rico analysis that starts in 1980 because the other regions do
discards thirty years the pr files carry. A point request to the
single pixel service outside its stated window, including the whole
of Alaska and northern Canada that the North America file covers,
returns nothing where the mosaic has data, and a Puerto Rico series
requested through it starts in 1980 where the file starts in 1950.

**Correct approach.** The mosaic per region, variable and year is the
distributed product and the unit of citation; a tile is a spatial
subset of the same values, chosen when the area of interest fits in
it and the download volume matters, and never combined with the
mosaic as a second source.[^daymet-getdata][^daymet-tst-retirement]
The region is chosen by which file's domain holds the cells, with
Hawaii and Puerto Rico in their own files regardless of the North
America bounding box, and a Puerto Rico record runs from 1950 when
the analysis can use it.[^ornl-v4-guide] A single pixel extraction is
bounded by the service's stated window, and a point outside it is
served from the mosaics.[^daymet-web-services]

**Verification.** The project site's description and get data pages
document the tiles, the TileID and the mosaicking, and the retirement
notice documents where the tiles now live.[^daymet-overview][^daymet-getdata][^daymet-tst-retirement]
The guide lists the three region files with their bounding boxes and
start years, and the CMR granule search on 2026-09-14 returned
granules named by region, variable and year with per-region bounding
boxes and no granule named as a tile.[^ornl-v4-guide][^cmr-daily-v4r1]
The web services page states the single pixel window.[^daymet-web-services]
The paper states that the three sub-domains are processed
independently.[^thornton-2021] The THREDDS catalogs themselves were
not read for this concept: on the reading date they redirect to a
host outside the sources consulted. The dataset concept lists this
trap among the product's known issues.[^dataset]

[^daymet-overview]: Daymet project site, description page, read 2026-09-14
[^daymet-getdata]: Daymet project site, get data page, read 2026-09-14
[^daymet-tst-retirement]: Daymet project site, tile selection tool retirement notice, read 2026-09-14
[^daymet-web-services]: Daymet project site, web services page, read 2026-09-14
[^ornl-v4-guide]: ORNL DAAC user guide, Daymet Daily V4, revision 2024-06-17, read 2026-09-14
[^cmr-daily-v4r1]: CMR collection C2532426483-ORNL_CLOUD and its granule search, read 2026-09-14
[^thornton-2021]: Thornton and others, 2021, Scientific Data 8, 190, doi:10.1038/s41597-021-00973-0, read at nature.com 2026-09-14
[^dataset]: This bundle's Daymet dataset concept
