---
type: dataset
spheres: [hydrosphere]
title: "OPERA DSWx-S1: surface water extent from radar, which sees through cloud and did not exist before December 2023"
description: "Dynamic Surface Water Extent from Sentinel-1, 30 m on MGRS tiles. The water layer carries not water, open water and inundated vegetation, with HAND and layover or shadow masks; there is no cloud class because radar does not need one. The archive begins 2023-12-01, so the product an analyst reaches for during a cloudy flood is absent from every event before that date."
tags: [opera, dswx, sentinel-1, radar, surface-water, flood, podaac]
generated: { by: claude-code/fable-5, at: 2026-09-07T20:05:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-08T04:19:56Z }
resource: https://podaac.jpl.nasa.gov/dataset/OPERA_L3_DSWX-S1_V1
version: "Product version 1.0 in CMR (collection C2949811996-POCLOUD); the specification read here is Rev A, JPL D-108761"
status: stable
stale_after: 2027-03-07
citation:
  access_date_required: true
  authority: https://podaac.jpl.nasa.gov/
  data: "OPERA (2024). OPERA Dynamic Surface Water Extent from Sentinel-1 product (Version 1). NASA Physical Oceanography Distributed Active Archive Center, accessed {access_date}, 10.5067/OPDSWS1-L3V1"
  doi: "10.5067/OPDSWS1-L3V1"
sources:
  - id: spec
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/opera/D-108761_OPERA_DSWx_S1AB_ProductSpec_Rev_A.pdf
    title: "OPERA DSWx-S1 Product Specification Rev A, JPL D-108761: the raster layers and the water classification classes verbatim"
  - id: atbd
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/opera/atbd/D-108763_Rev_A_OPERA_DSWx_S1_NI_ATBD_20240530_SIGNED.pdf
    title: "OPERA DSWx-S1 and NI Algorithm Theoretical Basis Document, Rev A, 2024-05-30"
  - id: cmr
    resource: https://cmr.earthdata.nasa.gov/search/collections.umm_json?concept_id=C2949811996-POCLOUD
    title: "CMR collection record for OPERA_L3_DSWX-S1_V1 (DOI, temporal extent beginning 2023-12-01), read 2026-09-07"
  - id: record
    resource: https://github.com/open-science-pillars/marketplace/issues/72
    title: "The event reconstruction record: the query showing zero granules over the Tulare box during the 2023 flood"
---

# OPERA DSWx-S1

**Identity.** Dynamic Surface Water Extent derived from Sentinel-1
radiometric terrain corrected backscatter: collection
`OPERA_L3_DSWX-S1_V1` (C2949811996-POCLOUD, DOI
10.5067/OPDSWS1-L3V1), 30 m, on the same MGRS tiling as its optical
sibling.[^cmr]

## The classification, verbatim from the specification

| Value | Class |
|---|---|
| 0 | Not water: valid data that is not class 1, 3, 250 or 251; masking can produce this where land cover masking is applied |
| 1 | Open water: entirely water and unobstructed to the sensor |
| 3 | Inundated vegetation: extracted from the high value in the dual polarization ratio and the wetland class in the land cover map |
| 250 | Height Above Nearest Drainage (HAND) masked: topographic height above the HAND threshold |
| 251 | Layover or shadow masked: computed from the geometry of the digital elevation model and the sensor, copied from the input burst products |
| 255 | Fill value (no data) |

**There is no cloud class and no snow class, because radar does not
need them.** That is the product's advantage and the reason an analyst
reaches for it during a flood. It is also why its classes cannot be
lined up against the optical product's
([the class mismatch gotcha](../gotchas/dswx-class-mismatch.md)).

## The archive begins after the floods people want it for

The collection's temporal extent begins **2023-12-01**.[^cmr] Measured
2026-09-07: a search over the Tulare Lake bed (lon -120.4 to -119.3,
lat 35.8 to 36.6) for 2023-03-01 to 2023-07-31, the whole reflood,
returns **zero granules**.[^record]

This is worth stating plainly because the reasoning that leads to the
product is sound and the conclusion is still wrong: the flood was
cloudy, radar sees through cloud, therefore use the radar product. For
any event before December 2023 there is nothing there. An analyst who
searches and finds nothing may conclude the search was wrong rather
than that the archive starts later, so a workflow that offers this
product states its start date beside the offer.

## Access

Cloud-hosted at PO.DAAC behind Earthdata Login, searchable in CMR by
collection concept id and bounding box, with per-layer COGs as
individual URLs on each granule.

## Known issues

- The archive's start date excludes every earlier event.
- The HAND and layover masks remove real terrain rather than
  identifying it as dry: a valley floor below the HAND threshold and a
  slope in layover are both absent from the classification, and an
  area denominator has to account for them.
- The class vocabulary differs from the optical product's on the same
  integers.

[^spec]: OPERA DSWx-S1 Product Specification Rev A, D-108761
[^atbd]: OPERA DSWx-S1 and NI ATBD Rev A, 2024-05-30
[^cmr]: CMR collection record, read 2026-09-07
[^record]: the event reconstruction record, open-science-pillars/marketplace issue 72
