---
type: dataset-gotcha
spheres: [biosphere, hydrosphere]
title: "A Level 3 chlorophyll composite is the mean of the observations that survived the flags in the period, with no count in the mapped file: a monthly mean is a mean of the sampled days, high latitudes have no winter value, cloudy seasons have few, and a climatology is re-cut every month"
description: "The mapped chlorophyll files are reprojected from binned Level 2 retrievals that passed a flag list (cloud and ice, high solar and sensor zenith, glint, straylight, atmospheric-correction failure, chlorophyll warnings and failures, coccolithophores) and the file's measure attribute is Mean: a monthly value in a cell is the mean of whatever clear, sunlit, unglinted, unflagged retrievals fell in that cell during the month, which can be one observation or thirty, and the mapped file carries no count, weight or day list to say which. Where the sun is too low there is no retrieval at all, so the high-latitude monthly series has no winter months; in a cloudy season the mean is of the few clear days, which are not a random sample of the month; instrument outages remove whole days from the daily record; and the monthly, seasonal and cumulative climatologies are recomputed as the record grows and named by their end date, so two files called the January climatology are two different means."
tags: [chlorophyll, chlor_a, level3, composite, monthly, climatology, binning, sampling, clouds, high-latitude, solar-zenith, flags, outage, modis, aqua, pace, oci, obdaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:30:00Z }
severity: medium
dataset: ../datasets/modis-aqua-l3-chlorophyll.md
status: draft
stale_after: 2027-03-14
sources:
  - id: modis-file
    resource: https://oceandata.sci.gsfc.nasa.gov/opendap/MODISA/L3SMI/2024/0601/AQUA_MODIS.20240601_20240630.L3m.MO.CHL.chlor_a.4km.nc.das
    title: "The attribute listing (OPeNDAP .das, metadata only) of the June 2024 MODIS-Aqua monthly 4 km file, read 2026-09-14: temporal_range month, measure Mean, the l2_flag_names list (ATMFAIL, LAND, HILT, HISATZEN, STRAYLIGHT, CLDICE, COCCOLITH, LOWLW, CHLWARN, CHLFAIL, NAVWARN, MAXAERITER, ATMWARN, HISOLZEN, NAVFAIL, FILTER, HIGLINT), the id naming the binned source file, a data_bins attribute, and the variables chlor_a, lat, lon and palette only; the listings of the 9 km cumulative climatology ending 2025-11-30 (temporal_range 24-year, created 2026-07-13) and the 9 km January climatology ending 2026-01-31 (temporal_range 23-year) and of the June 2024 PACE OCI monthly BGC file (measure Mean, no count variable) read the same way"
  - id: pace-v3-notes
    resource: https://oceancolor.gsfc.nasa.gov/files/reprocessing/PACE_OCI_V3_Release_Notes.pdf
    title: "PACE OCI V3 Processing Notes, April 2026, read in full 2026-09-14: Level 2 products binned and mapped into daily, 8-day and monthly composites, mapped products derived by reprojection of the binned data on a quasi-equal-area 4.6 km or 9.2 km integerized sinusoidal grid (appendix), data flagged at Level 2 masked in Level 3 (view zenith above 60 degrees, straylight, extreme glint, coccolithophores for the ocean color products), and, with the version 2 notes appended, the version 2 statement that view-zenith and straylight flagged data are masked in Level 3 products"
  - id: cmr-granules
    resource: https://cmr.earthdata.nasa.gov/search/granules.json?collection_concept_id=C3380709133-OB_CLOUD&temporal=2024-06-15T12:00:00Z,2024-06-15T12:00:01Z&page_size=500
    title: "CMR granule searches run 2026-09-14 on MODISA_L3m_CHL (C3380709133-OB_CLOUD): the granules whose period contains 2024-06-15, showing monthly climatology (MC) files for the same calendar month ending in 2024, 2025 and 2026, seasonal climatology (SC) and cumulative (CU) files ending at successive months, and the daily, 8-day, rolling 32-day, monthly, seasonal and annual composites at 4 km and 9 km"
  - id: atbd
    resource: https://oceancolor.gsfc.nasa.gov/files/atbd/atbd-obdaac-chlorophyll-a.pdf
    title: "Chlorophyll a, Algorithm Theoretical Basis Document version 1.1, 6 November 2023, read in full 2026-09-14: the validation criteria of sensor zenith below 60 degrees and solar zenith below 75 degrees, and the recommendation to use native-resolution rather than sub-sampled products for validation"
  - id: hu-2019
    resource: https://doi.org/10.1029/2019JC014941
    title: "Hu, Feng, Lee, Franz, Bailey, Werdell and Proctor, 2019, Improving satellite global chlorophyll a data products through algorithm refinement and data recovery, Journal of Geophysical Research: Oceans 124, 1524 to 1543 (registry record verified on Crossref and abstract read there 2026-09-14; the article was not read): the straylight masking scheme used to generate global chlorophyll maps relaxed from 7 by 5 to 3 by 3 pixels, with an average relative increase of 39 percent in data quantity for global oceans, so that data gaps can be filled"
  - id: alerts
    resource: https://www.earthdata.nasa.gov/data/alerts-outages/aqua-safe-mode-alert
    title: "Earthdata data alert, Aqua Safe Mode Alert, issued 2022-03-31 and resolved 2022-04-17 (an LP DAAC alert about the instrument, read 2026-09-14): MODIS produced no science data from 2022-03-31 and usable day data resumed on 2022-04-17; the Earthdata alerts list read the same day names Aqua MODIS data losses on 22, 27 and 28 July 2023 and 22 to 25 March 2024 (titles only)"
  - id: dataset
    resource: ../datasets/modis-aqua-l3-chlorophyll.md
    title: "This bundle's MODIS-Aqua Level 3 chlorophyll-a dataset concept: the periods, grids and climatology files the collection carries and the absence of a count layer; the PACE OCI dataset concept carries the daily, 8-day and monthly periods of that record"
