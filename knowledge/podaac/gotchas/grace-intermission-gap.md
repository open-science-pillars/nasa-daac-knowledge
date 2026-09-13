---
type: dataset-gotcha
spheres: [cryosphere, hydrosphere, geosphere]
title: "The GRACE to GRACE-FO gap: an eleven-month hole that a continuous-looking series hides, and every trend or acceleration fit across it inherits"
description: "GRACE stopped delivering science data in mid 2017 and GRACE-FO began in mid 2018, so the mascon record has no months between them; earlier battery-management months are missing too. A fit that treats the record as one continuous series puts any offset between the two missions, and the annual cycle the hole removes, into the trend and the acceleration, and nothing raises an error because the monthly files simply skip the missing epochs."
tags: [grace, grace-fo, gap, inter-mission, trend, acceleration, ice-sheet, ocean-mass, mascons]
generated: { by: knowledge-seeder/claude, at: 2026-09-13T20:00:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-13T18:39:32Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/125 }
severity: high
dataset: ../datasets/grace-fo-mascons.md
eval_case: grace-intermission-gap
status: stable
stale_after: 2027-03-13
sources:
  - id: nasa-tellus-grac-grfo-mascon-cri-grid-rl06
    resource: https://podaac.jpl.nasa.gov/dataset/TELLUS_GRAC-GRFO_MASCON_CRI_GRID_RL06.3_V4
    title: "PO.DAAC collection page: TELLUS_GRAC-GRFO_MASCON_CRI_GRID_RL06.3_V4 (the product's month list is the record of which epochs exist)"
  - id: grace-tellus
    resource: https://grace.jpl.nasa.gov/
    title: "GRACE Tellus project site: mission timeline and data availability"
  - id: landerer-2020
    resource: https://doi.org/10.1029/2020GL088306
    title: "Landerer and others, 2020, Extending the global mass change data record: GRACE Follow-On instrument and science data performance, Geophysical Research Letters (continuity of the two missions and the gap between them)"
  - id: velicogna-2020
    resource: https://doi.org/10.1029/2020GL087291
    title: "Velicogna and others, 2020, Continuity of ice sheet mass loss in Greenland and Antarctica from the GRACE and GRACE Follow-On missions, Geophysical Research Letters (how the gap was bridged for the ice sheets, and with what independent evidence)"
  - id: release-note
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/docs/GRACE_GRACE-FO_ReleaseNotes_JPL_MASCON.txt
    title: "JPL GRACE mascon solution release notes (RL06.3M version 4): the time-correlation procedure spanning GRACE and GRACE-FO, and the GRACE-FO uncertainty calibration"
  - id: months-rl06
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/docs/GRACE_GRACE-FO_Months_RL06.csv
    title: "GRACE and GRACE-FO RL06 month list (PO.DAAC): every calendar month since April 2002 with its solution index, the days used and the months with no coverage"
  - id: dataset
    resource: ../datasets/grace-fo-mascons.md
    title: "This bundle's mascon dataset concept, which lists the gap among the known issues"
---

# The GRACE to GRACE-FO gap

**Mechanism.** GRACE ended science operations in 2017 and GRACE-FO
launched in May 2018, with its first science months following the
in-orbit checkout; the mascon record therefore has no solutions for the eleven months
July 2017 through May 2018, and none for August and September 2018
either.[^landerer-2020][^months-rl06] Twenty months before the gap are
missing too (June and July 2002, June 2003, then from 2011 the
battery-management months: January and June 2011, May and October
2012, March, August and September 2013, February, July and December
2014, June, October and November 2015, April, September and October
2016, and February 2017), and some of the months that exist cover only
part of a calendar month.[^months-rl06][^grace-tellus] The product distributes one file per
solution epoch, so a series read from the files is a sequence of
existing months with the holes silently absent; the time axis is
irregular and nothing in the data marks where a mission ended.[^nasa-tellus-grac-grfo-mascon-cri-grid-rl06]

