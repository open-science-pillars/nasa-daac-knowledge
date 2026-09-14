---
type: dataset
spheres: [cryosphere]
title: "NSIDC-0051 NASA Team sea ice concentration from Nimbus-7 SMMR and DMSP SSM/I and SSMIS, Version 2"
description: "Daily (every other day under SMMR) and monthly sea ice concentration for both polar regions on the 25 km NSIDC polar stereographic grids, 26 October 1978 to 31 December 2025, from one sensor per day (Nimbus-7 SMMR, DMSP F8, F11 and F13 SSM/I, DMSP F17 SSMIS) with tie points calibrated across each sensor overlap to keep hemispheric extent and area continuous; the pole hole, coast and land are flag values in the concentration variable. Forward processing has stopped and the record is static; NSIDC-0803 (AMSR2) is the DAAC's continuing daily product."
tags: [nsidc-0051, sea-ice-concentration, nasa-team, smmr, ssmi, ssmis, passive-microwave, polar-stereographic, nsidc, cryosphere]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:30:00Z }
resource: https://nsidc.org/data/nsidc-0051/versions/2
version: "Version 2 (DOI 10.5067/MPYG15WAA4WX; DiGirolamo and others 2022, updated yearly), verified 2026-09-14: temporal coverage 26 October 1978 to 31 December 2025 with forward processing stopped and the record kept as a static product; the user guide is dated September 2023 and last updated July 2026; NSIDC-0803 Version 2 (AMSR2) is the alternative the product page names"
sources:
  - id: nsidc-0051-page
    resource: https://nsidc.org/data/nsidc-0051/versions/2
    title: "NSIDC product page: Sea Ice Concentrations from Nimbus-7 SMMR and DMSP SSM/I-SSMIS Passive Microwave Data, Version 2 (the end-of-processing notice, platforms, formats, coverage, strengths and limitations, the documents it links)"
  - id: nsidc-0051-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/nsidc-0051-v002-userguide.pdf
    title: "NSIDC-0051 Version 2 user guide (NSIDC, published September 2023, last updated July 2026): parameters and flag values, file naming, the pole hole table, projection and grid, sensor periods, the intercalibration of each transition, spillover and weather corrections, monthly generation, the overlap-period difference tables, accuracy and the version history"
  - id: nsidc-0803-page
    resource: https://nsidc.org/data/nsidc-0803/versions/2
    title: "NSIDC product page: AMSR2 Daily Polar Gridded Sea Ice Concentrations, Version 2 (the follow-on to NSIDC-0081 and NSIDC-0051, on the same 25 km grids, 1 January 2023 to present)"
  - id: sensor-change-assessment
    resource: https://nsidc.org/sites/default/files/documents/technical-reference/pm_seaice_assessment_amsr2-ssmis.pdf
    title: "Meier, Assessment of sensor change on long-term NSIDC DAAC passive microwave sea ice extent climate record, NSIDC DAAC, 21 June 2026: the three-year NSIDC-0803 against NSIDC-0051 comparison, 2023 through 2025"
  - id: sensors-summary
    resource: https://nsidc.org/sites/default/files/documents/technical-reference/smmr-ssmi-ssmis-sensors.pdf
    title: "NSIDC, Summary of SMMR, SSM/I, and SSMIS Sensors: channels, platforms, coverage dates and equator crossing times"
  - id: nt-vs-bt-article
    resource: https://nsidc.org/data/user-resources/help-center/descriptions-and-differences-between-nasa-team-and-bootstrap-algorithms
    title: "NSIDC help article: Descriptions of and differences between the NASA Team and Bootstrap algorithms (channels, tie points, weather filters, strengths, weaknesses, accuracy, the products that use each)"
  - id: cavalieri-1999
    resource: https://doi.org/10.1029/1999JC900081
    title: "Cavalieri, Parkinson, Gloersen, Comiso and Zwally, 1999, Deriving long-term time series of sea ice cover from satellite passive-microwave multisensor data sets, Journal of Geophysical Research: Oceans 104, 15803 to 15814 (the intercalibration method; cited on its Crossref record and abstract, the journal page sits behind a bot check)"
  - id: cavalieri-2012
    resource: https://doi.org/10.1109/LGRS.2011.2166754
    title: "Cavalieri, Parkinson, DiGirolamo and Ivanoff, 2012, Intersensor Calibration Between F13 SSMI and F17 SSMIS for Global Sea Ice Data Records, IEEE Geoscience and Remote Sensing Letters 9(2), 233 to 236 (cited on its Crossref record)"
  - id: comiso-1997
    resource: https://doi.org/10.1016/S0034-4257(96)00220-9
    title: "Comiso, Cavalieri, Parkinson and Gloersen, 1997, Passive microwave algorithms for sea ice concentration: A comparison of two techniques, Remote Sensing of Environment 60, 357 to 384 (cited on its Crossref record; the publisher page was not fetched)"
