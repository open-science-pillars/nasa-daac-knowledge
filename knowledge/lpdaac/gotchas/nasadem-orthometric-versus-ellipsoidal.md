---
type: dataset-gotcha
spheres: [geosphere]
title: "NASADEM heights are orthometric on the EGM96 geoid while GNSS, ICESat and ICESat-2, altimetry and lidar heights are ellipsoidal on WGS84: a comparison that skips the geoid separation is off by that separation, a smooth field of metres to tens of metres that looks like a DEM bias"
description: "The integer heights in NASADEM_HGT are metres above the EGM96 geoid, converted at the end of processing from the WGS84 ellipsoid heights the SRTM reprocessing and the ICESat control were done on; the floating-point SRTM-only heights in NASADEM_SHHP are still on the ellipsoid. The datum field of the catalogue records reads WGS84/EGM96, naming both. A GNSS receiver, an ICESat or ICESat-2 elevation and a lidar or altimeter height are ellipsoidal, while satellite DEMs such as SRTM, ASTER GDEM and NASADEM itself are on the geoid, and the difference between the two references at a place is the geoid undulation, which the guide's own coastal example shows reaching 17 m where the geoid-referenced product carries the sea at zero. A script that differences an ellipsoidal height against the merged DEM without the geoid, or differences the merged DEM against the SRTM-only DEM to find the fill, gets that separation as its answer and reads it as a bias, a fill, or an elevation change."
tags: [nasadem, nasadem-hgt, nasadem-shhp, egm96, wgs84, geoid, ellipsoid, orthometric, vertical-datum, srtm, dem, lpdaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T13:40:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-15T14:22:23Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/164 }
severity: high
dataset: ../datasets/nasadem.md
eval_case: nasadem-orthometric-versus-ellipsoidal
status: draft
stale_after: 2027-03-15
sources:
  - id: user-guide
    resource: https://lpdaac.usgs.gov/documents/2237/NASADEM_User_Guide_V13.pdf
    title: "NASADEM user guide, version 1.3, January 2025, read 2026-09-15: section 3 (the bold note that the integer heights in the merged void-free DEM files are relative to the EGM96 geoid whereas the floating-point heights in the SRTM-only DEM files are relative to the WGS84 ellipsoid) and Table 1; section 5.1.1 (the ellipsoid to geoid conversion, done after the reprocessing, by differencing a bilinearly resampled EGM96 conversion array from each ellipsoid-referenced quad); section 4.2.3.1 (ICESat heights on the TOPEX/Poseidon ellipsoid shifted to WGS84 by a latitude-dependent offset of about 70 cm); section 4.2.2.3 (ocean surface topography computed from the geoid, the circulation and the tides, with errors well under 50 cm); section 4.2.5 (the Bering Sea example, where the ellipsoid-referenced ocean elevation over 200,000 square kilometres varies gradually between -1 and 17 m); section 2 and 4.2.2.1 (the SRTM 16 m specification and the assessed 6.8 m absolute error)"
  - id: srtm-guide
    resource: https://lpdaac.usgs.gov/documents/179/SRTM_User_Guide_V3.pdf
    title: "SRTM Collection User Guide, revised October 2015, read 2026-09-15: the unit of elevation is metres referenced to the WGS84/EGM96 geoid, the convention NASADEM keeps for its merged product"
  - id: hgt-page
    resource: https://lpdaac.usgs.gov/products/nasadem_hgtv001/
    title: "LP DAAC product page for NASADEM_HGT v001, read 2026-09-15: the description names the conversion to geoid reference among the reprocessing improvements; the layer table lists DEM in metres with no datum column"
  - id: shhp-page
    resource: https://lpdaac.usgs.gov/products/nasadem_shhpv001/
    title: "LP DAAC product page for NASADEM_SHHP v001, read 2026-09-15: HGT_SRTMONLY (HGTS), the SRTM-only floating-point DEM in metres with fill -32768, and ERR in millimetres; the page does not name the ellipsoid, the guide does"
  - id: cmr-hgt
    resource: https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=NASADEM_HGT
    title: "CMR collection record for NASADEM_HGT v001 (C2763264762-LPCLOUD), read 2026-09-15: the geodetic model's horizontal datum name is WGS84/EGM96, the same string on the NASADEM_SHHP record"
  - id: dem-guide
    resource: https://lpdaac.usgs.gov/documents/642/DEM_Comparison_Guide.pdf
    title: "LP DAAC DEM Product Comparison Guide, read 2026-09-15: the specification table gives the datum of SRTM and NASADEM as WGS84/EGM96 and of ASTER GDEM as WGS84"
  - id: astgtm-guide
    resource: https://lpdaac.usgs.gov/documents/434/ASTGTM_User_Guide_V3.pdf
    title: "ASTER GDEM version 3 user guide, read 2026-09-15: the product table gives the DEM as referenced to the WGS84/EGM96 geoid, so the comparison guide's WGS84 for ASTER GDEM is a datum label, not an ellipsoidal height"
  - id: atl15
    resource: ../../nsidc/datasets/icesat2-atl15.md
    title: "The nsidc bundle's ICESat-2 ATL15 concept, whose grids are on the WGS 84 ellipsoid with WGS 84 as the vertical datum: an example of a satellite height product on the ellipsoid"
  - id: nasadem
    resource: ../datasets/nasadem.md
    title: "This bundle's NASADEM concept, with the collection table that gives each height layer its reference and the processing order"
  - id: void-gotcha
    resource: nasadem-void-fill-and-source-layer.md
    title: "This bundle's gotcha on the void fill, whose verification differences the two height layers and must allow for the datum first"
