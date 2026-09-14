---
type: dataset-gotcha
spheres: [biosphere, hydrosphere]
title: "A reprocessing rewrites the whole chlorophyll record and the catalogue keeps one version: a series comes from one reprocessing, files fetched before and after a reprocessing are two products, and the near-real-time tail is a third"
description: "OB.DAAC processes every sensor's record with one algorithm and calibration configuration and replaces the entire record when either changes: MODIS-Aqua is in R2022 (files carry R2022.0.3), which retuned both chlorophyll components and moved the CI-to-OCx transition from 0.15 to 0.2 up to 0.25 to 0.35, and PACE OCI has gone through versions 1, 2, 3, 3.1 and 3.2 between April 2024 and April 2026, the last fixing a reflectance correction the producer calls a significant improvement in accuracy and cross-track stability. CMR catalogues only the current version of each collection, the mapped files name their version only in a global attribute, and the refined MODIS-Aqua daily record trailed the near-real-time record by about three and a half months on 2026-09-14, the near-real-time files being processed with ancillary data and a calibration the producer calls less than optimal. A series assembled from files downloaded on different dates, or extended to the present with near-real-time files, therefore steps between processing configurations, and the step is not an ocean change."
tags: [chlorophyll, chlor_a, reprocessing, r2022, version, near-real-time, nrt, refined, calibration, modis, aqua, pace, oci, obdaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:30:00Z }
severity: medium
dataset: ../datasets/modis-aqua-l3-chlorophyll.md
status: draft
stale_after: 2027-03-14
sources:
  - id: atbd
    resource: https://oceancolor.gsfc.nasa.gov/files/atbd/atbd-obdaac-chlorophyll-a.pdf
    title: "Chlorophyll a, Algorithm Theoretical Basis Document version 1.1, 6 November 2023, read in full 2026-09-14: the statement that it describes the algorithm as implemented in the most recent reprocessing, R2022, of NASA's multi-mission ocean color processing, the R2022 adoption of updated parameters for both components, the hybrid algorithm as default since R2014, and the previous-versions paragraph with the 0.15 to 0.2 transition and the 2012 parameterization used before"
  - id: pace-v3-notes
    resource: https://oceancolor.gsfc.nasa.gov/files/reprocessing/PACE_OCI_V3_Release_Notes.pdf
    title: "PACE OCI V3 Processing Notes, April 2026, read in full 2026-09-14: the version history (version 1 on 11 April 2024, version 2 the first full-mission reprocessing, version 3, version 3.1 in August 2025, version 3.2 in April 2026), the changes to calibration, vicarious calibration, polarization, BRDF and masking at each step, and the consolidation of the suites into single Level 3 files in 3.2"
  - id: pace-v1-notes
    resource: https://oceancolor.gsfc.nasa.gov/files/reprocessing/PACE_Science_Data_V1_Release_Notes.pdf
    title: "PACE Science Data Initial Release Notes, read 2026-09-14: the version 1 caution that the data are preliminary and that users should expect frequent updates and reprocessing"
  - id: ancillary
    resource: https://oceancolor.gsfc.nasa.gov/files/obdaac-ancillary-data-sources.pdf
    title: "Ancillary Data at OB.DAAC (8 pages, read 2026-09-14): the two-step processing, near-real-time with the best ancillary data available at the time and a later refined processing once the optimal ancillary data exist"
  - id: cmr-nrt
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C4184125829-OB_CLOUD.umm_json
    title: "CMR collection record for PACE_OCI_L3M_BGC_NRT version 3.2 (read 2026-09-14): the abstract stating that near-real-time products use the best available combination of ancillary data and that the inputs and the calibration used are less than optimal, and the missing DOI explained by the collection being near-real-time"
  - id: cmr-collections
    resource: https://cmr.earthdata.nasa.gov/search/collections.json?short_name=MODISA_L3m_C*&options[short_name][pattern]=true&page_size=100
    title: "CMR collection searches run 2026-09-14: MODISA_L3m_CHL exists at version 2022.0 only, PACE_OCI_L3M_BGC at version 3.2 only, each with one near-real-time twin, and no earlier version of either is catalogued"
  - id: cmr-granules
    resource: https://cmr.earthdata.nasa.gov/search/granules.json?collection_concept_id=C3380709133-OB_CLOUD&page_size=3&sort_key=-start_date
    title: "CMR granule searches run 2026-09-14: the last refined MODIS-Aqua daily granule was 2026-05-30 and the last near-real-time daily granule 2026-09-12; the last refined PACE OCI daily granule was 2026-07-31 and the last near-real-time 2026-09-12"
  - id: modis-file
    resource: https://oceandata.sci.gsfc.nasa.gov/opendap/MODISA/L3SMI/2024/0601/AQUA_MODIS.20240601_20240630.L3m.MO.CHL.chlor_a.4km.nc.das
    title: "The attribute listings (OPeNDAP .das, metadata only) read 2026-09-14: the June 2024 MODIS-Aqua monthly file with processing_version R2022.0.3 and date_created 2026-07-10, the daily file of 2026-05-30 created 2026-07-08, the cumulative climatology created 2026-07-13, and the June 2024 PACE OCI monthly BGC file with processing_version 3.2 and date_created 2026-05-16; the version appears in the global attributes and, for PACE, in the file name"
  - id: hu-2019
    resource: https://doi.org/10.1029/2019JC014941
    title: "Hu, Feng, Lee, Franz, Bailey, Werdell and Proctor, 2019, Improving satellite global chlorophyll a data products through algorithm refinement and data recovery, Journal of Geophysical Research: Oceans 124, 1524 to 1543 (registry record verified on Crossref and abstract read there 2026-09-14; the article was not read): OCI2 gives lower chlorophyll than OCI1 below 0.05 mg per cubic metre and a smoother transition between 0.25 and 0.40, and a straylight mask relaxed from 7 by 5 to 3 by 3 pixels would increase data quantity by 39 percent on average"
  - id: dataset
    resource: ../datasets/modis-aqua-l3-chlorophyll.md
    title: "This bundle's MODIS-Aqua Level 3 chlorophyll-a dataset concept and, beside it, the PACE OCI dataset concept with its version history"
