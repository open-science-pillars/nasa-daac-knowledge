---
type: dataset-gotcha
spheres: [biosphere, geosphere]
title: "The HLS Fmask layer is bit-packed: cloud, shadow, snow, water and aerosol are bits to mask, not class values to compare"
description: "The HLS Fmask layer is one byte per pixel in which bit 1 is cloud, bit 2 adjacent to cloud or shadow, bit 3 cloud shadow, bit 4 snow or ice, bit 5 water and bits 6 and 7 the LaSRC aerosol level, with 255 the fill; several bits can be set at once because the labels are resampled to 30 m. It is not the Fmask algorithm's class raster, so a script that tests the byte against class integers (cloud equals 4, water equals 1, clear equals 0) passes clouded and shadowed pixels as clear, throws away clear pixels that carry a water, snow or low-aerosol bit, and reads the fill as a class, and nothing raises an error."
tags: [hls, hlsl30, hlss30, fmask, qa, cloud-mask, bit-packed, aerosol, lpdaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:40:00Z }
severity: high
dataset: ../datasets/hls-l30.md
eval_case: hls-fmask-is-bit-packed
status: draft
stale_after: 2027-03-14
sources:
  - id: user-guide
    resource: https://lpdaac.usgs.gov/documents/1698/HLS_User_Guide_V2.pdf
    title: "HLS Product User Guide, product version 2.0, April 2026, read in full 2026-09-14: section 4.2 (cloud masking), section 4.3 (the resampling rule that sets several bits), section 6.4 and Table 9 (the bit table), Appendix A (decoding by integer arithmetic, with the worked example of the value 100)"
  - id: hls-algorithms
    resource: https://hls.gsfc.nasa.gov/algorithms/
    title: "HLS project site, Algorithms page, read 2026-09-14: the QA band is named after Fmask but holds both the Fmask labels in bits 1 to 5 and the LaSRC aerosol level in bits 6 and 7; the dilated area may be treated as clear where data loss is a concern; high aerosol pixels are not recommended"
  - id: l30-known-issues
    resource: https://lpdaac.usgs.gov/documents/2434/HLS_v2.0_L30_known_issues_April2026.pdf
    title: "HLS L30 v2.0 Known Issues, April 2026, read 2026-09-14: bright-target failures are masked with bits 6 and 7 both set and the data under them should be discarded; a pixel below -0.2 reflectance has its QA set to the 255 fill; Fmask omission errors before April 2022"
  - id: s30-known-issues
    resource: https://lpdaac.usgs.gov/documents/2435/HLS_v2.0_S30_known_issues_April2026.pdf
    title: "HLS S30 V2.0 Known Issues, April 2026, read 2026-09-14: the same bright-target rule for S30, and the per-granule cloud mask boundary"
  - id: cmr-l30
    resource: https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=HLSL30&version=2.0
    title: "CMR collection record for HLSL30 v2.0, read 2026-09-14: the version 2 description, which says the two aerosol bits were added to the Fmask layer in this version"
  - id: l30
    resource: ../datasets/hls-l30.md
    title: "This bundle's HLS L30 concept, whose layer table lists Fmask as a uint8 bit field with fill 255"
  - id: s30
    resource: ../datasets/hls-s30.md
    title: "This bundle's HLS S30 concept, with the same layer on the Sentinel-2 product"
---

# The HLS Fmask layer is bit-packed

**Mechanism.** Every HLS v2.0 granule, L30 and S30 alike, carries one
quality assessment layer named `Fmask`, a uint8 raster with fill 255,
and the name is the trap: the layer is not the Fmask algorithm's
output raster of class integers. The guide says so in one sentence,
the Fmask integer output is mapped to an 8-bit bitwise representation,
and gives the mapping as Table 9, listed from the least significant
bit:[^user-guide]

| Bit | Value of the bit alone | Meaning when set |
|---|---|---|
| 0 | 1 | cirrus: reserved, not used in v2.0 |
| 1 | 2 | cloud |
| 2 | 4 | adjacent to cloud or shadow (the 150 m dilation) |
| 3 | 8 | cloud shadow |
| 4 | 16 | snow or ice |
| 5 | 32 | water |
| 6 and 7 | 64 and 128 | aerosol level: neither set is climatology aerosol, bit 6 alone is low, bit 7 alone is medium, both set is high |

