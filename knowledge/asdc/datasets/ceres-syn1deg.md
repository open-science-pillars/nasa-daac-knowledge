---
type: dataset
spheres: [atmosphere]
title: "CERES SYN1deg Edition4A, Edition4B and Edition1A: synoptic one degree observed and computed top-of-atmosphere, in-atmosphere and surface fluxes with clouds and aerosols"
description: "Hourly, three-hourly, daily, monthly hourly and monthly one degree grids of CERES observed top-of-atmosphere fluxes enhanced with hourly geostationary fluxes and clouds, together with Fu-Liou computed fluxes at the top of the atmosphere, at four pressure levels and at the surface, all-sky, clear-sky, pristine and aerosol-free, from March 2000 onward. It is the only CERES product carrying computed in-atmosphere profile fluxes and the project's product for regional diurnal and process studies. Its own data quality summary states that it should not be used to infer long-term trends of clouds or fluxes and is not of climate quality, and sends trend users to EBAF."
tags: [ceres, syn1deg, radiation-budget, diurnal-cycle, surface-flux, in-atmosphere-flux, geostationary, fu-liou, asdc]
generated: { by: knowledge-seeder/claude, at: 2026-09-19T05:30:00Z }
verified:
  - { by: human:PaulMRamirez, at: 2026-09-19T06:21:35Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/191 }
  - { by: human:PaulMRamirez, at: 2026-09-20T21:41:20Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/207 }
