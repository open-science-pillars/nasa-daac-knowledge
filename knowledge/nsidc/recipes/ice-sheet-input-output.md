---
type: recipe
spheres: [cryosphere]
title: "The input-output estimate of an ice sheet's mass balance: what falls on the grounded ice, less what leaves through the gate"
description: "The two terms of an input-output mass balance, which product supplies each, which concept holds each term's trap (the velocity mosaic that is a composite in map units, the thickness that is mass conservation in fast flow and an interpolation elsewhere, the mask that decides where the grounding line is, the surface mass balance that no NASA archive distributes over grounded Greenland), the gate rule that makes a node's flux legitimate, and how the result is read beside the gravimetric and altimetric estimates and the published assessment."
tags: [ice-sheet, mass-balance, input-output, discharge, flux-gate, surface-mass-balance, greenland, antarctica, its-live, bedmachine, velocity, thickness, recipe]
generated: { by: knowledge-seeder/claude, at: 2026-09-19T08:00:00Z }
verified:
  - { by: human:PaulMRamirez, at: 2026-09-19T08:08:31Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/198 }
  - { by: human:PaulMRamirez, at: 2026-09-20T21:41:20Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/207 }
inputs:
  - dataset: ../datasets/its-live-ice-velocity.md
  - dataset: ../datasets/bedmachine-greenland-antarctica.md
  - dataset: ../datasets/imbie-ice-sheet-assessment.md
  - velocity: "the surface velocity component normal to each flux gate node, per epoch, from the ITS_LIVE annual regional mosaics at 120 m in the region's polar stereographic projection, in the product's own map units, with the image pair count and the product's qualitative error beside it"
  - thickness: "the ice thickness at the same nodes from BedMachine, with errbed and with the source field that says which method made the pixel, of the product's nominal year"
  - surface_mass_balance: "the surface mass balance rate over the ice sheet's grounded domain, at the product's native sampling, aggregated to each velocity epoch's calendar year as a period weighted mean"
  - method: "the attested computation land-ice/knowledge/computations/ice-sheet-input-output.md: the discharge as the node sum of density times normal velocity times node width over the areal scale times thickness, the mass rate as the surface mass balance less the discharge epoch by epoch, each rate the mean of its epochs with an interval, the bar the mass rate's own half width plus the stated gate systematic, the gate and product statements as receipt facts"
expected:
  - quantity: "the identity"
    statement: "the mass rate of the grounded ice sheet equals the surface mass balance over it less the discharge across a gate set that spans its grounded margin, when both terms cover the same ice and the same years; the rate is compared with the bar the receipt carries and is a third estimate of the quantity the gravimetric and altimetric methods of land-ice/knowledge/computations/ice-sheet-balance.md measure"
  - quantity: "numeric anchor"
    statement: "there is no real-data anchor: the committed data root carries the real ITS_LIVE gate velocities and neither of the other two terms, so the record run is a refusal, and the only recorded numbers are the fixture's (Greenland, gate set synthetic-outlets, 2005-01 through 2014-12, seed 7: surface mass balance +400.086 and discharge +490.809 gigatonnes per year, mass rate minus 90.723 against a bar of 67.518, significant), recorded with their refusals and the reasons the two terms are missing in land-ice/knowledge/computations/ice-sheet-input-output.md"
expected_uncertainty:
  - quantity: "per term"
    statement: "the larger of the sampling error (the standard deviation of the annual epochs over the root of the effective sample size from the lag-1 autocorrelation) and the formal error, which is the mean of the per epoch uncertainties because the thickness error and the surface mass balance model error do not resample from year to year; the velocity product's own error is described by its user guide as typically unrealistically low and to be used with the image pair count as a qualitative metric, so a discharge interval built on it is a lower bound"
  - quantity: "the mass rate"
    statement: "the mass rate's own half width on the epochs both terms carry, plus the stated gate systematic, which is half the spread of the discharges under the other gate rules where the velocity stamp records a sensitivity and zero with that reason where it records none; the thickness nominal year, the mosaic's composite date, the surface mass balance model and its forcing enter the bookkeeping, never the bar"
