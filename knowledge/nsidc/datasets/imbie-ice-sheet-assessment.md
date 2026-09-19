---
type: dataset
spheres: [cryosphere]
title: "IMBIE 2023: the reconciled multi-method assessment of Greenland and Antarctic ice sheet mass balance, 1992 to 2020"
description: "The third Ice Sheet Mass Balance Inter-comparison Exercise combines 50 satellite estimates into one reconciled rate of mass change per ice sheet region over 1992 to 2020, reported for Greenland, the whole Antarctic ice sheet and its West, East and Peninsula regions, in six periods and over the full record, each with its own uncertainty. The estimates are grouped by technique (altimetry, gravimetry and the input-output method), aggregated inside each group and then combined as an error-weighted mean over the groups available at each epoch. This concept states what the assessment reports and what it does not: it is the published anchor a run of this bundle's ice sheet mass balance closure is read against, not an independent measurement of the closure's terms."
tags: [imbie, ice-sheet-mass-balance, assessment, intercomparison, greenland, antarctica, altimetry, gravimetry, input-output, reconciled, sea-level, cryosphere]
generated: { by: knowledge-seeder/claude, at: 2026-09-19T05:30:00Z }
resource: https://doi.org/10.5194/essd-15-1597-2023
version: "the third IMBIE assessment, published 20 April 2023 as Otosaka and others, Earth System Science Data 15, 1597 to 1616 (doi 10.5194/essd-15-1597-2023); the reconciled series it produces are archived at doi 10.5285/77B64C55-7166-4A06-9DEF-2E400398E452 (IMBIE Team, 2021) and the aggregation software at doi 10.5281/zenodo.7342481 (Otosaka and others, 2022). Article read in full and all three DOIs resolved on 2026-09-19; it supersedes the 2018 Antarctic and 2020 Greenland assessments, which it extends by 3 and 4 years to a common 1992 to 2020 record"
status: draft
stale_after: 2027-03-19
sources:
  - id: otosaka-2023
    resource: https://doi.org/10.5194/essd-15-1597-2023
    title: "Otosaka and 67 others, 2023, Mass balance of the Greenland and Antarctic ice sheets from 1992 to 2020, Earth System Science Data 15, 1597 to 1616: the third IMBIE assessment, its reconciled rates, its uncertainties and its technique groups"
  - id: imbie-pdf
    resource: https://essd.copernicus.org/articles/15/1597/2023/essd-15-1597-2023.pdf
    title: "The article as published by Copernicus (CC BY 4.0), read in full on 2026-09-19: the abstract, section 2 on the input estimates, section 3 on the aggregation equations, section 4 on the technique comparison, Table 2 and section 5.2 on the limitations"
  - id: crossref-otosaka
    resource: https://api.crossref.org/works/10.5194/essd-15-1597-2023
    title: "Crossref registry record for doi 10.5194/essd-15-1597-2023, read 2026-09-19: title, 68 authors led by Otosaka, journal Earth System Science Data, volume 15, pages 1597 to 1616, issued 2023-04-20"
  - id: imbie-data
    resource: https://doi.org/10.5285/77B64C55-7166-4A06-9DEF-2E400398E452
    title: "The reconciled time series the assessment publishes (IMBIE Team, 2021), two comma-separated files per region; the DOI resolved on 2026-09-19 to the UK Polar Data Centre record GB/NERC/BAS/PDC/01477 and is not a Crossref record"
  - id: imbie-software
    resource: https://doi.org/10.5281/zenodo.7342481
    title: "The IMBIE assessment software used to produce the published dataset (Otosaka and others, 2022); the DOI resolved on 2026-09-19"
  - id: gotcha-groups
    resource: ../gotchas/assessment-method-groups-are-not-independent.md
    title: "Bundle gotcha: the three technique groups share models, satellite records and, in one direction, their observations, and they do not cover the same ice"
  - id: gotcha-basins
    resource: ../gotchas/ice-sheet-boundaries-and-drainage-basins.md
    title: "Bundle gotcha: a per-region number names the basin set it used; the assessment carries both basin definitions"
  - id: computation
    resource: ../computations/ice-sheet-balance.md
    title: "Bundle attested computation: the ice sheet mass balance closure whose runs are read against this assessment"
---

# IMBIE 2023 reconciled ice sheet mass balance assessment

