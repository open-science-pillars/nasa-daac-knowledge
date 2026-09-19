---
type: dataset-gotcha
spheres: [cryosphere]
title: "An assessment's method groups are not independent measurements of the same thing: they share corrections and records, they cover different ice, and the reconciled uncertainty shrinks by the square root of a count"
description: "The reconciled ice sheet mass balance the IMBIE assessment publishes is an error-weighted mean over three technique groups whose members are themselves error-weighted means, and both steps divide the uncertainty by the square root of the number of contributors. The assessment calls the three techniques independent for that purpose, and its own text records what they share: glacial isostatic adjustment models used on two of them, two surface mass balance models behind every input-output estimate, one satellite gravity record behind sixteen gravimetry estimates, and a peripheral glacier domain that altimetry excludes, gravimetry cannot separate and the input-output method includes. Reading agreement with two groups as two confirmations, or the reconciled interval as the spread of independent measurements, overstates how well a rate is pinned."
tags: [imbie, assessment, intercomparison, altimetry, gravimetry, input-output, uncertainty, independence, gia, surface-mass-balance, peripheral-glaciers, greenland, antarctica, cryosphere]
generated: { by: knowledge-seeder/claude, at: 2026-09-19T05:30:00Z }
severity: medium
dataset: ../datasets/imbie-ice-sheet-assessment.md
status: draft
stale_after: 2027-03-19
sources:
  - id: assessment
    resource: ../datasets/imbie-ice-sheet-assessment.md
    title: "Bundle dataset concept: what the assessment reports per ice sheet and period, its uncertainties and its method groups"
  - id: imbie-pdf
    resource: https://essd.copernicus.org/articles/15/1597/2023/essd-15-1597-2023.pdf
    title: "Otosaka and 67 others, 2023, Mass balance of the Greenland and Antarctic ice sheets from 1992 to 2020, Earth System Science Data 15, 1597 to 1616, read in full 2026-09-19: the group counts, the aggregation equations, the technique comparison and the limitations section"
  - id: otosaka-2023
    resource: https://doi.org/10.5194/essd-15-1597-2023
    title: "The registry record of the assessment, verified on Crossref 2026-09-19"
  - id: gotcha-basins
    resource: ./ice-sheet-boundaries-and-drainage-basins.md
    title: "Bundle gotcha: a per-region number names the basin set and the grounded or floating scope it used"
  - id: gotcha-spread
    resource: ./firn-air-content-spread-dominates-the-altimetric-mass-rate.md
    title: "Bundle gotcha: the firn model spread that stands behind the altimetry group's conversion and behind this bundle's own altimetric rate"
  - id: computation
    resource: ../computations/ice-sheet-balance.md
    title: "Bundle attested computation: the closure whose runs are read against the assessment"
---

# An assessment's method groups are not independent measurements of the same thing

**Mechanism.** The assessment builds its published rate in two averaging
steps. Inside each technique group the contributed series are averaged
with inverse-error weights, and the group's uncertainty is the
quadrature sum of the member uncertainties divided by the square root
of the number of members; the three group series are then combined at
each epoch as an error-weighted mean, and the reconciled uncertainty is
the quadrature sum of the group uncertainties divided by the square
root of the number of groups available.[^imbie-pdf][^assessment] Both
divisions are the arithmetic of independent draws, and the assessment
names the three techniques as independent for that purpose. Its own
text records what they nonetheless share. Glacial isostatic adjustment
models correct both the gravimetry and, more weakly, the altimetry
estimates, and the assessment asks for an intercomparison of those
models because the choice moves the
result.[^imbie-pdf] Only two surface mass balance models, RACMO and
MAR, stand behind every input-output estimate included.[^imbie-pdf] The
sixteen gravimetry estimates for each ice sheet are different solutions
of one satellite gravity record, and the assessment states that the
small number of input-output estimates, one in Antarctica, limits its
ability to attribute within-group differences to method, corrections or
auxiliary data at all.[^imbie-pdf] The groups also do not cover the
same ice: the input-output estimates include the peripheral glaciers
and ice caps, the altimetry estimates exclude them, and satellite
gravimetry cannot separate them from the ice sheet, which the
assessment names as a source of systematic bias between techniques to
be removed in future rounds.[^imbie-pdf][^gotcha-basins] The result is
a set of differences with structure rather than scatter: across all ice
sheets the input-output estimate is the most negative and the altimetry
the most positive, except in East Antarctica, where the three disagree
on even the sign of the change, with a maximum difference of 105
gigatonnes per year, uncertainty 33, between the input-output and
gravimetry rates.[^imbie-pdf]

