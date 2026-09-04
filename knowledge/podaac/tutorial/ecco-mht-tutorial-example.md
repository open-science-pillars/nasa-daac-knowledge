---
type: convention
title: "The MHT chapter: scope machinery and a constants inconsistency worth knowing"
description: "Tutorial-companion facts: the chapter computes global and Atlantic MHT with basin masks at 26N, and its explicit unit conversion uses rho 1000 and cp 4000, unlike the closure chapter's 1029 and 3994."
tags: [ecco, tutorial-companion, mht, transport]
generated: { by: claude-code/fable-5, at: 2026-08-30T21:45:00Z }
status: draft
stale_after: 2027-01-04
sources:
  - id: tut-mht
    resource: https://ecco-v4-python-tutorial.readthedocs.io/ECCO_v4_Example_MHT.html
    title: "ECCO v4 Python Tutorial: Compute meridional heat transport"
    author: team:ecco-consortium
---

# The MHT chapter: scope machinery and a constants inconsistency worth knowing

The chapter computes meridional heat transport across chosen latitude
bands, both global and basin-specific, selecting the Atlantic basin
for the RAPID-MOCHA comparison at approximately 26 degrees North with
xgcm-derived masks; results carry units of PW over the 312-month
record.[^tut-mht] The scope discipline this exercises is owned by
[the MHT recipe](../recipes/ecco-mht-26n.md) and
[the basin-scope gotcha](../gotchas/ecco-mht-basin-scope.md) (a
no-mask computation is the full latitude circle, never the
RAPID-comparable number).

**Constants inconsistency, recorded for the upstream conversation.**
The chapter's explicit conversion multiplies transport by
1e-15 x 1000 x 4000, i.e. rho of 1000 and cp of 4000,[^tut-mht] while
the heat-budget closure chapter (and the bundle's recipe, quoting it)
uses rhoconst 1029 and c_p 3994, a difference of roughly 2.5 percent
in the example's absolute PW values. The bundle's anchors come from
`ecco_v4_py.calc_meridional_heat_trsp`, not this example's manual
conversion; no signed concept is contradicted, and the inconsistency
is a candidate note for the tutorial-companion upstream offer.

[^tut-mht]: ECCO v4 Python Tutorial: Compute meridional heat transport
