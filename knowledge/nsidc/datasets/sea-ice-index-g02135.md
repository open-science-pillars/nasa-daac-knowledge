---
type: dataset
spheres: [cryosphere]
title: "G02135 Sea Ice Index, Version 4: NOAA at NSIDC daily and monthly sea ice extent, area, images and GeoTIFFs from the NASA Team concentration records"
description: "The Sea Ice Index is a NOAA at NSIDC product, distributed from the NOAA archive at noaadata.apps.nsidc.org beside the NASA DAAC's products and not through Earthdata, that turns the NASA Team concentration grids into hemisphere-wide extent (cells at 15 percent or more) and area (concentration times cell area) values, daily and monthly, with images, GeoTIFFs and shapefiles, from 26 October 1978 to the present. Version 4 (July 2025) takes NSIDC-0051 as input through December 2024 and NSIDC-0803 (AMSR2) from 1 January 2025, drops the near-real-time and final distinction of Version 3, assumes the pole hole is ice-covered for extent and excludes it from area, and states its own steps at the sensor changes."
tags: [g02135, sea-ice-index, sea-ice-extent, sea-ice-area, noaa-at-nsidc, nasa-team, nsidc-0051, nsidc-0803, amsr2, cryosphere]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:30:00Z }
resource: https://nsidc.org/data/g02135/versions/4
version: "Version 4 (DOI 10.7265/a98x-0f50; Fetterer, Knowles, Meier, Savoie, Windnagel and Stafford 2025; released July 2025), verified 2026-09-14 on the NOAA archive listing: daily extent files N_seaice_extent_daily_v4.0.csv and S_seaice_extent_daily_v4.0.csv with rows through 12 September 2026, twelve monthly files per hemisphere named N_MM_extent_v4.0.csv, daily GeoTIFFs by year and month, and the 1981 to 2010 climatology files; Version 3 (DOI 10.7265/N5K072F8) is retired with coverage to 31 July 2025; the level of service was reduced to Basic for funding reasons"
sources:
  - id: g02135-page
    resource: https://nsidc.org/data/g02135/versions/4
    title: "NSIDC product page: Sea Ice Index, Version 4 (the citation naming the National Snow and Ice Data Center as publisher, the Basic level of service notice, platforms, formats, coverage, the HTTPS location on the NOAA archive, the documents it links)"
  - id: g02135-v3-page
    resource: https://nsidc.org/data/g02135/versions/3
    title: "NSIDC product page: Sea Ice Index, Version 3 (retired; coverage 26 October 1978 to 31 July 2025; DOI 10.7265/N5K072F8)"
  - id: g02135-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/g02135-v004-userguide.pdf
    title: "Sea Ice Index Version 4 user guide (Windnagel, NSIDC, revised July 2025): data sources, the extent and area calculations, the pole hole masks, monthly and daily data files, directory structure, accuracy, valid ice masks, consistency, tie points and the version history"
  - id: g02135-v3-user-guide
    resource: https://nsidc.org/sites/default/files/g02135-v003-userguide_1_1.pdf
    title: "Sea Ice Index Version 3 user guide: the near-real-time and final sections of the record, the NRTSI and GSFC inputs, the consistency comparisons between them, and the product history"
  - id: sii-special-report-28
    resource: https://nsidc.org/sites/default/files/documents/technical-reference/nsidc-special-report-28.pdf
    title: "Windnagel, Stafford, Fetterer and Meier, 2025, Sea Ice Index Version 4 Analysis, NSIDC Special Report 28 (July 2025): why Version 4 was released, the AMSR2 input, the end of the near-real-time and final distinction, gap filling, the pole hole change and the Version 3 to Version 4 extent comparison"
  - id: sii-special-report-19
    resource: https://nsidc.org/sites/default/files/nsidc-special-report-19.pdf
    title: "Windnagel, Brandt, Fetterer and Meier, 2017, Sea Ice Index Version 3 Analysis, NSIDC Special Report 19: the change of the monthly extent and area values to the average of the daily hemisphere-wide values"
  - id: noaadata-g02135
    resource: https://noaadata.apps.nsidc.org/NOAA/G02135/
    title: "The NOAA at NSIDC HTTPS archive of the Sea Ice Index: the north, south and seaice_analysis directories, the daily and monthly data, geotiff, images and shapefiles subdirectories, and the file names and CSV headers read on 2026-09-14"
  - id: daily-change-article
    resource: https://nsidc.org/data/user-resources/help-center/why-daily-change-sea-ice-extent-northern-hemisphere-larger-beginning-each-month
    title: "NSIDC help article: Why is the daily change in sea ice extent in the northern hemisphere larger at the beginning of each month? (the monthly valid ice masks and land spillover)"
  - id: nsidc-0051-dataset
    resource: nsidc-0051-sea-ice-concentration.md
    title: "This bundle's NSIDC-0051 dataset concept, the input record through December 2024"
  - id: nsidc-0803-page
    resource: https://nsidc.org/data/nsidc-0803/versions/2
    title: "NSIDC product page: AMSR2 Daily Polar Gridded Sea Ice Concentrations, Version 2, the input from 1 January 2025"
