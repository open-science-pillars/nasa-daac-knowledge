---
type: dataset-gotcha
spheres: [atmosphere]
title: "The SYN1deg documentation refuses long-term trend use in its own words and states that the product is not of climate quality, and the artifacts it names have the shape of the trends a user would want to report"
description: "The Edition4A data quality summary states that SYN1deg should not be used to infer long-term trends of clouds or fluxes and is not of climate quality, repeats the point in its computed flux cautions, and sends trend users to EBAF-TOA and EBAF-Surface, which remove the known geostationary artifacts, and cloud trend users to SSF1deg, which is of climate quality but does not cover the diurnal cycle. The refusal is not generic caution: the summaries name a decreasing surface net longwave anomaly trend caused by newer geostationary imagers retrieving higher cloud bases, and a decreasing polar downward longwave trend caused by Terra water vapor channel degradation. A trend fitted to this product's anomalies is a trend the documentation has already attributed to the instruments."
tags: [ceres, syn1deg, trends, climate-quality, anomalies, geostationary, ebaf, ssf1deg, product-choice]
generated: { by: knowledge-seeder/claude, at: 2026-09-19T05:30:00Z }
severity: high
dataset: ../datasets/ceres-syn1deg.md
eval_case: syn1deg-refuses-long-term-trend-use
status: draft
stale_after: 2027-03-19
sources:
  - id: syn-dqs
    resource: https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_SYN1deg_Ed4A_DQS_V1.pdf
    title: "CERES_SYN1deg_Ed4A Data Quality Summary, version 1, updated 5/8/2025, read in full on 2026-09-19: the statement in the nature of the products section that SYN1deg should not be used to infer long-term trends of clouds or fluxes and is not of climate quality, the advice to use EBAF-TOA and EBAF-Surface for long-term flux variability and trending and SSF1deg for regional cloud trends, the input change caution and its input data sources link, the computed flux caution advising against trend studies, the polar downward longwave trend, the geostationary cloud base height effect on the surface longwave anomaly series, the calendar year deseasonalization caution and the note to users describing the Edition4B record change in April 2022"
  - id: syn-dqs-surface
    resource: https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_SYN1deg_Surface_Ed4A.pdf
    title: "CERES Terra/Aqua Edition4A SYN1deg Computed Fluxes, Accuracy and Validation, 4/8/2021, read in full on 2026-09-19: the polar night longwave section attributing the downward trend in polar downward and net longwave anomalies to Terra water vapor channel degradation from about 2008, and the surface longwave irradiance anomaly section attributing a significant downward trend in the global net longwave anomaly series to higher cloud bases from the newer geostationary imagers"
  - id: syn-dqs-toa
    resource: https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_SYN1deg_TOA_Ed4A.pdf
    title: "CERES Terra/Aqua Edition4A SYN1deg Observed TOA Fluxes, Accuracy and Validation, 4/8/2021, read in full on 2026-09-19: the sixteen geostationary satellites over the seventeen year record, the regional trend comparisons of Edition4A and Edition3A against SSF1deg and the statement that a geostationary-artifact-free product would show a near zero SYN1deg minus SSF1deg trend difference"
  - id: ebaf-dqs
    resource: https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_EBAF_Ed4.2_DQS.pdf
    title: "CERES_EBAF_Ed4.2 and Ed4.2.1 Data Quality Summary, version 8, released 9/10/2026, read 2026-09-19: the regional climatology adjustments over five year overlap periods applied to the TOA observed fluxes, imager cloud properties and computed surface fluxes to facilitate trend analysis across the Terra-only, Terra and Aqua, and NOAA-20-only records"
  - id: cmr-syn-family
    resource: https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=CER_SYN1deg*&options%5Bshort_name%5D%5Bpattern%5D=true&page_size=60
    title: "CMR short name pattern search for CER_SYN1deg collections, run 2026-09-19: the four Edition4B collections, each beginning 2000-03-01 with no end date, which is the unbroken span a trend user reads off the catalog"
  - id: ebaf-versus
    resource: ../gotchas/ebaf-versus-syn1deg-versus-ssf.md
    title: "This bundle's gotcha on the division of labour between EBAF, SYN1deg and SSF, which owns the product-choice argument this trap sits inside"
  - id: dataset
    resource: ../datasets/ceres-syn1deg.md
    title: "This bundle's SYN1deg dataset concept, which lists this trap among the known issues"
---

# SYN1deg refuses long-term trend use

