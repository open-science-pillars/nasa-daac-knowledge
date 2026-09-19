---
okf_version: "0.2"
---

# nsidc bundle (NSIDC DAAC land ice and sea ice)

The NSIDC DAAC knowledge bundle, the cryosphere's first: ICESat-2 ATL15
gridded land ice height change, the MEaSUREs ice velocity mosaics
(ITS_LIVE and the older InSAR maps), the BedMachine ice thickness and
bed maps of Greenland and Antarctica, ICESat-2 ATL10 sea ice
freeboard, the NASA Team sea ice concentration record (NSIDC-0051)
and the NOAA at NSIDC Sea Ice Index (G02135) that is built from it,
as reviewable concepts with sources, statuses and steward sign-off. OKF v0.2 conformant
(okf_version: "0.2"; the vendored spec text lives in marketplace
docs/upstream). The six BedMachine and ATL10 concepts, the
ice sheet mass balance closure (an attested computation with its
recipe and run skill, the bundle's first) and the four land ice anchor
concepts (the published multi-method assessment a closure run is read
against, the firn model air content term the closure subtracts, and
their two gotchas) are drafts; the
rest are stable after the reviews recorded in log.md, and a
confirmation from the NSIDC DAAC or the product teams is invited on
each and never required. The mass
side of land ice (the GRACE mascons) lives in the podaac bundle and is
named where a concept here depends on it; the ice thickness a
discharge needs (BedMachine) is now in this bundle, and the closure
reads the podaac bundle's mascon product beside this bundle's
altimetry and firn terms.

What this bundle claims, for the people who know the data: [DIGEST.md](DIGEST.md).

## datasets

- [ICESat-2 ATL15 gridded Antarctic and Arctic land ice height change](datasets/icesat2-atl15.md), status: stable
- [MEaSUREs ITS_LIVE regional ice velocity mosaics, and the InSAR velocity maps they succeed](datasets/its-live-ice-velocity.md), status: stable
- [NSIDC-0051 NASA Team sea ice concentration from Nimbus-7 SMMR and DMSP SSM/I and SSMIS, Version 2](datasets/nsidc-0051-sea-ice-concentration.md), status: stable
- [G02135 Sea Ice Index, Version 4: NOAA at NSIDC daily and monthly sea ice extent, area, images and GeoTIFFs from the NASA Team concentration records](datasets/sea-ice-index-g02135.md), status: stable
- [BedMachine Greenland (IDBMG4 Version 6) and BedMachine Antarctica (NSIDC-0756 Version 4): ice thickness, bed topography, surface, error and mask on the polar stereographic grids](datasets/bedmachine-greenland-antarctica.md), status: stable
- [ICESat-2 ATL10 along-track sea ice freeboard, Version 7: total freeboard per ATL07 height segment on six beams, from a per-beam reference sea surface found in leads over 10 km sections](datasets/icesat2-atl10-freeboard.md), status: stable
- [IMBIE 2023: the reconciled multi-method assessment of Greenland and Antarctic ice sheet mass balance, 1992 to 2020](datasets/imbie-ice-sheet-assessment.md), status: draft
- [The firn model air content term the ice sheet closure subtracts: GEMB and GSFC-FDM firn air content as the ITS_LIVE elevation change products distribute it](datasets/firn-model-air-content.md), status: draft

## gotchas

- [ATL15 height change is not mass change: the conversion needs a firn model and a density assumption the product does not carry](gotchas/atl15-height-change-is-not-mass-change.md), severity high, status: stable
- [ATL15 delta_h is relative to the 1 January 2020 reference surface, and each lagged rate has its own window](gotchas/atl15-delta-h-reference-epoch.md), severity medium, status: stable
- [The grids are polar stereographic metres, not latitude and longitude: cell area varies, and a sum without the true cell area biases a total](gotchas/polar-stereographic-not-latlon.md), severity medium, status: stable
- [An annual velocity mosaic is a composite of image pairs with its own effective date and count, and a discharge needs ice thickness from another product](gotchas/velocity-mosaic-epochs-and-gaps.md), severity medium, status: stable
- [Ice sheet boundaries and drainage basins differ by definition: a per-basin number names the basin set it used](gotchas/ice-sheet-boundaries-and-drainage-basins.md), severity medium, status: stable
- [The Arctic pole hole differs by sensor and each product treats it differently: an Arctic total that ignores it steps at the sensor changes](gotchas/sea-ice-pole-hole-by-sensor.md), severity high, status: stable
- [The 15 percent threshold defines extent, and extent is not area: the two series answer different questions and are not interchangeable](gotchas/sea-ice-extent-is-not-area.md), severity medium, status: stable
- [Near-real-time and final sea ice concentration differ in input and processing, and a series that mixes NSIDC-0081, NSIDC-0051 and NSIDC-0803 steps at the join](gotchas/sea-ice-nrt-versus-final.md), severity medium, status: stable
- [NASA Team and Bootstrap concentrations are different retrievals from the same brightness temperatures: they differ where ice is thin, melting or marginal, and a series or a comparison that mixes them reads the algorithm as change](gotchas/sea-ice-nasa-team-versus-bootstrap.md), severity medium, status: stable
- [Sensor transitions (SMMR to SSM/I, F8 to F11 to F13 to F17, and on to AMSR2) leave steps that the intercalibration reduces and does not remove](gotchas/sea-ice-sensor-transitions.md), severity medium, status: stable
- [BedMachine thickness between flight lines is mass conservation or an interpolation, not a measurement: source, dataid and errbed say which method made each pixel and how far to trust it](gotchas/bedmachine-thickness-is-interpolated.md), severity high, status: draft
- [The BedMachine mask separates ocean, ice-free land, grounded ice and floating ice, and a discharge gate sits on grounded ice upstream of the grounding line, where the thickness is mass conservation and not hydrostatic](gotchas/bedmachine-mask-and-grounding-line.md), severity medium, status: stable
- [ATL10 freeboard is not sea ice thickness: total freeboard is the air and snow interface above the sea surface, and the conversion to thickness needs a snow depth and three densities the product does not carry](gotchas/atl10-freeboard-is-not-thickness.md), severity high, status: draft
- [The strong and weak beams of each ATLAS pair differ four to one in energy, and so in photon rate, segment length and precision: which of gtXl and gtXr is strong depends on sc_orient, and a freeboard statistic names its beams](gotchas/atl10-strong-versus-weak-beams.md), severity medium, status: stable
- [The firn air content correction is a spread between models, not a measured term: it sets the uncertainty of an altimetric mass rate and it changes sign inside the record](gotchas/firn-air-content-spread-dominates-the-altimetric-mass-rate.md), severity high, status: draft
- [An assessment's method groups are not independent measurements of the same thing: they share corrections and records, they cover different ice, and the reconciled uncertainty shrinks by the square root of a count](gotchas/assessment-method-groups-are-not-independent.md), severity medium, status: draft

## computations

- [Ice sheet mass balance closure from GRACE-FO mascons against altimetric volume change with a firn correction (attested)](computations/ice-sheet-balance.md), status: stable

## recipes

- [Closing an ice sheet's mass balance: gravimetry against firn-corrected altimetry, and the input-output estimate this bundle cannot yet make](recipes/ice-sheet-balance.md), status: stable
