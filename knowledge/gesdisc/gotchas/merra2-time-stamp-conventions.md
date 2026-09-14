---
type: dataset-gotcha
spheres: [atmosphere, hydrosphere]
title: "Time-averaged MERRA-2 collections are stamped at the centre of the interval and instantaneous ones on the hour: a join on the stamp alone is half an hour off"
description: "The hourly time-averaged collections (M2T1NXSLV, M2T1NXFLX and the other tavg1 files) stamp each hour's mean at 00:30, 01:30 and so on, the three-hourly averages at 01:30, 04:30 and so on, while the instantaneous collections (M2I1NXASM, M2I3NPASM) are stamped on the hour from 00:00. A join of an averaged flux with an instantaneous state by time stamp, by nearest hour or by array index pairs a mean over one interval with a snapshot at its edge, and a diurnal phase or a rate computed across the two is shifted by thirty minutes with no error raised."
tags: [merra-2, merra2, time-stamp, time-averaged, instantaneous, diurnal-cycle, gesdisc]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:30:00Z }
severity: medium
# medium: the offset is documented on every collection page and in
# the file specification, and it bites through a join across two
# collections rather than through a single collection read alone;
# no eval case is required at this severity.
dataset: ../datasets/merra-2.md
status: draft
stale_after: 2027-03-14
sources:
  - id: filespec
    resource: https://gmao.gsfc.nasa.gov/media/publications/zbly36ziNFDFbmYmvhQeVqPhUo/Bosilovich785.pdf
    title: "Bosilovich, Lucchesi and Suarez, 2016, MERRA-2: File Specification, GMAO Office Note No. 9 (version 1.1), read 2026-09-14: section 3 on instantaneous versus time-averaged products, the time dimension (minutes since the first time in the file) and the RangeBeginningTime global attribute, and each collection's frequency line"
  - id: gesdisc-m2t1nxslv
    resource: https://disc.gsfc.nasa.gov/datasets/M2T1NXSLV_5.12.4/summary
    title: "GES DISC collection page for M2T1NXSLV 5.12.4 (fetched 2026-09-14, text read from its CMR record: the data field is time-stamped with the central time of an hour starting from 00:30 UTC)"
  - id: gesdisc-m2t1nxflx
    resource: https://disc.gsfc.nasa.gov/datasets/M2T1NXFLX_5.12.4/summary
    title: "GES DISC collection page for M2T1NXFLX 5.12.4 (fetched 2026-09-14, text read from its CMR record: the same central-time stamping from 00:30 UTC)"
  - id: gesdisc-m2i1nxasm
    resource: https://disc.gsfc.nasa.gov/datasets/M2I1NXASM_5.12.4/summary
    title: "GES DISC collection page for M2I1NXASM 5.12.4 (fetched 2026-09-14, text read from its CMR record: the timestamp of a data field is on each hour starting from 00:00 UTC)"
  - id: readme
    resource: https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T1NXSLV.5.12.4/doc/MERRA2.README.pdf
    title: "GES DISC README Document for MERRA-2 Data Products (revised 2021-03-01), read 2026-09-14: every collection table's frequency line, 1-hourly from 00:30 UTC (time-averaged) against 1-hourly from 00:00 UTC (instantaneous), and daily from 00:30 UTC for the daily statistics"
  - id: dataset
    resource: ../datasets/merra-2.md
    title: "This bundle's MERRA-2 dataset concept, which states the stamping rule in its structure and lists this trap among the known issues"
---

# MERRA-2 time stamp conventions

**Mechanism.** MERRA-2 collections are either instantaneous or
time-averaged, never a mixture. Instantaneous collections hold
snapshots at synoptic and, for the hourly ones, every hour, stamped
on the hour: M2I1NXASM runs 00:00, 01:00 through 23:00 UTC, and the
three-hourly M2I3NPASM 00:00, 03:00 and so on. Time-averaged
collections hold a continuous sequence of averages over the stated
interval, stamped at the centre of the interval: the hourly
M2T1NXSLV and M2T1NXFLX at 00:30, 01:30 through 23:30, the
three-hourly averages at 01:30, 04:30 and so on; monthly files
average the calendar month, leap years counted.[^filespec][^gesdisc-m2t1nxslv][^gesdisc-m2i1nxasm]
Every collection page and every README table says which it is in one
line, and the daily statistics collection (M2SDNXSLV) is stamped
daily from 00:30.[^gesdisc-m2t1nxflx][^readme] Inside a file the time
coordinate is minutes since the first time in the file, and that
first time is the RangeBeginningTime global attribute, so the offset
is in the metadata and not in the variable's values.[^filespec]

**Wrong-result mode.** A flux from an averaged collection and a state
from an instantaneous one are both hourly, both 24 steps per daily
file, and both carry a time axis; a join by array index pairs the
00:30 mean with the 00:00 snapshot, a join by nearest time does the
same or picks the 01:00 snapshot for half the hours depending on tie
breaking, and a join that rounds the averaged stamp down to the hour
treats the 00:00 to 01:00 mean as the value at 00:00. A flux
integrated over a day is unaffected (the 24 averages tile the day
either way), but anything that pairs the two families is shifted by
thirty minutes: a bulk formula that combines an instantaneous wind
or temperature with an averaged flux, a rate of change of an
instantaneous state compared with an averaged tendency, a diurnal
phase read across the two, or a local-time conversion that puts the
half-hour stamp on the wrong side of a solar-time boundary. A
conversion of an hourly average to a local clock that ignores the
stamp puts the noon hour's mean at 12:30 in one series and at 12:00
in the other. None of this errors, and the two series agree to within
the natural hour-to-hour variability, which is why the offset is
easy to miss.[^filespec]

**Correct approach.** The time coordinate and its units, and the
RangeBeginningTime attribute, are read from each file rather than
assumed from the hour index; an averaged value stamped at t
represents the interval from t minus thirty minutes to t plus thirty
minutes, and an instantaneous value the instant t. A join pairs an
averaged value with the mean of the two instantaneous values that
bracket its interval, or interpolates the instantaneous series to the
half hour, or averages the instantaneous series over the same
interval; a daily cycle from an averaged collection places its bins
at the half hours; and any figure or table that mixes the two families
names the convention it used.[^filespec][^readme]

**Verification.** The rule is stated in section 3 of the file
specification and, per collection, in the frequency line of every
README table and the abstract of every collection record; on
2026-09-14 the CMR records for M2T1NXSLV and M2T1NXFLX read "the data
field is time-stamped with the central time of an hour starting from
00:30 UTC" and the record for M2I1NXASM "the timestamp of a data
field is on each hour starting from 00:00 UTC".[^filespec][^readme][^gesdisc-m2t1nxslv][^gesdisc-m2t1nxflx][^gesdisc-m2i1nxasm]
A reader can confirm on any pair of daily files: the first time value
of an averaged file resolves to 00:30 and of an instantaneous file to
00:00.[^filespec] The dataset concept states the rule and lists this
trap.[^dataset]

[^filespec]: Bosilovich, Lucchesi and Suarez, 2016, MERRA-2: File Specification, GMAO Office Note 9, version 1.1
[^gesdisc-m2t1nxslv]: GES DISC collection page and CMR record, M2T1NXSLV 5.12.4
[^gesdisc-m2t1nxflx]: GES DISC collection page and CMR record, M2T1NXFLX 5.12.4
[^gesdisc-m2i1nxasm]: GES DISC collection page and CMR record, M2I1NXASM 5.12.4
[^readme]: GES DISC README Document for MERRA-2 Data Products, revised 2021-03-01
[^dataset]: This bundle's MERRA-2 dataset concept
