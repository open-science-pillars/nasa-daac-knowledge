---
type: convention
title: "Heat budget closure: the tutorial's own checkpoints"
description: "The checkpoint numbers the tutorial's closure chapter itself produces: the summed-residual bound, the histogram scale, and the geothermal-omission signature; pass bars stay owned by the attested computation."
tags: [ecco, tutorial-companion, heat-budget, closure]
generated: { by: claude-code/fable-5, at: 2026-08-30T21:25:00Z }
status: draft
stale_after: 2027-01-04
sources:
  - id: tut-heat-closure
    resource: https://ecco-v4-python-tutorial.readthedocs.io/ECCO_v4_Heat_budget_closure.html
    title: "ECCO v4 Python Tutorial: Global Heat Budget Closure"
    author: team:ecco-consortium
---

# Heat budget closure: the tutorial's own checkpoints

Companion concept for the closure chapter: the numbers a correct
walkthrough produces, as the tutorial states them, so an agent
reproducing the chapter has the chapter's own acceptance signals. The
authoritative pass bar for OSP work is NOT here: it is owned by
[the attested computation](../computations/ecco-heat-budget.md), with
the formulation narrative on
[the recipe](../recipes/ecco-heat-budget.md).

**The closure checkpoint.** Summing residuals vertically and
temporally yields below 10^-12 degC per second for most grid points,
and the chapter's residual histogram is drawn on the range 0 to
2e-12.[^tut-heat-closure]

**The geothermal signature.** Recomputed with the geothermal flux
omitted, the residual map is plotted at the 1e-9 scale and the chapter
states the geothermal contribution sits well above the closure
residual, by three orders of magnitude;[^tut-heat-closure] the trap
itself is
[ecco-geothermal-flux](../gotchas/ecco-geothermal-flux.md).

**Consistency with the signed concepts.** The tutorial's bound is a
global, depth-and-time-summed statistic; the OSP tolerance is absolute
and pointwise on tile-interior cell-months (measured max 4.95e-11,
median 5.7e-14 degC/s). These are different statistics of the same
closure and do not conflict; no layer-decision issue arises from this
chapter.

**Eval fixture.** The checkpoints above are extracted as a grader
fixture in the ecco-agent-evals repository
(`fixtures/tutorial/heat-budget-checkpoints.yaml`), chapter cited, for
tutorial-fidelity cases.

[^tut-heat-closure]: ECCO v4 Python Tutorial: Global Heat Budget Closure
