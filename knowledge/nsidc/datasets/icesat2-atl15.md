---
type: dataset
spheres: [cryosphere]
title: "ICESat-2 ATL15 gridded Antarctic and Arctic land ice height change"
description: "Quarterly surface height difference surfaces relative to the ATL14 reference surface at 1 January 2020, and their rates over quarterly to six-year windows, on 1, 10, 20 and 40 km polar stereographic grids for Antarctica and six Arctic regions, derived from the ATL11 along-track time series; per-cell error fields and an ice-area field ship with the data."
tags: [icesat2, atl15, atl14, atl11, land-ice, height-change, nsidc, cryosphere]
generated: { by: knowledge-seeder/claude, at: 2026-09-13T20:30:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-13T21:10:06Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/129 }
resource: https://nsidc.org/data/atl15/versions/5
version: "Version 5 (DOI 10.5067/ATLAS/ATL15.005; derived from ATL11 version 7), CMR concept C3892628343-NSIDC_CPRD, verified 2026-09-13: 40 granules named ATL15_<region>_0329_<nn>km_005_02.nc, that is cycles 3 through 29, with granule time ranges 2019-01-01 through 2025-11-20; the user guide's version history dates the release covering cycle 29 to March 2026 and the retirement of version 4 to June 2026"
sources:
  - id: atl15-page
    resource: https://nsidc.org/data/atl15/versions/5
    title: "NSIDC product page: ATLAS/ICESat-2 L3B Gridded Antarctic and Arctic Land Ice Height Change, Version 5 (overview, projections, coverage, the documents it links)"
  - id: atl15-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/atl15-v005-userguide.pdf
    title: "ATL15 Version 5 user guide (NSIDC, published December 2025, updated June 2026): file contents, naming, resolution, geolocation, temporal resolution, quality and the version history"
  - id: atl14-15-atbd
    resource: https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl14_atl15_atbd_v005.pdf
    title: "Smith and others, ICESat-2 Algorithm Theoretical Basis Document for Land Ice DEM (ATL14) and Land Ice Height Change (ATL15), release 005, November 2025 (DOI 10.5067/7INP6DQAWRC2)"
  - id: atl15-data-dict
    resource: https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl15_data_dict_v5.pdf
    title: "ATL15 data dictionary, version 5: every group and variable with its dimensions, units and description"
  - id: atl14-15-known-issues
    resource: https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl14_atl15_known_issues_v005.pdf
    title: "Known issues in ATL14 and ATL15, release 005"
  - id: cmr-atl15
    resource: https://cmr.earthdata.nasa.gov/search/collections.json?short_name=ATL15
    title: "CMR collection record for ATL15 (provider NSIDC_CPRD), with its granule list"
  - id: smith-2020
    resource: https://doi.org/10.1126/science.aaz5845
    title: "Smith and others, 2020, Pervasive ice sheet mass loss reflects competing ocean and atmosphere processes, Science 368, 1239 to 1242 (the reference use of ICESat and ICESat-2 height change for mass balance)"
status: stable
stale_after: 2027-03-13
---

# ICESat-2 ATL15 gridded Antarctic and Arctic land ice height change

**Identity.** ATL15 is the gridded version of the ATL11 slope-corrected
land ice height time series: land ice height changes and change rates
for the Antarctic ice sheet and regions around the Arctic, at four
spatial resolutions (1, 10, 20 and 40 km), in netCDF-4, from
1 January 2019 to the most current processing, north of 59 N and south
of 60 S.[^atl15-page][^atl15-user-guide] It is produced together with
ATL14, the 100 m reference digital elevation model for 1 January 2020,
by one least-squares algorithm that fits a surface height and its
quarterly changes to the ATL11 data; ATL14 is the snapshot, ATL15 the
coarser 3-month height-change maps intended for visualization and for
integrated regional volume change.[^atl14-15-atbd] One granule covers
one region at one resolution: Antarctica in four quadrants split along
the 90 degree meridians (A1 to A4), Arctic Canada North (CN) and South
(CS), Greenland and its peripheral ice caps (GL), Iceland (IS),
Svalbard (SV) and the Russian Arctic (RA); the file name carries the
first and last complete cycle included, so ATL15_SV_0329_20km_005_02.nc
holds cycles 3 through 29 at 20 km.[^atl15-user-guide] The CMR record
(concept C3892628343-NSIDC_CPRD, version 005) listed 40 granules on
2026-09-13, all at cycles 03 through 29 and revision 02, with granule
time ranges ending on 2025-11-19 or 2025-11-20 by region.[^cmr-atl15] A reprocessed granule keeps its name and
increments the revision; NSIDC deletes the superseded one, and the
highest revision is the one to use.[^atl15-user-guide]

