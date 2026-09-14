---
type: dataset
spheres: [atmosphere]
title: "CERES EBAF Edition 4.2 and 4.2.1: energy balanced and filled top-of-atmosphere and surface radiative fluxes"
description: "Monthly and climatological one degree grids of observed top-of-atmosphere (TOA) and computed surface radiative fluxes, all-sky and clear-sky, with cloud radiative effects and basic cloud properties, March 2000 onward; the global mean net TOA flux is adjusted to an in situ ocean heating estimate, the clear-sky maps are spatially filled, and the record is stitched from Terra-only, Terra plus Aqua and NOAA-20-only periods by regional climatology adjustments. Edition 4.2.1 is the update CMR carries; no per-cell uncertainty field ships with the product."
tags: [ceres, ebaf, radiation-budget, toa-flux, surface-flux, cloud-radiative-effect, asdc]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:30:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-14T05:59:59Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/146 }
resource: https://ceres.larc.nasa.gov/data/#energy-balanced-and-filled-ebaf
version: "Edition 4.2 (TOA fluxes released December 2022, surface fluxes February 2023, both revised on January 2, 2024 for March 2000 through June 2023) and its update Edition 4.2.1 (TOA released November 25, 2024, surface March 14, 2025), which is the edition CMR carries: CERES_EBAF Edition4.2.1 (concept C3880496704-LARC_CLOUD, DOI 10.5067/TERRA-AQUA-NOAA20/CERES/EBAF_L3B004.2.1, TOA and surface in one file) and CERES_EBAF-TOA Edition4.2.1 (concept C3880497643-LARC_CLOUD, DOI 10.5067/TERRA-AQUA-NOAA20/CERES/EBAF-TOA_L3B004.2.1), both beginning 2000-03-01 and ongoing, CMR-verified 2026-09-14; no Edition4.2 collection record remains in CMR that day"
sources:
  - id: dqs
    resource: https://ceres.larc.nasa.gov/documents/DQ_summaries/Versioned/CERES_EBAF_Ed4.2_DQS_V7.pdf
    title: "CERES_EBAF_Ed4.2 and Ed4.2.1 Data Quality Summary, version 7, released 2026-07-01, the pinned copy (byte-identical to the file the unversioned link served on 2026-09-14; the documentation page lists a version 8 posted 2026-09-09, which was served at neither URL that day and was not read), read in full on 2026-09-14: the product description, the cautions, the satellite records and climatology adjustments, the edition changes"
  - id: ceres-data-page
    resource: https://ceres.larc.nasa.gov/data/#energy-balanced-and-filled-ebaf
    title: "CERES data products page (ordering tool), read 2026-09-14: the EBAF and EBAF-TOA entries with their parameter lists, grids and clear-sky wording, the SYN1deg and SSF entries, the availability table"
  - id: ceres-docs-page
    resource: https://ceres.larc.nasa.gov/data/documentation/#ebaf
    title: "CERES documentation page, read 2026-09-14: the EBAF data quality summary versions and the two reference papers"
  - id: asdc-catalog-ebaf
    resource: https://asdc.larc.nasa.gov/project/CERES/CERES_EBAF_Edition4.2.1
    title: "ASDC collection page for CERES_EBAF Edition4.2.1, read 2026-09-14 (it redirects to the Earthdata catalog): abstract, version description, DOI, temporal extent 2000-03-01 to present"
  - id: asdc-catalog-ebaf-toa
    resource: https://asdc.larc.nasa.gov/project/CERES/CERES_EBAF-TOA_Edition4.2.1
    title: "ASDC collection page for CERES_EBAF-TOA Edition4.2.1, read 2026-09-14 (it redirects to the Earthdata catalog): abstract, version description, DOI, temporal extent"
  - id: asdc-guide
    resource: https://asdc.larc.nasa.gov/documents/ceres/guide/cer_ebaf-toa.pdf
    title: "ASDC EBAF-TOA data set abstract (two pages, its edition table ends at Edition 2.8), read 2026-09-14: the product's purpose, and the ocean heat storage term by edition (0.9 for Edition 1A, 0.58 for Edition 2.6r)"
  - id: cmr-ebaf
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C3880496704-LARC_CLOUD.umm_json
    title: "CMR collection record for CERES_EBAF Edition4.2.1, read 2026-09-14: DOI, platforms Terra, Aqua and NOAA-20, temporal extent beginning 2000-03-01 and ending at present, related links"
  - id: cmr-ebaf-toa
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C3880497643-LARC_CLOUD.umm_json
    title: "CMR collection record for CERES_EBAF-TOA Edition4.2.1, read 2026-09-14: DOI, platforms, temporal extent, version description"
  - id: loeb-2018
    resource: https://doi.org/10.1175/JCLI-D-17-0208.1
    title: "Loeb and others, 2018, Clouds and the Earth's Radiant Energy System (CERES) Energy Balanced and Filled (EBAF) Top-of-Atmosphere (TOA) Edition-4.0 Data Product, Journal of Climate 31, 895 to 918: the TOA algorithm, the one-time net flux adjustment and the regional monthly uncertainties (record and abstract read on the Crossref registry 2026-09-14; the journal page was not read)"
  - id: kato-2018
    resource: https://doi.org/10.1175/JCLI-D-17-0523.1
    title: "Kato and others, 2018, Surface Irradiances of Edition 4.0 CERES EBAF Data Product, Journal of Climate 31, 4501 to 4527: the surface algorithm and the global annual mean surface irradiance uncertainties (record and abstract read on the Crossref registry 2026-09-14; the journal page was not read)"
  - id: loeb-2024
    resource: https://doi.org/10.1175/JCLI-D-24-0180.1
    title: "Loeb and others, 2024, Continuity in Top-of-Atmosphere Earth Radiation Budget Observations, Journal of Climate 37, 6093 to 6108: the NOAA-20 transition and the random error of global monthly anomalies after it (record and abstract read on the Crossref registry 2026-09-14)"
  - id: kato-2025
    resource: https://doi.org/10.1175/JCLI-D-23-0568.1
    title: "Kato and others, 2025, Seamless Continuity in CERES EBAF Surface Radiation Budget across Multiple Satellites, Journal of Climate 38, 2461 to 2478: the surface product's continuity across the satellite records; its abstract gives the Terra-only period as March 2000 through July 2002, where the data quality summary ends it in June 2002 (record and abstract read on the Crossref registry 2026-09-14)"
