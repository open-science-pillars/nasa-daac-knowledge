---
type: dead-end
spheres: [hydrosphere]
title: "The discrete divergence identity was tried as the oracle for regional budget closure; it holds for any array"
description: "Summing a box's pointwise convergence and comparing it to the flux through the box rim was proposed as the evidence that a regional heat budget validates itself; the identity is algebra, returned exactly zero on random data, and was retracted in the design note that records it. Regional closure is evidenced by disjoint data paths, two bars, and shipped mutation controls instead."
tags: [ecco, v4r4, budgets, regional, oracle, dead-end]
verified: { by: human:PaulMRamirez, at: 2026-09-06T00:34:32Z }
status: stable
load_bearing: high
eval_case: regional-closure-oracle
generated: { by: claude-code/fable-5, at: 2026-09-05T00:00:00Z }
stale_after: 2027-03-05
subject:
  - /computations/ecco-regional-heat-budget.md
attempt:
  goal: "Validate a regional (control-volume) heat budget without an independent reference, so a box budget could certify itself"
  method: "Show that the sum of pointwise convergence over the box equals the flux through the box rim (the discrete divergence theorem) and treat that agreement as the closure evidence"
failure:
  symptom: "The check passes bit for bit on any array, including random noise; it returned exactly zero on random data"
  cause: "Each interior face is added once and subtracted once from the same stored number, so the identity is algebra about the arrays, not physics about the grid or the implementation"
observations:
  - { at: 2026-08-31, by: claude-code/fable-5, source: design-note }
reopens_if: "Never as an oracle. The identity remains a permission to compute regional convergence from rim faces; a future check that reads the rim from raw face flux variables (a disjoint data path) is a different method, not this one reopened"
sources:
  - id: design-note
    resource: ../../../docs/regional-budget-design.md
    title: "The regional budget design note (2026-08-31): the argument as first drafted, its retraction, the random-data check, and the three requirements that replaced it"
  - id: regional-computation
    resource: ../computations/ecco-regional-heat-budget.md
    title: "The attested regional heat budget that carries the replacement evidence: disjoint data paths, an absolute and a relative bar, and mutation controls in the receipt"
---

# The discrete divergence identity was tried as the oracle for regional budget closure

# Attempted

The goal was a regional heat budget that could certify its own closure
with no independent reference. An early draft of the design note argued
that the discrete divergence theorem supplied that certificate: sum the
pointwise convergence over the box, compute the flux through the rim,
and agreement between the two would show the regional budget
closed.[^design-note]

# Observed

The identity was checked on random data and returned exactly zero. The
design note as landed on 2026-08-31 records the argument, the check, and
the retraction in one place: the agreement holds for any array, so it
says nothing about whether the physical terms are present, the grid is
read correctly, or the implementation is right.[^design-note]

# Why it fails

Every interior face is added once and subtracted once from the same
stored number. What remains is the rim by construction. The identity is
a statement about summation, and a budget missing a real term (the
geothermal flux, say) satisfies it as well as a complete one does. The
cause is understood; there is no open question about why.[^design-note]

# Do instead

The evidence has to cross an independence boundary. The attested
regional budget does it three ways: the boundary term is read from raw
face flux variables at the rim, never derived from the divergence field
the pointwise pipeline already computes; two bars are applied, an
absolute bar in per-volume units and a relative bar against the largest
regional term; and the receipt records that the sabotaged variants were
run and failed, so a pass ships with its demonstrated failure
modes.[^regional-computation]

# Reopens if

Never, as an oracle. What the identity licenses is narrower and still
useful: computing regional convergence from rim faces is a legitimate
substitute for summing cell convergences. A check that reads the rim
from raw face fluxes and compares it to an independently formed
tendency is a different method with its own evidence, not this attempt
retried.[^design-note]

[^design-note]: docs/regional-budget-design.md in open-science-pillars/nasa-daac-knowledge, the section headed "The oracle, corrected"
[^regional-computation]: computations/ecco-regional-heat-budget.md, the attested computation and its attester
