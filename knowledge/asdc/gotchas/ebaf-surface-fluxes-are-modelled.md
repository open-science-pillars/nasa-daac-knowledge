---
type: dataset-gotcha
spheres: [atmosphere]
title: "EBAF surface fluxes are radiative transfer output from assimilated and retrieved inputs, adjusted to the observed TOA, so their uncertainty is larger than the TOA fluxes' and shaped by the inputs rather than by the radiometer"
description: "The EBAF surface irradiances are computed hourly with the Fu-Liou radiative transfer model from imager cloud properties, reanalysis temperature and humidity, imager aerosols, retrieved surface albedo and skin temperature, then adjusted so that the computed TOA matches the observed EBAF TOA and recomputed. The global annual mean uncertainty of the surface net irradiance is 8 W m-2 against a TOA global mean net set to 0.71 W m-2, and the summary names regional trend artifacts that come from the inputs (MERRA-2's coarse sea surface temperature before April 2006, the Amazon net longwave trend of Edition 4.2, polar downward longwave trends, noisy anomalies over the Andes, Tibet and central eastern Africa). A surface energy budget or trend read from these fields as observations, with a TOA-sized error, misstates both the value and its uncertainty."
tags: [ceres, ebaf, surface-flux, radiative-transfer, fu-liou, merra-2, lagrange-multiplier, uncertainty, surface-energy-budget]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:30:00Z }
severity: medium
dataset: ../datasets/ceres-ebaf-ed4-2.md
status: draft
stale_after: 2027-03-14
sources:
  - id: dqs
    resource: https://ceres.larc.nasa.gov/documents/DQ_summaries/Versioned/CERES_EBAF_Ed4.2_DQS_V7.pdf
    title: "CERES_EBAF_Ed4.2 and Ed4.2.1 Data Quality Summary, version 7, 2026-07-01, the pinned copy (byte-identical to the file the unversioned link served on 2026-09-14; the documentation page lists a version 8 posted 2026-09-09, which was served at neither URL that day and was not read), read 2026-09-14: the surface flux cautions (MERRA-2 sources through March 2006, the Edition 4.2 skin temperature and Amazon trend, the polar downward longwave trend, the noisy adjustment regions), the Lagrange multiplier adjustment, the inputs (SYN1deg-Month hourly fluxes, MODIS and VIIRS clouds only, MERRA-2 profiles, imager skin temperature under clear sky), the albedo and aerosol corrections, and the January 2024 revision"
  - id: kato-2018
    resource: https://doi.org/10.1175/JCLI-D-17-0523.1
    title: "Kato and others, 2018, Surface Irradiances of Edition 4.0 CERES EBAF Data Product, Journal of Climate 31, 4501 to 4527: the algorithm (computed TOA forced to EBAF-TOA by adjusting surface, cloud and atmospheric properties; bias corrections from AIRS and from CALIPSO and CloudSat; Lagrange multiplier) and the global annual mean uncertainties (record and abstract read on the Crossref registry 2026-09-14; the journal page was not read)"
  - id: kato-2025
    resource: https://doi.org/10.1175/JCLI-D-23-0568.1
    title: "Kato and others, 2025, Seamless Continuity in CERES EBAF Surface Radiation Budget across Multiple Satellites, Journal of Climate 38, 2461 to 2478: the surface product limited to sun-synchronous imager clouds, the bias of a single orbit in strong diurnal cycle regions, the climatological adjustment, and the regional uncertainty unchanged from Edition 4.1 (record and abstract read on the Crossref registry 2026-09-14; the journal page was not read)"
  - id: loeb-2018
    resource: https://doi.org/10.1175/JCLI-D-17-0208.1
    title: "Loeb and others, 2018, CERES EBAF TOA Edition-4.0 Data Product, Journal of Climate 31, 895 to 918: the regional monthly TOA flux uncertainties, for the contrast with the surface numbers (record and abstract read on the Crossref registry 2026-09-14)"
  - id: asdc-catalog-ebaf
    resource: https://asdc.larc.nasa.gov/project/CERES/CERES_EBAF_Edition4.2.1
    title: "ASDC collection page for CERES_EBAF Edition4.2.1, read 2026-09-14: the abstract's statement that the surface fluxes are computed, consistent with EBAF-TOA, with cloud radiative effects from a cloud-free profile in the Fu-Liou radiative transfer model"
  - id: ceres-data-page
    resource: https://ceres.larc.nasa.gov/data/#energy-balanced-and-filled-ebaf
    title: "CERES data products page, read 2026-09-14: the EBAF entry's surface flux parameters"
  - id: dataset
    resource: ../datasets/ceres-ebaf-ed4-2.md
    title: "This bundle's EBAF dataset concept, which lists this trap among the known issues and carries the TOA uncertainties"
---

# EBAF surface fluxes are modelled

