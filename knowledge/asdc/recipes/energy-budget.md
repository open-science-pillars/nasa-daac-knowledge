---
type: recipe
spheres: [atmosphere, hydrosphere]
title: "Closing the Earth's energy budget: EBAF net TOA flux against Argo ocean heat content plus the published deep and non-ocean terms"
description: "The terms of the energy budget over a window, which product supplies each, which gotcha holds each term's trap (the EBAF anchor to in situ heating over a stated decade; the geodetic weighting the anchor is defined on; the Argo product's depth floor and mapped domain), the rule that the Argo receipt's window is the window, and how the residual is read: the absolute comparison as anchored, the anomaly trend as the independent one."
tags: [ceres, ebaf, energy-imbalance, net-toa-flux, ocean-heat-content, argo, earth-heat-inventory, anchoring, recipe]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T18:30:00Z }
inputs:
  - dataset: ../datasets/ceres-ebaf-ed4-2.md
  - toa_net: "the product's own global mean net TOA flux per calendar month (gtoa_net_all_mon, the geodetic mean the anchor is defined on) with the cos-latitude mean of the one degree grid beside it, from the CERES EBAF Edition 4.2.1 file, the edition and release date stated"
  - ohc_0_2000: "the 0 to 2000 dbar ocean heat content rate over the same window read from the ocean-science plugin's Argo computation receipt (knowledge/computations/argo-ohc.md there; the executor references/computations/argo_ohc.py), the receipt's window equal to the budget's window, its rate over the product's mapped domain and never scaled"
  - deep_ocean: "the published rate below 2000 m, 0.06 plus or minus 0.03 W m-2 over 1992 to 2020, with its source; the Argo receipt states the omission"
  - non_ocean: "land, cryosphere and atmosphere over 2006 to 2020 as published rates with their sources, 0.0822 plus or minus 0.0174 W m-2 together"
  - method: "the attested computation ../computations/energy-budget.md: four rate terms per unit Earth surface, the residual, the combined uncertainty, the verdict, the energy over the window, the anomaly trend against the published one, the anchoring as receipt facts"
expected:
  - quantity: "the identity"
    statement: "the window mean of the net TOA flux equals the ocean heat content rate plus the deep ocean and non-ocean rates within uncertainties; the residual is compared with the four term uncertainties in quadrature, the anchor's in situ uncertainty inside the radiation term"
  - quantity: "numeric anchor"
    statement: "2006-01 through 2020-12 on the stamped data root (180 of 180 months): toa_net +0.8746, ocean side 0.7427 (Argo 0 to 2000 dbar +0.6005, deep 0.06, non-ocean 0.0822) W m-2, residual +0.1319 against a bar of 0.1894, closed within uncertainty; anomaly trend +0.3706 W m-2 per decade with a 95 percent interval of [+0.0762, +0.6649] against the published 0.50 plus or minus 0.47; recorded with its loader, its receipt and its stamp in ../computations/energy-budget.md"
  - quantity: "the published imbalance"
    statement: "the Earth heat inventory's 0.76 plus or minus 0.2 W m-2 for 2006 to 2020, which the run's radiation term sits 0.11 above and the run's ocean side 0.02 below"
expected_uncertainty:
  - quantity: "radiation term"
    statement: "the anchor's in situ uncertainty (0.10 W m-2 at the 95 percent level) in quadrature with the larger of the sampling half width of the window mean under a lag-1 autocorrelated residual and the formal error the per-month floor propagates; the product ships no uncertainty field, so the floor is measured on the series and the published random error of a monthly anomaly is quoted beside it"
  - quantity: "ocean term"
    statement: "the Argo receipt's own uncertainty on its trend, the larger of its sampling half width and its formal error, converted with the Earth's area; the domain understatement is a stated bias, never folded into the uncertainty"
  - quantity: "published terms"
    statement: "the uncertainties the sources state, carried as stated; the deep ocean over 1992 to 2020 and the non-ocean terms over 2006 to 2020 are rates over other periods than the window, a stated limit"
sources:
  - id: computation
    resource: ../computations/energy-budget.md
    title: "The attested computation this recipe walks: the terms, the bookkeeping, the anomaly comparison, the fixture, the refusal rule, the reference run"
  - id: dataset
    resource: ../datasets/ceres-ebaf-ed4-2.md
    title: "This bundle's EBAF dataset concept: the radiation term's product"
  - id: gotcha-anchor
    resource: ../gotchas/ebaf-imbalance-anchored-to-ocean-heating.md
    title: "This bundle's gotcha: the anchor, its decade, and why the anomaly is the independent comparison"
  - id: gotcha-baseline
    resource: ../gotchas/ebaf-climatology-baseline.md
    title: "This bundle's gotcha: the product's climatology base period is the anchor decade"
  - id: dqs
    resource: https://ceres.larc.nasa.gov/documents/DQ_summaries/Versioned/CERES_EBAF_Ed4.2_DQS_V7.pdf
    title: "CERES_EBAF_Ed4.2 and Ed4.2.1 Data Quality Summary, version 7, 2026-07-01, read 2026-09-15: the anchoring and the geodetic weighting of global means"
  - id: vs-2023
    resource: https://doi.org/10.5194/essd-15-1675-2023
    title: "von Schuckmann and others (2023), Heat stored in the Earth system 1960 to 2020: where does the energy go?, Earth System Science Data 15, 1675 to 1709 (read in full 2026-09-15): the layer rates, the deep ocean, the atmospheric gain, the inventory fractions and the 2006 to 2020 imbalance"
  - id: loeb-2021
    resource: https://doi.org/10.1029/2021GL093047
    title: "Loeb and others (2021), Satellite and Ocean Data Reveal Marked Increase in Earth's Heating Rate, Geophysical Research Letters 48 (the registry record and abstract, 2026-09-15): the published trend of the imbalance"
  - id: ohc-receipt
    resource: ../references/retrieval/energy-budget-root/ohc-2000-receipt.json
    title: "The Argo ocean heat content receipt in the data root, the ocean term's source"
