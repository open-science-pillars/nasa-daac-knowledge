---
type: dataset-gotcha
spheres: [atmosphere]
title: "SYN1deg surface and in-atmosphere fluxes are radiative transfer output, and the tuned fields that would tie them to the observed TOA are the ones the summary advises against using, so the usable computed fluxes in this product are unconstrained"
description: "No CERES instrument measures a surface or an in-atmosphere flux. In SYN1deg every flux at the surface and at the 70, 200, 500 and 850 hPa levels is a Langley Fu-Liou computation from imager and geostationary cloud retrievals, reanalysis profiles, MATCH aerosols and retrieved albedos. The file carries both the initial untuned fields and the constrained tuned ones, and the summary states that the adjusted shortwave and longwave fluxes contain errors from code bugs, while the TOA validation document states that tuning the computed fluxes to the observed ones was unsuccessful for geostationary clouds. The observed quantity in the file is the TOA flux; the computed TOA flux beside it is not expected to match it, and the hourly surface uncertainty is several times the monthly one."
tags: [ceres, syn1deg, surface-flux, in-atmosphere-flux, radiative-transfer, fu-liou, tuned-fluxes, entropy, uncertainty]
generated: { by: knowledge-seeder/claude, at: 2026-09-19T05:30:00Z }
severity: high
dataset: ../datasets/ceres-syn1deg.md
eval_case: syn1deg-surface-fluxes-are-modelled-not-measured
status: draft
stale_after: 2027-03-19
sources:
  - id: syn-dqs
    resource: https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_SYN1deg_Ed4A_DQS_V1.pdf
    title: "CERES_SYN1deg_Ed4A Data Quality Summary, version 1, updated 5/8/2025, read in full on 2026-09-19: the statement that computed surface and in-atmosphere fluxes are only available through SYN1deg, the two TOA flux approaches and their agreement as a quality indicator, the computed flux algorithm and its inputs, the four pressure levels, the computed flux caution that the adjusted fluxes contain errors from code bugs and that the initial fluxes carry geostationary cloud artifacts, the entropy parameters computed with adjusted fluxes, and the recommendation of EBAF-Surface for monthly means"
  - id: syn-dqs-surface
    resource: https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_SYN1deg_Surface_Ed4A.pdf
    title: "CERES Terra/Aqua Edition4A SYN1deg Computed Fluxes, Accuracy and Validation, 4/8/2021, read in full on 2026-09-19: the statement that monthly mean SYN1deg computed surface flux uncertainties are generally the same as EBAF-Surface Edition4.0, the uncertainty table by temporal and spatial scale including the hourly gridded column, the buoy and land site comparisons and the Greenland Summit comparison"
  - id: syn-dqs-toa
    resource: https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_SYN1deg_TOA_Ed4A.pdf
    title: "CERES Terra/Aqua Edition4A SYN1deg Observed TOA Fluxes, Accuracy and Validation, 4/8/2021, read in full on 2026-09-19: the statement that tuning the computed fluxes by adjusting clouds and profile parameters was unsuccessful for geostationary clouds because the retrieval uncertainties were too large, and the comparison of the untuned computed shortwave anomalies across the geostationary record"
  - id: asdc-guide
    resource: https://asdc.larc.nasa.gov/documents/ceres/guide/cer_syn1deg.pdf
    title: "ASDC CERES SYN1deg Data Set Abstract, read in full on 2026-09-19: the file content list naming the constrained (tuned) vertical flux profiles, the constrained and initial TOA and surface fluxes by sky condition, and the adjusted radiative transfer model input parameters"
  - id: ceres-data-page
    resource: https://ceres.larc.nasa.gov/data/
    title: "CERES data products page, read 2026-09-19: the SYN1deg one-line description, which calls the Fu-Liou surface and in-atmospheric fluxes consistent with the CERES observed TOA fluxes, and the parameter groups that mark the surface and in-atmospheric fluxes as computed"
  - id: rutan-2015
    resource: https://doi.org/10.1175/JTECH-D-14-00165.1
    title: "Rutan and others, 2015, CERES Synoptic Product: Methodology and Validation of Surface Radiant Flux, Journal of Atmospheric and Oceanic Technology 32, 1121 to 1143: the synoptic product's surface flux methodology and validation (record verified on the Crossref registry 2026-09-19; the journal page was not read)"
  - id: ebaf-gotcha
    resource: ../gotchas/ebaf-surface-fluxes-are-modelled.md
    title: "This bundle's gotcha on the EBAF surface fluxes, which owns the adjustment chain that forces the computed TOA to the observed EBAF TOA and the global annual mean uncertainties of that product"
  - id: dataset
    resource: ../datasets/ceres-syn1deg.md
    title: "This bundle's SYN1deg dataset concept, which lists this trap among the known issues and carries the product's uncertainty table"