---

# A reprocessing rewrites the whole chlorophyll record and the catalogue keeps one version

**Mechanism.** The Ocean Biology Processing Group processes each
sensor's record with one configuration of calibration, atmospheric
correction and algorithm coefficients, and a reprocessing applies a
new configuration to the entire record. For MODIS-Aqua the current
configuration is R2022: the ATBD describes the chlorophyll algorithm
as implemented in that reprocessing, which adopted retuned parameters
for both the color index and the band-ratio components and a
transition of 0.25 to 0.35 mg per cubic metre where the
implementation used from R2014 until R2022 had a transition of 0.15
to 0.2 with the 2012 parameterization; the retuning gives lower values than before below
0.05 mg per cubic metre and a smoother transition, and the same
revision found the straylight mask could be relaxed for 39 percent
more data on average, so a reprocessing can change values and coverage
together (the ATBD does not state which mask R2022
uses).[^atbd][^hu-2019] For PACE OCI the record has been through
five versions (1, 2, 3, 3.1 and 3.2, four reprocessings) in two
years: version 1 on 11 April 2024 with the caution
that users should expect frequent updates and reprocessing, version 2
as the first full-mission reprocessing with revised calibration,
version 3 with a solar-diffuser-only calibration, the first vicarious
calibration gains, a polarization correction and a hyperspectral BRDF
table, version 3.1 in August 2025 with a ghosting correction and
corrected red gains, and version 3.2 in April 2026, which fixed an
error in the bidirectional reflectance correction's handling of the
relative azimuth across the scan, with what the notes call a
significant improvement in the accuracy and cross-track stability of
the reflectances from which chlorophyll is
derived.[^pace-v1-notes][^pace-v3-notes] The catalogue keeps one
version: CMR searches on 2026-09-14 found MODISA_L3m_CHL at 2022.0
only and PACE_OCI_L3M_BGC at 3.2 only, and the mapped files carry the
version in a global attribute (processing_version R2022.0.3 or 3.2)
and, for PACE, in the file name; the MODIS-Aqua file name carries no
version token.[^cmr-collections][^modis-file] The
files of a reprocessed record are new files: the June 2024 MODIS-Aqua
monthly file was created on 2026-07-10 and the June 2024 PACE monthly
file on 2026-05-16, months or years after the month they
describe.[^modis-file] Ahead of the refined record runs a
near-real-time record processed with the best ancillary data
available at the time, which the producer describes as inputs and a
calibration that are less than optimal, and which the refined
processing later replaces; on 2026-09-14 the refined MODIS-Aqua daily
record ended on 2026-05-30 and the refined PACE record on 2026-07-31,
while both near-real-time records ran to
2026-09-12.[^ancillary][^cmr-nrt][^cmr-granules]

