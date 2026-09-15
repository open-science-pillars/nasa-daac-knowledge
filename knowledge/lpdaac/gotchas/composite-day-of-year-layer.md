---
type: dataset-gotcha
spheres: [biosphere, geosphere]
title: "A MOD13 16-day composite is not an image of one day: each pixel is the observation the constrained-view maximum value rule selected, its date is in the composite day of the year layer, adjacent pixels can come from different days and geometries, and the date in the file name is the period's date, not the observation's"
description: "For each 16-day period MOD13Q1 and MOD13A1 keep one observation per pixel, chosen since Collection 6 from at most two candidates in the eight-day precomposited surface reflectance by comparing the two highest NDVI values and keeping the smaller view zenith angle, with the plain highest NDVI as backup. The day that observation was acquired is stored per pixel in the composite day of the year layer (int16, 1 to 366, fill -1), and its view zenith, sun zenith and relative azimuth angles in three more layers; the guide states that adjacent pixels can originate from different days with different geometries and residual contamination, and the file name carries the period's date, not the observation's. A script that places every value at the period's nominal date, differences two composites as a change over 16 days, treats a spatial gradient as a surface feature, or compares the composite with a field measurement on the file's date reads the sampling as the signal, and nothing raises an error because the layer is optional to open."
tags: [mod13, mod13q1, mod13a1, modis, composite, day-of-year, cv-mvc, maximum-value-composite, phenology, lpdaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T17:50:00Z }
severity: medium
dataset: ../datasets/mod13-vegetation-indices.md
status: draft
stale_after: 2027-03-15
sources:
  - id: vi-guide
    resource: https://lpdaac.usgs.gov/documents/621/MOD13_User_Guide_V61.pdf
    title: "MODIS Vegetation Index User's Guide, version 3.10, September 2019, read 2026-09-15: section 2 (Collection 6 ingests eight-day precomposited surface reflectance; Terra and Aqua eight days out of phase), section 5.1 (the compositing data flow of Figure 4 with at most two candidates, the constrained-view maximum value composite with n set to 2, the maximum value composite backup, and the statement that all compositing methods result in spatial discontinuities because disparate days can be chosen for adjacent pixels), Table 1 (the composite day of the year and the three angle layers), section 7.2 (the monthly product lacks the day of year layer because it is built from composites) and the FAQ (the vegetation products are composites of the best pixels from 16 consecutive days)"
  - id: q1-page
    resource: https://lpdaac.usgs.gov/products/mod13q1v061/
    title: "LP DAAC product page for MOD13Q1 v061, read 2026-09-15: the algorithm chooses the best available pixel value from all the acquisitions of the 16-day period by low clouds, low view angle and the highest NDVI or EVI; the variables table with the composite day of the year as int16, 1 to 366, fill -1, and the file name convention with its example day 193"
  - id: a1-page
    resource: https://lpdaac.usgs.gov/products/mod13a1v061/
    title: "LP DAAC product page for MOD13A1 v061, read 2026-09-15: the same description and the file name example with day 193"
  - id: mod15-page
    resource: https://lpdaac.usgs.gov/products/mod15a2hv061/
    title: "LP DAAC product page for MOD15A2H v061, read 2026-09-15: the file name example with day 209, and the description of the eight-day product as the best pixel from the eight days"
  - id: gpp-guide
    resource: https://lpdaac.usgs.gov/documents/972/MOD17_User_Guide_V61.pdf
    title: "MOD17 User's Guide for Collection 6.1, March 2021, read 2026-09-15 for section 1.3.1 (the eight-day summations are named for the first day included in the period) and section 2.3 (the MOD15A2H compositing selects the maximum FPAR across the eight days and the same day supplies the LAI, so the MOD17 model assumes leaf area constant within the period)"
  - id: mod13
    resource: ../datasets/mod13-vegetation-indices.md
    title: "This bundle's MOD13 concept, with the compositing description, the layer table and the quality fields"
  - id: mod15
    resource: ../datasets/mod15-lai-fpar.md
    title: "This bundle's MOD15 concept, whose eight-day composite carries no day of year layer"
  - id: mod11-clear-sky
    resource: mod11-clear-sky-and-view-time.md
    title: "This bundle's MOD11 gotcha, where the eight-day product is a simple average of the clear daily values with a view time layer, the averaging counterpart of the selection described here"
---

# The composite day of the year layer

**Mechanism.** A MOD13Q1 or MOD13A1 file is one value per pixel for a
16-day period, and the guide describes how the value is chosen. Since
Collection 6 the input is the eight-day precomposited Level-2G surface
reflectance, in which the surface reflectance algorithm has already
filtered each pixel's observations by quality, cloud and viewing
geometry, so that the 16-day period offers at most two candidate
observations per pixel; the guide's data flow figure labels the stack
"maximum 2 starting C6.0".[^vi-guide] The main rule, the
constrained-view maximum value composite, compares the n observations
with the highest NDVI, n being 2, and keeps the one with the smaller
view zenith angle, closest to nadir; the backup is the maximum value
composite of the AVHRR tradition, the observation with the highest
NDVI.[^vi-guide] The product page states the same rule as low clouds,
low view angle and the highest NDVI or EVI.[^q1-page] The guide then
states the consequence: all compositing methods inevitably result in
spatial discontinuities, because disparate days can always be chosen
for adjacent pixels over the 16-day period, so adjacent pixels may
originate from different days with different sun-pixel-sensor
geometries and different atmospheric and residual cloud or smoke
contamination.[^vi-guide]