**Wrong-result mode.** A rate computed elsewhere is compared against
the assessment, found to sit inside the reconciled interval, and
reported as confirmed by three independent techniques; or it agrees
with two of the three groups and the agreement is counted twice. Both
read the group count as a number of independent confirmations when the
groups share the corrections that carry most of the disagreement. The
same reading is made of the interval itself: the reconciled
uncertainty is taken as the spread of independent measurements, which
it is not, and it is narrower than the spread between the groups where
that spread is large, so a number can sit outside every group's own
rate and inside the reconciled interval. In Greenland the three
technique rates lie within a standard deviation of 19 gigatonnes per
year of each other against a reconciled uncertainty of 22, but in
Antarctica the spread is 79 against a reconciled uncertainty of 24, and
by region it is 54 at East Antarctica, 18 at West Antarctica and 16 at
the Peninsula.[^imbie-pdf] A third failure follows from the domains: an
altimetric rate computed over the ice sheet alone, or over the ice
sheet with its peripheral glaciers, is compared against the reconciled
rate without saying which ice each covers, and a difference that is a
difference of domain is attributed to method. An altimetric rate is
also not an independent check on the altimetry group, because it rests
on the same firn models.[^gotcha-spread]

**Correct approach.** A comparison against the assessment states which
number it is against: the reconciled rate for a period, the aggregated
rate of one technique group, or the spread between the groups, each of
which answers a different question.[^assessment][^imbie-pdf] The
reconciled uncertainty is voiced as the assessment's own bookkeeping
over its contributors rather than as the uncertainty of an independent
measurement, and where the between-group spread is quoted it is quoted
beside it, because the two differ by a factor of three in Antarctica
and its regions.[^imbie-pdf] The ice each side covers is named, so that
the peripheral glaciers are accounted for on both sides or the
mismatch is stated as a term, and the basin set and grounded or
floating scope are named with it.[^gotcha-basins][^imbie-pdf] A
statement that a result is corroborated names what the corroborating
estimate shares with it: the glacial isostatic adjustment model, the
surface mass balance model, the firn model, or the satellite record
itself.[^imbie-pdf][^gotcha-spread][^computation]

**Verification.** The assessment was fetched from the publisher and
read in full on 2026-09-19: the input data section for the group counts
(27 Greenland estimates as 8 altimetry, 16 gravimetry and 3
input-output, 23 Antarctic estimates as 6, 16 and 1, across 14 satellite
missions), the methods section for the two averaging steps and their
error equations and for the phrase naming the three techniques as
independent, the technique comparison for the spreads and the East
Antarctic disagreement, and the limitations section for the peripheral
glacier domains, the shared models and the calls for model
intercomparisons.[^imbie-pdf] Its record, with its 68 authors, journal,
volume, pages and year, was verified against the Crossref registry the
same day.[^otosaka-2023] The bundle's assessment concept carries the
per-period rates this gotcha does not restate, and the closure concept
is where a run of this bundle's own is compared against
them.[^assessment][^computation]

[^assessment]: This bundle's assessment dataset concept
[^imbie-pdf]: Otosaka and others, 2023, read in full 2026-09-19
[^otosaka-2023]: Otosaka and others, 2023, doi:10.5194/essd-15-1597-2023
[^gotcha-basins]: This bundle's gotcha on ice sheet boundaries and drainage basins
[^gotcha-spread]: This bundle's gotcha on the firn model spread
[^computation]: This bundle's attested ice sheet mass balance closure