status: draft
stale_after: 2027-03-15
---

# Closing the Earth's energy budget

**The terms.** The net radiation the Earth takes in at the top of the
atmosphere is the heat found in the Earth system: most of it in the
ocean, the rest in the land, the ice and the air.[^vs-2023] Each term
comes from one source, and each source carries a trap a concept in
this bundle or the ocean-science bundle names:

1. **Radiation: CERES EBAF.** The product's own global mean net TOA
   flux per month, the geodetic mean, since the product's anchor is
   defined on it: the shortwave and longwave fluxes were adjusted once
   so that the July 2005 through June 2015 mean equals an in situ heat
   uptake of 0.71 W m-2, so the window mean of the net flux is not
   independent of ocean heating over the months the window shares with
   that decade, and it carries the anchor's 0.10 W m-2
   uncertainty.[^dataset][^gotcha-anchor][^dqs] A cos-latitude mean
   of the one degree grid is a different number, 0.22 W m-2 higher
   over the record, because the net flux has a strong meridional
   gradient and the product's weights and solar division factor
   (4.0034) shift the balance; the loader writes both and the
   computation states the offset.[^dqs][^computation] The product's
   climatology base period is the same decade, so the anomaly is
   formed against the window's own mean.[^gotcha-baseline]
2. **Ocean: the Argo receipt.** The 0 to 2000 dbar rate over the
   window from the ocean-science plugin's attested Argo computation
   (knowledge/computations/argo-ohc.md in that bundle; the two are
   separate installs, so it is named by path), read from its receipt
   with its uncertainty and its stamp, never restated: the rate is
   over the Roemmich and Gilson product's mapped open-ocean domain
   and understates the global ocean by construction, and the product
   stops at 2000 dbar, so the deep ocean is a separate
   term.[^ohc-receipt]
3. **The rest, published.** The deep ocean below 2000 m (0.06 plus or
   minus 0.03 W m-2 over 1992 to 2020) and the land, cryosphere and
   atmosphere over 2006 to 2020 (0.0822 plus or minus 0.0174 W m-2
   together) from the Earth heat inventory, with their sources, never
   measured here.[^vs-2023]

**The window rule.** The Argo receipt's window must be the budget's
window: its rate is a whole-window quantity, and the computation
refuses a receipt over any other window rather than intersecting or
scaling it. A month with no radiation value is a hole dropped from
the mean and the fit, never interpolated.[^computation]

**How the residual is read.** The residual (radiation minus the sum of
the three ocean-side terms) is compared with the four term
uncertainties in quadrature. Inside it, the budget closes within
uncertainty, and the reading stops at the caveat: the agreement over
the months shared with the anchor decade is the in situ estimate
agreeing with an in situ estimate, and only the radiometric change
between the anchor decade and the window is independent
content.[^gotcha-anchor] Outside it, the first reading is the
bookkeeping: the weighting (a cos-latitude mean compared with an
anchor defined on the geodetic mean is 0.22 W m-2 off before any
physics), the edition and release date of the file, the Argo domain
and depth floor, and the periods of the published terms, before any
missing-physics conclusion is drawn.[^computation] The independent
comparison is the trend of the net flux anomaly against the published
satellite and in situ trend of the imbalance, 0.50 plus or minus 0.47
W m-2 per decade, in which the anchor cancels; the receipt states the
distance.[^loeb-2021]

**The attested form.** The computation walks these steps with the
anchoring, the weighting and the ocean input as receipt facts, four
terms, a residual and a verdict the attester recomputes; its
real-data run over 2006 through 2020 closes the budget within
uncertainty (residual +0.1319 W m-2 against a bar of 0.1894) with an
anomaly trend of +0.3706 W m-2 per decade, and is the anchor quoted
in the expectations above.[^computation]

**Provenance.** Every number quoted from this recipe names the
product edition and release date, the file read and its hash, the
weighting, the Argo receipt's run id, window and domain, the published
terms' periods and sources, the window and the months missing. The
data quality summary and the geodetic weights were read on
2026-09-15, the heat inventory paper in full the same day, every DOI
verified against the Crossref registry, and Loeb and others 2021
cited on its registry record and abstract, the journal page being
behind a bot check.[^dqs][^vs-2023][^loeb-2021]

[^computation]: computations/energy-budget.md
[^dataset]: datasets/ceres-ebaf-ed4-2.md
[^gotcha-anchor]: gotchas/ebaf-imbalance-anchored-to-ocean-heating.md
[^gotcha-baseline]: gotchas/ebaf-climatology-baseline.md
[^dqs]: CERES_EBAF_Ed4.2 and Ed4.2.1 Data Quality Summary, version 7, 2026-07-01
[^vs-2023]: von Schuckmann and others (2023), Earth System Science Data 15, doi:10.5194/essd-15-1675-2023
[^loeb-2021]: Loeb and others (2021), Geophysical Research Letters 48, doi:10.1029/2021GL093047
[^ohc-receipt]: references/retrieval/energy-budget-root/ohc-2000-receipt.json
