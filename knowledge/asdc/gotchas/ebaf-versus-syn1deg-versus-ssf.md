---
type: dataset-gotcha
spheres: [atmosphere]
title: "EBAF, SYN1deg and SSF answer different questions: EBAF is the balanced monthly climate record, SYN1deg carries the hourly diurnal cycle and the in-atmosphere fluxes, SSF carries the instantaneous footprints, and a diurnal or process study on EBAF misses what SYN1deg carries"
description: "The CERES family is a chain. SSF is the Level 2 footprint product, instantaneous and per instrument; SSF1deg grids it daily and monthly per instrument with a constant-meteorology diurnal assumption; SYN1deg adds hourly geostationary fluxes and clouds, MODIS and VIIRS aerosols and Fu-Liou surface and profile fluxes, and is the product the project names for regional diurnal and process studies; EBAF is built on SSF1deg and SYN1deg, monthly only, with its net flux anchored, its clear-sky filled, its single-satellite periods climatologically adjusted, and cloud properties that are not the ones its fluxes were derived with. An unadjusted SYN1deg net imbalance of about 4.3 W m-2, an EBAF-only diurnal cycle, or EBAF clouds correlated with EBAF fluxes as a process each asks a product a question it does not answer."
tags: [ceres, ebaf, syn1deg, ssf, ssf1deg, diurnal-cycle, processing-level, product-choice]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:30:00Z }
severity: medium
dataset: ../datasets/ceres-ebaf-ed4-2.md
status: draft
stale_after: 2027-03-14
sources:
  - id: ceres-data-page
    resource: https://ceres.larc.nasa.gov/data/
    title: "CERES data products page, read 2026-09-14: the EBAF, SYN1deg, SSF, CRS and SSF1deg entries with their one-line purposes, parameter lists, temporal resolutions and edition notes"
  - id: dqs
    resource: https://ceres.larc.nasa.gov/documents/DQ_summaries/Versioned/CERES_EBAF_Ed4.2_DQS_V7.pdf
    title: "CERES_EBAF_Ed4.2 and Ed4.2.1 Data Quality Summary, version 7, 2026-07-01, the pinned copy (byte-identical to the file the unversioned link served on 2026-09-14; the documentation page lists a version 8 posted 2026-09-09, which was served at neither URL that day and was not read), read 2026-09-14: the SYN1deg Edition 4 net imbalance, the SSF1deg constant-meteorology diurnal assumption, the diurnal asymmetry ratio from SYN1deg applied to SSF1deg shortwave, the SYN1deg longwave as the basis of EBAF longwave, the surface fluxes from SYN1deg-Month, the SYN1deg gap filling in the early Terra record, and the EBAF cloud properties not being the ones used for the fluxes"
  - id: cmr-syn1deg
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C3880454295-LARC_CLOUD.umm_json
    title: "CMR collection record for CER_SYN1deg-Month_Terra-Aqua-NOAA20 Edition4B, read 2026-09-14 (the search that day also returned the 1Hour, MHour and Day collections of the same edition, C3181056140, C3181056152 and C3880454279); beginning 2000-03-01"
  - id: cmr-ssf1deg
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C3880508032-LARC_CLOUD.umm_json
    title: "CMR collection record for CER_SSF1deg-Month_Terra-MODIS Edition4A, read 2026-09-14 (the search that day also returned the Aqua Edition4A, C3880507770, and NOAA20-VIIRS Edition1C, C3425515481, monthly collections)"
  - id: loeb-2018
    resource: https://doi.org/10.1175/JCLI-D-17-0208.1
    title: "Loeb and others, 2018, CERES EBAF TOA Edition-4.0 Data Product, Journal of Climate 31, 895 to 918: the EBAF TOA product as the balanced record with regional monthly uncertainties (record and abstract read on the Crossref registry 2026-09-14)"
  - id: loeb-doelling-2020
    resource: https://doi.org/10.3390/rs12081280
    title: "Loeb and Doelling, 2020, CERES EBAF from Afternoon-Only Satellite Orbits, Remote Sensing 12, 1280: the diurnal correction methodology of EBAF shortwave and the Aqua-only against Terra plus Aqua comparison (record and abstract read on the Crossref registry 2026-09-14)"
  - id: dataset
    resource: ../datasets/ceres-ebaf-ed4-2.md
    title: "This bundle's EBAF dataset concept, which lists this trap among the known issues"
---

# EBAF versus SYN1deg versus SSF

