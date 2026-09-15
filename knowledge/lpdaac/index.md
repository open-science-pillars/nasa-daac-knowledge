---
okf_version: "0.2"
---

# lpdaac bundle (LP DAAC land surface)

The LP DAAC knowledge bundle: the Land Processes Distributed Active
Archive Center's land surface products (the Harmonized Landsat and
Sentinel-2 surface reflectance first, then NASADEM and the MOD11 land
surface temperature), as reviewable concepts with
sources, statuses and steward sign-off. OKF v0.2 conformant
(okf_version: "0.2"; the vendored spec text lives in marketplace
docs/upstream). Every concept is a draft until the steward promotes it
after review, and a confirmation from the LP DAAC or the product teams
is invited on each and never required. The hydrology plugin's MOD16
evapotranspiration concepts stay in its bundle; a concept here names
them where it depends on them.

What this bundle claims, for the people who know the data: [DIGEST.md](DIGEST.md).

## datasets

- [HLS L30 version 2.0: Landsat 8 and 9 nadir BRDF-adjusted surface reflectance on 30 m MGRS tiles](datasets/hls-l30.md), status: stable
- [HLS S30 version 2.0: Sentinel-2 nadir BRDF-adjusted surface reflectance, bandpass-adjusted to Landsat, on 30 m MGRS tiles](datasets/hls-s30.md), status: stable
- [NASADEM version 1: SRTM reprocessed with ICESat control and void-filled from ASTER GDEM and ALOS PRISM, on 1 arc second tiles with EGM96 heights](datasets/nasadem.md), status: draft
- [MOD11A1 and MOD11A2 version 6.1: Terra MODIS clear-sky land surface temperature and classified emissivity, daily and eight-day, on 1 km sinusoidal tiles](datasets/mod11-land-surface-temperature.md), status: draft

## gotchas

- [The HLS Fmask layer is bit-packed: cloud, shadow, snow, water and aerosol are bits to mask, not class values to compare](gotchas/hls-fmask-is-bit-packed.md), severity high, status: stable
- [HLS L30 and S30 keep their sensors' band numbers: B05, B06, B07, B09, B10 and B11 name different wavelengths in the two products](gotchas/hls-band-names-differ.md), severity medium, status: stable
- [HLS reflectance is harmonized, not native: a nadir BRDF adjustment on both products and a bandpass adjustment on S30 make it differ from Landsat Collection 2 and Sentinel-2 surface reflectance](gotchas/hls-harmonized-not-native.md), severity medium, status: stable
- [HLS MGRS tiles overlap, each in its own UTM zone: a mosaic or an area sum that concatenates tiles counts the overlap twice](gotchas/hls-mgrs-tile-overlap.md), severity medium, status: stable
- [HLS reflectance is int16 scaled by 0.0001 with -9999 as fill, the thermal bands by 0.01, the QA byte by nothing with 255 as fill, and some granules do not say so in their tags](gotchas/hls-scale-and-fill.md), severity low, status: stable
- [NASADEM heights are orthometric on the EGM96 geoid while GNSS, ICESat and most satellite heights are ellipsoidal on WGS84: a comparison that skips the geoid separation is off by that separation, a smooth field of metres to tens of metres that looks like a DEM bias](gotchas/nasadem-orthometric-versus-ellipsoidal.md), severity high, status: draft
- [NASADEM heights are not all SRTM: the NUM layer says which pixels are ASTER GDEM, ALOS PRISM, an older SRTM edit or interpolation, and only it separates the February 2000 radar heights from the optical fill acquired years later](gotchas/nasadem-void-fill-and-source-layer.md), severity medium, status: draft
- [MOD11 is a clear-sky product observed at a varying local time: every value is one clear moment, a daily or eight-day mean is a mean of the clear moments that existed, and the observation hour is a layer to read, not a constant](gotchas/mod11-clear-sky-and-view-time.md), severity high, status: draft
- [MOD11 day and night fields are different quantities: two observations at different hours and angles, with their own quality bytes and clear-sky counts, and neither is a daily temperature](gotchas/mod11-day-and-night-are-different.md), severity medium, status: draft
- [MOD11 Emis_31 and Emis_32 are assigned from land cover class, not retrieved: they change only when the class, the snow cover or the arid-zone adjustment changes, and they are the emissivity the temperature retrieval assumed](gotchas/mod11-emissivity-is-classified.md), severity low, status: draft

## recipes

(none yet)
