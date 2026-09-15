---
type: dataset-gotcha
spheres: [geosphere, biosphere]
title: "MOD11 is a clear-sky product observed at a varying local time: every value is one clear moment, a daily or eight-day mean is a mean of the clear moments that existed, and the observation hour is a layer to read, not a constant"
description: "MOD11A1 holds a land surface temperature only where the MODIS cloud mask found the pixel clear and a 32 day temporal screen kept it; everywhere else the temperature is the fill value 0 and the quality byte says not produced due to cloud. The value that exists was observed at the local solar time in Day_view_time or Night_view_time, which varies by cell and by day, at the view zenith angle in the angle layer, and above 30 degrees latitude it is one observation chosen among several by view angle in the guide's account, or an average in the product page's. MOD11A2 is the simple average of whatever MOD11A1 values existed in eight days, with the days that contributed flagged bit by bit in Clear_sky_days, and its view time is the average of the times used. A mean built from these fields is therefore a clear-sky mean at a mixture of hours and angles, and a script that reads it as the mean surface temperature of the period at a fixed overpass time attributes the sampling to the surface."
tags: [mod11, mod11a1, mod11a2, modis, terra, land-surface-temperature, clear-sky, view-time, view-angle, cloud, lpdaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T13:40:00Z }
severity: high
dataset: ../datasets/mod11-land-surface-temperature.md
eval_case: mod11-clear-sky-and-view-time
status: draft
stale_after: 2027-03-15
sources:
  - id: user-guide
    resource: https://lpdaac.usgs.gov/documents/715/MOD11_User_Guide_V61.pdf
    title: "Collection-6 MODIS LST Products Users' Guide (Wan, June 2019) with the Collection 6.1 cover note, read 2026-09-15: section 2.1 (the clear-sky constraints and the 32 day temporal screening), 3.1 (the gridding, the multiple-observation rule above 30 degrees), 3.2 (local solar time, the UTC data day, the view angle sign), Table 9, Table 10 (QAPercentNotProducedCloud), 3.5 and Table 13 (the mandatory QA bits), 4.1 and 4.2 (the simple average, the averaged view time and angle, Clear_sky_days as uint8 with range 1 to 255 and no scale), section 10.1 (the monthly product flags the days with validated LSTs in each bit of a 32-bit integer) and Table 3 (Error_LST blind to cloud contamination)"
  - id: atbd
    resource: https://lpdaac.usgs.gov/documents/119/MOD11_ATBD.pdf
    title: "MODIS LST Algorithm Theoretical Basis Document, version 3.3, April 1999 (Wan), read 2026-09-15: section 2.2, the MODIS LST product based on thermal infrared data will only be available in clear sky conditions; section 2.1, the 1 K specification holds under clear-sky conditions"
  - id: a1-page
    resource: https://lpdaac.usgs.gov/products/mod11a1v061/
    title: "LP DAAC product page for MOD11A1 v061, read 2026-09-15: above 30 degrees latitude some pixels may have multiple observations meeting the clear-sky criteria and the pixel value is then the average of all qualifying observations; the variables table with the view time and angle layers, their fills and scales, and the clear-sky coverage layers"
  - id: a2-page
    resource: https://lpdaac.usgs.gov/products/mod11a2v061/
    title: "LP DAAC product page for MOD11A2 v061, read 2026-09-15: each pixel value is a simple average of all the corresponding MOD11A1 pixels collected within the eight-day period; Clear_sky_days and Clear_sky_nights in the variables table"
  - id: mod11
    resource: ../datasets/mod11-land-surface-temperature.md
    title: "This bundle's MOD11 concept, with the layer table, the quality bits and the uncertainty statement"
  - id: day-night
    resource: mod11-day-and-night-are-different.md
    title: "This bundle's gotcha on the separate daytime and nighttime fields, which each carry their own view time and coverage"
---

# MOD11 is a clear-sky product observed at a varying local time

**Mechanism.** The land surface temperature in MOD11 comes from
thermal infrared radiances, and the algorithm document states the
consequence plainly: the product will only be available in clear sky
conditions.[^atbd] The retrieval in the swath product is constrained
to pixels the MOD35 cloud mask calls clear at 95 per cent confidence
or better; the daily tiles accept 95 per cent over land at or below
2000 m, 66 per cent over land above 2000 m and 66 per cent over lakes,
and then remove cloud-contaminated values with constraints on the
temporal variation of clear-sky LST over 32 days, so the set of
pixels with a value is the clear set as the mask and the screen
define it, and it changes every day.[^user-guide] A pixel without a
value holds the fill 0 in LST_Day_1km or LST_Night_1km, and its
quality byte's mandatory bits read 10, not produced due to cloud
effects, or 11, not produced for other reasons; the granule metadata
count these as QAPercentNotProducedCloud and
QAPercentNotProducedOther over the whole tile.[^user-guide]