status: stable
stale_after: 2027-03-14
---

# CERES EBAF Edition 4.2 and 4.2.1

**Identity.** The Clouds and the Earth's Radiant Energy System (CERES)
Energy Balanced and Filled (EBAF) product is the CERES project's
Level 3b climate data record: monthly and climatological averages of
observed top-of-atmosphere (TOA) fluxes and computed surface fluxes,
all-sky and clear-sky, with the cloud radiative effect at both levels
and basic cloud properties from the collocated imagers, on a one degree
latitude by longitude grid with zonal and global means, from March
2000 onward.[^ceres-data-page][^asdc-catalog-ebaf] Two things make it
"balanced and filled": the shortwave and longwave TOA fluxes are
adjusted within their uncertainty so that the global mean net TOA flux
matches an in situ estimate of the Earth's heat uptake, and the
clear-sky maps, which have gaps in the standard CERES Level 3 products
wherever a region has no cloud-free footprints in a month, are filled
from CERES and imager measurements so that every region has a
clear-sky flux every month.[^dqs][^loeb-2018] Two collections carry
it: CERES_EBAF, TOA and surface in one file, and CERES_EBAF-TOA, the
TOA fluxes alone.[^cmr-ebaf][^cmr-ebaf-toa] The product page names the
cloud-free-area clear-sky flux as the EBAF-TOA collection's clear-sky
and the total-area clear-sky flux as the combined collection's, and
the data quality summary describes both definitions on the combined
product.[^ceres-data-page][^dqs] The surface fluxes are computed with
a radiative transfer model from assimilated and retrieved inputs and
adjusted for consistency with the observed TOA fluxes; they are not
measurements.[^kato-2018][^dqs]

