---
type: dataset-gotcha
spheres: [hydrosphere]
title: "OSCAR final, interim and nrt are three products with different inputs, and version 2 is not the third-degree OSCAR: a series that steps between them carries the input change as ocean change"
description: "The three OSCAR version 2 collections share a model and a file layout but not their inputs: final uses delayed-time altimetry and ERA5 winds, interim near-real-time altimetry and ERA5, nrt near-real-time altimetry and NCEP/NCAR reanalysis winds, at latencies of about a year and a half, a month and two days. They overlap over years rather than abutting, so a series extended to the present by switching collections at the end of final puts the altimetry and wind product changes into the record at the seam, and nothing in the files marks it. Version 2 also replaced the third-degree five-day product with a different grid, cadence, equatorial model and smoothing, so third-degree validation and results do not transfer."
tags: [oscar, surface-currents, versions, latency, near-real-time, interim, final, reprocessing, altimetry, era5, ncep]
generated: { by: knowledge-seeder/claude, at: 2026-09-13T21:00:00Z }
severity: medium
# medium: the collections are documented and separately catalogued, and
# the trap bites through mixing them or through comparison against the
# retired product rather than through a silently wrong single-collection
# statistic; no eval case is required at this severity.
dataset: ../datasets/oscar-v2.md
status: draft
stale_after: 2027-03-13
sources:
  - id: guide
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/oscar/open/L4/oscar_v2.0/docs/oscarv2guide.pdf
    title: "OSCAR v2.0 User's Handbook, Dohan, October 2021 (read in full 2026-09-13): the source datasets per quality level, the latency, the 2021 initial computation, the SST source change in 2016, and the differences from the third-degree and one-degree products"
  - id: cmr-final
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2098858642-POCLOUD.umm_json
    title: "CMR collection record, OSCAR_L4_OC_FINAL_V2.0 (C2098858642-POCLOUD): the abstract's latency statement and the granule range 1993-01-01 through 2026-01-16 (read 2026-09-13)"
  - id: cmr-interim
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2102959417-POCLOUD.umm_json
    title: "CMR collection record, OSCAR_L4_OC_INTERIM_V2.0 (C2102959417-POCLOUD): granules 2020-01-01 through 2026-08-31 (read 2026-09-13)"
  - id: cmr-nrt
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2102958977-POCLOUD.umm_json
    title: "CMR collection record, OSCAR_L4_OC_NRT_V2.0 (C2102958977-POCLOUD): granules 2021-01-01 through 2026-09-03 (read 2026-09-13)"
  - id: podaac-final
    resource: https://podaac.jpl.nasa.gov/dataset/OSCAR_L4_OC_FINAL_V2.0
    title: "PO.DAAC collection page, OSCAR_L4_OC_FINAL_V2.0: the three DOIs' collection family, the start and stop dates and the citation (read 2026-09-13)"
  - id: dohan-2010
    resource: https://doi.org/10.5670/oceanog.2010.08
    title: "Dohan and Maximenko, 2010, Monitoring ocean currents with satellite sensors, Oceanography 23: the validation the handbook cites for the third-degree product, which is not the version 2 validation (registry record verified; the article was not read)"
  - id: dataset
    resource: ../datasets/oscar-v2.md
    title: "This bundle's OSCAR dataset concept: the three collections, their concept ids and DOIs, and the granule ranges on the verification date"
---

# OSCAR final, interim and nrt are three products