---

# SYN1deg surface fluxes are modelled, not measured

**Mechanism.** The CERES instruments measure broadband radiances at
the top of the atmosphere, and the summary says plainly that computed
surface and in-atmosphere fluxes are only available through the
SYN1deg product.[^syn-dqs] Every such field is Langley Fu-Liou
radiative transfer output: cloud properties retrieved from MODIS or
VIIRS and from the geostationary imagers, stratified into four cloud
types per hour box and interpolated across missing hours, temperature,
humidity and ozone profiles from the assimilation, MATCH aerosol
optical thickness with its seven constituent types, ocean albedo from
a model and land albedo inferred from clear-sky TOA albedo, and an
empirical cloud base pressure that largely sets the downward longwave
flux in midlatitude and polar regions.[^syn-dqs][^rutan-2015] The same
computation produces the fluxes at 70, 200, 500 and 850 hPa, so an
atmospheric flux divergence taken from this product is a difference of
two model outputs.[^syn-dqs] That much the product shares with the
energy balanced one, whose gotcha
[ebaf-surface-fluxes-are-modelled](../gotchas/ebaf-surface-fluxes-are-modelled.md)
carries the adjustment chain and the global annual mean uncertainty
budget.[^ebaf-gotcha] What is different here is the constraint, or its
absence. The file carries each computed condition twice, as the
initial untuned computation and as the constrained tuned one, with the
adjusted radiative transfer inputs beside them.[^asdc-guide] The
summary's computed flux cautions state that, owing to bugs in the
code, the adjusted fluxes contain errors and that users are advised
not to use the adjusted shortwave and longwave fluxes, and that the
initial fluxes are affected by artifacts in cloud properties derived
from geostationary satellites.[^syn-dqs] The TOA validation document
adds why the tuning was thin in the first place: adjusting clouds and
profile parameters to bring the computed fluxes onto the observed ones
was unsuccessful for geostationary clouds, because the geostationary
retrieval uncertainties were too large to adjust the individual
properties with confidence.[^syn-dqs-toa] The product therefore states
its own quality check rather than enforcing it: computed TOA fluxes
from SYN1deg do not necessarily agree with the CERES-derived TOA
fluxes in the same file, and the agreement of the two approaches is
the indicator of TOA flux quality.[^syn-dqs] Users who do not need
hourly surface fluxes or the in-atmosphere levels are pointed to
EBAF-Surface, which is where the adjustment to the observed TOA
actually happens.[^syn-dqs] One consequence is easy to miss: the
entropy variables the product added at Edition4A are computed with the
adjusted fluxes, so they rest on the fields the cautions set
aside.[^syn-dqs] The scale of the uncertainty follows the scale of the
use: the surface validation document gives the hourly gridded downward
shortwave uncertainty as 43 W m-2 and the downward longwave as
21 W m-2 for ocean plus land, against 13 and 7 W m-2 for the monthly
gridded values.[^syn-dqs-surface]

