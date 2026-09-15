---
type: dataset-gotcha
spheres: [biosphere, geosphere]
title: "NDVI and EVI are empirical indices of red and near-infrared contrast, not measures of leaf area, biomass or green cover: NDVI compresses toward a ceiling over dense canopy, EVI is a different quantity with its own coefficients and a two-band fallback, and a difference or ratio of index values is not a proportional difference in vegetation"
description: "The MOD13 NDVI is a non-linear stretch of the near-infrared to red ratio that confines its values to -1 to 1: as the ratio rises from 5 to 10 to 15 to 20 the NDVI moves from 0.67 to 0.82 to 0.87 to 0.90, so the index becomes insensitive to leaf area above about 2 or 3, is most sensitive to the soil, litter or snow background at intermediate cover, and varies with leaf angle and clumping for the same leaf area. EVI is a separate formula with a blue-band aerosol term and a canopy background adjustment, replaced by a two-band form wherever the blue reflectance is high, and no quality bit says which form produced a pixel. A script that reads a 20 per cent rise in NDVI as 20 per cent more vegetation, that treats a flat NDVI over rainforest as an unchanged canopy, that regresses biomass or leaf area on the index with one relation across cover types, or that uses NDVI and EVI interchangeably reports a property of the index as a property of the land, and nothing raises an error because every value lies in the valid range."
tags: [mod13, mod13q1, mod13a1, modis, ndvi, evi, saturation, vegetation-index, leaf-area-index, biomass, lpdaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T17:50:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-15T18:34:53Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/172 }
severity: high
dataset: ../datasets/mod13-vegetation-indices.md
eval_case: index-is-not-a-state-variable
status: draft
stale_after: 2027-03-15
sources:
  - id: vi-atbd
    resource: https://lpdaac.usgs.gov/documents/104/MOD13_ATBD.pdf
    title: "MODIS Vegetation Index (MOD 13) Algorithm Theoretical Basis Document, version 3, April 30 1999 (Huete, Justice and van Leeuwen), read 2026-09-15: section 2.2.3 (saturation as an influence inherent to canopies, and the dependence of NDVI on canopy structure for a given LAI, cover or biomass), 2.2.7 (background sensitivity greatest at intermediate cover, 0.30 NDVI units at LAI 1 for background red reflectance from 0.06 to 0.33, disappearing above LAI 2), 2.2.8 (the NDVI saturation considerations with the ratio to NDVI table and the insensitivity to LAI above 2 or 3), 2.2.9 (leaf angle, clumping and dead material alter the NDVI to LAI relation; it is very difficult to derive biophysical plant parameters directly from the VI) and the opening of section 3 (vegetation indices are empirical measures of vegetation activity)"
  - id: vi-guide
    resource: https://lpdaac.usgs.gov/documents/621/MOD13_User_Guide_V61.pdf
    title: "MODIS Vegetation Index User's Guide, version 3.10, September 2019, read 2026-09-15: section 1.2 (indices as integrative functions of canopy structure and physiology; the NDVI ratio's non-linear asymptotic behaviour; the EVI equation with L 1, C1 6, C2 7.5 and G 2.5; the two-band EVI over bright targets where the blue reflectance is at or above 0.2, with the note that three-band values usually stay within -1 to 1 so the problem goes undetected), Table 1 (the valid range -2000 to 10000 and fill -3000), Table 5 (the quality bit field, which carries no field for the EVI formula used) and the FAQ (EVI superior at high vegetation density where NDVI tends to saturate)"
  - id: lai-guide
    resource: https://lpdaac.usgs.gov/documents/926/MOD15_User_Guide_V61.pdf
    title: "MODIS Collection 6.1 LAI/FPAR Product User's Guide, April 2020, read 2026-09-15: section 3 (in dense canopies the reflectances saturate and are weakly sensitive to canopy properties; such retrievals are flagged; the backup algorithm uses empirical relationships between NDVI and LAI and FPAR) and Table 5 (SCF_QC 001, main method used with saturation)"
  - id: gpp-guide
    resource: https://lpdaac.usgs.gov/documents/972/MOD17_User_Guide_V61.pdf
    title: "MOD17 User's Guide for Collection 6.1, March 2021, read 2026-09-15 for section 1.3.4: when LAI is greater than 3.0 surface reflectance has low sensitivity to LAI and the MODIS LAI is retrieved in most cases under reflectance saturation, so annual maximum LAI is set to 6.8 for forest pixels"
  - id: q1-page
    resource: https://lpdaac.usgs.gov/products/mod13q1v061/
    title: "LP DAAC product page for MOD13Q1 v061, read 2026-09-15: the variables table with NDVI and EVI as int16, valid range -2000 to 10000, fill -3000, scale 0.0001, and the red, NIR and blue reflectance layers"
  - id: mod13
    resource: ../datasets/mod13-vegetation-indices.md
    title: "This bundle's MOD13 concept, with the index equations, the layer table and the quality fields"
  - id: mod15
    resource: ../datasets/mod15-lai-fpar.md
    title: "This bundle's MOD15 concept, the retrieved leaf area index and FPAR with their standard deviation layers and algorithm path flag"
