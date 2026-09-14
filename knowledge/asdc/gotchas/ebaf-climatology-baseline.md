---
type: dataset-gotcha
spheres: [atmosphere]
title: "The EBAF climatology base period, the edition and the release date fix the anomaly baseline: the product's climatology is July 2005 through June 2015, and files of different editions or releases differ in the fields themselves"
description: "EBAF ships a climatology whose base period is July 2005 through June 2015 in Editions 4.0 through 4.2.1, the same decade the net flux is anchored over, and the single-satellite periods are adjusted to the Terra plus Aqua climatology of the overlap years. An anomaly against a self-built climatology over another window, or a climatology file from one edition or release applied to monthly means from another (Edition 4.2 surface fluxes differ from 4.1 throughout, Edition 4.2.1 differs from 4.2 after March 2022, and the January 2024 revision of 4.2 replaced fields through June 2023), mixes a baseline change into the anomaly."
tags: [ceres, ebaf, climatology, anomaly, baseline, base-period, edition, release-date]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:30:00Z }
severity: low
dataset: ../datasets/ceres-ebaf-ed4-2.md
status: draft
stale_after: 2027-03-14
sources:
  - id: dqs
    resource: https://ceres.larc.nasa.gov/documents/DQ_summaries/Versioned/CERES_EBAF_Ed4.2_DQS_V7.pdf
    title: "CERES_EBAF_Ed4.2 and Ed4.2.1 Data Quality Summary, version 7, 2026-07-01, the pinned copy (byte-identical to the file the unversioned link served on 2026-09-14; the documentation page lists a version 8 posted 2026-09-09, which was served at neither URL that day and was not read), read 2026-09-14: the climatological base period July 2005 through June 2015, the anchoring over the same decade, the periods each edition change affects, the climatology adjustments of the single-satellite periods, the version history, and the request to check the version and release date in the netCDF file"
  - id: dqs-ed4-1
    resource: https://ceres.larc.nasa.gov/documents/DQ_summaries/Versioned/CERES_EBAF_Ed4.1_DQS_V3.pdf
    title: "CERES_EBAF_Ed4.1 Data Quality Summary, version 3, 2021-12-09, read 2026-09-14 for one fact: the climatological mean values used to calculate deseasonalized monthly anomalies are for a base period of July 2005 through June 2015"
  - id: dqs-ed4-0
    resource: https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_EBAF_Ed4.0_DQS.pdf
    title: "CERES_EBAF_Ed4.0 Data Quality Summary, 2018-01-12, read 2026-09-14 for one fact: the climatological mean values are calculated relative to a base period of July 2005 through June 2015"
  - id: dqs-ed2-8
    resource: https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_EBAF_Ed2.8_DQS.pdf
    title: "CERES_EBAF_Ed2.8 Data Quality Summary, 2014-03-19, read 2026-09-14 for one fact: the anchoring period of that edition was July 2005 through June 2010"
  - id: ceres-data-page
    resource: https://ceres.larc.nasa.gov/data/#energy-balanced-and-filled-ebaf
    title: "CERES data products page, read 2026-09-14: the monthly means and climatology entries of the EBAF products"
  - id: dataset
    resource: ../datasets/ceres-ebaf-ed4-2.md
    title: "This bundle's EBAF dataset concept, which lists this trap among the known issues and carries the edition history"
---

# EBAF climatology baseline

**Mechanism.** The EBAF products come as monthly means and as a
climatology, and the climatological mean values, the ones the
project uses for deseasonalized monthly anomalies, are determined for
a base period of July 2005 through June 2015 in Edition 4.0, Edition
4.1 and Editions 4.2 and 4.2.1 alike; that decade is also the one the
global mean net flux is anchored over, chosen to avoid the
single-satellite periods, where the Edition 2.8 anchor had used July
2005 through June 2010.[^dqs][^dqs-ed4-1][^dqs-ed4-0][^dqs-ed2-8][^ceres-data-page]
The Terra-only months (March 2000 through June 2002) and the
NOAA-20-only months (April 2022 onward) are adjusted so that their
calendar-month climatology over the overlap years matches the Terra
plus Aqua one, for the TOA fluxes, the cloud properties and the
surface fluxes, so an anomaly in those periods is by construction an
anomaly against a Terra plus Aqua baseline.[^dqs] The fields change
between editions and releases in ways that move a baseline: Edition
4.2 TOA fluxes are the same as 4.1 from July 2002 through March 2022
but differ before and after, and its surface fluxes differ from 4.1
for every month (MERRA-2 profiles and imager-only clouds); Edition
4.2.1 is the same as 4.2 from March 2000 through March 2022 and
differs from April 2022 onward; and the January 2024 revision of
Edition 4.2 replaced the surface fluxes and the TOA total-area
clear-sky fluxes from March 2000 through June 2023, so that two
Edition 4.2 files with different release dates carry different
values for the same months.[^dqs]

**Wrong-result mode.** An anomaly series computed against a
climatology the analyst builds over a different window (the full
record, or a recent decade) differs from the product's anomalies by
the difference of the two climatologies, and a comparison with a
published EBAF anomaly, or with a model anomaly referenced to the
product's decade, then carries a constant offset per calendar month
that reads as a bias.[^dqs] A climatology file from Edition 4.1 or
from the pre-revision Edition 4.2 release applied to Edition 4.2.1
monthly means, or the reverse, subtracts a baseline computed from
different surface fluxes for every month and from different TOA
fluxes for the single-satellite periods, and the mismatch lands in
the anomaly as a step at the edition boundary or as a seasonal
pattern; and a global mean net flux averaged over the whole record is
not the anchor, which is the decade mean only.[^dqs] The release
date of the file is the only record of which processing it is, and
nothing in a subtraction of two variables checks it.

**Correct approach.** An anomaly statement from EBAF names the base
period (July 2005 through June 2015 for the product's own
climatology), the edition and the release date of the file, taken
from the netCDF file's own attributes as the summary asks, and uses
the climatology and the monthly means from the same edition and
release; a self-built climatology over another window is named as
such with its window.[^dqs] A series that crosses July 2002 or April
2022 is voiced with the climatology adjustment in view: the anomaly
in the single-satellite periods is relative to the Terra plus Aqua
baseline by construction.[^dqs] An Edition 4.2 file released before
January 2024 is replaced by the current release before anomalies are
formed, and any Edition 4.2 and 4.2.1 comparison is confined to April
2022 through July 2024, where the summary says the two can be
compared.[^dqs]

**Verification.** The Edition 4.2 summary states the base period, the
anchoring decade, the periods each edition change affects, the
climatology adjustments and the version history, and asks that the
version and release date in the netCDF file be checked against
it;[^dqs] the Edition 4.1 and 4.0 summaries state the same base
period, and the Edition 2.8 summary states the earlier anchoring
period;[^dqs-ed4-1][^dqs-ed4-0][^dqs-ed2-8] the ordering page lists the
monthly means and climatology entries.[^ceres-data-page] The dataset concept lists this trap among
the product's known issues and carries the edition history.[^dataset]

[^dqs]: CERES_EBAF_Ed4.2 and Ed4.2.1 Data Quality Summary, version 7, 2026-07-01
[^dqs-ed4-1]: CERES_EBAF_Ed4.1 Data Quality Summary, version 3, 2021-12-09
[^dqs-ed4-0]: CERES_EBAF_Ed4.0 Data Quality Summary, 2018-01-12
[^dqs-ed2-8]: CERES_EBAF_Ed2.8 Data Quality Summary, 2014-03-19
[^ceres-data-page]: CERES data products page, EBAF entries
[^dataset]: This bundle's EBAF dataset concept
