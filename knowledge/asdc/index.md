---
okf_version: "0.2"
---

# asdc bundle (ASDC radiation budget)

The ASDC knowledge bundle: the Atmospheric Science Data Center's
radiation budget and cloud products (CERES EBAF first), as reviewable
concepts with sources, statuses and steward sign-off. OKF v0.2
conformant (okf_version: "0.2"; the vendored spec text lives in
marketplace docs/upstream). Every concept is a draft until the steward
promotes it after review, and a confirmation from the ASDC or the CERES
team is invited on each and never required. The ocean heat content a
radiation imbalance is compared against lives in the podaac bundle's
ECCO recipes and in the ocean-science plugin's Argo computation; a
concept here names them where it depends on them, and the attested
energy budget reads the Argo receipt.

What this bundle claims, for the people who know the data: [DIGEST.md](DIGEST.md).

## datasets

- [CERES EBAF Edition 4.2 and 4.2.1: energy balanced and filled top-of-atmosphere and surface radiative fluxes](datasets/ceres-ebaf-ed4-2.md), status: stable

## gotchas

- [The EBAF net TOA flux is anchored to an in situ ocean heating estimate over a stated decade, so its global mean imbalance is not an independent check of ocean heat content](gotchas/ebaf-imbalance-anchored-to-ocean-heating.md), severity high, status: stable
- [EBAF carries two clear-sky definitions, the cloud-free-area flux and the total-region flux, and the cloud radiative effect changed definition at Edition 4.1, so a cloud radiative effect names its definition and edition](gotchas/ebaf-clear-sky-definitions.md), severity medium, status: stable
- [EBAF surface fluxes are radiative transfer output from assimilated and retrieved inputs, adjusted to the observed TOA, so their uncertainty is larger than the TOA fluxes' and shaped by the inputs rather than by the radiometer](gotchas/ebaf-surface-fluxes-are-modelled.md), severity medium, status: stable
- [EBAF, SYN1deg and SSF answer different questions: EBAF is the balanced monthly climate record, SYN1deg carries the hourly diurnal cycle and the in-atmosphere fluxes, SSF carries the instantaneous footprints, and a diurnal or process study on EBAF misses what SYN1deg carries](gotchas/ebaf-versus-syn1deg-versus-ssf.md), severity medium, status: stable
- [The EBAF climatology base period, the edition and the release date fix the anomaly baseline: the product's climatology is July 2005 through June 2015, and files of different editions or releases differ in the fields themselves](gotchas/ebaf-climatology-baseline.md), severity low, status: stable

## recipes

- [Closing the Earth's energy budget: EBAF net TOA flux against Argo ocean heat content plus the published deep and non-ocean terms](recipes/energy-budget.md), status: stable

## computations (OKF v0.2 section 10)

- [Energy budget closure: CERES EBAF net top-of-atmosphere flux against the Argo ocean heat content change (attested)](computations/energy-budget.md), status: stable (a synthetic fixture with a planted level, trend and closure proves the chain; the real-data anchor is the stamped data root under references/retrieval/energy-budget-root, run for 2006 through 2020; refuses a window the radiation record does not cover or an Argo receipt over another window)
