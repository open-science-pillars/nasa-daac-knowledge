---
type: dataset
spheres: [hydrosphere]
title: "OSCAR version 2 surface currents (final, interim and near-real-time)"
description: "Daily 0.25-degree global near-surface currents diagnosed from gridded altimetry, reanalysis winds and SST with a geostrophic plus Ekman plus thermal-wind model and averaged over the top 30 m, in three collections of decreasing quality and latency; the files carry total and geostrophic components and no uncertainty field."
tags: [oscar, surface-currents, ekman, geostrophic, altimetry, level4, podaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-13T21:00:00Z }
resource: https://podaac.jpl.nasa.gov/dataset/OSCAR_L4_OC_FINAL_V2.0
version: "Version 2.0 in three POCLOUD collections, CMR-verified 2026-09-13: final OSCAR_L4_OC_FINAL_V2.0 (C2098858642-POCLOUD, DOI 10.5067/OSCAR-25F20, daily granules 1993-01-01 through 2026-01-16), interim OSCAR_L4_OC_INTERIM_V2.0 (C2102959417-POCLOUD, DOI 10.5067/OSCAR-25I20, 2020-01-01 through 2026-08-31 and ongoing) and near-real-time OSCAR_L4_OC_NRT_V2.0 (C2102958977-POCLOUD, DOI 10.5067/OSCAR-25N20, 2021-01-01 through 2026-09-03 and ongoing); the user handbook is dated October 2021"
status: draft
stale_after: 2027-03-13
sources:
  - id: podaac-final
    resource: https://podaac.jpl.nasa.gov/dataset/OSCAR_L4_OC_FINAL_V2.0
    title: "PO.DAAC collection page, OSCAR_L4_OC_FINAL_V2.0: description, DOI, variables, the user guide link and the citation (read 2026-09-13)"
  - id: podaac-interim
    resource: https://podaac.jpl.nasa.gov/dataset/OSCAR_L4_OC_INTERIM_V2.0
    title: "PO.DAAC collection page, OSCAR_L4_OC_INTERIM_V2.0 (read 2026-09-13)"
  - id: podaac-nrt
    resource: https://podaac.jpl.nasa.gov/dataset/OSCAR_L4_OC_NRT_V2.0
    title: "PO.DAAC collection page, OSCAR_L4_OC_NRT_V2.0 (read 2026-09-13)"
  - id: cmr-final
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2098858642-POCLOUD.umm_json
    title: "CMR collection record for the final collection: abstract, temporal extent, DOI, platforms and the documentation links; the granule search for the same concept gave the first and last daily files (read 2026-09-13)"
  - id: cmr-interim
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2102959417-POCLOUD.umm_json
    title: "CMR collection record for the interim collection, with its granule range (read 2026-09-13)"
  - id: cmr-nrt
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2102958977-POCLOUD.umm_json
    title: "CMR collection record for the near-real-time collection, with its granule range (read 2026-09-13)"
  - id: guide
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/oscar/open/L4/oscar_v2.0/docs/oscarv2guide.pdf
    title: "OSCAR v2.0 User's Handbook, Kathleen Dohan, Earth and Space Research, October 2021 (13 pages, read in full 2026-09-13): the model outline, the source datasets per quality level, the file format, the latency, the known problems and the differences from the third-degree product"
  - id: bonjean-2002
    resource: https://doi.org/10.1175/1520-0485(2002)032<2938:DMAAOT>2.0.CO;2
    title: "Bonjean and Lagerloef, 2002, Diagnostic model and analysis of the surface currents in the tropical Pacific Ocean, Journal of Physical Oceanography 32, 2938 to 2954: the OSCAR model formulation the handbook cites as reference 1"
  - id: lagerloef-1999
    resource: https://doi.org/10.1029/1999JC900197
    title: "Lagerloef, Mitchum, Lukas and Niiler, 1999, Tropical Pacific near-surface currents estimated from altimeter, wind, and drifter data, Journal of Geophysical Research: Oceans 104: the original geostrophic plus Ekman model calibrated by 15 m drogued drifters, with the beta-plane treatment at the equator"
  - id: dohan-2017
    resource: https://doi.org/10.1002/2017JC012961
    title: "Dohan, 2017, Ocean surface currents from satellite data, Journal of Geophysical Research: Oceans: the OSCAR project's statement of what it computes and why (simplified physics, satellite observations)"
  - id: mulet-2021
    resource: https://doi.org/10.5194/os-17-789-2021
    title: "Mulet and others, 2021, The new CNES-CLS18 global mean dynamic topography, Ocean Science 17, 789 to 808: the mean dynamic topography inside the absolute dynamic topography the final and interim products differentiate"
---

# OSCAR version 2 surface currents

**Identity.** Ocean Surface Current Analyses Real-time (OSCAR) is a
global, daily, 0.25-degree analysis of near-surface currents produced
by Earth and Space Research and archived at PO.DAAC as three
collections of one version: final, interim and near-real-time
(nrt).[^podaac-final][^podaac-interim][^podaac-nrt] It is a Level 4
diagnosed product, not a measurement: the velocity is calculated from
gridded sea surface height (absolute dynamic topography from
altimetry), reanalysis 10 m winds and an SST analysis with a
simplified physical model that combines geostrophy, wind-driven Ekman
flow and a thermal-wind adjustment, and the value in each cell is an
average over an assumed well-mixed top 30 m of the
ocean.[^cmr-final][^guide][^dohan-2017] The model descends from the
tropical Pacific studies of the 1990s and 2000s: a geostrophic plus
Ekman surface layer calibrated against 15 m drogued drifters, with the
equator treated separately because geostrophy fails
there.[^lagerloef-1999][^bonjean-2002] The `resource` above is the
final collection; the three collections share one handbook, one
version number and one file layout.[^guide]

