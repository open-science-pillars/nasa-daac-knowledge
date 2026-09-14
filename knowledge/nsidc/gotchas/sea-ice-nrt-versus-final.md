---
type: dataset-gotcha
spheres: [cryosphere]
title: "Near-real-time and final sea ice concentration differ in input and processing, and a series that mixes NSIDC-0081, NSIDC-0051 and NSIDC-0803 steps at the join"
description: "NSIDC-0081 was the NASA Team near-real-time product: near-real-time brightness temperatures, F16, F17 and F18 SSMIS with F17 tie points applied to F18, automated masks, no manual quality control, unfilled gaps, one to two days of latency, and a documented warning against long-term trends. NSIDC-0051 is the final Goddard record with roughly a year of latency, manual cleaning and gap filling. The Sea Ice Index joined them until Version 3 and reprocessed the near-real-time months when the final data arrived, with monthly differences it measured at generally under 20,000 km2 and at most 1.6 percent; Version 4 joins NSIDC-0051 to NSIDC-0803 (AMSR2) at 1 January 2025 instead, with extent low by up to 3 to 5 percent in summer and area low by up to 6 percent. NSIDC-0081 is retired and NSIDC-0051 has stopped, so every current series contains a join, and a trend that crosses one without naming it reads the processing change as ice change."
tags: [sea-ice, near-real-time, nrt, nsidc-0081, nsidc-0051, nsidc-0803, amsr2, g02135, sea-ice-index, nasa-team, latency, reprocessing]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:30:00Z }
severity: medium
# medium: the Sea Ice Index names the source of every row in a column,
# the near-real-time guide carries the warning against trends in its
# limitations, and the product pages state the retirements, so the
# join is visible to a reader who looks; the measured differences are
# under one percent monthly for NSIDC-0081 and a few percent for
# NSIDC-0803, an error of the size of the sensor transitions rather
# than a silent corruption.
dataset: ../datasets/sea-ice-index-g02135.md
status: draft
stale_after: 2027-03-14
sources:
  - id: nsidc-0081-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/nsidc-0081-v002-userguide.pdf
    title: "NSIDC-0081 Version 2 user guide (published May 2023, updated April 2026): the near-real-time inputs from NSIDC-0080, F16, F17 and F18 with F17 tie points applied to F18, the masks, no manual removal of false ice, missing swaths and the 255 missing value, one to two day latency, and the limitation that the product is not reprocessed for consistency and is not for long-term trends"
  - id: nsidc-0081-page
    resource: https://nsidc.org/data/nsidc-0081/versions/2
    title: "NSIDC-0081 product page: retired as of 18 June 2026, forward processing ceased January 2026, coverage shown as 1 January 2024 to 14 January 2026, with NSIDC-0803 and NSIDC-0051 named as alternatives"
  - id: nsidc-0051-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/nsidc-0051-v002-userguide.pdf
    title: "NSIDC-0051 Version 2 user guide: the final record produced at Goddard about once a year with roughly one-year latency, manual quality control, gap filling, and the end of forward processing at 31 December 2025"
  - id: g02135-v3-user-guide
    resource: https://nsidc.org/sites/default/files/g02135-v003-userguide_1_1.pdf
    title: "Sea Ice Index Version 3 user guide: the near-real-time and final sections of the record, the reason for the split, the reprocessing when Goddard data arrive, the 2002 comparison (at most 1.6 percent) and the later comparisons (generally under 20,000 km2, much less than 1 percent), and the F17 tie points of the two products documented in different papers"
  - id: g02135-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/g02135-v004-userguide.pdf
    title: "Sea Ice Index Version 4 user guide: NSIDC-0051 through December 2024 and NSIDC-0803 from January 2025, the near-real-time product no longer used, the source column in each data file, the gap filling that revises a day's value on the next day, and images before 2025 still labelled final"
  - id: sii-special-report-28
    resource: https://nsidc.org/sites/default/files/documents/technical-reference/nsidc-special-report-28.pdf
    title: "NSIDC Special Report 28 (2025): the elimination of the near-real-time and final distinction, the AMSR2 input from 1 January 2025 chosen to avoid a change in the melt season, and the Version 3 to Version 4 extent differences"
  - id: sensor-change-assessment
    resource: https://nsidc.org/sites/default/files/documents/technical-reference/pm_seaice_assessment_amsr2-ssmis.pdf
    title: "Meier, 2026, sensor-change assessment: NSIDC-0803 and NSIDC-0081 against NSIDC-0051 over 2023 through 2025, extent and area, both hemispheres"
  - id: meier-2011
    resource: https://doi.org/10.1109/TGRS.2011.2117433
    title: "Meier, Khalsa and Savoie, 2011, Intersensor Calibration Between F-13 SSM/I and F-17 SSMIS Near-Real-Time Sea Ice Estimates, IEEE Transactions on Geoscience and Remote Sensing 49(9), 3343 to 3349 (the near-real-time F17 tie points; cited on its Crossref record)"
  - id: cavalieri-2012
    resource: https://doi.org/10.1109/LGRS.2011.2166754
    title: "Cavalieri, Parkinson, DiGirolamo and Ivanoff, 2012, Intersensor Calibration Between F13 SSMI and F17 SSMIS for Global Sea Ice Data Records, IEEE Geoscience and Remote Sensing Letters 9(2), 233 to 236 (the final record's F17 tie points; cited on its Crossref record)"
  - id: noaadata-g02135
    resource: https://noaadata.apps.nsidc.org/NOAA/G02135/north/daily/data/N_seaice_extent_daily_v4.0.csv
    title: "The Sea Ice Index daily extent file, read 2026-09-14: the Source Data column switching from NSIDC-0051 to NSIDC-0803 paths at 1 January 2025"
  - id: dataset
    resource: ../datasets/sea-ice-index-g02135.md
    title: "This bundle's Sea Ice Index concept, which lists this trap among the known issues"
  - id: nsidc-0051-dataset
    resource: ../datasets/nsidc-0051-sea-ice-concentration.md
    title: "This bundle's NSIDC-0051 dataset concept, which lists this trap among the known issues"
