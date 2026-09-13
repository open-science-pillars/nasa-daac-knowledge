---
type: dataset
spheres: [hydrosphere]
title: "OSCAR version 2 surface currents (final, interim and near-real-time)"
description: "Daily 0.25-degree global near-surface currents diagnosed from gridded altimetry, reanalysis winds and SST with a geostrophic plus Ekman plus thermal-wind model and averaged over the top 30 m, in three collections of decreasing quality and latency; the files carry total and geostrophic components and no uncertainty field."
tags: [oscar, surface-currents, ekman, geostrophic, altimetry, level4, podaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-13T21:00:00Z }
resource: https://podaac.jpl.nasa.gov/dataset/OSCAR_L4_OC_FINAL_V2.0
version: "Version 2.0 in three POCLOUD collections, CMR-verified 2026-09-13 with granule ranges from a first-and-last granule search the same day: final OSCAR_L4_OC_FINAL_V2.0 (C2098858642-POCLOUD, DOI 10.5067/OSCAR-25F20, daily granules 1993-01-01 through 2026-01-16), interim OSCAR_L4_OC_INTERIM_V2.0 (C2102959417-POCLOUD, DOI 10.5067/OSCAR-25I20, 2020-01-01 through 2026-08-31 and ongoing) and near-real-time OSCAR_L4_OC_NRT_V2.0 (C2102958977-POCLOUD, DOI 10.5067/OSCAR-25N20, 2021-01-01 through 2026-09-03 and ongoing); the user handbook is dated October 2021"
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
    title: "CMR collection record for the final collection: abstract, temporal extent (1993-01-01 to 2026-01-17), DOI, platforms, MetadataDates and the documentation links (read 2026-09-13)"
  - id: cmr-interim
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2102959417-POCLOUD.umm_json
    title: "CMR collection record for the interim collection: abstract, open-ended temporal extent from 2020-01-01 and MetadataDates (read 2026-09-13)"
  - id: cmr-nrt
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2102958977-POCLOUD.umm_json
    title: "CMR collection record for the near-real-time collection: abstract, open-ended temporal extent from 2021-01-01 and MetadataDates (read 2026-09-13)"
  - id: cmr-granules-final
    resource: https://cmr.earthdata.nasa.gov/search/granules.json?collection_concept_id=C2098858642-POCLOUD&page_size=1&sort_key=start_date
    title: "CMR granule search for the final collection, run 2026-09-13 with sort_key=start_date and again with sort_key=-start_date: the first granule record is oscar_currents_final_19930101 (1993-01-01) and the last is oscar_currents_final_20260116 (2026-01-16)"
  - id: cmr-granules-interim
    resource: https://cmr.earthdata.nasa.gov/search/granules.json?collection_concept_id=C2102959417-POCLOUD&page_size=1&sort_key=start_date
    title: "CMR granule search for the interim collection, run 2026-09-13 with sort_key=start_date and with sort_key=-start_date: first granule oscar_currents_interim_20200101, last oscar_currents_interim_20260831"
  - id: cmr-granules-nrt
    resource: https://cmr.earthdata.nasa.gov/search/granules.json?collection_concept_id=C2102958977-POCLOUD&page_size=1&sort_key=start_date
    title: "CMR granule search for the near-real-time collection, run 2026-09-13 with sort_key=start_date and with sort_key=-start_date: first granule oscar_currents_nrt_20210101, last oscar_currents_nrt_20260903"
  - id: granule
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-protected/OSCAR_L4_OC_FINAL_V2.0/oscar_currents_final_20200101.nc
    title: "One final granule (2020-01-01, the day the handbook's sample attributes come from), opened with an Earthdata token on 2026-09-13 to read its dimensions, variables and attributes, then deleted; the file is behind Earthdata login"
  - id: guide
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/oscar/open/L4/oscar_v2.0/docs/oscarv2guide.pdf
    title: "OSCAR v2.0 User's Handbook, Kathleen Dohan, Earth and Space Research, October 2021 (13 pages, read in full 2026-09-13): the model outline, the source datasets per quality level, the file format, the latency, the known problems and the differences from the third-degree product"
  - id: bonjean-2002
    resource: https://doi.org/10.1175/1520-0485(2002)032<2938:DMAAOT>2.0.CO;2
    title: "Bonjean and Lagerloef, 2002, Diagnostic model and analysis of the surface currents in the tropical Pacific Ocean, Journal of Physical Oceanography 32, 2938 to 2954: the OSCAR model formulation the handbook cites as reference 1 (registry record verified 2026-09-13; the record carries no abstract and the journal page was not read)"
  - id: lagerloef-1999
    resource: https://doi.org/10.1029/1999JC900197
    title: "Lagerloef, Mitchum, Lukas and Niiler, 1999, Tropical Pacific near-surface currents estimated from altimeter, wind, and drifter data, Journal of Geophysical Research: Oceans 104: the original geostrophic plus Ekman model calibrated by 15 m drogued drifters, with the beta-plane treatment at the equator (registry record verified and abstract read there 2026-09-13; the journal page was not read)"
  - id: dohan-2017
    resource: https://doi.org/10.1002/2017JC012961
    title: "Dohan, 2017, Ocean surface currents from satellite data, Journal of Geophysical Research: Oceans: the OSCAR project's statement of what it computes and why (simplified physics, satellite observations) (registry record verified and abstract read there 2026-09-13; the journal page was not read)"
  - id: mulet-2021
    resource: https://doi.org/10.5194/os-17-789-2021
    title: "Mulet and others, 2021, The new CNES-CLS18 global mean dynamic topography, Ocean Science 17, 789 to 808: the mean dynamic topography inside the absolute dynamic topography the final and interim products differentiate (registry record verified and abstract read there 2026-09-13; the article was not read)"
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
`oscar_currents_<level>_YYYYMMDD.nc`, with a maximum size of 32 MB,
holding total and geostrophic velocity on a 0.25-degree grid from
89.75S to 89.75N and 0 to 359.75E, one daily-average time per file,
and the value in each cell an average over the top 30 m.[^guide] The
final granule for 2020-01-01, opened on 2026-09-13, has dimensions
latitude 719, longitude 1440 and time 1, and four double-precision
fields `u`, `v` (zonal and meridional total surface current) and
`ug`, `vg` (the geostrophic component alone), each in metres per
second with a fill value of -999, a valid range of -3 to 3, a `depth`
attribute of 15 m and the comment that velocities are an average over
the top 30 m of the mixed layer; time is days since 1990-01-01 on a
Julian calendar, centred on the day.[^granule] The handbook's sample
attributes from the same day agree with the file on all of these and
state that velocities above 3 m/s are removed without further
processing.[^guide] The file's `source` attributes name the inputs
for the final product: the Copernicus SSALTO/DUACS delayed-time
absolute dynamic topography, in the granule under the product name
SEALEVEL_GLO_PHY_L4_MY_008_047 with DOI 10.48670/moi-00148 where the
handbook's 2021 sample names the earlier REP_OBSERVATIONS product
name, ERA5 10 m winds, and the Canadian Meteorological Centre SST
analysis (0.2-degree version 2 for 1993 through 2015, 0.1-degree
version 3 from 2016 per the handbook); the granule's `date_created`
is 2022-01-14 where the handbook's sample from the same day reads
2021-09-30, so the file was regenerated after the
handbook.[^granule][^guide] The absolute dynamic topography is the
altimeter anomaly on the CNES-CLS18 mean dynamic topography, so the
geostrophic component inherits that mean field and its own
error.[^guide][^mulet-2021]

