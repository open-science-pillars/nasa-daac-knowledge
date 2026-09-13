---
type: dataset-gotcha
spheres: [cryosphere, hydrosphere, geosphere]
title: "Degree-1 and C20/C30 replacements: large-scale mass trends from GRACE rest on terms the satellites do not measure, already substituted in the mascon product"
description: "GRACE senses no degree-1 (geocenter) term and its C20 oblateness term is unreliable, so the mascon product substitutes a modeled geocenter series and satellite-laser-ranging values for C20 (and C30 in the later record). The substitutions move ice-sheet and ocean-mass trends by amounts comparable to the formal errors. Comparing a mascon trend with a spherical-harmonic result that used different substitutions, or applying the substitutions again, attributes the difference to the ice or the ocean."
tags: [grace, grace-fo, degree-1, geocenter, c20, c30, oblateness, tn-13, tn-14, trends, mascons]
generated: { by: knowledge-seeder/claude, at: 2026-09-13T20:00:00Z }
verified:
  - { by: human:PaulMRamirez, at: 2026-09-13T18:39:32Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/125 }
  - { by: human:PaulMRamirez, at: 2026-09-13T18:50:46Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/126 }
severity: medium
# medium, as with the GIA gotcha: the substitutions are documented
# product behavior and bite through comparison inconsistency or
# re-application rather than through silently wrong single-product
# statistics; no eval case is required at this severity.
dataset: ../datasets/grace-fo-mascons.md
status: stable
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
  - id: podaac-grace-docs
    resource: https://podaac.jpl.nasa.gov/gravity/grace-documentation
    title: "PO.DAAC GRACE documentation index: the technical notes, including TN-13 (degree-1 geocenter coefficients, one per processing center) and TN-14 (NASA GSFC satellite laser ranging C20 and C30)"
  - id: tn-13-jpl
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/open/docs/TN-13_GEOC_JPL_RL0601.txt
    title: "GRACE Technical Note 13c: degree-1 (geocenter) gravity coefficients from JPL RL06"
  - id: tn-14
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/open/docs/TN-14_C30_C20_GSFC_SLR.txt
    title: "GRACE Technical Note 14: NASA GSFC SLR C20 and C30 solutions"
  - id: release-note
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/docs/GRACE_GRACE-FO_ReleaseNotes_JPL_MASCON.txt
    title: "JPL GRACE mascon solution release notes (RL06.3M version 4): which C20, C30 and geocenter series each release applied"
  - id: loomis-2020
    resource: https://doi.org/10.1029/2019GL085488
    title: "Loomis and others, 2020, Replacing GRACE/GRACE-FO C30 with satellite laser ranging: impacts on Antarctic Ice Sheet mass change, Geophysical Research Letters (the citation TN-14 names)"
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
laser ranging, with C30 also replaced once either mission flew
without two working accelerometers (GRACE from October 2016, GRACE-FO
from the start), which is when the missions observe C30 poorly;
laser-ranging C30 is usable from 2012, when LARES
launched.[^sun-2016][^loomis-2019][^loomis-2020]
The mascon product arrives with these substitutions already applied.
For RL06.3M version 4 the release note states them: C20 and C30 from
TN-14 version 3 across the whole series (C20 from TN-14 since the 2020
release, TN-11 before it; version 3 replacing version 2 in December
2023), and a geocenter computed at JPL by the Swenson 2008 method with
the mascon field itself as the background gravity field, consistent
with the TN-13 processing standard and self-consistent with TN-14
version 3, so the product's degree-1 series is its own, not the TN-13
file verbatim; degrees 2 and 3 are no longer taken from the spherical
harmonic solution since RL06M, because the solution includes onboard
GPS.[^release-note] TN-13 itself is the degree-1 series for the
spherical harmonic products, computed with C20 already replaced from
TN-14 version 3 and GIA removed with ICE-6G_D, with C30 replaced in
GRACE-FO from June 2019.[^tn-13-jpl] TN-14 version 3 carries C20 from
April 2002 and C30 from March 2012 onward, and names Loomis and others
2020 as its citation.[^tn-14][^loomis-2020]

**Wrong-result mode.** The substituted terms project onto the largest
scales, which is exactly where ice-sheet mass balance and global ocean
mass live, so the choice of series moves those trends: the GSFC C20
series against the earlier CSR TN-11 changes the Antarctic and
Greenland mass trends by 15.4 and 3.5 gigatonnes per year and the sea
level budget by 0.08 millimeters per year, amounts comparable to the
formal errors.[^loomis-2019]
Two traps follow. Comparing a mascon trend with a spherical-harmonic
result whose author applied a different geocenter or C20 series (or
none) attributes the difference to the ice sheet or the ocean.
Applying a technical-note replacement again to the mascon product,
because a spherical-harmonic recipe says to, corrects twice.

**Correct approach.** Any large-scale trend from the mascon product
names the degree-1 and C20/C30 series the product applied, read from
the release note at analysis time (for RL06.3M version 4: TN-14
version 3 for C20 and C30, and the JPL mascon-consistent geocenter),
beside the GIA model.[^release-note][^gia]
Cross-product and literature comparisons align those choices or quote
the spread as a systematic term beside the formal error. Nothing is
re-applied to a product that already carries it; the replacements
belong to the spherical-harmonic workflow, not to this one.

**Verification.** The product documentation lists the applied series
(link above).[^nasa-tellus-grac-grfo-mascon-cri-grid-rl06] The two
papers document the series and the trend sensitivity.[^sun-2016][^loomis-2019]
The double-application failure mode follows from the product being
pre-corrected, as with GIA.[^gia] Live checks on 2026-09-13: the
PO.DAAC documentation index lists the technical notes by name, TN-13
for the degree-1 coefficients (one file per processing center) and
TN-14 for the GSFC laser-ranging C20 and C30 solutions;[^podaac-grace-docs]
both files were read (TN-13 JPL RL0601, updated August 2024 with its
last point in May 2024; TN-14 version 3, created 31 August 2026,
spanning April 2002 through June 2026);[^tn-13-jpl][^tn-14] the
product release note was read and is the source for which series this
product applies;[^release-note] the four papers' records were
verified against the Crossref registry the same day (title, authors,
journal, year) and their abstracts read there, which is where the
trend changes and the accelerometer dates above come from; the journal
pages themselves sit behind a bot check.

[^nasa-tellus-grac-grfo-mascon-cri-grid-rl06]: PO.DAAC collection page: TELLUS_GRAC-GRFO_MASCON_CRI_GRID_RL06.3_V4
[^grace-tellus]: GRACE Tellus project site: the technical notes on the replacements
[^sun-2016]: Sun, Riva and Ditmar, 2016, Journal of Geophysical Research: Solid Earth, doi:10.1002/2016JB013073
[^loomis-2019]: Loomis, Rachlin and Luthcke, 2019, Geophysical Research Letters, doi:10.1029/2019GL082929
[^podaac-grace-docs]: PO.DAAC GRACE documentation index
[^tn-13-jpl]: GRACE Technical Note 13c, JPL degree-1 coefficients
[^tn-14]: GRACE Technical Note 14, GSFC SLR C20 and C30
[^gia]: This bundle's GIA gotcha
[^release-note]: JPL GRACE mascon solution release notes, RL06.3M version 4
[^loomis-2020]: Loomis and others, 2020, Geophysical Research Letters, doi:10.1029/2019GL085488
