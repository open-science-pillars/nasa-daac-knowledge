---
type: dataset-gotcha
spheres: [cryosphere]
title: "NASA Team and Bootstrap concentrations are different retrievals from the same brightness temperatures: they differ where ice is thin, melting or marginal, and a series or a comparison that mixes them reads the algorithm as change"
description: "NSIDC-0051 (NASA Team) and NSIDC-0079 (Bootstrap) cover the same grid, the same sensors and the same dates from different channel combinations, tie-point schemes, weather filters and intercalibration targets. NASA Team uses brightness temperature ratios with fixed per-sensor tie points and is insensitive to surface temperature but underestimates thin ice and loses ice types in spring melt; Bootstrap interpolates between brightness temperature clusters with tie points that change daily, retrieves ice down to 10 percent, is less sensitive to thin ice and layering but sensitive to surface temperature, and returns lower concentrations for thin ice types. Both are least accurate in surface melt and thin ice, and the Sea Ice Index is a NASA Team product; an extent or area from one algorithm set beside one from the other differs by algorithm before it differs by ice."
tags: [sea-ice, nasa-team, bootstrap, nsidc-0051, nsidc-0079, algorithm, tie-points, marginal-ice-zone, melt, thin-ice, g02135]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:30:00Z }
severity: medium
# medium: the two products are separately named and documented, the
# help article tabulates their differences, and the product pages
# name the algorithm, so a reader who looks sees which record they
# hold; the error is a comparison across algorithms rather than a
# hidden corruption, and the quantified differences in the read
# sources are qualitative or bounded at the sensor-transition scale.
dataset: ../datasets/nsidc-0051-sea-ice-concentration.md
status: draft
stale_after: 2027-03-14
sources:
  - id: nt-vs-bt-article
    resource: https://nsidc.org/data/user-resources/help-center/descriptions-and-differences-between-nasa-team-and-bootstrap-algorithms
    title: "NSIDC help article: Descriptions of and differences between the NASA Team and Bootstrap algorithms (channels, ratios versus cluster interpolation, fixed versus daily tie points, weather filters, the strengths, weaknesses and accuracy table, the products using each, and the references)"
  - id: nsidc-0051-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/nsidc-0051-v002-userguide.pdf
    title: "NSIDC-0051 Version 2 user guide: the revised NASA Team algorithm, its channels and weather filters, tie points tuned to minimize extent and area differences at each transition, the accuracy figures, and the care needed in summer melt and new ice"
  - id: nsidc-0051-page
    resource: https://nsidc.org/data/nsidc-0051/versions/2
    title: "NSIDC-0051 product page: strengths and limitations attributed to Comiso and others 1997 (ratios rather than differences, reliability within the pack in cold conditions, higher Antarctic uncertainty from flooded snow) and to Kern and others 2020 and Ivanova and others 2015 (underestimation in melt and thin ice)"
  - id: nsidc-0079-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/nsidc-0079-v004-userguide.pdf
    title: "NSIDC-0079 Version 4 user guide: the AMSR-E Bootstrap algorithm with daily varying tie points, sea_ice_area_fraction scaled by 0.001, calibration to 100 percent thick ice with thinner types retrieved as low as 80 percent, melt pond biases, 5 to 10 percent accuracy, the Version 3 change to intercalibrate on area rather than extent and to retrieve ice at 10 percent, and the sensor date ranges"
  - id: nsidc-0079-page
    resource: https://nsidc.org/data/nsidc-0079/versions/4
    title: "NSIDC-0079 product page: Bootstrap Sea Ice Concentrations from Nimbus-7 SMMR and DMSP SSM/I-SSMIS, Version 4 (DOI 10.5067/X5LG68MH013O; 1 November 1978 to 31 December 2025; Comiso 2023)"
  - id: comiso-1997
    resource: https://doi.org/10.1016/S0034-4257(96)00220-9
    title: "Comiso, Cavalieri, Parkinson and Gloersen, 1997, Passive microwave algorithms for sea ice concentration: A comparison of two techniques, Remote Sensing of Environment 60, 357 to 384 (the comparison paper both guides cite; cited on its Crossref record, which carries no abstract, and the publisher page was not fetched)"
  - id: g02135-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/g02135-v004-userguide.pdf
    title: "Sea Ice Index Version 4 user guide: the Index is based on the NASA Team algorithm, and its extent values are sensitive to the algorithm used and not comparable across studies without care"
  - id: dataset
    resource: ../datasets/nsidc-0051-sea-ice-concentration.md
    title: "This bundle's NSIDC-0051 dataset concept, which lists this trap among the known issues"
  - id: sii-dataset
    resource: ../datasets/sea-ice-index-g02135.md
    title: "This bundle's Sea Ice Index concept, which lists this trap among the known issues"
---

# NASA Team and Bootstrap concentrations are different retrievals from the same brightness temperatures

