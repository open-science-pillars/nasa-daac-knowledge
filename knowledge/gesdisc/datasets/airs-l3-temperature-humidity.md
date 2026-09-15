---
type: dataset
spheres: [atmosphere]
title: "AIRS version 7 level 3 temperature and water vapour: the daily and monthly 1 degree grids (AIRS3STD, AIRS3STM) as ascending and descending fields on fixed pressure levels with a count and a standard deviation beside every mean"
description: "The Atmospheric Infrared Sounder on Aqua, gridded by the AIRS science team into the version 7 level 3 standard products at GES DISC: a daily file (AIRS3STD) and a calendar-month file (AIRS3STM) on a 1 by 1 degree grid from 31 August 2002 to the present, each holding separate ascending (1:30 PM local, daytime) and descending (1:30 AM, night-time) grids, temperature on 24 standard pressure levels from 1000 to 1 hPa, water vapour mixing ratio and relative humidity on 12 levels from 1000 to 100 hPa and 12 layers bounded by the standard levels from 1000 to 70 hPa, surface skin and air temperature, total column water vapour, a forecast surface pressure, and for every mean a count of the level 2 retrievals that entered it and their standard deviation. No error field ships; the count and the standard deviation are what stand in, and the guide says the count does not characterise sampling bias."
tags: [airs, aqua, airs3std, airs3stm, level-3, temperature, water-vapour, humidity, pressure-levels, ascending, descending, gesdisc, atmosphere]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T13:30:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-15T13:59:41Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/161 }
resource: https://disc.gsfc.nasa.gov/datasets/AIRS3STD_7.0/summary
version: "Version 7.0 is the current AIRS science team level 3 release; concept ids and DOIs CMR-verified 2026-09-15, the DOIs resolving on doi.org the same day to the GES DISC pages: AIRS3STD C1701805652-GES_DISC (DOI 10.5067/UO3Q64CTTS1U, daily, from 2002-08-31, newest granule that day 2026-09-13 with processing version v7.0.10.0 in its name), AIRS3STM C1701805662-GES_DISC (DOI 10.5067/UBENJB9D3T2H, monthly, from 2002-09-01, newest granule August 2026 with v7.0.9.3 in its name, as every monthly granule from September 2021 on has), the support products AIRS3SPD C1701805657-GES_DISC and AIRS3SPM C1701805668-GES_DISC on 100 levels, and the superseded version 006 records AIRS3STD C1238517289-GES_DISC and AIRS3STM C1238517301-GES_DISC still in CMR; the post-DSM processing versions are v7.0.9.3 from 2021-09-23 and v7.0.10.0 from 2024-12-23 per Table 1 of the JPL memo of 2025-12-10, but the granule names read 2026-09-15 do not follow that boundary: the daily files still carry v7.0.9.3 through the end of December 2024 and the daily files of late August and early September 2026 mix v7.0.10.0 with v7.0.9.3 on some days"
sources:
  - id: cmr-airs3std
    resource: https://cmr.earthdata.nasa.gov/search/collections.json?short_name=AIRS3STD&provider=GES_DISC
    title: "CMR collection search for AIRS3STD, AIRS3STM, AIRS3SPD and AIRS3SPM under the GES_DISC provider, and the UMM records of the four version 7.0 collections (read 2026-09-15: concept ids, DOIs, the 2002 start dates with no end, the 1 degree gridded resolution, the abstracts, the document links and the two publication references; the same day the granule search gave the first and newest AIRS3STD and AIRS3STM granules and the processing versions in their names, and samples around the version boundaries: monthly granules v7.0.4.0 through August 2021 and v7.0.9.3 from September 2021 through August 2026, daily granules v7.0.9.3 on 19 to 27 December 2024 and a mix of v7.0.10.0 and v7.0.9.3 on 24 August to 4 September 2026)"
  - id: gesdisc-airs3std
    resource: https://disc.gsfc.nasa.gov/datasets/AIRS3STD_7.0/summary
    title: "GES DISC collection page for AIRS3STD 7.0 (fetched 2026-09-15; the page is rendered by script, so its text was read from the CMR record it is built from: the grating spectrometer, the 24 hour period per node, the westward progression from the dateline, the gores, the 1 by 1 degree binning and the mean, standard deviation and count maps)"
  - id: gesdisc-airs3stm
    resource: https://disc.gsfc.nasa.gov/datasets/AIRS3STM_7.0/summary
    title: "GES DISC collection page for AIRS3STM 7.0 (fetched 2026-09-15, text read from its CMR record: the calendar month file and its sentence that the monthly means are daily means weighted by input counts, which the version 7 user guide contradicts)"
  - id: airs-l3-ug
    resource: https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/V7_L3_User_Guide.pdf
    title: "Tian, Manning, Roman, Thrastarson, Fetzer and Monarrez, 2020, AIRS Version 7 Level 3 Product User Guide, version 1.0, April 2020, Jet Propulsion Laboratory (the AIRS level 3 product documentation, hosted at GES DISC and linked from the collection records; read in full 2026-09-15: the instrument variants, the standard and support levels in Tables 1 and 2, the daily and monthly periods, the short names, the nodes, the grids and their quality control, the field tables with the count and standard deviation ancillaries, the sampling and topography caveats of section 4 and the version 7 changes of section 5)"
  - id: airs-docs-index
    resource: https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/AIRS_Documentation.pdf
    title: "GES DISC AIRS Documentation index (read 2026-09-15: the current document list with dates, among them the version 7 level 2 and level 3 user guides, the level 3 standard pressure levels note of July 2020, the data outages list of April 2026, the DC restore anomaly memo of March 2026 and the deep space manoeuvre impact report of December 2025)"
  - id: airs-dsm
    resource: https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/AIRS_DSM_Impact.pdf
    title: "Wang and Yue, 2025, Impact of Deep Space Maneuver (DSM, Sept. 23, 2021) on AIRS products and Post-DSM Corrections, Jet Propulsion Laboratory, 10 December 2025 (read 2026-09-15: the overview and Table 1 of post-DSM processing versions, the two algorithm fixes, the statement that the fully corrected v7.0.9.3 and v7.0.10.0 were released to users in September 2025, the anomaly time series computed against a 2006 to 2015 climatology, and section 8 on the breakpoint in the version 7 time series)"
  - id: airs-dcr
    resource: https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/DC-Restore_Anomaly_Note_Final_260302_ADF1122.pdf
    title: "Pagano, Wang, Goodman and Sterzinger, 2026, AIRS DC Restore Anomaly, AIRS Design File Memo 1122, 2 March 2026 (read 2026-09-15: the anomaly of 19 to 28 January 2026, the modules affected, and the level 2 and level 3 products not generated between those dates)"
  - id: airs-outages
    resource: https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/AIRS_Data_Outages.pdf
    title: "Thrastarson (editor), AIRS/AMSU/HSB Data Outages, document version 1.1, 13 April 2026, Jet Propulsion Laboratory (read 2026-09-15 in its introduction: the list of outage periods from 2002 to 2020 by year and the pointer to the JPL outages page for later events)"
  - id: airs-jpl
    resource: https://airs.jpl.nasa.gov/
    title: "AIRS project site at JPL (fetched 2026-09-15: the home page answers, but every product and documentation path tried under it, data/get-data, data/about-the-data, data/outages and data/support, returned 404, so the AIRS level 3 product documentation was read in the JPL-authored user guide and memoranda that GES DISC hosts)"
  - id: susskind-2014
    resource: https://doi.org/10.1117/1.JRS.8.084994
    title: "Susskind, Blaisdell and Iredell, 2014, Improved methodology for surface and atmospheric soundings, error estimates, and quality control procedures: the atmospheric infrared sounder science team version-6 retrieval algorithm, Journal of Applied Remote Sensing 8, 084994 (the retrieval reference on the collection records; title, authors, journal and year verified on the Crossref registry 2026-09-15, no abstract carried there)"
  - id: kahn-2014
    resource: https://doi.org/10.5194/acp-14-399-2014
    title: "Kahn and others, 2014, The Atmospheric Infrared Sounder version 6 cloud products, Atmospheric Chemistry and Physics 14, 399 to 426 (the cloud reference on the collection records; record and abstract read on the Crossref registry 2026-09-15)"
  - id: ding-2020
    resource: https://doi.org/10.1175/JTECH-D-19-0129.1
    title: "Ding, Savtchenko, Hearty, Wei, Theobald, Vollmer, Tian and Fetzer, 2020, Assessing the Impacts of Two Averaging Methods on AIRS Level 3 Monthly Products and Multiyear Monthly Means, Journal of Atmospheric and Oceanic Technology 37, 1027 to 1050 (named by the user guide for the monthly averaging change; record and abstract read on the Crossref registry 2026-09-15, the journal page sits behind a bot check: the count-weighted method gives a warmer surface and a drier column than the average of daily means, and the multi-year means are compared with MERRA-2)"
  - id: merra2
    resource: ../datasets/merra-2.md
    title: "This bundle's MERRA-2 dataset concept: the reanalysis AIRS multi-year means are compared against, whose own pressure-level fields are undefined below ground and whose 0.625 by 0.5 degree grid carries the same area-weighting trap as this 1 degree one"