**Mechanism.** Version 2 of OSCAR is distributed as three collections
with their own short names and DOIs, described by the producer as
three quality levels determined by the best available source
datasets.[^guide][^podaac-final] The model, grid and file layout are
the same; the inputs are not. Final uses the Copernicus SSALTO/DUACS
delayed-time (reprocessed) absolute dynamic topography, ERA5 10 m
winds, and Canadian Meteorological Centre SST at 0.2 degrees for 1993
through 2015 and 0.1 degrees from 2016. Interim uses the SSALTO/DUACS
near-real-time absolute dynamic topography, ERA5 winds and the
0.1-degree SST. Nrt uses the near-real-time dynamic topography, the
0.1-degree SST, and NCEP/NCAR Reanalysis 1 winds in place of
ERA5.[^guide] The handbook gives latencies of about 1.5 years, about
one month and two days; the collection abstract gives about one year
for final.[^guide][^cmr-final] The record was computed in full once in
early 2021 and has been produced in real time since, the source data
being read at about the time each file is made.[^guide] The
collections overlap rather than abut: on 2026-09-13 CMR held final
granules through 2026-01-16, interim granules from 2020-01-01 through
2026-08-31, and nrt granules from 2021-01-01 through 2026-09-03, so
for any day since 2021 up to three files exist with different
inputs.[^cmr-final][^cmr-interim][^cmr-nrt][^dataset] Version 2 itself
replaced the third-degree five-day OSCAR: a daily file on a finer grid
with the geostrophic components added, the maximum-mask velocity and
the filtered velocity dropped, a changed equatorial model (the
equatorial solution within five degrees with a blended turbulence
parameterization), a changed gradient method suited to the finer
inputs, and velocities above 3 m/s removed; the validation the
handbook cites by paper is for the third-degree product, and version 2
validation is referred to the producer's website.[^guide][^dohan-2010]

**Wrong-result mode.** A series that takes final where it exists and
continues with interim (and then nrt) to reach the present changes its
altimetry product from delayed-time to near-real-time at the seam, and
its wind product from ERA5 to NCEP/NCAR at the second seam; the
near-real-time dynamic topography lacks the later altimeter passes the
reprocessed field uses, so the geostrophic component differs at the
seam and a trend, an anomaly or a variance computed across it carries
the input change as if the ocean had changed. The same date read from
two collections gives two values, and a workflow that opens "the OSCAR
file for that day" without the collection name is not reproducible. A
comparison of a version 2 result with a third-degree result from the
literature, or a claim that version 2 has the third-degree product's
validated accuracy, compares products that differ in equatorial model,
gradient method, cadence and smoothing.[^guide] Inside final, the 2016
change of SST source is an inhomogeneity in the thermal-wind term that
a long-record statistic straddles without notice.[^guide] Nothing in
the files marks any of these seams; the `source` attribute names the
inputs, and only the file name and the collection distinguish the
levels.[^guide]

**Correct approach.** One collection per series, named with its short
name and DOI: final for any record-length statistic, interim to extend
it by months with the seam date stated and the input change named,
nrt for the latest days only.[^guide][^dataset] A statement that spans
the seam says which dates come from which collection and that the
altimetry (and, for nrt, the wind) input changed there, and a trend or
anomaly is fitted within one collection or reported with the seam as a
known step.[^guide] The version is version 2, cited by the
collection's DOI, and validation quoted for it is version 2
validation, not the third-degree paper.[^dohan-2010][^guide] A final
series that crosses 2016 carries the SST source change as a
caveat.[^guide]

**Verification.** The handbook's source-datasets, latency and
differences sections were read in full on 2026-09-13 and are the
producer's statement of the inputs per level and the version 2
changes.[^guide] The three CMR collection records and their first and
last granules were read the same day; the overlap above is the
catalogue state on that date, and the granule ranges move
daily.[^cmr-final][^cmr-interim][^cmr-nrt] The collection page repeats
the family and the dates.[^podaac-final] The 2010 paper's record was
verified against the Crossref registry (title, authors, journal,
year); it is cited here only as the third-degree validation the
handbook names.[^dohan-2010]

[^guide]: OSCAR v2.0 User's Handbook, Dohan, October 2021
[^cmr-final]: CMR collection record, C2098858642-POCLOUD, and its granule range
[^cmr-interim]: CMR collection record, C2102959417-POCLOUD, and its granule range
[^cmr-nrt]: CMR collection record, C2102958977-POCLOUD, and its granule range
[^podaac-final]: PO.DAAC collection page, OSCAR_L4_OC_FINAL_V2.0
[^dohan-2010]: Dohan and Maximenko, 2010, Oceanography, doi:10.5670/oceanog.2010.08
[^dataset]: This bundle's OSCAR dataset concept
