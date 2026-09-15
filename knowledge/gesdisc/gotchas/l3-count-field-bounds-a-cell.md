---
type: dataset-gotcha
spheres: [atmosphere]
title: "A level 3 cell is the average of however many retrievals of whatever quality fell in it, and the count or weight field is the only bound on that: an aggregate that drops it treats a one-retrieval cell as a full one, and the AIRS monthly mean changed its weighting between versions 6 and 7"
description: "AIRS level 3 stores beside every mean a count (_ct) of the level 2 retrievals that entered it and their standard deviation, plus TotalCounts, the retrievals that fell in the cell whether used or not; OMNO2d stores Weight, the sum of the area and overlap weights of the pixels averaged; OMTO3d stores nothing of the kind. A cell's value can rest on one retrieval or fifty, on near-nadir pixels one day and swath-edge pixels the next, and the retrievals differ in quality within the accepted range. The AIRS version 6 monthly mean weighted each day by its count and so favoured clear days, a bias the guide says grows in multi-year climatologies; version 7 averages the daily means without regard to count. A regional mean, a monthly rebuilt from dailies, or a per-cell trend that ignores the count or weight carries these differences as signal, and the count itself does not measure sampling bias."
tags: [airs, omi, level-3, count, weight, totalcounts, sampling, averaging, airs3std, airs3stm, omno2d, omto3d, gesdisc, atmosphere]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T13:30:00Z }
severity: medium
# medium, not high, although an unweighted aggregate runs silently: the
# count and Weight fields sit beside every mean in the file and the
# guides say what they bound, so the omission is visible to a reader who
# opens the file, and the averaging-method difference is documented and
# measured rather than hidden.
dataset: ../datasets/airs-l3-temperature-humidity.md
status: draft
stale_after: 2027-03-15
sources:
  - id: airs-l3-ug
    resource: https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/V7_L3_User_Guide.pdf
    title: "Tian, Manning, Roman, Thrastarson, Fetzer and Monarrez, 2020, AIRS Version 7 Level 3 Product User Guide, version 1.0, April 2020, JPL (read 2026-09-15: the introduction on quality indicators best and good and on the count map, section 2.2 on the per-field ensembles, the TqJoint grids and the total count, section 2.5 on the _ct and _sdev ancillaries and the yield, section 4.1 that the count does not characterise sampling biases, and section 5.1 on the change from averaging by observation to averaging by day)"
  - id: ding-2020
    resource: https://doi.org/10.1175/JTECH-D-19-0129.1
    title: "Ding, Savtchenko, Hearty, Wei, Theobald, Vollmer, Tian and Fetzer, 2020, Assessing the Impacts of Two Averaging Methods on AIRS Level 3 Monthly Products and Multiyear Monthly Means, Journal of Atmospheric and Oceanic Technology 37, 1027 to 1050 (record and abstract read on the Crossref registry 2026-09-15: averaging by observation gives days with more retrievals and regimes with better retrieval skill a disproportionate share, a warmer global surface, a slightly colder 500 hPa and a drier column than averaging by day, and the multi-year means of both are compared with MERRA-2)"
  - id: cmr-airs3stm
    resource: https://cmr.earthdata.nasa.gov/search/collections.json?short_name=AIRS3STM&provider=GES_DISC
    title: "CMR collection and UMM records for AIRS3STM and AIRS3STD 7.0 (read 2026-09-15: the monthly abstract's sentence that the means are the daily products weighted by input counts, carried from the version 6 description and contradicted by the version 7 guide, and the daily abstract's sentence that the count map can be used to generate custom multi-day maps)"
  - id: omno2-readme-v5
    resource: https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level3/OMNO2d.004/doc/README.OMNO2.c4v5.pdf
    title: "OMI Nitrogen Dioxide Algorithm Team, December 2024, OMNO2 README Document, Collection 4 Version 5.0 (read 2026-09-15: section 6 on OMNO2d, the weight equations, the Weight field as the sum of weights for combining files and regions, and the limitations on cells whose value matches no measurement, on swath-edge pixels, on precession and on looking at the weights when a periodicity appears)"
  - id: omno2d-filespec
    resource: https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.2_ProductRequirements_Designs/OMNO2d_FileSpec_V003.pdf
    title: "OMI NO2 Algorithm Team, 2013, OMNO2d File Specification, version 1.1 (read 2026-09-15: Table 6, the five fields with Weight as the statistical weight factor for spatial or temporal averages)"
  - id: omto3d-fs-v4
    resource: https://docserver.gesdisc.eosdis.nasa.gov/public/project/OMI/OMTO3d_004.fs
    title: "Leonard, 2024, OMTO3d file specification, PFS 1.0.12, 12 September 2024 (read 2026-09-15: the five fields, none of them a count or weight)"
  - id: omto3d-filespec-v3
    resource: https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.2_ProductRequirements_Designs/OMTO3d_FileSpec_V003.pdf
    title: "Leonard, 2013, OMTO3d file specification, PFS 1.0.7.1 (read 2026-09-15: the weighted average by fractional overlap and the same five fields)"
  - id: omi-dataset
    resource: ../datasets/omi-no2-and-ozone.md
    title: "This bundle's OMI level 3 dataset concept, which describes Weight and the absence of a count in OMTO3d and lists this trap"
  - id: dataset
    resource: ../datasets/airs-l3-temperature-humidity.md
    title: "This bundle's AIRS level 3 dataset concept, which describes the ancillaries and lists this trap"
