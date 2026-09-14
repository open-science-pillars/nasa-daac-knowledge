---
type: dataset-gotcha
spheres: [biosphere, geosphere]
title: "HLS reflectance is int16 scaled by 0.0001 with -9999 as fill, the thermal bands by 0.01, the QA byte by nothing with 255 as fill, and some granules do not say so in their tags"
description: "Every HLS reflective band is int16 reflectance times 10,000 with an offset of zero and a fill of -9999; the two L30 thermal bands are int16 brightness temperature in hundredths of a degree Celsius with the same fill; the Fmask byte is unscaled with fill 255; the four angle layers are uint16 hundredths of a degree with fill 40,000. A small number of granules lack the scale_factor and offset tags in their COGs, so a reader that scales by the tag scales those by nothing, and the correction itself writes the fill into pixels whose reflectance fell below -0.2. A mean that includes -9999, or a mixture of scaled and unscaled granules, is wrong by orders of magnitude and visibly so; the trap is in the automatic conversion, not the numbers."
tags: [hls, hlsl30, hlss30, scale-factor, fill-value, int16, nodata, cog, lpdaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:40:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-14T12:12:43Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/145 }
severity: low
dataset: ../datasets/hls-l30.md
status: stable
stale_after: 2027-03-14
sources:
  - id: user-guide
    resource: https://lpdaac.usgs.gov/documents/1698/HLS_User_Guide_V2.pdf
    title: "HLS Product User Guide, product version 2.0, April 2026, read in full 2026-09-14: Tables 6 and 7 (type, scale and fill per layer), Table 8 (the angle layers), Table 11 (ADD_OFFSET, REF_SCALE_FACTOR, ANG_SCALE_FACTOR, THERM_SCALE_FACTOR, FILLVALUE, QA_FILLVALUE, ANG_FILLVALUE in the metadata)"
  - id: l30-page
    resource: https://lpdaac.usgs.gov/products/hlsl30v002/
    title: "LP DAAC product page for HLSL30 v2.0, read 2026-09-14: the variables table with data type, fill value and scale factor per layer"
  - id: s30-page
    resource: https://lpdaac.usgs.gov/products/hlss30v002/
    title: "LP DAAC product page for HLSS30 v2.0, read 2026-09-14: the variables table with data type, fill value and scale factor per layer"
  - id: l30-known-issues
    resource: https://lpdaac.usgs.gov/documents/2434/HLS_v2.0_L30_known_issues_April2026.pdf
    title: "HLS L30 v2.0 Known Issues, April 2026, read 2026-09-14: issue 1 (reflectance below -0.2 set to -9999 and QA to 255) and issue 8 (scale_factor and offset not set in some granules' COGs)"
  - id: s30-known-issues
    resource: https://lpdaac.usgs.gov/documents/2435/HLS_v2.0_S30_known_issues_April2026.pdf
    title: "HLS S30 V2.0 Known Issues, April 2026, read 2026-09-14: issue 1 (the same -0.2 rule), issue 6 (snow reflectance up to 1.6 in the visible), issue 7 (scale_factor and offset not set in some granules' COGs), and the resolved issue where an affected band sets every band of the pixel to fill"
  - id: hls-l30-page
    resource: https://hls.gsfc.nasa.gov/products-description/l30/
    title: "HLS project site, L30 product description, read 2026-09-14: the layer table's saturation flag column, value 12000 for the reflective bands"
  - id: l30
    resource: ../datasets/hls-l30.md
    title: "This bundle's HLS L30 concept, with the layer table"
  - id: s30
    resource: ../datasets/hls-s30.md
    title: "This bundle's HLS S30 concept, with the layer table"
---

# HLS reflectance is int16 scaled by 0.0001 with -9999 as fill

**Mechanism.** The guide's Tables 6, 7 and 8 give the encoding of
every layer, the product pages' variables tables repeat it, and this
bundle's two dataset concepts carry it in their layer
tables:[^user-guide][^l30-page][^s30-page][^l30][^s30]