---

# A Level 3 chlorophyll composite is the mean of the observations that survived the flags

**Mechanism.** The producer's Level 3 chain bins the Level 2
retrievals of a period onto a quasi-equal-area integerized sinusoidal
grid and reprojects the binned values onto the mapped grid; data
flagged at Level 2 are masked before binning, and the processing notes
name the masks for the current PACE versions (view zenith above 60
degrees, straylight, extreme glint, coccolithophores for the ocean
color products).[^pace-v3-notes] The MODIS-Aqua mapped file records
the same fact as an `l2_flag_names` list (atmospheric-correction
failure, land, high top-of-atmosphere radiance, high sensor zenith,
straylight, cloud or ice, coccolithophores, low water-leaving
radiance, chlorophyll warning and failure, navigation warning and
failure, aerosol iteration limit, atmospheric-correction warning, high
solar zenith, filter, high glint), an `id` naming the binned source
file, a `measure` of "Mean" and a `temporal_range` of month, and it
holds `chlor_a`, `lat`, `lon` and a palette and nothing else: no count
of contributing observations, no weight and no list of the days that
contributed.[^modis-file] The PACE BGC mapped file is the same:
`measure` "Mean", no count.[^modis-file] A monthly value in a cell is
therefore the mean of the clear, sunlit, unglinted, unflagged
retrievals that fell in that cell during the month, however many
there were. The straylight mask alone controls a large share of the
sample: the 2019 revision found that it could be relaxed from 7 by 5
to 3 by 3 pixels without loss of quality, with an average relative
increase of 39 percent in data quantity for the global ocean, so the
sampling of a composite is also a property of the processing
configuration (the ATBD does not state which mask R2022
uses).[^hu-2019] Where the sun is too low no
retrieval is attempted (the high solar zenith flag is in the mask
list, and the producer's own validation admits pairs only below 75
degrees solar zenith), so the high-latitude record has no values in
the dark months; where clouds persist, the month's mean is the mean of
its few clear days.[^modis-file][^atbd] Instrument outages remove
whole days: Aqua's safe mode from 2022-03-31 to usable data on
2022-04-17, and the data losses of 22, 27 and 28 July 2023 and 22 to
25 March 2024 named in the Earthdata alerts.[^alerts] The
climatologies are composites of the same kind over the whole record,
recomputed as it grows: the catalogue holds monthly climatology files
for one calendar month ending in 2024, 2025 and 2026 side by side,
seasonal and cumulative climatologies ending at successive months, and
the cumulative file ending 2025-11-30 carries `temporal_range`
"24-year" and was created in July 2026.[^cmr-granules][^modis-file]

