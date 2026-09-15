---
type: dataset-gotcha
spheres: [biosphere, geosphere]
title: "MODIS sinusoidal cells are equal-area but not 250 m or 500 m squares and not aligned with latitude and longitude: the nominal 500 m cell is 463 m on the 6371007.181 m sphere, a tile's bounding rectangle in degrees is not its footprint, and a reprojection to a geographic grid changes cell areas, resamples the indices and breaks the bit fields and the day of the year layer"
description: "Every MODIS land tile is a square block of the sinusoidal projection, 10 by 10 degrees at the equator, 4800, 2400 or 1200 cells on a side at the nominal 250 m, 500 m and 1 km, on a sphere of radius 6371007.181 m; the guide calls the projection equal area, and the corners are given accurately only by the projection coordinates in the metadata, while the bounding rectangle and ring point fields give the latitude and longitude of the geographic tile. Ten degrees of arc on that sphere is 1,111,950 m, so the 500 m cell is 463.31 m and covers 0.2147 square kilometres, not 0.25, and a tile away from the equator is not a rectangle of degrees. A script that multiplies a pixel count by 0.25 square kilometres, selects tiles or pixels by a latitude and longitude box, or reprojects the file to a geographic grid with an interpolating resampler before decoding the quality bits and the day of the year layer overstates areas by a sixth, clips the tile along the wrong edges, and blends integers that were never quantities."
tags: [modis, sinusoidal, projection, tile, cell-area, reprojection, resampling, mod13, mod15, mod17, lpdaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T17:50:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-15T18:34:53Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/172 }
severity: low
dataset: ../datasets/mod13-vegetation-indices.md
status: stable
stale_after: 2027-03-15
sources:
  - id: lai-guide
    resource: https://lpdaac.usgs.gov/documents/926/MOD15_User_Guide_V61.pdf
    title: "MODIS Collection 6.1 LAI/FPAR Product User's Guide, April 2020, read 2026-09-15: section 4 (the sinusoidal grid tiling system, tiles 10 by 10 degrees at the equator, the tile coordinate system from (0, 0) at the upper left to (35, 17) at the lower right, Table 3 with 2400 by 2400 rows and columns at 500 m, and the metadata notes: the sinusoidal projection has a unique sphere measuring 6371007.181 m, UpperLeftPointMtrs and LowerRightMtrs in projection coordinates are the only metadata that accurately reflect the extreme corners of the gridded image, and BOUNDINGRECTANGLE and GRINGPOINT give the latitude and longitude of the geographic tile)"
  - id: vi-guide
    resource: https://lpdaac.usgs.gov/documents/621/MOD13_User_Guide_V61.pdf
    title: "MODIS Vegetation Index User's Guide, version 3.10, September 2019, read 2026-09-15: section 1.1 (tiles approximately 1200 by 1200 km at the equator in the sinusoidal grid, an equal area projection), section 3 (grid files of 10 by 10 degree extent), Tables 1 and 5 (the integer layers: the indices with fill -3000, the uint16 quality bit field, the int16 day of the year with fill -1, the int8 reliability rank) and the FAQ (tiles are 10 by 10 degrees at the equator but vary according to latitude; the projection is sinusoidal and the MODIS reprojection tool converts it)"
  - id: vi-atbd
    resource: https://lpdaac.usgs.gov/documents/104/MOD13_ATBD.pdf
    title: "MODIS Vegetation Index Algorithm Theoretical Basis Document, version 3, April 1999, read 2026-09-15 for the production section: the integerized sinusoidal grid derived from the sinusoidal projection, split into 36 by 18 tiles of approximately 10 by 10 degrees, 648 tiles of which about 290 hold land, each 1200 by 1200 cells at 1 km or 4800 by 4800 at 250 m, every cell keeping its geolocation through time"
  - id: cmr-q1
    resource: https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=MOD13Q1&version=061
    title: "CMR collection record for MOD13Q1 v061, read 2026-09-15: the spatial extent as the MODIS Sinusoidal Tiling System with a Cartesian coordinate system, a 250 m gridded resolution and a global bounding rectangle"
  - id: mod11
    resource: ../datasets/mod11-land-surface-temperature.md
    title: "This bundle's MOD11 concept, which states from the MOD11 guide that the nominal 1 km cell is 0.928 km on the ground, and describes the 1200 by 1200 tile"
  - id: mod13
    resource: ../datasets/mod13-vegetation-indices.md
    title: "This bundle's MOD13 concept, with the integer layers this gotcha names and the tile geometry"
  - id: mod15
    resource: ../datasets/mod15-lai-fpar.md
    title: "This bundle's MOD15 concept, with the byte layers and the land cover codes above the valid range"
  - id: mod17
    resource: ../datasets/mod17-gpp-npp.md
    title: "This bundle's MOD17 concept, whose per-area carbon layers are the ones an area sum multiplies"
  - id: hls-overlap
    resource: hls-mgrs-tile-overlap.md
    title: "This bundle's HLS gotcha on overlapping UTM tiles, the other tiling trap in this bundle; sinusoidal tiles partition one projection and do not overlap"
