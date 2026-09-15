---
type: dataset
spheres: [cryosphere]
title: "MEaSUREs ITS_LIVE regional ice velocity mosaics, and the InSAR velocity maps they succeed"
description: "Annual mean surface velocity mosaics for sixteen glacier regions including Greenland and Antarctica, 1984 through 2022 plus a 2014 to 2022 climatology, at 120 m on polar stereographic or UTM grids, synthesized from tens of millions of Landsat, Sentinel-1 and Sentinel-2 image-pair velocities by autoRIFT; error fields and an image-pair count ship with the data, and the older MEaSUREs Greenland and Antarctic InSAR velocity maps are the alternatives."
tags: [its-live, measures, ice-velocity, velocity-mosaic, autorift, greenland, antarctica, nsidc, cryosphere]
generated: { by: knowledge-seeder/claude, at: 2026-09-13T20:30:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-13T21:10:06Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/129 }
resource: https://nsidc.org/data/nsidc-0776/versions/2
version: "NSIDC-0776 Version 2 (DOI 10.5067/JQ6337239C96; the user guide's version history dates Version 2 to July 2025), CMR concept C3618748415-NSIDC_CPRD with 546 granules, annual files 1984 through 2022 and one climatological file per region for 2014 through 2022, verified 2026-09-13; Version 1 (DOI 10.5067/6II6VW8LLWJ7, C3298525133-NSIDC_CPRD, 1985 through 2018, Landsat only) is still listed. Alternatives verified the same day: NSIDC-0725 Version 5 (C3298042936-NSIDC_CPRD, 2014-12-01 through 2023-11-30), NSIDC-0478 Version 2 (C3291179132-NSIDC_CPRD, 2000-09-03 through 2018-05-31), NSIDC-0670 Version 1 (C3291956575-NSIDC_CPRD, 1995-12-01 through 2015-10-31) and NSIDC-0484 Version 2 (C3291177469-NSIDC_CPRD, 1996-01-01 through 2016-12-31)"
sources:
  - id: nsidc-0776-page
    resource: https://nsidc.org/data/nsidc-0776/versions/2
    title: "NSIDC product page: MEaSUREs ITS_LIVE Regional Glacier and Ice Sheet Surface Velocities, Version 2 (Gardner and others 2025, DOI 10.5067/JQ6337239C96)"
  - id: nsidc-0776-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/nsidc-0776-v002-userguide.pdf
    title: "NSIDC-0776 Version 2 user guide: parameters of the annual and climatological files, regions and projections, processing, error computation and the map-unit velocity statement"
  - id: its-live-site
    resource: https://its-live.jpl.nasa.gov/
    title: "ITS_LIVE project site (NASA JPL): the dataset list, the monthly and annual mosaic description, the STAC and Zarr cloud access, and the citations it asks for"
  - id: its-live-v1-description
    resource: https://its-live-data.s3.amazonaws.com/documentation/ITS_LIVE-Regional-Glacier-and-Ice-Sheet-Surface-Velocities.pdf
    title: "ITS_LIVE Regional Glacier and Ice Sheet Surface Velocities product description, version 1 (June 2019): the parameter table with date, dt and count"
  - id: its-live-known-issues
    resource: https://its-live-data.s3.amazonaws.com/documentation/ITS_LIVE-Regional-Glacier-and-Ice-Sheet-Surface-Velocities-Known-Issues.pdf
    title: "ITS_LIVE Regional Glacier and Ice Sheet Surface Velocities known issues (June 2019): surface skipping and locking, inter-sensor bias, sensor precision bias in velocity magnitude"
  - id: gardner-2018
    resource: https://doi.org/10.5194/tc-12-521-2018
    title: "Gardner and others, 2018, Increased West Antarctic and unchanged East Antarctic ice discharge over the last 7 years, The Cryosphere 12, 521 to 547 (the autoRIFT method paper the product asks to be cited)"
  - id: nsidc-0725-page
    resource: https://nsidc.org/data/nsidc-0725/versions/5
    title: "NSIDC product page: MEaSUREs Greenland Annual Ice Sheet Velocity Mosaics from SAR and Landsat, Version 5 (Joughin 2023, DOI 10.5067/USBL3Z8KF9C3)"
  - id: nsidc-0725-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/nsidc-0725-v005-userguide.pdf
    title: "NSIDC-0725 user guide (published August 2022, updated September 2024): parameters vv, vx, vy, ex, ey and dT, the 1 December to 30 November measurement years, the error-weighted aggregation and the quality statement"
  - id: nsidc-0478-page
    resource: https://nsidc.org/data/nsidc-0478/versions/2
    title: "NSIDC product page: MEaSUREs Greenland Ice Sheet Velocity Map from InSAR Data, Version 2 (Joughin and others 2015, DOI 10.5067/OC7B04ZM9G6Q)"
  - id: nsidc-0478-user-guide
    resource: https://nsidc.org/sites/default/files/nsidc-0478-v002-userguide.pdf
    title: "NSIDC-0478 Version 2 user guide: eleven winter mosaics, vv, vx, vy, ex, ey, 500 m before 2014 and 200 m after, EPSG 3413"
  - id: nsidc-0670-page
    resource: https://nsidc.org/data/nsidc-0670/versions/1
    title: "NSIDC product page: MEaSUREs Multi-year Greenland Ice Sheet Velocity Mosaic, Version 1 (Joughin and others 2016, DOI 10.5067/QUA5Q9SVMSJG)"
  - id: nsidc-0670-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/nsidc-0670-v001-userguide.pdf
    title: "NSIDC-0670 user guide: the 1995 to 2015 error-weighted multi-year mosaic at 250 m, and why it is not a uniform average"
  - id: nsidc-0484-page
    resource: https://nsidc.org/data/nsidc-0484/versions/2
    title: "NSIDC product page: MEaSUREs InSAR-Based Antarctica Ice Velocity Map, Version 2 (Rignot, Mouginot and Scheuchl 2017, DOI 10.5067/D7GK8F5J8M8R)"
  - id: nsidc-0484-user-guide
    resource: https://nsidc.org/sites/default/files/nsidc-0484-v002-userguide.pdf
    title: "NSIDC-0484 Version 2 user guide: VX, VY, ERRX, ERRY, STDX, STDY and CNT at 450 m on the 71 S polar stereographic grid, 1996 to 2016"
  - id: cmr-its-live
    resource: https://cmr.earthdata.nasa.gov/search/collections.json?keyword=ITS_LIVE
    title: "CMR collection records for the ITS_LIVE products and the MEaSUREs velocity maps (provider NSIDC_CPRD)"
