---
type: recipe
spheres: [cryosphere]
title: "Closing an ice sheet's mass balance: gravimetry against firn-corrected altimetry, and the input-output estimate this bundle cannot yet make"
description: "The terms of an ice sheet mass balance closure, which product supplies each, which concept holds each term's trap (the mascon GIA model, leakage and selection; the height change that is not a mass change without a firn model and a density; the discharge that needs a grounded flux gate and an interpolated thickness), the annual-lag rule that removes the seasonal cycle, and how the residual is read: correction consistency before missing physics."
tags: [ice-sheet, mass-balance, closure, greenland, antarctica, grace-fo, mascons, altimetry, its-live, atl15, firn, gemb, discharge, recipe]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T20:00:00Z }
verified:
  - { by: human:PaulMRamirez, at: 2026-09-16T03:06:45Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/176 }
  - { by: human:PaulMRamirez, at: 2026-09-20T21:41:20Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/207 }
inputs:
  - dataset: ../../podaac/datasets/grace-fo-mascons.md
  - dataset: ../datasets/icesat2-atl15.md
  - dataset: ../datasets/its-live-ice-velocity.md
  - dataset: ../datasets/bedmachine-greenland-antarctica.md
  - gravimetry: "the JPL CRI mascon grid summed over the ice sheet's land mascons per solution month, in gigatonnes, the per-mascon formal error in quadrature, the selection rule and its sensitivity stated, the missing months left as holes"
  - altimetry: "the surface height change summed with true cell areas to a volume anomaly per epoch (ITS_LIVE elevation change, monthly, or ATL15 delta_h with ice_area, quarterly), less the GEMB firn air content volume anomaly at the same epochs over the same domains, times a stated ice density"
  - firn: "the GEMB firn air content anomaly of the ice sheet balance root, its two-model spread floored at the series median per domain"
  - method: "the attested computation land-ice/knowledge/computations/ice-sheet-balance.md: each rate the mean of its annual-lag differences with an interval, the residual on the common epochs with its own half width plus the mascon selection systematic, the verdict, the bookkeeping as receipt facts"
expected:
  - quantity: "the identity"
    statement: "the gravimetric rate equals the altimetric rate after the firn air content change is removed and a density applied, within the residual's own uncertainty plus the mascon selection systematic, only under consistent bookkeeping; the residual is compared with the bar the receipt carries"
  - quantity: "numeric anchor"
    statement: "Greenland, 2003-01 through 2016-12 on the stamped data root (151 of 168 mascon months, 168 ITS_LIVE epochs, 127 common annual-lag differences): gravimetry minus 281.297 and altimetry minus 283.353 Gt per year on their own epochs, a residual of minus 25.123 on the common epochs against a bar of 140.813, closed within uncertainty; both rates about 55 Gt per year more negative than the IMBIE 2023 assessment's reconciled rates for the period; recorded with its loaders and stamps in land-ice/knowledge/computations/ice-sheet-balance.md"
expected_uncertainty:
  - quantity: "per term"
    statement: "the larger of the sampling error (the standard deviation of the annual-lag differences over the root of the effective sample size, floored at the number of non-overlapping years) and the formal error the per-epoch uncertainties propagate, times Student's t; the anchor's term intervals rest on the sampling error and are dominated by the year-to-year variability of the rate, the formal errors (3.99 Gt per year for gravimetry, 44.83 for altimetry) standing beside them"
  - quantity: "the residual"
    statement: "the residual's own half width on the common epochs, 128.9 Gt per year in the anchor because the two records disagree by hundreds of gigatonnes per year at the annual scale even though their means agree to 2, plus the stated mascon selection systematic of 11.9; the firn model spread enters the altimetry term's formal error and the GIA model, the density and the leakage enter the bookkeeping, never the bar"