**The three collections.** Final uses delayed-time altimetry and ERA5
winds and has a latency the handbook puts at about 1.5 years (the
collection abstract says about one year); interim uses near-real-time
altimetry and ERA5 winds, about one month behind; nrt uses
near-real-time altimetry and NCEP/NCAR Reanalysis 1 winds, about two
days behind.[^guide][^cmr-final] A granule search on 2026-09-13
(first and last granule by start date) found final granules from
1993-01-01 through 2026-01-16, interim granules from 2020-01-01
through 2026-08-31 and nrt granules from 2021-01-01 through
2026-09-03; the collection records state the extents as 1993-01-01
to 2026-01-17 for final and open-ended from 2020-01-01 and
2021-01-01 for the other two. The collections therefore overlap over
years rather than abutting, and the same date can exist in all three
with different
inputs.[^cmr-granules-final][^cmr-granules-interim][^cmr-granules-nrt][^cmr-final][^cmr-interim][^cmr-nrt] The whole record was
computed once in early 2021 and has been produced in real time since,
with the source-data access dates coinciding with the files' creation
dates.[^guide] The gotcha on versions and latency carries what changes
between the levels and what a series across them measures.

## Uncertainty

- **No uncertainty field ships with the product.** The files carry the
  four velocity components and nothing else; the handbook's
  calibration section points to a validation page on the producer's
  website and, for the earlier third-degree product, to Dohan and
  Maximenko 2010; the bundle holds no validation number for version
  2 (the Verification paragraph says why).[^guide]
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
- The handbook is dated October 2021 and does not say whether the
  collections were reprocessed since the 2021 computation; the one
  granule opened was created in January 2022 and names a newer
  altimetry product name than the handbook's sample.[^guide][^granule]
  The CMR records' `meta.revision-date` fields read 2026-08-19 (final)
  and 2026-07-27 (interim and nrt), while their `MetadataDates`
  UPDATE entries read 2024-03-11, 2023-07-31 and 2022-02-05; these
  are metadata dates, not data dates.[^cmr-final][^cmr-interim][^cmr-nrt]

