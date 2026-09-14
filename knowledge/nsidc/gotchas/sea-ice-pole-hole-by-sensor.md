---
type: dataset-gotcha
spheres: [cryosphere]
title: "The Arctic pole hole differs by sensor and each product treats it differently: an Arctic total that ignores it steps at the sensor changes"
description: "Each passive microwave sensor leaves a circle around the North Pole unobserved, and the masked hole shrinks from 1.19 million km2 under SMMR to 0.31 under SSM/I (August 1987), to 0.029 under SSMIS (January 2008), and grows to 0.064 under AMSR2 (January 2025 in the Sea Ice Index). NSIDC-0051 carries the hole as flag value 251 in the concentration variable, NSIDC-0079 as a missing sentinel, and the Sea Ice Index counts it as ice-covered in extent and excludes it from area. An Arctic total formed by summing cells, or by treating the flag as a concentration, steps by the mask difference at each transition, and nothing in the files marks the step as an artefact."
tags: [sea-ice, pole-hole, nsidc-0051, nsidc-0079, g02135, sea-ice-index, sea-ice-extent, sea-ice-area, smmr, ssmi, ssmis, amsr2, sensor-transition, arctic]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:30:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-14T12:17:15Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/148 }
severity: high
# high: the step is silent (the files carry a flag or an assumption,
# not an error field), it lands at the sensor changes where a reader
# expects nothing, and at 0.88 million km2 it is about a fifth of a
# recent September monthly extent, so a trend or a record-low
# statement that crosses 1987 or 2008 without the treatment stated is
# wrong without any sign of it; the eval case tests that the
# treatment is surfaced unprompted.
dataset: ../datasets/nsidc-0051-sea-ice-concentration.md
eval_case: sea-ice-pole-hole-by-sensor
status: draft
stale_after: 2027-03-14
sources:
  - id: nsidc-0051-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/nsidc-0051-v002-userguide.pdf
    title: "NSIDC-0051 Version 2 user guide: the pole hole table (sizes, radii, latitudes and dates by mask), the 251 flag value, the note that SMMR and SSM/I-SSMIS have different data gaps at the North Pole and that a pole mask is provided for time series of extent and area, and the Version 1 history entry that introduced the SSMIS mask"
  - id: nsidc-0079-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/nsidc-0079-v004-userguide.pdf
    title: "NSIDC-0079 Version 4 user guide: the same pole hole table, the 1100 missing sentinel that covers the never-measured pixels near the pole, and the statement of no coverage poleward of 84.5 N (SMMR) and 87.2 N (SSM/I and SSMIS)"
  - id: nsidc-0081-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/nsidc-0081-v002-userguide.pdf
    title: "NSIDC-0081 Version 2 user guide: the SSMIS pole hole mask as a circle that symmetrically covers the observed maximum extent of the jagged missing area, and the 251 flag"
  - id: g02135-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/g02135-v004-userguide.pdf
    title: "Sea Ice Index Version 4 user guide: the four masks including AMSR2, the assumption that the hole is ice covered for extent and excluded from area, the documented discontinuities in the monthly area series, the removed August 1987 area value, and the use of the SMMR hole throughout for anomaly and trend images"
  - id: sii-special-report-28
    resource: https://nsidc.org/sites/default/files/documents/technical-reference/nsidc-special-report-28.pdf
    title: "NSIDC Special Report 28 (2025): the AMSR2 pole hole is slightly larger and differently shaped than the SSMIS one because of the resampling in NSIDC-0802"
  - id: noaadata-g02135
    resource: https://noaadata.apps.nsidc.org/NOAA/G02135/north/monthly/data/
    title: "The Sea Ice Index monthly extent and area files, read 2026-09-14: the August file carries -9999 area for 1987, and the September file carries the extents used for scale here"
  - id: dataset
    resource: ../datasets/nsidc-0051-sea-ice-concentration.md
    title: "This bundle's NSIDC-0051 dataset concept, which lists this trap among the known issues"
  - id: sii-dataset
    resource: ../datasets/sea-ice-index-g02135.md
    title: "This bundle's Sea Ice Index concept, which lists this trap among the known issues"
---

# The Arctic pole hole differs by sensor and each product treats it differently

**Mechanism.** The orbit inclination of each satellite leaves a
circular sector centred on the North Pole that its sensor never
observes, and the sector's size depends on the sensor: the NSIDC-0051
and NSIDC-0079 user guides both tabulate a SMMR mask of 1.19 million
km2 (radius 611 km, poleward of 84.5 N), an SSM/I mask of 0.31 million
km2 (311 km, 87.2 N) and an SSMIS mask of 0.029 million km2 (94 km,
89.18 N).[^nsidc-0051-user-guide][^nsidc-0079-user-guide] The mask
is not the raw gap: for SSMIS it is a circle that symmetrically covers
the observed maximum extent of a jagged, day-to-day varying missing
area, chosen so that the number and location of masked cells is the
same every day.[^nsidc-0081-user-guide] The masks change on the
calendar of the sensors, not on a physical event: the SMMR mask gives
way to the SSM/I mask in the summer of 1987 (NSIDC-0051 dates the
SMMR mask through June 1987 and the SSM/I mask from July, while the
Sea Ice Index dates them through July and from August, and the SMMR
data themselves end on 20 August 1987), the SSMIS mask begins in
January 2008 although SSMIS data begin in January 2007, deliberately,
to allow a year of comparison with SSM/I, and the mask was itself a
March 2015 change applied back to 2008.[^nsidc-0051-user-guide][^g02135-user-guide]
In the Sea Ice Index a fourth mask enters on 1 January 2025 with the
AMSR2 input: 0.064 million km2, a rounded square 255 km wide inside a
circle at 88.5 N, larger than the SSMIS hole because the AMSR2
brightness temperatures are resampled to resemble
SSMIS.[^g02135-user-guide][^sii-special-report-28] Each product then
represents the hole its own way. NSIDC-0051 stores it as the value
251 inside the same byte array as the concentrations 0 to 250, beside
253 for coast and 254 for land; NSIDC-0079 stores it as the missing
sentinel 1100 in a field scaled by 0.001; the Sea Ice Index assumes
the whole hole is covered by ice above 15 percent and counts its area
in extent, while area, which weights by concentration, leaves the hole
out, and its concentration anomaly and trend images apply the largest
(SMMR) hole to the entire series so that they stay
continuous.[^nsidc-0051-user-guide][^nsidc-0079-user-guide][^g02135-user-guide]