**Identity.** The Ice Sheet Mass Balance Inter-comparison Exercise
(IMBIE) is a community assessment that collects mass balance estimates
made by different groups from different satellite techniques, puts them
on a common footing and combines them into one reconciled series per
ice sheet region. The third assessment covers 1 January 1992 to
31 December 2020 for Greenland and Antarctica together, extending the
2018 Antarctic and 2020 Greenland assessments by 3 and 4 years, and it
is published as a paper with its data and its aggregation code carrying
their own DOIs.[^otosaka-2023][^imbie-pdf][^imbie-data][^imbie-software]
The article's record (title, its 68 authors led by Otosaka, journal,
volume, pages and year) was verified against the Crossref registry on
2026-09-19, and the article itself was reachable and read in full the
same day.[^crossref-otosaka][^imbie-pdf]
It rests on 50 satellite-based estimates: 27 for Greenland (8 from
altimetry, 16 from gravimetry, 3 from the input-output method) and 23
for Antarctica (6 altimetry, 16 gravimetry, 1 input-output), drawing on
14 satellite missions, with estimates from all three techniques
available between 2003 and 2018 in Greenland and between 2002 and 2018
in Antarctica.[^imbie-pdf] The regions are the common definitions of
the Greenland ice sheet (GrIS), the Antarctic ice sheet (AIS) and its
West (WAIS), East (EAIS) and Peninsula (APIS) parts; participants were
free to use either of two drainage basin sets, the ICESat-slope basins
of Zwally and others (27 in Antarctica, 19 in Greenland) or the
velocity-drawn basins of Rignot and others (18 and 6), which differ by
0.1 percent of Antarctic and 1.1 percent of Greenland ice sheet extent,
and the assessment combines trends regardless of which was
used.[^imbie-pdf][^gotcha-basins] The published output is the reconciled
annual rate of mass balance and the cumulative mass change, with
uncertainties, as two files per region, one in gigatonnes and one in
millimetres of sea level equivalent.[^imbie-pdf][^imbie-data]

**What it reports for each ice sheet over each period.** Table 2 of the
assessment gives the rate of mass change in gigatonnes per year for
each region over six periods and over the whole record, each period
running from 1 January of the first year to 31 December of the last.
The rate is given first and its uncertainty in
parentheses.[^imbie-pdf][^otosaka-2023]

| Period | GrIS | AIS | WAIS | EAIS | APIS |
|---|---|---|---|---|---|
| 1992 to 1996 | -35 (29) | -70 (40) | -37 (19) | -27 (33) | -7 (11) |
| 1997 to 2001 | -48 (36) | -19 (39) | -42 (19) | 21 (32) | 2 (11) |
| 2002 to 2006 | -180 (39) | -62 (41) | -64 (20) | 21 (34) | -20 (11) |
| 2007 to 2011 | -280 (38) | -130 (45) | -129 (23) | 19 (36) | -21 (12) |
| 2012 to 2016 | -213 (40) | -150 (43) | -131 (21) | -13 (35) | -6 (13) |
| 2017 to 2020 | -257 (42) | -115 (55) | -94 (25) | 0 (47) | -21 (12) |
| 1992 to 2020 | -169 (16) | -92 (18) | -82 (9) | 3 (15) | -13 (5) |

Over the 29 years the two ice sheets together contributed 21.0
millimetres to global mean sea level, with the loss rising from 105
gigatonnes per year over 1992 to 1996 to 372 gigatonnes per year over
2016 to 2020, and Antarctica alone lost 2671 gigatonnes with an
uncertainty of 530, raising sea level by 7.4 millimetres with an
uncertainty of 1.5.[^imbie-pdf] Greenland's annual rates vary widely
inside these period means, from a loss of 86 gigatonnes in 2017 to a
record 444 in 2019.[^imbie-pdf] Over the periods when all three
techniques are available the assessment also reports a separate
reconciled rate: minus 221 with an uncertainty of 22 gigatonnes per
year for Greenland over 2003 to 2018, and minus 115 with an uncertainty
of 24 for Antarctica over 2003 to 2019.[^imbie-pdf]

**The method groups.** Every contributed estimate is assigned to one of
three groups by the satellite technique behind it. Altimetry measures
surface elevation change and becomes a mass change either by
prescribing a density or by a model-based correction for firn
compaction, after a correction for bedrock motion; the assessment
describes it as the technique with the finest spatial resolution, of
the order of a hundred square kilometres, reaching back to the early
1990s. The input-output method combines satellite ice velocities with
an ice thickness to compute discharge and subtracts it from a regional
climate model's surface mass balance, at drainage basin resolution.
Gravimetry measures the change in Earth's gravity field and becomes a
mass change after model corrections for glacial isostatic adjustment
and for leakage from the ocean and from land hydrology, at a resolution
of the order of a hundred thousand square kilometres and only since
2002.[^imbie-pdf] The aggregation is three steps: each submitted series
is turned into a monthly rate by a 36 month sliding weighted
least-squares fit; the rates inside each group are averaged with
inverse-error weights, the group error being the quadrature sum of the
member errors divided by the square root of the number of members; and
the groups are combined at each epoch as an error-weighted mean over
the one to three groups then available, the reconciled error being the
quadrature sum of the group errors divided by the square root of the
number of groups.[^imbie-pdf] Only two surface mass balance models,
RACMO and MAR, stand behind the input-output estimates
included.[^imbie-pdf]

