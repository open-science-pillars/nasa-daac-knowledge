---
type: recipe
spheres: [cryosphere, hydrosphere]
title: "From a regional GRACE mass change to a sea level equivalent, with its uncertainty"
description: "How a mass change over an ice sheet, a glacier region or a basin, summed at mascon scale from the JPL mascon product, becomes a contribution to global mean sea level in millimeters, and which uncertainty terms travel with it: the formal error, coastal leakage, the GIA model, the low-degree replacements and the inter-mission gap, each stated separately."
tags: [grace, grace-fo, mascons, ice-sheet, sea-level, sea-level-equivalent, mass-balance, budget]
generated: { by: knowledge-seeder/claude, at: 2026-09-13T20:00:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-13T18:39:32Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/125 }
inputs:
  - dataset: ../datasets/grace-fo-mascons.md
  - collections: "TELLUS_GRAC-GRFO_MASCON_CRI_GRID_RL06.3_V4 (the CRI-filtered grid, with its mascon placement and formal-uncertainty files); the unfiltered grid TELLUS_GRAC-GRFO_MASCON_GRID_RL06.3_V4 for the leakage comparison"
  - region: "a mask defined at mascon scale (whole mascons, chosen from the placement file), never at 0.5-degree cell scale; for an ice sheet, the land mascons of the sheet with the CRI partition on the coast"
  - method: "sum the equivalent-water-thickness anomaly over the region's mascons with true mascon areas, convert to gigatonnes, fit a trend with seasonal terms and the gap acknowledged, convert the trend to a sea level equivalent"
expected:
  - quantity: "regional mass change in gigatonnes and its trend in gigatonnes per year"
    statement: "one centimeter of equivalent water thickness over one square kilometer is 1e-5 gigatonnes, so the region's mass in gigatonnes is the sum over its mascons of anomaly (cm) times mascon area (km2) times 1e-5; the trend is the slope of a fit that carries annual and semi-annual terms and treats the 2017 to 2018 gap as a hole"
  - quantity: "sea level equivalent in millimeters of global mean sea level"
    statement: "one millimeter of global mean sea level is the mass of one millimeter of water over the ocean's area: about 362 gigatonnes for an ocean area of 3.62e8 km2 (the 2018 budget rounds to 360), and the recipe states the constant it used, since published budgets differ in the third digit; a mass loss of the region is a sea level rise of that mass divided by that constant"
  - quantity: "numeric anchor"
    statement: "none recorded yet: this recipe is a draft; the attested computation that closes the sea level budget (the sea-level-budget-closure roadmap deliverable, in ocean-science) will record the first anchor and its tolerance"
expected_uncertainty:
  - quantity: "formal error"
    statement: "from the product's per-mascon uncertainty grids, combined with the product's guidance on spatial correlation rather than as independent errors (sqrt(N) under-states it); the floor of the statement, never the whole of it"
  - quantity: "coastal leakage"
    statement: "for an ice sheet, the dominant land-to-ocean leakage runs outward, so the CRI partition and the difference between the CRI and unfiltered grids over the coastal mascons bound it; state it as its own term (the coastal-leakage gotcha)"
  - quantity: "GIA model"
    statement: "the product applies one GIA model; for Antarctica the spread between GIA models is the largest systematic term in the mass trend and is quoted beside the formal error, never folded into it (the GIA gotcha)"
  - quantity: "low-degree replacements and the gap"
    statement: "the degree-1 and C20/C30 series the product applied are named; a window that crosses the 2017 to 2018 gap states how continuity was handled and cites the bridging evidence (the two gotchas)"
sources:
  - id: nasa-tellus-grac-grfo-mascon-cri-grid-rl06
    resource: https://podaac.jpl.nasa.gov/dataset/TELLUS_GRAC-GRFO_MASCON_CRI_GRID_RL06.3_V4
    title: "PO.DAAC collection page: TELLUS_GRAC-GRFO_MASCON_CRI_GRID_RL06.3_V4, with the product documentation, the placement and uncertainty files"
  - id: release-note
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/docs/GRACE_GRACE-FO_ReleaseNotes_JPL_MASCON.txt
    title: "JPL GRACE mascon solution release notes (RL06.3M version 4): what changed between releases, the July 2025 GAD fix, and the placement, land mask and scale factor files unchanged since RL05M"
  - id: watkins-2015
    resource: https://doi.org/10.1002/2014JB011547
    title: "Watkins and others, 2015, Improved methods for observing Earth's time variable mass distribution with GRACE using spherical cap mascons, Journal of Geophysical Research: Solid Earth (the JPL mascon solution and the CRI filter)"
  - id: wiese-2016
    resource: https://doi.org/10.1002/2016WR019344
    title: "Wiese, Landerer and Watkins, 2016, Quantifying and reducing leakage errors in the JPL RL05M GRACE mascon solution, Water Resources Research (leakage and the scale factors, and why the scale factors are for hydrology)"
  - id: wcrp-2018
    resource: https://doi.org/10.5194/essd-10-1551-2018
    title: "WCRP Global Sea Level Budget Group, 2018, Global sea-level budget 1993 to present, Earth System Science Data (the budget terms, the gigatonne to millimeter conversion and the ocean area convention)"
  - id: velicogna-2020
    resource: https://doi.org/10.1029/2020GL087291
    title: "Velicogna and others, 2020, Continuity of ice sheet mass loss in Greenland and Antarctica from the GRACE and GRACE Follow-On missions, Geophysical Research Letters (ice-sheet mass trends across the gap, the reference for a cross-check)"
  - id: leakage
    resource: ../gotchas/grace-coastal-leakage.md
    title: "This bundle's coastal-leakage gotcha"
  - id: gia
    resource: ../gotchas/grace-gia-correction.md
    title: "This bundle's GIA gotcha"
  - id: gap
    resource: ../gotchas/grace-intermission-gap.md
    title: "This bundle's inter-mission gap gotcha"
  - id: low-degree
    resource: ../gotchas/grace-low-degree-replacements.md
    title: "This bundle's degree-1 and C20/C30 gotcha"
