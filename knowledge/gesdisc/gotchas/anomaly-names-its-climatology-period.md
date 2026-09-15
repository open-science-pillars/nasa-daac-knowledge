---
type: dataset-gotcha
spheres: [atmosphere]
title: "An anomaly names its climatology period: an AIRS or OMI departure is relative to a base period and a processing version, the records carry documented breaks (the 2021 Aqua manoeuvre, the January 2026 AIRS gap, the OMI row anomaly onset, the collection 4 reprocessings), and two anomalies on different bases differ by a number that is not a constant"
description: "Neither AIRS level 3 nor the OMI level 3 grids ship an anomaly or a climatology; a user builds both, and the departure depends on the years averaged, the node, the product version and the averaging method. The AIRS record begins 31 August 2002 and carries the deep space manoeuvre of 23 September 2021, corrected only in the v7.0.9.3 and v7.0.10.0 files released in September 2025, and the 19 to 28 January 2026 gap; the OMI records begin 1 October 2004 and carry the row anomaly onset of June 2007 and the collection 4 reprocessings of 2024. The JPL manoeuvre report states its base period, 2006 to 2015, beside every anomaly it shows, and the version 7 guide says a count-weighted base grows a sampling bias in multi-year means. An anomaly quoted without its base period, version and node cannot be compared with another, and one whose base spans a break carries the break into every year."
tags: [airs, omi, anomaly, climatology, base-period, trend, breakpoint, deep-space-maneuver, row-anomaly, airs3stm, omno2d, omto3d, gesdisc, atmosphere]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T13:30:00Z }
severity: low
dataset: ../datasets/airs-l3-temperature-humidity.md
status: draft
stale_after: 2027-03-15
sources:
  - id: airs-dsm
    resource: https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/AIRS_DSM_Impact.pdf
    title: "Wang and Yue, 2025, Impact of Deep Space Maneuver (DSM, Sept. 23, 2021) on AIRS products and Post-DSM Corrections, JPL, 10 December 2025 (read 2026-09-15: the overview with Table 1 of the post-manoeuvre processing versions and their date ranges, the figure captions that compute every anomaly as the departure from the mean climatology of 2006 to 2015 and mark the manoeuvre date, and section 8 on the breakpoint test over November 2018 to September 2024 with the seasonal cycle removed by the monthly means of that window)"
  - id: airs-l3-ug
    resource: https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/V7_L3_User_Guide.pdf
    title: "Tian, Manning, Roman, Thrastarson, Fetzer and Monarrez, 2020, AIRS Version 7 Level 3 Product User Guide, version 1.0, April 2020, JPL (read 2026-09-15: section 1.1 on the variants' end dates, section 1.3 on the monthly product for trend analysis, section 1.5 on the nodes, and section 5.1 on the averaging change and its bias in multi-year climatological estimates)"
  - id: airs-dcr
    resource: https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/DC-Restore_Anomaly_Note_Final_260302_ADF1122.pdf
    title: "Pagano, Wang, Goodman and Sterzinger, 2026, AIRS DC Restore Anomaly, AIRS Design File Memo 1122, 2 March 2026 (read 2026-09-15: no daily level 3 between 19 and 28 January 2026, partial files on those dates, the January 2026 monthly missing the affected granules)"
  - id: ding-2020
    resource: https://doi.org/10.1175/JTECH-D-19-0129.1
    title: "Ding and others, 2020, Assessing the Impacts of Two Averaging Methods on AIRS Level 3 Monthly Products and Multiyear Monthly Means, Journal of Atmospheric and Oceanic Technology 37, 1027 to 1050 (record and abstract read on the Crossref registry 2026-09-15: the two averaging methods give different multi-year monthly means)"
  - id: cmr-airs3std
    resource: https://cmr.earthdata.nasa.gov/search/collections.json?short_name=AIRS3STD&provider=GES_DISC
    title: "CMR collection, UMM and granule records for AIRS3STD and AIRS3STM 7.0 (read 2026-09-15: the 2002-08-31 and 2002-09-01 starts, the processing versions in the first and newest granule names)"
  - id: cmr-omi
    resource: https://cmr.earthdata.nasa.gov/search/collections.json?short_name=OMNO2d&provider=GES_DISC
    title: "CMR collection, UMM and granule records for OMNO2d and OMTO3d 003 and 004 (read 2026-09-15: the 2004-10-01 starts, the collection 4 versions produced from October 2024 and October 2025, the last OMNO2d 003 granule of 2026-03-15)"
  - id: omno2-readme-v5
    resource: https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level3/OMNO2d.004/doc/README.OMNO2.c4v5.pdf
    title: "OMI Nitrogen Dioxide Algorithm Team, December 2024, OMNO2 README Document, Collection 4 Version 5.0 (read 2026-09-15: the December 2024 release on collection 4 radiances, and the limitations paragraph on trend analyses across anomaly-affected and unaffected periods)"
  - id: omi-dug
    resource: https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.2_ProductRequirements_Designs/README.OMI_DUG.pdf
    title: "OMI Team, 2012, OMI Data User's Guide, OMI-DUG-5.0 (read 2026-09-15: Table 12 of the row anomaly onset dates)"
  - id: merra2
    resource: ../datasets/merra-2.md
    title: "This bundle's MERRA-2 dataset concept: the reanalysis AIRS multi-year means are compared with, whose own record carries stream boundaries and observing-system steps, so an AIRS-minus-reanalysis anomaly has two base periods and two sets of breaks"
  - id: omi-dataset
    resource: ../datasets/omi-no2-and-ozone.md
    title: "This bundle's OMI level 3 dataset concept, which lists this trap"
  - id: dataset
    resource: ../datasets/airs-l3-temperature-humidity.md
    title: "This bundle's AIRS level 3 dataset concept, which lists this trap"