sources:
  - id: computation
    resource: land-ice/knowledge/computations/ice-sheet-input-output.md
    title: "The attested computation this recipe walks: the terms, the gate rule, the fixture, the refusal rule, the reference run and the reading of the three estimates"
  - id: closure
    resource: land-ice/knowledge/computations/ice-sheet-balance.md
    title: "Bundle attested computation: the gravimetric and altimetric estimates of the same mass rate, and their anchored run"
  - id: closure-recipe
    resource: ../recipes/ice-sheet-balance.md
    title: "Bundle recipe: the closure's own walk, whose third estimate this recipe is"
  - id: its-live
    resource: ../datasets/its-live-ice-velocity.md
    title: "Bundle dataset concept: the MEaSUREs ITS_LIVE regional velocity mosaics, their error fields and the map-unit convention"
  - id: gotcha-mosaic
    resource: ../gotchas/velocity-mosaic-epochs-and-gaps.md
    title: "Bundle gotcha: an annual mosaic is a composite with its own effective date and count, and a discharge needs thickness from another product"
  - id: bedmachine
    resource: ../datasets/bedmachine-greenland-antarctica.md
    title: "Bundle dataset concept: BedMachine thickness, bed, mask, source and errbed, and the nominal years"
  - id: gotcha-thickness
    resource: ../gotchas/bedmachine-thickness-is-interpolated.md
    title: "Bundle gotcha: thickness between flight lines is mass conservation or an interpolation, with source, dataid and errbed saying which"
  - id: gotcha-gate
    resource: ../gotchas/bedmachine-mask-and-grounding-line.md
    title: "Bundle gotcha: a discharge gate sits on grounded ice upstream of the grounding line"
  - id: gotcha-grid
    resource: ../gotchas/polar-stereographic-not-latlon.md
    title: "Bundle gotcha: a sum on a polar stereographic grid needs the true ground scale"
  - id: gotcha-basins
    resource: ../gotchas/ice-sheet-boundaries-and-drainage-basins.md
    title: "Bundle gotcha: a per-region number names the boundary set it used"
  - id: imbie
    resource: ../datasets/imbie-ice-sheet-assessment.md
    title: "Bundle dataset concept: the published multi-method assessment, its input-output group and the spread between the three technique groups"
  - id: gotcha-groups
    resource: ../gotchas/assessment-method-groups-are-not-independent.md
    title: "Bundle gotcha: an assessment's method groups are not independent measurements of the same thing"
  - id: firn
    resource: ../datasets/firn-model-air-content.md
    title: "Bundle dataset concept: the firn air content term, which the altimetric method needs and this one does not"
  - id: data-root
    resource: land-ice/knowledge/references/retrieval/ice-sheet-input-output-root/RECORD.json
    title: "The stamped data root: the velocity term, the gate table, the absent terms with their reasons, and SOURCES.json"
  - id: gardner-2018
    resource: https://doi.org/10.5194/tc-12-521-2018
    title: "Gardner and others (2018), Increased West Antarctic and unchanged East Antarctic ice discharge over the last 7 years, The Cryosphere 12, 521 to 547: the reference flux-gate discharge computation"
status: stable
stale_after: 2027-03-19
---

# The input-output estimate of an ice sheet's mass balance

**Two terms, and neither is a height.** An ice sheet gains mass at
its surface and loses it through its margin. The input-output method
measures those two separately and subtracts: the surface mass balance
over the grounded ice, from a model, less the discharge of ice
through a gate near the grounding line, from a velocity times a
thickness. It is the third of the three satellite methods the
assessments reconcile, beside gravimetry and
altimetry.[^imbie][^closure] Its one structural advantage is that it
needs no firn model: an altimetric mass rate is a surface height
change, and a height is a mass only after the firn air content change
is removed and a density applied, which in this bundle's closure is
what dominates the altimetric rate's formal error.[^firn][^closure]
It pays for that with a regional climate model in the input term and
a mass conservation inversion in the thickness.[^gotcha-thickness]

**1. The discharge, factor one: velocity.** The ITS_LIVE regional
mosaics give the surface velocity at 120 m for sixteen glacier-covered
regions, annually and as a record mean.[^its-live] Three properties
of them decide what a flux gate may say. An annual mosaic is an
error-weighted fit of the image pairs whose spans overlap the year,
not a calendar mean, so it is a composite with its own effective date
and its own count, which the file carries as `count`; annual coverage
is nearly complete for all regions only after 2013.[^gotcha-mosaic]
The error fields are, in the Version 2 user guide's own words,
typically unrealistically low, to be used with the image pair count
as qualitative error metrics, so a discharge interval built on them
alone is a lower bound.[^its-live] And Version 2 velocities are in
map units, uncorrected for projection scale, so a map velocity times
a map gate width is the ground flux times the projection's areal
scale; the two readings differ by a few percent, and a statement
names which one it took.[^its-live][^gotcha-grid]

**2. The discharge, factor two: thickness, and the method that made
it.** BedMachine gives a continuous thickness, but between the radar
flight lines the number is computed: mass conservation where the ice
flows fast, kriging or streamline diffusion or a perturbation
inversion in the slow interior, hydrostatic equilibrium on floating
ice. The file says which per pixel in `source`, how far to trust it
in `errbed`, and what the pixel is in `mask`.[^bedmachine][^gotcha-thickness]
A gate node is a legitimate place to multiply a velocity by a
thickness only where the thickness was made by mass conservation,
which is what the method was built to conserve, and only where the
mask says grounded ice, because the discharge of an ice sheet is the
flux across the grounding line and ice that has crossed it has
already left the sheet.[^gotcha-gate] The attested computation
refuses a gate set that fails either test rather than reporting a
number from it.[^computation] Two further facts travel with the
thickness: it is of the product's nominal year, 2007 for Greenland
and 2015 for Antarctica, while the velocity is of each epoch, so a
discharge series holds the thickness fixed while the velocity
changes; and errbed is not stated by either guide to be a formal
covariance or independent between cells, so summing it along a gate
treats it as fully correlated.[^bedmachine][^gotcha-thickness] The
reference flux-gate computation in the literature is Gardner and
others 2018, an Antarctic discharge of 1929 gigatonnes per year in
2015 with an uncertainty of 40.[^gardner-2018]