status: stable
stale_after: 2027-03-13
---

# From a regional GRACE mass change to a sea level equivalent

**Method.** The mascon product gives a monthly anomaly of equivalent
water thickness on 0.5-degree cells that represent 3-degree mascons;
the information lives at the mascon, so the region is a set of whole
mascons taken from the placement file (unchanged since RL05M, as the
release note states, so a region defined on an earlier release still
holds), and every sum runs over mascons with their true areas, not
over cells.[^watkins-2015][^nasa-tellus-grac-grfo-mascon-cri-grid-rl06][^release-note]
For an ice sheet the region is its land mascons with the CRI partition
along the coast; the scale factors distributed with the product come
from a land hydrology model and are for hydrology, not for ice.[^wiese-2016]

1. **Mass in gigatonnes.** For each month, sum over the region's
   mascons: anomaly in centimeters times mascon area in square
   kilometers times 1e-5. The result is the region's mass anomaly in
   gigatonnes against the product's baseline period, which the
   statement names.
2. **Trend.** Fit the monthly series with a linear term plus annual
   and semi-annual terms, on the epochs read from the files, with the
   2017 to 2018 gap and the earlier missing months left as holes.[^gap]
   The slope is the mass trend in gigatonnes per year; an acceleration
   term is added only for a window that does not cross the gap, or
   with the bridging evidence cited.[^velicogna-2020]
3. **Sea level equivalent.** One millimeter of global mean sea level
   is the mass of a millimeter of water over the ocean's area, about
   362 gigatonnes for 3.62e8 square kilometers, where the 2018 budget
   rounds to 360 gigatonnes per millimeter; the statement names the
   constant it used, because published budgets differ in the third
   digit.[^wcrp-2018] A mass loss contributes a rise of that mass
   divided by the constant.

**Uncertainty, term by term.** The formal error comes from the
product's uncertainty grids, combined per the product's guidance on
correlated mascon errors rather than as independent terms.[^nasa-tellus-grac-grfo-mascon-cri-grid-rl06]
Leakage is bounded by the CRI partition and by the CRI-versus-unfiltered
difference over the coastal mascons.[^leakage] The GIA model is the
largest systematic for Antarctica and is quoted as a spread beside the
formal error.[^gia] The degree-1 and C20/C30 series are named, and
the gap handling is stated.[^low-degree][^gap] The sea level equivalent
carries the same terms scaled by the constant; the constant itself
contributes only in the third digit.

**Cross-check.** The Tellus ice-sheet mass time series distributed
beside the mascon grids are derived from the same solutions and should
reproduce the regional sum to within the leakage term; a disagreement
larger than that is a region-definition error, not a science result.
An independent method (altimetry, or the input-output method) is the
only check on the trend across the gap.[^velicogna-2020]

**Provenance.** Every number quoted from this recipe names the product
version, the baseline period, the GIA model, the low-degree series,
the region definition at mascon scale, the window and the gap
handling. Live checks on 2026-09-13: the CMR record for the collection
(version RL06.3Mv04, DOI 10.5067/TEMSC-3JC634) states 4,551 mascons on
an equal-area 3-degree grid, the CRI partition of the coastal mascons,
the gain factors as an option for sub-mascon hydrology with Wiese and
others 2016 as their reference, and the product as the recommended one
for land-ice applications;[^nasa-tellus-grac-grfo-mascon-cri-grid-rl06]
the release note was read: RL06.3M version 4 differs from RL06.1M
version 3 only in the accelerometer transplant bundle, which touches
the wide-dead-band months (January and February 2023, and July 2023
onward), with the GRACE-FO uncertainty calibration updated for
low-signal land mascons; a July 2025 fix corrected the GAD mass added
back to the ocean part of land/ocean mascons, and only files whose
series extends past March 2025 carry it, so a coastal ice-sheet sum
names the file's last month beside the version;[^release-note] the
WCRP 2018 budget paper was read in full on the journal's site, and the
360 gigatonnes per millimeter figure is its;[^wcrp-2018] every DOI was
verified against the Crossref registry the same day (title, authors,
journal, year) and the Velicogna abstract read there; the Wiley
journal pages sit behind a bot check.

[^nasa-tellus-grac-grfo-mascon-cri-grid-rl06]: PO.DAAC collection page: TELLUS_GRAC-GRFO_MASCON_CRI_GRID_RL06.3_V4
[^watkins-2015]: Watkins and others, 2015, Journal of Geophysical Research: Solid Earth, doi:10.1002/2014JB011547
[^wiese-2016]: Wiese, Landerer and Watkins, 2016, Water Resources Research, doi:10.1002/2016WR019344
[^wcrp-2018]: WCRP Global Sea Level Budget Group, 2018, Earth System Science Data, doi:10.5194/essd-10-1551-2018
[^velicogna-2020]: Velicogna and others, 2020, Geophysical Research Letters, doi:10.1029/2020GL087291
[^leakage]: This bundle's coastal-leakage gotcha
[^gia]: This bundle's GIA gotcha
[^gap]: This bundle's inter-mission gap gotcha
[^low-degree]: This bundle's degree-1 and C20/C30 gotcha
[^release-note]: JPL GRACE mascon solution release notes, RL06.3M version 4