---

# The count field bounds a level 3 cell

**Mechanism.** A level 3 cell is a statistic of the level 2
retrievals that fell in it and passed a screen, and both products
here say so in their own terms. In AIRS level 3 the value in a
field is the mean over all observations that fell in the 1 degree
cell and passed quality control, where the level 2 quality
indicators best (0) and good (1) are both accepted, so the ensemble
mixes two accepted qualities and differs between fields and levels;
beside every mean sit _ct, a 16-bit count of the level 2
observations in the mean, and _sdev, their standard deviation, and
beside every grid sits TotalCounts, the number of AIRS fields of
regard in the cell whether used or not, so that _ct over
TotalCounts is a yield.[^airs-l3-ug] The guide says in one sentence
what the count is not: "we provide the count of samples, but this
does not characterize sampling biases, which result from the
retrieval algorithm", the bias being height and species dependent
because the retrieval loses sensitivity under cloud.[^airs-l3-ug]
The monthly product's weighting changed between versions: version
6 averaged by observation, each day weighted by its count, which
favoured the less cloudy days because the retrieval fails above
about 70 percent cloud cover, and the guide says that sampling bias
"may become more significant and consistent in multi-year
climatological estimates"; version 7 averages by day, the plain
mean of the daily means, and the study the guide cites finds the
count-weighted method warmer at the surface, slightly colder at 500
hPa and drier in the column, with the average of daily means the
closer to MERRA-2.[^airs-l3-ug][^ding-2020] The CMR abstract of the
monthly collection still carries the version 6 sentence, that the
means are daily products weighted by input counts.[^cmr-airs3stm]
In OMNO2d the value of a cell is the area-weighted average of every
level 2 field of view overlapping it, each weighted by a term
linear in its area and by its fractional overlap, and the Weight
field is the sum of those weights, provided so that files and
regions can be combined as a weighted mean; the README says the
value in a cell "may not correspond to any one actual measurement",
that the 8 to 10 pixels farthest from nadir are large enough to
carry NO2 from some distance away, that the day-to-day shift of the
ground track within the orbit's repeat cycle (which the README calls
precession relative to the fixed grid) puts a fixed cell under large
pixels one day and small ones the next, and that
the weights are where to look when a series shows a
periodicity.[^omno2-readme-v5][^omno2d-filespec] OMTO3d is a weighted
average by fractional overlap as well, but its file carries five
fields and none of them is a count, a weight or a standard
deviation.[^omto3d-fs-v4][^omto3d-filespec-v3]

