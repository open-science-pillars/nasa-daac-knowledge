---
type: dataset-gotcha
spheres: [geosphere]
title: "NASADEM heights are not all SRTM: the NUM layer says which pixels are ASTER GDEM, ALOS PRISM, an older SRTM edit or interpolation, and only it separates the February 2000 radar heights from the optical fill acquired years later"
description: "The NASADEM_HGT height layer is a merge. Where the reprocessed SRTM has a value the height is SRTM; where it is void the height is an error-suppressed ASTER GDEM3 built from draft GDEM3, GDEM2 and ALOS PRISM AW3D30, shifted vertically by an interpolated delta surface so that the seam does not show, and in the last resort interpolation. The companion NUM layer codes the source per pixel: 1 to 23 an SRTM scene count, 41 to 94 PRISM, 110 to 160 GDEM3, 170 to 220 GDEM2, 231 to 246 older SRTM and national DEM edits carried through the GDEMs, 250 interpolation, 0 water. An analysis that reads every height as February 2000 radar treats optical stereo surfaces from 2000 to 2013 as the same measurement, and nothing in the height layer marks the difference."
tags: [nasadem, nasadem-hgt, num, void-fill, aster-gdem, prism, aw3d30, srtm, dem, lpdaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T13:40:00Z }
severity: medium
dataset: ../datasets/nasadem.md
status: draft
stale_after: 2027-03-15
sources:
  - id: user-guide
    resource: https://lpdaac.usgs.gov/documents/2237/NASADEM_User_Guide_V13.pdf
    title: "NASADEM user guide, version 1.3, January 2025, read 2026-09-15: Table 1 (the hgt, num and swb layers), Table 2 (the NUM index), section 5.1.2 (water masking), 5.1.3 (unwrapping error removal), 5.1.4 (the fill sources, GMTED2010 not used, the mutual dependency of the DEMs), 5.1.5 (the GDEM error mask, the delta surface fill and its remnant voids) and 5.1.6"
  - id: hgt-page
    resource: https://lpdaac.usgs.gov/products/nasadem_hgtv001/
    title: "LP DAAC product page for NASADEM_HGT v001, read 2026-09-15: the NUM layer indicates the number of scenes processed for each pixel and the source of the data; the source of each elevation pixel is also distributed as NASADEM_NUMNC; the layer table with NUM and SWB as uint8 classes"
  - id: dem-guide
    resource: https://lpdaac.usgs.gov/documents/642/DEM_Comparison_Guide.pdf
    title: "LP DAAC DEM Product Comparison Guide, read 2026-09-15: SRTM acquired 2000-02-11 to 2000-02-21 by C-band radar, ASTER GDEM version 3 from scenes acquired 2000-03-01 to 2013-11-30 by an optical stereo sensor whose images can contain cloud, and the fill sources it lists for NASADEM"
  - id: astgtm-guide
    resource: https://lpdaac.usgs.gov/documents/434/ASTGTM_User_Guide_V3.pdf
    title: "ASTER GDEM version 3 user guide, read 2026-09-15 for its own NUM convention: the number of scenes used per pixel, capped at 50, and a fill source index, on a product referenced to the WGS84/EGM96 geoid"
  - id: cmr-numnc
    resource: https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=NASADEM_NUMNC
    title: "CMR collection record for NASADEM_NUMNC v001 (concept C2763264768-LPCLOUD), read 2026-09-15: the merged DEM source layer as its own netCDF-4 collection"
  - id: nasadem
    resource: ../datasets/nasadem.md
    title: "This bundle's NASADEM concept, with the collection table, the processing order and the uncertainty statement"
---

# NASADEM heights are not all SRTM

**Mechanism.** NASADEM_HGT is described by its guide as the void-filled
DEM merge, and the merge has two kinds of member. Where the
reprocessed SRTM strip data unwrapped, the height is the SRTM
interferometric height of February 2000, improved by the new
unwrapping and the ripple correction.[^user-guide][^dem-guide] Where
it did not, the height comes from a void-free, error-suppressed GDEM3
that the project built for the purpose out of three unreleased drafts
of ASTER GDEM3, ASTER GDEM2, the ALOS PRISM AW3D30 DEM and some of the
reprocessed SRTM itself, with GDEM2 as first choice for filling the
draft GDEM3, SRTM second and PRISM third; GMTED2010 and other DEMs
were not used.[^user-guide] The ASTER inputs are optical stereo
surfaces from scenes acquired between March 2000 and November 2013,
an instrument that sees cloud where radar does not, and the GDEM
error mask exists to remove those clouds: a pixel was rejected when
it differed by more than 80 m from both SRTM and PRISM AW3D30, or
from its neighbours by more than 100 m, with the mask grown to fill
enclosed areas.[^dem-guide][^user-guide] The fill is a modified delta
surface fill: the difference between the primary and the filler DEM
is computed where both exist, median filtered near voids, interpolated
across the void from its edges by an inverse square root of distance
rule in sixteen directions, and added to the filler inside the void,
so that the seam is smooth by construction. The guide's own caution is
that a fill adjusted this way may look smoother but be less correct
in terms of actual elevations.[^user-guide] Where no filler had data,
the height is interpolation.[^user-guide]

