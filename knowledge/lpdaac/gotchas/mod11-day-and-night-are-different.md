---
type: dataset-gotcha
spheres: [geosphere, biosphere]
title: "MOD11 day and night fields are different quantities: two observations at different hours and angles, with their own quality bytes and clear-sky coverage layers, and neither is a daily temperature"
description: "Every MOD11A1 and MOD11A2 tile carries LST_Day_1km and LST_Night_1km as separate layers, each from its own overpass, with its own QC byte, its own view time and view angle and its own clear-sky coverage layer (a count on the daily product, one flag bit per day on the eight-day product). The daytime retrieval uses one coefficient set and the nighttime another for bare soil, the simulations behind them span different surface-to-air temperature ranges, and the guide records that the day and night view angles at a location are usually quite different on the same day. A cell can be clear at one and cloudy at the other. A script that reads one field as the land surface temperature, averages the two into a daily mean, or applies the day quality byte to the night field, has combined two samplings into a number that neither observation supports."
tags: [mod11, mod11a1, mod11a2, modis, terra, land-surface-temperature, day, night, diurnal, lpdaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T13:40:00Z }
severity: medium
dataset: ../datasets/mod11-land-surface-temperature.md
status: draft
stale_after: 2027-03-15
sources:
  - id: user-guide
    resource: https://lpdaac.usgs.gov/documents/715/MOD11_User_Guide_V61.pdf
    title: "Collection-6 MODIS LST Products Users' Guide (Wan, June 2019) with the Collection 6.1 cover note, read 2026-09-15: section 2.1 (the separate daytime and nighttime coefficient sets for hot and warm bare soil and the simulation ranges), Table 5 (the swath DayNightFlag), section 3.2 and Table 9 (the twelve daily layers), Table 10 (DayNightFlag Both on the tile), Table 13 (QC_Day and QC_Night), section 4.2 and Table 14 (the eight-day layers), and section 5 (the day/night algorithm's note that day and night view angles usually differ)"
  - id: a1-page
    resource: https://lpdaac.usgs.gov/products/mod11a1v061/
    title: "LP DAAC product page for MOD11A1 v061, read 2026-09-15: daytime and nighttime surface temperature bands provided with associated quality control, observation times, view zenith angles and clear-sky coverages; the variables table"
  - id: a2-page
    resource: https://lpdaac.usgs.gov/products/mod11a2v061/
    title: "LP DAAC product page for MOD11A2 v061, read 2026-09-15: the same daytime and nighttime pairing on the eight-day product, with Clear_sky_days and Clear_sky_nights"
  - id: mod11
    resource: ../datasets/mod11-land-surface-temperature.md
    title: "This bundle's MOD11 concept, with the layer table and the quality bits"
  - id: clear-sky
    resource: mod11-clear-sky-and-view-time.md
    title: "This bundle's gotcha on the clear-sky sampling and the view time, which applies to each of the two fields on its own"
---

# MOD11 day and night fields are different quantities

**Mechanism.** The swath product MOD11_L2 is produced for every
daytime and every nighttime swath, and each granule's DayNightFlag
says which it is.[^user-guide] The daily tile gathers both into one
file whose DayNightFlag reads Both, as two sets of layers: LST_Day_1km
with QC_Day, Day_view_time, Day_view_angl and Clear_day_cov, and
LST_Night_1km with QC_Night, Night_view_time, Night_view_angl and
Clear_night_cov.[^user-guide][^a1-page] The eight-day tile keeps the
same pairing with Clear_sky_days and Clear_sky_nights as the flags
of the days and nights that contributed, one bit per day rather than
a count.[^user-guide][^a2-page] Nothing is shared between the pair
except the grid and the two emissivity layers.

The two observations are made at different local solar times and,
the guide records, usually at quite different view zenith angles at a
given location on the same day; each has its own clear-sky test, so a
cell can hold a daytime value and a nighttime fill or the
reverse.[^user-guide] The retrieval itself is not one function of
radiance: for the hot and warm bare soil zone between 38 degrees south
and 49.5 degrees north there are two separate sets of split-window
coefficients, one for daytime and one for nighttime, because the
range of diurnal variation in LST over the seasons at bare soil sites
is very wide; the radiative transfer simulations behind the
coefficients set the surface minus air temperature range to 8 to 29 K
for daytime and -10 to 4 K for nighttime, and the air temperature
range to 280 to 325 K by day and 275 to 305 K by night.[^user-guide]
The quality bytes are likewise two: QC_Day describes the daytime LST
and QC_Night the nighttime one, each with the mandatory bits, the
data quality bits and the error classes for that observation
alone.[^user-guide]

**Wrong-result mode.** A script that opens LST_Day_1km as "the land
surface temperature" reports the surface near its daytime maximum
under clear sky and nothing else, and one that opens the night layer
reports a different quantity under the same name. An average of the
two layers presented as a daily mean temperature is the midpoint of
two clear-sky moments whose hours differ by cell and whose view angles
differ, taken only where both exist; where one is fill, an average
that does not test the fill is halved or pulled toward 0 K, and one
that drops the cell biases the mean toward cells clear at both
times.[^user-guide] A mask built from QC_Day and applied to
LST_Night_1km keeps night pixels the night byte marks as not produced
and drops good ones. A time series that concatenates day and night
values as consecutive samples carries the day to night difference as
signal. A comparison of the daytime field with a nighttime station
reading, or with a model temperature at a single hour, compares
different times of day, and the daytime and nighttime coefficients
mean the two fields do not even share a retrieval error
budget.[^user-guide] Each of these runs without error, because the two
layers have the same shape, type, scale and fill.

**Correct approach.** The daytime and nighttime fields are kept as
two products of the same tile, each read with its own quality byte,
its own view time and angle and its own coverage layer, and each
named as day or night in whatever is reported. A quantity that needs
both, such as a day to night difference, is computed only where both
are valid and is stated as the difference between the two clear-sky
observations at their two recorded hours, not as a diurnal range. A
period mean is a daytime clear-sky mean or a nighttime clear-sky
mean, never an unlabelled one ([the clear-sky and view time
gotcha](mod11-clear-sky-and-view-time.md)).[^clear-sky][^mod11]

**Verification.** On any tile the histograms of Day_view_time and
Night_view_time occupy different hours of the day, the two view angle
layers differ cell by cell, and the mandatory bits of QC_Day and
QC_Night differ in which cells they mark as not produced, so the sets
of valid cells in the two temperature layers are not the same
set.[^user-guide] Clear_day_cov and Clear_night_cov, or Clear_sky_days
and Clear_sky_nights, differ across the tile.[^user-guide][^a2-page]

[^user-guide]: Collection-6 MODIS LST Products Users' Guide, June 2019, sections 2.1, 3.2, 3.5, 4.2 and 5, Tables 5, 9, 10, 13 and 14
[^a1-page]: LP DAAC product page, MOD11A1 v061, read 2026-09-15
[^a2-page]: LP DAAC product page, MOD11A2 v061, read 2026-09-15
[^mod11]: this bundle's MOD11 concept
[^clear-sky]: this bundle's gotcha on clear-sky sampling and view time