resource: https://ceres.larc.nasa.gov/data/
version: "Edition4B for Terra-Aqua-NOAA20 (release date May 7, 2025, named Edition4.2 on the ordering tool), the edition CMR carries: CER_SYN1deg-Month_Terra-Aqua-NOAA20 (concept C3880454295-LARC_CLOUD, DOI 10.5067/TERRA-AQUA-NOAA20/CERES/SYN1DEGMONTH_L3.004B), CER_SYN1deg-1Hour (C3181056140-LARC_CLOUD), CER_SYN1deg-MHour (C3181056152-LARC_CLOUD) and CER_SYN1deg-Day (C3880454279-LARC_CLOUD), all Edition4B, all beginning 2000-03-01 and ending at present, CMR-verified 2026-09-19; the earlier data sets are Terra-Aqua Edition4A (release date September 13, 2017) and Terra-NPP Edition1A (release date October 3, 2017), and the only data quality summary published for the family is the Edition4A one, whose front page introduces Edition4B and says an updated summary will be available soon"
sources:
  - id: syn-dqs
    resource: https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_SYN1deg_Ed4A_DQS_V1.pdf
    title: "CERES_SYN1deg_Ed4A Data Quality Summary, version 1, updated 5/8/2025, read in full on 2026-09-19: the note to users introducing Edition4B, the nature of the products, the observed and computed flux algorithms and inputs, the all-sky and clear-sky flux computations, the processing level table, the cautions and helpful hints, the version history, the expected reprocessing and the attribution section. The documentation page links this file from the unversioned DQ_summaries directory and lists no SYN1deg summary in the Versioned directory as of that date"
  - id: syn-dqs-toa
    resource: https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_SYN1deg_TOA_Ed4A.pdf
    title: "CERES Terra/Aqua Edition4A SYN1deg Observed TOA Fluxes, Accuracy and Validation, 4/8/2021, read in full on 2026-09-19: the regional monthly all-sky shortwave and longwave uncertainty terms and their combinations, the daily and hourly diurnal uncertainties, and the Edition4A against Edition3A comparisons against SSF1deg"
  - id: syn-dqs-surface
    resource: https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_SYN1deg_Surface_Ed4A.pdf
    title: "CERES Terra/Aqua Edition4A SYN1deg Computed Fluxes, Accuracy and Validation, 4/8/2021, read in full on 2026-09-19: the statement that monthly mean SYN1deg computed surface flux uncertainties are generally the same as EBAF-Surface Edition4.0, the uncertainty table, the buoy and land site comparisons, the polar night longwave section, the 2004 aerosol optical thickness issue and the geostationary cloud base height section"
  - id: ceres-data-page
    resource: https://ceres.larc.nasa.gov/data/
    title: "CERES data products page (visualization, ordering and subsetting tool), read 2026-09-19: the SYN1deg entry with its one-line purpose, its parameter list by group, its spatial and temporal resolution table and its ordering link, and the SSF and CldTypHist entries"
  - id: ceres-docs-page
    resource: https://ceres.larc.nasa.gov/data/documentation/
    title: "CERES documentation page, read 2026-09-19: the data quality summary table (the SYN1deg row, its editions, its version numbers and its posting dates) and the SYN1deg reference list"
  - id: asdc-guide
    resource: https://asdc.larc.nasa.gov/documents/ceres/guide/cer_syn1deg.pdf
    title: "ASDC CERES SYN1deg Data Set Abstract (five pages), read in full on 2026-09-19: the per-product descriptions, the list of what the files include, the discontinuation of SYN1deg-M3Hour at Edition4A and the modification history tables"
  - id: asdc-catalog
    resource: https://asdc.larc.nasa.gov/project/CERES/CER_SYN1deg-Month_Terra-Aqua-NOAA20_Edition4B
    title: "ASDC collection page for CER_SYN1deg-Month Edition4B, read 2026-09-19: it redirects to the Earthdata catalog page for the collection, as the ASDC project pages do"
  - id: cmr-syn-month
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C3880454295-LARC_CLOUD.umm_json
    title: "CMR collection record for CER_SYN1deg-Month_Terra-Aqua-NOAA20 Edition4B, read 2026-09-19: the DOI, the version description, the processing level, the platforms and instruments, the temporal extent, the abstract and the related URLs including the ordering tool link"
  - id: cmr-syn-family
    resource: https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=CER_SYN1deg*&options%5Bshort_name%5D%5Bpattern%5D=true
    title: "CMR short name pattern search for CER_SYN1deg collections, run 2026-09-19: four collections, Month, Day, MHour and 1Hour, all Edition4B Terra-Aqua-NOAA20, all beginning 2000-03-01 with no end date and collection progress ACTIVE, and no SYN1deg-3Hour collection among them"
  - id: doi-syn
    resource: https://doi.org/10.5067/TERRA-AQUA-NOAA20/CERES/SYN1DEGMONTH_L3.004B
    title: "DOI resolution checks run 2026-09-19: the four Edition4B DOIs each redirect (302) to their own collection's Earthdata catalog page, while the Terra+Aqua Edition4A and Terra+NPP Edition1A DOIs printed in the data quality summary's attribution section return 404"
  - id: ebaf-dqs
    resource: https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_EBAF_Ed4.2_DQS.pdf
    title: "CERES_EBAF_Ed4.2 and Ed4.2.1 Data Quality Summary, version 8, released 9/10/2026, read 2026-09-19 (the unversioned link served version 8 that day; the bundle's EBAF concepts cite version 7, whose clear-sky and product-description text is identical): the SYN1deg Edition4 net imbalance, the EBAF clear-sky filling and the EBAF transitions"
  - id: rutan-2015
    resource: https://doi.org/10.1175/JTECH-D-14-00165.1
    title: "Rutan and others, 2015, CERES Synoptic Product: Methodology and Validation of Surface Radiant Flux, Journal of Atmospheric and Oceanic Technology 32, 1121 to 1143: the synoptic product's surface flux methodology and validation, named by the CERES documentation page as the product's surface flux reference (record verified on the Crossref registry 2026-09-19; the journal page was not read)"
  - id: doelling-2013
    resource: https://doi.org/10.1175/JTECH-D-12-00136.1
    title: "Doelling and others, 2013, Geostationary Enhanced Temporal Interpolation for CERES Flux Products, Journal of Atmospheric and Oceanic Technology 30, 1072 to 1090: the geostationary temporal interpolation the product rests on, named by the CERES documentation page as a SYN1deg flux reference (record verified on the Crossref registry 2026-09-19; the journal page was not read)"
  - id: doelling-2016
    resource: https://doi.org/10.1175/JTECH-D-15-0147.1
    title: "Doelling and others, 2016, Advances in Geostationary-Derived Longwave Fluxes for the CERES Synoptic (SYN1deg) Product, Journal of Atmospheric and Oceanic Technology 33, 503 to 521: the geostationary longwave flux algorithm, named by the CERES documentation page as a SYN1deg flux reference (record verified on the Crossref registry 2026-09-19; the journal page was not read)"
