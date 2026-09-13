---
type: dataset-gotcha
spheres: [cryosphere]
title: "Ice sheet boundaries and drainage basins differ by definition: a per-basin number names the basin set it used"
description: "Two basin schemes are in common use for the ice sheets: the GSFC drainage systems of Zwally and others (2012), drawn on ICESat surface slopes, and the IMBIE basins of Rignot and others, drawn on velocity and archived at NSIDC as NSIDC-0709. They divide the ice sheets differently: under the two definitions the IMBIE 2018 assessment gives West Antarctica areas that differ by close to 300,000 square kilometres. A per-basin height change, volume change or discharge that does not name its basin set, its grounded or floating scope and its ice sheet boundary is not comparable with one computed on the other."
tags: [icesat2, atl15, its-live, drainage-basins, imbie, zwally, rignot, ice-sheet-boundary, grounding-line, greenland, antarctica]
generated: { by: knowledge-seeder/claude, at: 2026-09-13T20:30:00Z }
severity: medium
# medium: the basin sets are documented and the trap is a comparison
# inconsistency, not a silently wrong single-product statistic; no
# eval case is required.
dataset: ../datasets/icesat2-atl15.md
status: draft
stale_after: 2027-03-13
sources:
  - id: gsfc-drainage-systems
    resource: https://earth.gsfc.nasa.gov/cryo/data/polar-altimetry/antarctic-and-greenland-drainage-systems
    title: "Zwally, Giovinetto, Beckley and Saba, 2012, Antarctic and Greenland Drainage Systems, GSFC Cryospheric Sciences Laboratory: the 27 Antarctic systems and the Greenland systems drawn on ICESat DEM slopes, the East and West Antarctic allocation, and the note that users adjust area statistics to their own junction points"
  - id: nsidc-0709-page
    resource: https://nsidc.org/data/nsidc-0709/versions/2
    title: "NSIDC product page: MEaSUREs Antarctic Boundaries for IPY 2007-2009 from Satellite Radar, Version 2 (Mouginot, Scheuchl and Rignot 2017, DOI 10.5067/AXE4121732AD): ice shelves, basins, grounding line and coastline"
  - id: nsidc-0709-user-guide
    resource: https://nsidc.org/sites/default/files/nsidc-0709-v002-userguide.pdf
    title: "NSIDC-0709 Version 2 user guide: Basins_IMBIE_Antarctica_v02 (the IMBIE 2016 Rignot basins) and the refined Basins_Antarctica_v02, both consistent with each other, drawn on historical nomenclature plus the DEM and velocity"
  - id: imbie-2018
    resource: https://doi.org/10.1038/s41586-018-0179-y
    title: "The IMBIE team (Shepherd and others), 2018, Mass balance of the Antarctic Ice Sheet from 1992 to 2017, Nature 558, 219 to 222: Extended Data Fig. 2 gives the basin areas under the Zwally and the Rignot definitions"
  - id: imbie-2019
    resource: https://doi.org/10.1038/s41586-019-1855-2
    title: "The IMBIE team (Shepherd and others), 2019, Mass balance of the Greenland Ice Sheet from 1992 to 2018, Nature 579, 233 to 239: Extended Data Fig. 2 shows the Greenland basins used under two definitions"
  - id: rignot-2011
    resource: https://doi.org/10.1126/science.1208336
    title: "Rignot, Mouginot and Scheuchl, 2011, Ice Flow of the Antarctic Ice Sheet, Science 333, 1427 to 1430: the velocity map on which the IMBIE basins are drawn"
  - id: atl14-15-atbd
    resource: https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl14_atl15_atbd_v005.pdf
    title: "Smith and others, ICESat-2 ATBD for ATL14 and ATL15, release 005: the ice masks the product uses (BedMachine v3 in Greenland, a time-varying mask in Antarctica) and the ice_area field, which define the product's own extent"
  - id: dataset
    resource: ../datasets/icesat2-atl15.md
    title: "This bundle's ATL15 dataset concept, which lists this trap among the known issues"
  - id: velocity-dataset
    resource: ../datasets/its-live-ice-velocity.md
    title: "This bundle's velocity mosaic concept, which lists this trap among the known issues"
---

# Ice sheet boundaries and drainage basins differ by definition

