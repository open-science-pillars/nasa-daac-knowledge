---
type: dataset-gotcha
spheres: [biosphere, geosphere]
title: "HLS MGRS tiles overlap, each in its own UTM zone: a mosaic or an area sum that concatenates tiles counts the overlap twice"
description: "HLS grids both products into the Sentinel-2 MGRS tiles, 109,800 m squares in the UTM zone of the tile. Adjacent tiles in one zone overlap, by around 8 to 10 km according to the user guide and around 4,900 m according to the project site, and tiles on either side of a zone boundary overlap more and are in different projections. A pixel in the overlap is delivered in two or more granules, so an area total, a pixel count or a cloud-free composite built by concatenating tiles counts it twice, and a mosaic of two zones' tiles in one of their projections resamples one of them."
tags: [hls, hlsl30, hlss30, mgrs, utm, tiling, overlap, mosaic, lpdaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:40:00Z }
severity: medium
dataset: ../datasets/hls-l30.md
status: draft
stale_after: 2027-03-14
sources:
  - id: user-guide
    resource: https://lpdaac.usgs.gov/documents/1698/HLS_User_Guide_V2.pdf
    title: "HLS Product User Guide, product version 2.0, April 2026, read in full 2026-09-14: section 3.5 (the tiling, the 109,800 m tile, the 8 to 10 km overlap within a zone and greater overlap across zones, the negative southern y convention), section 4.3 (reprojection from the neighbouring zone), section 6.1 (the file timestamp is not the tile's sensing time), Table 11 (HORIZONTAL_CS_NAME, ULX, ULY, LANDSAT_PRODUCT_ID and PRODUCT_URI)"
  - id: hls-tiling
    resource: https://hls.gsfc.nasa.gov/products-description/tiling-system/
    title: "HLS project site, Tiling System, read 2026-09-14: 109.8 km tiles, an overlap of around 4,900 m between adjacent tiles within a zone and greater overlap on the zone border, the tile designation explained"
  - id: hls-algorithms
    resource: https://hls.gsfc.nasa.gov/algorithms/
    title: "HLS project site, Algorithms page, read 2026-09-14: spatial co-registration, the 15 m origin shift between Landsat and MGRS and the reprojection of Landsat scenes from an adjacent zone"
  - id: l30-known-issues
    resource: https://lpdaac.usgs.gov/documents/2434/HLS_v2.0_L30_known_issues_April2026.pdf
    title: "HLS L30 v2.0 Known Issues, April 2026, read 2026-09-14: issues 9 and 10 (projection metadata labels every tile northern, the angle layers carry a false northing of ten million), issue 14 (duplicate granules from reprocessed input), issue 16 (two overpasses gridded into one tile above 80 degrees north)"
  - id: s30-known-issues
    resource: https://lpdaac.usgs.gov/documents/2435/HLS_v2.0_S30_known_issues_April2026.pdf
    title: "HLS S30 V2.0 Known Issues, April 2026, read 2026-09-14: issue 4 (a cloud mask boundary that follows the tile boundary in a mosaic) and issue 8 (projection metadata)"
  - id: l30
    resource: ../datasets/hls-l30.md
    title: "This bundle's HLS L30 concept"
  - id: s30
    resource: ../datasets/hls-s30.md
    title: "This bundle's HLS S30 concept"
---

# HLS MGRS tiles overlap, each in its own UTM zone

**Mechanism.** HLS adopts the tiling ESA uses for Sentinel-2: UTM
projection, tiles 109,800 m on a side (110 km nominally), aligned
with the Military Grid Reference System, so that tile 11SPC is in UTM
zone 11, latitude band S, column P and row C of the 6 by 8 degree
grid zone.[^user-guide] Both products, from Landsat scenes on their
own WRS-2 path and row grid and from Sentinel-2 granules, are gridded
into the same tiles, which is what makes the two stackable.[^user-guide][^l30][^s30]