status: stable
stale_after: 2027-03-19
---

# CERES SYN1deg

**Identity.** The CERES Synoptic one degree (SYN1deg) products are the
project's Level 3 synoptic record: one degree regional averages of
observed top-of-atmosphere (TOA) fluxes together with computed TOA,
in-atmosphere and surface fluxes, coincident imager cloud and aerosol
properties and hourly geostationary cloud properties, at hourly,
three-hourly, daily, monthly hourly and monthly
resolution.[^syn-dqs][^cmr-syn-month] The observed fluxes come from
CERES radiances converted with angular distribution models and from
geostationary radiances converted narrowband to broadband and then
normalized against CERES, so that the hours between the Terra, Aqua
and NOAA-20 overpasses are filled by measurements rather than by an
assumption of constant meteorology.[^syn-dqs][^doelling-2013][^doelling-2016]
The computed fluxes come from the Langley Fu-Liou radiative transfer
model driven by imager and geostationary cloud properties, reanalysis
temperature, humidity and ozone profiles, MATCH aerosols and retrieved
surface albedos.[^syn-dqs][^rutan-2015] Two things distinguish it from
the energy balanced product this bundle already carries: it is the only
CERES product that carries computed surface and in-atmosphere fluxes,
and it carries a synoptic rather than a monthly view, which is why the
ordering page names it for regional diurnal and process
studies.[^syn-dqs][^ceres-data-page] The summary names field campaigns
and intensive observation periods as further uses, and states that the
hourly computed surface fluxes can be compared with ground site
fluxes.[^syn-dqs]

**What it is not for.** The summary's own words: the product "should
not be used to infer long-term trends of clouds or fluxes and are not
of climate quality", and users are advised to use the EBAF-TOA and
EBAF-Surface products to determine the long-term flux natural
variability and temporal trending.[^syn-dqs] The unadjusted global
mean net TOA imbalance is the reason a global budget is not asked of
it either: the SYN1deg summary gives the Edition4A net imbalance as
about plus 4.5 W m-2 against an expected ocean heating rate of about
0.71 W m-2, and the EBAF summary, describing the same quantity, gives
about 4.3 W m-2, so the two documents differ on the number by
0.2 W m-2.[^syn-dqs][^ebaf-dqs] The gotcha
[syn1deg-refuses-long-term-trend-use](../gotchas/syn1deg-refuses-long-term-trend-use.md)
carries what the refusal covers and what it leaves open, and
[ebaf-versus-syn1deg-versus-ssf](../gotchas/ebaf-versus-syn1deg-versus-ssf.md)
carries the division of labour across the family.

**Editions.** Three data sets carry the product: Terra-Aqua Edition4A,
released September 13, 2017; Terra-NPP Edition1A, released October 3,
2017, produced with similar code, and whose NPP CERES instrument is
not placed on the same radiometric scale as Terra's; and
Terra-Aqua-NOAA20 Edition4B, released May 7, 2025, which the ordering
tool labels Edition4.2.[^syn-dqs] Edition4B improves the
three-channel geostationary cloud retrievals, especially at night,
makes the Meteosat 8 through 11 retrievals consistent, avoids suspect
cloud retrievals during twilight, has no Terra or Aqua observations
from April 2022 onward and uses NOAA-20 alone, and bases the cloud
retrievals and flux computations from April 2022 on the MERRA-2
reanalysis; the CMR version description adds the improvement to
two-channel imagers early in the mission and to Meteosat 8 and 9, and
the interpolation that fills the hours where the twilight retrievals
were removed.[^syn-dqs][^cmr-syn-month] Documentation lags the
product: the only published data quality summary is the Edition4A one,
whose note to users introduces Edition4B and says an updated summary
will be available soon, so an Edition4B file is read against an
Edition4A document.[^syn-dqs][^ceres-docs-page] The Edition4A
Terra-Aqua record is not planned for reprocessing until the CERES
Edition 5 suite exists, and coverage is extended in two month
intervals.[^syn-dqs]

