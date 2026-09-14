---
type: dataset-gotcha
spheres: [atmosphere, geosphere]
title: "Every Daymet year has 365 days: leap years keep February 29 and drop December 31, so a positional or generated-date join misaligns after February in a leap year"
description: "The Daymet calendar is a 365-day year in every year. In a leap year the files include February 29 and discard December 31, so a leap year's file has 365 time steps whose last one is December 30. Code that labels the steps with a no-leap calendar puts every value from February 29 onward one day late, code that joins a 366-day observation record by position on a 365-day assumption misaligns everything after February 28, and an annual total over a leap year sums 365 days; nothing raises an error, because 365 steps is exactly what every other year has."
tags: [daymet, calendar, 365-day, leap-year, time-axis, join, alignment, ornldaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:40:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-14T12:17:15Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/143 }
severity: high
# high: the misalignment is silent (every year has the same number of
# steps, so no length check catches it) and it corrupts daily joins,
# anomalies and totals from February 29 to the end of every leap year;
# the eval case exercises the trap.
dataset: ../datasets/daymet-v4.md
eval_case: daymet-365-day-year
status: draft
stale_after: 2027-03-14
sources:
  - id: ornl-v4-guide
    resource: https://daac.ornl.gov/DAYMET/guides/Daymet_Daily_V4.html
    title: "ORNL DAAC user guide, Daymet Daily V4 (documentation revision 2024-06-17): the Daymet calendar section (all years have 1 to 365 days, leap day included, December 31 discarded in leap years) and the coverage statement (through December 31, or December 30 in leap years)"
  - id: daymet-overview
    resource: https://daymet.ornl.gov/overview
    title: "Daymet project site, description page: the calendar section with the same statement"
  - id: cmr-daily-v4r1
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2532426483-ORNL_CLOUD.umm_json
    title: "CMR collection record for Daymet Daily Version 4 R1: the abstract's coverage statement (December 31, or December 30 in leap years) and the one-file-per-year granule structure"
  - id: dataset
    resource: ../datasets/daymet-v4.md
    title: "This bundle's Daymet dataset concept, which lists this trap among the known issues"
---

# Every Daymet year has 365 days

**Mechanism.** The Daymet calendar is based on a standard calendar
year, and all Daymet years, including leap years, have 1 to 365 days:
in a leap year the data include leap day, February 29, and December 31
is discarded to keep the 365-day year.[^ornl-v4-guide][^daymet-overview]
The product's coverage statement says the same thing from the other
end: each year runs to December 31, or to December 30 in leap
years.[^ornl-v4-guide][^cmr-daily-v4r1] The data are one file per
variable, region and year, so a leap year's file has the same 365 time
steps as any other year, and by the calendar arithmetic its sixtieth
step is February 29 and its last step is December
30.[^ornl-v4-guide][^cmr-daily-v4r1] This is neither the standard
calendar (366 days in a leap year) nor the CF no-leap calendar (365
days with no February 29): it is a third convention that the file
count and the step count do not reveal.[^ornl-v4-guide]

**Wrong-result mode.** Three readings go wrong on a leap year, and
none of them errors. A time axis generated as day 1 to day 365 under a
no-leap calendar labels step 60 as March 1 and every later step one
day late, through step 365 labeled December 31 when it is December
30; every daily anomaly, degree-day sum and event date from March
onward is shifted by one day, in leap years only, so a multi-year
series carries a one-day shift in one year of every four. A join by
position against a 366-day record (a station file, a model forcing
series, a reanalysis) aligns January 1 through February 28 and then
pairs Daymet's February 29 with the record's February 29 correctly
only if the record also has it; if the join was built on a 365-day
assumption the record's February 29 is skipped and everything after
it is off by one, and either way the record's December 31 has no
Daymet partner. An annual total or mean over a leap year sums 365
days and omits December 31, so a Daymet annual precipitation total
for a leap year is low by that day's precipitation against a 366-day
station total, and a year length counted from the file is 365 for
every year. A stitched multi-year daily series carries a one-day hole
at the end of every leap year that a calendar-aware time axis shows
and a count-based one hides.

**Correct approach.** The time coordinate in the files, not a
generated day count, is the record of which calendar dates a year's
365 steps stand for, and the guide's calendar statement is the rule
behind it: February 29 present, December 31 absent, in leap
years.[^ornl-v4-guide] A join against a 366-day record is a join on
calendar dates with December 31 of leap years treated as missing in
Daymet, never a positional join and never a shift; an annual total
over a leap year is stated as a 365-day total that omits December 31,
and a comparison against a 366-day total says so. Where a consumer
requires a 366-day leap year, the product documentation provides no
value for December 31, and whatever fill the analysis chooses is the
analysis's own step, stated as such.

**Verification.** The guide's calendar section and the project site's
description page carry the rule.[^ornl-v4-guide][^daymet-overview]
The coverage statement in the guide and in the CMR abstract ends leap
years on December 30.[^ornl-v4-guide][^cmr-daily-v4r1] On any leap
year's file the check is direct: 365 time steps, a step dated
February 29, and no step dated December 31. No Daymet file was opened
for this concept; the statements rest on the documentation read on
2026-09-14.[^ornl-v4-guide][^cmr-daily-v4r1] The dataset concept lists
this trap among the product's known issues.[^dataset]

[^ornl-v4-guide]: ORNL DAAC user guide, Daymet Daily V4, revision 2024-06-17, read 2026-09-14
[^daymet-overview]: Daymet project site, description page, read 2026-09-14
[^cmr-daily-v4r1]: CMR collection C2532426483-ORNL_CLOUD, read 2026-09-14
[^dataset]: This bundle's Daymet dataset concept