---

# Near-real-time and final sea ice concentration differ, and a mixed series steps at the join

**Mechanism.** Two NASA Team products covered the same grid and the
same days with different inputs and different processing. NSIDC-0081,
the near-real-time product, took near-real-time brightness
temperatures from NSIDC-0080, used SSMIS on F16, F17 and F18 with the
F17 tie points applied unchanged to F18 because the brightness
temperature differences were judged minimal, removed residual weather
with National Ice Center valid ice masks in the north and AMSR-E
sea surface temperature masks in the south, did no manual removal of
false ice, left missing swaths unfilled (value 255), and was
delivered within one to two days of acquisition with the stated
purpose of temporarily extending the long-term record until it was
updated.[^nsidc-0081-user-guide] NSIDC-0051, the final Goddard record,
used brightness temperatures processed at Goddard and NSIDC, one
sensor (F17 alone in the SSMIS era), a sea surface temperature valid
ice mask, manual inspection of every field, spatial and temporal gap
filling, and reached NSIDC about once a year with roughly a year of
latency; its F17 tie points are those of Cavalieri and others 2012,
while the near-real-time F17 tie points are those of Meier and others
2011.[^nsidc-0051-user-guide][^g02135-v3-user-guide][^cavalieri-2012][^meier-2011]
The NSIDC-0081 guide lists among its limitations that the product is
not reprocessed for long-term consistency and is not for long-term
trends.[^nsidc-0081-user-guide] The Sea Ice Index through Version 3
joined the two: the final section ran from the start of the record to
the most recent Goddard delivery, the near-real-time section covered
the last 6 to 18 months, each image was labelled with its source, and
when Goddard data arrived NSIDC reprocessed the near-real-time months
so that only the most recent three to six months used the less
quality-checked input; its own comparisons put the monthly extent and
area differences between the two inputs at most at 1.6 percent (June
2002 area) in an early test and, after the near-real-time brightness
temperature source changed, generally below 20,000 km2, much less than
1 percent.[^g02135-v3-user-guide] The 2023 through 2025 assessment
puts the daily NSIDC-0081 extent biases against NSIDC-0051 at a size
similar to the AMSR2 product's, that is up to about 100,000 to
150,000 km2 low in the Arctic summer, and its Antarctic area bias at a
maximum of about 150,000 km2.[^sensor-change-assessment] The
landscape has since changed: NSIDC-0081 forward processing ceased in
January 2026 and the product was retired on 18 June 2026, NSIDC-0051
stopped at 31 December 2025, and the Sea Ice Index Version 4 uses
NSIDC-0051 through December 2024 and NSIDC-0803 (AMSR2) from
1 January 2025, with no near-real-time and final distinction because
AMSR2 has no equivalent pair of products; its gap filling now revises
a day's extent on the following day instead of a year
later.[^nsidc-0081-page][^nsidc-0051-user-guide][^g02135-user-guide][^sii-special-report-28]
NSIDC-0803 against NSIDC-0051 over the three-year overlap is low by up
to 3 to 4 percent of Arctic extent in summer and 4 to 5 percent of
Antarctic extent in December through February, by about 6 percent of
Arctic area in summer and early autumn and 5 to 6 percent of Antarctic
area in November through January, with the differences concentrated
near the ice edge.[^sensor-change-assessment]