**What it says about their independence.** The assessment calls
altimetry, gravimetry and the input-output method "three independent
satellite techniques" and both of its error equations reduce the
uncertainty by the square root of a count on that basis, inside a group
and again across the groups.[^imbie-pdf] It does not claim that the
three groups observe the same ice or rest on separate corrections, and
it records the opposite in several places: the peripheral glaciers and
ice caps are included by the input-output estimates, excluded by the
altimetry estimates and inseparable from the ice sheet for gravimetry,
which the assessment names as a source of systematic bias between the
techniques to be removed in future rounds; glacial isostatic adjustment
models correct both the gravimetry and the altimetry estimates; and the
assessment asks for intercomparisons of the surface mass balance and
glacial isostatic adjustment models precisely because their choice
moves the estimates.[^imbie-pdf] It also states plainly where the
groups disagree: across all ice sheets the input-output estimate is the
most negative and the altimetry the most positive, except in East
Antarctica, where the three disagree on even the sign of the change
with a maximum difference of 105 gigatonnes per year, uncertainty 33,
between the input-output and gravimetry rates.[^imbie-pdf] This bundle
carries that reading as its own gotcha.[^gotcha-groups]

## Uncertainty

Every rate above carries the uncertainty the assessment computed for
it, and those uncertainties are the quadrature sums described under the
method groups, not measurement errors in the sense a single instrument
would report.[^imbie-pdf] Three properties of them matter to anyone
comparing a number against this anchor. First, they shrink with the
number of contributed estimates rather than with any demonstration that
those estimates are independent, by the square root of the member count
inside a group and again by the square root of the group count across
groups; in Antarctica one group, the input-output method, has a single
member.[^imbie-pdf] Second, the spread between the groups is not inside
them: over their common period the three Greenland technique rates lie
within a standard deviation of 19 gigatonnes per year of each other
against a reconciled uncertainty of 22, while in Antarctica the spread
is 79 against a reconciled uncertainty of 24, four times larger than in
Greenland, and by region the spreads are 54 at EAIS, 18 at WAIS and 16
at APIS.[^imbie-pdf] Third, the assessment reports two different
uncertainties for the same headline number: the abstract gives the
Greenland 1992 to 2020 rate as 169 with an uncertainty of 9 gigatonnes
per year, while Table 2 gives minus 169 with an uncertainty of
16.[^imbie-pdf] Within a technique group the members also disagree by
more than one might expect: the Greenland gravimetry solutions differ
by a median of 36 gigatonnes per year with a standard deviation of 30
over 2012 to 2014, and the Antarctic ones by a median of 41 over 2004
to 2014, and the assessment states that the small number of
input-output estimates, one in Antarctica, limits its ability to
attribute within-group differences to method, corrections or auxiliary
data.[^imbie-pdf] Of the individual annual rates contributed, 96
percent at GrIS, 83 at AIS, 83 at APIS, 76 at EAIS and 81 at WAIS fall
inside the reconciled uncertainty range.[^imbie-pdf]

## What this concept does not carry

The assessment is a published comparison, not a product this bundle
reads: no loader, no data root and no receipt here reads the archived
IMBIE series, and the rates above are quoted from the paper's Table 2
and its section 4 rather than recomputed.[^imbie-pdf][^imbie-data] The
assessment reports no per-basin time series, which its own roadmap
names as future work, so a basin-scale number has no anchor
here.[^imbie-pdf] It ends in 2020, so a window that runs past 2020 has
no period in this table to be read against, and the 2017 to 2020 row is
four years long where the others are five.[^imbie-pdf] The closure this
bundle attests compares its own gravimetric and firn-corrected
altimetric rates against these numbers and owns every number its
receipts produce; this concept owns only what the assessment
published.[^computation]

[^otosaka-2023]: Otosaka and others, 2023, Earth System Science Data, doi:10.5194/essd-15-1597-2023
[^imbie-pdf]: The assessment as published by Copernicus, read in full 2026-09-19
[^crossref-otosaka]: Crossref registry record for the assessment, read 2026-09-19
[^imbie-data]: The archived reconciled series, IMBIE Team 2021
[^imbie-software]: The IMBIE aggregation software, Otosaka and others 2022
[^gotcha-groups]: This bundle's gotcha on the technique groups
[^gotcha-basins]: This bundle's gotcha on ice sheet boundaries and drainage basins
[^computation]: This bundle's attested ice sheet mass balance closure