**Structure.** The archived temporal resolutions are SYN1deg-1Hour,
SYN1deg-3Hour, SYN1deg-Day, SYN1deg-MHour and SYN1deg-Month; the
monthly three-hourly product, SYN1deg-M3Hour, was discontinued at
Edition4A, where the hourly and daily products were added, and the
ordering page's resolution table still lists it.[^asdc-guide][^ceres-data-page]
Processing is done on a nested grid with one degree equal-angle
regions between 45 degrees north and south and wider longitude zones
toward the poles, and the delivered file is a complete 360 by 180 one
degree grid produced by replication; zonal and global means exist only
on SYN1deg-Month, because the geographical distribution and number of
clear-sky regions are considered insufficient for a representative
zonal or global mean on the finer products.[^syn-dqs] Global means are
geodetic area-weighted averages of the 180 zonal means, with the
oblate Earth and the annual cycle of declination and Earth-sun
distance giving the solar division factor 4.0034 rather than
4.[^syn-dqs] The hour index of the hourly product is GMT, 0 to 1 GMT
being the first hour box, whose midpoint is 0.5 GMT except for
shortwave fluxes, where the integrated cosine of the solar zenith
angle is the midpoint.[^syn-dqs] No twilight flux is added at
Edition4A, unlike Edition3A, so the shortwave flux and the albedo are
consistent with each other and albedo is a daytime
parameter.[^syn-dqs]

The computed fluxes are evaluated at the TOA, at four pressure levels
(70, 200, 500 and 850 hPa) and at the surface; the ASDC data set
abstract's list of file contents names the TOA, 70, 200 and 500 hPa
levels and the surface and does not name the 850 hPa
level.[^syn-dqs][^asdc-guide] Each computed flux exists in several
sky conditions (all-sky, clear-sky, pristine, meaning clear-sky
without aerosols, and total-sky without aerosols) and in two forms,
the initial untuned computation and the constrained tuned one, with
the adjusted radiative transfer input parameters carried
alongside.[^asdc-guide][^syn-dqs] The observed TOA fluxes are provided
for clear-sky and all-sky in the longwave, shortwave and window
bands.[^syn-dqs] Cloud properties are stratified into four pressure
layers and are diurnally complete, and the aerosols are the MATCH
assimilated optical thickness together with the MODIS retrievals; the
auxiliary fields are the assimilation's skin temperature, precipitable
water, column ozone and surface type.[^syn-dqs][^ceres-data-page]
Geostationary coverage is between 60 degrees south and 60 degrees
north, and no geostationary data is used
poleward.[^syn-dqs][^syn-dqs-toa] Which clear-sky convention each of
these fields carries is the subject of
[ceres-clear-sky-conventions](../conventions/ceres-clear-sky-conventions.md).

**Access and identifiers.** The CERES visualization, ordering and
subsetting tool is the service the summary and the CMR record both
name for the product, at a SYN1deg selection page the ordering tool
labels Edition4.2; the CMR record also links Earthdata Search and a
CMR virtual directory, and the ASDC collection and project pages
redirect to the Earthdata catalog.[^syn-dqs][^ceres-data-page][^cmr-syn-month][^asdc-catalog]
CMR carries four Edition4B collections on 2026-09-19, Month, Day,
MHour and 1Hour, all beginning 2000-03-01 with no end date and marked
ACTIVE, and no SYN1deg-3Hour collection, although the summary and the
data set abstract both describe a three-hourly
product.[^cmr-syn-family][^syn-dqs][^asdc-guide] The platforms on the
monthly record are Terra (CERES-FM1, CERES-FM2 and MODIS), Aqua
(CERES-FM3, CERES-FM4 and MODIS), NOAA-20 (CERES-FM6 and VIIRS) and
the geostationary imaging radiometers.[^cmr-syn-month] Each Edition4B
DOI resolves to its own collection's catalog page; the Terra+Aqua and
Terra+NPP DOIs printed in the summary's attribution section return 404
at doi.org, so a citation copied from the summary does not
resolve.[^doi-syn][^syn-dqs] Two boilerplate defects sit in the
monthly CMR record read that day: its abstract names the product
Edition4A and states a three-hourly temporal resolution, both of which
belong to sibling collections rather than to the monthly Edition4B
one.[^cmr-syn-month]