sources:
  - id: computation
    resource: land-ice/knowledge/computations/ice-sheet-balance.md
    title: "The attested computation this recipe walks: the terms, the rate method, the fixture, the refusal rule, the reference run"
  - id: gotcha-firn
    resource: ../gotchas/atl15-height-change-is-not-mass-change.md
    title: "Bundle gotcha: height change is not mass change without a firn model and a density"
  - id: atl15
    resource: ../datasets/icesat2-atl15.md
    title: "Bundle dataset concept: ICESat-2 ATL15, the reduced resolutions and ice_area"
  - id: gotcha-epoch
    resource: ../gotchas/atl15-delta-h-reference-epoch.md
    title: "Bundle gotcha: delta_h is relative to the 2020 reference surface and each lagged rate has its own window"
  - id: its-live
    resource: ../datasets/its-live-ice-velocity.md
    title: "Bundle dataset concept: the ITS_LIVE products, whose elevation change files supply the altimetry and firn terms and whose velocity mosaics a discharge would take"
  - id: gotcha-mosaic
    resource: ../gotchas/velocity-mosaic-epochs-and-gaps.md
    title: "Bundle gotcha: an annual mosaic is a composite with its own effective date, and a discharge needs thickness from another product"
  - id: bedmachine
    resource: ../datasets/bedmachine-greenland-antarctica.md
    title: "Bundle dataset concept: BedMachine thickness, bed, mask and error"
  - id: gotcha-gate
    resource: ../gotchas/bedmachine-mask-and-grounding-line.md
    title: "Bundle gotcha: a discharge gate sits on grounded ice upstream of the grounding line"
  - id: gotcha-thickness
    resource: ../gotchas/bedmachine-thickness-is-interpolated.md
    title: "Bundle gotcha: thickness between flight lines is mass conservation or an interpolation, with errbed saying which"
  - id: gotcha-basins
    resource: ../gotchas/ice-sheet-boundaries-and-drainage-basins.md
    title: "Bundle gotcha: a per-region number names its boundary set"
  - id: gotcha-grid
    resource: ../gotchas/polar-stereographic-not-latlon.md
    title: "Bundle gotcha: a sum on a polar stereographic grid needs the true cell area"
  - id: mascons
    resource: ../../podaac/datasets/grace-fo-mascons.md
    title: "Podaac bundle dataset concept: the JPL mascon solutions"
  - id: gotcha-gia
    resource: ../../podaac/gotchas/grace-gia-correction.md
    title: "Podaac bundle gotcha: the GIA model already applied"
  - id: gotcha-leakage
    resource: ../../podaac/gotchas/grace-coastal-leakage.md
    title: "Podaac bundle gotcha: leakage across the coastline"
  - id: gotcha-gap
    resource: ../../podaac/gotchas/grace-intermission-gap.md
    title: "Podaac bundle gotcha: the GRACE to GRACE-FO gap"
  - id: gotcha-low-degree
    resource: ../../podaac/gotchas/grace-low-degree-replacements.md
    title: "Podaac bundle gotcha: the degree-1 and C20/C30 replacements"
  - id: data-root
    resource: land-ice/knowledge/references/retrieval/ice-sheet-balance-root/RECORD.json
    title: "The stamped data root: the loaders' stamps, the bookkeeping and closure tables, and SOURCES.json"
  - id: otosaka-2023
    resource: https://doi.org/10.5194/essd-15-1597-2023
    title: "Otosaka and others (2023), Mass balance of the Greenland and Antarctic ice sheets from 1992 to 2020, Earth System Science Data 15, 1597 to 1616 (IMBIE)"
  - id: smith-2020
    resource: https://doi.org/10.1126/science.aaz5845
    title: "Smith and others (2020), Pervasive ice sheet mass loss reflects competing ocean and atmosphere processes, Science 368, 1239 to 1242"
status: stable
stale_after: 2027-03-15
---

# Closing an ice sheet's mass balance

**The three estimates.** An ice sheet's mass balance is measured
three ways that share no instrument: gravimetry weighs the mass
change directly; altimetry measures the volume change and needs a
firn model and a density to make it a mass; the input-output method
subtracts the discharge across the grounding line from the surface
mass balance.[^otosaka-2023][^smith-2020] The IMBIE assessments
reconcile all three, and in Greenland over 2003 to 2018 the three
agree within a standard deviation of 19 Gt per year around a
reconciled minus 221 with an uncertainty of 22.[^otosaka-2023] This
bundle's attested closure makes the first two and refuses to state
the third; each term comes from one product, and each product carries
a trap a concept names:[^computation]

1. **Gravimetry: the JPL mascons.** The CRI grid summed over the ice
   sheet's land mascons per solution month, in gigatonnes, with the
   one-sigma-per-mascon error in quadrature.[^mascons] The traps: the
   GIA model is already subtracted (ICE-6G_D), and over Antarctica
   it is the largest systematic of the estimate; the degree-1 and
   C20/C30 series are the product's substitutions; the coastal
   mascons leak land signal into the ocean and ocean signal into the
   land, which the CRI filter reduces and does not remove; and the
   mascon set that is the ice sheet is a rule, not a fact, since a
   3-degree mascon straddles Nares Strait and Denmark Strait, so the
   rule, its sensitivity and the comparison with the provider's own
   series are stated in the stamp and half the sensitivity spread
   is the systematic the bar carries.[^gotcha-gia][^gotcha-low-degree][^gotcha-leakage][^gotcha-basins]
   The months the product lacks (June 2003, the battery-management
   months, the inter-mission gap) are holes, and a rate across the gap
   needs a citation of the continuity evidence.[^gotcha-gap]
