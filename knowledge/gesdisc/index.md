---
okf_version: "0.2"
---

# gesdisc bundle (GES DISC atmosphere and hydrology)

The GES DISC knowledge bundle: the Goddard Earth Sciences Data and
Information Services Center's atmospheric and hydrologic products
(MERRA-2 first, then the AIRS level 3 soundings, the OMI level 3
trace gases and the OCO-2 and OCO-3 solar-induced fluorescence Lite
files, with a connector concept for the GES DISC subsetter and
OPeNDAP routes), as reviewable concepts with sources, statuses and
steward sign-off. OKF v0.2 conformant (okf_version: "0.2"; the vendored
spec text lives in marketplace docs/upstream). Every concept is a draft
until the steward promotes it after review, and a confirmation from the
GES DISC or the product teams is invited on each and never required.
The hydrology plugin's own IMERG and NLDAS-2 concepts stay in its
bundle; a concept here names them where it depends on them. This
bundle's eval cases live in open-science-pillars/agent-evals under
merra2/cases/, airs/cases/ (the OMI row anomaly case lives under
airs/cases/ as well) and oco2/cases/, one per high-severity gotcha, and their registration
in the evals manifests is the coordinator's step, not this bundle's.

What this bundle claims, for the people who know the data: [DIGEST.md](DIGEST.md).

## datasets

- [MERRA-2: the GMAO atmospheric reanalysis, 1980 onward, as the file collections a user meets at GES DISC](datasets/merra-2.md), status: stable
- [AIRS version 7 level 3 temperature and water vapour: the daily and monthly 1 degree grids (AIRS3STD, AIRS3STM) as ascending and descending fields on fixed pressure levels with a count and a standard deviation beside every mean](datasets/airs-l3-temperature-humidity.md), status: stable
- [OMI level 3 nitrogen dioxide and total ozone: the daily OMNO2d 0.25 degree grid with its Weight field and the daily TOMS-like OMTO3d 1 degree grid, gridded from row-anomaly-screened level 2 retrievals since October 2004](datasets/omi-no2-and-ozone.md), status: stable
- [OCO-2 and OCO-3 solar-induced fluorescence Lite files: one netCDF-4 file per day of offset-corrected 757 and 771 nm retrievals per sounding, with a derived 740 nm value, a geometric daily correction factor, a three-level quality flag and a one-sigma uncertainty beside every value](datasets/oco2-sif-lite.md), status: stable

## gotchas

- [PRECTOTCORR is the observation-corrected precipitation the land surface saw and PRECTOT is the atmosphere's own: a water budget that mixes them carries the correction as a residual](gotchas/merra2-prectotcorr-versus-prectot.md), severity high, status: stable
- [Time-averaged MERRA-2 collections are stamped at the centre of the interval and instantaneous ones on the hour: a join on the stamp alone is half an hour off](gotchas/merra2-time-stamp-conventions.md), severity medium, status: stable
- [MERRA-2 is four production streams joined at 1992, 2001 and 2011, with reprocessed months carrying their own prefix, and an observing system whose entries leave documented steps: a long series is not one homogeneous record](gotchas/merra2-stream-boundaries-and-discontinuities.md), severity medium, status: stable
- [The 0.625 by 0.5 degree MERRA-2 grid is a regular latitude-longitude grid: cell area falls toward the poles, no area variable ships, and a plain mean is not a global mean](gotchas/merra2-grid-weights.md), severity low, status: stable
- [A MERRA-2 short name encodes time treatment, frequency, vertical structure and variable group, and the same variable name lives in several collections: a search by variable alone lands on the wrong one](gotchas/merra2-collection-short-names.md), severity medium, status: stable
- [AIRS level 3 profiles sit on fixed pressure levels, not model levels, and the lowest levels lie below the terrain: the per-level count falls to zero there, the layer water vapour is integrated below the surface, and a mean at 1000 or 925 hPa over land is a mean over the low ground only](gotchas/airs-pressure-levels-and-surface-mask.md), severity high, status: draft
- [AIRS ascending and descending grids are 1:30 PM and 1:30 AM local time with their own ensembles and their own 24-hour windows: an average of the two is a two-sample diurnal estimate, not a daily mean, and a daily file is not a calendar day](gotchas/airs-ascending-descending-nodes.md), severity medium, status: stable
- [The OMI row anomaly has removed cross-track rows since June 2007, growing in 2008 and 2009 and changing since: the level 2 flag names the rows, the level 3 grids drop them, and a series across the onset mixes a change in sampling with a change in the atmosphere](gotchas/omi-row-anomaly.md), severity high, status: draft
- [A level 3 cell is the average of however many retrievals of whatever quality fell in it, and the count or weight field is the only bound on that: an aggregate that drops it treats a one-retrieval cell as a full one, and the AIRS monthly mean changed its weighting between versions 6 and 7](gotchas/l3-count-field-bounds-a-cell.md), severity medium, status: stable
- [An anomaly names its climatology period: an AIRS or OMI departure is relative to a base period and a processing version, the records carry documented breaks (the 2021 Aqua manoeuvre, the January 2026 AIRS gap, the OMI row anomaly onset, the collection 4 reprocessings), and two anomalies on different bases differ by a number that is not a constant](gotchas/anomaly-names-its-climatology-period.md), severity low, status: stable
- [OCO-2 SIF is a radiance emitted by chlorophyll, not a photosynthesis rate: the file carries no gross primary production, the SIF to GPP relation is empirical, scale-dependent and varies with biome and physiology, and a SIF value read as GPP is a number with an unstated slope](gotchas/sif-is-not-photosynthesis.md), severity high, status: draft
- [OCO-2 SIF is two retrievals, at 757 and 771 nm, each corrected by a daily barren-surface offset, and the 740 nm field is formed from them by fixed factors: values at different wavelengths, adjusted against unadjusted, and version 10 against version 11 are different quantities](gotchas/sif-two-bands-and-offsets.md), severity medium, status: stable
- [OCO-2 SIF soundings are footprints under 1.3 by 2.25 km along a 10 km ground track, imprecise one by one and sampled once per overpass: a gridded mean is a mean of however many samples fell in the cell, it needs its count and standard error, and negative values belong in it](gotchas/sif-soundings-are-sparse.md), severity medium, status: stable
- [The Daily_SIF fields are the instantaneous retrievals times a clear-sky geometric factor: the daily correction factor is the ratio of the day's integrated cosine of the solar zenith angle to its value at the overpass, not an observed daily mean, and an instantaneous and a daily field are different quantities](gotchas/sif-daily-correction.md), severity low, status: stable

## recipes

(none yet)

## connectors

- [GES DISC subsetting and OPeNDAP access to MERRA-2, AIRS and the OCO SIF Lite files: Cloud OPeNDAP by granule URL with a DAP4 constraint, the Harmony enterprise subsetter by collection, bounding box, variables and time, and an Earthdata Login bearer token on every data request; the on-premises subsetter and OPeNDAP servers retire in September 2026](connectors/gesdisc-subsetter-opendap.md), status: stable