## Uncertainty

- **No uncertainty field is named in the parameter list.** The
  ordering page's SYN1deg parameter groups are fluxes, clouds,
  aerosols and auxiliary assimilation fields, with no per-region
  uncertainty; the numbers below come from the two accuracy and
  validation summaries.[^ceres-data-page][^syn-dqs-toa][^syn-dqs-surface]
- **Observed TOA fluxes, regional monthly.** For the all-sky
  shortwave flux the summary combines a CERES calibration term of
  1 W m-2 (one standard deviation), a radiance-to-flux conversion term
  of 1 W m-2 and a diurnal correction term of 3.5 W m-2 into
  3.8 W m-2; for the all-sky longwave flux the three terms are 1.8,
  0.75 and 0.6 W m-2, combining to 2.0 W m-2. The daily regional
  all-sky shortwave diurnal uncertainty is 8 W m-2, and the daily and
  hourly regional all-sky longwave diurnal uncertainties are 1.5 and
  2.81 W m-2. The summary notes that the diurnal correction terms,
  derived against GERB observations, may be
  overestimated.[^syn-dqs-toa]
- **Computed surface fluxes.** The surface summary states that the
  uncertainty in monthly mean Edition4A SYN1deg computed surface
  fluxes is generally the same as in monthly mean Edition4.0
  EBAF-Surface fluxes, and gives the EBAF-Surface table as the
  estimate: for ocean plus land, downward longwave 21 W m-2 hourly
  gridded, 7 monthly gridded, 6 monthly zonal, 5 monthly global and
  5 annual global; downward shortwave 43 hourly gridded, 13 monthly
  gridded, 7 monthly zonal, 6 monthly global and 4 annual global;
  upward longwave 15 monthly gridded and 3 monthly global; upward
  shortwave 11 monthly gridded and 3 monthly global. Polar monthly
  gridded values are larger, for example 12 W m-2 for Arctic and
  Antarctic downward longwave and 21 W m-2 for Antarctic downward
  shortwave.[^syn-dqs-surface] These are model output uncertainties,
  not radiometric ones (the gotcha
  [syn1deg-surface-fluxes-are-modelled-not-measured](../gotchas/syn1deg-surface-fluxes-are-modelled-not-measured.md)).
- **Validation against surface sites.** The comparisons in the
  surface summary are run on EBAF-Surface fluxes, with the statement
  that the root-mean-square differences of monthly mean SYN1deg fluxes
  are similar. Against 85 sites the mean differences of monthly one
  degree downward fluxes are 1.98 W m-2 shortwave (standard deviation
  12.64) and 0.08 W m-2 longwave (9.21); against ocean buoys 4.67
  (10.65) and 1.19 (4.84); over the Greenland Summit site the downward
  shortwave is biased low by 4 W m-2 and the downward longwave high by
  11 W m-2, attributed to a positive cloud fraction bias over high
  elevation. Buoys in the high-dust tropical Atlantic, excluded from
  those statistics, show monthly downward shortwave biases that can
  exceed minus 40 W m-2.[^syn-dqs-surface]
- **The global net imbalance is unadjusted.** The observed global
  mean net TOA flux is not constrained to an ocean heating estimate,
  and the summary gives the Edition4A imbalance as about plus
  4.5 W m-2 against an expected 0.71 W m-2, directing users who need
  balanced fluxes to EBAF.[^syn-dqs]
