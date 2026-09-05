---
type: convention
title: "Volume and sea level budget: the tutorial's own checkpoints"
description: "The ETAN budget chapter's acceptance signals: tendency agreement within 1e-6 m, residuals below 1e-11 m/s, and the ETAN caveats; a different identity from the interior volume budget, stated precisely."
tags: [ecco, tutorial-companion, volume-budget, sea-level]
generated: { by: claude-code/fable-5, at: 2026-08-30T21:45:00Z }
status: draft
stale_after: 2027-01-04
sources:
  - id: tut-volume
    resource: https://ecco-v4-python-tutorial.readthedocs.io/ECCO_v4_Volume_budget_closure.html
    title: "ECCO v4 Python Tutorial: ECCOv4 Global Volume and Sea Level Budget (updated 2025-08-21)"
    author: team:ecco-consortium
---

# Volume and sea level budget: the tutorial's own checkpoints

The chapter closes the model sea level anomaly (`ETAN`) budget in the
z* coordinate system, drawing on the Piecuch budget-evaluation
document, and needs about 7 GB of memory.[^tut-volume]

**Checkpoints.** The two routes to the time-mean tendency agree to
within 10^-6 meters ("these are the same to within 10^-6 meters!"),
and almost all residuals sit below 10^-11 m/s; the chapter closes the
ETAN budget using `UVELMASS`, `VVELMASS`, `WVELMASS`, and
`oceFWflx`.[^tut-volume]

**Identity discipline, so nothing reads as a contradiction.** The
chapter's identity is the SEA LEVEL budget, where `oceFWflx` appears
as an explicit term; the bundle's
[interior volume budget](../recipes/ecco-volume-budget.md) is a
different identity that closes on transport convergence alone, because
`WVELMASS` at the surface already carries the freshwater flux and
adding `oceFWflx` there double-counts. Both are true of the same
model; the chapter itself states that the surface vertical velocity
equals `oceFWflx` in the time-mean, which is the same fact seen from
the other side.[^tut-volume]

**ETAN caveats.** `ETAN` is not comparable to observed sea level;
among the chapter's reasons, floating sea-ice displaces a volume of
seawater equal to its weight, so ETAN follows ice growth and
melt.[^tut-volume]

**Eval fixture.** Extracted to the ecco-agent-evals repository at
`fixtures/tutorial/volume-budget-checkpoints.yaml`, chapter cited.

[^tut-volume]: ECCO v4 Python Tutorial: ECCOv4 Global Volume and Sea Level Budget (updated 2025-08-21)