The file records which observation was kept. The composite day of the
year layer is an int16 with valid range 1 to 366 and fill -1, the day
of year the selected observation was acquired, and the view zenith,
sun zenith and relative azimuth angle layers carry that observation's
geometry in hundredths of a degree ([this bundle's MOD13
concept](../datasets/mod13-vegetation-indices.md)).[^vi-guide][^q1-page][^mod13]
The file name carries one day of year, which the product page calls
the acquisition date; the examples on the product pages are day 193
for both products, and the MOD17 guide says of its own eight-day
sums that they are named for the first day of the period. The sources
read here do not state the MOD13 convention in so many words, and 193
is 1 plus twelve times 16, the form a period named by its first day
would take on a cycle that starts on day 1.[^q1-page][^a1-page][^gpp-guide]
The monthly MOD13A3 product has no day of the year layer because it is
built from the 16-day composites by a weighted average.[^vi-guide]
Terra and Aqua are processed eight days out of phase, so the two
streams together sample every eight days, each still a selection over
16.[^vi-guide]

The pattern is general to the composited land products, in two forms.
MOD13 selects one observation and records its date; MOD15A2H selects
the day of maximum FPAR across its eight days and carries the LAI of
the same day, and records no date, so the MOD17 model that consumes it
assumes leaf area constant within the period ([this bundle's MOD15
concept](../datasets/mod15-lai-fpar.md)).[^gpp-guide][^mod15-page][^mod15]
MOD11A2, by contrast, averages the clear daily values of its eight
days and carries the days used as flags and the view time as an
average, the averaging counterpart of this selection ([the MOD11
clear-sky gotcha](mod11-clear-sky-and-view-time.md)).[^mod11-clear-sky]

**Wrong-result mode.** A time series built from the 16-day files with
each value placed at the period's nominal date, the file day or its
midpoint, is a series whose true sample times differ from the assumed
ones by up to 15 days in either direction, by a different amount in
each pixel and each period. A phenology metric read from it (the day
of green-up, the day of peak, the length of the season) inherits that
offset, and the offset is not random: the rule keeps the greener of the
candidates, so the selected day is whichever of them had the higher
NDVI rather than a representative day of the period, and the series is
not a period mean of anything.[^vi-guide] A difference of two consecutive
composites read as a change over 16 days can be a change over one day
or over 31, depending on which observations the two periods kept in
that pixel. A comparison with a flux tower, a field campaign or a
weather record on the file's date compares the index with conditions
the pixel was not observed under. A spatial gradient or an edge in a
single composite that coincides with a change in the day of the year
layer is a compositing seam, two acquisition dates and geometries
side by side, and the guide names this outcome as inevitable; a
classifier or an edge detector reads it as a land surface
feature.[^vi-guide] A script that averages the reflectance layers or
the angle layers across a window treats a set of different
observation dates and geometries as one. None of this raises an
error: the day of the year layer is one of twelve, optional to open,
and the series looks evenly spaced.[^vi-guide][^q1-page]

**Correct approach.** The composite day of the year layer is read with
the index and used as the time coordinate of each pixel's value, with
the fill -1 excluded, so a time series is a set of irregularly spaced
samples per pixel and a phenology fit is made against the recorded
dates rather than the period dates.[^vi-guide][^q1-page] A comparison
with a dated ground record is made on the pixel's recorded day, and
the view zenith, sun zenith and relative azimuth layers of that
observation are the geometry to state beside it, since the rule keeps
the smaller view angle of two candidates rather than a nadir
view.[^vi-guide] A change between composites is a change between two
recorded dates, and a spatial analysis carries the day of the year
layer as a covariate or checks its discontinuities against the edges
it finds. The selection rule is stated with any statistic derived from
the composite: the value is the highest-NDVI candidate of a filtered
pair, not a mean over the period.[^vi-guide][^mod13]

**Verification.** On any 16-day tile a histogram of the composite day
of the year layer spans the period rather than one value, and a map
of it shows patches whose boundaries coincide with edges in the NDVI
and angle layers.[^vi-guide] For one pixel across a year, the
differences between consecutive recorded days are not all 16, while
the file names step by exactly 16, and the recorded day sits inside
the 16-day window that starts on the file's day of year in every
period; a recorded day outside that window would contradict the
period naming inferred above and is a finding to record.[^vi-guide][^q1-page]

[^vi-guide]: MODIS Vegetation Index User's Guide, version 3.10, September 2019, sections 2, 5.1, 7.2, Table 1, Figure 4 and the FAQ
[^q1-page]: LP DAAC product page, MOD13Q1 v061, read 2026-09-15
[^a1-page]: LP DAAC product page, MOD13A1 v061, read 2026-09-15
[^mod15-page]: LP DAAC product page, MOD15A2H v061, read 2026-09-15
[^gpp-guide]: MOD17 User's Guide for Collection 6.1, March 2021, sections 1.3.1 and 2.3
[^mod13]: this bundle's MOD13 concept
[^mod15]: this bundle's MOD15 concept
[^mod11-clear-sky]: this bundle's MOD11 gotcha on clear-sky sampling and view time