status: draft
stale_after: 2027-03-14
---

# NSIDC-0051 NASA Team sea ice concentration, Version 2

**Identity.** NSIDC-0051 is the Goddard Space Flight Center's NASA
Team sea ice concentration record: the fraction of ocean area covered
by sea ice in each 25 km cell of the NSIDC polar stereographic grids,
for the north and south polar regions, generated from brightness
temperatures of the Nimbus-7 Scanning Multichannel Microwave
Radiometer (SMMR), the DMSP F8, F11 and F13 Special Sensor
Microwave/Imagers (SSM/I) and the DMSP F17 Special Sensor Microwave
Imager/Sounder (SSMIS), with the algorithm coefficients calibrated to
reduce differences in sea ice extent and area between the
sensors.[^nsidc-0051-page][^nsidc-0051-user-guide] The record runs
from 26 October 1978 to 31 December 2025; the data producer has
stopped forward processing, the data remain available as a static
product, and the product page names NSIDC-0803, the AMSR2 daily polar
gridded sea ice concentrations, as the alternative for the period
after.[^nsidc-0051-page][^nsidc-0051-user-guide] The DOI is
10.5067/MPYG15WAA4WX and the citation is DiGirolamo, Parkinson,
Cavalieri, Gloersen and Zwally, 2022, updated yearly; the archive is
the NASA NSIDC DAAC and access needs a free Earthdata
login.[^nsidc-0051-page][^nsidc-0051-user-guide] The data were produced
at Goddard about once per year with roughly a one-year latency, from
SMMR brightness temperatures processed at Goddard and from SSM/I and
SSMIS brightness temperatures processed at
NSIDC.[^nsidc-0051-user-guide]

**Structure.** One netCDF-4 file per day and per month and hemisphere,
CF 1.6 and ACDD 1.3, named
NSIDC0051_SEAICE_PS_N25km_20220630_v2.0.nc (the day is omitted from
monthly names, and the sensor code, N07, F08, F11, F13 or F17, appears
only in the browse image names).[^nsidc-0051-user-guide] The
concentration variable is named for the sensor, F17_ICECON for
example, with dimensions (t, y, x) so files concatenate along time; on
a day without data the file exists but carries no ICECON variable,
which is the case every other day of the SMMR period (the SMMR scanner
ran on alternate days for spacecraft power) and for the gap from
December 1987 to January 1988.[^nsidc-0051-user-guide] Concentration
is packed as unsigned bytes 0 to 250 for 0 to 100 percent, and the same
array carries four flag values: 251 for the pole hole mask, 252
unused, 253 for coast (a land cell orthogonally adjacent to ocean) and
254 for land from a fixed land mask.[^nsidc-0051-user-guide] The grids
are 304 columns by 448 rows in the north and 316 by 332 in the south,
NSIDC Sea Ice Polar Stereographic North and South (EPSG 3411 and 3412,
Hughes 1980 ellipsoid, true scale at 70 N and 70 S), with a crs
variable and x and y cell-centre coordinates in projected metres; the
nominal 25 km resolution varies by latitude because the grids are not
equal area, which is the subject of this bundle's projection
gotcha.[^nsidc-0051-user-guide] One sensor supplies each day: Nimbus-7
SMMR from 26 October 1978 through 20 August 1987, F8 SSM/I through
18 December 1991, F11 SSM/I through 29 September 1995, F13 SSM/I
through 31 December 2007 and F17 SSMIS from 1 January 2008 through
31 December 2025; Version 1.1 (December 2015) removed the overlap
dates during the transitions, so the join between sensors is one
day.[^nsidc-0051-user-guide] The sensors' circular unobserved sectors
at the North Pole are masked at three sizes: 1.19 million km2 (radius
611 km, poleward of 84.5 N) for SMMR, 0.31 million km2 (311 km,
87.2 N) for SSM/I and 0.029 million km2 (94 km, 89.18 N) for SSMIS,
the last applied from January 2008 although SSMIS data begin in
January 2007, to allow the comparison with SSM/I during the 2007
transition (its own gotcha).[^nsidc-0051-user-guide]