| Layers | Type | Scale | Offset | Fill | Unit after scaling |
|---|---|---|---|---|---|
| reflective bands, both products | int16 | 0.0001 | 0 | -9999 | reflectance |
| L30 B10 and B11 (TIRS) | int16 | 0.01 | 0 | -9999 | degrees Celsius, brightness temperature |
| Fmask | uint8 | none | | 255 | bit field |
| SZA, SAA, VZA, VAA | uint16 | 0.01 | | 40000 | degrees |

The same values are in the granule metadata as REF_SCALE_FACTOR,
THERM_SCALE_FACTOR, ANG_SCALE_FACTOR, ADD_OFFSET, FILLVALUE,
QA_FILLVALUE and ANG_FILLVALUE.[^user-guide] The reflective and
thermal fills are the same integer under different scales, so a
-9999 read as reflectance is -0.9999 and read as temperature is
-99.99 degrees. The known issues documents add two facts. For a small
number of granules the scale_factor and offset were not set in the
COG files of some bands; the code has been corrected and the affected
granules have not been reprocessed, so a reader that converts by the
tag leaves those bands as integers.[^l30-known-issues][^s30-known-issues]
And the correction writes fill into data: where the aerosol retrieval
next to a bright target drives a pixel's reflectance below -0.2, the
reflectance is set to -9999 and the QA byte to 255, so a fill pixel
can sit inside an otherwise clear scene.[^l30-known-issues][^s30-known-issues]
Reflectance is not bounded by the scaling either: over undetected
snow the visible bands reach 1.6, and the project site's layer table
gives 12000, that is 1.2 after scaling, as a saturation flag value,
a column the guide does not carry.[^s30-known-issues][^hls-l30-page]

**Wrong-result mode.** The failures are large rather than subtle,
which is why this concept is low severity. A tile mean that includes
-9999 is pulled negative; a composite that averages a granule read as
integers with granules read as scaled reflectance is dominated by the
integers; a threshold on reflectance applied to an unscaled granule
selects everything or nothing; a normalized difference index is
scale-free but not fill-free, and a fill pixel in one band gives an
index of the wrong sign. Since June 2025 an S30 pixel affected by
packet loss in any band is fill in every band, but before that date,
and in every granule not reprocessed, a fill can be in one band and
not another.[^s30-known-issues] A reflectance above 1 is not an
error to clip but a snow pixel the correction handled badly, and
clipping hides it.[^s30-known-issues]

**Correct approach.** The fill is tested as the integer -9999 on the
raw array before any scaling, on every band used, and the QA fill 255
is tested on the QA byte; the scaling is applied explicitly as
0.0001 for reflectance, 0.01 for the thermal and angle layers, from
the guide's tables rather than from the tag alone, so the granules
without tags convert like the rest.[^user-guide][^l30-known-issues]
Values above 1 are kept and flagged by the aerosol bits and the snow
bit, not clipped.[^s30-known-issues]

**Verification.** The minimum of any reflective band's raw integers
on a granule that has fill is -9999 and the next value up is inside
the reflectance range; on a granule missing its tags, a GeoTIFF
reader reports no scale and the integers are the same order of
magnitude as on a tagged granule, thousands rather than
tenths.[^l30-known-issues] The metadata field REF_SCALE_FACTOR in the
granule's cmr.xml reads 0.0001 on both kinds.[^user-guide]

[^user-guide]: HLS Product User Guide, product version 2.0, April 2026, Tables 6, 7, 8 and 11
[^l30-page]: LP DAAC product page, HLSL30 v2.0, variables table
[^s30-page]: LP DAAC product page, HLSS30 v2.0, variables table
[^l30-known-issues]: HLS L30 v2.0 Known Issues, April 2026, issues 1 and 8
[^s30-known-issues]: HLS S30 V2.0 Known Issues, April 2026, issues 1, 6 and 7 and the resolved issues
[^hls-l30-page]: HLS project site, L30 product description
[^l30]: this bundle's HLS L30 concept
[^s30]: this bundle's HLS S30 concept