status: stable
stale_after: 2027-03-13
---

# MEaSUREs ITS_LIVE regional ice velocity mosaics

**Identity.** ITS_LIVE (Inter-Mission Time Series of Land Ice Velocity
and Elevation) is a NASA MEaSUREs project at JPL that processes optical
and radar image pairs into glacier and ice sheet surface velocities;
its project site describes regional velocity mosaics at 120 m, monthly
and annual, from 1985 to the present, served from the cloud through a
STAC catalogue and Zarr data cubes as well as archived at
NSIDC.[^its-live-site] The archived regional product is NSIDC-0776:
Version 2 holds mean annual surface velocities for 1984 through 2022
plus climatological means for 2014 through 2022, for sixteen
glacier-covered regions of the Randolph Glacier Inventory version 6
(Alaska through Antarctic and Subantarctic, Greenland periphery
included), on 120 m grids, derived by the autonomous Repeat Image
Feature Tracking chain (autoRIFT) from Landsat 4, 5, 7, 8 and 9,
Sentinel-1A and 1B and Sentinel-2A and 2B; annual coverage is nearly
complete for all regions after 2013 and scarce before, for want of
imagery and radiometric quality.[^nsidc-0776-page][^nsidc-0776-user-guide]
Version 1 (1985 through 2018, Landsat only, eight regions at 240 m or
120 m) remains a separate collection with its own DOI, and its product
description carries an effective-date field the version 2 annual
files do not.[^its-live-v1-description][^cmr-its-live] The CMR record
for Version 2 (concept C3618748415-NSIDC_CPRD) listed 546 granules on
2026-09-13, named NSIDC-0776_RGI<id>_<year>_V02.0.nc for the annual
files and NSIDC-0776_RGI<id>_2014-2022_V02.0.nc for the
climatology.[^cmr-its-live][^nsidc-0776-user-guide] The project site
and the user guide both ask that Gardner and others 2018 be cited
beside the data.[^its-live-site][^nsidc-0776-user-guide][^gardner-2018]