The height layer carries none of this. The record of the source is
the NUM layer of the same granule, a byte per pixel that the product
page describes as the number of scenes processed for each pixel and
the source of the data, and that the guide's Table 2 decodes:[^hgt-page][^user-guide]

| NUM value | Source |
|---|---|
| 0 | water in the corrected SRTM water body data |
| 1 to 23 | SRTM, the value being the number of SRTM scenes (23 is the largest known) |
| 41 to 94 | PRISM AW3D30, the value minus 40 being its scene count (up to 54 in polar areas, 37 elsewhere) |
| 110 to 160 | GDEM3, count saturated at 50 |
| 170 to 220 | GDEM2, count saturated at 50 |
| 231, 232, 233, 234 | SRTM version 3 or version 2, or SRTM with the NGA fill, as carried inside GDEM3 or GDEM2 |
| 241, 242 | the USGS National Elevation Dataset, through GDEM2 or GDEM3 (United States) |
| 243, 244 | the Canadian Digital Elevation Data, through GDEM2 or GDEM3 |
| 245, 246 | Alaska DEM, through GDEM2 or GDEM3 |
| 250 | interpolation |
| 251 | quad edge averaged where two neighbouring quads disagreed, generally a GDEM error |
| 255 | error (NUM missing; none known) |

The count and the source share one byte, so a value is a scene count
only inside its band: 12 is twelve SRTM scenes, 52 is twelve PRISM
scenes, and 122 is twelve GDEM3 scenes.[^user-guide] The same layer
is distributed on its own in netCDF-4 as NASADEM_NUMNC.[^hgt-page][^cmr-numnc]
The ASTER GDEM's own NUM layer follows a different convention, a
scene count capped at 50 plus a fill index, so a decoder written for
one does not read the other.[^astgtm-guide] The water mask is the
third layer, swb, 0 for land and 255 for water, and over water the
height is an edited value rather than a measurement: oceans are set to
zero, lakes are flattened, river segments were adjusted to their new
shores, and land pixels touching water were raised to the water height
plus one metre if lower.[^user-guide]

**Wrong-result mode.** An analysis that treats every pixel of hgt as
the SRTM radar height of February 2000 mixes measurements. A slope,
roughness or drainage derivation crosses from a radar phase centre
height into an optical stereo surface shifted by an interpolated
delta, and the transition is smooth by design, so no artefact flags
it. A change detection that differences NASADEM against SRTM version
3, or against a later DEM, reads the switch of source as a change in
the terrain: inside a former SRTM void the "change" is the difference
between two instruments and up to thirteen years of acquisition dates,
not an event. A vertical accuracy statement quoted from the SRTM
mission figures, which this bundle's NASADEM concept carries, is
applied to pixels whose height never came from SRTM.[^nasadem] A NUM
value read as a plain scene count makes a PRISM or GDEM pixel look
like a well-observed SRTM one. Over water, a mean or a slope includes
the flattened and raised values of the edit.[^user-guide]

The failure is largest where the voids were: steep terrain, low
backscatter deserts and the edges of the coverage, which the guide and
the comparison guide name as the places the new unwrapping and the
fill did their work.[^user-guide][^dem-guide]

**Correct approach.** The height layer is read together with the NUM
layer of the same tile, and the NUM byte is decoded by Table 2 into a
source class before it is used as a count. The fraction of a study
area whose height is not SRTM (NUM outside 1 to 23 and not 0) is a
property of the result and is stated with it. A comparison against
another DEM or an earlier SRTM release is restricted to SRTM-sourced
pixels, or the filled pixels are reported separately with their
source and its acquisition period. Water pixels are identified from
swb (or NUM 0) and excluded from terrain statistics. Where the
SRTM-only height is wanted without any fill, the NASADEM_SHHP
collection carries it, on the ellipsoid and with voids.[^user-guide][^nasadem]

**Verification.** A histogram of the NUM layer over the study area
shows which bands of Table 2 are present; a value above 23 that is not
0 or 255 is not an SRTM pixel. The filled regions, mapped from NUM,
coincide with the areas where NASADEM_SHHP's hgt_srtmOnly layer holds
its fill value -32768 (after the datum difference is allowed for),
because that collection has the voids the merge filled.[^user-guide]
Inside a filled region the texture changes with the source while the
height does not step at the boundary, which is the signature of the
delta surface fill.[^user-guide]

[^user-guide]: NASADEM user guide, version 1.3, January 2025, Tables 1 and 2 and section 5.1
[^hgt-page]: LP DAAC product page, NASADEM_HGT v001, read 2026-09-15
[^dem-guide]: LP DAAC DEM Product Comparison Guide, read 2026-09-15
[^astgtm-guide]: ASTER GDEM version 3 user guide, the NUM convention
[^cmr-numnc]: CMR collection record C2763264768-LPCLOUD, read 2026-09-15
[^nasadem]: this bundle's NASADEM concept
