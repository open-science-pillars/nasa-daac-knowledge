---
type: dataset-gotcha
spheres: [atmosphere, hydrosphere]
title: "The EBAF net TOA flux is anchored to an in situ ocean heating estimate over a stated decade, so its global mean imbalance is not an independent check of ocean heat content"
description: "The unadjusted CERES net TOA flux carries an imbalance of several watts per square metre that calibration cannot resolve, and EBAF removes it with a one-time adjustment to the shortwave and longwave fluxes that sets the July 2005 through June 2015 global mean net flux to the in situ Earth heat uptake, 0.71 W m-2, most of it Argo ocean heat content change. A comparison of EBAF's decade-mean imbalance with an ocean heat content series therefore confirms the input, and the anchor's value and period have changed between editions, so a comparison also names which edition set it. The variations about the mean are what the ocean data did not set."
tags: [ceres, ebaf, energy-imbalance, net-toa-flux, ocean-heat-content, argo, anchoring, edition]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:30:00Z }
severity: high
dataset: ../datasets/ceres-ebaf-ed4-2.md
eval_case: ebaf-imbalance-anchored-to-ocean-heating
status: draft
stale_after: 2027-03-14
sources:
  - id: dqs
    resource: https://ceres.larc.nasa.gov/documents/DQ_summaries/Versioned/CERES_EBAF_Ed4.2_DQS_V7.pdf
    title: "CERES_EBAF_Ed4.2 and Ed4.2.1 Data Quality Summary, version 7, 2026-07-01, the pinned copy (byte-identical to the file the unversioned link served on 2026-09-14; the documentation page lists a version 8 posted 2026-09-09, which was served at neither URL that day and was not read), read 2026-09-14: the SYN1deg Edition 4 net imbalance of about 4.3 W m-2 against the expected ocean heating rate of about 0.71 W m-2, the constrainment within uncertainty, and Edition 4.2 balanced with the Edition 4.1 ocean heat storage value over July 2005 through June 2015"
  - id: dqs-ed4-0
    resource: https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_EBAF_Ed4.0_DQS.pdf
    title: "CERES_EBAF_Ed4.0 Data Quality Summary, 2018-01-12, read 2026-09-14: the anchoring paragraph with the composition of the 0.71 plus or minus 0.10 W m-2 heat uptake (Argo to 1800 m, below 2000 m, ice and atmosphere), and the Edition 4.0 against 2.8 global mean table"
  - id: dqs-ed2-8
    resource: https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_EBAF_Ed2.8_DQS.pdf
    title: "CERES_EBAF_Ed2.8 Data Quality Summary, 2014-03-19, read 2026-09-14: the earlier anchor, 0.58 plus or minus 0.38 W m-2 over July 2005 through June 2010, and its composition"
  - id: asdc-guide
    resource: https://asdc.larc.nasa.gov/documents/ceres/guide/cer_ebaf-toa.pdf
    title: "ASDC EBAF-TOA data set abstract, read 2026-09-14: the ocean heat storage term by edition (0.9 W m-2 for Terra Edition 1A, 0.58 W m-2 from Edition 2.6r) and the abstract's own quoted value of about 0.58 W m-2"
  - id: asdc-catalog-ebaf
    resource: https://asdc.larc.nasa.gov/project/CERES/CERES_EBAF_Edition4.2.1
    title: "ASDC collection page for CERES_EBAF Edition4.2.1, read 2026-09-14: the abstract's statement that the TOA net flux is constrained to the ocean heat storage"
  - id: loeb-2018
    resource: https://doi.org/10.1175/JCLI-D-17-0208.1
    title: "Loeb and others, 2018, CERES EBAF TOA Edition-4.0 Data Product, Journal of Climate 31, 895 to 918: the one-time adjustment to shortwave and longwave TOA fluxes so that the July 2005 through June 2015 global mean net flux equals the in situ 0.71 W m-2 (record and abstract read on the Crossref registry 2026-09-14; the journal page was not read)"
  - id: johnson-2016
    resource: https://doi.org/10.1038/nclimate3043
    title: "Johnson, Lyman and Loeb, 2016, Improving estimates of Earth's energy imbalance, Nature Climate Change 6, 639 to 640: the in situ heat uptake estimate the Edition 4 anchor cites (record verified on the Crossref registry 2026-09-14; the registry carries no abstract and the journal page was not read; the value is taken from the data quality summaries, which cite it)"
  - id: dataset
    resource: ../datasets/ceres-ebaf-ed4-2.md
    title: "This bundle's EBAF dataset concept, which lists this trap among the known issues and carries the edition history"
---

# The EBAF imbalance is anchored to ocean heating

**Mechanism.** The CERES instruments' calibration and the flux
algorithms leave a sizeable imbalance in the global mean net TOA
radiation: with the current calibration the SYN1deg Edition 4 net
imbalance is about 4.3 W m-2, against an expected observed ocean
heating rate of about 0.71 W m-2.[^dqs] EBAF removes the inconsistency
with an objective constrainment that adjusts the shortwave and
longwave TOA fluxes within their ranges of uncertainty, as a one-time
adjustment, so that the global mean net TOA flux over July 2005
through June 2015 equals the in situ value of 0.71 W m-2.[^dqs][^loeb-2018]
That value is an estimate of the Earth's heat uptake assembled from
ocean and other in situ data: 0.61 plus or minus 0.09 W m-2 from a
weighted linear fit to Argo ocean heat content anomalies to 1800 m,
0.07 plus or minus 0.04 W m-2 from ocean heat storage below 2000 m
over 1981 through 2010, and 0.03 plus or minus 0.01 W m-2 from ice
warming and melt and atmospheric and lithospheric warming, for a
total of 0.71 plus or minus 0.10 W m-2 at the 95 percent level, with
the uncertainty covering XBT corrections and Argo sampling.[^dqs-ed4-0][^johnson-2016]
The anchor has moved with the editions: Terra Edition 1A used an
ocean heat storage term of 0.9 W m-2, Edition 2.6r through 2.8 used
0.58 plus or minus 0.38 W m-2 over July 2005 through June 2010, and
Edition 4.0 onward uses 0.71 W m-2 over July 2005 through June 2015;
Edition 4.2 was balanced with the same value and the same decade as
Edition 4.1, chosen to avoid the single-satellite periods, and the
Edition 4.2 minus 4.1 global net record mean differs by less than
0.02 W m-2.[^asdc-guide][^dqs-ed2-8][^dqs-ed4-0][^dqs] The ASDC data
set abstract for EBAF-TOA still quotes the older value, about
0.58 W m-2, as the heat storage the product is constrained to.[^asdc-guide]