status: draft
stale_after: 2027-03-14
---

# G02135 Sea Ice Index, Version 4

**Identity and archive.** The Sea Ice Index is a source of consistent
sea ice extent and concentration images and of extent and area values
for the whole Arctic and the whole Antarctic, from November 1978 to
the present, with trends and anomalies against the 1981 through 2010
reference period; its stated purpose is a quick look at hemisphere-wide
change, and its monthly products are the ones it recommends for trend
analysis because errors in the daily product average out and daily
variation is often weather.[^g02135-page][^g02135-user-guide] It is a
NOAA at NSIDC product, not a NASA DAAC product: the citation names the
National Snow and Ice Data Center as publisher (Fetterer, Knowles,
Meier, Savoie, Windnagel and Stafford, 2025, DOI 10.7265/a98x-0f50),
its maintenance and distribution are supported by the NOAA at NSIDC
team with funding from NOAA's National Centers for Environmental
Information and other NOAA programs, with assistance from the NSIDC
NASA DAAC, and the files are served from the NOAA archive at
https://noaadata.apps.nsidc.org/NOAA/G02135/ over plain HTTPS rather
than through Earthdata, so no login is
required.[^g02135-page][^g02135-user-guide][^noaadata-g02135] The
product page carries a notice that the data set was changed to a Basic
level of service for funding reasons.[^g02135-page] Version 4 was
released in July 2025; Version 3 (DOI 10.7265/N5K072F8) is retired with
coverage 26 October 1978 to 31 July 2025, and its images and values
before 1 January 2025 were not reprocessed in Version 4 because the
SSMIS input did not change.[^g02135-v3-page][^g02135-user-guide][^sii-special-report-28]

**Inputs and the record's joins.** Version 4 has two data sources:
NSIDC-0051, the Goddard NASA Team record, for October 1978 through
December 2024, and NSIDC-0803, the AMSR2 daily polar gridded sea ice
concentrations, from 1 January 2025 to the present; the near-real-time
NSIDC-0081 product that Version 3 used for its most recent 6 to 18
months is no longer used, and the "near-real-time" and "final" labels
of Version 3 are gone from images dated 2025 onward.[^g02135-user-guide][^g02135-v3-user-guide][^sii-special-report-28]
The AMSR2 record was started on 1 January 2025 rather than mid-year so
that the sensor does not change during the Arctic melt season; the
AMSR2 brightness temperatures are resampled and smoothed to resemble
SSMIS before the NASA Team retrieval, and over 1 January to 30 June
2025 the Version 4 extents differ from the Version 3 SSMIS extents by
less than 0.2 million km2 (mean 0.05) in the Northern Hemisphere and
less than 0.15 million km2 (mean 0.04) in the Southern, with the AMSR2
value lower on about 80 percent of Northern Hemisphere days; the
report states that this affects derived extent trends and that the
resampling does not fully achieve a zero-mean
difference.[^sii-special-report-28] The instrument periods inside the
NSIDC-0051 part of the record (SMMR to 20 August 1987, F8, F11 and F13
SSM/I, F17 SSMIS from 1 January 2008) carry their own intercalibrated
joins (its own gotcha).[^g02135-user-guide][^nsidc-0051-dataset]

**Extent and area.** Daily extent is the sum of the areas of all grid
cells with concentration of 15 percent or greater, with each cell's
true area taken from the NSIDC-0771 cell-area files (382 to 664 km2 in
the northern grid, 443 to 664 km2 in the southern), and the region not
imaged around the North Pole assumed to be entirely ice covered above
15 percent and so counted in extent.[^g02135-user-guide] Monthly extent
and area are the averages of the daily hemisphere-wide values over the
month, a method adopted in Version 3 (October 2017) so that the monthly
values match what a user obtains by averaging the daily file; the
monthly images are still made from the monthly mean concentration
field with the 15 percent cutoff, so an extent read off a monthly image
and the monthly value in the file are different
quantities.[^g02135-user-guide][^sii-special-report-19] Area is the
same sum with each cell weighted by its concentration, over the cells
at 15 percent or more, and excludes the pole hole, so area is always
less than extent (its own gotcha).[^g02135-user-guide] The guide states
that the 15 percent cutoff is somewhat arbitrary, that 20 or 30 percent
gives different numbers with similar trends, and that the extent
values have uncertain significance taken individually and are useful
in a temporal series.[^g02135-user-guide]

