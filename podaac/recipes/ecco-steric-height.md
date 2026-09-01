---
type: recipe
title: "Steric height and its trend from ECCO v4r4 density"
description: "Column-integrated steric height from RHOAnoma on the native grid: the hFac weighting, the region registry, and the Boussinesq limit that makes a global mean a diagnostic, not a sea level."
tags: [ecco, steric-height, sea-level, recipe, native-grid]
inputs: "ECCO_L4_DENS_STRAT_PRESS_LLC0090GRID_MONTHLY_V4R4 (RHOAnoma) for the chosen months; the geometry granule (rA, drF, hFacC, maskC)"
expected: "Reference region us-northeast-coast, 2010-01 through 2010-12 (measured 2026-09-01): steric trend +135.7772 mm per year over 102 wet columns, matching the attested sea-level partition's signed receipt to four decimals; regional area-mean steric height near -19.6 m"
expected_uncertainty: "Any area-mean outside -60 to 0 m is suspect. A GLOBAL mean steric height is a Boussinesq diagnostic: the model conserves volume, not mass, so global steric change does not translate to modeled sea-surface rise and the attested form refuses to report it without that caveat"
generated: { by: claude-code/fable-5, at: 2026-09-01T05:35:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-01T05:53:24Z }
status: stable
stale_after: 2027-01-04
sources:
  - id: attested-computation
    resource: ../computations/ecco-steric-height.md
    title: "The attested computation this recipe walks: contract, cross-computation anchor, reference run"
  - id: sea-level-partition
    resource: ../computations/ecco-regional-sea-level.md
    title: "The attested sea-level partition whose steric term anchors the reference trend"
---

# Steric height and its trend from ECCO v4r4 density

Steric height is the sea-level contribution of density change: for
each column, minus one over rho0 times the vertical sum of RHOAnoma
times hFacC times drF, with hFacC doing the same partial-cell and
land-mask work it does in every native-grid integral. Area-weight by
rA over the region, fit a linear trend across months, and report mm
per year.[^attested-computation]

The number to reproduce: over the US northeast coast box for 2010 the
trend is +135.7772 mm per year, and the attested sea-level partition,
computed from different code, records the same value in its signed
receipt to four decimals.[^sea-level-partition] That agreement is the
recipe's anchor: two independent routes to the same physical quantity
through the same bundle. The limit to respect: globally, ECCO is
Boussinesq (volume-conserving), so a global-mean steric change is a
water-mass diagnostic, not a modeled sea-surface rise; the attested
form carries that caveat as a required receipt field.[^attested-computation]

[^attested-computation]: computations/ecco-steric-height.md, contract and reference run
[^sea-level-partition]: computations/ecco-regional-sea-level.md, the signed steric trend