**Wrong-result mode.** A regional mean of an AIRS or OMNO2d field
that averages cells equally gives a cell resting on one retrieval
the same say as a cell resting on fifty, so a cloudy or
anomaly-thinned region's mean is driven by its sparsest cells, and
a daily series of that mean varies with how many retrievals each
day left in each cell as much as with the atmosphere.[^airs-l3-ug][^omno2-readme-v5]
A monthly or multi-day AIRS field rebuilt from the daily files
without the counts is the average by day, and rebuilt with them the
average by observation; neither is wrong, but the two differ in the
direction the study measured, and a user who compares a rebuilt
monthly with the archived AIRS3STM of the other version, or reads
the CMR sentence and weights by count to match a version 7 file
that is not count-weighted, carries the difference as a
discrepancy.[^airs-l3-ug][^ding-2020][^cmr-airs3stm] A per-cell
OMNO2d series shows a periodicity where the cell alternates between
nadir and swath-edge pixels as the ground track shifts, which reads as a signal until the
Weight field is plotted beside it.[^omno2-readme-v5] A cell with a
count of zero is fill, not zero, and a mean that treats fill as a
value or a count-zero level as a retrieval fails
silently.[^airs-l3-ug] Reading the count as a quality score is the
opposite error: the guide says the count does not characterise the
sampling bias, so a high-count cell in a persistently cloudy region
is well sampled among the clear scenes and biased toward them all
the same.[^airs-l3-ug] OMTO3d gives no handle on any of this
within the file; the bound has to come from the level 2 or level
2G inputs.[^omto3d-fs-v4]

**Correct approach.** An aggregate of level 3 cells carries the
count or the Weight through every step: a regional or temporal
mean is the count- or weight-weighted mean, or it is the plain mean
with the counts reported beside it and the choice stated, because
the two answer different questions; a rebuilt AIRS monthly names
which of the two averaging methods it used and which version's
archived monthly it is comparable with.[^airs-l3-ug][^ding-2020] A
comparison across fields or levels in AIRS uses the TqJoint grids,
whose single criterion gives every field the same ensemble, and
cells below a stated count are excluded with the threshold
named.[^airs-l3-ug] An OMNO2d series is read with its Weight, and
the combination of days or cells follows the README's weighted
formula.[^omno2-readme-v5] For OMTO3d the number of pixels behind a
cell is recovered from the level 2G product or stated as
unknown.[^omto3d-fs-v4][^omi-dataset]

**Verification.** Sections 2.5 and 4.1 of the AIRS guide define the
ancillaries and state the count's limit, section 5.1 states the
averaging change, and the study's abstract carries the direction
of the difference.[^airs-l3-ug][^ding-2020] Section 6 of the NO2
README defines Weight and the weighting equations and Table 6 of
the file specification lists it as the fifth field; the two OMTO3d
specifications list five fields without it.[^omno2-readme-v5][^omno2d-filespec][^omto3d-fs-v4][^omto3d-filespec-v3]
The check a reader runs on one AIRS daily file: Temperature_A_ct at
500 hPa ranges from 0 to well above 1 across a swath, TotalCounts_A
is at least as large everywhere, and an equal-weight regional mean
differs from the count-weighted one; on one OMNO2d file, Weight
along a swath edge is lower than at nadir.[^airs-l3-ug][^omno2-readme-v5]
Both dataset concepts list this trap.[^dataset][^omi-dataset]

[^airs-l3-ug]: Tian and others, 2020, AIRS Version 7 Level 3 Product User Guide, version 1.0
[^ding-2020]: Ding and others, 2020, Journal of Atmospheric and Oceanic Technology, doi:10.1175/JTECH-D-19-0129.1
[^cmr-airs3stm]: CMR collection and UMM records, AIRS3STM and AIRS3STD 7.0, read 2026-09-15
[^omno2-readme-v5]: OMI NO2 Algorithm Team, 2024, OMNO2 README, collection 4 version 5.0
[^omno2d-filespec]: OMI NO2 Algorithm Team, 2013, OMNO2d File Specification, version 1.1
[^omto3d-fs-v4]: Leonard, 2024, OMTO3d file specification, PFS 1.0.12
[^omto3d-filespec-v3]: Leonard, 2013, OMTO3d file specification, PFS 1.0.7.1
[^omi-dataset]: This bundle's OMI level 3 dataset concept
[^dataset]: This bundle's AIRS level 3 dataset concept