**Verification.** The three CMR collection records, the granule
searches and the three collection pages were read on 2026-09-13,
the handbook was read in full the same day, and one final granule
was opened and deleted the same day; every file-level fact above is
from that granule or the handbook's sample attributes, and every
range from the granule searches.[^cmr-final][^cmr-granules-final][^guide][^granule]
The four papers' registry records were verified on 2026-09-13 (title,
authors, journal, year) and the abstracts of the 1999, 2017 and 2021
papers read there; no journal page was read. The producer's
validation page, which the handbook names for version 2 validation,
was unreachable from the drafting session (the host is blocked by the
network policy), so no validation number is quoted.[^guide]

[^podaac-final]: PO.DAAC collection page, OSCAR_L4_OC_FINAL_V2.0
[^podaac-interim]: PO.DAAC collection page, OSCAR_L4_OC_INTERIM_V2.0
[^podaac-nrt]: PO.DAAC collection page, OSCAR_L4_OC_NRT_V2.0
[^cmr-final]: CMR collection record, C2098858642-POCLOUD
[^cmr-interim]: CMR collection record, C2102959417-POCLOUD
[^cmr-nrt]: CMR collection record, C2102958977-POCLOUD
[^cmr-granules-final]: CMR granule search, final collection, first and last granule, 2026-09-13
[^cmr-granules-interim]: CMR granule search, interim collection, first and last granule, 2026-09-13
[^cmr-granules-nrt]: CMR granule search, near-real-time collection, first and last granule, 2026-09-13
[^granule]: One OSCAR final granule, 2020-01-01, opened and deleted on 2026-09-13
[^guide]: OSCAR v2.0 User's Handbook, Dohan, October 2021
[^bonjean-2002]: Bonjean and Lagerloef, 2002, Journal of Physical Oceanography, doi:10.1175/1520-0485(2002)032<2938:DMAAOT>2.0.CO;2
[^lagerloef-1999]: Lagerloef and others, 1999, Journal of Geophysical Research: Oceans, doi:10.1029/1999JC900197
[^dohan-2017]: Dohan, 2017, Journal of Geophysical Research: Oceans, doi:10.1002/2017JC012961
[^mulet-2021]: Mulet and others, 2021, Ocean Science, doi:10.5194/os-17-789-2021
