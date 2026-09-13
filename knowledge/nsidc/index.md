---
okf_version: "0.2"
---

# nsidc bundle (NSIDC DAAC land ice)

The NSIDC DAAC knowledge bundle, the cryosphere's first: ICESat-2 ATL15
gridded land ice height change and the MEaSUREs ice velocity mosaics
(ITS_LIVE and the older InSAR maps), as reviewable concepts with
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

- [ICESat-2 ATL15 gridded Antarctic and Arctic land ice height change](datasets/icesat2-atl15.md), status: draft
- [MEaSUREs ITS_LIVE regional ice velocity mosaics, and the InSAR velocity maps they succeed](datasets/its-live-ice-velocity.md), status: draft

## gotchas

- [ATL15 height change is not mass change: the conversion needs a firn model and a density assumption the product does not carry](gotchas/atl15-height-change-is-not-mass-change.md), severity high, status: draft
- [ATL15 delta_h is relative to the 1 January 2020 reference surface, and each lagged rate has its own window](gotchas/atl15-delta-h-reference-epoch.md), severity medium, status: draft
- [The grids are polar stereographic metres, not latitude and longitude: cell area varies, and a sum without the true cell area biases a total](gotchas/polar-stereographic-not-latlon.md), severity medium, status: draft
- [An annual velocity mosaic is a composite of image pairs with its own effective date and count, and a discharge needs ice thickness from another product](gotchas/velocity-mosaic-epochs-and-gaps.md), severity medium, status: draft
- [Ice sheet boundaries and drainage basins differ by definition: a per-basin number names the basin set it used](gotchas/ice-sheet-boundaries-and-drainage-basins.md), severity medium, status: draft
