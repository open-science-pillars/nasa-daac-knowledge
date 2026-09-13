---
type: dataset
spheres: [hydrosphere, geosphere, cryosphere]
title: GRACE/GRACE-FO JPL mascon solutions
description: "Monthly mass anomaly (equivalent water thickness) on 3-degree mascons, RL06.3 version 4; formal per-mascon uncertainty grids ship with the data."
tags: [grace, grace-fo, mascons, mass, podaac]
generated: { by: knowledge-seeder/claude, at: 2026-07-06T00:00:00Z }
resource: https://podaac.jpl.nasa.gov/dataset/TELLUS_GRAC-GRFO_MASCON_CRI_GRID_RL06.3_V4
version: "JPL RL06.3 version 4 (RL06.3Mv04, DOI 10.5067/TEMSC-3JC634), CMR-verified 2026-07-04 and again 2026-09-13 with one granule covering 2002-04-16 through 2026-07-16; CRI-filtered grid (TELLUS_GRAC-GRFO_MASCON_CRI_GRID_RL06.3_V4) and unfiltered grid (TELLUS_GRAC-GRFO_MASCON_GRID_RL06.3_V4) both live"
sources:
  - id: release-note
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/docs/GRACE_GRACE-FO_ReleaseNotes_JPL_MASCON.txt
    title: "JPL GRACE mascon solution release notes (RL06.3M version 4): the GIA model, the low-degree series and the changes between releases"
  - id: months-rl06
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/docs/GRACE_GRACE-FO_Months_RL06.csv
    title: "GRACE and GRACE-FO RL06 month list (PO.DAAC): the solutions that exist and the months with no coverage"
status: stable
verified:
  - { by: human:PaulMRamirez, at: 2026-07-04T00:00:00Z }
  - { by: human:PaulMRamirez, at: 2026-09-13T18:39:32Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/125 }
stale_after: 2027-01-04
---

# GRACE/GRACE-FO JPL mascon solutions

**Identity.** Monthly surface mass anomalies (expressed as equivalent
water thickness) estimated directly on 4,551 equal-area 3-degree spherical-cap mass
concentration blocks (mascons) from GRACE (2002-2017) and GRACE-FO
(2018-present) inter-satellite ranging; the JPL solution line, RL06.3
v4 as of the verification date. Distributed as 0.5-degree grids that
REPRESENT the 3-degree mascons: the native information scale is the
mascon, not the grid cell. The CRI-filtered variant separates
coastline-straddling mascons into land and ocean parts; derived
Tellus time series (ocean mass, Greenland, Antarctica) are separate
collections.

**Structure.** Monthly fields of water-equivalent thickness anomaly
against a stated baseline period, with scale/gain guidance and the
uncertainty grids below; a GIA correction is already applied to the
standard product: ICE-6G_D (Peltier and others 2018) since RL06M,
removed before the CRI filter and from the released fields, referenced
to the 2008-01-01 epoch of the static field since the 2020 fix; the
C20 and C30 terms come from TN-14 version 3 and the degree-1 term from
JPL's own mascon-consistent geocenter, per the release note.[^release-note]
Month gaps exist: the product's month list marks July 2017 through May
2018 and August and September 2018 with no coverage, and twenty earlier
months missing, mostly the battery-management months from 2011
on.[^months-rl06]

**Land-ice use.** The mascon product is the standard GRACE input for
ice-sheet and glacier mass balance and for the mass term of the sea
level budget: a region is a set of whole mascons, its mass is the sum
of anomaly times mascon area, and the trend converts to a sea level
equivalent at about 362 gigatonnes per millimeter (the recipe
[grace-mass-to-sea-level](../recipes/grace-mass-to-sea-level.md)
carries the steps and every uncertainty term). Units are centimeters
of equivalent water thickness against the product's baseline period,
which the product documentation names, as it names the applied GIA
model and the degree-1 and C20/C30 series; every mass statement
repeats those four names. The scale factors distributed with the CRI
grid come from a land hydrology model and are not applied over ice.

## Uncertainty

- **Formal per-mascon uncertainty grids ship with the product**:
  monthly 1-sigma estimates per mascon. They capture solution noise,
  scale with latitude and month, and are the quantitative floor for
  any mass statement.
- The formal errors do NOT include the two dominant systematic terms:
  coastal leakage (its own gotcha) and the GIA model choice (its own
  gotcha); both exceed the formal errors regionally.
- Averaging mascons reduces noise slower than white-noise intuition
  suggests (mascon errors are spatially correlated); basin averages
  quote the product's guidance, not sqrt(N).
- **Native resolution is the mascon, not the grid cell** (order 300 km
  spherical caps): a basin whose area approaches or falls below the
  mascon scale is resolution- and leakage-dominated, so state the
  resolution and leakage caveats before delivering its TWS series.

## Known issues

- [grace-coastal-leakage](../gotchas/grace-coastal-leakage.md)
- [grace-gia-correction](../gotchas/grace-gia-correction.md)
- [grace-intermission-gap](../gotchas/grace-intermission-gap.md): the
  2017 to 2018 inter-mission gap breaks trend and acceleration fits that
  treat the record as continuous.
- [grace-low-degree-replacements](../gotchas/grace-low-degree-replacements.md):
  the degree-1 and C20/C30 series the product applies move large-scale
  trends; nothing is re-applied.

[^release-note]: JPL GRACE mascon solution release notes, RL06.3M version 4
[^months-rl06]: GRACE and GRACE-FO RL06 month list, PO.DAAC
