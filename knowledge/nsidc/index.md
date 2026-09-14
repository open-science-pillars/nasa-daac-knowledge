---
okf_version: "0.2"
---

# nsidc bundle (NSIDC DAAC land ice and sea ice)

The NSIDC DAAC knowledge bundle, the cryosphere's first: ICESat-2 ATL15
gridded land ice height change, the MEaSUREs ice velocity mosaics
(ITS_LIVE and the older InSAR maps), the NASA Team sea ice
concentration record (NSIDC-0051) and the NOAA at NSIDC Sea Ice Index
(G02135) that is built from it, as reviewable concepts with
sources, statuses and steward sign-off. OKF v0.2 conformant
(okf_version: "0.2"; the vendored spec text lives in marketplace
docs/upstream). Every concept is a draft today; the steward promotes
one once it has been reviewed, and a confirmation from the NSIDC DAAC
or the product teams is invited on each and never required. The mass
side of land ice (the GRACE mascons) lives in the podaac bundle, and
the ice thickness a discharge needs (BedMachine) is not yet in this
bundle; both are named where a concept here depends on them.

What this bundle claims, for the people who know the data: [DIGEST.md](DIGEST.md).

## datasets

- [ICESat-2 ATL15 gridded Antarctic and Arctic land ice height change](datasets/icesat2-atl15.md), status: stable
- [MEaSUREs ITS_LIVE regional ice velocity mosaics, and the InSAR velocity maps they succeed](datasets/its-live-ice-velocity.md), status: stable
- [NSIDC-0051 NASA Team sea ice concentration from Nimbus-7 SMMR and DMSP SSM/I and SSMIS, Version 2](datasets/nsidc-0051-sea-ice-concentration.md), status: draft
- [G02135 Sea Ice Index, Version 4: NOAA at NSIDC daily and monthly sea ice extent, area, images and GeoTIFFs from the NASA Team concentration records](datasets/sea-ice-index-g02135.md), status: draft

## gotchas

- [ATL15 height change is not mass change: the conversion needs a firn model and a density assumption the product does not carry](gotchas/atl15-height-change-is-not-mass-change.md), severity high, status: draft
- [ATL15 delta_h is relative to the 1 January 2020 reference surface, and each lagged rate has its own window](gotchas/atl15-delta-h-reference-epoch.md), severity medium, status: stable
- [The grids are polar stereographic metres, not latitude and longitude: cell area varies, and a sum without the true cell area biases a total](gotchas/polar-stereographic-not-latlon.md), severity medium, status: stable
- [An annual velocity mosaic is a composite of image pairs with its own effective date and count, and a discharge needs ice thickness from another product](gotchas/velocity-mosaic-epochs-and-gaps.md), severity medium, status: stable
- [Ice sheet boundaries and drainage basins differ by definition: a per-basin number names the basin set it used](gotchas/ice-sheet-boundaries-and-drainage-basins.md), severity medium, status: stable
- [The Arctic pole hole differs by sensor and each product treats it differently: an Arctic total that ignores it steps at the sensor changes](gotchas/sea-ice-pole-hole-by-sensor.md), severity high, status: draft
- [The 15 percent threshold defines extent, and extent is not area: the two series answer different questions and are not interchangeable](gotchas/sea-ice-extent-is-not-area.md), severity medium, status: draft
- [Near-real-time and final sea ice concentration differ in input and processing, and a series that mixes NSIDC-0081, NSIDC-0051 and NSIDC-0803 steps at the join](gotchas/sea-ice-nrt-versus-final.md), severity medium, status: draft
- [NASA Team and Bootstrap concentrations are different retrievals from the same brightness temperatures: they differ where ice is thin, melting or marginal, and a series or a comparison that mixes them reads the algorithm as change](gotchas/sea-ice-nasa-team-versus-bootstrap.md), severity medium, status: draft
- [Sensor transitions (SMMR to SSM/I, F8 to F11 to F13 to F17, and on to AMSR2) leave steps that the intercalibration reduces and does not remove](gotchas/sea-ice-sensor-transitions.md), severity medium, status: draft
