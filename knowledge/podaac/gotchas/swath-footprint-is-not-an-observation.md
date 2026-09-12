---
type: dataset-gotcha
spheres: [hydrosphere]
title: "A catalogue match on a swath granule is not an observation of your place"
description: "A spatial search returns granules whose footprint intersects the query box, and for a wide-swath product a footprint spans continents. Measured over the Tulare Lake bed: of the first eight SWOT LakeSP granules a bounding-box search returned for late July and August 2023, only two contain any lake feature inside the box, and both are the same pass. The other six hold thousands of features elsewhere. A date taken from the search rather than from the file is a date on which nothing was observed."
tags: [swot, lakesp, cmr, search, swath, footprint, observation, podaac]
generated: { by: claude-code/fable-5, at: 2026-09-07T20:15:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-08T04:19:56Z }
severity: high
dataset: ../datasets/swot-karin.md
eval_case: swath-footprint-is-not-an-observation
status: stable
stale_after: 2027-03-07
sources:
  - id: record
    resource: https://github.com/open-science-pillars/marketplace/issues/72
    title: "The event reconstruction record: the granule-by-granule check over the Tulare box, with the counts inside and outside"
  - id: karin
    resource: ../datasets/swot-karin.md
    title: "This bundle's SWOT KaRIn concept: the swath geometry that makes a granule footprint continental"
---

# A catalogue match on a swath granule is not an observation

**Mechanism.** A spatial search asks whether a granule's footprint
intersects a box. For a wide-swath instrument on a repeating orbit,
one granule's footprint is a long strip: the SWOT LakeSP granules
checked here span from about 28 to 55 degrees north and from 121 to
111 degrees west in a single file. Any query box inside that strip
matches, whether or not the instrument produced a feature there.

For a vector product the distinction is sharper than for a raster
one. A LakeSP granule holds lake polygons, and a lake appears only if
it was observed and matched: a granule can hold several thousand
features, all of them hundreds of kilometres from the query box, and
still be a legitimate match for it.

**Measured (2026-09-07).** Over the Tulare Lake bed (lon -120.4 to
-119.3, lat 35.8 to 36.6), searching the LakeSP D collection for
2023-07-25 to 2023-08-20 returned 13 observation granules. Of the
first eight opened:[^record]

| Granule pass | Features in the file | Features inside the box |
|---|---|---|
| cycle 001 pass 190, 2023-07-27 | 1,563 | 0 |
| cycle 001 pass 218, 2023-07-28 | 3,594 | 0 |
| cycle 001 pass 246, 2023-07-29 | 4,314 | 0 |
| cycle 001 pass 261, 2023-07-30 | 3,228 | **22** |

Two of the eight hold features inside the box, and both are the same
pass on the same day. The first date the search offers is 2023-07-27;
the first date the lake was observed is **2023-07-30**.

**Wrong-result mode.** A timeline that takes its first date from the
search begins three days before the instrument saw the place, and a
gap analysis built the same way counts revisits that did not happen.
Worse, the error is invisible in the direction that matters: a reader
who opens the file finds it full of data, just not of this place, and
a workflow that computes "number of observations in the window" from
the search returns a number several times too large. Where the
timeline is used to say when a feature was first or last seen, the
answer is wrong by whole passes.

**Correct approach.** Treat the search as a candidate list and the
file as the evidence. Open each granule, filter to the region by the
feature geometry, and count what is actually there; report the dates
on which features were found, not the dates the search returned. Where
a workflow reports coverage, it reports both numbers and the
difference between them, because the difference is itself a fact about
the product's sampling. For a raster swath product the same rule
applies with a different test: read the valid-data mask inside the
region rather than trusting the footprint.

**Verification.** Run a bounding-box search over a small region for a
window of a few weeks, open every granule returned, and count the
features whose geometry falls inside the region. Confirm that the
count of granules with any feature inside is smaller than the count
returned, and that the first such date is later than the search's
first date.

[^record]: the event reconstruction record, open-science-pillars/marketplace issue 72
[^karin]: this bundle's SWOT KaRIn concept
