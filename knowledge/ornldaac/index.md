---
okf_version: "0.2"
---

# ornldaac bundle (ORNL DAAC surface meteorology and biogeochemistry)

The ORNL DAAC knowledge bundle: the Oak Ridge National Laboratory
Distributed Active Archive Center's biogeochemical, surface
meteorology and biomass products (Daymet first, then GEDI L4A and
L4B), as reviewable concepts with sources, statuses and steward
sign-off. OKF v0.2 conformant
(okf_version: "0.2"; the vendored spec text lives in marketplace
docs/upstream). Every concept is a draft until the steward promotes it
after review, and a confirmation from the ORNL DAAC or the product
teams is invited on each and never required.

What this bundle claims, for the people who know the data: [DIGEST.md](DIGEST.md).

## datasets

- [Daymet Version 4 (release R1): daily surface weather on a 1 km grid for North America, Hawaii and Puerto Rico](datasets/daymet-v4.md), status: stable
- [GEDI L4A footprint aboveground biomass density (Version 3): a modeled biomass density and its prediction standard error for every 25 m laser footprint the mission sampled within about 51.6 degrees of the equator](datasets/gedi-l4a-footprint-biomass.md), status: draft
- [GEDI L4B gridded mean aboveground biomass density (Version 2.1): 1 km cell means inferred from the L4A footprint sample by hybrid estimation, with a standard error of the mean, the sample counts, a quality flag and the prediction stratum in ten GeoTIFF layers](datasets/gedi-l4b-gridded-biomass.md), status: draft

## gotchas

- [Every Daymet year has 365 days: leap years keep February 29 and drop December 31, so a positional or generated-date join misaligns after February in a leap year](gotchas/daymet-365-day-year.md), severity high, status: stable
- [The Daymet grid is Lambert conformal conic meters, not latitude and longitude: a cell is one square kilometer only on the standard parallels, and a lat/lon subset comes back as a projected box](gotchas/daymet-lcc-projection-and-cell-area.md), severity medium, status: stable
- [Tiles, mosaics and region files are three cuts of one estimate: the 2-degree tiles are mosaicked into the per-region files, and the three regions differ in extent, start year and service coverage](gotchas/daymet-tiles-mosaics-regions.md), severity medium, status: stable
- [Version 4 R1 re-derived every 2020 and 2021 file with corrected Canadian station inputs and changed no earlier year: a Version 4 file for those years is a different estimate under a different DOI](gotchas/daymet-v4-r1-correction.md), severity medium, status: stable
- [Daymet values are interpolated from stations, and the error is not the domain average: station-sparse and high-relief regions carry larger error, which the cross-validation files quantify and the derived variables lack](gotchas/daymet-station-sparse-error.md), severity low, status: stable
- [A GEDI footprint is a sample, not a pixel: the L4A footprints are 25 m spots 60 m apart along eight tracks 600 m apart, and a mean of the footprints in an area is a sample mean of a model output, not the area's biomass density](gotchas/gedi-footprint-is-not-a-pixel.md), severity high, status: draft
- [The L4B standard error is the hybrid estimator's standard error of the cell mean, built from the L4A model parameter covariance and the footprint clusters in the cell: a cell with few tracks carries a large one, at two tracks the estimator itself runs low, and the percent layer is capped at 100](gotchas/gedi-l4b-standard-error.md), severity medium, status: draft
- [Every shot the L4A algorithm could run on carries a biomass prediction, flagged rather than removed: l2a_quality_flag_rel3 and l4a_quality_flag_rel3 gate which footprints are fit for a prediction, degrade_include_flag and elev_highestreturn_outlier_flag gate which are fit for gridding, and the L4B sample is the gated one](gotchas/gedi-quality-and-degrade-flags.md), severity medium, status: draft
- [GEDI biomass is a model output, not a measurement: L4A AGBD is a linear model of L2A relative height metrics, calibrated on simulated waveforms and field plots and stratified by plant functional type and world region, so a footprint's value changes with the version's models and with the 1 km stratum it falls in](gotchas/gedi-biomass-is-a-model-output.md), severity medium, status: draft
- [GEDI observes only between about 51.6 degrees north and south: the L4A and L4B products carry no footprint or estimated cell for the boreal forest, and the file and record extents (85 degrees in the L4B grid, 56 north in the L4A collection record) are not coverage](gotchas/gedi-latitude-limits.md), severity low, status: draft

## recipes

(none yet)