**Wrong-result mode.** A monthly series read as thirty days of
observation treats a one-clear-day month and a fully sampled month as
equal points; a regional monthly mean averages cells sampled on
different days and different numbers of days, so its variability
contains the sampling. A trend in a high-latitude series fitted across
the calendar treats the winter months as missing at random when they
are missing by geometry every year, and a seasonal cycle there is the
cycle of the sunlit months only. In a cloudy season the clear days
are not a random sample of the month (clear-sky conditions select
particular weather), so a monthly mean is biased toward those
conditions, and the bias changes with the season and the region. An
anomaly computed against a climatology file downloaded at a different
time is an anomaly against a different mean, because the climatology
file with the same calendar month in its name has a different end
date and a different set of years.[^cmr-granules] A daily series that
crosses an outage reads the hole as missing data of the ordinary kind,
and a composite spanning it is a mean of fewer days.[^alerts] A
comparison of coverage or data quantity between records processed
under different straylight masks compares the masks.[^hu-2019]

**Correct approach.** A composite series is described with its
sampling: the count of contributing observations per cell, which the
mapped file does not carry and which therefore comes from the binned
file the mapped file names in its `id`, or from the daily files
counted per cell over the period.[^modis-file] A high-latitude series
is defined on the months that have values, with the winter absence
stated as the geometry it is, not as a gap; a cloudy-season mean is
reported with the number of days behind it; a series across an outage
names the outage. A climatology is cited by its file name with its
start and end dates, and an anomaly names the climatology file it was
computed against.[^cmr-granules] What a Level 3 monthly chlorophyll
value therefore is: the mean of the retrievals that passed the
producer's flags in that cell during that month, with the sampling
left to the binned file and the daily record.[^dataset]

**Verification.** The processing notes' appendix and Level 2 and
Level 3 sections are the producer's statement of the binning,
reprojection and masking, read in full on 2026-09-14; the four MODIS
file listings and the two PACE file listings read the same day
through OPeNDAP show the `measure`, `temporal_range`, `l2_flag_names`
and `id` attributes and the absence of a count variable; the CMR
granule listing read the same day shows the coexisting climatology
files; the Hu 2019 abstract, read on the Crossref registry record,
states the straylight change and the data-quantity figure; the alert
page and the alerts list state the outages.[^pace-v3-notes][^modis-file][^cmr-granules][^hu-2019][^alerts]
No source read states the number of observations behind any
particular composite, and this concept quotes none.

[^modis-file]: Attribute listings of MODIS-Aqua and PACE OCI L3m files, read through OPeNDAP on 2026-09-14
[^pace-v3-notes]: PACE OCI V3 Processing Notes, April 2026, with the version 2 notes appended
[^cmr-granules]: CMR granule searches on the MODISA_L3m_CHL collection, 2026-09-14
[^atbd]: Chlorophyll a ATBD version 1.1, OB.DAAC, 6 November 2023
[^hu-2019]: Hu and others, 2019, Journal of Geophysical Research: Oceans, doi:10.1029/2019JC014941
[^alerts]: Earthdata data alert, Aqua Safe Mode Alert, and the alerts list, 2026-09-14
[^dataset]: This bundle's MODIS-Aqua Level 3 chlorophyll-a dataset concept
