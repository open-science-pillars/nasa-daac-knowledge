---
type: dataset-gotcha
spheres: [atmosphere]
title: "Geostationary artifacts sit in the SYN1deg surface and in-atmosphere irradiances, because the observed TOA fluxes are normalized against CERES and the computed fluxes are not, so structure at a domain boundary or at a satellite change is an input artifact before it is weather"
description: "The geostationary radiances that fill the hours between CERES overpasses are cross-calibrated and the broadband geostationary TOA fluxes are regressed onto CERES fluxes, which removes most of the artifacts from the observed fluxes. The computed fluxes get no such normalization: they are driven by the geostationary cloud retrievals themselves, whose channel count, view angle and imager generation change across domain boundaries in space and across satellite replacements in time. The summary states outright that there are geostationary artifacts in the Edition4A surface and in-atmosphere irradiances, and the validation documents show one satellite out of family in its own domain and a longitude discontinuity at a domain edge. Geostationary coverage stops at 60 degrees, so the artifact geography stops there too."
tags: [ceres, syn1deg, geostationary, artifacts, surface-flux, in-atmosphere-flux, cloud-retrieval, view-angle, domain-boundary]
generated: { by: knowledge-seeder/claude, at: 2026-09-19T05:30:00Z }
severity: medium
dataset: ../datasets/ceres-syn1deg.md
status: draft
stale_after: 2027-03-19
sources:
  - id: syn-dqs
    resource: https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_SYN1deg_Ed4A_DQS_V1.pdf
    title: "CERES_SYN1deg_Ed4A Data Quality Summary, version 1, updated 5/8/2025, read in full on 2026-09-19: the computed flux caution naming geostationary artifacts in the surface and in-atmosphere irradiances, the expected change in mean cloud properties at any domain crossing in time or space, the normalization of the geostationary broadband fluxes against CERES by monthly regression over five degree regions, the geostationary cloud retrieval channel families and the two-channel assumptions, the sixty degree coverage limit, the statement that EBAF removes all known geostationary artifacts, and the surface longwave anomaly caution on cloud base heights from the newer imagers"
  - id: syn-dqs-toa
    resource: https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_SYN1deg_TOA_Ed4A.pdf
    title: "CERES Terra/Aqua Edition4A SYN1deg Observed TOA Fluxes, Accuracy and Validation, 4/8/2021, read in full on 2026-09-19: the Edition3A artifacts named as artifacts (the longitude wave pattern from three-hourly sampling, the triangular southern ocean biases at large view zenith angles and the sign change at the 105 degrees west satellite boundary), the statement that most observed hours rest on geostationary clouds so the computed fluxes are impacted by geostationary cloud retrieval quality, the GOES-9 domain being out of family in Edition4A with larger view angles raising cloud fraction and optical depth and so raising computed TOA shortwave and lowering surface shortwave, and the absence of geostationary data poleward of sixty degrees"
  - id: syn-dqs-surface
    resource: https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_SYN1deg_Surface_Ed4A.pdf
    title: "CERES Terra/Aqua Edition4A SYN1deg Computed Fluxes, Accuracy and Validation, 4/8/2021, read in full on 2026-09-19: the section attributing the decreasing surface net longwave anomaly trend to the higher cloud bases and slightly larger cloud fractions retrieved by the newer geostationary imagers, with the larger effect at night, and the pointer to the project's geostationary operational periods table"
  - id: doelling-2013
    resource: https://doi.org/10.1175/JTECH-D-12-00136.1
    title: "Doelling and others, 2013, Geostationary Enhanced Temporal Interpolation for CERES Flux Products, Journal of Atmospheric and Oceanic Technology 30, 1072 to 1090: the geostationary temporal interpolation and normalization method the product rests on (record verified on the Crossref registry 2026-09-19; the journal page was not read)"
  - id: doelling-2016
    resource: https://doi.org/10.1175/JTECH-D-15-0147.1
    title: "Doelling and others, 2016, Advances in Geostationary-Derived Longwave Fluxes for the CERES Synoptic (SYN1deg) Product, Journal of Atmospheric and Oceanic Technology 33, 503 to 521: the geostationary longwave flux algorithm improved for Edition4A (record verified on the Crossref registry 2026-09-19; the journal page was not read)"
  - id: dataset
    resource: ../datasets/ceres-syn1deg.md
    title: "This bundle's SYN1deg dataset concept, which lists this trap among the known issues"
---

# SYN1deg geostationary artifacts