**3. The input: surface mass balance over the grounded ice.** This is
the term the bundle cannot supply. The ITS_LIVE Greenland elevation
change product carries firn air content and no surface mass balance
field; the only GEMB surface mass balance in the distribution is
masked to the floating Antarctic ice shelves and is not an input to a
grounded balance; and the two regional climate models the
assessment's own input-output estimates rest on, RACMO and MAR, are
not distributed by a NASA archive.[^data-root][^imbie] The
computation refuses an ice sheet whose grounded surface mass balance
is absent rather than differencing a shelf accumulation against a
grounded discharge.[^computation]

**The gate rule.** A discharge is a flux through a curve, and where
the curve is drawn decides what is inside it. Three statements make a
gate set usable: the rule that placed its nodes, whether it spans the
ice sheet's grounded margin, and which product's mask decided that a
node is grounded. A set of segments across a handful of fast outlets
is a discharge of those outlets, not of the ice sheet, so an ice
sheet wide mass rate cannot be formed from it, and the computation
refuses rather than scaling it up.[^computation] The velocity
product's own masks cannot place the gate: in the Greenland mosaic
the floating ice mask carries no cell at all, so the ice mask's
margin is the only boundary it offers and that margin is not the
grounding line.[^data-root][^gotcha-gate] Half the spread of the
discharge under the other gate rules is the systematic that belongs
in the bar, in the way the closure's mascon selection sensitivity
is.[^closure][^computation]

**How the result is read.** The mass rate is the surface mass balance
less the discharge at each epoch, then the mean, so a year both terms
carry differences two numbers measured in the same year before the
mean is taken; the bar is the mass rate's own half width plus the
gate systematic, and the verdict is whether the rate is
distinguishable from zero.[^computation] Beside it stand the other
two estimates of the same quantity. The assessment reconciles all
three and records where they part: across all ice sheets the
input-output estimate is the most negative and altimetry the most
positive, except in East Antarctica, where the three disagree on even
the sign; the input-output estimates include the peripheral glaciers
and ice caps, the altimetry estimates exclude them and gravimetry
cannot separate them, a systematic bias between the techniques the
assessment names as still to be removed; and only three input-output
estimates stand behind the Greenland group, one behind the Antarctic,
on two surface mass balance models.[^imbie][^gotcha-groups][^gotcha-basins]
So a third estimate is read for its sign and its distance from the
other two, not as a tiebreak: the three are not independent in the
sense the error propagation assumes, and an input-output rate below
both of the others is the expected ordering rather than a
disagreement. This bundle's own two estimates already sit about 55
gigatonnes per year more negative than the assessment's reconciled
Greenland rates for 2003 to 2016, outside the assessment's
uncertainty and inside their own intervals, and a third estimate is
what would show whether that offset belongs to the two observing
systems or to the reconciliation.[^closure][^imbie]

[^computation]: land-ice/knowledge/computations/ice-sheet-input-output.md, the attested computation and its refusals
[^closure]: land-ice/knowledge/computations/ice-sheet-balance.md, the gravimetric and altimetric estimates
[^closure-recipe]: recipes/ice-sheet-balance.md
[^its-live]: datasets/its-live-ice-velocity.md
[^gotcha-mosaic]: gotchas/velocity-mosaic-epochs-and-gaps.md
[^bedmachine]: datasets/bedmachine-greenland-antarctica.md
[^gotcha-thickness]: gotchas/bedmachine-thickness-is-interpolated.md
[^gotcha-gate]: gotchas/bedmachine-mask-and-grounding-line.md
[^gotcha-grid]: gotchas/polar-stereographic-not-latlon.md
[^gotcha-basins]: gotchas/ice-sheet-boundaries-and-drainage-basins.md
[^imbie]: datasets/imbie-ice-sheet-assessment.md
[^gotcha-groups]: gotchas/assessment-method-groups-are-not-independent.md
[^firn]: datasets/firn-model-air-content.md
[^data-root]: land-ice/knowledge/references/retrieval/ice-sheet-input-output-root/RECORD.json and SOURCES.json
[^gardner-2018]: Gardner and others (2018), The Cryosphere 12, doi:10.5194/tc-12-521-2018