**Wrong-result mode.** A series assembled from files fetched at
different times, some before and some after a reprocessing, steps
between configurations at the fetch boundary, and the step reads as a
change in the ocean: for MODIS-Aqua across the previous reprocessing to R2022 the low
end of the range and the transition zone moved; for
PACE across 3.1 to 3.2 the reflectance correction and the vicarious
gains changed. A series extended to the present with near-real-time
files splices a differently processed tail onto the refined record,
and the tail is later replaced, so the same query returns different
values months apart. A comparison between two sensors or two studies
that used different reprocessings compares configurations as well as
oceans, and an anomaly against a climatology built from the previous
reprocessing is offset by the reprocessing's change. Because the
catalogue keeps only the current version and the MODIS-Aqua file name
does not carry it, a file on disk cannot be told from the current
product except by its `processing_version` and `date_created`
attributes.[^modis-file][^cmr-collections]

**Correct approach.** A chlorophyll series is built from one
reprocessing, identified by the `processing_version` attribute read
from every file it uses (R2022.0.3 for MODIS-Aqua, 3.2 for PACE OCI
on 2026-09-14) and stated with the result, and its end date is the end
of the refined record, with any near-real-time extension marked as
such and understood to be replaced later.[^modis-file][^cmr-granules]
An analysis that must span a reprocessing re-fetches the whole record
under the new version rather than appending; a comparison across
sensors names both versions; an anomaly uses a climatology from the
same version as the series.[^cmr-collections] What a chlorophyll
series from the OB.DAAC therefore is: the current reprocessing's
reading of the record up to the refined end, the same on every day it
is fetched only until the next reprocessing.[^dataset]

**Verification.** The ATBD's version and previous-versions
statements and the PACE processing notes' version history were read
in full on 2026-09-14 and are the producer's own account of what each
reprocessing changed; the ancillary-data document and the
near-real-time collection record state the two-step processing and
its caveat; the CMR collection and granule searches run the same day
show the single catalogued version and the refined and near-real-time
end dates; the file listings show the version and creation
attributes; the Hu 2019 abstract, read on the registry record, states
the value and coverage changes of the retuning.[^atbd][^pace-v3-notes][^ancillary][^cmr-nrt][^cmr-collections][^cmr-granules][^modis-file][^hu-2019]
The MODIS-Aqua R2022 reprocessing notes themselves are on OB.DAAC web
pages that redirected to the Earthdata landing page and were not
read, so the magnitude of the change in the MODIS-Aqua record at
R2022 is not quoted here.

[^atbd]: Chlorophyll a ATBD version 1.1, OB.DAAC, 6 November 2023
[^pace-v3-notes]: PACE OCI V3 Processing Notes, April 2026
[^pace-v1-notes]: PACE Science Data Initial Release Notes
[^ancillary]: Ancillary Data at OB.DAAC
[^cmr-nrt]: CMR collection record, C4184125829-OB_CLOUD
[^cmr-collections]: CMR collection searches, 2026-09-14
[^cmr-granules]: CMR granule searches, last refined and near-real-time granules, 2026-09-14
[^modis-file]: Attribute listings of MODIS-Aqua and PACE OCI L3m files, read through OPeNDAP on 2026-09-14
[^hu-2019]: Hu and others, 2019, Journal of Geophysical Research: Oceans, doi:10.1029/2019JC014941
[^dataset]: This bundle's MODIS-Aqua Level 3 chlorophyll-a dataset concept
