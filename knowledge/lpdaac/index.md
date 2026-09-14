---
okf_version: "0.2"
---

# lpdaac bundle (LP DAAC land surface)

The LP DAAC knowledge bundle: the Land Processes Distributed Active
Archive Center's land surface products (the Harmonized Landsat and
Sentinel-2 surface reflectance first), as reviewable concepts with
sources, statuses and steward sign-off. OKF v0.2 conformant
(okf_version: "0.2"; the vendored spec text lives in marketplace
docs/upstream). Every concept is a draft until the steward promotes it
after review, and a confirmation from the LP DAAC or the product teams
is invited on each and never required. The hydrology plugin's MOD16
evapotranspiration concepts stay in its bundle; a concept here names
them where it depends on them.

What this bundle claims, for the people who know the data: [DIGEST.md](DIGEST.md).

## datasets

- [HLS L30 version 2.0: Landsat 8 and 9 nadir BRDF-adjusted surface reflectance on 30 m MGRS tiles](datasets/hls-l30.md), status: draft
- [HLS S30 version 2.0: Sentinel-2 nadir BRDF-adjusted surface reflectance, bandpass-adjusted to Landsat, on 30 m MGRS tiles](datasets/hls-s30.md), status: draft

## gotchas

- [The HLS Fmask layer is bit-packed: cloud, shadow, snow, water and aerosol are bits to mask, not class values to compare](gotchas/hls-fmask-is-bit-packed.md), severity high, status: draft
- [HLS L30 and S30 keep their sensors' band numbers: B05, B06, B07, B09, B10 and B11 name different wavelengths in the two products](gotchas/hls-band-names-differ.md), severity medium, status: draft
- [HLS reflectance is harmonized, not native: a nadir BRDF adjustment on both products and a bandpass adjustment on S30 make it differ from Landsat Collection 2 and Sentinel-2 surface reflectance](gotchas/hls-harmonized-not-native.md), severity medium, status: draft
- [HLS MGRS tiles overlap, each in its own UTM zone: a mosaic or an area sum that concatenates tiles counts the overlap twice](gotchas/hls-mgrs-tile-overlap.md), severity medium, status: draft
- [HLS reflectance is int16 scaled by 0.0001 with -9999 as fill, the thermal bands by 0.01, the QA byte by nothing with 255 as fill, and some granules do not say so in their tags](gotchas/hls-scale-and-fill.md), severity low, status: draft

## recipes

(none yet)