---

# NASADEM heights are orthometric on the EGM96 geoid

**Mechanism.** The NASADEM guide states the two references in one
bold sentence: the integer heights in the merged void-free DEM files
are relative to the EGM96 geoid, whereas the floating-point heights in
the SRTM-only DEM files are relative to the WGS84 ellipsoid.[^user-guide]
Its Table 1 repeats it per layer, hgt in metres relative to the EGM96
geoid and hgt_srtmOnly in metres relative to the WGS84 ellipsoid, and
this bundle's NASADEM concept carries the same table.[^user-guide][^nasadem]
The geoid is the reference the original SRTM products used, metres
referenced to the WGS84/EGM96 geoid, and the guide says most DEM
users want it because it puts the oceans at zero.[^srtm-guide][^user-guide]
The conversion was the last step: the whole reprocessing, including
the ripple correction against ICESat, was done on the ellipsoid, and
a conversion array from a standard EGM96 database at 15 by 15 arc
second postings, as the guide gives it, bilinearly resampled to 1 arc
second, was then differenced
from each ellipsoid-referenced quad, so the geoid height is the
ellipsoid height minus the array, and the SRTM-only collection is the
product before that subtraction.[^user-guide]

The catalogue does not make the distinction easy to see. The CMR
records of both collections give the horizontal datum name as
WGS84/EGM96, one string naming the ellipsoid of the coordinates and
the geoid of the heights, and the comparison guide's specification
table lists the same string against ASTER GDEM's plain WGS84, yet the
ASTER GDEM guide gives that product's heights as referenced to the
WGS84/EGM96 geoid too, so the shorter string is a datum label and not
a different reference.[^cmr-hgt][^dem-guide][^astgtm-guide] The
product page layer tables give the
DEM and the SRTM-only DEM in metres with no datum column, and the
product page for the SRTM-only collection does not name the
ellipsoid; the guide does.[^hgt-page][^shhp-page]

The heights a comparison brings to the DEM are usually ellipsoidal:
a GNSS receiver's height, ICESat and ICESat-2 elevations, radar and
laser altimetry and lidar surveys that report heights above the
ellipsoid. Satellite DEMs are not: SRTM, ASTER GDEM and NASADEM itself
are geoid-referenced.[^srtm-guide][^astgtm-guide][^user-guide] The
guide's own control data are ellipsoidal: ICESat GLAS elevations are given as
ellipsoid heights on the TOPEX/Poseidon ellipsoid and were shifted to
WGS84 by a latitude-dependent offset of about 70 cm on average before
comparison with the ellipsoid-referenced SRTM strips.[^user-guide] The
nsidc bundle's ICESat-2 ATL15 concept records its grids on the WGS 84
ellipsoid with WGS 84 as the vertical datum.[^atl15] The separation
between the two references at a place is the geoid undulation, a
smooth field. The guide gives its magnitude in one place: in the
Bering Sea example used to demonstrate the ripple correction, the
ocean elevation on the ellipsoid, computed from the geoid, the
circulation and the tides with errors well under 50 cm, varies
gradually between -1 and 17 m over 200,000 square kilometres, where
the geoid-referenced product carries the same water at
zero.[^user-guide] Against that, the SRTM specification was an
absolute vertical error under 16 m at the 90 per cent level and the
assessed average absolute error about 6.8 m.[^user-guide] The global
range of the undulation is not stated in the sources read here and no
figure for it is quoted.

