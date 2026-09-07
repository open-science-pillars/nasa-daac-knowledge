---
type: dataset
title: "OPERA DSWx-HLS: surface water extent from optical imagery, with cloud as the dominant class"
description: "Dynamic Surface Water Extent from Harmonized Landsat Sentinel-2, 30 m, ten GeoTIFF layers per granule on MGRS tiles. The water layer carries three water classes (not water, open water, partial surface water) plus snow, cloud, ocean and fill, and over a mountain scene in spring the cloud class routinely dominates: a March 2023 tile over the southern Sierra is 57 per cent cloud and 41 per cent fill. Granules are reprocessed, so an acquisition from 2023 can carry a 2026 production date."
tags: [opera, dswx, hls, surface-water, flood, optical, podaac]
generated: { by: claude-code/fable-5, at: 2026-09-07T20:00:00Z }
resource: https://podaac.jpl.nasa.gov/dataset/OPERA_L3_DSWX-HLS_V1
version: "Product version 1.0 in CMR (collection C2617126679-POCLOUD); the specification read here is v1.0.1, JPL D-107395 Rev B of 2024-07-10, and observed granules carry the v1.1 suffix in their filenames"
status: draft
stale_after: 2027-03-07
citation:
  access_date_required: true
  authority: https://podaac.jpl.nasa.gov/
  data: "OPERA (2023). OPERA Dynamic Surface Water Extent from Harmonized Landsat Sentinel-2 product (Version 1). NASA Physical Oceanography Distributed Active Archive Center, accessed {access_date}, 10.5067/OPDSW-PL3V1"
  doi: "10.5067/OPDSW-PL3V1"
  note: "the access date matters twice over: the archive is reprocessed, so a granule's production date can be years after its acquisition, and a receipt records both"
sources:
  - id: spec
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/opera/OPERA_DSWx-HLS_ProductSpec_v1.0.0_D-107395_RevB.pdf
    title: "OPERA DSWx-HLS Product Specification v1.0.1, JPL D-107395 Rev B, 2024-07-10: Table 4-1, the ten raster layers and the water classification classes verbatim"
  - id: atbd
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/opera/atbd/DSWx-HLS_ATBD_V1_4_DAAC_Distribution.pdf
    title: "OPERA DSWx-HLS Algorithm Theoretical Basis Document V1.4: how the diagnostic layer becomes the interpreted classification"
  - id: cmr
    resource: https://cmr.earthdata.nasa.gov/search/collections.umm_json?concept_id=C2617126679-POCLOUD
    title: "CMR collection record for OPERA_L3_DSWX-HLS_V1 (DOI, temporal extent, documentation links), read 2026-09-07"
  - id: record
    resource: https://github.com/open-science-pillars/marketplace/issues/72
    title: "The event reconstruction record: the granule counts over the Tulare box, the layers of one granule, and the class census of its water layer"
---

# OPERA DSWx-HLS

**Identity.** Dynamic Surface Water Extent derived from Harmonized
Landsat Sentinel-2 surface reflectance: collection
`OPERA_L3_DSWX-HLS_V1` (C2617126679-POCLOUD, DOI
10.5067/OPDSW-PL3V1), 30 m, on MGRS tiles of 3660 by 3660 pixels in
the tile's UTM zone. The record runs from 2016-01-01 to the
present.[^cmr]

## Ten layers, one classification

A granule is ten cloud-optimized GeoTIFFs, named by band suffix:
`B01_WTR` (the interpreted water classification), `B02_BWTR` (binary
water, the union of the water classes), `B03_CONF` (confidence),
`B04_DIAG` (the diagnostic layer the interpretation derives from),
`B05_WTR-1` and `B06_WTR-2` (intermediate interpretations),
`B07_LAND`, `B08_SHAD`, `B09_CLOUD` and `B10_DEM`.[^spec][^record]

**The water classification, verbatim from the specification's Table
4-1:**[^spec]

| Value | Class |
|---|---|
| 0 | Not water: valid reflectance that is not class 1, 2, 252, 253 or 254; masking can produce this where land cover masking is applied |
| 1 | Open water: entirely water and unobstructed to the sensor |
| 2 | Partial surface water: inundated, at least 20 per cent and less than 100 per cent open water, such as wetlands, water bodies with emergent vegetation, and pixels bisected by coastlines |
| 252 | Snow/ice, from the input HLS Fmask quality assurance data |
| 253 | Cloud, cloud shadow, or adjacent to cloud or cloud shadow, from the same Fmask data |
| 254 | Ocean masked, using a shoreline database with an added margin |
| 255 | Fill value (no data) |

Note that the classes are not a severity ordering and the high values
are not "worse water": 252, 253 and 254 are statements about what the
sensor could not see, and 0 can itself be the result of masking.

## The cloud class is usually the largest one

Measured over the Tulare Lake bed on 2026-09-07, in the granule
`OPERA_L3_DSWx-HLS_T10SGE_20230320T184011Z_20260317T233817Z_L8_30_v1.1`
(acquired 2023-03-20, at the height of the reflood):[^record]

| Class | Pixels | Share of the tile |
|---|---|---|
| 0 not water | 151,948 | 1.13 per cent |
| 1 open water | 1,222 | 0.01 per cent |
| 2 partial surface water | 6,632 | 0.05 per cent |
| 253 cloud and adjacent | 7,694,305 | 57.44 per cent |
| 255 fill | 5,541,493 | 41.37 per cent |

One per cent of that scene is classified at all. An area timeline
built from scenes like this one has a denominator that moves from date
to date, and a series of water areas without the valid fraction beside
each one is not a series: it is a record of when the sky was clear.
Every area this product yields is quoted with the valid fraction of
the region on that date.

## The archive is reprocessed

That granule was acquired 2023-03-20 and **produced 2026-03-17**, and
another over the same box carries an acquisition of 2023-03-02 with a
production date of 2026-04-03.[^record] So a timeline built today from
this archive may not reproduce one built last year from the same
acquisitions. A receipt records the granule identifier, which carries
both dates, and not merely the acquisition date.

## Access

Cloud-hosted at PO.DAAC behind Earthdata Login, searchable in CMR by
collection concept id and bounding box; the per-layer COGs are
individual `GET DATA` URLs on the granule, so a workflow that needs
only the water classification fetches one file of about 120 kB rather
than the whole granule.

## Known issues

- The cloud class dominates optical scenes in wet seasons, which is
  when floods happen.
- Class 2 is a genuine third state and not a rounding of class 1; a
  binary reading has to say which side it put class 2 on, and the
  `B02_BWTR` layer makes that choice by unioning them.
- The sibling radar product does not share this class vocabulary, and
  the two cannot be concatenated
  ([the class mismatch gotcha](../gotchas/dswx-class-mismatch.md)).

[^spec]: OPERA DSWx-HLS Product Specification v1.0.1, D-107395 Rev B
[^atbd]: OPERA DSWx-HLS ATBD V1.4
[^cmr]: CMR collection record, read 2026-09-07
[^record]: the event reconstruction record, open-science-pillars/marketplace issue 72
