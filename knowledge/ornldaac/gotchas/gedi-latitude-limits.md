---
type: dataset-gotcha
spheres: [biosphere]
title: "GEDI observes only between about 51.6 degrees north and south: the L4A and L4B products carry no footprint or estimated cell for the boreal forest, and the file and record extents (85 degrees in the L4B grid, 56 north in the L4A collection record) are not coverage"
description: "The instrument rides the International Space Station, so its footprints lie within the band the station overflies, nominally 51.6 degrees north and south, with a margin of a fraction of a degree from pointing the lasers up to 40 km either side of the ground track. The L4B GeoTIFFs span the full EASE-Grid 2.0, 85 to -85 degrees, with valid cells nominally within 52; the L4A Version 3 collection record's bounding rectangle reaches 56 north and 53 south, a catalog extent that no source read explains. The high-latitude forests north of the band, more than 30 percent of global forest area by the boreal product's own statement, are covered by separate ICESat-2 products at the same archive that are designed to contribute the northern component from 51.6 degrees north. A global sum from L4B is a temperate and tropical sum, a zero or outside-domain cell north of 52 is not a treeless one, and a search box lying wholly north of about 52 returns nothing."
tags: [gedi, latitude, coverage, iss, boreal, ease-grid, domain, ornldaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T14:02:24Z }
severity: low
# low: the latitude band is on every product page and in every
# abstract, the L4B quality flag marks cells outside the domain, and
# the wrong reading is an omission a reader sees on any map; no eval
# case is required.
dataset: ../datasets/gedi-l4b-gridded-biomass.md
status: draft
stale_after: 2027-03-15
sources:
  - id: ornl-l4b-v2-guide
    resource: https://daac.ornl.gov/GEDI/guides/GEDI_L4B_Gridded_Biomass.html
    title: "ORNL DAAC user guide, GEDI L4B Version 2 (documentation revision 2022-04-26): the user notes on measurements nominally between 51.6 and -51.6 degrees, the instrument rotation of up to 6 degrees pointing the lasers up to 40 km either side of the ground track, the data files spanning 85 to -85 degrees with valid cells nominally within 52, and the quality flag value for cells outside the GEDI domain"
  - id: ornl-l4a-v3-guide
    resource: https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V3.html
    title: "ORNL DAAC user guide, GEDI L4A Version 3 (documentation revision 2026-09-02): the footprints within the band the station observes, nominally 51.6 degrees north and south, and the study area table of 52 to -52"
  - id: cmr-l4a-v3
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C4212593885-ORNL_CLOUD.umm_json
    title: "CMR collection record for GEDI L4A Version 3: the bounding rectangle 56 north to 53 south and the abstract's nominal 51.6 degree band"
  - id: cmr-l4b-v21
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2792577683-ORNL_CLOUD.umm_json
    title: "CMR collection record for GEDI L4B Version 2.1: the bounding rectangle 52 north to 52 south"
  - id: cmr-boreal-v3
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C3904051179-ORNL_CLOUD.umm_json
    title: "CMR collection record for Circumpolar Boreal Forest Aboveground Biomass Density, Version 3 (Boreal_AGB_Density_ICESat2_V3_2437, DOI 10.3334/ORNLDAAC/2437): the abstract stating that the high northern latitude forests account for more than 30 percent of global forest area, that the product provides the northern component to which GEDI contributes the temperate and tropical portions, and that it is intended to contribute northward from 51.6 degrees north"
  - id: crossref-patterson-2019
    resource: https://api.crossref.org/works/10.1088/1748-9326/ab18df
    title: "Crossref registry record for Patterson and others 2019, Environmental Research Letters 14, 065007: the abstract's statement that the 1 km grid covers the latitudes overflown by the station, 51.6 degrees south to 51.6 degrees north"
  - id: dataset
    resource: ../datasets/gedi-l4b-gridded-biomass.md
    title: "This bundle's GEDI L4B dataset concept, which lists this trap among the known issues"
  - id: l4a-dataset
    resource: ../datasets/gedi-l4a-footprint-biomass.md
    title: "This bundle's GEDI L4A dataset concept, which lists this trap among the known issues"
---

# GEDI observes only between about 51.6 degrees north and south

