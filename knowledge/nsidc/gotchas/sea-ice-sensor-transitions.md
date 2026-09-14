---
type: dataset-gotcha
spheres: [cryosphere]
title: "Sensor transitions (SMMR to SSM/I, F8 to F11 to F13 to F17, and on to AMSR2) leave steps that the intercalibration reduces and does not remove"
description: "NSIDC-0051 joins five sensors on single days (21 August 1987, 19 December 1991, 30 September 1995, 1 January 2008) with tie points regressed over overlaps of 22 days, 16 days, five months and twelve months and tuned to minimize hemispheric extent and area differences; the residual differences the guide tabulates run from 0.70 percent of Northern Hemisphere extent and 1.34 percent of area at the SMMR to F8 join down to a few hundredths of a percent, are statistically significant at the F11 to F13 and F13 to F17 joins, and are larger regionally and in the marginal ice zone. The Sea Ice Index's join to AMSR2 at 1 January 2025 adds differences of up to 0.2 million km2 of extent. A trend or a regional series that treats the record as one instrument reads these residuals as ice change."
tags: [sea-ice, sensor-transition, intercalibration, tie-points, smmr, ssmi, ssmis, amsr2, f8, f11, f13, f17, nsidc-0051, g02135, sea-ice-index]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:30:00Z }
severity: medium
# medium: the guide tabulates the residual differences at every join
# and dates the joins to the day, the variable name in each file
# carries the sensor, and the hemispheric residuals are a fraction of
# a percent, so the trap is a missing uncertainty term at the
# hemispheric scale and a larger, unquantified one regionally rather
# than a silently wrong number.
dataset: ../datasets/nsidc-0051-sea-ice-concentration.md
status: draft
stale_after: 2027-03-14
sources:
  - id: nsidc-0051-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/nsidc-0051-v002-userguide.pdf
    title: "NSIDC-0051 Version 2 user guide: the sensor periods, the overlap lengths and tie-point regressions for each transition, the subjective tuning of the F8 and F11 open-water tie points, the removal of overlap dates in Version 1.1, the statement that calibration on extent and area does not mean the concentrations match, the Northern and Southern Hemisphere sensor difference tables, and the limitation that coefficients are fixed per sensor"
  - id: nsidc-0051-page
    resource: https://nsidc.org/data/nsidc-0051/versions/2
    title: "NSIDC-0051 product page: the strength of thorough intercalibration and the limitation that fixed coefficients bias the retrieval when surface conditions change (Cavalieri and others 1999 and 2012)"
  - id: cavalieri-1999
    resource: https://doi.org/10.1029/1999JC900081
    title: "Cavalieri, Parkinson, Gloersen, Comiso and Zwally, 1999, Deriving long-term time series of sea ice cover from satellite passive-microwave multisensor data sets, JGR Oceans 104, 15803 to 15814: the abstract on the Crossref record states the lack of a full year of overlap as the major obstacle and the reduction of overlap differences to under 0.05 percent in extent and 0.6 percent or less in area (journal page behind a bot check)"
  - id: cavalieri-2012
    resource: https://doi.org/10.1109/LGRS.2011.2166754
    title: "Cavalieri, Parkinson, DiGirolamo and Ivanoff, 2012, Intersensor Calibration Between F13 SSMI and F17 SSMIS for Global Sea Ice Data Records, IEEE GRSL 9(2), 233 to 236 (the F13 to F17 calibration over a twelve-month overlap; cited on its Crossref record)"
  - id: nsidc-0079-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/nsidc-0079-v004-userguide.pdf
    title: "NSIDC-0079 Version 4 user guide: the Bootstrap record's own sensor dates (which differ from NSIDC-0051's by days to months) and the Version 3 change to intercalibrate the first two transitions on area"
  - id: g02135-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/g02135-v004-userguide.pdf
    title: "Sea Ice Index Version 4 user guide: tie-point adjustments as the guard against false jumps at a new instrument, the instrument usage table, and the consistency section on the AMSR2 resampling"
  - id: sii-special-report-28
    resource: https://nsidc.org/sites/default/files/documents/technical-reference/nsidc-special-report-28.pdf
    title: "NSIDC Special Report 28 (2025): the AMSR2 join dated to 1 January 2025 to avoid the melt season, extent differences of less than 0.2 and 0.15 million km2 with means of 0.05 and 0.04, AMSR2 lower on about 80 percent of Northern Hemisphere days, and the statement that the resampling does not achieve a zero-mean difference and that trends will be affected"
  - id: sensor-change-assessment
    resource: https://nsidc.org/sites/default/files/documents/technical-reference/pm_seaice_assessment_amsr2-ssmis.pdf
    title: "Meier, 2026, sensor-change assessment: the seasonal AMSR2 biases in extent and area over 2023 through 2025, larger in summer as at earlier transitions and concentrated near the ice edge"
  - id: sensors-summary
    resource: https://nsidc.org/sites/default/files/documents/technical-reference/smmr-ssmi-ssmis-sensors.pdf
    title: "NSIDC sensors summary: frequencies, swath widths and equator crossing times of Nimbus-7 SMMR and the DMSP SSM/I and SSMIS platforms"
  - id: dataset
    resource: ../datasets/nsidc-0051-sea-ice-concentration.md
    title: "This bundle's NSIDC-0051 dataset concept, which lists this trap among the known issues"
  - id: sii-dataset
    resource: ../datasets/sea-ice-index-g02135.md
    title: "This bundle's Sea Ice Index concept, which lists this trap among the known issues"