**Structure.** One netCDF file per day, named
`oscar_currents_<level>_YYYYMMDD.nc`, holding four fields on a
719 by 1440 grid from 89.75S to 89.75N and 0 to 359.75E: `u` and `v`,
the zonal and meridional total surface current, and `ug` and `vg`, the
geostrophic component alone, all in metres per second with a fill
value of -999, a valid range of plus or minus 3 (velocities above
3 m/s are removed without further processing) and a `depth` attribute
of 15 m beside the comment that the value is an average over the top
30 m.[^guide][^podaac-final] Time is one value per file, days since
1990-01-01 on a Julian calendar, centred on the day, and the day's
value is a daily average.[^guide] The `source` attribute names the
inputs: for the final product the Copernicus SSALTO/DUACS delayed-time
absolute dynamic topography, ERA5 10 m winds and the Canadian
Meteorological Centre SST analysis (0.2-degree version 2 for 1993
through 2015, 0.1-degree version 3 from 2016).[^guide] The absolute
dynamic topography is the altimeter anomaly on the CNES-CLS18 mean
dynamic topography, so the geostrophic component inherits that mean
field and its own error.[^guide][^mulet-2021]

**The three collections.** Final uses delayed-time altimetry and ERA5
winds and has a latency the handbook puts at about 1.5 years (the
collection abstract says about one year); interim uses near-real-time
altimetry and ERA5 winds, about one month behind; nrt uses
near-real-time altimetry and NCEP/NCAR Reanalysis 1 winds, about two
days behind.[^guide][^cmr-final] On 2026-09-13 CMR held final granules
from 1993-01-01 through 2026-01-16, interim granules from 2020-01-01
through 2026-08-31 and nrt granules from 2021-01-01 through
2026-09-03, so the collections overlap over years rather than
abutting, and the same date can exist in all three with different
inputs.[^cmr-final][^cmr-interim][^cmr-nrt] The whole record was
computed once in early 2021 and has been produced in real time since,
with the source-data access dates coinciding with the files' creation
dates.[^guide] The gotcha on versions and latency carries what changes
between the levels and what a series across them measures.

## Uncertainty

- **No uncertainty field ships with the product.** The files carry the
  four velocity components and nothing else; the handbook's
  calibration section points to a validation page on the producer's
  website and, for the earlier third-degree product, to Dohan and
  Maximenko 2010.[^guide] That page could not be reached from the
  session that drafted this concept (the producer's host is blocked
  by the network policy), so the bundle holds no validation number
  for version 2.
- **What stands in.** The product is a model solution, so its error
  is dominated by what the model omits (the gotcha on the geostrophic
  plus Ekman formulation) and by the errors of its inputs: the
  handbook names high winds, rain, residual orbit error, optimal
  interpolation error and sparse coverage in the source fields, the
  smoothing inherent in gridded inputs and in the gradient
  calculation, inaccuracy within about 100 km of coastlines, and the
  weakest performance where eddies are not the dominant signal (the
  North Pacific gyre) and in the meridional component of strong zonal
  flows near the equator.[^guide]
- **The 30 m average is not a surface velocity and not a 15 m
  velocity.** The value is the layer average of the analytical
  solution over the top 30 m; the `depth` attribute of 15 m is the
  layer's midpoint, and a comparison against a drifter drogued at 15 m
  or a current meter at one depth is a comparison against a different
  quantity.[^guide][^lagerloef-1999]

## Known issues

- [oscar-is-geostrophic-plus-ekman](../gotchas/oscar-is-geostrophic-plus-ekman.md):
  the product is a diagnosed geostrophic plus Ekman plus thermal-wind
  current; tides, inertial motion and any other ageostrophic flow are
  absent by construction, and the equatorial band uses the model's own
  equatorial solution.
- [oscar-versions-and-latency](../gotchas/oscar-versions-and-latency.md):
  final, interim and nrt differ in their altimetry and wind inputs, so
  a series that steps from one to the next carries the input change
  as if it were the ocean's; version 2 also differs from the
  third-degree product in grid, cadence, equatorial model and
  smoothing.
- The final collection's SST input changes from the 0.2-degree to the
  0.1-degree Canadian analysis at the start of 2016, a documented
  inhomogeneity inside the one collection meant for long
  records.[^guide]
- The handbook is dated October 2021 and the collection metadata was
  last revised in July and August 2026; the handbook does not say
  whether the collections were reprocessed since the 2021
  computation.[^guide][^cmr-final]

[^podaac-final]: PO.DAAC collection page, OSCAR_L4_OC_FINAL_V2.0
[^podaac-interim]: PO.DAAC collection page, OSCAR_L4_OC_INTERIM_V2.0
[^podaac-nrt]: PO.DAAC collection page, OSCAR_L4_OC_NRT_V2.0
[^cmr-final]: CMR collection record, C2098858642-POCLOUD, and its granule range
[^cmr-interim]: CMR collection record, C2102959417-POCLOUD, and its granule range
[^cmr-nrt]: CMR collection record, C2102958977-POCLOUD, and its granule range
[^guide]: OSCAR v2.0 User's Handbook, Dohan, October 2021
[^bonjean-2002]: Bonjean and Lagerloef, 2002, Journal of Physical Oceanography, doi:10.1175/1520-0485(2002)032<2938:DMAAOT>2.0.CO;2
[^lagerloef-1999]: Lagerloef and others, 1999, Journal of Geophysical Research: Oceans, doi:10.1029/1999JC900197
[^dohan-2017]: Dohan, 2017, Journal of Geophysical Research: Oceans, doi:10.1002/2017JC012961
[^mulet-2021]: Mulet and others, 2021, Ocean Science, doi:10.5194/os-17-789-2021
