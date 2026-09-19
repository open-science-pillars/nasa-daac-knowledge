---
type: convention
spheres: [atmosphere]
title: "CERES clear-sky conventions: the cloud-free-area flux, the filled cloud-free-area flux, the total-region flux and the computed cloud-removed flux, and the pristine and aerosol-free computations beside them"
description: "The CERES radiation products carry more than one quantity named clear-sky. An observed clear-sky flux is built from footprints identified as cloud-free and is missing where a region had none; EBAF fills that map and, from Edition4.1, also carries a total-region clear-sky flux defined the way climate models define one; SYN1deg computes clear-sky fluxes by removing the clouds from the same profiles used for all-sky, so their sampling equals the all-sky sampling, and computes pristine and aerosol-free conditions beside them. A cloud radiative effect is all-sky minus clear-sky in every one of these products, so it inherits whichever convention the subtracted field carries, and nothing in a difference of two flux variables records which one that was."
tags: [ceres, clear-sky, cloud-radiative-effect, convention, ebaf, syn1deg, ssf1deg, pristine, model-comparison]
generated: { by: knowledge-seeder/claude, at: 2026-09-19T05:30:00Z }
status: draft
stale_after: 2027-03-19
sources:
  - id: syn-dqs
    resource: https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_SYN1deg_Ed4A_DQS_V1.pdf
    title: "CERES_SYN1deg_Ed4A Data Quality Summary, version 1, updated 5/8/2025, read in full on 2026-09-19: the all-sky and clear-sky flux computation section, the pristine and aerosol-free conditions, the default clear-sky regions and the cloud fraction threshold, the statement that SYN1deg clear-sky shortwave and longwave fluxes rely on CERES-only clear-sky footprint fluxes, the cautions that the computed clear-sky sampling equals the all-sky sampling and that cloud radiative effects are all-sky minus clear-sky, and the zonal mean caution for default regions"
  - id: ebaf-dqs
    resource: https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_EBAF_Ed4.2_DQS.pdf
    title: "CERES_EBAF_Ed4.2 and Ed4.2.1 Data Quality Summary, version 8, released 9/10/2026, read 2026-09-19 (the unversioned link served version 8 that day, and its clear-sky text is identical to the version 7 copy the bundle's EBAF concepts cite): the gaps in clear-sky maps and their filling, the total-region clear-sky flux added at Edition4.1 and its climate model wording, the cloud radiative effect definition and its change from Edition4.0, the unphysical cloud effect signs under the cloud-free-area definition, and the partly cloudy footprint contribution to the EBAF clear-sky fluxes"
  - id: ceres-data-page
    resource: https://ceres.larc.nasa.gov/data/
    title: "CERES data products page, read 2026-09-19: the clear-sky wording on the EBAF-TOA entry (cloud-free areas of the region) and the EBAF entry (total area of the region), and the SYN1deg parameter groups"
  - id: asdc-guide
    resource: https://asdc.larc.nasa.gov/documents/ceres/guide/cer_syn1deg.pdf
    title: "ASDC CERES SYN1deg Data Set Abstract, read in full on 2026-09-19: the file content list naming the observed clear-sky and all-sky TOA fluxes, the constrained and initial fluxes for the pristine, clear-sky, total-sky-no-aerosol and total-sky conditions, and the direct and diffuse shortwave surface fluxes by condition"
  - id: loeb-2020
    resource: https://doi.org/10.1175/JCLI-D-19-0381.1
    title: "Loeb and others, 2020, Toward a Consistent Definition between Satellite and Model Clear-Sky Radiative Fluxes, Journal of Climate 33, 61 to 75: the paper the EBAF summary names for the total-region clear-sky methodology (record verified on the Crossref registry 2026-09-19; the journal page was not read)"
  - id: ebaf-clear-sky-gotcha
    resource: ../gotchas/ebaf-clear-sky-definitions.md
    title: "This bundle's gotcha on the two EBAF clear-sky definitions, which owns the size of the difference between them and the edition history of the EBAF cloud radiative effect"
  - id: syn-dataset
    resource: ../datasets/ceres-syn1deg.md
    title: "This bundle's SYN1deg dataset concept, which owns the product's resolutions, editions and uncertainty numbers"
---

# CERES clear-sky conventions

**Four quantities are called clear-sky.** The first is the observed
cloud-free-area flux: a CERES footprint is identified as clear or not,
and a regional monthly mean is formed from the clear footprints alone.
In the standard Level 3 products a region that observed no clear-sky
footprint in the month, the threshold being a cloud fraction below
0.1 percent, carries a default value rather than a flux, and the
SYN1deg summary notes that many regions lack clear-sky fluxes in some
months and that zonal means over bands with many default regions are
read with that in mind, no spatial interpolation being
performed.[^syn-dqs] The second is that same cloud-free-area quantity
made spatially complete: EBAF infers clear-sky fluxes from CERES and
imager measurements so that every one degree region has a clear-sky
TOA flux every month, and its TOA clear-sky fluxes take in both the
cloud-free footprints and the clear portion of partly cloudy
footprints, the latter through imager narrowband to broadband
relationships corrected to match the observed footprint clear-sky
fluxes.[^ebaf-dqs] The third is the total-region flux, which EBAF has
carried since Edition4.1 in addition to the cloud-free-area one: the
clear-sky flux for the whole region including its cloudy portions,
which the summary describes as defined in a manner more in line with
how clear-sky fluxes are represented in climate models, and which
Loeb and others 2020 is named for.[^ebaf-dqs][^loeb-2020] The fourth
is the computed cloud-removed flux: SYN1deg computes clear-sky fluxes
hourly by removing the clouds from the radiative transfer calculation,
with the same temperature and humidity profiles as the all-sky
calculation, so that the clear-sky sampling equals the all-sky
sampling; the summary states that this is consistent with the method
used in climate models but differs from the sampling of the observed
TOA clear-sky fluxes that are in the same file.[^syn-dqs]

