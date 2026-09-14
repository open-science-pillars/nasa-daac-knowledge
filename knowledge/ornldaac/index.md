---
okf_version: "0.2"
---

# ornldaac bundle (ORNL DAAC surface meteorology and biogeochemistry)

The ORNL DAAC knowledge bundle: the Oak Ridge National Laboratory
Distributed Active Archive Center's biogeochemical and surface
meteorology products (Daymet first), as reviewable concepts with
sources, statuses and steward sign-off. OKF v0.2 conformant
(okf_version: "0.2"; the vendored spec text lives in marketplace
docs/upstream). Every concept is a draft until the steward promotes it
after review, and a confirmation from the ORNL DAAC or the product
teams is invited on each and never required.

What this bundle claims, for the people who know the data: [DIGEST.md](DIGEST.md).

## datasets

- [Daymet Version 4 (release R1): daily surface weather on a 1 km grid for North America, Hawaii and Puerto Rico](datasets/daymet-v4.md), status: draft

## gotchas

- [Every Daymet year has 365 days: leap years keep February 29 and drop December 31, so a calendar-date join misaligns after February in a leap year](gotchas/daymet-365-day-year.md), severity high, status: draft
- [The Daymet grid is Lambert conformal conic meters, not latitude and longitude: a cell is one square kilometer only on the standard parallels, and a lat/lon subset comes back as a projected box](gotchas/daymet-lcc-projection-and-cell-area.md), severity medium, status: draft
- [Tiles, mosaics and region files are three cuts of one estimate: the 2-degree tiles are mosaicked into the per-region files, and the three regions differ in extent, start year and service coverage](gotchas/daymet-tiles-mosaics-regions.md), severity medium, status: draft
- [Version 4 R1 re-derived every 2020 and 2021 file with corrected Canadian station inputs and changed nothing else: a Version 4 file for those years is a different estimate under a different DOI](gotchas/daymet-v4-r1-correction.md), severity medium, status: draft
- [Daymet values are interpolated from stations, and the error is not the domain average: station-sparse and high-relief regions carry larger error, which the cross-validation files quantify and the derived variables lack](gotchas/daymet-station-sparse-error.md), severity low, status: draft

## recipes

(none yet)
