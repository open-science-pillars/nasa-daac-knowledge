---
type: Attested Computation
title: "Regional sea level partition from ECCO (attested, draft)"
description: "Sanctioned regional partition of ECCO sea level into manometric and steric parts with a machine-checked closure residual and convention-bound bookkeeping fields in the receipt."
tags: [ecco, sea-level, steric, manometric, attested, native-grid]
runtime: python
parameters:
  - { name: region, type: string, required: true }
  - { name: period, type: string, required: true }
computation: references/computations/ecco_regional_sea_level.py
executor:
  resource: references/skills/run-sea-level.md
  receipt: [run_id, code_sha256, bound_parameters, ssh_variant, months, cells_evaluated, trend_total_mm_yr, trend_mass_mm_yr, trend_steric_mm_yr, partition_residual_max]
attester:
  resource: references/attesters/sea_level_partition.py
generated: { by: claude-code/fable-5, at: 2026-08-30T22:40:00Z }
status: draft
stale_after: 2027-01-04
sources:
  - id: convention-slbc
    resource: https://github.com/open-science-pillars/ocean-science/blob/main/knowledge/conventions/sea-level-budget-closure.md
    title: "OSP convention: sea level budget closure, a correction-consistency problem first (steward-verified 2026-07-06, v0.1-form)"
    author: human:PaulMRamirez
  - id: gotcha-ssh-ib
    resource: https://github.com/open-science-pillars/ocean-science/blob/main/knowledge/gotchas/ecco-ssh-ib-variants.md
    title: "OSP gotcha: ECCO SSH inverse-barometer variants (steward-verified 2026-07-06, v0.1-form)"
    author: human:PaulMRamirez
  - id: fields-ssh
    resource: ../fields/ecco-v4r4/ssh.md
    title: "Bundle fields concept: sea surface height (stable)"
  - id: fields-obp
    resource: ../fields/ecco-v4r4/obp.md
    title: "Bundle fields concept: ocean bottom pressure (stable)"
  - id: pattern-heat
    resource: ecco-heat-budget.md
    title: "Bundle attested computation: heat budget closure (the pattern; steward-signed stable)"
---

# Regional sea level partition from ECCO (attested, draft)

The sanctioned computation behind receipted sea level briefings: over a
named coastal region and period, partition ECCO's sea level change into
the manometric (ocean-mass) piece and the steric piece, and prove the
partition closed. Version 1 scope is deliberately ECCO-internal: total
from the `SSH` variant, manometric from `OBP`, steric as the density
integral, all from one dynamically consistent product on the native
grid,[^fields-ssh][^fields-obp] so closure is a machine-checkable
identity rather than a cross-product reconciliation. Cross-product
budgets (altimetry, GRACE-FO) are governed by the closure convention's
full corrections table[^convention-slbc] and are OUT of this
computation's attested scope; a briefing may cite those concepts as
context but takes no computed numbers from them in v1.

## Parameters

- `region` (string, required): a named coastal segment or basin from
  the computation's region registry (native-grid mask; the registry is
  part of the sanctioned file, so an unregistered region fails
  attestation rather than improvising a mask).
- `period` (string, required): an inclusive month range within
  1992-01 to 2017-12 (ECCO v4r4's span; briefings state this boundary
  plainly).

## The attester criterion (deterministic, consumer-side)

A run PASSES only when ALL hold:

- **A1, sanctioned code**: `code_sha256` equals the sha256 of the
  computation file.
- **A2, declared parameters only**: `bound_parameters` binds exactly
  `region` and `period`, region in the registry, period within span.
- **A3, convention bookkeeping** (the closure convention's consistency
  requirements as receipt facts[^convention-slbc]): `ssh_variant` is
  stated and is exactly `SSH` (one variant, named, never
  mixed[^gotcha-ssh-ib]); all three trends cover identical `months`
  (matching-period rule); and the regional scope means the Boussinesq
  global-mean correction is out of scope by construction (recorded
  here, not in the receipt).
- **A4, closure**: `partition_residual_max`, the largest absolute
  monthly residual of (total minus mass minus steric) over the region's
  area-mean anomaly series, sits at or below **1.0e-3 m**. The
  tolerance is measured, not assumed (the heat-budget
  precedent[^pattern-heat]): sanctioned fixture run of 2026-08-30
  (us-northeast-coast, 2010-01:2010-12, 102 cells) measured a maximum
  monthly residual of 5.085e-04 m, and the tolerance carries roughly 2x
  headroom over that; the residual is the ECCO-internal wedge between
  the SSH variant and OBP plus model-density steric, and a residual
  above tolerance is a formulation or variant-pairing error, not data
  noise.
- **A5, evaluated substance**: `months` and `cells_evaluated` are
  positive.

## Boundaries

ECCO v4r4 ends at 2017-12: every v1 briefing is a retrospective,
methodological demonstration and says so; the operational cadence
arrives with V4r5. Produced by Open Science Pillars (personal-hat open
source), not a NASA or JPL product.

[^convention-slbc]: OSP convention: sea level budget closure (steward-verified 2026-07-06, v0.1-form)
[^gotcha-ssh-ib]: OSP gotcha: ECCO SSH inverse-barometer variants (steward-verified 2026-07-06, v0.1-form)
[^fields-ssh]: Bundle fields concept: sea surface height (stable)
[^fields-obp]: Bundle fields concept: ocean bottom pressure (stable)
[^pattern-heat]: Bundle attested computation: heat budget closure (the pattern)
