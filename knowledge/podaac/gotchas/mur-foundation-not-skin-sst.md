---
type: dataset-gotcha
spheres: [hydrosphere]
title: "MUR analysed_sst is a foundation temperature: a comparison against a skin or daytime surface temperature, or a diurnal cycle read from the product, measures the definition and not the ocean"
description: "The MUR analysed field carries the CF standard name sea_surface_foundation_temperature, the temperature below the diurnally stratified layer, similar to a pre-dawn value at one to five metres, built from nighttime skin and subskin observations. A skin radiometer, a daytime infrared retrieval or a model skin temperature includes the diurnal warming and the skin effect that the foundation definition removes, so a difference between them and MUR contains those layers before it contains any error, and a diurnal amplitude derived from MUR is zero by construction."
tags: [ghrsst, mur, sst, foundation, skin, subskin, diurnal, level4, comparison]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:30:00Z }
severity: medium
dataset: ../datasets/ghrsst-mur.md
status: draft
stale_after: 2027-03-14
sources:
  - id: gds-2-0-r5
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ghrsst/open/docs/GDS20r5.pdf
    title: "GHRSST Data Processing Specification version 2.0 revision 5 (2012), the document the PO.DAAC collection page links as the user's guide (read 2026-09-14, the SST type definitions and the Level 4 product specification): the skin, subskin, foundation and depth definitions, and the analysed_sst standard name"
  - id: podaac-collection
    resource: https://podaac.jpl.nasa.gov/dataset/MUR-JPL-L4-GLOB-v4.1
    title: "PO.DAAC collection page, MUR-JPL-L4-GLOB-v4.1 (read 2026-09-14): the description naming nighttime L2P skin and subskin observations and in situ observations as the inputs, and the variable table"
  - id: mur-project
    resource: https://podaac.jpl.nasa.gov/MEaSUREs-MUR
    title: "PO.DAAC MUR project page (read 2026-09-14): the producer's statement that the analysed value estimates the foundation temperature, the near-surface temperature below the extent of diurnal fluctuation"
  - id: doi-product
    resource: https://doi.org/10.5067/GHGMR-4FJ04
    title: "The product DOI, resolved on 2026-09-14 to the Earthdata catalog record for MUR-JPL-L4-GLOB-v4.1, which carries the same description as the collection page"
  - id: dataset
    resource: ../datasets/ghrsst-mur.md
    title: "This bundle's MUR dataset concept (read 2026-09-14), which names foundation-versus-skin mixing as the standing trap"
---

# MUR analysed_sst is a foundation temperature

**Mechanism.** GHRSST defines four temperatures of the upper ocean.
The skin temperature is the temperature of the interface as an
infrared radiometer sees it; the subskin temperature is the
temperature at the base of the conductive laminar layer, about one
millimetre down, which a microwave radiometer approximates and which
carries a large potential diurnal cycle in low wind and high sun; the
foundation temperature is the temperature not influenced by a
thermally stratified layer of diurnal variability, similar to a
night-time minimum or pre-dawn value at depths of about one to five
metres, equal to the subskin temperature only when there is no
diurnal signal; and the depth temperature is a measurement at a
stated depth.[^gds-2-0-r5] The specification states that only in situ
contact thermometry measures the foundation temperature, and that an
analysis procedure estimates it from satellite skin and subskin
measurements.[^gds-2-0-r5] The MUR analysed field carries the
standard name sea_surface_foundation_temperature in the Level 4
format, and the producer states that the analysed value is an
estimate of the foundation temperature, the near-surface temperature
below the extent of diurnal fluctuation due to surface solar
heating.[^gds-2-0-r5][^mur-project] The inputs are nighttime L2P skin
and subskin observations from microwave and infrared instruments and
in situ observations from the iQuam project, so the daytime surface is
not among the observations the analysis is built
from.[^podaac-collection][^doi-product] One analysis exists per day;
there is no time of day inside it.[^podaac-collection]

**Wrong-result mode.** A difference between MUR and a daytime
infrared retrieval, a ship or buoy skin radiometer, a model's skin
temperature or a geostationary afternoon field contains the diurnal
warming and the skin effect, which the foundation definition removes,
before it contains any error of either product; read as a bias or as
a validation statistic it is a statement about the definitions. A
diurnal cycle or an afternoon peak derived from MUR is zero by
construction, so a thermal-stress or air-sea flux calculation that
takes the analysed value as the surface temperature at midday uses a
pre-dawn quantity in the afternoon and is low on calm, sunny days by
the whole stratified layer (this concept's inference from the
definitions above). A match-up against buoys that reports
their depth as if it were the same quantity mixes the foundation
level with a depth temperature, which the specification treats as
distinct types.[^gds-2-0-r5] The dataset concept names this mixing of
product types as the standing trap for MUR comparisons.[^dataset]

**Correct approach.** A comparison against MUR is a comparison
against a foundation temperature: the reference is a pre-dawn or
nighttime value, an in situ temperature at a stated depth in the
one-to-five metre range with the depth recorded, or another foundation
analysis, and the reference's SST type is named beside the
number.[^gds-2-0-r5] A comparison against a skin or subskin quantity
carries a stated model of the diurnal warming and the skin effect, or
is restricted to conditions where the specification says the two
coincide (no diurnal signal), and the residual is reported as the
difference between two defined quantities rather than as an accuracy
of MUR.[^gds-2-0-r5] A question about the surface temperature at a
time of day, or about the diurnal cycle, is outside what the product
carries and is answered from a skin or subskin product or an in situ
record with time stamps.[^mur-project]

**Verification.** The Level 4 specification assigns analysed_sst the
standard name sea_surface_foundation_temperature; no granule was
opened for this concept to read the attribute.[^gds-2-0-r5] The
producer's project page states the foundation definition in its own
words, and the collection page and the DOI's catalog record name the
nighttime inputs.[^mur-project][^podaac-collection][^doi-product]
The specification, the collection page, the project page and the
DOI record were read on 2026-09-14; the DOI resolves to the Earthdata
catalog entry for the collection.[^doi-product] The dataset concept
carries the same caveat among its known issues.[^dataset]

[^gds-2-0-r5]: GHRSST Data Processing Specification version 2.0 revision 5, PO.DAAC archive copy
[^podaac-collection]: PO.DAAC collection page, MUR-JPL-L4-GLOB-v4.1
[^mur-project]: PO.DAAC MUR project page
[^doi-product]: Product DOI 10.5067/GHGMR-4FJ04, resolved to the Earthdata catalog record
[^dataset]: This bundle's MUR dataset concept
