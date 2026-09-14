---
okf_version: "0.2"
---

# gesdisc bundle (GES DISC atmosphere and hydrology)

The GES DISC knowledge bundle: the Goddard Earth Sciences Data and
Information Services Center's atmospheric and hydrologic products
(MERRA-2 first), as reviewable concepts with sources, statuses and
steward sign-off. OKF v0.2 conformant (okf_version: "0.2"; the vendored
spec text lives in marketplace docs/upstream). Every concept is a draft
until the steward promotes it after review, and a confirmation from the
GES DISC or the product teams is invited on each and never required.
The hydrology plugin's own IMERG and NLDAS-2 concepts stay in its
bundle; a concept here names them where it depends on them. This
bundle's eval cases live in open-science-pillars/agent-evals under
merra2/cases/, one per high-severity gotcha, and their registration
in the evals manifests is the coordinator's step, not this bundle's.

What this bundle claims, for the people who know the data: [DIGEST.md](DIGEST.md).

## datasets

- [MERRA-2: the GMAO atmospheric reanalysis, 1980 onward, as the file collections a user meets at GES DISC](datasets/merra-2.md), status: draft

## gotchas

- [PRECTOTCORR is the observation-corrected precipitation the land surface saw and PRECTOT is the atmosphere's own: a water budget that mixes them carries the correction as a residual](gotchas/merra2-prectotcorr-versus-prectot.md), severity high, status: draft
- [Time-averaged MERRA-2 collections are stamped at the centre of the interval and instantaneous ones on the hour: a join on the stamp alone is half an hour off](gotchas/merra2-time-stamp-conventions.md), severity medium, status: draft
- [MERRA-2 is four production streams joined at 1992, 2001 and 2011, with reprocessed months carrying their own prefix, and an observing system whose entries leave documented steps: a long series is not one homogeneous record](gotchas/merra2-stream-boundaries-and-discontinuities.md), severity medium, status: draft
- [The 0.625 by 0.5 degree MERRA-2 grid is a regular latitude-longitude grid: cell area falls toward the poles, no area variable ships, and a plain mean is not a global mean](gotchas/merra2-grid-weights.md), severity low, status: draft
- [A MERRA-2 short name encodes time treatment, frequency, vertical structure and variable group, and the same variable name lives in several collections: a search by variable alone lands on the wrong one](gotchas/merra2-collection-short-names.md), severity medium, status: draft

## recipes

(none yet)
