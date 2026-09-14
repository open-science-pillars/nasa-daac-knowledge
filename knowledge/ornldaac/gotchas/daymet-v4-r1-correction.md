---
type: dataset-gotcha
spheres: [atmosphere, geosphere]
title: "Version 4 R1 re-derived every 2020 and 2021 file with corrected Canadian station inputs and changed nothing else: a Version 4 file for those years is a different estimate under a different DOI"
description: "Daymet Version 4 R1, published 2022-11-01 under DOI 10.3334/ORNLDAAC/2129, updated all 2020 and 2021 files for every variable after the station inputs used for those years were found to lack January readings for a significant portion of Canadian weather stations; NCEI corrected the ingest feed and the two years were rerun with new inputs. Files outside 2020 and 2021 are unchanged from Version 4 (DOI 10.3334/ORNLDAAC/1840), which is superseded and marked access restricted. A series that mixes Version 4 and R1 files for 2020 and 2021, or cites the Version 4 DOI for data downloaded after the R1 release, carries a version difference concentrated in high-latitude January as if it were weather."
tags: [daymet, version, v4, v4-r1, release, correction, doi, ghcn, canada, ornldaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:40:00Z }
severity: medium
# medium: the change is stated on the landing pages and in the CMR
# abstracts, it is confined to two years, and the version is written
# in each file's global attributes, so a mixed series is detectable
# from the files; no eval case is required.
dataset: ../datasets/daymet-v4.md
status: draft
stale_after: 2027-03-14
sources:
  - id: cmr-daily-v4r1
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2532426483-ORNL_CLOUD.umm_json
    title: "CMR collection record for Daymet Daily Version 4 R1 (version 4.1, DOI 10.3334/ORNLDAAC/2129): the abstract's R1 paragraph on the 2020 and 2021 rerun, the missing Canadian January readings, the corrected NCEI feed and the unchanged other years; the record's create date 2022-11-01"
  - id: cmr-xval-v4r1
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2531991823-ORNL_CLOUD.umm_json
    title: "CMR collection record for the Version 4 R1 station-level inputs and cross-validation dataset: the same R1 paragraph, so the cross-validation files for 2020 and 2021 changed with the grids"
  - id: ornl-v4-landing
    resource: https://daac.ornl.gov/cgi-bin/dsviewer.pl?ds_id=1840
    title: "ORNL DAAC landing page for Daymet Version 4 (DOI 10.3334/ORNLDAAC/1840): the notice that a newer version exists as of 2022-11-01 with the R1 citation, the version history table (4 published 2020-12-15, 4.1 published 2022-11-01) and the restricted-access notice on the Version 4 files"
  - id: ornl-v4-guide
    resource: https://daac.ornl.gov/DAYMET/guides/Daymet_Daily_V4.html
    title: "ORNL DAAC user guide, Daymet Daily V4 (documentation revision 2024-06-17): the Version_software and Version_data global attributes, the station input download dates per year, the note that all Daymet data are provisional, and the DAAC's versioning practice"
  - id: daymet-citations
    resource: https://daymet.ornl.gov/citations
    title: "Daymet project site, citations page: the Version 4 R1 DOIs for the daily, monthly, annual and cross-validation datasets"
  - id: dataset
    resource: ../datasets/daymet-v4.md
    title: "This bundle's Daymet dataset concept, which lists this trap among the known issues"
---

# The Version 4 R1 correction

**Mechanism.** In Version 4 R1, all 2020 and 2021 files were updated
to improve predictions, especially in high-latitude areas: the input
files used to derive the 2020 and 2021 data had, for a significant
portion of Canadian weather stations, missing daily readings for the
month of January; NCEI corrected the Environment Canada ingest feed
that caused the gap, and the 2020 and 2021 files were re-derived with
new GHCNd inputs; files outside 2020 and 2021 are unchanged from the
previous Version 4 release.[^cmr-daily-v4r1] The same statement
stands on the Version 4 R1 station-level cross-validation collection,
so the cross-validation record for those two years changed with the
grids.[^cmr-xval-v4r1] R1 is a new DOI, 10.3334/ORNLDAAC/2129,
published 2022-11-01 as ORNL DAAC version 4.1; the Version 4 landing
page (DOI 10.3334/ORNLDAAC/1840, published 2020-12-15) carries the
superseding notice and marks its files as access
restricted.[^ornl-v4-landing] The guide records that Version 4 built
2020 from a GHCN Daily download of 2021-02-14 and 2021 from one of
2022-02-16, and that each file's global attributes Version_software
and Version_data record what produced it; all Daymet data are
provisional and subject to revision.[^ornl-v4-guide] The four current
collections, daily, monthly, annual and cross-validation, are all R1
and carry their own DOIs.[^daymet-citations]

**Wrong-result mode.** A daily series assembled from Version 4 files
for 1980 through 2021 (downloaded before November 2022 and kept) and
R1 files for later years is one series with a break at 2020 that is a
version difference, not weather; the difference is concentrated in
Canadian high latitudes and in January, so a trend, an anomaly or an
extreme statistic for those regions reads the correction as a signal
and a comparison of 2020 or 2021 against a climatology built from the
same source is off by the correction. A study that cites DOI
10.3334/ORNLDAAC/1840 for files obtained after the R1 release names
the wrong data, and a reproduction that fetches the cited DOI is
refused, since access to Version 4 is restricted. Because every year
outside 2020 and 2021 is identical between the two releases, a
version check on any other year shows nothing, and the files for the
two changed years have the same names in both releases apart from the
collection they came from.

**Correct approach.** The current product is Version 4 R1 under DOI
10.3334/ORNLDAAC/2129, and the version of every file in a series is
the value of its Version_data and Version_software global attributes,
read from the files rather than assumed from the download
date.[^cmr-daily-v4r1][^ornl-v4-guide] A series that includes 2020 or
2021 is R1 throughout; a result derived from Version 4 files for
those years is a result on superseded data and says so. The
cross-validation files that accompany an uncertainty statement are
the R1 files for 2020 and 2021.[^cmr-xval-v4r1]

**Verification.** The CMR abstracts of the daily and cross-validation
R1 collections carry the correction statement and the scope (2020 and
2021 only).[^cmr-daily-v4r1][^cmr-xval-v4r1] The Version 4 landing
page carries the superseding notice, the version history and the
restricted-access notice.[^ornl-v4-landing] The guide carries the
global attribute names and the input download dates.[^ornl-v4-guide]
The Version 4 R1 user guide and release notes themselves were not
read for this concept: on the reading date the DAAC's links to them
redirect to hosts outside the sources consulted, so the statement of
what changed rests on the CMR abstracts and the Version 4 landing
page. The dataset concept lists this trap among the product's known
issues.[^dataset]

[^cmr-daily-v4r1]: CMR collection C2532426483-ORNL_CLOUD, read 2026-09-14
[^cmr-xval-v4r1]: CMR collection C2531991823-ORNL_CLOUD, read 2026-09-14
[^ornl-v4-landing]: ORNL DAAC landing page for Daymet Daily V4 (ds_id 1840), read 2026-09-14
[^ornl-v4-guide]: ORNL DAAC user guide, Daymet Daily V4, revision 2024-06-17, read 2026-09-14
[^daymet-citations]: Daymet project site, citations page, read 2026-09-14
[^dataset]: This bundle's Daymet dataset concept