The aerosol reading of bits 6 and 7 is fixed by the guide's own
worked example: the value 100, binary 01100100, decodes as low
aerosol, water and adjacent to cloud, and 100 is 64 plus 32 plus 4,
so bit 6 alone is low.[^user-guide] The project site describes the
same byte: named after the cloud masking algorithm, holding the Fmask
labels and the dilation in bits 1 to 5 and the LaSRC aerosol optical
thickness level in bits 6 and 7, and the aerosol bits are new in
version 2.0.[^hls-algorithms][^cmr-l30] The layer tables of this bundle's
L30 and S30 concepts list the layer the same way on both
products.[^l30][^s30]

The bits are not mutually exclusive. The labels are produced at the
input resolution and resampled to 30 m with a rule that turns on an
output bit when any of the contributing input pixels carries the
label, and picks the highest aerosol level among them, so one HLS
pixel can be cloud and water and snow at once; the guide says the
lower six bits may not be mutually exclusive for exactly this
reason.[^user-guide] There is no clear class: a clear pixel is one with
none of bits 1 to 5 set, and it still carries an aerosol level in the
top two bits, so a clear pixel with low aerosol has the value 64, not
0.[^user-guide]

**Wrong-result mode.** A script written for a class raster compares
the byte to integers. `fmask == 0` as the clear test keeps only
climatology-aerosol pixels and silently discards every clear pixel
whose aerosol level is low or medium, and every clear water and clear
snow pixel; the composite that results is thinner than the archive
and biased toward whatever surfaces carry no water or snow bit.
`fmask == 4` or `fmask == 2` as the cloud test catches only pixels
whose byte is exactly that value; a cloud pixel that is also adjacent
(6), or cloud over water (34), or cloud with high aerosol (194), passes
as clear, and the composite carries cloud. Treating 255 as a class, or
as clear because it matches nothing, passes fill pixels that the
correction itself wrote: a pixel whose reflectance fell below -0.2
near a bright target has reflectance -9999 and QA 255, and both look
like data to a comparison.[^l30-known-issues][^s30-known-issues] None
of this raises an error, because every one of these values is a valid
uint8.

The failure compounds where the mask matters most. Bright targets,
snow and cloud edges are where the aerosol retrieval fails and where
the known issues documents say the data under bits 6 and 7 both set
should be discarded, and a value comparison never tests those
bits.[^l30-known-issues][^s30-known-issues]

**Correct approach.** Each condition is a bit test, a bitwise AND with
the bit's value or the integer division the guide's Appendix A gives
for environments without bit operators, and the fill is tested first
as the whole byte equal to 255.[^user-guide] A clear-sky selection is
then a statement of which bits it excludes: cloud (2) and cloud shadow
(8) in every case; adjacent (4) as a choice, since the project site says the
dilated area can be treated as clear where data loss is a concern;
snow (16) and water (32) by what is being measured, not as a proxy
for cloud; and the aerosol level by masking bits 6 and 7 together,
with both set (192) excluded on the known issues documents'
recommendation.[^hls-algorithms][^l30-known-issues] The selection is
the same on L30 and S30, because in v2.0 the cloud and shadow bits
come exclusively from Fmask 4.7 for both products.[^user-guide]

**Verification.** On any granule, a histogram of the Fmask byte shows
values above 63 that no class raster would hold, and a count of
pixels with bit 1 set is at least the count of pixels equal to 2 and
larger wherever cloud coincides with water, snow or a dilation.
Decoding the value 100 by the bit table gives low aerosol, water and
adjacent to cloud, as the guide's Appendix A does.[^user-guide] The
metadata field CLOUD_COVERAGE in the granule's cmr.xml, the percentage
of cloud and cloud shadow by Fmask, agrees with a bit-tested count
over the tile and not with a value-tested one.[^user-guide]

[^user-guide]: HLS Product User Guide, product version 2.0, April 2026, section 6.4, Table 9 and Appendix A
[^hls-algorithms]: HLS project site, Algorithms page, Cloud Masking and Quality Assessment
[^l30-known-issues]: HLS L30 v2.0 Known Issues, April 2026, issue 1
[^s30-known-issues]: HLS S30 V2.0 Known Issues, April 2026, issue 1
[^cmr-l30]: CMR collection record C2021957657-LPCLOUD, version description
[^l30]: this bundle's HLS L30 concept
[^s30]: this bundle's HLS S30 concept