**Structure.** The delta_h group holds the height difference between
the model surface at each quarterly epoch and the reference surface,
which is the ATL14 surface at the reference date 1 January 2020
(decimal year 2020.0), so delta_h at that epoch is zero by
construction; the time axis is in days since the ATLAS epoch, midnight
at the start of 1 January 2018.[^atl14-15-atbd][^atl15-data-dict]
The 1 km files add data_count, misfit_rms and misfit_scaled_rms for
the fit, and every resolution carries ice_area, the ice-covered area
of each cell in square metres, which is time-varying where the ice
front mask changes (Antarctica, and Greenland on a quarterly mask) and
where the inferred surface falls below the EGM2008
geoid.[^atl15-user-guide][^atl14-15-atbd] The height-change rates are
in the groups dhdt_lag1 (quarterly), dhdt_lag4 (annual), dhdt_lag8
(biennial), dhdt_lag12, dhdt_lag16, dhdt_lag20 and dhdt_lag24
(triennial through hexennial); each rate is the difference between two
height-difference surfaces the stated interval apart divided by that
interval, its time value is the midpoint of the two epochs, and its
ice_area is the minimum ice extent over the differencing period; more
lag groups are added as the mission lengthens.[^atl15-user-guide][^atl14-15-atbd]
The grids are square in projected coordinates: the NSIDC Sea Ice Polar
Stereographic North projection (EPSG 3413, standard latitude 70 N,
central meridian 45 W) for the Arctic regions and the Antarctic Polar
Stereographic projection (EPSG 3031, standard latitude 71 S, central
meridian 0) for Antarctica, on the WGS 84 ellipsoid with WGS 84 as the
vertical datum, so the area of a cell differs from the square of the
grid spacing and ice_area is the area that accounts for the
distortion.[^atl15-user-guide][^atl14-15-atbd] The solution is computed
on 61 by 61 km tiles (44 km near the pole), matched at the edges and
mosaicked; the reduced resolutions are area-weighted averages of the
1 km fields, and a tile_stats group records per-tile fit
statistics.[^atl15-user-guide][^atl14-15-atbd] Ocean tides and the
dynamic atmosphere are removed from floating ice using CATS2008 in
Antarctica and AOTIM-5-2018 in the Arctic, with a scaling across
grounding zones; the ATBD contains no firn, density or glacial
isostatic adjustment term, so the product is surface height change
and nothing else (its own gotcha).[^atl14-15-atbd]

**Land-ice use.** The product's stated purpose is height-change
patterns and integrated regional volume change, with error fields
intended to allow error propagation into mass-change
estimates.[^atl14-15-atbd] The reference use is Smith and others 2020,
which turns ICESat and ICESat-2 height change into grounded and
floating mass change with a firn model, a glacial isostatic adjustment
model, elastic compensation, tides and the inverse barometer applied
on top of the altimetry.[^smith-2020] A regional volume change from
ATL15 is a sum of delta_h or dhdt times ice_area over the cells of a
named region, which is the area weighting the ATBD itself applies
when it forms the reduced-resolution averages, with ice_area as the
ice-covered area of each cell; the epoch and the lag group are part
of the statement.[^atl14-15-atbd][^atl15-data-dict]

## Uncertainty

- **Per-cell error fields ship with the product**: delta_h_sigma, the
  estimated error in the height change relative to the 1 January 2020
  surface, with the same three dimensions as delta_h, and dhdt_sigma in
  every lag group.[^atl15-data-dict][^atl14-15-atbd] They are formal
  errors of the least-squares model: per-point errors from the ATL11
  uncorrelated error, correlated errors through the bias parameters
  tied to surface slope and geolocation error, and a remaining scatter
  term added in quadrature; the calculation is carried out on the
  preliminary tile solutions because the matched solution's errors
  appear artificially small.[^atl14-15-atbd] Zero error values that
  appeared where the ice mask had fine structure were removed in
  version 4 by smoothing the error estimates before
  interpolation.[^atl15-user-guide]