**Mechanism.** The refusal is written twice in the product's own
summary. In the section describing the nature of the products: the
SYN1deg Edition4A "should not be used to infer long-term trends of
clouds or fluxes and are not of climate quality", with the advice that
users turn to EBAF-TOA and EBAF-Surface to determine the long-term
flux natural variability and temporal trending, and that the Terra or
Aqua SSF1deg MODIS-retrieved cloud properties are of climate quality
for regional cloud trends although they do not encompass the entire
diurnal cycle.[^syn-dqs] And again in the computed flux cautions,
where the sentence on the code bugs in the adjusted fluxes is followed
by the statement that users are advised not to use SYN1deg Edition4A
fluxes for trend studies.[^syn-dqs] The reason is the constellation
the product is built on. Sixteen geostationary satellites entered the
record over its first seventeen years, and the summary states that
whenever a geostationary domain is crossed, in time or in space, a
slight change in mean cloud property values is expected, and that when
a satellite at a longitude position is upgraded to a newer generation
imager the discontinuity in fluxes at that temporal boundary is more
pronounced in Edition4A than it was in
Edition3A.[^syn-dqs-toa][^syn-dqs] Other inputs move too: the summary
notes that key inputs changed at various times during the record and
that such changes, if large enough, may introduce spurious unphysical
jumps, pointing at the project's input data sources timeline rather
than at a correction.[^syn-dqs] The energy balanced products are
different in exactly this respect: their summary describes regional
climatology adjustments computed over five year overlap periods and
applied to the TOA observed fluxes, the imager cloud properties and
the computed surface fluxes in order to facilitate trend analysis
across the satellite records, and the SYN1deg summary states that
EBAF-TOA and EBAF-Surface use the SYN1deg fluxes and clouds as inputs
but remove all known geostationary artifacts.[^ebaf-dqs][^syn-dqs]
Two named artifacts show what the refusal is protecting against. As
the newer geostationary imagers replaced the older ones, their higher
retrieved cloud bases lowered the computed nighttime downward longwave
irradiance, and the surface summary reports a significant downward
trend in the global surface net longwave anomaly series as a
consequence; and the degradation of the Terra water vapor channel
from about 2008 puts a downward trend in the polar downward longwave
and net longwave anomaly series.[^syn-dqs-surface][^syn-dqs] The
catalog gives no hint of any of this: the four Edition4B collections
each begin 2000-03-01 and carry no end date, which reads as one
continuous quarter-century series.[^cmr-syn-family]

**Wrong-result mode.** A trend or an anomaly series fitted to SYN1deg
fluxes or cloud properties, regionally or globally, returns a number
that the documentation has already attributed to the instruments, and
the two named cases have the sign and the location a physical result
would have: a decreasing surface net longwave trend that reads as a
change in the greenhouse effect, and a decreasing polar downward
longwave trend that reads as an Arctic or Antarctic signal.[^syn-dqs-surface]
A diurnal cycle compared between the early and the late record mixes
the change in the cycle with the change in the geostationary
constellation that samples it.[^syn-dqs][^syn-dqs-toa] A monthly
deseasonalization built on the 365 day calendar year introduces
variability of its own into CERES anomalies, which the summary flags
separately.[^syn-dqs] A record assembled across the data sets, Terra
plus Aqua Edition4A before April 2022 and NOAA-20 with the MERRA-2
atmosphere in Edition4B after it, crosses a satellite change and a
reanalysis change at one point in time with no climatology adjustment
in the product to absorb it.[^syn-dqs] And because the product is the
one the project names for diurnal and process work, the trap is
reached from a legitimate starting point: a user who came for the
hourly fluxes has the whole record in hand and nothing in the files
marks where the trend question stops being answerable.[^syn-dqs][^ebaf-versus]

**Correct approach.** A long-term flux trend or a flux variability
statement has its product named by the summary, EBAF-TOA or
EBAF-Surface, whose climatology adjustments across the satellite
records exist for that purpose, and a regional cloud property trend
has SSF1deg, with the absence of the diurnal cycle stated as the
price.[^syn-dqs][^ebaf-dqs] Where SYN1deg is the product that carries
the quantity at all, the hourly and in-atmosphere fields it alone
holds, a statement about change over time in it is voiced as what the
summary says it is, not of climate quality, with the geostationary
transitions and the input changes named as the alternative
explanation; the summary sanctions no window over which a trend from
this product stands, and offers the other products in place of
one.[^syn-dqs] The project's own use of SYN1deg trends is a
diagnostic of the product rather than a geophysical result: the TOA
validation document compares Edition4A and Edition3A regional trends
against SSF1deg precisely to expose the remaining artifacts, and
states that a product free of geostationary artifacts would show a
near zero difference there.[^syn-dqs-toa] The distinction between the
questions the product answers and the questions it refuses is the
subject of
[ebaf-versus-syn1deg-versus-ssf](../gotchas/ebaf-versus-syn1deg-versus-ssf.md),
and what is new here is that the refusal is the product's own and is
written about trends specifically.[^ebaf-versus]

**Verification.** The Edition4A summary carries the refusal in the
nature of the products section and again in the computed flux
cautions, names EBAF-TOA, EBAF-Surface and SSF1deg as the
alternatives, states the expected cloud property change at
geostationary domain crossings and the more pronounced discontinuity
at imager upgrades, flags the input changes and the calendar year
deseasonalization, and describes the April 2022 record change in its
note to users.[^syn-dqs] The surface validation document attributes
the polar longwave anomaly trend to the Terra water vapor channel
degradation and the global surface net longwave anomaly trend to the
newer geostationary cloud base heights.[^syn-dqs-surface] The TOA
validation document counts the geostationary satellites in the record
and uses the SYN1deg minus SSF1deg trend difference as the artifact
test.[^syn-dqs-toa] The EBAF summary describes the climatology
adjustments that make trend analysis its purpose.[^ebaf-dqs] The CMR
search of 2026-09-19 shows the four collections with no end
date.[^cmr-syn-family] The dataset concept lists this trap among the
product's known issues.[^dataset]

[^syn-dqs]: CERES_SYN1deg_Ed4A Data Quality Summary, version 1, 5/8/2025
[^syn-dqs-surface]: CERES SYN1deg Edition4A computed flux accuracy and validation, 4/8/2021
[^syn-dqs-toa]: CERES SYN1deg Edition4A observed TOA flux accuracy and validation, 4/8/2021
[^ebaf-dqs]: CERES_EBAF_Ed4.2 and Ed4.2.1 Data Quality Summary, version 8, 9/10/2026
[^cmr-syn-family]: CMR short name pattern search for CER_SYN1deg collections, 2026-09-19
[^ebaf-versus]: This bundle's EBAF versus SYN1deg versus SSF gotcha
[^dataset]: This bundle's SYN1deg dataset concept
