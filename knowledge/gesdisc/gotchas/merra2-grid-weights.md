---
type: dataset-gotcha
spheres: [atmosphere, hydrosphere]
title: "The 0.625 by 0.5 degree MERRA-2 grid is a regular latitude-longitude grid: cell area falls toward the poles, no area variable ships, and a plain mean is not a global mean"
description: "Every MERRA-2 collection is on the same 576 by 361 regular grid, half a degree in latitude with rows at both poles, interpolated from the model's cubed sphere. A cell's area is proportional to the cosine of its latitude, so an unweighted mean over the grid over-represents the polar rows; the constants collection carries surface fractions and geopotential but no cell-area variable (the specification's revision history records AREA removed from the constants tables), and the land collection's values are per unit land area, so a total also needs the land fraction."
tags: [merra-2, merra2, grid, area-weights, global-mean, cosine-latitude, land-fraction, gesdisc]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:30:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-14T12:12:43Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/144 }
severity: low
# low: the grid is documented, the weighting is standard practice on
# any regular latitude-longitude grid, and the error in an unweighted
# mean is bounded and visible; recorded because the product ships no
# area variable and the land collection's per-land-area convention
# compounds the mistake.
dataset: ../datasets/merra-2.md
status: stable
stale_after: 2027-03-14
sources:
  - id: filespec
    resource: https://gmao.gsfc.nasa.gov/media/publications/zbly36ziNFDFbmYmvhQeVqPhUo/Bosilovich785.pdf
    title: "Bosilovich, Lucchesi and Suarez, 2016, MERRA-2: File Specification, GMAO Office Note No. 9 (version 1.1), read 2026-09-14: the horizontal grid (576 by 361, 0.625 by 0.5 degrees, origin at 180 W and 90 S, interpolated from the cubed sphere), the global attributes with the latitude and longitude bounds and resolutions, the revision history (AREA removed from the constants tables in version 1.1), and the land budget note that LND quantities are per unit land area"
  - id: readme
    resource: https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T1NXSLV.5.12.4/doc/MERRA2.README.pdf
    title: "GES DISC README Document for MERRA-2 Data Products (revised 2021-03-01), read 2026-09-14: the constants collection M2C0NXASM (FRLAKE, FRLAND, FRLANDICE, FROCEAN, PHIS, SGH) with no area variable, and the dimensions longitude 576 by latitude 361 on every collection"
  - id: gmao-faq
    resource: https://gmao.gsfc.nasa.gov/gmao-products/merra-2/faq_merra-2/
    title: "GMAO MERRA-2 FAQ, read 2026-09-14: the land collection holds land-only values not weighted by the land fraction while the other collections are grid-box averages over all tiles; below-ground pressure-level points are undefined and area averages that include them are not representative; the model computes on a cubed-sphere grid of tiles and the output is on the regular 576 by 361 grid"
  - id: cmr-merra2
    resource: https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=M2T1NXSLV&provider=GES_DISC
    title: "CMR collection record for M2T1NXSLV (C1276812863-GES_DISC), read 2026-09-14: the global bounding rectangle from 180 W to 180 E and 90 S to 90 N, and the collection titles naming the 0.625 by 0.5 degree grid"
  - id: dataset
    resource: ../datasets/merra-2.md
    title: "This bundle's MERRA-2 dataset concept, which states the grid in its structure and lists this trap among the known issues"
---

# MERRA-2 grid weights

**Mechanism.** All MERRA-2 output is on one regular
longitude-latitude grid: 576 points at 0.625 degrees in longitude
from 180 W eastward and 361 points at 0.5 degrees in latitude from
90 S to 90 N, so that rows exist at both poles; the model itself runs
on a cubed sphere of roughly 50 km and the distributed fields are
interpolated to the regular grid for convenience.[^filespec][^cmr-merra2][^gmao-faq]
On a regular grid the width of a cell in longitude shrinks with the
cosine of latitude while its height stays fixed, so the area a value
represents falls from the equator toward the poles and the two pole
rows stand for half-height caps. The constants collection ships the
surface-type fractions (FRLAND, FRLANDICE, FRLAKE, FROCEAN) and the
surface geopotential, and no cell-area variable; the specification's
revision history records AREA removed from the constants tables in
its version 1.1.[^readme][^filespec] The land collection (LND) holds
values per unit land area from the land model alone, defined only
where the land fraction is non-zero and undefined elsewhere, while
FLX, RAD and the other collections are grid-box averages over all
tiles weighted by their fractions.[^filespec][^gmao-faq]

**Wrong-result mode.** A global or regional mean computed as the
plain average of the array weights every row equally, so the polar
and high-latitude rows, which cover a small fraction of the sphere,
count as much as the tropics; the error is a bias whose sign and size
depend on the meridional gradient of the field, and it is largest for
quantities that differ strongly between the tropics and the poles,
such as temperature, precipitable water and precipitation. A land
total formed by multiplying an LND flux by grid-cell area counts the
whole cell as land where the land fraction is a coastal sliver, and a
land mean over LND fields mixes per-land-area values with undefined
points where the fraction is zero.[^filespec][^gmao-faq] A mean on a
pressure level that intersects the terrain includes undefined
below-ground points, which are not extrapolated in MERRA-2, so an
unscreened area average there is not comparable with reanalyses that
extrapolate.[^gmao-faq] None of this errors: the arrays are full,
regular and unit-consistent.

**Correct approach.** An area mean weights each cell by its area,
proportional to the cosine of its latitude for the interior rows with
the pole rows as half cells, or by the exact spherical area between
the half-degree bounds; a total multiplies by that area; a land total
or mean multiplies an LND value by the cell's land area (cell area
times FRLAND from the constants collection) and skips the undefined
points; and a pressure-level average screens the undefined
below-ground points and says so.[^filespec][^readme][^gmao-faq]

**Verification.** The grid definition, its origin, the resolution
attributes and the absence of an area variable are in the file
specification and the README constants table; the CMR record carries
the global bounding rectangle; the FAQ carries the per-land-area
convention and the undefined below-ground rule.[^filespec][^readme][^cmr-merra2][^gmao-faq]
A reader can check the two conventions on one file: the latitude
coordinate runs from minus 90 to plus 90 in 361 steps, and an LND
field is undefined over the open ocean where FRLAND is
zero.[^filespec][^gmao-faq] The dataset concept states the grid and
lists this trap.[^dataset]

[^filespec]: Bosilovich, Lucchesi and Suarez, 2016, MERRA-2: File Specification, GMAO Office Note 9, version 1.1
[^readme]: GES DISC README Document for MERRA-2 Data Products, revised 2021-03-01
[^gmao-faq]: GMAO MERRA-2 FAQ
[^cmr-merra2]: CMR collection record for M2T1NXSLV, read 2026-09-14
[^dataset]: This bundle's MERRA-2 dataset concept
