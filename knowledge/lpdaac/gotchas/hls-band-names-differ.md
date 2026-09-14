---
type: dataset-gotcha
spheres: [biosphere, geosphere]
title: "HLS L30 and S30 keep their sensors' band numbers: B05, B06, B07, B09, B10 and B11 name different wavelengths in the two products"
description: "The HLS band codes retain the OLI numbering in L30 and the MSI numbering in S30. B05 is the near infrared in L30 and the first red-edge band in S30; B06 and B07 are the shortwave infrared in L30 and red-edge bands in S30; B09 is cirrus in L30 and water vapour in S30; B10 and B11 are thermal brightness temperature in L30 and cirrus and SWIR 1 in S30; the S30 near infrared and shortwave infrared are B8A, B11 and B12, codes that L30 does not have or means differently. A script keyed on one product's codes either fails on the other for a missing file or silently substitutes a red-edge band for the near infrared in an index."
tags: [hls, hlsl30, hlss30, band-names, oli, msi, ndvi, red-edge, lpdaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:40:00Z }
severity: medium
dataset: ../datasets/hls-s30.md
status: draft
stale_after: 2027-03-14
sources:
  - id: user-guide
    resource: https://lpdaac.usgs.gov/documents/1698/HLS_User_Guide_V2.pdf
    title: "HLS Product User Guide, product version 2.0, April 2026, read in full 2026-09-14: section 3.4 and Table 3 (the band code names by product), Tables 6 and 7 (the layers of each product), section 6.1 (the file lists of one L30 and one S30 granule)"
  - id: hls-s30-page
    resource: https://hls.gsfc.nasa.gov/products-description/s30/
    title: "HLS project site, S30 product description, read 2026-09-14: the OLI to MSI band matchup table (OLI 5 to MSI 8A, OLI 6 to MSI 11, OLI 7 to MSI 12)"
  - id: hls-algorithms
    resource: https://hls.gsfc.nasa.gov/algorithms/
    title: "HLS project site, Algorithms page, read 2026-09-14: Table 1 with the L30 and S30 band codes side by side per band name"
  - id: l30-page
    resource: https://lpdaac.usgs.gov/products/hlsl30v002/
    title: "LP DAAC product page for HLSL30 v2.0, read 2026-09-14: the variables table (Band 5 NIR, Band 6 SWIR1, Band 7 SWIR2, Band 9 Cirrus, Band10 TIRS1, Band11 TIRS2)"
  - id: s30-page
    resource: https://lpdaac.usgs.gov/products/hlss30v002/
    title: "LP DAAC product page for HLSS30 v2.0, read 2026-09-14: the variables table (Red Edge1 to 3, Band 8 NIR Broad, Band 8A NIR Narrow, Water Vapor, Band 11 SWIR1, Band 12 SWIR2)"
  - id: l30
    resource: ../datasets/hls-l30.md
    title: "This bundle's HLS L30 concept, with the L30 layer table"
  - id: s30
    resource: ../datasets/hls-s30.md
    title: "This bundle's HLS S30 concept, with the S30 layer table"
---

# HLS L30 and S30 keep their sensors' band numbers

**Mechanism.** The guide states the rule in one sentence: all Landsat
8 and 9 OLI and Sentinel-2 MSI reflective spectral band nomenclatures
are retained in the HLS products.[^user-guide] The products are
harmonized in reflectance and grid, not in file naming, and the layer
file of a band is named by its code, `...v2.0.B05.tif`. Table 3 of the
guide, and Table 1 of the project site, give the codes side by
side:[^user-guide][^hls-algorithms]

| Band | L30 code | S30 code |
|---|---|---|
| coastal aerosol | B01 | B01 |
| blue | B02 | B02 |
| green | B03 | B03 |
| red | B04 | B04 |
| red-edge 1, 2, 3 | none | B05, B06, B07 |
| NIR broad | none | B08 |
| NIR narrow | B05 | B8A |
| SWIR 1 | B06 | B11 |
| SWIR 2 | B07 | B12 |
| water vapour | none | B09 |
| cirrus | B09 | B10 |
| thermal infrared 1 and 2 (brightness temperature) | B10, B11 | none |