**Processing.** The concentrations come from a revised NASA Team
algorithm, which uses the 18 GHz vertical and horizontal and 37 GHz
vertical channels of SMMR and the 19.3 GHz and 37 GHz channels of SSM/I
and SSMIS, with the polarization and spectral gradient ratios of those
channels, tie points for open water, first-year and multiyear ice, and
a weather filter that for SSM/I and SSMIS adds the 19.3 and 22.2 GHz
combination because the 19.3 GHz channel sits on the shoulder of the
22.2 GHz water vapour line.[^nsidc-0051-user-guide][^nt-vs-bt-article]
The tie points of each new sensor were derived from linear regressions
of brightness temperatures during the overlap with its predecessor
(22 days for SMMR to F8, 16 days for F8 to F11, five months for F11 to
F13, twelve months for F13 to F17), with the F8 and F11 open-water tie
points tuned by hand to minimize the extent and area differences in
the overlap; Cavalieri and others 1999 and 2012 document the
method.[^nsidc-0051-user-guide][^cavalieri-1999][^cavalieri-2012] After
the retrieval, a land-to-ocean spillover correction subtracts a
per-sensor minimum coastal concentration wherever open water is
nearby, a valid ice mask from monthly climatological sea surface
temperature zeroes ice where the ocean is warmer than 278 K in the
north and 275 K in the south, manual inspection removes remaining
spurious ice, and gaps are filled by spatial interpolation of
brightness temperatures and temporal interpolation of concentrations,
except the period 3 December 1987 through 12 January 1988, which is
left missing.[^nsidc-0051-user-guide] Monthly grids are the average of
the available daily grids, excluding missing pixels; October 1978,
December 1987 and January 1988 rest on three, two and nineteen days,
and the guide's own recommendation is that extent and area be computed
from the daily grids and then averaged, because computing them from a
monthly mean concentration map can bias the
series.[^nsidc-0051-user-guide]

**Sea ice use.** The product's stated applications are monitoring the
distribution, extent and area of the Arctic and Antarctic sea ice
cover, polynyas, regional and global trends, and model
validation.[^nsidc-0051-user-guide] The 15 percent concentration
contour is the conventional ice edge for this product and defines
extent, while area weights each cell by its concentration; the two
differ by construction and by their treatment of the pole hole (its own
gotcha).[^nsidc-0051-user-guide] The NOAA at NSIDC Sea Ice Index in
this bundle is built from this product through December 2024 and from
NSIDC-0803 after.[^nsidc-0803-page]

## Uncertainty

- **Concentration accuracy is seasonal.** The guide's summary of the
  validation studies puts total concentration within plus or minus
  5 percent of the actual value in winter and plus or minus 15 percent
  in the Arctic summer when melt ponds are present, best within the
  consolidated pack where ice is thicker than 20 cm and concentration
  high, and worse as the proportion of thin ice
  grows.[^nsidc-0051-user-guide] The product page lists
  underestimation during the melt season and for thin ice, higher
  uncertainties in the Antarctic from flooded snow, fixed algorithm
  coefficients per sensor that bias the retrieval when surface
  conditions change, and false coastal ice from mixed land and ocean in
  the footprint.[^nsidc-0051-page][^comiso-1997]
- **The calibration is hemispheric, not local.** The tie points were
  tuned to minimize the differences in hemispheric extent and area
  during each overlap; the guide states that this does not mean the
  concentrations themselves are well matched, that significant regional
  differences may remain, and that sensor-to-sensor differences are
  likely to persist in the marginal ice zones.[^nsidc-0051-user-guide]
  The residual differences it tabulates for the Northern Hemisphere
  overlaps are 0.70 percent in extent and 1.34 percent in area for SMMR
  to F8, 0.01 and 0.18 percent for F8 to F11, near zero and 0.18 percent
  for F11 to F13, and near zero in extent and 0.54 percent in area for
  F13 to F17; the F11 to F13 and F13 to F17 differences in extent and
  area were statistically significant (its own
  gotcha).[^nsidc-0051-user-guide][^cavalieri-1999]
- **No per-cell error field ships with the data.** The concentration
  variable and its flags are the whole content; the uncertainty is the
  published accuracy above and the overlap tables, and the pole hole
  flag marks where there is no observation at all.[^nsidc-0051-user-guide]
- **Residual weather and land effects.** Some weather effects and land
  contamination remain after the automated and manual corrections,
  varying with season, and occasional bad scan lines persist; May 1986
  carries bands of false concentration below one percent over the open
  Weddell, Bellingshausen and Amundsen Seas, and the 14 September 1984
  field was replaced by the average of 12 and 16 September after a
  geolocation error put several hundred thousand km2 of false ice in
  it.[^nsidc-0051-user-guide]