---

# Sensor transitions leave steps that the intercalibration reduces and does not remove

**Mechanism.** NSIDC-0051 is one series made of five sensors, each
with its own frequencies (18.0 GHz on SMMR against 19.35 GHz on
SSM/I and SSMIS), footprint, altitude, incidence angle and local
observation time, and each supplying the whole record on its own days:
SMMR through 20 August 1987, F8 SSM/I through 18 December 1991,
F11 SSM/I through 29 September 1995, F13 SSM/I through 31 December
2007 and F17 SSMIS from 1 January 2008, with the overlap dates removed
since Version 1.1 so that each join is a single
day.[^nsidc-0051-user-guide][^sensors-summary] Comparisons of the
sensors during their overlaps with the published tie points showed
significant differences, and the remedy was a new set of tie points
for each new sensor from linear least-squares fits of its brightness
temperatures against its predecessor's over the overlap, tuned so that
hemispheric extent and area matched: 22 days of SMMR and F8 overlap
(9 July to 20 August 1987), 16 days of F8 and F11 (3 to 18 December
1991), five months of F11 and F13 (May to September 1995) and twelve
months of F13 and F17 (all of 2007), with the F8 and F11 open-water
tie points adjusted subjectively, within one standard error except for
the Antarctic F8 values, and a further adjustment to an Antarctic F11
ice tie point.[^nsidc-0051-user-guide][^cavalieri-1999][^cavalieri-2012]
Cavalieri and others 1999 name the lack of a complete year of overlap
between sequential sensors as the major obstacle and report overlap
differences reduced to under 0.05 percent in extent and 0.6 percent
or less in area; the guide's own tables give the residual mean
differences in the Northern Hemisphere as 0.055 million km2 (0.70
percent) of extent and 0.073 million km2 (1.34 percent) of area for
SMMR to F8, 0.01 and 0.18 percent for F8 to F11, near zero and
0.18 percent for F11 to F13, and near zero in extent with 0.54
percent of area for F13 to F17, with Southern Hemisphere values of the
same order, and states that the F11 to F13 differences in extent and
area, and the F13 to F17 differences, were statistically significant
even where hemispheric mean concentration was
not.[^cavalieri-1999][^nsidc-0051-user-guide] The calibration is on
the hemispheric totals: the guide says in as many words that this does
not mean the concentrations themselves are well matched, that
relatively large and significant regional differences were seen at the
F11 to F13 transition, and that sensor-to-sensor differences are likely
to remain, particularly in the marginal ice zones; the product page
adds that the coefficients are fixed for a sensor, so a change in
characteristic surface conditions biases the
retrieval.[^nsidc-0051-user-guide][^nsidc-0051-page] Version 1.1's
reprocessing, the March 2015 pole hole change (its own gotcha) and the
use of the SSM/I pole hole through 2007 so that the F13 and F17 year
could be compared are all parts of the same
seam.[^nsidc-0051-user-guide] The Bootstrap record joins the same
sensors on different days (SMMR to 31 July 1987, F8 from 1 August, F11
from 18 December 1991, F13 from 10 May 1995) and since its Version 3
intercalibrates the first two joins on area rather than extent, so the
two records' seams do not coincide.[^nsidc-0079-user-guide] The newest
join is the Sea Ice Index's to AMSR2 on 1 January 2025, dated to avoid
a change in the melt season: over the first half of 2025 the AMSR2
extents differ from the SSMIS ones by less than 0.2 million km2 in the
north (mean 0.05) and 0.15 in the south (mean 0.04), lower on about
80 percent of northern days, the resampling that was meant to give a
zero-mean difference does not fully achieve it, and the three-year
assessment finds the biases larger in summer, as at earlier
transitions, and concentrated near the ice
edge.[^sii-special-report-28][^sensor-change-assessment][^g02135-user-guide]