---

# NDVI and EVI are indices, not state variables

**Mechanism.** The MOD13 products carry two numbers per pixel that
look like measurements of vegetation and are not. The algorithm
document defines them in its first sentence on the algorithm:
vegetation indices are empirical measures of vegetation activity,
combinations of the red and near-infrared reflectances designed to
enhance the vegetation signal, and the guide calls them integrative
functions of canopy structure (cover, leaf area, leaf angle
distribution) and physiology (pigments, photosynthesis) at
once.[^vi-atbd][^vi-guide] NDVI is (NIR minus red) over (NIR plus red),
a normalized transform of the NIR to red ratio that confines the
result to -1 to 1, and the algorithm document spells out what the
transform does to sensitivity: as the ratio rises from 5 to 10 the
NDVI moves from 0.67 to 0.82, at 15 it is 0.87, and at 20 it is 0.90,
so the stretch enhances low values and compresses high ones, leaving
very low sensitivity to spatial and temporal variation in densely
vegetated areas; the NDVI has been reported insensitive to leaf area
index above 2 or 3, partly because the red band's chlorophyll
absorption itself saturates, and the MODIS red band, narrower than
AVHRR's, may saturate more quickly.[^vi-atbd] Below that ceiling the
index is not a function of the canopy alone: the background sensitivity
is greatest at intermediate cover, where the NDVI varies by 0.30 units
at a leaf area index of 1 for background red reflectances from 0.06 to
0.33, and only disappears above a leaf area index of 2, where
saturation begins; and for a given leaf area, cover or biomass the
NDVI varies with leaf angle distribution, clumping and the share of
woody, senescent and dead material, so the same leaf area in smaller
cover fractions yields the lowest NDVI and a more planophile canopy a
higher one.[^vi-atbd] The document's conclusion is that it is very
difficult to derive biophysical plant parameters directly from the
index, and that the relations that exist are site specific
regressions subject to background, atmosphere, calibration and sun
and view angle.[^vi-atbd]

EVI is not a corrected NDVI but a different quantity: (NIR minus red)
over (NIR plus 6 times red minus 7.5 times blue plus 1), times 2.5,
with the blue term resisting aerosol and the constant adjusting for
the canopy background; the guide's own FAQ says it is superior at high
vegetation density where NDVI tends to saturate.[^vi-guide] Over
bright targets, where the blue reflectance is at or above about 0.2
(snow, ice, cloud, heavy aerosol, and the guide names sub-pixel cloud
and snow under the canopy), the three-band EVI produces extreme
values, so the product substitutes a two-band EVI, 2.5 times (NIR
minus red) over (NIR plus 2.4 times red plus 1); because the
three-band values usually stay inside -1 to 1 the guide says these
problems are usually undetected, and the quality bit field of Table 5
carries no field that says which formula produced a pixel.[^vi-guide]
Both indices are stored as int16 with valid range -2000 to 10000 and
fill -3000, all inside the type, so any value reads as a
number.[^q1-page][^vi-guide]

The products that do carry a state variable say the same thing from
the other side. The MOD15 leaf area index is retrieved by inverting a
radiative transfer model, and its guide states that in dense canopies
the reflectances saturate and are weakly sensitive to canopy
properties, so those retrievals are flagged (SCF_QC 001) and their
dispersion is large; its backup path is exactly the empirical NDVI to
LAI relation.[^lai-guide] The MOD17 guide says reflectance has low
sensitivity to leaf area above 3, that the MODIS LAI is mostly
retrieved under saturation there, and that forest annual maximum LAI
is set to 6.8 for that reason ([this bundle's MOD15
concept](../datasets/mod15-lai-fpar.md)).[^gpp-guide][^mod15]

