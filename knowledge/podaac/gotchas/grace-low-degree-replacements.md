---
type: dataset-gotcha
spheres: [cryosphere, hydrosphere, geosphere]
title: "Degree-1 and C20/C30 replacements: large-scale mass trends from GRACE rest on terms the satellites do not measure, already substituted in the mascon product"
description: "GRACE senses no degree-1 (geocenter) term and its C20 oblateness term is unreliable, so the mascon product substitutes a modeled geocenter series and satellite-laser-ranging values for C20 (and C30 in the later record). The substitutions move ice-sheet and ocean-mass trends by amounts comparable to the formal errors. Comparing a mascon trend with a spherical-harmonic result that used different substitutions, or applying the substitutions again, attributes the difference to the ice or the ocean."
tags: [grace, grace-fo, degree-1, geocenter, c20, c30, oblateness, tn-13, tn-14, trends, mascons]
generated: { by: knowledge-seeder/claude, at: 2026-09-13T20:00:00Z }
severity: medium
# medium, as with the GIA gotcha: the substitutions are documented
# product behavior and bite through comparison inconsistency or
# re-application rather than through silently wrong single-product
# statistics; no eval case is required at this severity.
dataset: ../datasets/grace-fo-mascons.md
status: draft
stale_after: 2027-03-13
sources:
  - id: nasa-tellus-grac-grfo-mascon-cri-grid-rl06
    resource: https://podaac.jpl.nasa.gov/dataset/TELLUS_GRAC-GRFO_MASCON_CRI_GRID_RL06.3_V4
    title: "PO.DAAC collection page: TELLUS_GRAC-GRFO_MASCON_CRI_GRID_RL06.3_V4 (the product documentation names the degree-1 and C20/C30 series applied)"
  - id: grace-tellus
    resource: https://grace.jpl.nasa.gov/
    title: "GRACE Tellus project site: the technical notes on degree-1 (TN-13) and C20/C30 (TN-14) replacement"
  - id: sun-2016
    resource: https://doi.org/10.1002/2016JB013073
    title: "Sun, Riva and Ditmar, 2016, Optimizing estimates of annual variations and trends in geocenter motion and J2 from a combination of GRACE data and geophysical models, Journal of Geophysical Research: Solid Earth (the basis of the degree-1 series)"
  - id: loomis-2019
    resource: https://doi.org/10.1029/2019GL082929
    title: "Loomis, Rachlin and Luthcke, 2019, Improved Earth oblateness rate reveals increased ice sheet losses and mass-driven sea level rise, Geophysical Research Letters (satellite laser ranging C20 and C30, and what the replacement does to ice-sheet and ocean-mass trends)"
  - id: gia
    resource: ./grace-gia-correction.md
    title: "This bundle's GIA gotcha: the same shape of trap, a model choice applied before the user sees the data"
---

# Degree-1 and C20/C30 replacements

**Mechanism.** A satellite pair orbiting the Earth's center of mass
cannot observe the degree-1 term of the gravity field (the geocenter
motion), and GRACE's estimate of C20, the oblateness term, is
degraded by aliasing. Both terms carry large-scale mass signal, so
the projects substitute them: a modeled geocenter series estimated
from GRACE with an ocean and a GIA model, and C20 from satellite
laser ranging, with C30 also replaced in the later record after the
accelerometer degradation on GRACE and on GRACE-FO.[^sun-2016][^loomis-2019]
The mascon product arrives with these substitutions already
applied, named in its documentation.[^nasa-tellus-grac-grfo-mascon-cri-grid-rl06][^grace-tellus]

**Wrong-result mode.** The substituted terms project onto the largest
scales, which is exactly where ice-sheet mass balance and global ocean
mass live, so the choice of series moves those trends by amounts the
cited work quantifies as comparable to the formal errors.[^loomis-2019]
Two traps follow. Comparing a mascon trend with a spherical-harmonic
result whose author applied a different geocenter or C20 series (or
none) attributes the difference to the ice sheet or the ocean.
Applying a technical-note replacement again to the mascon product,
because a spherical-harmonic recipe says to, corrects twice.

**Correct approach.** Any large-scale trend from the mascon product
names the degree-1 and C20/C30 series the product applied (read from
the product documentation at analysis time) beside the GIA model.[^gia]
Cross-product and literature comparisons align those choices or quote
the spread as a systematic term beside the formal error. Nothing is
re-applied to a product that already carries it; the replacements
belong to the spherical-harmonic workflow, not to this one.

**Verification.** The product documentation lists the applied series
(link above).[^nasa-tellus-grac-grfo-mascon-cri-grid-rl06] The two
papers document the series and the trend sensitivity.[^sun-2016][^loomis-2019]
The double-application failure mode follows from the product being
pre-corrected, as with GIA.[^gia] Drafted without live access to the
sources from the drafting environment; the maintainer's review checks
each link before the concept goes stable.

[^nasa-tellus-grac-grfo-mascon-cri-grid-rl06]: PO.DAAC collection page: TELLUS_GRAC-GRFO_MASCON_CRI_GRID_RL06.3_V4
[^grace-tellus]: GRACE Tellus project site: the technical notes on the replacements
[^sun-2016]: Sun, Riva and Ditmar, 2016, Journal of Geophysical Research: Solid Earth, doi:10.1002/2016JB013073
[^loomis-2019]: Loomis, Rachlin and Luthcke, 2019, Geophysical Research Letters, doi:10.1029/2019GL082929
[^gia]: This bundle's GIA gotcha