The tiles are not a partition. The guide says adjacent tiles in the
same UTM zone overlap horizontally and vertically by around 8 to 10
km, and that two adjacent tiles from neighbouring UTM zones may
overlap much more; the project site's tiling page says the overlap
within a zone is around 4,900 m and greater on the zone border. The
two project documents disagree on the within-zone figure and this
concept quotes both; either way the overlap is many 30 m
pixels.[^user-guide][^hls-tiling] Each tile is in its own zone's
projection, so the two tiles that share a zone border hold the same
ground in two coordinate systems, and a Landsat scene whose zone is
the neighbouring one is reprojected before it is gridded, which is
why the metadata field HORIZONTAL_CS_NAME on an L30 granule can name
a zone other than the tile's.[^user-guide][^hls-algorithms]

Three smaller facts sit with this one. HLS keeps the southern
hemisphere y coordinate negative (a false northing of zero) where
other providers add ten million metres, and the projection metadata
in the files labels every tile as northern, so a tool that trusts the
EPSG code it reads places a southern tile wrongly and the L30 angle
layers really do carry the ten million metre false northing while
their metadata says zero.[^user-guide][^l30-known-issues] The UTC
timestamp in a file name is the input scene's time (L30) or the
orbit's start of sensing (S30), not the tile's, so two granules of one
tile on one day can be the same overpass with different timestamps,
and the L30 archive holds duplicates whose names differ by a fraction
of a second after a USGS reprocessing.[^user-guide][^l30-known-issues]
And above 80 degrees north, two consecutive Landsat overpasses can be
gridded into one tile.[^l30-known-issues]

**Wrong-result mode.** A regional total built by summing per-tile
results, burned area, water area, cloud-free pixel count, crop area by
class, counts every pixel in an overlap strip once per tile that
holds it; with an overlap of several kilometres on each side of a
tile, the strip is a substantial share of the tile, and the excess
scales with the number of tile boundaries the region crosses, not
with anything on the ground. A mosaic assembled by pasting tiles in
one projection carries seams where the pasted tile came from the
other zone and was resampled, and a cloud mask boundary that follows
the tile boundary in a mosaic is the sign of a masking error in one
of the granules.[^s30-known-issues] A per-date composite that treats
each granule as one observation double-weights the overlap in a
median, and counts a Landsat duplicate pair as two clear
observations.[^l30-known-issues] None of this errors: every granule
is valid on its own.

**Correct approach.** A region is defined once, in one coordinate
system, and each pixel of the region is assigned to exactly one
granule per date before anything is summed; where two granules of
one date cover a pixel, one is chosen by rule (the tile whose zone
matches the region's projection, or the tile in which the pixel is
farther from the edge) and the choice is recorded. Tiles from
different zones are reprojected to the region's system once, with the
resampling named. Granules of one tile and date are deduplicated by
the input scene identifier in the metadata (LANDSAT_PRODUCT_ID, or
PRODUCT_URI on S30) rather than by the file timestamp.[^user-guide]
Southern-hemisphere tiles are positioned by the negative y in the
data, not by the hemisphere in the EPSG code the file
reports.[^l30-known-issues]

**Verification.** The upper-left coordinates ULX and ULY of two
adjacent tiles in one zone, from their metadata, differ by less than
109,800 m, and the difference is the tile spacing; the extent of each
tile, 109,800 m divided by 30 m or 3660 pixels, exceeds that spacing
by the overlap. A
pixel count over a region computed from a dissolved tile footprint
and from a concatenation of tiles differ by the overlap area, and the
first agrees with the region's area at 30 m.[^user-guide]

[^user-guide]: HLS Product User Guide, product version 2.0, April 2026, sections 3.5, 4.3, 6.1 and Table 11
[^hls-tiling]: HLS project site, Tiling System page
[^hls-algorithms]: HLS project site, Algorithms page, Spatial Co-registration
[^l30-known-issues]: HLS L30 v2.0 Known Issues, April 2026, issues 9, 10, 14 and 16
[^s30-known-issues]: HLS S30 V2.0 Known Issues, April 2026, issues 4 and 8
[^l30]: this bundle's HLS L30 concept
[^s30]: this bundle's HLS S30 concept