**Wrong-result mode.** A script that treats the index as a linear
measure of vegetation reports a property of the transform as a
property of the land. A rise in NDVI from 0.67 to 0.82, about 22 per
cent, corresponds to a doubling of the NIR to red ratio, and the same
doubling from 10 to 20 moves the NDVI by about 0.09 (0.08 on the
document's rounded values); a relative change
computed on the index is therefore not comparable between a sparse
and a dense pixel, and a ratio of two NDVI values is not a ratio of
anything physical.[^vi-atbd] A trend fitted over evergreen broadleaf
forest that comes out flat is read as an unchanged canopy when the
index is above its sensitive range and a change in leaf area from 4
to 6 would not show; the same flat series in the MOD15 LAI would at
least carry the saturation flag.[^vi-atbd][^lai-guide] A regression
of biomass, leaf area or cover on NDVI built at one site and applied
across a tile mixes canopy structures, backgrounds and seasons for
which the relation differs, and the intermediate-cover pixels where
the fit looks best are the ones whose index moved by 0.30 with the
background alone.[^vi-atbd] A model or comparison that uses NDVI in
one period and EVI in another, or that averages the two, or that
substitutes one for the other because both are "vegetation indices",
attributes their formula difference to vegetation, and over snow,
cloud edges and heavy aerosol the EVI it averages is a two-band
quantity with no flag.[^vi-guide] A phenology or greenness fraction
read directly off the index, without the empirical calibration the
algorithm document calls site specific, inherits the leaf angle and
clumping dependence as if it were a change in greenness.[^vi-atbd]
None of this raises an error: every input is inside the valid range,
the fill -3000 scales to a plausible -0.3, and the index looks like a
fraction.[^vi-guide][^q1-page]

**Correct approach.** The index is used as an index: a relative,
ordinal measure of vegetation activity, compared with itself over
time within a cover type and season, with NDVI read as saturating above
a leaf area index of about 2 to 3 and EVI preferred where the canopy
is dense, and each index kept separate from the other in any series
or comparison.[^vi-atbd][^vi-guide] Where a state variable is needed,
the retrieved one is used: MOD15 leaf area index and FPAR, which carry
a per-pixel standard deviation and an algorithm path flag that says
whether the main inversion, the saturated inversion or the NDVI
backup produced the value, so a saturated forest canopy is at least
labelled as such.[^lai-guide][^mod15] A biophysical relation applied to
the index is stated with the cover type, site, season and background
it was calibrated for, and the pixels it is applied to are screened
by the pixel reliability rank, the aerosol bits and the snow and
shadow bits of the MOD13 quality layer, because those are the
conditions the algorithm document names as changing the index
independently of the vegetation.[^vi-atbd][^vi-guide][^mod13]

**Verification.** On a tile that holds both products, a scatter of
MOD13A1 NDVI against MOD15A2H LAI for the same period flattens above
a leaf area index of about 2 to 3 while the EVI keeps some slope, and
the NDVI spread at a leaf area index near 1 is of the order of the
0.30 units the algorithm document gives for the background
range.[^vi-atbd] A scatter of NDVI against EVI on the same tile is not
a line, and over snow or bright cloud edges the EVI values sit on a
different relation, the two-band one.[^vi-guide] Recomputing the ratio
from the red and NIR reflectance layers of the file reproduces the
algorithm document's table: pixels with a ratio of 10 have NDVI near
0.82 and pixels with a ratio of 20 near 0.90, an interval of about
0.09 for a doubling (0.08 on the document's rounded
values).[^vi-atbd][^q1-page]

[^vi-atbd]: MODIS Vegetation Index Algorithm Theoretical Basis Document, version 3, April 1999, sections 2.2.3, 2.2.7, 2.2.8, 2.2.9 and 3
[^vi-guide]: MODIS Vegetation Index User's Guide, version 3.10, September 2019, section 1.2, Tables 1 and 5 and the FAQ
[^lai-guide]: MODIS Collection 6.1 LAI/FPAR Product User's Guide, April 2020, section 3 and Table 5
[^gpp-guide]: MOD17 User's Guide for Collection 6.1, March 2021, section 1.3.4
[^q1-page]: LP DAAC product page, MOD13Q1 v061, read 2026-09-15
[^mod13]: this bundle's MOD13 concept
[^mod15]: this bundle's MOD15 concept