**Wrong-result mode.** A surface energy budget or a cloud radiative
effect at the surface that takes a SYN1deg irradiance as an
observation inherits the uncertainty of the clouds, the profiles and
the aerosols with no marker in the file that this is what it is, and
at hourly resolution that uncertainty is several times the monthly
one.[^syn-dqs-surface] A comparison against a ground site that reads
the difference as site error inverts the direction of the uncertainty,
which is the comparison the product invites, since its own summary
offers the diurnally complete hourly surface fluxes as comparable with
ground site fluxes.[^syn-dqs] An atmospheric heating rate profile from
the in-atmosphere levels, presented beside observed TOA fluxes from
the same file, reads as an observed divergence when only one end of it
was observed.[^syn-dqs] A user who picks the constrained fields
because "constrained to the observed TOA" is the phrase the ordering
page uses for this product's computed fluxes lands on exactly the
fields the summary advises against, and a user who picks the initial
fields gets the geostationary cloud artifacts
instead.[^ceres-data-page][^syn-dqs] An entropy production statement
inherits the same problem one step removed.[^syn-dqs] And a computed
minus observed TOA difference in this product read as an error in the
observations reverses the summary's own reading of that difference as
a quality indicator for both.[^syn-dqs]

**Correct approach.** A flux statement at the surface or inside the
atmosphere from SYN1deg names the quantity as computed with the
Fu-Liou model from imager and geostationary clouds, assimilation
profiles and MATCH aerosols, and carries the uncertainty of the scale
it is used at, the hourly gridded numbers for an hourly or diurnal
statement and the monthly ones for a monthly mean.[^syn-dqs][^syn-dqs-surface]
Where the tuned fields are involved, the statement records that the
summary advises against the adjusted shortwave and longwave fluxes and
that the alternative initial fields carry geostationary cloud
artifacts, so that neither is voiced as a flux constrained to the
observations.[^syn-dqs] A monthly mean surface flux has a product of
its own, EBAF-Surface, whose adjustment to the observed TOA is
documented and whose gotcha carries its uncertainty; the synoptic
product earns its place where the hourly cycle or the in-atmosphere
levels are the point.[^syn-dqs][^ebaf-gotcha] A comparison with ground
sites is a validation of the computation against the measurement, in
that direction, with the published site statistics as the context the
difference is read against.[^syn-dqs-surface] The observed quantity in
the file remains the TOA flux, and the distance between the computed
and observed TOA fluxes is the product's own statement about how far
the computation stands from the measurement that month.[^syn-dqs]

**Verification.** The Edition4A summary states that computed surface
and in-atmosphere fluxes are available only through SYN1deg, describes
the two TOA approaches and names their agreement as the quality
indicator, lists the computed flux inputs and the four pressure
levels, carries the cautions on the adjusted and initial fluxes and on
the entropy parameters, and recommends EBAF-Surface to users of
monthly means.[^syn-dqs] The TOA validation document states that the
tuning was unsuccessful for geostationary clouds.[^syn-dqs-toa] The
surface validation document carries the uncertainty table by temporal
and spatial scale and the site comparisons.[^syn-dqs-surface] The
ASDC data set abstract lists the constrained and initial fields and
the adjusted model inputs as separate file
contents.[^asdc-guide] The ordering page's one-line description of the
product is where the phrase about consistency with the observed TOA
fluxes appears.[^ceres-data-page] Rutan and others 2015 was verified
against the Crossref registry on 2026-09-19 (title, authors, journal,
volume, pages, year); the journal page was not read.[^rutan-2015] The
dataset concept lists this trap among the product's known
issues.[^dataset]

[^syn-dqs]: CERES_SYN1deg_Ed4A Data Quality Summary, version 1, 5/8/2025
[^syn-dqs-surface]: CERES SYN1deg Edition4A computed flux accuracy and validation, 4/8/2021
[^syn-dqs-toa]: CERES SYN1deg Edition4A observed TOA flux accuracy and validation, 4/8/2021
[^asdc-guide]: ASDC CERES SYN1deg data set abstract
[^ceres-data-page]: CERES data products page, SYN1deg entry
[^rutan-2015]: Rutan and others, 2015, Journal of Atmospheric and Oceanic Technology, doi:10.1175/JTECH-D-14-00165.1
[^ebaf-gotcha]: This bundle's EBAF surface fluxes gotcha
[^dataset]: This bundle's SYN1deg dataset concept
