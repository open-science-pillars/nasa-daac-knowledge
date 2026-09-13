---
type: recipe
spheres: [hydrosphere, cryosphere]
title: "Closing the global mean sea level budget: altimetry against GRACE-FO mass plus Argo steric"
description: "The three terms of the sea level budget, which product supplies each, which gotcha or convention holds each term's trap (altimetry corrections and era dependence; the Argo deep-steric floor; mass with its GIA model, leakage, the inter-mission gap and the low-degree replacements), the matching-period rule at the month, and how the residual is read: correction consistency before missing physics."
tags: [sea-level, budget, closure, altimetry, nasa-ssh, grace, grace-fo, argo, steric, manometric, recipe]
generated: { by: knowledge-seeder/claude, at: 2026-09-13T21:00:00Z }
inputs:
  - dataset: ../datasets/nasa-ssh.md
  - dataset: ../datasets/grace-fo-mascons.md
  - altimetry: "the global mean of the NASA-SSH simple grids per calendar month, the dynamic atmospheric correction as the product applies it, the reference-mission era stated"
  - steric: "a gridded Argo steric height (Roemmich and Gilson, or a successor) integrated over its sampled depth range and averaged over the ocean, the depth floor stated; regionally, profiles through core's observations connector, a loader outside the gate"
  - mass: "the CRI-filtered mascon grids summed over the ocean mascons per the mass recipe, in millimeters of sea level equivalent, the formal uncertainty carried, the missing months left as holes"
  - method: "the attested computation ../computations/sea-level-budget.md: residual per month, four trends with the sanctioned interval, the combined uncertainty with the deep-steric systematic stated separately, the verdict, the corrections table as receipt facts"
expected:
  - quantity: "the identity"
    statement: "altimetry equals mass plus steric plus the deep-steric term below the Argo floor, within uncertainties, only under consistent bookkeeping; the residual trend is compared with the quadrature of the three term uncertainties plus the deep-steric uncertainty"
  - quantity: "numeric anchor"
    statement: "none recorded yet: no real-data run exists, and the attested computation's reference run is a synthetic fixture whose known closure proves the chain, not the ocean; the first real-data anchor is recorded in ../computations/sea-level-budget.md when it is measured"
expected_uncertainty:
  - quantity: "per term"
    statement: "the larger of the sampling half width from the sanctioned trend chain and the formal error propagated from the product's per-month uncertainties; the mass term's systematics (GIA model, leakage, low-degree replacements) are quoted beside it as the mass recipe states them, never folded into the formal error"
  - quantity: "deep steric"
    statement: "the steric contribution below the Argo sampling floor is not measured by the array and is not zero; it is stated as a value with an uncertainty of its own, and a budget that omits it has omitted a real term"
sources:
  - id: convention-slbc
    resource: ../conventions/sea-level-budget-closure.md
    title: "Bundle convention: sea level budget closure, a correction-consistency problem first"
  - id: computation
    resource: ../computations/sea-level-budget.md
    title: "The attested computation this recipe walks: the identity, the bookkeeping, the fixture, the refusal rule, the reference run"
  - id: nasa-ssh
    resource: ../datasets/nasa-ssh.md
    title: "Bundle dataset concept: NASA-SSH, the altimetry term"
  - id: mascons
    resource: ../datasets/grace-fo-mascons.md
    title: "Bundle dataset concept: GRACE/GRACE-FO JPL mascons, the mass term"
  - id: recipe-mass
    resource: grace-mass-to-sea-level.md
    title: "Bundle recipe: from a GRACE mass change to a sea level equivalent"
  - id: gotcha-gia
    resource: ../gotchas/grace-gia-correction.md
    title: "Bundle gotcha: the GIA model already applied"
  - id: gotcha-leakage
    resource: ../gotchas/grace-coastal-leakage.md
    title: "Bundle gotcha: coastal leakage"
  - id: gotcha-gap
    resource: ../gotchas/grace-intermission-gap.md
    title: "Bundle gotcha: the GRACE to GRACE-FO gap"
  - id: gotcha-low-degree
    resource: ../gotchas/grace-low-degree-replacements.md
    title: "Bundle gotcha: the degree-1 and C20/C30 replacements"
  - id: release-note
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/docs/GRACE_GRACE-FO_ReleaseNotes_JPL_MASCON.txt
    title: "JPL GRACE mascon solution release notes (RL06.3M version 4): the GAD de-aliasing signal restored over the ocean part of the mascons"
  - id: wcrp-2018
    resource: https://doi.org/10.5194/essd-10-1551-2018
    title: "WCRP Global Sea Level Budget Group (2018), Global sea-level budget 1993 to present, Earth System Science Data"
  - id: roemmich-gilson-2009
    resource: https://doi.org/10.1016/j.pocean.2009.03.004
    title: "Roemmich and Gilson (2009), the gridded Argo steric estimate, Progress in Oceanography"