---

# Sinusoidal cells are equal-area, not 500 m squares in degrees

**Mechanism.** The MODIS land products, MOD13, MOD15 and MOD17 among
them, are gridded on one projection and one tiling. The guides
describe it: a sinusoidal projection the vegetation index guide calls
equal area, split into 36 by 18 tiles that are 10 by 10 degrees at the
equator and approximately 1200 by 1200 km there, numbered from (0, 0)
at the upper left to (35, 17) at the lower right, 648 tiles of which
about 290 hold land; a tile is 4800 cells on a side at the nominal
250 m, 2400 at 500 m and 1200 at 1 km, and every cell keeps its
geolocation through time.[^vi-guide][^vi-atbd][^lai-guide] The
projection is on a sphere with a unique radius of 6371007.181 m, and
the guide notes what the metadata can and cannot say about a tile's
position: the UpperLeftPointMtrs and LowerRightMtrs fields, in
projection metres, are the only metadata that accurately reflect the
extreme corners of the gridded image, while the BOUNDINGRECTANGLE and
GRINGPOINT fields hold the latitude and longitude of the geographic
tile.[^lai-guide] The vegetation index guide's FAQ says the tiles are
10 by 10 degrees at the equator but vary according to latitude, and
the CMR record describes the extent as a Cartesian coordinate system
on the MODIS sinusoidal tiling system.[^vi-guide][^cmr-q1]

Two consequences follow from those statements by arithmetic, and are
recorded here as derived from them rather than quoted. Ten degrees of
arc on a sphere of radius 6371007.181 m is 1,111,950.5 m; divided
over 2400 columns that is 463.31 m per cell, over 4800 it is 231.66 m
and over 1200 it is 926.63 m, the last within two metres of the 0.928
km this bundle's MOD11 concept quotes from the MOD11 guide for the
nominal 1 km cell.[^lai-guide][^mod11] A 463.31 m square covers
214,660 square metres, 0.2147 square kilometres, where a 500 m square
would cover 0.25, a ratio of 1.165; the 250 m cell covers 0.0537
square kilometres against 0.0625, the same ratio. Because the
projection is equal area, that cell area is the same in every tile at
every latitude, which is the property that makes a pixel count a land
area at all.[^vi-guide] The cells are square in projection metres, not
in degrees: the vegetation index guide's FAQ says the 10 by 10 degree
tiles vary according to latitude, and the LAI guide's metadata note
says the geographic bounding rectangle does not give the gridded
image's corners, so a tile away from the equator is not a rectangle
of degrees and its bounding rectangle is wider than its
footprint.[^lai-guide][^vi-guide]