**Wrong-result mode.** Three fits go wrong on a series treated as
continuous. A linear trend across the gap absorbs any offset between
the two missions as if it were mass change (an inter-mission bias,
which the projects bound against independent mass estimates rather
than measure: the GRACE-FO team reports no evidence of one at the
level of those estimates, a bound, not a proof).[^landerer-2020] An acceleration
(a quadratic term) across an eleven-month hole is fit to two segments
that do not overlap; the hole falls near one end of most windows, so
the annual cycle it removes aliases into the quadratic. And a window
whose length is quoted in months from the number of files is shorter
in calendar time than it claims. None of this errors; the fit returns
numbers with formal uncertainties that assume the sampling is regular.

**Correct approach.** Read the epochs from the files' time stamps,
never from their count, and state the gap and the missing months in
any trend or acceleration statement. Fit with a model that carries the
annual and semi-annual cycles as terms and with the gap acknowledged
as a hole, never interpolated. For a window that spans the gap, say
how the inter-mission continuity was handled and cite the independent
evidence for it: for the ice sheets, the continuity analysis that
fills the gap with the mass budget (input-output) method and finds the
two missions consistent across it at continental and regional scales
is the reference,[^velicogna-2020] and for the global record the
GRACE-FO performance paper's comparison against independent
estimates.[^landerer-2020] For a window that ends or starts near the
gap, prefer a window that does not cross it and say why. Quote the
formal error and the systematic terms (leakage, GIA, the low-degree
replacements) separately; a formal error alone under-states a trend
across the gap.

**Verification.** The product's month list shows the missing epochs
directly (the collection page and the Tellus site record the
timeline).[^nasa-tellus-grac-grfo-mascon-cri-grid-rl06][^grace-tellus]
The two cited papers document the gap, the two missions' continuity
and the bridging evidence for the ice sheets.[^landerer-2020][^velicogna-2020]
The dataset concept lists the gap among the product's known issues.[^dataset]
Live checks on 2026-09-13 from a session with the NASA hosts allowed: the
CMR record for the collection (concept C3195527175-POCLOUD, version
RL06.3Mv04, DOI 10.5067/TEMSC-3JC634) reports one granule covering
2002-04-16 through 2026-07-16, so the months that exist and the months
that do not are read from the file's time axis, not from the catalog;
the product's month list, read the same day, is the record behind the
counts above (solution 163 is June 2017, the next, 164, is June 2018,
and August and September 2018 are marked as missing);[^months-rl06]
the release note states that the time-correlation procedure of the
solution spans both missions and that the GRACE-FO months carry an
additional calibrated uncertainty for the missing GRACE-D
accelerometer, which is the product's own account of continuity, not
an independent check on it;[^release-note] both papers' records were
verified against the Crossref registry the same day (title, authors,
journal, year) and their abstracts read there: Landerer and others
2020 states the eleven-month gap and reports no inter-mission bias at
the level of independent estimates over June 2018 through December
2019, and Velicogna and others 2020 fills the gap with the mass budget
method and finds the series consistent across it; the journal pages
themselves sit behind a bot check.

[^nasa-tellus-grac-grfo-mascon-cri-grid-rl06]: PO.DAAC collection page: TELLUS_GRAC-GRFO_MASCON_CRI_GRID_RL06.3_V4
[^grace-tellus]: GRACE Tellus project site: mission timeline and data availability
[^landerer-2020]: Landerer and others, 2020, Geophysical Research Letters, doi:10.1029/2020GL088306
[^velicogna-2020]: Velicogna and others, 2020, Geophysical Research Letters, doi:10.1029/2020GL087291
[^dataset]: This bundle's mascon dataset concept
[^release-note]: JPL GRACE mascon solution release notes, RL06.3M version 4
[^months-rl06]: GRACE and GRACE-FO RL06 month list, PO.DAAC
