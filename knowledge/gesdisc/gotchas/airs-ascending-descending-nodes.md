---
type: dataset-gotcha
spheres: [atmosphere]
title: "AIRS ascending and descending grids are 1:30 PM and 1:30 AM local time with their own ensembles and their own 24-hour windows: an average of the two is a two-sample diurnal estimate, not a daily mean, and a daily file is not a calendar day"
description: "Every AIRS level 3 file holds separate ascending (_A, sub-satellite point moving south to north, 1:30 PM local equator crossing, daytime outside the polar zones) and descending (_D, 1:30 AM, night-time) grids, each with its own count, standard deviation and quality-controlled ensemble, and each daily grid covers a nominal 24 hours offset from midnight: 1:30 PM to 1:30 PM UTC for descending and 1:30 AM to 1:30 AM for ascending, starting at the antimeridian. The guide separates the nodes to keep the diurnal signal. A mean of the two fields is the average of one afternoon and one early-morning sample weighted by whatever counts each node had, not the day's mean; a mean of one node is that local time only; and a daily file joined to a calendar-day series from another product is up to half a day off."
tags: [airs, aqua, airs3std, airs3stm, ascending, descending, local-time, diurnal-cycle, daily-mean, gesdisc, atmosphere]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T13:30:00Z }
severity: medium
dataset: ../datasets/airs-l3-temperature-humidity.md
status: draft
stale_after: 2027-03-15
sources:
  - id: airs-l3-ug
    resource: https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/V7_L3_User_Guide.pdf
    title: "Tian, Manning, Roman, Thrastarson, Fetzer and Monarrez, 2020, AIRS Version 7 Level 3 Product User Guide, version 1.0, April 2020, JPL (read 2026-09-15: section 1.3 on the nominal 24-hour periods per node and the westward gridding from the antimeridian, section 1.5 on the nodes and their equator crossing times, section 2.2 on the six grids, the _A and _D suffixes and the sentence that the separation mitigates the suppression of the diurnal signal, and section 2.4 on the per-node grid start and end time attributes)"
  - id: cmr-airs3std
    resource: https://cmr.earthdata.nasa.gov/search/collections.json?short_name=AIRS3STD&provider=GES_DISC
    title: "CMR collection and UMM records for AIRS3STD 7.0 (read 2026-09-15: the abstract's 24-hour period for either the descending, 1:30 AM, or ascending, 1:30 PM, orbit, and the dateline handling so that points in a grid box are coincident in time)"
  - id: gesdisc-airs3std
    resource: https://disc.gsfc.nasa.gov/datasets/AIRS3STD_7.0/summary
    title: "GES DISC collection page for AIRS3STD 7.0 (fetched 2026-09-15, text read from its CMR record)"
  - id: ding-2020
    resource: https://doi.org/10.1175/JTECH-D-19-0129.1
    title: "Ding and others, 2020, Assessing the Impacts of Two Averaging Methods on AIRS Level 3 Monthly Products and Multiyear Monthly Means, Journal of Atmospheric and Oceanic Technology 37, 1027 to 1050 (record and abstract read on the Crossref registry 2026-09-15: the day-to-day orbit shift changes the counts a cell receives, which is what weights any count-weighted average of the nodes)"
  - id: dataset
    resource: ../datasets/airs-l3-temperature-humidity.md
    title: "This bundle's AIRS level 3 dataset concept, which describes the grids and lists this trap"
---

# AIRS ascending and descending nodes

