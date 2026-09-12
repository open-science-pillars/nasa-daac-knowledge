---
type: dataset-gotcha
spheres: [hydrosphere]
title: "The two DSWx products collide on the same integers: an area timeline that spans them measures the product change"
description: "DSWx-HLS and DSWx-S1 share a name, a grid and a layer called WTR, and carve the world differently. Class 2 is partial surface water in the optical product and unused in the radar one; class 3 is inundated vegetation in the radar product and unused in the optical one. Above the data range they collide outright: 252 and 253 are snow and cloud in the optical product while 250 and 251 are HAND and layover masks in the radar one. A timeline that unions the water classes across the two measures the changeover, and nothing raises an error."
tags: [opera, dswx, hls, sentinel-1, surface-water, flood, class-table, timeline]
generated: { by: claude-code/fable-5, at: 2026-09-07T20:10:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-08T04:19:56Z }
severity: high
dataset: ../datasets/opera-dswx-hls.md
eval_case: dswx-class-mismatch
status: stable
stale_after: 2027-03-07
sources:
  - id: hls-spec
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/opera/OPERA_DSWx-HLS_ProductSpec_v1.0.0_D-107395_RevB.pdf
    title: "OPERA DSWx-HLS Product Specification v1.0.1, D-107395 Rev B, Table 4-1: the optical product's classes"
  - id: s1-spec
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/opera/D-108761_OPERA_DSWx_S1AB_ProductSpec_Rev_A.pdf
    title: "OPERA DSWx-S1 Product Specification Rev A, D-108761: the radar product's classes"
  - id: hls
    resource: ../datasets/opera-dswx-hls.md
    title: "This bundle's DSWx-HLS concept, with the class table and the measured cloud share"
  - id: s1
    resource: ../datasets/opera-dswx-s1.md
    title: "This bundle's DSWx-S1 concept, with the class table and the 2023-12-01 archive start"
  - id: record
    resource: https://github.com/open-science-pillars/marketplace/issues/72
    title: "The event reconstruction record: both class tables read from the specifications, side by side"
---

# The two DSWx products collide on the same integers

**Mechanism.** The two products share a family name, a 30 m MGRS grid,
a layer called `WTR` and a data type of uint8. They do not share a
class vocabulary, and the differences are not labelled anywhere in the
data:

| Value | DSWx-HLS | DSWx-S1 |
|---|---|---|
| 0 | not water | not water |
| 1 | open water | open water |
| 2 | **partial surface water** | not used |
| 3 | not used | **inundated vegetation** |
| 250 | not used | **HAND masked** |
| 251 | not used | **layover or shadow masked** |
| 252 | **snow and ice** | not used |
| 253 | **cloud and adjacent** | not used |
| 254 | **ocean masked** | not used |
| 255 | fill | fill |

Two failures follow, and the second is the dangerous one.

**The water classes are different phenomena.** Partial surface water
is an optical judgement about an inundated pixel between 20 and 100
per cent open water. Inundated vegetation is a radar judgement from the dual
polarization ratio and a wetland land-cover class. They overlap in the
world and are not the same measurement, so a timeline that unions "the
water classes" in each product is not measuring one quantity.

**The mask values collide.** A reader who knows the optical table and
meets a radar granule reads 250 and 251 as unused and may treat them
as data; a reader who knows the radar table and meets an optical
granule reads 252 and 253 as unused in the same way. Nothing in either
file objects, because both are valid uint8 and both products document
their own table only.

**Wrong-result mode.** An inundation area timeline that runs across
the changeover date shows a step. If the step is at the changeover it
will be read as a flood receding or a new flood beginning, because
that is what a step in an area timeline means to a reader. Over a
vegetated floodplain the radar product's inundated vegetation class
can add area the optical product never had, and over a cloudy scene
the optical product's cloud class removes area the radar product never
loses, so the step can go either way and its sign carries no
information about water.

**Correct approach.** One product per timeline, stated in the receipt
with its class table. Where a timeline must span the changeover, write
the crosswalk explicitly: name which classes are being summed on each
side, show the discontinuity at the changeover date rather than
smoothing it, and quote the two series separately as well as joined.
Where a single number is wanted for a region and date, say which
product produced it. And carry the valid fraction with every area from
the optical product, because its cloud class routinely dominates.

**Verification.** Take an area over a floodplain and compute the
water area from each product for a date when both exist, using each
product's own table; the two numbers differ, and the difference is not
an error to reconcile but the two definitions. Then compute a timeline
across the changeover with a single class list and confirm the step
appears where the product changes rather than where the water does.

[^hls-spec]: OPERA DSWx-HLS Product Specification v1.0.1
[^s1-spec]: OPERA DSWx-S1 Product Specification Rev A
[^record]: the event reconstruction record, open-science-pillars/marketplace issue 72