**Mechanism.** GEDI is attached to the International Space Station
and collects data globally between 51.6 degrees north and 51.6
degrees south, the latitudes the station overflies; the L4A
footprints are located within that band, nominally, and the L4B grid
covers the same latitudes.[^ornl-l4b-v2-guide][^ornl-l4a-v3-guide][^crossref-patterson-2019]
The band has a small margin: the instrument can be rotated on its
mount by up to 6 degrees, pointing the lasers up to 40 km on either
side of the station's ground track, a fraction of a degree of
latitude, so the exact coverage varies slightly by
orbit.[^ornl-l4b-v2-guide] The L4A guide's study area table gives 52
to -52 and the L4B collection record 52 north to 52 south; the L4A
Version 3 collection record's bounding rectangle reaches 56 north and
53 south, a catalog extent that no source read
explains.[^ornl-l4a-v3-guide][^cmr-l4b-v21][^cmr-l4a-v3]
The L4B GeoTIFFs are cut to the full EASE-Grid 2.0, 85 to -85
degrees of latitude, with cells holding valid values nominally within
52 to -52, and the quality flag layer's value 0 marks cells outside
the GEDI domain.[^ornl-l4b-v2-guide] The forests north of the band
are the subject of separate products at the same archive: the
circumpolar boreal biomass product from ICESat-2 states that high
northern latitude forests account for more than 30 percent of global
forest area, that it provides the northern component of global forest
structure estimates to which GEDI contributes the temperate and
tropical portions, and that it is intended to contribute northward
from 51.6 degrees north.[^cmr-boreal-v3]

**Wrong-result mode.** A global forest biomass total from L4B is a
total for the temperate and tropical band, short of the boreal
forest, and a comparison with a global map or inventory that includes
Canada, Fennoscandia and Siberia compares different
areas.[^ornl-l4b-v2-guide][^cmr-boreal-v3] A cell north of 52
degrees in the L4B mean layer holds zero or no data, and read as a
biomass of zero it turns the domain edge into a treeless line; the
quality flag distinguishes outside-domain cells from estimated
ones.[^ornl-l4b-v2-guide] A search box lying wholly north of about
52 degrees, which the L4A record's bounding rectangle permits,
returns nothing, and a study area in the boreal zone has no GEDI
biomass at all; a box whose south edge lies below 52 returns
everything inside the band and nothing above it, so the empty north
shows only as an absence.[^cmr-l4a-v3][^ornl-l4b-v2-guide]

**Correct approach.** The GEDI products cover the band the station
overflies, and a global statement built on them is stated for that
band; the boreal component comes from the ICESat-2 products designed
for it, and a combined estimate names both sources and their
different methods.[^ornl-l4b-v2-guide][^cmr-boreal-v3] In L4B the
quality flag, not the mean layer, says whether a cell is outside the
domain, on land without an estimate, or estimated.[^ornl-l4b-v2-guide]

**Verification.** The band, the pointing margin and the grid extent
are in the L4B guide's user notes, the bounding rectangles are in the
two CMR records, and the boreal product's abstract is in its CMR
record.[^ornl-l4b-v2-guide][^cmr-l4a-v3][^cmr-l4b-v21][^cmr-boreal-v3]
On the L4B files the check is the QF layer, 0 poleward of the band.
No GEDI file was opened for this concept. Both dataset concepts list
this trap among the known issues.[^dataset][^l4a-dataset]

[^ornl-l4b-v2-guide]: ORNL DAAC user guide, GEDI L4B Version 2, revision 2022-04-26, read 2026-09-15
[^ornl-l4a-v3-guide]: ORNL DAAC user guide, GEDI L4A Version 3, revision 2026-09-02, read 2026-09-15
[^cmr-l4a-v3]: CMR collection C4212593885-ORNL_CLOUD, read 2026-09-15
[^cmr-l4b-v21]: CMR collection C2792577683-ORNL_CLOUD, read 2026-09-15
[^cmr-boreal-v3]: CMR collection C3904051179-ORNL_CLOUD, read 2026-09-15
[^crossref-patterson-2019]: Crossref record for doi:10.1088/1748-9326/ab18df, read 2026-09-15
[^dataset]: This bundle's GEDI L4B dataset concept
[^l4a-dataset]: This bundle's GEDI L4A dataset concept