**Editions.** Edition 4.2 exists because the Terra and Aqua orbits
began drifting from their maintained equator crossing times: the
record is Terra-only from March 2000 through June 2002, Terra plus
Aqua from July 2002 through March 2022, and NOAA-20-only from April
2022 onward, with the single-satellite periods tied to the Terra plus
Aqua record by regional climatology adjustments computed over overlap
periods (July 2002 through June 2007 for Terra, May 2018 through
March 2022 for NOAA-20), applied to the TOA fluxes, the cloud
properties and the computed surface fluxes (the Kato and others 2025
abstract gives the Terra-only period as March 2000 through July 2002;
the summary's June 2002 is used here).[^dqs][^loeb-2024][^kato-2025]
Edition 4.2.1 replaced the GEOS-5.4.1 atmosphere, discontinued in July
2024, with MERRA-2 for the imager cloud retrievals from April 2022
onward, fixed the incorrect NOAA-20 narrowband-to-broadband
coefficients that had affected the Edition 4.2 clear-sky longwave
fluxes from April 2022 through January 2024, recovered some missing
days, and corrected the VIIRS aerosol optical thickness for the surface
fluxes; March 2000 through March 2022 is the same in both, and the
two can be compared from April 2022 through July 2024.[^dqs] The
January 2024 revision of Edition 4.2 replaced the surface fluxes and
the TOA total-area clear-sky fluxes from March 2000 through June 2023,
so two Edition 4.2 files with different release dates carry different
values for those months; the data quality summary asks that the
version and release date in the netCDF file be checked against
it.[^dqs]
The three data quality summary editions read for this concept all
anchor the global mean net flux and define the climatology over the
same decade, July 2005 through June 2015; the anchoring is a one-time
adjustment carried unchanged from Edition 4.1 into 4.2, with an
Edition 4.2 minus 4.1 global net record mean difference below
0.02 W m-2.[^dqs][^loeb-2018]

**Structure.** One netCDF file per collection per order, with monthly
means (regional one degree, zonal one degree, global) and a
climatology whose base period is July 2005 through June 2015; global
means use zonal geodetic weights (the oblate Earth and the annual
cycle of declination and Earth-sun distance make the solar division
factor 4.0034 rather than 4).[^dqs][^ceres-data-page] The TOA fluxes
are defined at a 20 km reference level, the twilight correction adds
refracted shortwave flux for solar zenith angles above 90 degrees so
that outgoing shortwave can exceed the incoming near the terminator
and an albedo formed from the two can exceed one, the surface net
flux is downward minus upward, and the cloud radiative effect is
all-sky minus clear-sky.[^dqs] The cloud properties in the file
(fraction, optical depth, effective pressure and temperature) are
climatologically adjusted for the user's trend monitoring and are not
the cloud properties used to derive the fluxes.[^dqs] The parameter
list on the ordering page names no uncertainty field: the
uncertainties below come from the papers and the data quality summary,
not from the file.[^ceres-data-page]

**Access and identifiers.** The CERES ordering tool subsets and
serves the product; the ASDC collection pages redirect to the
Earthdata catalog, whose pages carry the DOIs and a temporal extent of
2000-03-01 to present.[^ceres-data-page][^asdc-catalog-ebaf][^asdc-catalog-ebaf-toa]
Both CMR records begin 2000-03-01 and end at present, name Terra, Aqua
and NOAA-20 as platforms, and link the Edition 4.2 data quality
summary as their quality document.[^cmr-ebaf][^cmr-ebaf-toa] Observed
on 2026-09-14: the two DOIs resolve to each other's catalog page, the
combined product's DOI (10.5067/TERRA-AQUA-NOAA20/CERES/EBAF_L3B004.2.1)
landing on the EBAF-TOA page and the EBAF-TOA DOI on the combined
product's page, while each page's own DOI field is correct; a user
following a DOI checks the short name on the page it
reaches.[^asdc-catalog-ebaf][^asdc-catalog-ebaf-toa] The ASDC
data set abstract for EBAF-TOA predates Edition 4 (its edition table
ends at 2.8) and quotes an ocean heat storage term of about
0.58 W m-2, the Edition 2.6r value, not the Edition 4 anchor.[^asdc-guide]

## Uncertainty

- **No uncertainty field ships with the product.** The ordering page's
  parameter list has none, and the data quality summary quotes
  uncertainties from the papers.[^ceres-data-page][^dqs]
- **TOA, regional monthly.** For Edition 4.0, whose TOA algorithm
  Edition 4.2 inherits, the one standard deviation uncertainty in a
  one degree regional monthly all-sky TOA flux is 3 W m-2 for the
  Terra-only period and 2.5 W m-2 for the Terra plus Aqua period, for
  shortwave and longwave alike; the clear-sky regional monthly
  uncertainty is 6 and 5 W m-2 (shortwave) and 5 and 4.5 W m-2
  (longwave) for the two periods.[^loeb-2018]
- **TOA, global mean net.** The global mean net TOA flux over July
  2005 through June 2015 is set to the in situ value, 0.71 W m-2, by
  construction; its stated uncertainty is that of the ocean heating
  estimate, not of the radiometry (the gotcha
  [ebaf-imbalance-anchored-to-ocean-heating](../gotchas/ebaf-imbalance-anchored-to-ocean-heating.md)
  carries the composition of that number and its history).[^loeb-2018][^dqs]
- **TOA, across the satellite transitions.** The random error in
  global monthly anomalies following the Terra-only and NOAA-20
  transitions is estimated below 0.15 W m-2 for TOA flux and below
  0.1 percent for cloud fraction.[^loeb-2024]
- **Surface, global annual mean.** For Edition 4.0, whose surface
  algorithm Edition 4.2 inherits, the uncertainties in all-sky global
  annual mean upward and downward shortwave irradiance are 3 and
  4 W m-2, in upward and downward longwave 3 and 6 W m-2, and, with
  all errors taken as independent, 8 W m-2 in the net; Edition 4.2.1
  keeps the regional mean uncertainty of Edition 4.1 and improves the
  anomaly time series.[^kato-2018][^kato-2025] These are different in
  kind from the TOA numbers: they are model output uncertainties
  (the gotcha
  [ebaf-surface-fluxes-are-modelled](../gotchas/ebaf-surface-fluxes-are-modelled.md)).
- **Known artifacts the summary names.** Cloud properties may show
  discontinuities at July 2002 and April 2022; Terra MODIS water vapor
  and 8.55 micron channel degradation since 2008 leaves artificial
  cloud property trends over polar regions and non-polar night oceans,
  with a discontinuity at the February 2016 Terra anomaly; Edition
  4.2.1 over-adjusts Arctic polar night cloud fraction; MERRA-2's
  coarse sea surface temperature source through March 2006 biases
  near-surface and skin temperatures so that surface trends from April
  2006 are the ones the summary stands behind; surface flux
  adjustments are large over the Andes, Tibet and central eastern
  Africa, where deseasonalized anomalies are noisy; Aqua's August
  2020 outage is filled from NOAA-20 for the whole month and September
  1 through 3, 2020 is not filled.[^dqs]

## Known issues

- [ebaf-imbalance-anchored-to-ocean-heating](../gotchas/ebaf-imbalance-anchored-to-ocean-heating.md):
  the global mean net TOA flux is set to an ocean heating estimate
  over a stated decade, so an EBAF imbalance is not an independent
  check of ocean heat content.
- [ebaf-clear-sky-definitions](../gotchas/ebaf-clear-sky-definitions.md):
  cloud-free-area and total-area clear-sky fluxes coexist, the cloud
  radiative effect changed definition at Edition 4.1, and a cloud
  radiative effect names its definition and edition.
- [ebaf-surface-fluxes-are-modelled](../gotchas/ebaf-surface-fluxes-are-modelled.md):
  the surface fluxes are radiative transfer output from assimilated
  and retrieved inputs, with larger and differently shaped
  uncertainty than the TOA fluxes.
- [ebaf-versus-syn1deg-versus-ssf](../gotchas/ebaf-versus-syn1deg-versus-ssf.md):
  EBAF, SYN1deg and SSF answer different questions; a diurnal or
  process study on EBAF's monthly means misses what SYN1deg carries.
- [ebaf-climatology-baseline](../gotchas/ebaf-climatology-baseline.md):
  the climatology base period and the edition and release date fix
  the anomaly baseline.

[^dqs]: CERES_EBAF_Ed4.2 and Ed4.2.1 Data Quality Summary, version 7, 2026-07-01
[^ceres-data-page]: CERES data products page, EBAF entries
[^ceres-docs-page]: CERES documentation page, EBAF entries
[^asdc-catalog-ebaf]: ASDC collection page, CERES_EBAF Edition4.2.1
[^asdc-catalog-ebaf-toa]: ASDC collection page, CERES_EBAF-TOA Edition4.2.1
[^asdc-guide]: ASDC EBAF-TOA data set abstract
[^cmr-ebaf]: CMR collection record C3880496704-LARC_CLOUD
[^cmr-ebaf-toa]: CMR collection record C3880497643-LARC_CLOUD
[^loeb-2018]: Loeb and others, 2018, Journal of Climate, doi:10.1175/JCLI-D-17-0208.1
[^kato-2018]: Kato and others, 2018, Journal of Climate, doi:10.1175/JCLI-D-17-0523.1
[^loeb-2024]: Loeb and others, 2024, Journal of Climate, doi:10.1175/JCLI-D-24-0180.1
[^kato-2025]: Kato and others, 2025, Journal of Climate, doi:10.1175/JCLI-D-23-0568.1