**Mechanism.** The CERES products form a chain, and each link has a
stated purpose. SSF (Single Scanner Footprint) is Level 2: the
individual footprint's observed TOA fluxes, imager clouds and
aerosols, and parameterized surface fluxes, instantaneous and per
instrument (Terra, Aqua, S-NPP, NOAA-20), which the project names for
comparison with other sensors in the same orbit.[^ceres-data-page]
SSF1deg is Level 3: daily and monthly gridded averages of SSF per
instrument, which account for the diurnal variation by assuming
constant meteorology between overpasses, so that a drift in a
satellite's crossing time changes its monthly regional fluxes where
clouds have a systematic diurnal cycle (the reason the Terra and Aqua
drift forced the NOAA-20 transition).[^ceres-data-page][^dqs]
SYN1deg is Level 3 with the diurnal cycle in it: hourly CERES and
geostationary TOA fluxes, MODIS or VIIRS and geostationary cloud
properties, MODIS or VIIRS aerosols, and Fu-Liou surface and
in-atmosphere profile fluxes consistent with the observed TOA fluxes,
at hourly, three-hourly, daily and monthly resolutions, and it is the
product the project names as suitable for regional diurnal and
process studies.[^ceres-data-page] EBAF is Level 3b, monthly and
climatological only, built on the two: its shortwave all-sky fluxes
are SSF1deg observations with diurnal corrections whose diurnal
asymmetry ratio comes from SYN1deg, its all-sky longwave fluxes have
the SYN1deg longwave as their basis, its surface fluxes come from
SYN1deg-Month's hourly fluxes, its early Terra data gaps of more than
a week are filled from SYN1deg over non-polar regions, and on top of
that its net flux is anchored, its clear-sky maps are filled, its
single-satellite periods are climatologically adjusted, and the cloud
properties in its file are climatologically adjusted for the user's
trend monitoring and are not the cloud properties used to derive its
TOA fluxes, total clear-sky fluxes or surface fluxes.[^dqs][^loeb-doelling-2020]
The unadjusted SYN1deg Edition 4 global net imbalance is about
4.3 W m-2; EBAF's is 0.71 W m-2 by construction.[^dqs] The current
SYN1deg collections are Edition4B (Terra, Aqua and NOAA-20, from
March 2000), and SSF1deg-Month exists per satellite (Terra and Aqua
Edition4A, NOAA-20 Edition1C).[^cmr-syn1deg][^cmr-ssf1deg]

**Wrong-result mode.** A diurnal cycle of cloud radiative effect, a
morning-versus-afternoon contrast, a study of the radiative response
to a process on hourly or daily time scales, or a match-up with a
field campaign day, run on EBAF, has monthly means as its finest
resolution and cloud properties that were adjusted for continuity and
never fed to the flux calculation, so the "process" it finds is a
relation between a smoothed cloud record and a flux record derived
from a different cloud record.[^dqs] A global mean net flux or an
energy budget from SYN1deg carries the 4.3 W m-2 imbalance and
disagrees with EBAF by that amount, which then reads as a
disagreement between two observations.[^dqs] A clear-sky map from
SSF1deg has gaps where EBAF's is filled, so a clear-sky statistic
over regions or months differs between them by the sampling, and a
per-satellite SSF1deg record after 2021 carries the orbit drift that
EBAF's transition to NOAA-20 was designed to keep out.[^dqs][^ceres-data-page]
A footprint-scale question (a same-orbit sensor comparison, a
single-scene flux) has no answer in either gridded product.[^ceres-data-page]

**Correct approach.** The question chooses the product: a monthly to
decadal climate record, a model evaluation, a global mean budget or a
meridional heat transport is EBAF's purpose, and its numbers carry
the anchoring, the filling and the transitions with them; a diurnal,
daily or process study, or anything that needs in-atmosphere profile
fluxes, is SYN1deg's, whose fluxes are consistent with the observed
TOA but whose net is unbalanced; a footprint or same-orbit comparison
is SSF's; a per-instrument gridded record is SSF1deg's, with its
constant-meteorology diurnal assumption stated.[^ceres-data-page][^dqs]
A statement that mixes them names the product of each term: EBAF
fluxes beside SYN1deg clouds, or an EBAF global mean beside a SYN1deg
regional diurnal cycle, is a legitimate combination when each is
labelled, and the 4.3 against 0.71 W m-2 difference in the global net
is the anchoring, not a discrepancy.[^dqs] The EBAF cloud properties
are a continuity-adjusted record for trend monitoring and are voiced
as such, never as the clouds behind the fluxes in the same
file.[^dqs]

**Verification.** The CERES data products page gives each product's
one-line purpose and its parameters and resolutions, and marks
SYN1deg as suitable for regional diurnal and process studies and SSF
for same-orbit sensor comparison;[^ceres-data-page] the Edition 4.2
summary states the SYN1deg imbalance, the SSF1deg diurnal assumption,
the SYN1deg inputs to EBAF, and that the EBAF cloud properties are not
the ones used to derive the fluxes;[^dqs] the CMR records give the
current SYN1deg and SSF1deg collections and their start dates as read
on 2026-09-14.[^cmr-syn1deg][^cmr-ssf1deg] Loeb and others 2018 and
Loeb and Doelling 2020 were verified against the Crossref registry on
2026-09-14 (title, authors, journal, volume, pages, year) and their
abstracts read there; the journal pages were not
read.[^loeb-2018][^loeb-doelling-2020] The dataset concept lists this
trap among the product's known issues.[^dataset]

[^ceres-data-page]: CERES data products page
[^dqs]: CERES_EBAF_Ed4.2 and Ed4.2.1 Data Quality Summary, version 7, 2026-07-01
[^cmr-syn1deg]: CMR collection record C3880454295-LARC_CLOUD, SYN1deg-Month Edition4B
[^cmr-ssf1deg]: CMR collection record C3880508032-LARC_CLOUD, SSF1deg-Month Terra Edition4A
[^loeb-2018]: Loeb and others, 2018, Journal of Climate, doi:10.1175/JCLI-D-17-0208.1
[^loeb-doelling-2020]: Loeb and Doelling, 2020, Remote Sensing, doi:10.3390/rs12081280
[^dataset]: This bundle's EBAF dataset concept