**Mechanism.** The AIRS level 3 products are separated into the
ascending and descending portions of the orbit, where the words
refer to the direction of the sub-satellite point: ascending moves
from the southern to the northern hemisphere with an equatorial
crossing at 1:30 PM local time, descending from north to south at
1:30 AM, and outside the polar zones these are daytime and
night-time.[^airs-l3-ug][^cmr-airs3std] Each file carries both as
separate HDF-EOS grids (ascending, descending, and the TqJoint and
MW_Only pairs), every field taking the suffix _A or _D, and each
grid has its own count, standard deviation and TotalCounts, because
the level 2 retrievals that pass quality control at 1:30 PM are not
the ones that pass at 1:30 AM; the guide's stated reason for the
separation is that it "mitigates the suppression of the diurnal
signal in the data".[^airs-l3-ug] The daily grid's time window is
per node and not a calendar day: the descending grid covers 1:30 PM
to 1:30 PM UTC (centred on the 1:30 AM crossing) and the ascending
grid 1:30 AM to 1:30 AM, the gridding starting at the antimeridian
and progressing westward with the orbits so that points in one cell
are coincident in time and the two parts of a scan line that cross
the dateline go to different days' files; the per-node start and end
times are file attributes (AscendingGridStartTimeUTC and the
three others).[^airs-l3-ug][^cmr-airs3std] The monthly file keeps
the nodes apart the same way.[^airs-l3-ug]

**Wrong-result mode.** A "daily mean" formed as the average of the
_A and _D fields is the mean of two samples of the diurnal cycle,
one in the early afternoon and one before dawn, so for any quantity
with a diurnal cycle (surface skin and air temperature over land,
low-level humidity, cloud) it is neither the daytime nor the
night-time value nor the 24-hour mean, and the error has the sign
and size of the cycle's asymmetry about those two hours; weighting
the two by their counts makes the result drift with whichever node
had more clear-sky retrievals that day.[^airs-l3-ug][^ding-2020] A
series built from one node alone is a 1:30 PM or a 1:30 AM series,
and a comparison with a reanalysis daily mean, a station's daily
mean, or another sounder's local time reads the difference in local
time as bias.[^airs-l3-ug] A join of the daily file to a calendar
day assumes a midnight-to-midnight window the file does not have:
the descending grid of the file dated D holds observations from
1:30 PM UTC on D minus 1, and a cell east of the antimeridian and
one west of it in the same file can be almost a day apart in
observation time, by design.[^airs-l3-ug] Near the poles the
day-night reading of the nodes fails, because both nodes see the
polar day or the polar night.[^airs-l3-ug]

**Correct approach.** An AIRS level 3 quantity is named with its
node, and a statement about the day is a statement about 1:30 PM
or 1:30 AM local time; where one number per day is needed the two
nodes are reported separately or combined with the diurnal cycle
stated as an assumption, and the counts of both nodes are carried so
that a cell empty in one node is not read as a half-day
mean.[^airs-l3-ug] A comparison with a reanalysis or a model samples
it at the node's local time (the 1:30 PM and 1:30 AM hours of the
hourly collections), and a comparison between nodes is a
day-minus-night difference, which the guide's example maps of
surface skin temperature show as a large signal over
land.[^airs-l3-ug] A calendar-day series uses the per-node grid
start and end attributes to place each daily file in
time.[^airs-l3-ug]

**Verification.** Sections 1.3, 1.5 and 2.2 of the user guide carry
the node definitions, the 24-hour windows and the diurnal-signal
sentence, and the CMR abstract repeats the crossing times and the
per-node period.[^airs-l3-ug][^cmr-airs3std][^gesdisc-airs3std] The
check a reader runs on one daily file: SurfSkinTemp_A minus
SurfSkinTemp_D over a desert is large and positive, and the file's
AscendingGridStartTimeUTC and DescendingGridStartTimeUTC attributes
differ by twelve hours and neither reads midnight.[^airs-l3-ug] The
dataset concept lists this trap.[^dataset]

[^airs-l3-ug]: Tian and others, 2020, AIRS Version 7 Level 3 Product User Guide, version 1.0
[^cmr-airs3std]: CMR collection and UMM records, AIRS3STD 7.0, read 2026-09-15
[^gesdisc-airs3std]: GES DISC collection page and CMR record, AIRS3STD 7.0
[^ding-2020]: Ding and others, 2020, Journal of Atmospheric and Oceanic Technology, doi:10.1175/JTECH-D-19-0129.1
[^dataset]: This bundle's AIRS level 3 dataset concept