status: stable
stale_after: 2027-03-15
---

# AIRS version 7 level 3 temperature and water vapour

**Identity.** The Atmospheric Infrared Sounder (AIRS) is a grating
spectrometer of resolving power 1200 on the Aqua platform, and its
science team's version 7 level 3 standard products are the gridded
means a user meets first at GES DISC: AIRS3STD, one file per day, and
AIRS3STM, one file per calendar month, both on a 1 by 1 degree grid
of 360 by 180 cells with centres from 179.5 W to 179.5 E and 89.5 S
to 89.5 N, from 31 August 2002 (daily) and September 2002 (monthly)
to the present.[^cmr-airs3std][^gesdisc-airs3std][^airs-l3-ug] The
"AIRS-only" variant (the S in the short name) is the one that spans
the mission; the AIRS plus AMSU variant (AIRX) ends in September
2016 with the AMSU-A2 power failure of 24 September 2016, and the
AIRS plus AMSU plus HSB variant (AIRH) ends in February 2003 with
the HSB failure of 5 February 2003.[^airs-l3-ug] The standard
product carries temperature on 24 standard pressure levels (1000,
925, 850, 700, 600, 500, 400, 300, 250, 200, 150, 100, 70, 50, 30,
20, 15, 10, 7, 5, 3, 2, 1.5 and 1 hPa, ordered from the surface
upward), geopotential height on the same levels, water vapour mass
mixing ratio and relative humidity on the 12 levels from 1000 to 100
hPa, the layer mixing ratio on 12 layers whose boundaries are the
first 13 standard levels, 1000 down to 70 hPa (mid-layer pressures
961.8 to 83.7 hPa, the topmost layer being 100 to 70 hPa), and the
single-level fields
a climatology reaches for: surface skin temperature, surface air
temperature, total column water vapour in kilograms per square
metre, surface mixing ratio and relative humidity, tropopause
pressure, temperature and height, and a forecast surface
pressure.[^airs-l3-ug] The support products AIRS3SPD and AIRS3SPM
carry the same grids at 100 levels for the team and for users
willing to invest in them.[^airs-l3-ug][^cmr-airs3std] The
collection page at GES DISC is rendered by script; its text is the
CMR record's, which still describes the monthly mean as the daily
means weighted by input counts, a sentence the version 7 guide
contradicts (below).[^gesdisc-airs3stm][^airs-l3-ug]