**Wrong-result mode.** A series built by appending NSIDC-0081 days to
NSIDC-0051 days, or NSIDC-0803 days to NSIDC-0051 days, carries a
processing step at the join of the sizes above, and a trend, an
anomaly against the 1981 through 2010 climatology, or a record-low
statement whose window ends in the appended part reads that step as
ice change; the near-real-time months are the ones most likely to be
the current year, so the join sits exactly where a record statement
is made.[^nsidc-0081-user-guide][^sensor-change-assessment] A Sea Ice
Index value downloaded in one year and again the next can differ for
the same month because the near-real-time input was replaced
(Version 3) or because a gap was refilled (Version 4), so a table
built from two downloads mixes revisions.[^g02135-v3-user-guide][^g02135-user-guide]
A daily NSIDC-0081 field with an unfilled swath summed as if complete
undercounts by the swath, where the same day in NSIDC-0051 is
interpolated.[^nsidc-0081-user-guide][^nsidc-0051-user-guide]

**Correct approach.** A series names the product behind each epoch:
the Sea Ice Index carries this in the source_dataset column of the
monthly files and the Source Data column of the daily file, and the
NSIDC-0051 and NSIDC-0081 file names carry the product
identifier.[^g02135-user-guide][^nsidc-0051-user-guide][^nsidc-0081-user-guide]
A trend or an anomaly is computed on one input stream, or across a
join whose measured difference (the Index's under 1 percent for
NSIDC-0081, the assessment's few percent for NSIDC-0803, seasonally
varying) is stated as part of the uncertainty; the Sea Ice Index's own
monthly series is the reference for a joined hemispheric record, with
its join dated and its differences published, and the images before
2025 still say "final" because the SSMIS input did not
change.[^g02135-user-guide][^sii-special-report-28][^sensor-change-assessment]
A statement about the current year names the download date of the
file it used.[^g02135-user-guide]

**Verification.** The NSIDC-0081 guide and product page (with the
retirement notice), the NSIDC-0051 guide, the near-real-time and
consistency sections of the Sea Ice Index Version 3 guide, the
Version 4 guide, Special Report 28 and the June 2026 assessment were
read on 2026-09-14; the two tie-point papers are cited on their
Crossref records.[^nsidc-0081-user-guide][^nsidc-0081-page][^nsidc-0051-user-guide][^g02135-v3-user-guide][^g02135-user-guide][^sii-special-report-28][^sensor-change-assessment][^meier-2011][^cavalieri-2012]
The daily extent file was read the same day and its Source Data
column switches from NSIDC-0051 paths to NSIDC-0803 paths at
1 January 2025.[^noaadata-g02135] One disagreement is recorded: the
NSIDC-0081 product page gives the coverage as 1 January 2024 to
14 January 2026 while its guide gives 1 January 2023 to 14 January
2026; the retirement makes the difference moot for new work. The
two dataset concepts list this trap among their known
issues.[^dataset][^nsidc-0051-dataset]

[^nsidc-0081-user-guide]: NSIDC-0081 Version 2 user guide, NSIDC
[^nsidc-0081-page]: NSIDC product page, NSIDC-0081 Version 2
[^nsidc-0051-user-guide]: NSIDC-0051 Version 2 user guide, NSIDC
[^g02135-v3-user-guide]: Sea Ice Index Version 3 user guide, NSIDC
[^g02135-user-guide]: Sea Ice Index Version 4 user guide, NSIDC
[^sii-special-report-28]: Windnagel and others, 2025, NSIDC Special Report 28
[^sensor-change-assessment]: Meier, 2026, sensor-change assessment, NSIDC DAAC
[^meier-2011]: Meier and others, 2011, IEEE TGRS, doi:10.1109/TGRS.2011.2117433
[^cavalieri-2012]: Cavalieri and others, 2012, IEEE GRSL, doi:10.1109/LGRS.2011.2166754
[^noaadata-g02135]: The Sea Ice Index daily extent file on the NOAA at NSIDC archive
[^dataset]: This bundle's Sea Ice Index concept
[^nsidc-0051-dataset]: This bundle's NSIDC-0051 dataset concept