**Mechanism.** A regional number from ATL15 or a velocity mosaic is a
sum or an integral over a region, and the region is a choice. The GSFC
drainage systems (Zwally and others 2012) divide Antarctica into 27
systems drawn on downslope vectors from an ICESat DEM, allocate West
Antarctica as systems 18 to 23 and 1, East Antarctica as 2 to 17 and
the Peninsula as 24 to 27, place parts of the Ronne, Filchner and
Ross ice shelves in East Antarctica, draw the divides to prominent
coastline points rather than to grounding line junctions, and tell
users to adjust area and other statistics if different junction points
are chosen; Greenland is divided the same way on a 1 km ICESat DEM
with its ice sheet boundary from a surface type
map.[^gsfc-drainage-systems] The IMBIE basins (Rignot and others)
are drawn on the InSAR velocity map of Antarctica and are archived at
NSIDC in NSIDC-0709 as Basins_IMBIE_Antarctica_v02, the basins used
for the IMBIE 2016 exercise, beside a refined and consistent set,
Basins_Antarctica_v02, with the ice shelves, the grounding line and
the coastline as separate layers.[^nsidc-0709-page][^nsidc-0709-user-guide][^rignot-2011]
The two schemes are not the same partition. The IMBIE 2018 Antarctic
assessment used both and reports the areas: under the Zwally
definition the Peninsula, West and East Antarctica cover 227,725,
1,748,200 and 9,909,800 square kilometres, and under the Rignot
definition 232,950, 2,039,525 and 9,620,225 square kilometres, so the
West Antarctic sector differs by close to 300,000 square kilometres
between them, moved to or from East Antarctica.[^imbie-2018] The
Greenland assessment likewise shows its basins under two definitions
and reports by the regions NW, CW, SW, SE, NE and NO.[^imbie-2019]
ATL15 has an extent of its own as well: its ice_area field follows the
input ice mask (BedMachine v3 in Greenland, a time-varying mask in
Antarctica) and drops cells whose surface falls below the geoid, and
grounded and floating ice are both in the product, so a basin
polygon clipped or not clipped at the grounding line changes what a
sum contains.[^atl14-15-atbd]

**Wrong-result mode.** A West Antarctic volume change from ATL15 on
the Zwally systems compared with a West Antarctic mass change
published on the Rignot basins compares two regions whose areas
differ by about a sixth, and the difference between the numbers is
read as a disagreement between the observing systems or as a change
in the ice. A per-basin discharge from a velocity mosaic through
gates drawn on one basin set, combined with a surface mass balance
integrated over the other, produces a mass budget for no region at
all. A total that sums ATL15 over a basin polygon without clipping to
grounded ice includes ice shelf height change, which carries no sea
level mass, and one clipped to the coastline of one scheme and the
grounding line of another double counts or omits the strip between.
None of this errors: every basin file overlays every grid.

**Correct approach.** A per-basin or per-sector number names its
basin definition (the GSFC drainage systems or the IMBIE basins, with
the version of the file), whether it is grounded ice only or includes
the floating portion, and which coastline or grounding line closes
it; a comparison across studies is made on the same definition or
states that it is not, and an ice sheet total is voiced with the
sector allocation that the definition implies (which ice shelves count
as East Antarctica, for instance).[^gsfc-drainage-systems][^nsidc-0709-user-guide][^imbie-2018]
A sum over ATL15 uses ice_area of the same group and epoch, so that
the product's own extent and the basin polygon are both in the
statement.[^atl14-15-atbd]

**Verification.** The GSFC page, read 2026-09-13, gives the system
numbering, the sector allocation, the treatment of the ice shelves
and the note on junction points; the NSIDC-0709 product page and user
guide, read the same day, name the IMBIE 2016 basins and the refined
set.[^gsfc-drainage-systems][^nsidc-0709-page][^nsidc-0709-user-guide]
The two IMBIE papers were read on the journal's site the same day,
and the basin areas above are quoted from the 2018 paper's Extended
Data Fig. 2 caption; both records were verified against the Crossref
registry (title, journal, year).[^imbie-2018][^imbie-2019] Rignot and
others 2011 is cited on its Crossref record; the journal page sits
behind a bot check.[^rignot-2011] The ATBD gives the ice masks and the
ice_area definition.[^atl14-15-atbd] The two dataset concepts list
this trap among their known issues.[^dataset][^velocity-dataset]

[^gsfc-drainage-systems]: Zwally and others, 2012, Antarctic and Greenland Drainage Systems, GSFC
[^nsidc-0709-page]: NSIDC product page, NSIDC-0709 Version 2
[^nsidc-0709-user-guide]: NSIDC-0709 Version 2 user guide
[^imbie-2018]: The IMBIE team, 2018, Nature, doi:10.1038/s41586-018-0179-y
[^imbie-2019]: The IMBIE team, 2019, Nature, doi:10.1038/s41586-019-1855-2
[^rignot-2011]: Rignot, Mouginot and Scheuchl, 2011, Science, doi:10.1126/science.1208336
[^atl14-15-atbd]: ATL14/ATL15 ATBD, release 005
[^dataset]: This bundle's ATL15 dataset concept
[^velocity-dataset]: This bundle's velocity mosaic concept