**Structure.** Each file holds six HDF-EOS grids beside a location
grid: ascending and descending, ascending_TqJoint and
descending_TqJoint, and ascending_MW_Only and descending_MW_Only;
field names take the grid's suffix, so the temperature profile is
Temperature_A in the ascending grid and Temperature_TqJ_D in the
descending joint grid.[^airs-l3-ug] Ascending means the
sub-satellite point moving south to north with a 1:30 PM local
equator crossing, daytime outside the polar zones; descending is
north to south at 1:30 AM, night-time; the guide says the separation
into nodes mitigates the suppression of the diurnal signal.[^airs-l3-ug]
The value in a cell is the mean of the level 2 retrievals that fell
in it and passed quality control: in the ascending and descending
grids each field and level is filtered by its own level 2 quality
indicator (best, 0, or good, 1), which gives every field the most
data available but a different ensemble per field and per level,
while the TqJoint grids apply one criterion to every field, the
surface air temperature indicator at 0 or 1, so that fields and
levels share an ensemble.[^airs-l3-ug] Every floating-point field has
two ancillaries, a 16-bit count with the suffix _ct (the number of
level 2 observations in the mean) and a standard deviation with the
suffix _sdev; each grid also carries TotalCounts, the number of AIRS
fields of regard that fell in the cell whether used or not, so that
count over TotalCounts is a yield; a value of minus 9999 or a count
of zero marks a missing cell.[^airs-l3-ug] A daily file covers a
nominal 24 hours per node rather than midnight to midnight: 1:30 PM
to 1:30 PM UTC for the descending node and 1:30 AM to 1:30 AM for
the ascending, the gridding starting at the antimeridian and moving
westward with the orbits so that neighbouring cells are no more than
about 100 minutes apart by the guide's figure (the collection record
says about 90), the cell edge sitting on the 180 degree
meridian, and gores left between the swaths where the day had no
coverage.[^airs-l3-ug][^gesdisc-airs3std] The monthly file is the
calendar month, and in version 7 it is the plain arithmetic mean of
the daily means ("averaged by day"), a change from version 6, whose
monthly mean weighted each day by its counts and so favoured the
less cloudy days, a bias the guide says grows in multi-year
climatological estimates; the count-weighted method gives a warmer
global surface and a drier column than the average of daily
means.[^airs-l3-ug][^ding-2020] Version 7 also dropped the minimum,
maximum and standard error ancillaries, the 8-day product, the
quantised 5 degree product and the total column and surface carbon
monoxide, methane and ozone fields, whose information came almost
entirely from the first-guess climatology.[^airs-l3-ug] File names
read AIRS.YYYY.MM.DD.L3.RetStd_IR001.v7.0.x.y.G<production>.hdf for
the daily product and RetStd_IR031 for the monthly, and the
processing version in the name matters: after the Aqua deep space
manoeuvre of 23 September 2021 shifted the focal plane by about one
micrometre, the science team reprocessed the record from that date
with a corrected radiative transfer table and a corrected
first-guess network, released in September 2025 as v7.0.9.3 (23
September 2021 to 23 December 2024) and v7.0.10.0 (from 23 December
2024), replacing the v7.0.7.0 files of May 2022 whose water vapour
and near-surface fields carried a discontinuity at the manoeuvre
date.[^airs-dsm] The file names read on 2026-09-15 do not follow the
memo's boundary between the two versions: every monthly granule from
September 2021 through August 2026 carries v7.0.9.3, the daily
granules of 19 to 27 December 2024 all carry v7.0.9.3, and the daily
granules of late August and early September 2026 carry v7.0.10.0 on
most days and v7.0.9.3 on some, so the processing string in a file's
name, not the memo's date range, says which version a given file
is.[^cmr-airs3std][^airs-dsm]