The layers on this grid are integers with meanings that survive a
copy and not an interpolation: the indices with fill -3000, the
uint16 quality bit field, the int16 composite day of the year with
fill -1 and the int8 reliability rank in MOD13, the bytes with land
cover codes 249 to 255 above the valid range in MOD15, and the int16
and uint16 sums with codes 32761 to 32767 and 65529 to 65535 in MOD17
([this bundle's MOD13, MOD15 and MOD17 concepts](../datasets/mod13-vegetation-indices.md)).[^vi-guide][^mod13][^mod15][^mod17]

**Wrong-result mode.** An area computed as a pixel count times 0.25
square kilometres, or times 0.0625 at 250 m, overstates it by 16.5 per
cent, and a carbon total built from a MOD17 per-area sum times that
area inherits the same factor; the error is silent because the nominal
resolution is in the product name and the collection
description.[^lai-guide][^vi-guide][^mod17] A selection of tiles by a
latitude and longitude box that uses the BOUNDINGRECTANGLE or ring
points selects by the geographic tile the guide says those fields
describe, not by the gridded image's corners, and a subset cut from a
reprojected raster by the same box crosses the tile's skewed edges
diagonally.[^lai-guide] A reprojection to a geographic grid changes the
cell area with latitude, so a count on the output grid is no longer an
area, and a mean over the output grid weights cells by an area that
changes with latitude, which the equal area input did not
have.[^vi-guide] A reprojection with an
interpolating resampler (bilinear, cubic) averages neighbouring
integers: the bit field becomes a number with no bit meaning, the day
of the year becomes a fraction of a day between two dates, the
reliability rank becomes 1.5, a fill of -3000 beside an NDVI of 8000
becomes 2500 and the MOD15 code 253 beside an LAI byte of 30 becomes
an LAI of 14; and a resampler that honours the declared fill masks
only the one code the product page names.[^vi-guide][^mod15] The
opposite of this bundle's HLS trap also holds: sinusoidal tiles do not
overlap, so a mosaic that de-duplicates by geographic overlap, as it
must for the MGRS tiles, is doing work the grid does not need ([the
HLS tile overlap gotcha](hls-mgrs-tile-overlap.md)).[^vi-atbd][^hls-overlap]

**Correct approach.** Areas are computed on the native grid from the
projection metadata, as the number of valid cells times the square of
the cell size read from UpperLeftPointMtrs, LowerRightMtrs and the
column count, and an area-weighted mean of a per-area quantity on the
native grid is an unweighted mean, because the projection is equal
area.[^lai-guide][^vi-guide] Tiles are chosen by the tile grid, the
horizontal and vertical numbers of the file name, and a point is
located by projecting its latitude and longitude onto the sinusoidal
sphere rather than by comparing it with the bounding
rectangle.[^lai-guide] Where a geographic grid is required, the integer
layers are decoded first (the quality bits into masks, the codes into
a class layer, the day of the year kept as an integer) and resampled
by nearest neighbour, the scaled continuous layers are reprojected
with the fill and the codes masked, and any area or count on the
output grid is weighted by the output cell's true area.[^vi-guide][^mod13]

**Verification.** On any MOD13A1, MOD15A2H or MOD17A2H file, the
difference between the LowerRightMtrs and UpperLeftPointMtrs eastings
divided by 2400 is 463.31 m, and the same for the northings; on a
MOD13Q1 file the divisor is 4800 and the result 231.66 m, and the
tile's edge length, 1,111,950 m, is the same for every tile
regardless of latitude.[^lai-guide] The geographic bounding rectangle
of a tile away from the equator, read from the metadata and converted
to an area on the sphere, is larger than 2400 squared times 0.2147
square kilometres, the area the tile's cells add up to, and the
difference grows with latitude, since the guide gives the rectangle as
the geographic tile and not as the gridded image. A reprojected copy of a MOD13 file
made with a bilinear resampler holds values in the day of the year
layer that are not integers, or integers that occur in no source
pixel, and quality values whose bits 8 and 9, always zero in the
source, are set.[^vi-guide]

[^lai-guide]: MODIS Collection 6.1 LAI/FPAR Product User's Guide, April 2020, section 4 and Table 3
[^vi-guide]: MODIS Vegetation Index User's Guide, version 3.10, September 2019, sections 1.1 and 3, Tables 1 and 5 and the FAQ
[^vi-atbd]: MODIS Vegetation Index Algorithm Theoretical Basis Document, version 3, April 1999, the production, projection and tile section
[^cmr-q1]: CMR collection record C1748066515-LPCLOUD, read 2026-09-15
[^mod11]: this bundle's MOD11 concept
[^mod13]: this bundle's MOD13 concept
[^mod15]: this bundle's MOD15 concept
[^mod17]: this bundle's MOD17 concept
[^hls-overlap]: this bundle's HLS MGRS tile overlap gotcha
