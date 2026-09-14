---
type: dataset-gotcha
spheres: [atmosphere]
title: "EBAF carries two clear-sky definitions, the cloud-free-area flux and the total-region flux, and the cloud radiative effect changed definition at Edition 4.1, so a cloud radiative effect names its definition and edition"
description: "The traditional CERES clear-sky flux is the flux over the cloud-free portions of a one degree region, sampled where cloud-free footprints exist and filled where they do not. Since Edition 4.1 EBAF also carries a clear-sky flux for the total region, the cloudy portions included with their clouds removed, which is the definition climate models use, and the cloud radiative effect is computed from it. The two differ by about 2 W m-2 in the global mean longwave and by more at high latitudes in winter and under cirrus, so a cloud radiative effect compared across editions, or against a model, with the definitions mixed reads the definition change as a change in clouds."
tags: [ceres, ebaf, clear-sky, cloud-radiative-effect, total-region, cloud-free, edition, model-comparison]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:30:00Z }
severity: medium
dataset: ../datasets/ceres-ebaf-ed4-2.md
status: draft
stale_after: 2027-03-14
sources:
  - id: dqs
    resource: https://ceres.larc.nasa.gov/documents/DQ_summaries/Versioned/CERES_EBAF_Ed4.2_DQS_V7.pdf
    title: "CERES_EBAF_Ed4.2 and Ed4.2.1 Data Quality Summary, version 7, 2026-07-01, the pinned copy (byte-identical to the file the unversioned link served on 2026-09-14; the documentation page lists a version 8 posted 2026-09-09, which was served at neither URL that day and was not read), read 2026-09-14: the clear-sky gap problem and its filling, the cloud-free-area flux of Edition 4.0 against the total-region flux added in Edition 4.1, the cloud radiative effect computed from the total-region flux in Edition 4.2, the unphysical cloud effect signs with cloud-free-area fluxes, and the January 2024 revision of the total-area clear-sky fluxes"
  - id: dqs-ed4-0
    resource: https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_EBAF_Ed4.0_DQS.pdf
    title: "CERES_EBAF_Ed4.0 Data Quality Summary, 2018-01-12, read 2026-09-14: the global mean table for July 2005 through June 2015 (Edition 2.8 against 4.0) with clear-sky fluxes and cloud radiative effects, and the change in net cloud radiative effect from clear-sky changes alone"
  - id: ceres-data-page
    resource: https://ceres.larc.nasa.gov/data/#energy-balanced-and-filled-ebaf
    title: "CERES data products page, read 2026-09-14: the EBAF-TOA entry (clear-sky for cloud-free areas of the region) and the EBAF entry (clear-sky for the total area of the region)"
  - id: loeb-2020
    resource: https://doi.org/10.1175/JCLI-D-19-0381.1
    title: "Loeb and others, 2020, Toward a Consistent Definition between Satellite and Model Clear-Sky Radiative Fluxes, Journal of Climate 33, 61 to 75: the adjustment from the cloud-free-area to the total-region definition and its global and regional size (record and abstract read on the Crossref registry 2026-09-14; the journal page was not read)"
  - id: loeb-2018
    resource: https://doi.org/10.1175/JCLI-D-17-0208.1
    title: "Loeb and others, 2018, CERES EBAF TOA Edition-4.0 Data Product, Journal of Climate 31, 895 to 918: the net cloud radiative effect of Edition 4.0 against 2.8 differing by 3 W m-2 owing to clear-sky flux differences (record and abstract read on the Crossref registry 2026-09-14)"
  - id: dataset
    resource: ../datasets/ceres-ebaf-ed4-2.md
    title: "This bundle's EBAF dataset concept, which lists this trap among the known issues"
---

# EBAF clear-sky definitions