**Access.** Both collections are searchable in CMR by short name
under the GES_DISC provider and served through Earthdata Search and
the GES DISC data tree; each is cited by its own DOI, and the
documentation the records link (the user guide, the documentation
index, the outages list and the anomaly memoranda) is JPL-authored
and hosted on the GES DISC document server, because the JPL project
site's product pages no longer answer at the paths tried.[^cmr-airs3std][^airs-docs-index][^airs-jpl]

## Uncertainty

- **No error field ships in the version 7 level 3 product.** The
  version 6 standard error ancillary was removed; what remains beside
  each mean is the count of retrievals and their standard deviation,
  and the standard deviation is the spread of the retrievals that
  entered the cell that day or month, not a retrieval error.[^airs-l3-ug]
  The level 2 error estimates and quality indicators are the
  retrieval algorithm's, documented for version 6 and carried into
  version 7.[^susskind-2014][^airs-l3-ug]
- **The count does not characterise sampling bias.** The retrieval
  fails under cloud cover above about 70 percent, so the ensemble in
  a cell is biased toward clearer scenes, and the bias is height and
  species dependent within a grid box: fields correlated with
  cloudiness (cloud properties, water vapour) carry a different
  sampling bias from temperature or the surface fields, and total
  cloudiness in the box cannot be used to correct it.[^airs-l3-ug][^kahn-2014]
  Yield differs between levels of one profile as well: more samples
  enter the temperature profile at altitude than near the surface,
  and over topography the per-level count falls toward zero as the
  profile approaches 1000 hPa (the pressure-level gotcha below).[^airs-l3-ug]
- **The nodes are two local times, not a daily mean.** A daytime and
  a night-time field with their own ensembles sit in every file; the
  guide separates them to keep the diurnal signal, and nothing in
  the file averages them (the node gotcha below).[^airs-l3-ug]