**The pole hole in this product.** Four Arctic pole hole masks are
overlaid on the input before extent and area are computed: SMMR
(1.19 million km2, radius 611 km, 84.5 N) through July 1987, SSM/I
(0.31 million km2, 311 km, 87.2 N) August 1987 through December 2007,
SSMIS (0.029 million km2, 94 km, 89.18 N) January 2008 through
31 December 2024, and AMSR2 (0.064 million km2, a rounded square of
255 km width inside a circle at 88.5 N) from January 2025.[^g02135-user-guide][^sii-special-report-28]
Because extent counts the hole as ice and area excludes it, the
Northern Hemisphere monthly area series has documented discontinuities
at the August to September 1987 boundary and at the December 2007 to
January 2008 boundary, and the August 1987 area value has been removed
from the file; the monthly concentration anomaly and trend images use
the largest (SMMR) hole for the whole series to keep them continuous
(its own gotcha).[^g02135-user-guide]

**Files.** The archive splits into north, south and seaice_analysis;
under north and south sit daily and monthly, each with data, geotiff,
images and (monthly) shapefiles, and the geotiff and images directories
are further split by year and month (YYYY/XX_MMM) for daily files and
by month (XX_MMM) for monthly ones.[^g02135-user-guide][^noaadata-g02135]
The daily extent file (N_seaice_extent_daily_v4.0.csv and its southern
twin) has two header rows and the columns Year, Month, Day, Extent and
Missing in millions of km2, and Source Data, the path of the input
file or files; the listing read on 2026-09-14 showed rows from
26 October 1978 to 12 September 2026, NSIDC-0051 paths through
31 December 2024 and NSIDC-0803 paths from 1 January 2025 (the
1 January 2025 row names the NSIDC-0803 files for 1 and 2 January and
the NSIDC-0051 file for 31 December 2024), extent to three decimal
places, and SMMR-era rows every other day.[^g02135-user-guide][^noaadata-g02135] The monthly files
(N_01_extent_v4.0.csv through N_12_extent_v4.0.csv and the S files)
carry year, mo, source_dataset (NSIDC-0051 or NSIDC-0803), region,
extent and area, with -9999 where a month could not be computed; the
September file read the same day shows extent 7.05 and area 4.58 for
1979, 4.27 and 2.82 for 2007, 4.35 and 2.91 for 2024 from NSIDC-0051,
and 4.75 and 3.08 for 2025 from NSIDC-0803, and the August file carries
-9999 area for 1987.[^g02135-user-guide][^noaadata-g02135] The
climatology files hold the 1981 to 2010 mean, standard deviation and
the 10th, 25th, 50th, 75th and 90th percentiles of daily extent by day
of year; daily and monthly GeoTIFFs are named
N_20250901_concentration_v4.0.tif, N_20250901_extent_v4.0.tif,
N_197909_concentration_v4.0.tif and so on; seaice_analysis holds the
regional and hemispheric spreadsheets, among them
Sea_Ice_Index_Monthly_Data_by_Year_G02135_v4.0.xlsx and the Meier 2007
Arctic region mask.[^g02135-user-guide][^noaadata-g02135]

## Uncertainty

- **Concentration accuracy sets the floor.** The guide cites plus or
  minus 5 percent in winter and plus or minus 15 percent in summer for
  a grid cell's Arctic concentration, with larger differences reported
  against operational charts; the ice edge is where cells cross
  15 percent, a 15 percent contour that matched aircraft ice edges in
  the March 1988 study behind the convention, while a broad diffuse
  edge is sometimes missed at concentrations as high as 60 percent
  and the 25 km cells do not represent a marginal ice zone
  well.[^g02135-user-guide] Extent images are more reliable than
  concentration images because the emissivity contrast between water
  and ice is large even at low concentration.[^g02135-user-guide]