- **Known artifacts the summaries name.** Geostationary artifacts
  remain in the surface and in-atmosphere irradiances, and a change of
  mean cloud properties is expected wherever a geostationary domain is
  crossed in time or space; the adjusted (tuned) shortwave and
  longwave fluxes contain errors from code bugs and the summary
  advises against using them, while the initial fluxes are affected by
  geostationary cloud artifacts; cloud base heights from the newer
  geostationary imagers are higher than from the older ones, which
  puts a decreasing trend in the surface net longwave anomaly series;
  Terra water vapor channel degradation from about 2008 puts a
  downward trend in polar downward longwave anomalies; only Aqua
  aerosol optical thicknesses were used from July through December
  2004, making the global mean 0.006 to 0.009 smaller than the Terra
  plus Aqua value and affecting computed clear-sky fluxes; a daily
  total solar irradiance scaling glitch biased global averaged daily
  and monthly fluxes about 0.2 W m-2 high during August 2019 and May
  through July 2020, out of a twenty year mean of 339.88 W m-2; and
  the Aqua outage of August 16 to September 3, 2020 was filled from
  NOAA-20 through August 31, with September 1 to 3 not
  filled.[^syn-dqs][^syn-dqs-surface]

## Known issues

- [syn1deg-surface-fluxes-are-modelled-not-measured](../gotchas/syn1deg-surface-fluxes-are-modelled-not-measured.md):
  the surface and in-atmosphere fluxes are radiative transfer output,
  and in this product they are not adjusted to the observed TOA the
  way the energy balanced product's are.
- [syn1deg-refuses-long-term-trend-use](../gotchas/syn1deg-refuses-long-term-trend-use.md):
  the product's own documentation refuses long-term trend use and
  states that the product is not of climate quality.
- [syn1deg-geostationary-artifacts](../gotchas/syn1deg-geostationary-artifacts.md):
  artifacts from the geostationary inputs appear in the surface and
  in-atmosphere irradiances, at domain boundaries in space and at
  satellite changes in time.
- [ebaf-versus-syn1deg-versus-ssf](../gotchas/ebaf-versus-syn1deg-versus-ssf.md):
  which of EBAF, SYN1deg and SSF answers which question.
- [ceres-clear-sky-conventions](../conventions/ceres-clear-sky-conventions.md):
  the clear-sky conventions the radiation products carry, and which
  one each field uses.

[^syn-dqs]: CERES_SYN1deg_Ed4A Data Quality Summary, version 1, 5/8/2025
[^syn-dqs-toa]: CERES SYN1deg Edition4A observed TOA flux accuracy and validation, 4/8/2021
[^syn-dqs-surface]: CERES SYN1deg Edition4A computed flux accuracy and validation, 4/8/2021
[^ceres-data-page]: CERES data products page, SYN1deg entry
[^ceres-docs-page]: CERES documentation page, data quality summary table
[^asdc-guide]: ASDC CERES SYN1deg data set abstract
[^asdc-catalog]: ASDC collection page, CER_SYN1deg-Month Edition4B
[^cmr-syn-month]: CMR collection record C3880454295-LARC_CLOUD
[^cmr-syn-family]: CMR short name pattern search for CER_SYN1deg collections
[^doi-syn]: DOI resolution checks, 2026-09-19
[^ebaf-dqs]: CERES_EBAF_Ed4.2 and Ed4.2.1 Data Quality Summary, version 8, 9/10/2026
[^rutan-2015]: Rutan and others, 2015, Journal of Atmospheric and Oceanic Technology, doi:10.1175/JTECH-D-14-00165.1
[^doelling-2013]: Doelling and others, 2013, Journal of Atmospheric and Oceanic Technology, doi:10.1175/JTECH-D-12-00136.1
[^doelling-2016]: Doelling and others, 2016, Journal of Atmospheric and Oceanic Technology, doi:10.1175/JTECH-D-15-0147.1
