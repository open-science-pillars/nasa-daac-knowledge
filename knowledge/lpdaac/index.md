---
okf_version: "0.2"
---

# lpdaac bundle (LP DAAC land surface)

The LP DAAC knowledge bundle: the Land Processes Distributed Active
Archive Center's land surface products (the Harmonized Landsat and
Sentinel-2 surface reflectance first, then NASADEM and the MOD11 land
surface temperature, then the MODIS vegetation indices, leaf area
index and FPAR, and gross and net primary productivity), as
reviewable concepts with
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
- [NASADEM version 1: SRTM reprocessed with ICESat control and void-filled from ASTER GDEM and ALOS PRISM, on 1 arc second tiles with EGM96 heights](datasets/nasadem.md), status: stable
- [MOD11A1 and MOD11A2 version 6.1: Terra MODIS clear-sky land surface temperature and classified emissivity, daily and eight-day, on 1 km sinusoidal tiles](datasets/mod11-land-surface-temperature.md), status: stable
- [MOD13Q1 and MOD13A1 version 6.1: Terra MODIS NDVI and EVI composited over 16 days by a constrained-view maximum value rule, with the input reflectances, the view geometry, the composite day of year and two quality layers, on 250 m and 500 m sinusoidal tiles](datasets/mod13-vegetation-indices.md), status: draft
- [MOD15A2H version 6.1: Terra MODIS leaf area index and FPAR retrieved by a biome look-up table inversion of red and near-infrared reflectance, composited over eight days by maximum FPAR, with retrieval standard deviations and two quality bytes, on 500 m sinusoidal tiles](datasets/mod15-lai-fpar.md), status: draft
- [MOD17A2H and MOD17A3HGF version 6.1: Terra MODIS gross primary productivity summed over eight days and gap-filled annual net primary production from a radiation use efficiency model driven by MOD15 FPAR and LAI, GMAO reanalysis weather and a fixed biome parameter table, on 500 m sinusoidal tiles](datasets/mod17-gpp-npp.md), status: draft

## gotchas

- [The HLS Fmask layer is bit-packed: cloud, shadow, snow, water and aerosol are bits to mask, not class values to compare](gotchas/hls-fmask-is-bit-packed.md), severity high, status: stable
- [HLS L30 and S30 keep their sensors' band numbers: B05, B06, B07, B09, B10 and B11 name different wavelengths in the two products](gotchas/hls-band-names-differ.md), severity medium, status: stable
- [HLS reflectance is harmonized, not native: a nadir BRDF adjustment on both products and a bandpass adjustment on S30 make it differ from Landsat Collection 2 and Sentinel-2 surface reflectance](gotchas/hls-harmonized-not-native.md), severity medium, status: stable
- [HLS MGRS tiles overlap, each in its own UTM zone: a mosaic or an area sum that concatenates tiles counts the overlap twice](gotchas/hls-mgrs-tile-overlap.md), severity medium, status: stable
- [HLS reflectance is int16 scaled by 0.0001 with -9999 as fill, the thermal bands by 0.01, the QA byte by nothing with 255 as fill, and some granules do not say so in their tags](gotchas/hls-scale-and-fill.md), severity low, status: stable
- [NASADEM heights are orthometric on the EGM96 geoid while GNSS, ICESat and ICESat-2, altimetry and lidar heights are ellipsoidal on WGS84: a comparison that skips the geoid separation is off by that separation, a smooth field of metres to tens of metres that looks like a DEM bias](gotchas/nasadem-orthometric-versus-ellipsoidal.md), severity high, status: draft
- [NASADEM heights are not all SRTM: the NUM layer says which pixels are ASTER GDEM, ALOS PRISM, an older SRTM edit or interpolation, and inside the HGT granule only it separates the February 2000 radar heights from the optical fill acquired years later](gotchas/nasadem-void-fill-and-source-layer.md), severity medium, status: stable
- [MOD11 is a clear-sky product observed at a varying local time: every value is one clear moment, a daily or eight-day mean is a mean of the clear moments that existed, and the observation hour is a layer to read, not a constant](gotchas/mod11-clear-sky-and-view-time.md), severity high, status: draft
- [MOD11 day and night fields are different quantities: two observations at different hours and angles, with their own quality bytes and clear-sky coverage layers, and neither is a daily temperature](gotchas/mod11-day-and-night-are-different.md), severity medium, status: stable
- [MOD11 Emis_31 and Emis_32 are assigned from land cover class, not retrieved: they change only when the class, the snow cover or the arid-zone adjustment changes, and they are the emissivity the temperature retrieval assumed](gotchas/mod11-emissivity-is-classified.md), severity low, status: stable
- [NDVI and EVI are empirical indices of red and near-infrared contrast, not measures of leaf area, biomass or green cover: NDVI compresses toward a ceiling over dense canopy, EVI is a different quantity with its own coefficients and a two-band fallback, and a difference or ratio of index values is not a proportional difference in vegetation](gotchas/index-is-not-a-state-variable.md), severity high, status: draft
- [A MOD13 16-day composite is not an image of one day: each pixel is the observation the constrained-view maximum value rule selected, its date is in the composite day of the year layer, adjacent pixels can come from different days and geometries, and the date in the file name is the period's date, not the observation's](gotchas/composite-day-of-year-layer.md), severity medium, status: draft
- [MOD15 LAI and FPAR and MOD17 GPP and NPP are model outputs, not measurements: a look-up table inversion by biome and a light use efficiency model with fixed biome parameters and reanalysis weather, each with a quality layer that says which algorithm path or which filled input produced the value, and with land cover codes stored inside the data type above the valid range](gotchas/lai-and-gpp-are-model-outputs.md), severity medium, status: draft
- [MODIS sinusoidal cells are equal-area but not 250 m or 500 m squares and not aligned with latitude and longitude: the nominal 500 m cell is 463 m on the 6371007.181 m sphere, a tile's bounding rectangle in degrees is not its footprint, and a reprojection to a geographic grid changes cell areas, resamples the indices and breaks the bit fields and the day of the year layer](gotchas/sinusoidal-grid-cell-area.md), severity low, status: draft

## recipes

(none yet)