**Wrong-result mode.** A global mean net TOA flux formed from EBAF
over the anchor decade, with the product's geodetic weights, returns
0.71 W m-2 by construction. Reported as satellite confirmation of the
ocean heat content trend, or as an observed energy imbalance to be
compared with an Argo or ECCO heat content change over that decade,
it compares the ocean data with itself: the agreement is the
constraint, and a disagreement over the same decade is a difference
between two ocean heating estimates, not a radiation-versus-ocean
test.[^loeb-2018][^dqs-ed4-0] Over any other window the EBAF global
mean net still carries the anchor's offset, because the adjustment is
made once to the entire record, so an "EBAF imbalance" for, say, 2015
through 2024 is the anchor plus the change in the unadjusted net flux
since the anchor decade, and a comparison with ocean heat content over that
window inherits the anchor's 0.10 W m-2 uncertainty and its edition.
A number taken from a page rather than from the summary can be the
wrong edition's anchor (0.58 on the ASDC abstract, 0.71 in the
Edition 4 summaries), and a comparison of an Edition 2.8 imbalance
with an Edition 4 one reads a 0.13 W m-2 change of anchor as a change
in the Earth.[^asdc-guide][^dqs-ed4-0] Nothing in the file marks the
anchoring; the net flux variable looks like an observation.

**Correct approach.** What the ocean data did not set is the
variation: the adjustment is made once to the entire record, and the
Edition 4.0 summary draws the consequence itself, that the time
dependence of the EBAF TOA fluxes is tied to the CERES instrument
radiometric stability; so the interannual anomalies and the trend of
the EBAF global mean net flux come from the radiometry, and a
comparison of their change with a change in ocean heat content over
the same window is the independent test the product supports (the
uncertainty of an anomaly is the radiometric one, and the product's
own transition analysis puts the random error of global monthly
anomalies after the satellite transitions below 0.15 W m-2, in the
dataset concept).[^dqs-ed4-0][^loeb-2018][^dqs][^dataset] An energy imbalance
statement from EBAF names the edition, the anchor value and its decade
(0.71 W m-2 over July 2005 through June 2015 for Edition 4.0 through
4.2.1) and says that the mean is set to that value; it quotes the
ocean-side number, its depth range and its period beside it rather than
as a check. The ocean heat content change itself, for the ECCO state
estimate, is the podaac bundle's recipe
knowledge/podaac/recipes/ecco-ocean-heat-content.md (volume-weighted on
the native grid, changes rather than absolutes; the bundles are
separate installs, so it is named by bundle path),
and a comparison uses its change over the chosen window against the
EBAF net flux anomaly integrated over the same window, never the EBAF
decade mean.

**Verification.** The Edition 4.2 summary states the imbalance,
the constrainment and the reuse of the Edition 4.1 anchor and
decade;[^dqs] the Edition 4.0 summary gives the anchor's value,
period and composition and cites Johnson and others 2016 for
it;[^dqs-ed4-0][^johnson-2016] the Edition 2.8 summary gives the
earlier anchor and period;[^dqs-ed2-8] the ASDC data set abstract
lists the 0.9 and 0.58 W m-2 terms by edition and quotes 0.58 in its
description;[^asdc-guide] the ASDC collection page states that the
TOA net flux is constrained to the ocean heat storage.[^asdc-catalog-ebaf]
Loeb and others 2018 was verified against the Crossref registry on
2026-09-14 (title, authors, journal, volume, pages, year) and its
abstract read there: a one-time adjustment to shortwave and longwave
TOA fluxes so that the global mean net TOA flux for July 2005 through
June 2015 is consistent with the in situ value of 0.71 W m-2; the
journal page itself was not read.[^loeb-2018] Johnson and others 2016
was verified on the registry the same day (title, authors, journal,
volume, pages, year), which carries no abstract for it; its number is
taken from the summaries that cite it.[^johnson-2016] The dataset
concept lists this trap among the product's known issues.[^dataset]

[^dqs]: CERES_EBAF_Ed4.2 and Ed4.2.1 Data Quality Summary, version 7, 2026-07-01
[^dqs-ed4-0]: CERES_EBAF_Ed4.0 Data Quality Summary, 2018-01-12
[^dqs-ed2-8]: CERES_EBAF_Ed2.8 Data Quality Summary, 2014-03-19
[^asdc-guide]: ASDC EBAF-TOA data set abstract
[^asdc-catalog-ebaf]: ASDC collection page, CERES_EBAF Edition4.2.1
[^loeb-2018]: Loeb and others, 2018, Journal of Climate, doi:10.1175/JCLI-D-17-0208.1
[^johnson-2016]: Johnson, Lyman and Loeb, 2016, Nature Climate Change, doi:10.1038/nclimate3043
[^dataset]: This bundle's EBAF dataset concept