**Two further conditions sit beside them.** SYN1deg also computes
pristine fluxes, which are the clear-sky computation with the aerosols
removed so that only molecular scattering and absorption remain, and
cloudy-sky fluxes with no aerosols, which are the all-sky computation
with the aerosols removed.[^syn-dqs] Each computed condition exists in
the file twice, as the initial untuned computation and as the
constrained tuned one, and the direct and diffuse surface shortwave
fluxes are carried for total-sky, clear-sky, pristine and actinic
conditions.[^asdc-guide]

**Which convention a field carries.** The observed TOA clear-sky
fluxes in SYN1deg are cloud-free-area fluxes from CERES footprints
alone: the summary states that the Edition4A clear-sky shortwave and
longwave fluxes do not incorporate geostationary-derived clear-sky
fluxes and rely on CERES-only clear-sky footprint fluxes, and that a
region without a single clear Terra or Aqua footprint in the month is
default.[^syn-dqs] The computed clear-sky, pristine and aerosol-free
fluxes in the same file are cloud-removal quantities at every level
the product computes, the TOA, the pressure levels and the
surface.[^syn-dqs][^asdc-guide] On the EBAF side the ordering page
labels the two collections differently, the EBAF-TOA entry as
clear-sky for the cloud-free areas of the region and the EBAF entry as
clear-sky for the total area, and the cloud radiative effect of
Edition4.2 is computed from the total-region flux where Edition4.0
used the cloud-free portions only.[^ceres-data-page][^ebaf-dqs]

**Why mixing them changes a cloud radiative effect.** Both summaries
define the cloud radiative effect the same way, as all-sky flux minus
clear-sky flux.[^syn-dqs][^ebaf-dqs] The definition says nothing about
which clear-sky field is subtracted, so the effect inherits the
convention of its subtrahend. A cloud radiative effect formed against
a pristine flux is a cloud plus aerosol effect, since the aerosols are
absent from one term and present in the other.[^syn-dqs] One formed
against a cloud-free-area flux carries the sampling mismatch between
all-sky and clear-sky that the EBAF summary names as the reason
unphysical signs, a positive net shortwave or a negative net longwave
cloud effect, occur in rare regions and months, the example given
being clear-sky sampled more by day than by night, or at large solar
zenith angle over polar regions.[^ebaf-dqs] One formed against a
computed cloud-removed flux carries no such mismatch, because that
field is sampled exactly where the all-sky field is, which is also why
it is the one the SYN1deg summary calls consistent with the model
method.[^syn-dqs] And one formed by subtracting a computed clear-sky
field from an observed all-sky field crosses two boundaries at once,
the convention and the observed against computed provenance, in a
product whose computed and observed TOA fluxes are not expected to
agree exactly.[^syn-dqs]

**What the documentation does not say.** Neither summary gives a
conversion between the SYN1deg computed cloud-removed clear-sky flux
and the EBAF total-region clear-sky flux, and neither states the size
of the sampling difference between the computed and the observed
clear-sky fields that sit in the same SYN1deg file; the SYN1deg
summary states that the sampling differs and stops
there.[^syn-dqs][^ebaf-dqs] The one documented conversion is EBAF's
own, between the cloud-free-area and total-region definitions, whose
global and regional sizes and whose edition history belong to the
gotcha [ebaf-clear-sky-definitions](../gotchas/ebaf-clear-sky-definitions.md)
and are not repeated here.[^ebaf-clear-sky-gotcha][^loeb-2020] Neither
summary states an uncertainty for the clear-sky fields separate from
the all-sky ones, and the product resolutions, editions and
uncertainty numbers that these conventions are read against belong to
the dataset concepts.[^syn-dataset] Nothing in a flux variable, or in
a difference of two of them, records the convention that produced it:
the convention is fixed by the product, the edition and the variable,
which is where a reader of a cloud radiative effect finds
it.[^ebaf-dqs][^syn-dqs]

[^syn-dqs]: CERES_SYN1deg_Ed4A Data Quality Summary, version 1, 5/8/2025
[^ebaf-dqs]: CERES_EBAF_Ed4.2 and Ed4.2.1 Data Quality Summary, version 8, 9/10/2026
[^ceres-data-page]: CERES data products page, EBAF and SYN1deg entries
[^asdc-guide]: ASDC CERES SYN1deg data set abstract
[^loeb-2020]: Loeb and others, 2020, Journal of Climate, doi:10.1175/JCLI-D-19-0381.1
[^ebaf-clear-sky-gotcha]: This bundle's EBAF clear-sky definitions gotcha
[^syn-dataset]: This bundle's SYN1deg dataset concept