**Wrong-result mode.** A comparison of an ellipsoidal height with the
merged DEM that skips the conversion returns the local geoid
undulation plus the real difference. Because the undulation is smooth
over tens of kilometres, it does not look like noise: a validation of
NASADEM against GNSS points, ICESat or ICESat-2 elevations, or an
airborne lidar DEM on the ellipsoid reports a systematic bias of
metres to more than ten metres and attributes it to the product; a
change detection between an ellipsoidal survey and NASADEM reports
uplift or subsidence of the same size; a flood, coastal or hydraulic
calculation that mixes a water level on one reference with terrain on
the other places the water line at the wrong height by the
undulation. The trap is inside the product too: hgt_srtmOnly minus
hgt is not the fill map, it is the geoid undulation everywhere plus
the fill where the SRTM-only layer is void, and a script that expects
zero outside the voids finds a field of metres and reads it as a
processing difference between the two collections.[^user-guide][^void-gotcha]
Nothing fails, because both layers are metres, both are heights of
the same terrain, and the datum field of the catalogue names WGS84.

**Correct approach.** The comparison is made on one reference. An
ellipsoidal height is converted to the geoid with the EGM96 model,
the one the product used, before it is differenced against hgt, or
hgt is converted the other way with the same model; a different
geoid model gives a different height by the difference between the
models, which is then part of the comparison. Where an ellipsoidal
comparison is wanted without a conversion, the SRTM-only height in
NASADEM_SHHP is already on the WGS84 ellipsoid, with its voids and
without the fill, and its err layer is the precision of that
height.[^user-guide][^nasadem] The reference in use is stated with
every height, because the catalogue string WGS84/EGM96 names both and
decides neither.[^cmr-hgt]

**Verification.** The product carries its own check. Over ocean and
large lakes the merged DEM holds the water mask's edited value, zero
for the ocean, while the SRTM-only layer holds the ellipsoid height
of the water surface where SRTM measured it, so hgt_srtmOnly minus
hgt at coastal water pixels is the local undulation plus the ocean
topography, of the size the guide's Bering Sea example shows, and the
same difference over land, away from the voids, is a smooth field of
the same size rather than zero or noise.[^user-guide] An external
ellipsoidal height set differenced against hgt shows a mean offset
that varies smoothly across the area and vanishes once the EGM96
undulation is applied to one side.

[^user-guide]: NASADEM user guide, version 1.3, January 2025, sections 2, 3, 4.2.2, 4.2.3.1, 4.2.5 and 5.1.1, Table 1
[^srtm-guide]: SRTM Collection User Guide, October 2015, the unit of elevation
[^hgt-page]: LP DAAC product page, NASADEM_HGT v001, read 2026-09-15
[^shhp-page]: LP DAAC product page, NASADEM_SHHP v001, read 2026-09-15
[^cmr-hgt]: CMR collection records C2763264762-LPCLOUD and C2763266322-LPCLOUD, read 2026-09-15
[^dem-guide]: LP DAAC DEM Product Comparison Guide, read 2026-09-15
[^astgtm-guide]: ASTER GDEM version 3 user guide, the WGS84/EGM96 geoid reference
[^atl15]: the nsidc bundle's ICESat-2 ATL15 concept, knowledge/nsidc/datasets/icesat2-atl15.md
[^nasadem]: this bundle's NASADEM concept
[^void-gotcha]: this bundle's gotcha on the void fill and the NUM layer