---

# An anomaly names its climatology period

**Mechanism.** An anomaly is a departure from a mean, and neither
product ships the mean: the AIRS level 3 files are daily and
monthly means of retrievals, the OMI level 3 files daily grids,
and any climatology or departure is built by the user from a chosen
set of years, one node, one product version and one averaging
method.[^airs-l3-ug][^omno2-readme-v5] The JPL report on the Aqua
deep space manoeuvre shows what the discipline looks like: every
anomaly time series it plots is captioned as the departure from the
mean climatology of 2006 to 2015, the manoeuvre date is marked, and
its breakpoint test names its own window, November 2018 to
September 2024, with the seasonal cycle removed by that window's
monthly means.[^airs-dsm] The records the base period is drawn from
carry breaks the documents date. AIRS: the record begins 31 August
2002; the HSB variant ends 5 February 2003 and the AMSU variant 24
September 2016; the manoeuvre of 23 September 2021 shifted the
focal plane and left a discontinuity in the version 7 water vapour
and near-surface temperature that the v7.0.7.0 files of 2022 still
carried and that the v7.0.9.3 and v7.0.10.0 reprocessing of
September 2025 reduced, so the same month can exist in two
processing versions with different means; the DC restore anomaly
left no daily files for 20 to 27 January 2026 and a January 2026
monthly file built from fewer granules; and the version 6 to
version 7 change replaced a count-weighted monthly mean, whose bias
the guide says grows in multi-year climatological estimates, with a
mean of daily means.[^cmr-airs3std][^airs-l3-ug][^airs-dsm][^airs-dcr][^ding-2020]
OMI: the records begin 1 October 2004; the row anomaly begins 25
June 2007 and widens in 2008 and 2009, changing the sampling of
every cell after it; OMNO2d moved to collection 4 radiances in
December 2024 (version 004, produced from October 2025, the 003
stream ending 15 March 2026) and OMTO3d to its version 004 in
October 2024 with 003 still in production.[^cmr-omi][^omi-dug][^omno2-readme-v5]
MERRA-2, the reanalysis these means are compared with, has its own
stream boundaries and observing-system steps, so an AIRS-minus-
reanalysis anomaly has two base periods and two sets of
breaks.[^merra2]

