---
type: dataset-gotcha
spheres: [cryosphere]
title: "The grids are polar stereographic metres, not latitude and longitude: cell area varies, and a sum without the true cell area biases a total"
description: "ATL15 and the MEaSUREs velocity mosaics are on polar stereographic grids (EPSG 3413 in the north with true scale at 70 N, EPSG 3031 in the south with true scale at 71 S) whose x and y are metres, and a grid that is square in those metres has a ground area per cell that changes with latitude through the projection's scale factor. Summing a field over cells with the nominal spacing squared as the area, or treating x and y as degrees, biases an ice sheet total and misplaces every feature; ATL15 ships the true ice-covered area per cell as ice_area, and ITS_LIVE Version 2 velocities are themselves in map units."
tags: [icesat2, atl15, its-live, polar-stereographic, epsg-3413, epsg-3031, projection, cell-area, ice-area, volume-change]
generated: { by: knowledge-seeder/claude, at: 2026-09-13T20:30:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-13T21:10:06Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/129 }
severity: medium
# medium: the projections are documented on every product page and
# the products ship the area or state the map-unit convention; the
# error is a few percent to tens of percent on a total and is caught
# by the product's own area field; no eval case is required.
dataset: ../datasets/icesat2-atl15.md
status: stable
stale_after: 2027-03-13
sources:
  - id: atl14-15-atbd
    resource: https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl14_atl15_atbd_v005.pdf
    title: "Smith and others, ICESat-2 ATBD for ATL14 and ATL15, release 005: the two projections, the statement that cell area differs from the grid spacing squared, ice_area, and the area weighting of the reduced resolutions"
  - id: atl15-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/atl15-v005-userguide.pdf
    title: "ATL15 Version 5 user guide: geolocation in EPSG 3413 and EPSG 3031, and the same statement about cell area"
  - id: atl15-data-dict
    resource: https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl15_data_dict_v5.pdf
    title: "ATL15 data dictionary, version 5: ice_area in square metres, accounting for the area distortion of the polar stereographic projections"
  - id: nsidc-ps-guide
    resource: https://nsidc.org/data/user-resources/help-center/guide-nsidcs-polar-stereographic-projection
    title: "NSIDC guide to its polar stereographic projection: the true-scale latitude, the 6 percent distortion at the poles and the 31 percent (north) and 22 percent (south) distortion at the grid edges"
  - id: nsidc-0776-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/nsidc-0776-v002-userguide.pdf
    title: "NSIDC-0776 Version 2 user guide: regions and their EPSG codes, the mapping variable, and the statement that Version 2 velocities are in map units with scale errors of up to a few percent, uncorrected"
  - id: nsidc-0725-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/nsidc-0725-v005-userguide.pdf
    title: "NSIDC-0725 user guide: the EPSG 3413 definition table (latitude of true scale 70, central meridian 45 W)"
  - id: dataset
    resource: ../datasets/icesat2-atl15.md
    title: "This bundle's ATL15 dataset concept, which lists this trap among the known issues"
  - id: velocity-dataset
    resource: ../datasets/its-live-ice-velocity.md
    title: "This bundle's velocity mosaic concept, which lists this trap among the known issues"
---

# The grids are polar stereographic metres, not latitude and longitude