2. **Altimetry: a height change, then a firn model, then a
   density.** The surface height change is summed with true cell
   areas to a volume anomaly (the ITS_LIVE elevation change monthly,
   or ATL15 delta_h with ice_area quarterly on the reduced
   resolution whose error fields account for the track
   correlation), and it is a volume of surface, not of
   ice.[^atl15][^gotcha-epoch][^its-live][^gotcha-grid] The firn air
   content anomaly over the same domains at the same epochs is
   removed and the remainder multiplied by a stated ice density (917
   kg per cubic metre, the GEMB product's own); the firn model, its
   forcing, the density and the elastic and GIA handling of the
   altimetry are receipt facts, and a run without a firn term over
   the altimetry domain refuses rather than states a volume in
   gigatonnes.[^gotcha-firn][^smith-2020] The firn uncertainty in
   this root is a two-model spread that crosses zero and is floored
   at its series median before it is propagated; it dominates the
   altimetric rate's formal error.[^data-root]
3. **The input-output estimate, not made here.** A surface mass
   balance over the grounded sheet and a discharge through flux
   gates: velocity from the ITS_LIVE mosaics (composites with their
   own effective dates and counts) times BedMachine thickness across
   gates on grounded ice upstream of the grounding line, where the
   thickness between flight lines is mass conservation or an
   interpolation with errbed saying which, and the Antarctic guide's
   mass-conservation threshold is 30 metres per
   year.[^its-live][^gotcha-mosaic][^bedmachine][^gotcha-gate][^gotcha-thickness]
   The committed root holds no Greenland surface mass balance and no
   grounded Antarctic one (the ITS_LIVE distribution carries GEMB
   output over the floating shelves only, and the RACMO2 and MAR
   alternates were not read), so the estimate awaits a surface mass
   balance loader; the published reference is IMBIE's input-output
   group.[^data-root][^otosaka-2023]

**The annual-lag rule.** Each term's rate over the window is the
mean of its annual-lag differences, the value at an epoch less the
value twelve months earlier, so the seasonal cycle of each product
cancels exactly without a climatology fit, a monthly hole removes
only the differences it touches, and a quarterly product sits on its
own epochs. The interval takes the effective sample size from the
lag-1 autocorrelation of the differences, floored at the number of
non-overlapping years, and the larger of the sampling and the formal
error.[^computation] On a smooth altimetry record the sampling error
is the year-to-year variability of the rate itself, so the term's
interval says how variable the rate was; the formal error beside it
is only the propagated per-epoch error, and for the mascon term it
omits leakage by the stamp's own statement (3.99 Gt per year at 95
percent against a provider monthly one sigma whose median is 23 Gt),
so neither number is the measurement uncertainty the assessment
quotes.

**How the residual is read.** The residual is the mean of altimetry
minus gravimetry differences on the epochs both terms carry, so the
interannual signal both observing systems see cancels first; what
remains is the disagreement of the two records, and its scatter sets
the bar. In the anchor the two rates agree in the mean to 2 Gt per
year while the residual series scatters by 203 Gt per year from month
to month, the altimetry rate near minus 800 against a gravimetry rate
near minus 300 in early 2010 and the reverse in early 2013: a reader
audits the firn model and its forcing, the altimetry record's mission
transitions, the mascon selection and the density before reading
missing physics into the residual, as the closure convention the
podaac bundle keeps for sea level says.[^computation][^gotcha-firn]
Both rates sit about 55 Gt per year more negative than the IMBIE 2023
assessment's reconciled rates for the period, outside the
assessment's uncertainty and inside the intervals each rate carries;
the provider's own Greenland mascon series agrees with the mass term
to 4 Gt per year over the same months, so the offset from the
assessment is a property of the mascon product and the selection, not
of this sum.[^otosaka-2023][^data-root] Antarctica refuses on this
root; the numbers the reader compares against are the assessment's
(minus 115 with an uncertainty of 24 Gt per year over 2003 to 2019,
with the three techniques spread by 79).[^otosaka-2023]

[^computation]: land-ice/knowledge/computations/ice-sheet-balance.md, the attested closure and its reference run
[^gotcha-firn]: gotchas/atl15-height-change-is-not-mass-change.md
[^atl15]: datasets/icesat2-atl15.md
[^gotcha-epoch]: gotchas/atl15-delta-h-reference-epoch.md
[^its-live]: datasets/its-live-ice-velocity.md
[^gotcha-mosaic]: gotchas/velocity-mosaic-epochs-and-gaps.md
[^bedmachine]: datasets/bedmachine-greenland-antarctica.md
[^gotcha-gate]: gotchas/bedmachine-mask-and-grounding-line.md
[^gotcha-thickness]: gotchas/bedmachine-thickness-is-interpolated.md
[^gotcha-basins]: gotchas/ice-sheet-boundaries-and-drainage-basins.md
[^gotcha-grid]: gotchas/polar-stereographic-not-latlon.md
[^mascons]: podaac bundle, datasets/grace-fo-mascons.md
[^gotcha-gia]: podaac bundle, gotchas/grace-gia-correction.md
[^gotcha-leakage]: podaac bundle, gotchas/grace-coastal-leakage.md
[^gotcha-gap]: podaac bundle, gotchas/grace-intermission-gap.md
[^gotcha-low-degree]: podaac bundle, gotchas/grace-low-degree-replacements.md
[^data-root]: land-ice/knowledge/references/retrieval/ice-sheet-balance-root/RECORD.json and SOURCES.json
[^otosaka-2023]: Otosaka and others (2023), Earth System Science Data 15, doi:10.5194/essd-15-1597-2023
[^smith-2020]: Smith and others (2020), Science 368, doi:10.1126/science.aaz5845