**Structure.** An annual file carries v (the hypotenuse of vx and vy),
vx and vy (the mean annual velocity of a sinusoidal fit to each
component), v_error, vx_error and vy_error, count (the number of image
pairs in the error-weighted least-squares fit), the landice and
floatingice masks, the mapping variable that describes the coordinate
reference system, and x and y in projection metres; the fill value is
minus 32767 for velocities and 32767 for errors, and 0 for
count.[^nsidc-0776-user-guide] The climatological file adds the
component trends dvx_dt and dvy_dt and their projection dv_dt onto the
flow direction, the seasonal amplitude and phase of each component,
outlier_percent, the sensor group and its inclusion flag, dt_max (the
sensor-specific maximum image-pair separation admitted), and v, vx and
vy defined with a time intercept of 1 January 2018.[^nsidc-0776-user-guide]
Regions north of 55 N are on the NSIDC Sea Ice Polar Stereographic
North grid (EPSG 3413), the Antarctic region on the Antarctic Polar
Stereographic grid (EPSG 3031), High Mountain Asia on a Lambert
projection for Northern Asia, and the rest on local UTM zones; vx and
vy are rotated into the map x and y directions of the mosaic's
projection.[^nsidc-0776-user-guide] Version 2 velocities are computed
in map units and not corrected for projection scale, so they are the
horizontal velocities that would be measured in map space, which can
differ from ground velocities by up to a few percent depending on the
projection and location; Version 1 had corrected this
distortion.[^nsidc-0776-user-guide] The annual values are an
error-weighted least-squares fit of all image-pair velocities whose
spans overlap the year, each weighted by the fraction of the year it
covers and by the inverse square of its displacement error, after
tying each pair to stable ground, discarding pairs with large stable
shifts, removing skipping and locking errors, masking 2 km from the
glacier edge, and dropping velocities above 20,000 metres per year;
Sentinel-2 data are excluded where they double the seasonal
amplitude.[^nsidc-0776-user-guide]

**Alternatives and predecessors.** Four older MEaSUREs velocity maps
at NSIDC cover the two ice sheets with radar interferometry and
speckle tracking rather than the multi-sensor synthesis:

- NSIDC-0725 Version 5, Greenland annual ice sheet velocity mosaics
  from SAR and Landsat (Joughin): one mosaic per measurement year from
  1 December to 30 November, 2014 through 2023, posted at 200 m on
  EPSG 3413, with vv, vx, vy, the component errors ex and ey and a
  temporal offset dT in days between the weighted measurement date and
  the midpoint of the year, from Sentinel-1, TerraSAR-X and TanDEM-X
  and Landsat 8 and 9, as error-weighted averages of all data at each
  point with interferometric phase where possible; its guide states
  that the mosaics are not true annual averages and should not be used
  for inter-annual change in the interior above about
  2,000 m.[^nsidc-0725-page][^nsidc-0725-user-guide]
- NSIDC-0478 Version 2, the Greenland ice sheet velocity map from InSAR
  data: eleven winter mosaics from 2000/2001 on, at 500 m before 2014
  and 200 m after, with vv, vx, vy, ex and ey on EPSG 3413 and a
  shapefile of the source image pairs; the CMR record spans
  2000-09-03 through 2018-05-31.[^nsidc-0478-page][^nsidc-0478-user-guide][^cmr-its-live]
- NSIDC-0670 Version 1, the multi-year Greenland mosaic: one
  error-weighted average of RADARSAT, ALOS PALSAR, TerraSAR-X, ERS
  tandem and Landsat 8 data collected between 1995 and 2015, at 250 m,
  with vx, vy, ex and ey; its guide states that it is not a uniformly
  averaged velocity for the twenty years and that a coastal glacier's
  velocity may have fluctuated wildly within it.[^nsidc-0670-page][^nsidc-0670-user-guide]
- NSIDC-0484 Version 2, the InSAR-based Antarctica ice velocity map
  (Rignot, Mouginot and Scheuchl): one map at 450 m on the 71 S polar
  stereographic grid from data collected 1996 through 2016, with VX,
  VY, the errors ERRX and ERRY, the standard deviations STDX and STDY
  and the scene count CNT; its guide states that ERRX and ERRY indicate
  relative quality rather than absolute error.[^nsidc-0484-page][^nsidc-0484-user-guide]

## Uncertainty

- **Error fields ship with every product, and each guide says how far
  to trust them.** In NSIDC-0776 the error of an image-pair velocity is
  the standard deviation of the component velocities over stable
  ground after the geolocation offset correction, or the root sum of
  squares of the two images' pointing uncertainty where no stable
  surface is in view, updated to the standard deviation of the pair
  against the annual mean once the pair is co-registered in the
  mosaic; the guide states that this formal propagation typically
  produces errors that are unrealistically low, and that v_error,
  vx_error and vy_error together with count are to be used as
  qualitative error metrics.[^nsidc-0776-user-guide] In NSIDC-0725 the
  errors represent the average behaviour of the data, can be much
  lower or higher locally, and are correlated over large areas, so a
  difference between two mosaics that exceeds the errors over a few
  percent of the ice sheet is not by itself significant; the guide
  also states that the interior errors are well under 1 metre per
  year after recalibration.[^nsidc-0725-user-guide] NSIDC-0484's
  errors are relative quality, with STDX, STDY and CNT beside
  them.[^nsidc-0484-user-guide]