**Wrong-result mode.** An Arctic total that sums the grid without
separating the flag from the data is wrong twice over: the 251 flag
read as a concentration is 100.4 percent of a cell, and read as zero
it is open water at the pole; either way the treated region changes
size by 0.88 million km2 in August 1987 and by 0.28 million km2 in
January 2008, and, in a record that continues with AMSR2 on the Index's
mask, by 0.035 million km2 in the other direction in January
2025.[^nsidc-0051-user-guide][^g02135-user-guide] A total that
correctly masks the hole and sums the observed cells still steps by
those amounts, because the observed area itself grew, and the step is
of the size of a climate signal: in the Sea Ice Index monthly file the
September extent is 7.05 million km2 in 1979 and 4.27 in 2007, so the
1987 step of 0.88 million km2 is about a fifth of that 2007 value and
larger than the Index's own AMSR2 transition differences of less than
0.2 million km2.[^noaadata-g02135][^sii-special-report-28] The Sea Ice
Index's own area column carries the step by design, which is why its
guide records discontinuities in the Northern Hemisphere monthly area
at the August to September 1987 and December 2007 to January 2008
boundaries and why the August 1987 area is removed from the file
(-9999 on 2026-09-14), while its extent column carries no step because
the hole is counted as ice throughout; an area trend across 1987 or
2008 read from that column, or a comparison of a pre-2008 and a
post-2008 area, therefore contains the mask change as if it were ice
loss or gain.[^g02135-user-guide][^noaadata-g02135] Nothing in the
files marks any of this: the NSIDC-0051 guide says only that the
different data gaps at the pole need to be taken into account in any
time series of extent or area and that a pole mask is provided for
the purpose.[^nsidc-0051-user-guide]

**Correct approach.** A hemispheric total from the concentration grids
separates the flag or sentinel values from the concentrations before
any arithmetic, and then states which of two treatments it applies
across the whole record: the hole filled by a stated assumption, which
for extent is the Sea Ice Index's assumption of full ice cover and
which adds the mask area to the observed extent, or the hole held at
one size, the largest, for every epoch, which is the Index's own choice
for its anomaly and trend images and which discards the SSM/I, SSMIS
and AMSR2 observations inside the SMMR
circle.[^g02135-user-guide][^nsidc-0051-user-guide] For area, where the
hole cannot be filled without a concentration, the Index's practice is
exclusion with the discontinuity documented and the August 1987 value
dropped, and an area series that spans a mask change names the mask
sizes on each side.[^g02135-user-guide] A statement that compares
totals across 1987, 2008 or 2025 names the mask treatment beside the
number, and the dates of the mask changes are the sensors' dates in
the product guides, not the dates of the sensors' first data (the
SSMIS mask begins a year after SSMIS data).[^nsidc-0051-user-guide]

**Verification.** The pole hole tables in the NSIDC-0051 and
NSIDC-0079 guides agree on the three sizes, radii and latitudes; the
Sea Ice Index guide adds the AMSR2 mask and states the extent and area
treatments, the discontinuities and the removed August 1987 value; all
were read on 2026-09-14.[^nsidc-0051-user-guide][^nsidc-0079-user-guide][^g02135-user-guide]
The August and September monthly files were read from the NOAA archive
the same day: the August file carries -9999 area for 1987 with extent
7.63 present, and the September extents quoted above are the file's
values.[^noaadata-g02135] The one-month disagreement between the
NSIDC-0051 guide (SMMR mask through June 1987) and the Sea Ice Index
guide (through July 1987) on the SMMR to SSM/I mask date is recorded
above and not resolved here; the SMMR data end on 20 August 1987 in
both.[^nsidc-0051-user-guide][^g02135-user-guide] The two dataset
concepts list this trap among their known
issues.[^dataset][^sii-dataset]

[^nsidc-0051-user-guide]: NSIDC-0051 Version 2 user guide, NSIDC
[^nsidc-0079-user-guide]: NSIDC-0079 Version 4 user guide, NSIDC
[^nsidc-0081-user-guide]: NSIDC-0081 Version 2 user guide, NSIDC
[^g02135-user-guide]: Sea Ice Index Version 4 user guide, NSIDC
[^sii-special-report-28]: Windnagel and others, 2025, NSIDC Special Report 28
[^noaadata-g02135]: The Sea Ice Index monthly files on the NOAA at NSIDC archive
[^dataset]: This bundle's NSIDC-0051 dataset concept
[^sii-dataset]: This bundle's Sea Ice Index concept
