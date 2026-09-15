---
type: dataset-gotcha
spheres: [atmosphere]
title: "AIRS level 3 profiles sit on fixed pressure levels, not model levels, and the lowest levels lie below the terrain: the per-level count falls to zero there, the layer water vapour is integrated below the surface, and a mean at 1000 or 925 hPa over land is a mean over the low ground only"
description: "The AIRS version 7 level 3 temperature profile is reported on 24 standard pressure levels from 1000 to 1 hPa and water vapour on 12 levels from 1000 to 100 hPa and 12 layers bounded by the standard levels from 1000 to 70 hPa, the same levels in every cell whatever the elevation; where the terrain rises above a level no retrieval reaches it, the level's count (_ct) drops toward zero while TotalCounts stays full, and the cell reads as fill. The layer mixing ratio profile assumes an atmosphere down to 1000 hPa and extends below the surface, while the total column water vapour does not. A regional mean at a low level over topography, a vertical integral of the layers, or a comparison against a reanalysis on model levels or with its own below-ground convention, returns a number the file raised no error about."
tags: [airs, aqua, airs3std, airs3stm, pressure-levels, surface-pressure, topography, water-vapour, temperature, gesdisc, atmosphere]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T13:30:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-15T13:59:41Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/161 }
severity: high
dataset: ../datasets/airs-l3-temperature-humidity.md
eval_case: airs-pressure-levels-and-surface-mask
status: draft
stale_after: 2027-03-15
sources:
  - id: airs-l3-ug
    resource: https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/V7_L3_User_Guide.pdf
    title: "Tian, Manning, Roman, Thrastarson, Fetzer and Monarrez, 2020, AIRS Version 7 Level 3 Product User Guide, version 1.0, April 2020, JPL (read 2026-09-15: Table 1 of the 24 temperature and 12 water vapour levels and the 12 layer midpoints from 961.8 to 83.7 hPa, whose boundaries the H2OPressureLay dimension note places at the standard levels, so the layers run 1000 to 70 hPa, the StdPressureLev and H2OPressureLev dimension notes, the field table with SurfPres_Forecast, Topography, H2O_MMR_Lyr and TotH2OVap and the _ct and TotalCounts ancillaries, section 1.3 on missing data where topography intrudes into the lower profile, section 4.2 on unequal numbers of samples within profiles due to topography and section 4.4 on the difference between TotH2OVap and the vertical integral of the layers)"
  - id: cmr-airs3std
    resource: https://cmr.earthdata.nasa.gov/search/collections.json?short_name=AIRS3STD&provider=GES_DISC
    title: "CMR collection and UMM records for AIRS3STD and AIRS3STM 7.0 (read 2026-09-15: the abstract's statement that each mean map has a count map, that counts bound the points per bin, and that surface pressure is among the parameters)"
  - id: gesdisc-airs3std
    resource: https://disc.gsfc.nasa.gov/datasets/AIRS3STD_7.0/summary
    title: "GES DISC collection page for AIRS3STD 7.0 (fetched 2026-09-15, text read from its CMR record: the mean, standard deviation and count maps per parameter)"
  - id: merra2
    resource: ../datasets/merra-2.md
    title: "This bundle's MERRA-2 dataset concept: the reanalysis carries 42 pressure levels and 72 model layers, and its below-ground pressure-level points are undefined rather than extrapolated, so a comparison at a low level is between two masked fields"
  - id: dataset
    resource: ../datasets/airs-l3-temperature-humidity.md
    title: "This bundle's AIRS level 3 dataset concept, which names the levels, the ancillaries and this trap"
---

# AIRS pressure levels and the surface mask

**Mechanism.** The AIRS level 3 standard product reports temperature
and geopotential height on 24 fixed pressure levels (1000, 925, 850,
700, 600, 500, 400, 300, 250, 200, 150, 100, 70, 50, 30, 20, 15, 10,
7, 5, 3, 2, 1.5 and 1 hPa, surface upward), water vapour mass mixing
ratio and relative humidity on the 12 levels from 1000 to 100 hPa,
and a layer mixing ratio on 12 layers whose boundaries are the
standard levels from 1000 down to 70 hPa, the topmost layer being 100
to 70 hPa, with mid-layer pressures from 961.8 to 83.7 hPa; the
level 3 levels are a
subset of the 28 level 2 pressure levels, and the support product
carries 100.[^airs-l3-ug] These are pressure levels, the same in
every cell, not the terrain-following or hybrid levels of a model:
the retrieval's own vertical coordinate is the pressure grid, and
the file carries the terrain separately, as Topography in metres in
the location grid and as SurfPres_Forecast, the forecast surface
pressure, in the ascending, descending and TqJoint grids (the field
table lists it among the standard and TqJoint grid fields, not among
the microwave-only ones).[^airs-l3-ug] Where the ground rises
above a level, no retrieval reports that level, and the guide names
the consequence twice: the monthly product is complete except where
the retrieval was problematical or "where topography intrudes into
the lower altitude regime of profiles", and over topography the
count of samples actually included at a level, Temperature_A_ct,
"may drop rapidly to zero as the profile approaches the 1000mb
level", while TotalCounts_A, the number of fields of regard in the
cell, stays the maximum any level could use.[^airs-l3-ug] A cell
with a count of zero holds the fill value minus 9999 at that level
and a valid value at the levels above.[^airs-l3-ug][^cmr-airs3std]
The layer product does not stop at the ground: the layer mixing
ratio profile "assumes the atmosphere extends downward all the way
to 1000mb and it can extend below the surface", whereas the total
column water vapour TotH2OVap does not make that assumption, so the
two disagree wherever the surface pressure is below 1000 hPa, which
the guide says happens over ocean as well as land.[^airs-l3-ug]
MERRA-2, the reanalysis AIRS multi-year means are compared with,
keeps its own convention: pressure-level points below ground are
undefined, not extrapolated, and its 72 model layers are a different
coordinate again.[^merra2]