- **The record has documented breaks.** The deep space manoeuvre of
  23 September 2021 left a breakpoint in the uncorrected version 7
  time series, largest in water vapour above 300 hPa and between 500
  and 900 hPa and in the near-surface temperature, which the
  September 2025 reprocessing reduced; the JPL memo quantifies it
  with anomalies against a 2006 to 2015 climatology.[^airs-dsm] The
  DC restore circuit anomaly of 19 to 28 January 2026 left no daily
  level 3 files between those dates, partial files on the 19th and
  28th, and a January 2026 monthly file missing those granules; the
  outages document lists the earlier gaps year by year.[^airs-dcr][^airs-outages]
- **Two fields disagree by construction.** The layer mixing ratio
  profile assumes an atmosphere down to 1000 hPa and can extend
  below the surface, while the total column water vapour does not;
  a vertical integral of the layers exceeds the column wherever the
  surface pressure is below 1000 hPa, over ocean as well as land.[^airs-l3-ug]
- **Relative humidity above about 200 percent is unrealistic**,
  occurring where specific humidity is very low or the air very
  cold, and the guide says such values are to be excluded; and the
  product is compressed by rounding to 11 bits of mantissa, so a
  fine histogram of mixing ratio shows a digitisation beat.[^airs-l3-ug]
- **The reanalysis comparison is the multi-year mean's.** The
  averaging-method study compares AIRS multi-year monthly means with
  MERRA-2 and finds the average of daily means the closer; MERRA-2's
  own pressure-level fields are undefined below ground, so a
  comparison at 1000 or 925 hPa over terrain is between two masked
  fields, not a full grid.[^ding-2020][^merra2]

## Known issues

- [airs-pressure-levels-and-surface-mask](../gotchas/airs-pressure-levels-and-surface-mask.md):
  the levels are fixed pressure levels, the lowest lie below the
  terrain, the per-level count drops to zero there, and the layer
  water vapour extends below the surface while the column does not.
- [airs-ascending-descending-nodes](../gotchas/airs-ascending-descending-nodes.md):
  ascending is 1:30 PM and descending 1:30 AM local time with their
  own ensembles; a mean of the two is a two-sample diurnal estimate,
  not a daily mean.
- [l3-count-field-bounds-a-cell](../gotchas/l3-count-field-bounds-a-cell.md):
  a cell's mean rests on the retrievals its count names, the monthly
  mean's weighting changed between versions, and an aggregate that
  drops the count treats a one-retrieval cell as a full one.
- [anomaly-names-its-climatology-period](../gotchas/anomaly-names-its-climatology-period.md):
  an anomaly is relative to a base period and a processing version,
  and the record carries the 2021 manoeuvre and the 2026 gap.

[^cmr-airs3std]: CMR collection, UMM and granule records for AIRS3STD, AIRS3STM, AIRS3SPD and AIRS3SPM 7.0, GES_DISC provider, read 2026-09-15
[^gesdisc-airs3std]: GES DISC collection page and CMR record, AIRS3STD 7.0
[^gesdisc-airs3stm]: GES DISC collection page and CMR record, AIRS3STM 7.0
[^airs-l3-ug]: Tian and others, 2020, AIRS Version 7 Level 3 Product User Guide, version 1.0
[^airs-docs-index]: GES DISC AIRS Documentation index
[^airs-dsm]: Wang and Yue, 2025, Impact of Deep Space Maneuver on AIRS products and Post-DSM Corrections, JPL, 2025-12-10
[^airs-dcr]: Pagano and others, 2026, AIRS DC Restore Anomaly, AIRS Design File Memo 1122, 2026-03-02
[^airs-outages]: Thrastarson (editor), AIRS/AMSU/HSB Data Outages, version 1.1, 2026-04-13
[^airs-jpl]: AIRS project site at JPL, home page reachable, product pages not
[^susskind-2014]: Susskind, Blaisdell and Iredell, 2014, Journal of Applied Remote Sensing, doi:10.1117/1.JRS.8.084994
[^kahn-2014]: Kahn and others, 2014, Atmospheric Chemistry and Physics, doi:10.5194/acp-14-399-2014
[^ding-2020]: Ding and others, 2020, Journal of Atmospheric and Oceanic Technology, doi:10.1175/JTECH-D-19-0129.1
[^merra2]: This bundle's MERRA-2 dataset concept