- **Daily values are provisional and can change.** With AMSR2 input,
  scattered missing cells are filled on the first pass by copying the
  previous day and on the next day's pass by averaging the days on
  either side, and the daily extent is rewritten, so a value downloaded
  on one day may differ slightly the next; a whole missing day is
  filled from its neighbours only when the following day has data, and
  two or more consecutive missing days get no rows; cells that remain
  missing are summed into the Missing column, which cannot simply be
  added to extent.[^g02135-user-guide][^sii-special-report-28]
- **Masks and the month boundary.** The Northern Hemisphere valid ice
  masks from National Ice Center climatologies change each month, and
  with the imperfect land spillover correction this produces a larger
  day-to-day extent change at the start of a month, especially in
  summer.[^daily-change-article][^g02135-user-guide]
- **Gaps and bad days in the record.** No values for 3 December 1987
  to 13 January 1988; every-other-day values in the SMMR period; the
  14 September 1984 extent is in error and provided for completeness;
  a one-day change larger than 500,000 km2 raises an operator
  flag.[^g02135-user-guide]
- **The input records' own uncertainty**: the Goddard record's
  seasonal accuracy, residual weather effects, sensor transitions and
  the AMSR2 differences are those of NSIDC-0051 and
  NSIDC-0803.[^nsidc-0051-dataset][^nsidc-0803-page]

## Known issues

- [sea-ice-pole-hole-by-sensor](../gotchas/sea-ice-pole-hole-by-sensor.md):
  extent counts the hole as ice and area excludes it, so the area
  series steps at the mask changes by design.
- [sea-ice-extent-is-not-area](../gotchas/sea-ice-extent-is-not-area.md):
  the two columns answer different questions and the monthly image
  and the monthly value use different averaging.
- [sea-ice-nrt-versus-final](../gotchas/sea-ice-nrt-versus-final.md):
  the record joins NSIDC-0051 to NSIDC-0803 at 1 January 2025 and,
  in Version 3, to NSIDC-0081 for its most recent months.
- [sea-ice-sensor-transitions](../gotchas/sea-ice-sensor-transitions.md):
  the SMMR, SSM/I, SSMIS and AMSR2 joins leave documented residual
  steps.
- [sea-ice-nasa-team-versus-bootstrap](../gotchas/sea-ice-nasa-team-versus-bootstrap.md):
  the Index is a NASA Team product; a Bootstrap extent is a different
  series.
- [polar-stereographic-not-latlon](../gotchas/polar-stereographic-not-latlon.md):
  the GeoTIFFs are on EPSG 3411 and 3412, and the Index itself uses
  the true cell areas rather than 625 km2.
- Monthly averages conflate a temporal and a spatial average: a cell
  at 50 percent for a month may have been fully ice covered for half
  the month and open for the other half.[^g02135-user-guide]

**Verification.** The Version 4 and Version 3 product pages, the
Version 4 user guide, the near-real-time and consistency sections of
the Version 3 guide, Special Report 28 and the summary of Special
Report 19 were read on 2026-09-14, and the NOAA archive listing was
walked the same day: the directory tree, the daily and monthly file
names, the CSV headers and the rows quoted above come from the files
themselves, and no GeoTIFF was
opened.[^g02135-page][^g02135-v3-page][^g02135-user-guide][^g02135-v3-user-guide][^sii-special-report-28][^sii-special-report-19][^noaadata-g02135]
One inconsistency between sources is recorded: the Version 4 guide's
Table 1 ends the F17 SSMIS usage period on 31 December 2022 and its
temporal coverage section dates the Goddard input to 31 December 2020
"as of January 2017", while its data sources section, the NSIDC-0051
guide and the monthly files themselves carry NSIDC-0051 through
December 2024; this concept follows the data sources section and the
files.[^g02135-user-guide][^noaadata-g02135] The help article on the
month-boundary extent change was read the same
day.[^daily-change-article]

[^g02135-page]: NSIDC product page, Sea Ice Index Version 4
[^g02135-v3-page]: NSIDC product page, Sea Ice Index Version 3
[^g02135-user-guide]: Sea Ice Index Version 4 user guide, NSIDC
[^g02135-v3-user-guide]: Sea Ice Index Version 3 user guide, NSIDC
[^sii-special-report-28]: Windnagel and others, 2025, NSIDC Special Report 28
[^sii-special-report-19]: Windnagel and others, 2017, NSIDC Special Report 19
[^noaadata-g02135]: The NOAA at NSIDC archive listing of G02135
[^daily-change-article]: NSIDC help article on the month-boundary extent change
[^nsidc-0051-dataset]: This bundle's NSIDC-0051 dataset concept
[^nsidc-0803-page]: NSIDC product page, NSIDC-0803 Version 2