Only B01 to B04 mean the same thing in both products. The codes B05,
B06, B07, B09, B10 and B11 exist in both products and name different
wavelengths; B08, B8A and B12 exist only in S30; there is no B08 in
L30 at all.[^user-guide] This bundle's two dataset concepts carry the
full layer tables.[^l30][^s30] The product pages' variables tables say the
same in the DAAC's words: L30 Band 5 is NIR and Band 6 SWIR1, S30 Band
5 is Red Edge1 and Band 11 SWIR1.[^l30-page][^s30-page] The bandpass
adjustment that makes S30 OLI-like is keyed on this matchup, OLI 5 to
MSI 8A, OLI 6 to MSI 11, OLI 7 to MSI 12, and the matchup is not
reflected in the codes.[^hls-s30-page]

**Wrong-result mode.** Two failures, one loud and one quiet. A script
written for S30 that opens `B8A`, `B11` and `B12` on an L30 granule
fails for missing files, which is the loud one. A script written for
L30 that computes a normalized difference vegetation index from B05
and B04 runs unchanged on S30, because S30 has a B05, and the index it
returns uses the first red-edge band at 0.69 to 0.71 micrometres in
place of the near infrared at 0.85 to 0.88: every file opens, every
array has the right shape, and the time series that stacks L30 and
S30 by date carries a step at every S30 date that has nothing to do
with the land.[^user-guide] The same script's normalized burn ratio
or normalized difference water index from B05 and B06 or B07 on S30
mixes two red-edge bands. In the other direction, an S30 script that
reads B10 as cirrus reads a brightness temperature in hundredths of a
degree Celsius on L30, and B11 as SWIR 1 reads the second thermal
band.[^user-guide] The thermal codes are scaled by 0.01 where the
reflective ones are scaled by 0.0001, so the substituted values are
not even in the same numeric range, and a ratio index hides that
too.[^user-guide]

**Correct approach.** The band a computation needs is named by its
physical name and resolved to a code per product from Table 3: near
infrared is L30 B05 and S30 B8A (the narrow band, the one the bandpass
adjustment ties to OLI 5), shortwave infrared 1 is L30 B06 and S30 B11,
shortwave infrared 2 is L30 B07 and S30 B12, cirrus is L30 B09 and S30
B10.[^user-guide][^hls-s30-page] The product is read from the file
name (`HLS.L30` or `HLS.S30`) before the code is chosen. A time series
that stacks the two products stacks by physical band, and carries the
product in each record, since the red-edge, broad NIR and water vapour
bands exist on S30 dates only and the thermal bands on L30 dates only.
S30 B08, the broad near infrared, is a second NIR that has no L30
counterpart and no bandpass adjustment, so an index built on it is not
harmonized with the L30 dates.[^user-guide][^hls-s30-page]

**Verification.** On one tile and one date with both products, the
L30 B05 and S30 B8A rasters agree far more closely over vegetation
than L30 B05 and S30 B05 do; a vegetation
index from the wrong pair is visibly lower over vegetation because the
red edge sits on the rising flank of the vegetation spectrum. The
guide's file lists show the difference directly: the L30 example
directory has no B08, B8A or B12 file and the S30 example has all
three.[^user-guide]

[^user-guide]: HLS Product User Guide, product version 2.0, April 2026, section 3.4, Table 3, Tables 6 and 7, section 6.1
[^hls-s30-page]: HLS project site, S30 product description, band matchup table
[^hls-algorithms]: HLS project site, Algorithms page, Table 1
[^l30-page]: LP DAAC product page, HLSL30 v2.0, variables table
[^s30-page]: LP DAAC product page, HLSS30 v2.0, variables table
[^l30]: this bundle's HLS L30 concept
[^s30]: this bundle's HLS S30 concept