**Mechanism.** A CERES clear-sky flux is traditionally the flux over
the cloud-free part of a region: a footprint about 20 km across at
nadir is clear or it is not, monthly clear-sky maps from SSF1deg have
gaps wherever a one degree region had no cloud-free footprints, and
EBAF fills those gaps by inferring clear-sky fluxes from CERES and
imager measurements so that every region has a value every
month.[^dqs] That filled flux is still a cloud-free-area quantity.
Edition 4.0 provided only it; the total-region definition entered at
Edition 4.1, in the summary's words, "in addition to the clear-sky
flux determined only for the cloud-free portions of a region provided
in Ed4.0, EBAF Ed4.1 and subsequent editions also include clear-sky
flux estimates for the total region, which includes the cloudy
portions", defined to match how climate models compute clear-sky
fluxes, and the cloud radiative effect in Edition 4.2 is all-sky
minus that total-region clear-sky flux, where Edition 4.0 used the
cloud-free portions only.[^dqs][^loeb-2020] The size of the
difference is the size of the adjustment that converts one definition
to the other: a global mean longwave adjustment of minus 2.2 W m-2 at
the TOA and 2.7 W m-2 at the surface, pronounced at high latitudes in
winter and in regions of high upper-tropospheric humidity and cirrus
(the west tropical Pacific, the South Pacific and intertropical
convergence zones), and a shortwave adjustment of 0.5 W m-2 at the
TOA and minus 1.9 W m-2 at the surface, largest over sea ice off
Antarctica and over heavy aerosol regions; the interannual variation
of the adjustment is small against that of the cloud radiative
effect.[^loeb-2020] The two EBAF collections are labelled with
different clear-sky wording on the ordering page, cloud-free areas
for EBAF-TOA and total area for EBAF, and the January 2024 revision
of Edition 4.2 replaced the TOA total-area clear-sky fluxes (with the
surface fluxes) from March 2000 through June
2023.[^ceres-data-page][^dqs] Clear-sky definitions have moved before:
the net cloud radiative effect of Edition 4.0 was minus 18 W m-2
against minus 21 W m-2 in Edition 2.8, owing to differences in the
global mean clear-sky fluxes rather than in all-sky ones (the Edition
4.0 summary's table has 268.1 against 265.4 W m-2 clear-sky longwave
and net cloud radiative effect minus 17.9 against minus 21.3 W m-2 for
the same decade).[^loeb-2018][^dqs-ed4-0]

**Wrong-result mode.** A cloud radiative effect from an Edition 4.0
file (cloud-free-area) placed beside one from Edition 4.2 (total
region), or a cloud radiative effect computed by hand as all-sky minus
the cloud-free-area clear-sky flux from a file that also carries the
total-region flux, differs from the product's by about 2 W m-2 in the
global mean longwave and by more regionally, and the difference reads
as a change in clouds between editions or as a model error when the
number is compared with a climate model whose clear-sky flux is by
construction total-region.[^loeb-2020][^dqs] The cloud-free-area
definition also produces cloud radiative effects of unphysical sign in
rare regions and months, a positive net shortwave or a negative net
longwave cloud effect, from the mismatch of sampling between all-sky
and clear-sky (clear-sky sampled more by day than by night, or at
large solar zenith angle over polar regions), which a reader takes for
a cloud property.[^dqs] Nothing in a difference of two flux variables
records which clear-sky definition went into it.

**Correct approach.** A cloud radiative effect statement names the
clear-sky definition (cloud-free-area or total-region), the edition
and the release date of the file it came from, and, for a comparison
with a model or between editions, uses the total-region definition on
both sides, which is what the Edition 4.2 product's own cloud radiative
effect variables carry; a cloud-free-area cloud effect is stated as
such and not compared with a model's.[^dqs][^loeb-2020] Where a
regional value of one definition stands in for the other, the
adjustment's regional structure from Loeb and others 2020 (largest at
high latitudes in winter, under cirrus and over sea ice and heavy
aerosol) is the size of the error being accepted.[^loeb-2020] An
Edition 4.2 file released before January 2024 predates the revision of
the total-area clear-sky fluxes, and the release date in the file
says which processing it is.[^dqs]

**Verification.** The Edition 4.2 summary describes both definitions,
the edition at which the total-region flux entered, the cloud
radiative effect's definition change from Edition 4.0, and the
unphysical signs with cloud-free-area fluxes;[^dqs] the Edition 4.0
summary's global mean table shows the clear-sky and cloud radiative
effect changes between Editions 2.8 and 4.0;[^dqs-ed4-0] the ordering
page labels the two collections' clear-sky wording.[^ceres-data-page] Loeb and others 2020 and Loeb
and others 2018 were verified against the Crossref registry on
2026-09-14 (title, authors, journal, volume, pages, year) and their
abstracts read there, which is where the adjustment sizes and the net
cloud radiative effect difference come from; the journal pages
themselves were not read.[^loeb-2020][^loeb-2018] The dataset concept
lists this trap among the product's known issues.[^dataset]

[^dqs]: CERES_EBAF_Ed4.2 and Ed4.2.1 Data Quality Summary, version 7, 2026-07-01
[^dqs-ed4-0]: CERES_EBAF_Ed4.0 Data Quality Summary, 2018-01-12
[^ceres-data-page]: CERES data products page, EBAF entries
[^loeb-2020]: Loeb and others, 2020, Journal of Climate, doi:10.1175/JCLI-D-19-0381.1
[^loeb-2018]: Loeb and others, 2018, Journal of Climate, doi:10.1175/JCLI-D-17-0208.1
[^dataset]: This bundle's EBAF dataset concept