**Wrong-result mode.** A hemispheric trend that carries only the
fit's formal error omits a term the record documents: a residual of a
few hundredths to about one percent at each of four joins, and a few
percent seasonally at the AMSR2 join, which, if it happened to align,
would read as a change of the size of the residual concentrated on the
join dates.[^nsidc-0051-user-guide][^sii-special-report-28] A regional
series, a marginal ice zone series or a concentration-based statistic
(area, a melt-season mean) crosses the joins with a step that is not
the hemispheric residual but the unquantified regional one the guide
warns of, so a regional trend that starts before 1987 or straddles
1995 or 2008 carries a sensor signature that no field in the file
marks.[^nsidc-0051-user-guide] A change-point analysis that finds
1987, 1991, 1995 or 2008 is finding the sensors unless the point is
shown to survive the hemispheric residuals and the pole hole
treatment.[^nsidc-0051-user-guide] A comparison of the AMSR2 years
with the SSMIS years without the assessment's seasonal biases reads a
few percent of summer extent and about 6 percent of Arctic area as ice
loss.[^sensor-change-assessment]

**Correct approach.** A series from NSIDC-0051 names the sensor of
each epoch (the concentration variable is named N07_ICECON,
F08_ICECON, F11_ICECON, F13_ICECON or F17_ICECON, and the browse file
names carry the same code) and treats the four join dates as known
seams; a hemispheric extent or area trend carries the guide's residual
differences at the joins as an uncertainty term beside its formal
error, and a regional or concentration-weighted statement says that
the intercalibration was hemispheric and does not bound its own
step.[^nsidc-0051-user-guide] The AMSR2 continuation is voiced with
the published biases (Special Report 28 for the first half of 2025,
the June 2026 assessment for 2023 through 2025, seasonal and larger in
area than in extent), and a record statement for a year on the AMSR2
side names the join.[^sii-special-report-28][^sensor-change-assessment]
A Bootstrap series is treated as having its own seams on its own
dates.[^nsidc-0079-user-guide]

**Verification.** The transition subsections, the sensor period
table, the Version 1.1 note and the two sensor difference tables of
the NSIDC-0051 guide were read on 2026-09-14, with the product page,
the NSIDC-0079 guide's acquisition and version sections, the Sea Ice
Index guide's tie-point and consistency sections, Special Report 28
and the June 2026 assessment; Cavalieri and others 1999 and 2012 are
cited on their Crossref records, and the 1999 figures here are from
the abstract on that record.[^nsidc-0051-user-guide][^nsidc-0051-page][^nsidc-0079-user-guide][^g02135-user-guide][^sii-special-report-28][^sensor-change-assessment][^cavalieri-1999][^cavalieri-2012][^sensors-summary]
The two dataset concepts list this trap among their known
issues.[^dataset][^sii-dataset]

[^nsidc-0051-user-guide]: NSIDC-0051 Version 2 user guide, NSIDC
[^nsidc-0051-page]: NSIDC product page, NSIDC-0051 Version 2
[^cavalieri-1999]: Cavalieri and others, 1999, JGR Oceans, doi:10.1029/1999JC900081
[^cavalieri-2012]: Cavalieri and others, 2012, IEEE GRSL, doi:10.1109/LGRS.2011.2166754
[^nsidc-0079-user-guide]: NSIDC-0079 Version 4 user guide, NSIDC
[^g02135-user-guide]: Sea Ice Index Version 4 user guide, NSIDC
[^sii-special-report-28]: Windnagel and others, 2025, NSIDC Special Report 28
[^sensor-change-assessment]: Meier, 2026, sensor-change assessment, NSIDC DAAC
[^sensors-summary]: NSIDC, Summary of SMMR, SSM/I, and SSMIS Sensors
[^dataset]: This bundle's NSIDC-0051 dataset concept
[^sii-dataset]: This bundle's Sea Ice Index concept