**Wrong-result mode.** Two anomalies of the same field on different
base periods differ by the difference of the two climatologies, and
because the record has breaks and a trend that difference is not a
single offset: a base of 2003 to 2012 and a base of 2006 to 2015
differ by the change over the years they do not share, a base that
includes 2021 to 2025 from the uncorrected v7.0.7.0 files carries
the manoeuvre's discontinuity into every anomaly year, and a base
that includes January 2026 carries a month whose mean rests on
fewer granules.[^airs-dsm][^airs-dcr] An AIRS anomaly compared with
a reanalysis anomaly on a 1991 to 2020 base, or with another
sounder's on its own years, reads the base-period difference as a
bias between instruments.[^merra2] An OMI anomaly whose base spans
2007 to 2009 averages years with different swath sampling, and the
NO2 team's trend caution applies to the climatology as much as to
the trend.[^omno2-readme-v5][^omi-dug] An AIRS anomaly built from a
version 6 monthly base and a version 7 monthly year, or a monthly
base rebuilt from daily files by the other averaging method,
carries the averaging difference the study measured.[^ding-2020][^airs-l3-ug]
An anomaly of one node compared with an anomaly of the other, or
with a daily-mean product, is the diurnal cycle's anomaly, not the
field's.[^airs-l3-ug] The severity is low because the error is a
known, computable difference a reader can remove once the base
period is stated, not a silent one; it becomes the row anomaly's or
the manoeuvre's own severity where the base spans them
unknowingly.[^airs-dsm][^omno2-readme-v5]

**Correct approach.** A quoted anomaly names its base period, the
product and version (with the processing version of the files
where the record has been reprocessed), the node, the averaging
method for any rebuilt monthly, and whether the base crosses a
documented break; a base period is chosen to lie within one
processing version and, for OMI, on one side of the row anomaly
onset or sampled with the surviving rows on both sides.[^airs-dsm][^omno2-readme-v5][^airs-l3-ug]
A comparison of anomalies from two products is made on a common
base period computed from each, or the two bases and their
difference are reported.[^merra2] The JPL report's practice, the
base period in the caption of every anomaly figure, is the form
this concept records.[^airs-dsm]

**Verification.** The manoeuvre report's figure captions carry the
2006 to 2015 base, its Table 1 the processing versions and dates,
and its section 8 the window of the breakpoint test; the DC restore
memo carries the January 2026 dates; the CMR granule records carry
the processing versions in the file names and the start dates; the
user's guide Table 12 carries the row anomaly onsets and the NO2
README the collection 4 release.[^airs-dsm][^airs-dcr][^cmr-airs3std][^cmr-omi][^omi-dug][^omno2-readme-v5]
The check a reader runs: the same AIRS3STM month of 2022 requested
from the archive in 2024 and in 2026 carries a different processing
version in its file name, and the global mean 600 hPa water vapour
anomaly on a 2006 to 2015 base differs between the two files by the
amount the report's figures show.[^airs-dsm][^cmr-airs3std] Both
dataset concepts list this trap.[^dataset][^omi-dataset]

[^airs-dsm]: Wang and Yue, 2025, Impact of Deep Space Maneuver on AIRS products and Post-DSM Corrections, JPL, 2025-12-10
[^airs-l3-ug]: Tian and others, 2020, AIRS Version 7 Level 3 Product User Guide, version 1.0
[^airs-dcr]: Pagano and others, 2026, AIRS DC Restore Anomaly, AIRS Design File Memo 1122, 2026-03-02
[^ding-2020]: Ding and others, 2020, Journal of Atmospheric and Oceanic Technology, doi:10.1175/JTECH-D-19-0129.1
[^cmr-airs3std]: CMR collection, UMM and granule records, AIRS3STD and AIRS3STM 7.0, read 2026-09-15
[^cmr-omi]: CMR collection, UMM and granule records, OMNO2d and OMTO3d 003 and 004, read 2026-09-15
[^omno2-readme-v5]: OMI NO2 Algorithm Team, 2024, OMNO2 README, collection 4 version 5.0
[^omi-dug]: OMI Team, 2012, OMI Data User's Guide, OMI-DUG-5.0
[^merra2]: This bundle's MERRA-2 dataset concept
[^omi-dataset]: This bundle's OMI level 3 dataset concept
[^dataset]: This bundle's AIRS level 3 dataset concept