The value that does exist is a single moment. The daily product maps
each day's clear-sky swath pixels to the sinusoidal grid, and each
cell records when it was seen: Day_view_time and Night_view_time are
the local solar time of the observation in tenths of an hour, local
solar time being UTC plus the cell's longitude divided by 15, and
Day_view_angl and Night_view_angl the view zenith angle with a sign
that says whether MODIS looked from the east or the west.[^user-guide][^a1-page]
The time is a layer with a valid range of 0 to 240 tenths of an hour
because it varies; the data day in the file name is UTC and the local
solar data day of a cell can be the day before or after it.[^user-guide]
Above 30 degrees latitude a cell can be seen clear more than once in
a day. The guide says the Collection 6 daily value is then one
observation, the clear-sky LST at the smaller view zenith angle
unless the one at the larger angle is warmer by at least 2 K; the
product page says the value is the average of all qualifying
observations. The two documents differ on this point and both are
recorded as read.[^user-guide][^a1-page] Whichever holds, the view
angle of what was kept varies from cell to cell up to the 65 degree
edge of the swath.[^user-guide]

The eight-day product inherits all of it. MOD11A2 is the simple
average of the MOD11A1 values that exist in the eight days, with
Clear_sky_days and Clear_sky_nights recording which days contributed;
its view time and view angle are averages over the days used.[^user-guide][^a2-page]
Those two layers are bytes with a valid range of 1 to 255 and no
scale, described by the guide as the days in clear-sky conditions with
valid LSTs and by the product page as bit fields; the guide says of
the monthly product that the days with validated LSTs are flagged in
each bit of a 32-bit integer, and the eight-day byte follows the same
design with one bit per day, so the number of contributing days is
the number of set bits, not the stored value. Which bit is the first
day of the period is not stated in the sources read.[^user-guide][^a2-page]
A cell clear on one day and a cell clear on all eight both hold a
value in the same layer, with the flags in another. The daytime and
nighttime fields are each sampled this way on their own
([the day and night gotcha](mod11-day-and-night-are-different.md)).[^day-night]

**Wrong-result mode.** A monthly, seasonal or annual mean built from
these layers is a mean of the clear observations that existed, and a
script that reports it as the mean land surface temperature of the
period has attributed the sampling to the surface: cells and seasons
differ in how often they were clear, so the mean is taken over
different fractions of the period in different places, and a change
in cloudiness between years appears as a change in temperature. An
anomaly series from MOD11A2 mixes changes in the number of set bits
of Clear_sky_days with changes in the surface. A script that reads
the Clear_sky_days byte as the number of days, or filters on it as if
it were, weights a cell clear on the eighth day alone (a high bit set)
as if it had been clear on many days. A comparison against a station record at a
fixed hour, or against a model field at a fixed time step, is made
at the wrong hour wherever the code assumes one overpass time instead
of reading Day_view_time, and the assumed hour is wrong by a
different amount in each cell of a tile because local solar time
moves with longitude and the observation moves with the
orbit.[^user-guide] A mean that includes the fill value 0, which is a
valid uint16 and scales to 0 K, is pulled toward zero by exactly the
cloudy pixels the product excluded.[^user-guide] A quality screen that
keeps the mandatory bits 00 only, without reading the temperature
alongside, keeps fill pixels too, because the guide notes a quality
byte of 0 is meaningful only where the LST is valid.[^user-guide] None
of this raises an error: the fill is a number, the coverage layer is
optional to read and looks like a count, and the time layer looks
like a constant to a script that never opens it.

The accuracy figure that travels with the product, 1 K, is itself
stated under clear-sky conditions, and the swath product's error
layer does not account for cloud contamination.[^atbd][^user-guide]

**Correct approach.** A value is used only where the temperature is
not fill and the mandatory quality bits read 00 or, by choice, 01,
with the temperature and the quality byte read together. The mean
over a period is stated as a clear-sky mean and carries the number of
clear observations per cell from Clear_day_cov and Clear_night_cov in
the daily product, or the number of set bits in Clear_sky_days and
Clear_sky_nights in the eight-day product, as a weight or as a
minimum for a cell to be reported; the eight-day byte is decoded bit
by bit, never used as a count, and the bit-to-day assignment is stated
as unconfirmed unless the file specification has been read. A comparison with a timed record uses the cell's own
Day_view_time or Night_view_time, converted from local solar time
with the cell's longitude, and the view angle layer where angle
matters; on the eight-day product both are averages. Above 30 degrees
latitude the daily value is treated as one observation chosen or
averaged by the rule the two documents give differently, and a reader
who needs to know which reads the granule rather than assuming.[^user-guide][^a1-page][^mod11]

**Verification.** On any tile the fraction of fill in LST_Day_1km
equals the sum of QAPercentNotProducedCloud and
QAPercentNotProducedOther in the granule metadata to within the
rounding of a percentage.[^user-guide] A histogram of Day_view_time
over the tile spans a range of hours rather than one value, and the
number of set bits in Clear_sky_days on the eight-day tile varies
across the tile in any cloudy season, while the stored bytes include
values above eight that no count of days could reach.[^user-guide][^a2-page] A mean computed with
and without the fill value differs, and the one with it is lower.

[^user-guide]: Collection-6 MODIS LST Products Users' Guide, June 2019, sections 2.1, 3.1, 3.2, 3.5, 4.1 and 4.2
[^atbd]: MODIS LST Algorithm Theoretical Basis Document, version 3.3, April 1999, sections 2.1 and 2.2
[^a1-page]: LP DAAC product page, MOD11A1 v061, read 2026-09-15
[^a2-page]: LP DAAC product page, MOD11A2 v061, read 2026-09-15
[^mod11]: this bundle's MOD11 concept
[^day-night]: this bundle's gotcha on the day and night fields
