---
type: convention
title: "Salt, salinity, and freshwater budgets: the tutorial's own checkpoints"
description: "The chapter's acceptance signals: the salt-budget residual summed over depth and time is essentially zero; salinity residuals are larger but small against the tendencies; extensive vs intensive discipline."
tags: [ecco, tutorial-companion, salt-budget]
generated: { by: claude-code/fable-5, at: 2026-08-30T21:45:00Z }
status: draft
stale_after: 2027-01-04
sources:
  - id: tut-salt
    resource: https://ecco-v4-python-tutorial.readthedocs.io/ECCO_v4_Salt_and_salinity_budget.html
    title: "ECCO v4 Python Tutorial: Salt, Salinity and Freshwater Budgets (updated 2024-10-17; Tesdal, Abernathey, Fenty, Boland, Delman)"
    author: team:ecco-consortium
---

# Salt, salinity, and freshwater budgets: the tutorial's own checkpoints

The chapter, built on the Piecuch budget-evaluation note, closes three
related budgets and keeps them distinct: salt and freshwater content
are extensive quantities, salinity is intensive, and the closure
bookkeeping differs between them.[^tut-salt]

**Checkpoints.** The salt-budget residual summed over depth and time
is essentially zero everywhere; the salinity-budget residuals are more
extensive (concentrated on continental shelves and high latitudes)
but, as accumulated residuals, very small compared to the salinity
tendencies.[^tut-salt]

The bundle's authoritative formulation and measured tolerances are
owned by [the salt-budget recipe](../recipes/ecco-salt-budget.md) and
its [attested computation draft](../computations/ecco-salt-budget.md);
the chapter's checkpoints above are the tutorial's own acceptance
signals, not the OSP pass bar. Consistent, no layer-decision issue.

[^tut-salt]: ECCO v4 Python Tutorial: Salt, Salinity and Freshwater Budgets (updated 2024-10-17; Tesdal, Abernathey, Fenty, Boland, Delman)