- **The reduced resolutions exist for their errors.** The 10, 20 and
  40 km averages are provided primarily because their error estimates
  account for the per-track correlated errors in the ICESat-2 data, and
  the lagged rates exist because their errors use the model covariance
  that is not distributed; a user-formed average or difference of 1 km
  cells has no such error.[^atl14-15-atbd]
- **Sampling sets the resolution, not the grid.** Across-track beam
  pair spacing is 3 km and repeat-track spacing reaches 15 km in
  southern Greenland; each track is measured at most four times a year
  and clouds remove as many as half of those, so the product resolves
  year-to-year change at a few kilometres but season-to-season change
  noisily, with striping that follows the track timing where episodic
  snowfall or melt occurs.[^atl14-15-atbd] data_count and delta_h_sigma
  are the fields that show where coverage limits the
  estimate.[^atl15-user-guide]
- **The early record is weaker.** Precise pointing on the reference
  ground tracks began in April 2019; earlier data enter only through
  crossovers, so the first epoch (the first quarter of 2019) is less
  well constrained than later ones, the 2018 epoch has been dropped
  since version 4, and cycle 2 has much lower data density than the
  rest.[^atl14-15-atbd][^atl14-15-known-issues]
- **Ice fronts and grounding zones.** The product excludes the height
  change of ice front advance and retreat through the time-varying
  mask, with less reliable coverage for smaller Antarctic shelves and
  none for Arctic fronts outside Greenland; near grounding lines the
  tide correction is a scaled model in Antarctica around the Ross and
  Filchner-Ronne shelves and absent elsewhere, so grounding zone
  height changes are less accurate.[^atl14-15-known-issues]
- **Isolated cells with large errors.** A few points marked as ice but
  unconnected to the ice sheet and unsampled by repeat tracks carry
  poorly constrained solutions; their error estimates of tens to
  hundreds of metres are the way to find them.[^atl14-15-known-issues]
- **What the formal errors do not contain**: the firn air content
  change and the density assumption that turn a height change into a
  mass change (its own gotcha), and the choice of region boundary (its
  own gotcha).

## Known issues

- [atl15-height-change-is-not-mass-change](../gotchas/atl15-height-change-is-not-mass-change.md):
  ATL15 is surface height; a mass number needs a firn model and its
  uncertainty.
- [atl15-delta-h-reference-epoch](../gotchas/atl15-delta-h-reference-epoch.md):
  delta_h is relative to the 1 January 2020 surface and each lag group
  has its own window.
- [polar-stereographic-not-latlon](../gotchas/polar-stereographic-not-latlon.md):
  the grids are in projected metres; ice_area, not the grid spacing
  squared, is the cell area.
- [ice-sheet-boundaries-and-drainage-basins](../gotchas/ice-sheet-boundaries-and-drainage-basins.md):
  a per-basin total names the basin definition it used.
- The four Antarctic quadrants overlap by one pixel in the 40 km
  product.[^atl14-15-known-issues]

**Verification.** The product page, the version 5 user guide, the
ATBD release 005, the data dictionary and the known issues note were
read in full on 2026-09-13, and the CMR collection and granule records
were read the same day.[^atl15-page][^atl15-user-guide][^atl14-15-atbd][^atl15-data-dict][^atl14-15-known-issues][^cmr-atl15]
Two of those documents disagree on one date: the user guide's quality
section says cycles 1 and 2 comprise all data before April 2020,
while the ATBD says the planned precise pointing on the reference
ground tracks began in April 2019 and that release 004 and later
carry data from 2019 onward; this concept follows the ATBD, and the
user guide's date reads as a typo to raise with
NSIDC.[^atl15-user-guide][^atl14-15-atbd] Smith and others 2020 was
read in full from the NASA technical reports server copy and its
record verified against the Crossref registry the same day; the
journal page sits behind a bot check.[^smith-2020] No granule was
opened from the drafting session (the Earthdata Cloud host was
unreachable), so the variable names and dimensions above come from
the data dictionary.[^atl15-data-dict]

[^atl15-page]: NSIDC product page, ATL15 Version 5
[^atl15-user-guide]: ATL15 Version 5 user guide, NSIDC
[^atl14-15-atbd]: ATL14/ATL15 ATBD, release 005, doi:10.5067/7INP6DQAWRC2
[^atl15-data-dict]: ATL15 data dictionary, version 5
[^atl14-15-known-issues]: Known issues in ATL14 and ATL15, release 005
[^cmr-atl15]: CMR collection record for ATL15
[^smith-2020]: Smith and others, 2020, Science, doi:10.1126/science.aaz5845