**Mechanism.** ATL15 is provided in polar stereographic coordinates on
the WGS 84 ellipsoid: in the Northern Hemisphere the NSIDC Sea Ice
Polar Stereographic North grid with a standard latitude of 70 N and a
central meridian of 45 W (EPSG 3413), in the Southern Hemisphere the
Antarctic Polar Stereographic grid with a standard latitude of 71 S
and a central meridian of 0 (EPSG 3031); x and y are grid-cell centre
coordinates in metres.[^atl14-15-atbd][^atl15-user-guide] The
velocity mosaics use the same two grids for the polar regions
(NSIDC-0776 for regions north of 55 N and for Antarctica, NSIDC-0725
and the older Greenland maps on EPSG 3413, NSIDC-0484 on the 71 S
grid), with UTM zones and a Lambert projection for the other ITS_LIVE
regions, and the mapping variable in each file describes the coordinate
reference system.[^nsidc-0776-user-guide][^nsidc-0725-user-guide]
A stereographic projection is conformal, not equal-area: the scale is
true at the standard latitude and grows away from it, so a cell that
is 1 km by 1 km in projected metres covers a ground area that departs
from one square kilometre by the square of the scale factor at its
latitude. The ATBD states it directly: because the products are
defined on grids that are square in these projected coordinates, the
area of each grid cell is different from the square of the grid
spacing, and the scaling between grid area and true area varies with
distance from the true-scale latitude.[^atl14-15-atbd] NSIDC's own
guide to the projection gives the size of the effect on its sea ice
grids, which are true at 70 N and at 70 S: 6 percent distortion at
the poles, rising to 31 percent at the edge of the northern grid and
22 percent at the edge of the southern one; the guide does not say
whether those figures are linear or area distortions, and its
southern grid is true at 70 S where EPSG 3031 is true at 71 S, so the
figures describe the guide's grids and not ATL15's
exactly.[^nsidc-ps-guide] The ATL15 grids extend to 59 N and 60 S,
which is closer to their true-scale latitudes than the guide's grid
edges, so the distortion inside ATL15's extent is smaller than the
guide's edge figures; the ATBD gives no figure and provides ice_area
instead.[^atl15-user-guide][^atl14-15-atbd] For this reason ATL15 carries
ice_area, the ice-covered area of each cell in square metres computed
from the 100 m mask and cell areas and accounting for the projection's
area distortion, and its reduced resolutions are area-weighted
averages of the 1 km fields.[^atl14-15-atbd][^atl15-data-dict]
The velocity products carry the same geometry into their values:
NSIDC-0776 Version 2 velocities are calculated in map units and not
corrected for the scale distortion, so they are horizontal velocities
as measured in map space, differing from ground velocities by up to a
few percent depending on projection and location; Version 1 had
applied the correction.[^nsidc-0776-user-guide]

**Wrong-result mode.** An ice sheet volume change formed as the sum of
delta_h times the nominal cell area (the grid spacing squared) weights
every cell equally in map space while the ground area they represent
differs from it by an amount the sources bound at a few percent for
the velocity products' scale and at 6 percent at the pole and tens of
percent at the edges of NSIDC's wider sea ice grids; the bias grows with distance from the
true-scale latitude, toward the pole in Antarctica and toward both the
southern tip of Greenland and the far north of the Arctic regions, so
it is not uniform and does not cancel between regions of gain and
loss. The same sum with ice_area omitted
also counts partly ice-covered coastal cells at full area. Reading x
and y as longitude and latitude, or writing the arrays into a
geographic raster without reprojecting, places every feature wrongly
and makes any overlay with a basin mask or a GRACE mascon grid
meaningless. For the velocities, a flux gate drawn in projected
coordinates and multiplied by a map-space velocity needs no scale
correction on either factor, while a gate length measured on the
ground combined with a Version 2 velocity, or a Version 2 velocity
compared with a GPS station, is off by the local scale factor unless
one side is corrected.[^nsidc-0776-user-guide]

**Correct approach.** A total over ATL15 cells weights each cell by
ice_area from the same group and epoch, which is both the projection
correction and the ice mask; a reduced-resolution granule is already
area-weighted at its scale.[^atl14-15-atbd][^atl15-data-dict] Any
overlay (basins, mascons, a velocity mosaic on the other grid) is
done in one coordinate reference system read from the file's mapping
variable or the documented EPSG code, with reprojection where the
systems differ.[^nsidc-0776-user-guide][^atl15-user-guide] A flux from
a velocity mosaic states whether the velocity and the gate geometry
are in map space or corrected to ground, consistently on both
factors.[^nsidc-0776-user-guide]

**Verification.** The ATBD and the user guide both state the
projections and that cell area differs from the spacing squared; the
data dictionary describes ice_area as accounting for the area
distortion; NSIDC's projection guide gives the distortion figures; the
NSIDC-0776 guide states the map-unit convention and its two
implications; all were read on
2026-09-13.[^atl14-15-atbd][^atl15-user-guide][^atl15-data-dict][^nsidc-ps-guide][^nsidc-0776-user-guide]
The two dataset concepts list this trap among their known
issues.[^dataset][^velocity-dataset]

[^atl14-15-atbd]: ATL14/ATL15 ATBD, release 005
[^atl15-user-guide]: ATL15 Version 5 user guide, NSIDC
[^atl15-data-dict]: ATL15 data dictionary, version 5
[^nsidc-ps-guide]: NSIDC guide to the polar stereographic projection
[^nsidc-0776-user-guide]: NSIDC-0776 Version 2 user guide
[^nsidc-0725-user-guide]: NSIDC-0725 user guide
[^dataset]: This bundle's ATL15 dataset concept
[^velocity-dataset]: This bundle's velocity mosaic concept