status: draft
stale_after: 2027-03-13
---

# Closing the global mean sea level budget

**The three terms.** Sea level as altimetry measures it is the sum of
the water added to the ocean (mass, from gravimetry) and the expansion
of the water already there (steric, from hydrography), plus whatever
the hydrography does not reach.[^convention-slbc][^wcrp-2018] Each
term comes from one product, and each product carries a trap that a
concept in this bundle names:

1. **Altimetry: NASA-SSH.** The global mean of the simple grids per
   calendar month (the grids share passes, so the month is the
   sample). The product applies the dynamic atmospheric correction and
   sits on a fixed mean sea surface; its trends are era-dependent
   (reference missions only, one ground track), and a budget over a
   period names the era.[^nasa-ssh]
2. **Steric: gridded Argo.** The Roemmich and Gilson estimate, or a
   successor, integrated over the depth range the array samples and
   averaged over the ocean; the sampled depth floor is stated, because
   the steric contribution below it is not measured and is not
   zero.[^roemmich-gilson-2009][^convention-slbc] A regional budget
   may instead build the term from profiles through core's
   observations connector; that is a loader outside the gate, since
   no gate depends on a connector.
3. **Mass: the mascons.** The CRI-filtered grids summed over the ocean
   mascons with their true areas, converted to millimeters of sea
   level per the mass recipe, the formal uncertainty carried.[^mascons][^recipe-mass]
   The product restores the GAD de-aliasing signal over the ocean part
   of its mascons, so the mass term's atmospheric convention is the
   product's, and the corrections table says so beside the altimetry
   correction.[^release-note]
   Four traps hold this term: the GIA model the product already
   subtracted,[^gotcha-gia] coastal leakage into the nearshore ocean
   mascons,[^gotcha-leakage] the 2017 to 2018 inter-mission gap and
   the battery-management months a continuous-looking series
   hides,[^gotcha-gap] and the degree-1 and C20/C30 series substituted
   into the product.[^gotcha-low-degree]

**The matching-period rule, at the month.** Every term covers the same
window, and a month with no solution in any term is a hole in the
budget: dropped from every term, never interpolated, the trends fitted
on the epochs that remain. A window that crosses the inter-mission gap
states how continuity was handled and cites the independent evidence,
or the computation refuses it.[^gotcha-gap]

**How the residual is read.** The residual trend (altimetry minus mass
minus steric) minus the stated deep-steric term is compared with the
quadrature of the three term uncertainties plus the deep-steric
uncertainty. Inside it, the budget closes within uncertainty. Outside
it, the first reading is correction consistency: the GIA treatment of
altimetry against mass, the inverse-barometer conventions, the
reference frames, the smoothing, the period and the gap, audited from
the corrections table the receipt carries, before any missing-physics
conclusion is drawn; a budget that closes only because two
inconsistencies cancel is the other failure the table is there to
catch.[^convention-slbc]

**The attested form.** The computation walks these steps with the
corrections table as receipt facts, four trends with the sanctioned
interval, and a verdict the attester recomputes; its fixture run is
the reference until a real-data run is made, and no numeric anchor is
quoted here until then.[^computation]

**Provenance.** Every number quoted from this recipe names the three
product versions, the steric estimate and its depth floor, the GIA
model and low-degree series the mass term carries, the ocean mask, the
window, the months missing and the gap handling. The mascon product's
release note was read on 2026-09-13; the journal sources resolve by
DOI but their pages were not readable from the session, so the
maintainer's review opens them before the recipe goes stable.[^release-note]

[^convention-slbc]: conventions/sea-level-budget-closure.md
[^computation]: computations/sea-level-budget.md
[^nasa-ssh]: datasets/nasa-ssh.md
[^mascons]: datasets/grace-fo-mascons.md
[^recipe-mass]: recipes/grace-mass-to-sea-level.md
[^gotcha-gia]: gotchas/grace-gia-correction.md
[^gotcha-leakage]: gotchas/grace-coastal-leakage.md
[^gotcha-gap]: gotchas/grace-intermission-gap.md
[^gotcha-low-degree]: gotchas/grace-low-degree-replacements.md
[^wcrp-2018]: WCRP Global Sea Level Budget Group (2018), Earth System Science Data 10, doi:10.5194/essd-10-1551-2018
[^roemmich-gilson-2009]: Roemmich and Gilson (2009), Progress in Oceanography 82, doi:10.1016/j.pocean.2009.03.004
[^release-note]: JPL GRACE mascon solution release notes, RL06.3M version 4
