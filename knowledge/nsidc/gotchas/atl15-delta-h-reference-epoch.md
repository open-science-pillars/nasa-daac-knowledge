---
type: dataset-gotcha
spheres: [cryosphere]
title: "ATL15 delta_h is relative to the 1 January 2020 reference surface, and each lagged rate has its own window"
description: "delta_h is the height difference between the surface at each quarterly epoch and the ATL14 surface at the reference date 1 January 2020, so it is zero at that epoch and negative or positive on either side of it; the dhdt_lag groups are differences of two delta_h surfaces a fixed interval apart, time-stamped at the midpoint of their window. A trend that reads delta_h as change since the start of the record, or a dhdt value as the rate at its time stamp rather than over its window, is not the height change it claims."
tags: [icesat2, atl15, delta_h, dhdt, reference-epoch, time-axis, trend]
generated: { by: knowledge-seeder/claude, at: 2026-09-13T20:30:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-13T21:10:06Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/129 }
severity: medium
# medium: the product documents the epoch and the windows, and the
# error bites through a misread convention rather than through a
# silently wrong single-product statistic; no eval case is required.
dataset: ../datasets/icesat2-atl15.md
status: stable
stale_after: 2027-03-13
sources:
  - id: atl14-15-atbd
    resource: https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl14_atl15_atbd_v005.pdf
    title: "Smith and others, ICESat-2 ATBD for ATL14 and ATL15, release 005: the reference date 2020.0, the time reference in days since 1 January 2018, the definition of the lagged rates and their midpoint time stamps"
  - id: atl15-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/atl15-v005-userguide.pdf
    title: "ATL15 Version 5 user guide: the delta_h group, the dhdt_lag1 through dhdt_lag24 groups and their temporal resolutions, the time axis"
  - id: atl15-data-dict
    resource: https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl15_data_dict_v5.pdf
    title: "ATL15 data dictionary, version 5: delta_h described as height change relative to the datum (1 January 2020) surface"
  - id: dataset
    resource: ../datasets/icesat2-atl15.md
    title: "This bundle's ATL15 dataset concept, which lists this trap among the known issues"
---

# ATL15 delta_h is relative to the 1 January 2020 reference surface

**Mechanism.** The ATL14/ATL15 model is one reference surface (the
ATL14 DEM) at a reference date, plus a set of quarterly height-change
maps for dates before and after it that give the accumulated surface
height change between the ice surface and the DEM; the reference date
was chosen as a round number away from either end of the data so that
edge effects do not enter the DEM, and it is decimal year 2020.0,
midnight at the start of 1 January 2020, for releases 001 through
005, with the note that a later release might move it toward the
centre of the series.[^atl14-15-atbd] delta_h is therefore the height
difference with respect to that surface: the data dictionary describes
it as height change relative to the datum (1 January 2020) surface,
and the operators that build the solution remove the columns that fall
in the reference epoch so that the surface there is exactly
zero.[^atl15-data-dict][^atl14-15-atbd] The epochs before 2020 carry
negative time offsets from the reference, not negative heights; the
time axis of every group counts days since the ATLAS epoch (midnight
at the start of 1 January 2018), and the first epoch in the product is
the first quarter of 2019.[^atl15-user-guide][^atl14-15-atbd]
The dhdt_lag groups are not fits: each rate is the difference between
two delta_h surfaces the named interval apart (one quarter for lag1,
one year for lag4, two years for lag8, and so on to six years for
lag24) divided by that interval, and its time value is the midpoint of
the two epochs, so in the annual group the rate between 2019 and 2020
is stamped 2019.5; its ice_area is the minimum ice extent between the
first and last epochs of the window.[^atl14-15-atbd][^atl15-user-guide]

**Wrong-result mode.** Two readings go wrong. delta_h at the first
epoch is the height of early 2019 relative to 2020, a negative of the
2019 to 2020 change, and a series read as change since the record
began has the wrong sign convention for the first year and an offset
for every epoch after; the epoch at which the series crosses zero is
the reference date, not a moment of no change. A dhdt value read as
the instantaneous rate at its time stamp is an average over a window
whose length is the lag: the lag24 field stamped in 2022 is the mean
rate from 2019 to 2025, and a plot of a long-lag rate against time
smooths any event over its window. Fitting a line to delta_h to get a
rate duplicates what the lag groups already provide without their
covariance-based errors, and a rate quoted from dhdt_lag1 is a
quarter-to-quarter difference the ATBD describes as noisy and striped
where snowfall or melt is episodic, effects the ATBD expects to be much
less noticeable in annual or longer rates.[^atl14-15-atbd]

**Correct approach.** A height-change statement from ATL15 names the
two epochs it differences, or the lag group and the window its time
stamp centres, and states that delta_h is relative to the 1 January
2020 surface; a rate over a period comes from the lag group whose
window matches the period, with dhdt_sigma as its error, and a rate
over a period no lag group covers is the difference of the two delta_h
surfaces divided by their separation, stated as such and without a
covariance-based error.[^atl14-15-atbd][^atl15-user-guide] The time
axis is converted from days since 1 January 2018 to dates before any
epoch is named.[^atl15-user-guide]

**Verification.** The ATBD states the reference date, the time system
and the construction and time stamping of the lagged rates; the user
guide's table lists the lag groups and their temporal resolutions and
its temporal information section gives the time axis; the data
dictionary describes delta_h relative to the 1 January 2020
datum.[^atl14-15-atbd][^atl15-user-guide][^atl15-data-dict] All three
were read on 2026-09-13. A granule was not opened from the drafting
session (the Earthdata Cloud host was unreachable from it), so the
zero at the reference epoch is stated from the ATBD's construction and
not from a file. The dataset concept lists this trap among the
product's known issues.[^dataset]

[^atl14-15-atbd]: ATL14/ATL15 ATBD, release 005
[^atl15-user-guide]: ATL15 Version 5 user guide, NSIDC
[^atl15-data-dict]: ATL15 data dictionary, version 5
[^dataset]: This bundle's ATL15 dataset concept