**Wrong-result mode.** A regional or zonal mean of Temperature_A or
H2O_MMR_A at 1000 or 925 hPa over a region with terrain averages
only the cells that reach that pressure: over a plateau or a
mountain range the low-lying valleys and coasts carry the mean, the
high ground contributes nothing, and the result is a sampling
artefact that changes with the region's hypsometry rather than a
property of the air; nothing flags it, because the fill cells are
simply absent from the mean.[^airs-l3-ug] A time series of a
low-level field over such a region varies with the day-to-day
set of cells whose count is nonzero, which varies with the swath
gores and the clouds, not only with the weather.[^airs-l3-ug] A
column water vapour built by integrating H2O_MMR_Lyr over the 12
layers includes air below the surface and exceeds TotH2OVap, the
excess growing with elevation and appearing over the ocean too
whenever the surface pressure is below 1000 hPa; the guide says a
topographic correction using the layer fractions above the surface
is only partial because the mixing ratio is not constant through a
layer.[^airs-l3-ug] A comparison at 925 hPa with a model on its
native levels, or with a reanalysis that extrapolates below ground,
compares a masked field with a full or a synthetic one and reads the
difference over land as bias; a comparison with MERRA-2's
pressure-level fields is between two masks whose edges are drawn
from different surface pressures.[^merra2][^airs-l3-ug] Reading the
count as a quality measure inverts it here: a level whose count is
a tenth of TotalCounts over a mountain is not a poorly retrieved
level, it is a level mostly below the ground.[^airs-l3-ug]

**Correct approach.** A level is below the surface of a cell where
its pressure exceeds the cell's surface pressure, and the file
carries that pressure as SurfPres_Forecast beside the profile, so a
low-level analysis masks by it (or by the per-level count against
TotalCounts) and states which cells and what fraction of the region
entered the mean; a near-surface quantity over land is the surface
field the product provides for it (SurfAirTemp, H2O_MMR_Surf,
RelHumSurf, SurfSkinTemp), not the 1000 hPa level.[^airs-l3-ug] A
column water vapour is TotH2OVap; an integral of the layers is a
different quantity, and where it is wanted the layers below
SurfPres_Forecast are removed with the partial correction the guide
describes.[^airs-l3-ug] A comparison with a model or a reanalysis
is on a common mask: the same cells and levels, each side's
below-ground points removed by its own surface pressure, with the
count carried so that a cell resting on one retrieval is known as
such.[^merra2][^airs-l3-ug] The TqJoint grids give every field and
level the same ensemble, which removes the difference in yield
between levels that is due to quality control but not the one due
to terrain.[^airs-l3-ug]

**Verification.** Table 1 of the user guide lists the levels and the layer midpoints
(with the layer boundaries at the standard levels), and
the guide's sections 4.2 and 4.4 state the count drop over
topography and the below-surface extent of the layers in the words
quoted above.[^airs-l3-ug] The check a reader runs on one daily
file: over the Tibetan plateau, the Andes or Antarctica,
Temperature_A_ct at 1000 hPa is zero and Temperature_A is fill while
TotalCounts_A and the 500 hPa count are not, and SurfPres_Forecast_A
in those cells is well below 925 hPa; and the sum of H2O_MMR_Lyr_A
over the 12 layers, converted to a column, exceeds TotH2OVap_A in
those cells and over any ocean cell whose SurfPres_Forecast_A is
below 1000 hPa.[^airs-l3-ug] The CMR record names the count map and
the surface pressure among the fields.[^cmr-airs3std][^gesdisc-airs3std]
The dataset concept lists this trap among its known issues.[^dataset]

[^airs-l3-ug]: Tian and others, 2020, AIRS Version 7 Level 3 Product User Guide, version 1.0
[^cmr-airs3std]: CMR collection and UMM records, AIRS3STD and AIRS3STM 7.0, read 2026-09-15
[^gesdisc-airs3std]: GES DISC collection page and CMR record, AIRS3STD 7.0
[^merra2]: This bundle's MERRA-2 dataset concept
[^dataset]: This bundle's AIRS level 3 dataset concept