**Mechanism.** NSIDC archives two sea ice concentration records from
the same SMMR, SSM/I and SSMIS brightness temperatures on the same
25 km grids over the same years, one per algorithm, both developed at
Goddard in the 1980s: NSIDC-0051 from the NASA Team algorithm and
NSIDC-0079 from the Bootstrap algorithm.[^nt-vs-bt-article][^nsidc-0051-user-guide][^nsidc-0079-user-guide]
NASA Team works from the 19 GHz vertical and horizontal and 37 GHz
vertical channels through two ratios, the polarization ratio and the
spectral gradient ratio, whose values cluster at three surface types
(open water and two ice types, first-year and multiyear in the Arctic,
type A and B in the Antarctic) and are mixed linearly between nine
fixed tie points per hemisphere and sensor; its weather filter is a
gradient ratio threshold that in practice removes ice below about
15 percent; using ratios makes it insensitive to surface temperature,
and it has difficulty distinguishing ice types during the spring melt,
underestimates thin ice, and may count grease ice, nilas and new ice
as open water.[^nt-vs-bt-article][^nsidc-0051-user-guide] Bootstrap
works from the 37 GHz horizontal and vertical and 19 GHz vertical
channels by interpolating each observation between the cluster of
100 percent ice and the open-water point in a two-channel scatter
plot, using 37H against 37V inside the pack and 19V against 37V near
the edge where that pair is more sensitive to the ice-water boundary;
its tie points change daily and by hemisphere from the day's own
brightness temperatures, which makes it less sensitive to thin ice and
to snow and ice layering but sensitive to changes in surface
temperature, and its maps show a well identified marginal ice zone
with very high concentrations in the inner pack while the real
gradient near the edge may be steeper than it
retrieves.[^nt-vs-bt-article][^nsidc-0079-user-guide] NSIDC-0079 is
calibrated to 100 percent for thick ice (thicker than about 50 cm) and
returns as little as 80 percent for areas fully covered by thinner ice
types, carries melt pond biases in the Arctic summer, retrieves ice
down to 10 percent since Version 3 where the NASA Team weather filter
cuts near 15 percent, and its Version 3 intercalibrated the SMMR to F8
and F8 to F11 transitions on sea ice area rather than extent, where
NSIDC-0051 tuned its tie points to minimize both extent and area
differences.[^nsidc-0079-user-guide][^nsidc-0051-user-guide] Both
algorithms are least accurate where there is surface melt or thin ice
and near the ice edge where concentrations are low, and both quote
errors under 5 percent for high-concentration winter ice away from
the edge; Comiso and others 1997 is the comparison of the two
techniques that both guides cite, and NSIDC-0051's product page
attributes to it the higher Antarctic uncertainty from flooded snow
and the reliability within the pack in cold
conditions.[^nt-vs-bt-article][^nsidc-0051-page][^comiso-1997] The
Sea Ice Index, NSIDC-0081 and NSIDC-0803 are NASA Team products, and
the Index's guide states that its extent values are sensitive to the
algorithm used.[^nt-vs-bt-article][^g02135-user-guide]

**Wrong-result mode.** A time series that switches from one algorithm
to the other, or a comparison between a NASA Team extent (the Sea Ice
Index) and a Bootstrap extent, changes the retrieval where it means to
observe the ice: the two differ most in the marginal ice zone, over
thin and new ice and in the melt season, which are the regimes where a
summer minimum, a freeze-up date or an ice edge position is
measured.[^nt-vs-bt-article][^nsidc-0079-user-guide] A concentration
difference map between NSIDC-0051 and NSIDC-0079 for one day is
therefore not an error field of either; it is the sum of two
algorithms' regime-dependent behaviour, and the thin-ice
underestimation on one side and the surface temperature sensitivity on
the other point in directions that vary with season and place. An
area series is more exposed than an extent series, because area
carries the concentration inside the edge where the algorithms
disagree on thin and melting ice, while extent depends on the edge
alone; and a Bootstrap extent at its 10 percent floor and a NASA Team
extent at 15 percent are not the same quantity even before the
retrievals differ.[^nsidc-0079-user-guide][^nt-vs-bt-article]

**Correct approach.** A sea ice series names its algorithm and its
product, and stays on it; NSIDC-0079 Version 4 is the Bootstrap record
on the same grids and dates as NSIDC-0051 (1 November 1978 to
31 December 2025, DOI 10.5067/X5LG68MH013O), so an analysis that wants
the Bootstrap view has a full-length record and never needs to splice
one algorithm into the other.[^nsidc-0079-page][^nsidc-0079-user-guide]
A comparison across the two is a statement about algorithm
sensitivity, voiced as such with the regime (winter pack, marginal ice
zone, melt season, thin ice) named, and the difference between them in
a regime is part of the uncertainty of any hemispheric or regional
number from either.[^nt-vs-bt-article] The Sea Ice Index and the
NASA Team records use the 15 percent edge; a Bootstrap extent quoted
beside them states its threshold.[^g02135-user-guide][^nsidc-0079-user-guide]

**Verification.** The help article's algorithm descriptions and its
table of differences, the NSIDC-0051 and NSIDC-0079 guides and product
pages, and the Sea Ice Index guide were read on 2026-09-14; Comiso and
others 1997 is cited on its Crossref record (title, authors, journal,
volume, pages and year verified the same day), the record carries no
abstract, and the publisher page was not read, so the paper is cited
here only for what the NSIDC pages attribute to
it.[^nt-vs-bt-article][^nsidc-0051-user-guide][^nsidc-0051-page][^nsidc-0079-user-guide][^nsidc-0079-page][^g02135-user-guide][^comiso-1997]
No quantitative field-by-field comparison of the two products was
read, so this concept carries no number for their difference beyond
the accuracy figures each guide states. The two dataset concepts list
this trap among their known issues.[^dataset][^sii-dataset]

[^nt-vs-bt-article]: NSIDC help article on the NASA Team and Bootstrap algorithms
[^nsidc-0051-user-guide]: NSIDC-0051 Version 2 user guide, NSIDC
[^nsidc-0051-page]: NSIDC product page, NSIDC-0051 Version 2
[^nsidc-0079-user-guide]: NSIDC-0079 Version 4 user guide, NSIDC
[^nsidc-0079-page]: NSIDC product page, NSIDC-0079 Version 4
[^comiso-1997]: Comiso and others, 1997, Remote Sensing of Environment, doi:10.1016/S0034-4257(96)00220-9
[^g02135-user-guide]: Sea Ice Index Version 4 user guide, NSIDC
[^dataset]: This bundle's NSIDC-0051 dataset concept
[^sii-dataset]: This bundle's Sea Ice Index concept