- **Systematic biases the errors do not carry.** Feature tracking can
  lock onto stationary radiometric features (skipping), sensors differ
  in bias (Landsat 4 and 5 read about 5 metres per year slow against
  Landsat 8 over High Mountain Asia glaciers in the cited study), and
  the velocity magnitude of a noisier sensor is biased high because
  magnitude errors follow a Rice distribution; components, or
  magnitudes projected onto a common flow direction, keep a symmetric
  error.[^its-live-known-issues]
- **Effective date and coverage.** An annual mosaic is a composite
  whose image pairs are not evenly spread over the year: NSIDC-0725
  reports the temporal skew as dT, discards data with a skew beyond
  half the output interval so the time-stamp error is at most about
  183 days, and states that seasonal availability of optical imagery
  can weight mid-summer over mid-winter; NSIDC-0776 reports count and
  states the coverage limits before 2013 (its own
  gotcha).[^nsidc-0725-user-guide][^nsidc-0776-user-guide]
- **Map-space velocities.** NSIDC-0776 Version 2 velocities carry the
  projection scale distortion, up to a few percent; a flux gate drawn
  in the same projection needs no scale correction to its
  cross-section, while a comparison with a GPS station does need the
  velocity corrected for map distortion.[^nsidc-0776-user-guide]
- **Posting is not resolution.** NSIDC-0725 is posted at 200 m but
  its true resolution ranges from a few hundred metres to 1.5 km, and
  a narrow glacier's speed is an average over moving ice and
  stationary rock.[^nsidc-0725-user-guide]

## Known issues

- [velocity-mosaic-epochs-and-gaps](../gotchas/velocity-mosaic-epochs-and-gaps.md):
  a mosaic's effective date and coverage are part of any flux
  statement, and a discharge needs ice thickness from
  [BedMachine](bedmachine-greenland-antarctica.md), described in this
  bundle.
- [polar-stereographic-not-latlon](../gotchas/polar-stereographic-not-latlon.md):
  the grids are projected metres, the velocities are map-space
  velocities, and area per cell varies.
- [ice-sheet-boundaries-and-drainage-basins](../gotchas/ice-sheet-boundaries-and-drainage-basins.md):
  a per-basin discharge names the basin and gate definition it used.

**Verification.** The NSIDC product pages for NSIDC-0776, NSIDC-0725,
NSIDC-0478, NSIDC-0670 and NSIDC-0484 and each one's user guide were
read in full on 2026-09-13, as were the ITS_LIVE project site and the
version 1 product description and known issues documents it links,
and the CMR collection records for every product named
above.[^nsidc-0776-page][^nsidc-0776-user-guide][^nsidc-0725-page][^nsidc-0725-user-guide][^nsidc-0478-page][^nsidc-0478-user-guide][^nsidc-0670-page][^nsidc-0670-user-guide][^nsidc-0484-page][^nsidc-0484-user-guide][^its-live-site][^its-live-v1-description][^its-live-known-issues][^cmr-its-live]
The NSIDC-0725 guide the version 5 page links still carries Version 4
in its running header while its version history and file names are
version 5.[^nsidc-0725-user-guide] Gardner and others 2018 is cited
on its Crossref record (title, authors, journal, year, volume and
pages verified the same day) and its abstract; the journal site was
not reachable from the drafting session.[^gardner-2018]

[^nsidc-0776-page]: NSIDC product page, NSIDC-0776 Version 2
[^nsidc-0776-user-guide]: NSIDC-0776 Version 2 user guide
[^its-live-site]: ITS_LIVE project site, NASA JPL
[^its-live-v1-description]: ITS_LIVE regional velocities product description, version 1
[^its-live-known-issues]: ITS_LIVE regional velocities known issues
[^gardner-2018]: Gardner and others, 2018, The Cryosphere, doi:10.5194/tc-12-521-2018
[^nsidc-0725-page]: NSIDC product page, NSIDC-0725 Version 5
[^nsidc-0725-user-guide]: NSIDC-0725 user guide
[^nsidc-0478-page]: NSIDC product page, NSIDC-0478 Version 2
[^nsidc-0478-user-guide]: NSIDC-0478 Version 2 user guide
[^nsidc-0670-page]: NSIDC product page, NSIDC-0670 Version 1
[^nsidc-0670-user-guide]: NSIDC-0670 user guide
[^nsidc-0484-page]: NSIDC product page, NSIDC-0484 Version 2
[^nsidc-0484-user-guide]: NSIDC-0484 Version 2 user guide
[^cmr-its-live]: CMR collection records, ITS_LIVE and MEaSUREs velocity maps