- **The successor is not identical.** Over the three-year overlap 2023
  through 2025, NSIDC-0803 (AMSR2) runs low against NSIDC-0051 by up to
  about 100,000 to 150,000 km2 of Arctic extent in summer (3 to
  4 percent), by up to about 200,000 km2 of Antarctic extent from
  December to February (4 to 5 percent), by a consistent 100,000 to
  200,000 km2 of Arctic area (about 6 percent in summer and early
  autumn, about 1 percent in winter) and by 300,000 to 400,000 km2 of
  Antarctic area from November to January (5 to 6 percent), with the
  largest differences near the ice edge and near-zero bias inside the
  pack.[^sensor-change-assessment]

## Known issues

- [sea-ice-pole-hole-by-sensor](../gotchas/sea-ice-pole-hole-by-sensor.md):
  the masked pole hole shrinks at the sensor changes, and an Arctic
  total that ignores it steps there.
- [sea-ice-extent-is-not-area](../gotchas/sea-ice-extent-is-not-area.md):
  extent is the area of cells at 15 percent or more, area weights by
  concentration; the two answer different questions.
- [sea-ice-nrt-versus-final](../gotchas/sea-ice-nrt-versus-final.md):
  the near-real-time product and the AMSR2 successor differ from this
  record in input and processing, and a series that joins them steps at
  the join.
- [sea-ice-nasa-team-versus-bootstrap](../gotchas/sea-ice-nasa-team-versus-bootstrap.md):
  NSIDC-0079 is the Bootstrap record on the same grid and dates, and
  the two algorithms differ where the ice is thin, melting or marginal.
- [sea-ice-sensor-transitions](../gotchas/sea-ice-sensor-transitions.md):
  the intercalibration reduces the steps at the sensor changes and does
  not remove them.
- [polar-stereographic-not-latlon](../gotchas/polar-stereographic-not-latlon.md):
  the grids are projected metres on the Hughes ellipsoid (EPSG 3411 and
  3412, not 3413 and 3031), and cell area varies with latitude.
- The NASA Team algorithm is not designed for freshwater ice, and the
  spillover filter may affect open water features near coasts such as
  coastal polynyas.[^nsidc-0051-user-guide]

**Verification.** The product page and the Version 2 user guide were
read in full on 2026-09-14, and the product page carried the notice
that forward processing has stopped with the final coverage through
31 December 2025.[^nsidc-0051-page][^nsidc-0051-user-guide] The
NSIDC-0803 product page, the sensors summary, the NASA Team and
Bootstrap help article and Meier's June 2026 sensor-change assessment
were read the same day.[^nsidc-0803-page][^sensors-summary][^nt-vs-bt-article][^sensor-change-assessment]
Cavalieri and others 1999, Cavalieri and others 2012 and Comiso and
others 1997 are cited on their Crossref registry records (title,
authors, journal, volume, pages and year verified 2026-09-14); the
1999 abstract on the record states that the procedure reduced ice
extent differences during the overlaps to less than 0.05 percent and
area differences to 0.6 percent or less; the journal pages sit behind
a bot check and were not read.[^cavalieri-1999][^cavalieri-2012][^comiso-1997]
No granule was opened, so the variable names, flag values and grid
dimensions above come from the user guide; the Sea Ice Index's daily
extent file (its own concept) names NSIDC-0051 files as the source of
its rows through 31 December 2024, read the same day.[^nsidc-0051-user-guide]

[^nsidc-0051-page]: NSIDC product page, NSIDC-0051 Version 2
[^nsidc-0051-user-guide]: NSIDC-0051 Version 2 user guide, NSIDC
[^nsidc-0803-page]: NSIDC product page, NSIDC-0803 Version 2
[^sensor-change-assessment]: Meier, 2026, Assessment of sensor change on the NSIDC DAAC passive microwave sea ice extent record
[^sensors-summary]: NSIDC, Summary of SMMR, SSM/I, and SSMIS Sensors
[^nt-vs-bt-article]: NSIDC help article on the NASA Team and Bootstrap algorithms
[^cavalieri-1999]: Cavalieri and others, 1999, JGR Oceans, doi:10.1029/1999JC900081
[^cavalieri-2012]: Cavalieri and others, 2012, IEEE GRSL, doi:10.1109/LGRS.2011.2166754
[^comiso-1997]: Comiso and others, 1997, Remote Sensing of Environment, doi:10.1016/S0034-4257(96)00220-9