**Mechanism.** No CERES instrument measures a surface flux. The EBAF
surface irradiances are computed: the Edition 4.2 surface product is
based on the SYN1deg-Month product's hourly Fu-Liou radiative transfer
fluxes, driven by MODIS and VIIRS cloud properties interpolated in
time between overpasses (geostationary clouds, used in Edition 4.1,
are dropped), MERRA-2 temperature and humidity profiles for the whole
record, imager aerosol optical thickness (Dark Target and Deep Blue,
with corrections to the VIIRS values from April 2022 in Edition
4.2.1), surface albedos from several algorithms with a correction
toward the albedo history map, and a skin temperature that is
imager-derived over land under clear sky and taken from the reanalysis
under cloud.[^dqs][^asdc-catalog-ebaf] The computed TOA irradiances
are then forced to match the EBAF-TOA irradiances by adjusting
surface, cloud and atmospheric properties within their uncertainty,
in two parts, bias corrections (upper-tropospheric temperature and
humidity against AIRS, cloud fraction against CALIPSO and CloudSat)
and a Lagrange multiplier step, after which the surface irradiances
are recomputed with the adjusted properties.[^kato-2018][^dqs] The
uncertainty is therefore that of the inputs and the model, not of a
radiometer: for Edition 4.0 the all-sky global annual mean upward and
downward shortwave irradiances carry 3 and 4 W m-2, the upward and
downward longwave 3 and 6 W m-2, and the net, with all errors taken
as independent, 8 W m-2; Edition 4.2.1 keeps the regional mean
uncertainty of Edition 4.1 and improves the anomaly time
series.[^kato-2018][^kato-2025] The TOA fluxes, by contrast, carry a
regional monthly uncertainty of 2.5 to 3 W m-2 and a global mean net
that is set to 0.71 W m-2 by the anchoring.[^loeb-2018][^dataset] The
shape differs too: the summary names artifacts that are input
artifacts. MERRA-2's coarse sea surface temperature and sea ice
source through March 2006 biases land skin and near-surface air
temperatures high, so surface trends are the summary's from April
2006 on; Edition 4.2 used the GEOS-5.4.1 skin temperatures by mistake,
which makes the regional trend of surface net longwave flux over the
Amazon unphysically large; the Terra water vapor channel degradation
since about 2008 puts a downward trend in polar downward longwave
anomalies in Edition 4.2, mitigated in 4.2.1; the surface flux
adjustments are large over the Andes, Tibet and central eastern
Africa, where deseasonalized anomalies are noisy; and a single
sun-synchronous orbit biases the regional surface irradiance in
regions with strong cloud diurnal cycles, which the climatological
adjustment removes from the mean but which is the reason the
single-satellite periods are adjusted at all.[^dqs][^kato-2025]
The January 2024 revision of Edition 4.2 replaced the surface fluxes
from March 2000 through June 2023.[^dqs]

**Wrong-result mode.** A surface energy budget that takes the EBAF
surface net radiation as an observation and closes it against
turbulent fluxes to a fraction of a watt per square metre has an
8 W m-2 term in it presented as if it were a 0.1 W m-2 one; a regional
surface flux trend over land from March 2000, over the Amazon from
Edition 4.2, or over the poles from Edition 4.2 surface files, is a
trend the summary attributes to the inputs; a downward longwave
anomaly over the Andes or Tibet that looks like a signal is where the
adjustment is largest and the anomalies are noisy.[^dqs][^kato-2018]
A comparison of EBAF surface fluxes with an in situ radiometer site
that treats the difference as site error inverts the direction of the
uncertainty. And an Edition 4.2 surface file released before January
2024 is the superseded processing.[^dqs] The file carries the surface variables beside the TOA ones with no
marker of their different provenance.

**Correct approach.** A surface flux statement from EBAF says that
the flux is computed, names the edition (4.2.1 for anything after
March 2022, where the cloud retrieval and the flux computation share
the same MERRA-2 atmosphere), and quotes the Kato and others 2018
global annual mean uncertainties, 3 and 4 W m-2 shortwave up and
down, 3 and 6 W m-2 longwave up and down, 8 W m-2 net, as the
uncertainty of a global mean, with regional uncertainties larger and
unchanged from Edition 4.1.[^kato-2018][^kato-2025] A surface trend
starts no earlier than April 2006, avoids the Amazon net longwave and
the polar downward longwave in Edition 4.2, and treats the Andes,
Tibet and central eastern Africa anomalies as noisy; a surface energy
budget carries the surface net radiation's uncertainty as a term of
its own rather than inheriting the TOA anchor's.[^dqs] The observed
quantity in the file is the TOA flux; the surface flux is consistent
with it by construction, which is a property of the product, not an
observation of the surface.[^kato-2018]

**Verification.** The Edition 4.2 summary describes the inputs, the
Lagrange multiplier adjustment, the albedo and aerosol corrections
and the surface cautions above, and its version history dates the
January 2024 revision;[^dqs] the ASDC collection page states that the
surface fluxes are computed and consistent with EBAF-TOA;[^asdc-catalog-ebaf]
the ordering page lists the surface flux parameters.[^ceres-data-page] Kato and others 2018, Kato and others 2025
and Loeb and others 2018 were verified against the Crossref registry
on 2026-09-14 (title, authors, journal, volume, pages, year) and their
abstracts read there, which is where the algorithm description and
the uncertainty numbers come from; the journal pages were not
read.[^kato-2018][^kato-2025][^loeb-2018] The dataset concept lists
this trap among the product's known issues.[^dataset]

[^dqs]: CERES_EBAF_Ed4.2 and Ed4.2.1 Data Quality Summary, version 7, 2026-07-01
[^kato-2018]: Kato and others, 2018, Journal of Climate, doi:10.1175/JCLI-D-17-0523.1
[^kato-2025]: Kato and others, 2025, Journal of Climate, doi:10.1175/JCLI-D-23-0568.1
[^loeb-2018]: Loeb and others, 2018, Journal of Climate, doi:10.1175/JCLI-D-17-0208.1
[^asdc-catalog-ebaf]: ASDC collection page, CERES_EBAF Edition4.2.1
[^ceres-data-page]: CERES data products page, EBAF entries
[^dataset]: This bundle's EBAF dataset concept