**Mechanism.** The product's hourly coverage comes from the
geostationary constellation, and the two uses it makes of that
constellation are protected very differently. For the observed TOA
fluxes, the geostationary radiances are cross-calibrated against the
imager, converted narrowband to broadband, turned into fluxes with
angular distribution models, and then normalized: matched
instantaneous gridded CERES and geostationary fluxes are regressed
against one another over a month in five degree regions and the
relation is applied to all geostationary fluxes, which removes biases
that depend on cloud amount, on solar and view zenith angle and on
region.[^syn-dqs][^doelling-2013][^doelling-2016] For the computed
fluxes there is no such anchor: they are driven by the geostationary
cloud retrievals themselves, and the validation document states that
because most observed hours rest on geostationary clouds, the computed
fluxes are impacted by the geostationary cloud retrieval
quality.[^syn-dqs-toa] The summary's computed flux cautions say it in
one line, that there are geostationary artifacts in the Edition4A
surface and in-atmosphere irradiances.[^syn-dqs] The retrievals differ
across the constellation by construction: first generation imagers use
two channels, visible and infrared, later ones five, and the
multi-channel imagers use an algorithm close to the imager one, so the
same cloud yields different properties depending on which satellite
watched it; the daytime two-channel retrieval assumes fixed particle
radii and the nighttime two-channel retrieval assumes unit infrared
emissivity, leaving the cloud height unadjusted for optical
depth.[^syn-dqs] The summary states that a change in mean cloud
property values is expected whenever a domain is crossed, in time or
in space.[^syn-dqs] The validation document shows both shapes: in
Edition3A a longitude wave pattern from three-hourly sampling,
triangular biases across the southern ocean where view zenith angles
are largest, and a sign change at 105 degrees west where the two GOES
domains meet, most of which Edition4A removed from the observed
fluxes; and in Edition4A a satellite out of family within its own
domain, GOES-9 from 2003 to 2005 sitting near 160 degrees east rather
than 140, whose larger view angles raised retrieved cloud fractions
and optical depths and with them the computed TOA shortwave flux while
lowering the computed surface shortwave flux.[^syn-dqs-toa] The same
mechanism acts in the longwave through cloud base: the newer imagers
retrieve higher cloud bases and slightly larger cloud fractions, more
so at night, which lowers the computed nighttime downward longwave
irradiance as they replace the older ones.[^syn-dqs-surface] The
geography of all this has an edge, because geostationary data is used
only between 60 degrees south and 60 degrees north, and poleward of
that the product rests on CERES alone.[^syn-dqs][^syn-dqs-toa]

**Wrong-result mode.** A map or a map difference of computed surface
or in-atmosphere irradiance carries structure aligned with the
geostationary domains, longitude bands, a discontinuity at a domain
edge or a bias where view zenith angles are large, and that structure
is read as a regional radiative feature because nothing in the file
names the satellite that produced each hour.[^syn-dqs-toa][^syn-dqs]
A time series at a fixed location that crosses a satellite replacement
picks up the retrieval change as a step or a drift, which the surface
summary has already documented for the nighttime downward longwave
irradiance.[^syn-dqs-surface] A comparison between two regions in
different domains, a Pacific stratus deck against an Atlantic one,
compares imager generations along with the clouds.[^syn-dqs] A
comparison that straddles 60 degrees latitude compares a
geostationary-enhanced estimate with a CERES-only one.[^syn-dqs-toa]
And a reader who checks the observed TOA fluxes in the same file and
finds them clean concludes that the computed fields are clean too,
when the normalization that cleaned the first was never applied to the
second.[^syn-dqs][^syn-dqs-toa]

**Correct approach.** A statement about a computed surface or
in-atmosphere irradiance from SYN1deg carries the geostationary
domain and the satellite that occupied it over the period, which the
project publishes as an operational periods timeline on its general
product information page, and treats structure that aligns with a
domain boundary or a satellite change as an artifact candidate before
it is a result.[^syn-dqs-surface][^syn-dqs] A regional comparison
holds the imager generation fixed where it can, by choosing an
interval inside one satellite's record, and states the crossing where
it cannot.[^syn-dqs-toa] The observed TOA fluxes are the fields the
normalization protects, and the summary's own artifact test is the
difference between the synoptic and the single-instrument gridded
products, which is near zero where no artifact
remains.[^syn-dqs-toa][^doelling-2013] For a monthly mean the summary
points at EBAF-Surface, which uses the SYN1deg fluxes and clouds as
input and removes all known geostationary artifacts, so the artifact
question and the product choice are the same
question.[^syn-dqs] Nothing in the product marks the hours whose
clouds came from which satellite, so the attribution is made from the
timeline rather than from the file.[^syn-dqs]

**Verification.** The Edition4A summary states the geostationary
artifacts in the surface and in-atmosphere irradiances, describes the
normalization of the observed geostationary fluxes against CERES, sets
out the retrieval channel families and their assumptions, gives the
sixty degree coverage limit and states that EBAF removes all known
geostationary artifacts.[^syn-dqs] The TOA validation document names
the Edition3A patterns as artifacts, states that the computed fluxes
are impacted by geostationary cloud retrieval quality, and documents
the GOES-9 domain as out of family in Edition4A.[^syn-dqs-toa] The
surface validation document attributes the nighttime downward longwave
change to the newer imagers' cloud bases and points at the operational
periods table.[^syn-dqs-surface] Doelling and others 2013 and Doelling
and others 2016 were verified against the Crossref registry on
2026-09-19 (title, authors, journal, volume, pages, year); the journal
pages were not read.[^doelling-2013][^doelling-2016] The dataset
concept lists this trap among the product's known issues.[^dataset]

[^syn-dqs]: CERES_SYN1deg_Ed4A Data Quality Summary, version 1, 5/8/2025
[^syn-dqs-toa]: CERES SYN1deg Edition4A observed TOA flux accuracy and validation, 4/8/2021
[^syn-dqs-surface]: CERES SYN1deg Edition4A computed flux accuracy and validation, 4/8/2021
[^doelling-2013]: Doelling and others, 2013, Journal of Atmospheric and Oceanic Technology, doi:10.1175/JTECH-D-12-00136.1
[^doelling-2016]: Doelling and others, 2016, Journal of Atmospheric and Oceanic Technology, doi:10.1175/JTECH-D-15-0147.1
[^dataset]: This bundle's SYN1deg dataset concept
