---
type: dataset
spheres: [cryosphere]
title: "BedMachine Greenland (IDBMG4 Version 6) and BedMachine Antarctica (NSIDC-0756 Version 4): ice thickness, bed topography, surface, error and mask on the polar stereographic grids"
description: "One netCDF-4 file per ice sheet holding bed elevation, ice surface elevation, ice thickness, the thickness and bed error, an ice, ocean and land mask, a geoid offset and a source map that says which method made each pixel, at 150 m on the EPSG 3413 grid for Greenland (nominal year 2007) and 500 m on the EPSG 3031 grid for Antarctica (nominal year 2015). Thickness comes from mass conservation where ice flows fast, from kriging, streamline diffusion or ice flow perturbation analysis in the slow interior and from hydrostatic equilibrium on floating ice, constrained by radar flight lines; the Antarctic surface and thickness are in ice equivalent with the firn air content removed."
tags: [bedmachine, idbmg4, nsidc-0756, measures, icebridge, ice-thickness, bed-topography, bathymetry, mass-conservation, errbed, greenland, antarctica, nsidc, cryosphere]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T13:30:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-15T14:22:23Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/162 }
resource: https://nsidc.org/data/idbmg4/versions/6
version: "Greenland IDBMG4 Version 6 (DOI 10.5067/6B6B225B8V2D; the user guide's version history dates Version 6 to 11 December 2025 and the retirement of Version 5 to 13 January 2026), CMR concept C3903728370-NSIDC_CPRD with two granules, BedMachineGreenland-v6.nc and BedMachineGreenland_bed-v6.tif; Antarctica NSIDC-0756 Version 4 (DOI 10.5067/POJQI54A45HX; first public release V4.1 dated 21 January 2026 in the guide, Version 3 retired 24 February 2026), CMR concept C3973022985-NSIDC_CPRD with one granule, NSIDC-0756_BedMachineAntarctica_19700101-20191001_V04.1.nc; both verified 2026-09-15"
sources:
  - id: idbmg4-page
    resource: https://nsidc.org/data/idbmg4/versions/6
    title: "NSIDC product page: IceBridge BedMachine Greenland, Version 6 (overview, parameters, 150 m, EPSG 3413, temporal coverage 1993 to 2021, the version summary, the citation and the user guide link), read 2026-09-15"
  - id: idbmg4-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/idbmg4-v006-userguide.pdf
    title: "IceBridge BedMachine Greenland Version 6 user guide (NSIDC): the parameter table with the mask, source and dataid codes, resolution, nominal year, the source data table, the mass conservation processing, the error statement and the version history, read in full 2026-09-15"
  - id: nsidc-0756-page
    resource: https://nsidc.org/data/nsidc-0756/versions/4
    title: "NSIDC product page: MEaSUREs BedMachine Antarctica, Version 4 (overview, parameters including firn air content, 500 m, EPSG 3031, temporal coverage 1970 to 2019, the version summary, the citation and the user guide link), read 2026-09-15"
  - id: nsidc-0756-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/nsidc-0756-v004-userguide.pdf
    title: "MEaSUREs BedMachine Antarctica Version 4 user guide (NSIDC, January 2026): the parameter table with the mask, source and dataid codes, the ice equivalent convention, the file name, the methods by ice regime, the firn air correction, the error statement and the version history, read in full 2026-09-15"
  - id: idbmg4-v5-page
    resource: https://nsidc.org/data/idbmg4/versions/5
    title: "NSIDC product page for IceBridge BedMachine Greenland Version 5 (DOI 10.5067/GMEVBWFLWA7X), marked retired with a more recent version available, read 2026-09-15"
  - id: nsidc-0756-v3-page
    resource: https://nsidc.org/data/nsidc-0756/versions/3
    title: "NSIDC product page for MEaSUREs BedMachine Antarctica Version 3 (DOI 10.5067/FPSU0V1MWUB6), marked retired with a more recent version available, read 2026-09-15"
  - id: idbmg4-v5-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/idbmg4-v005-userguide.pdf
    title: "IceBridge BedMachine Greenland Version 5 user guide (retired version): its parameter table, whose mask carries 4 for non-Greenland land, read 2026-09-15 for that table"
  - id: nsidc-0756-v3-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/nsidc-0756-v003-userguide.pdf
    title: "MEaSUREs BedMachine Antarctica Version 3 user guide (retired version): its parameter table, whose dataid labels value 1 as REMA, read 2026-09-15 for that table"
  - id: cmr-idbmg4
    resource: https://cmr.earthdata.nasa.gov/search/collections.json?short_name=IDBMG4
    title: "CMR collection record for IDBMG4 (provider NSIDC_CPRD, version 6, concept C3903728370-NSIDC_CPRD) and its granule list, read 2026-09-15"
  - id: cmr-nsidc-0756
    resource: https://cmr.earthdata.nasa.gov/search/collections.json?short_name=NSIDC-0756
    title: "CMR collection record for NSIDC-0756 (provider NSIDC_CPRD, version 4, concept C3973022985-NSIDC_CPRD) and its granule list, read 2026-09-15"
  - id: morlighem-2017
    resource: https://doi.org/10.1002/2017GL074954
    title: "Morlighem and others, 2017, BedMachine v3: Complete Bed Topography and Ocean Bathymetry Mapping of Greenland From Multibeam Echo Sounding Combined With Mass Conservation, Geophysical Research Letters 44, issue 21 (the Greenland method paper the product asks to be cited), record and abstract verified against the Crossref registry 2026-09-15"
  - id: morlighem-2020
    resource: https://doi.org/10.1038/s41561-019-0510-8
    title: "Morlighem and others, 2020, Deep glacial troughs and stabilizing ridges unveiled beneath the margins of the Antarctic ice sheet, Nature Geoscience 13, 132 to 137 (the Antarctic method paper the product asks to be cited), record verified against the Crossref registry 2026-09-15"
  - id: basins-gotcha
    resource: ../gotchas/ice-sheet-boundaries-and-drainage-basins.md
    title: "This bundle's ice sheet boundaries gotcha, which records from the ATL14 and ATL15 ATBD that the Greenland ice mask of those products is BedMachine v3"
status: stable
stale_after: 2027-03-15
---

# BedMachine Greenland and BedMachine Antarctica

**Identity.** BedMachine is the pair of bed topography and bathymetry
maps of the two ice sheets that NSIDC distributes as IceBridge
BedMachine Greenland (IDBMG4) and MEaSUREs BedMachine Antarctica
(NSIDC-0756); each carries the ice surface elevation, the ice
thickness, an error estimate and an ice, ocean and land mask beside
the bed.[^idbmg4-page][^nsidc-0756-page] Greenland is one netCDF file,
BedMachineGreenland-v6.nc, with the bed also provided as a GeoTIFF,
at 150 m on the WGS 84 / NSIDC Sea Ice Polar Stereographic North grid
(EPSG 3413), covering 59 N to 84 N and 90 W to 9 E; its source data
were collected between 1 January 1993 and 31 December 2021, and the
nominal year of the data set is 2007.[^idbmg4-user-guide][^idbmg4-page]
Antarctica is one netCDF file,
NSIDC-0756_BedMachineAntarctica_19700101-20191001_V04.1.nc, at 500 m
on the WGS 84 / Antarctic Polar Stereographic grid (EPSG 3031),
covering 53 S to 90 S; the page and the guide's temporal coverage
section give the data as collected between 1 January 1970 and
1 October 2019, while the guide's acquisition section says the radar
campaigns were flown between 1967 and 2020, and its nominal year,
2015, is the year of the reference surface digital elevation
model.[^nsidc-0756-user-guide][^nsidc-0756-page] The CMR records
(concept C3903728370-NSIDC_CPRD for IDBMG4 version 6, concept
C3973022985-NSIDC_CPRD for NSIDC-0756 version 4) listed two granules
for Greenland and one for Antarctica on
2026-09-15.[^cmr-idbmg4][^cmr-nsidc-0756] The Greenland guide's
version history dates Version 6 to 11 December 2025 and the removal
of Version 5 to 13 January 2026; the Antarctic guide dates Version 4
to 21 January 2026, released as V4.1 following the data provider's
own numbering, and the removal of Version 3 to 24 February 2026, so
the Version 5 and Version 3 pages that earlier work cites are retired
pages.[^idbmg4-user-guide][^nsidc-0756-user-guide][^idbmg4-v5-page][^nsidc-0756-v3-page]
Version 6 of Greenland generated an ensemble of bed maps using
ICESat-2 time series and took the median depth for some glaciers,
added IceBoost thickness for the peripheral glaciers, added a Randolph
Glacier Inventory field and new bathymetry; Version 4 of Antarctica
introduced ice flow perturbation analysis for the interior bed,
IceBoost thickness for the peripheral glaciers and the Peninsula, new
coastal bathymetry and the same inventory
field.[^idbmg4-user-guide][^nsidc-0756-user-guide]

**Structure.** Both files carry the same core variables on projected
x and y in metres: bed (bed elevation relative to the geoid), surface
(ice surface elevation relative to the geoid), thickness (ice
thickness), errbed (the bed topography and ice thickness error),
geoid (the height of the EIGEN-6C4 geoid above the WGS 84 ellipsoid,
to be added to bed to obtain ellipsoidal height), mask, source,
dataid, rgi and a mapping variable with the coordinate reference
system, all in metres where they are
heights.[^idbmg4-user-guide][^nsidc-0756-user-guide] The mask is 0 for
ocean, 1 for ice-free land, 2 for grounded ice and 3 for floating ice
in both Version 6 and Version 4 parameter tables, and Antarctica adds
4 for Lake Vostok; the retired Greenland Version 5 guide's table also
carried 4 for non-Greenland land, a value the Version 6 table no
longer lists.[^idbmg4-user-guide][^nsidc-0756-user-guide][^idbmg4-v5-user-guide] The source
variable records the method that produced each pixel: in Greenland
0 none, 1 GIMP DEM, 2 mass conservation, 3 synthetic,
4 interpolation, 5 hydrostatic equilibrium, 6 kriging, 7 RTopo-2,
8 gravity inversion, 9 IceBoost and 10 and above bathymetry data; in
Antarctica 1 REMA or IBCSO v2, 2 mass conservation, 3 interpolation,
4 hydrostatic, 5 ice flow perturbation analysis, 6 gravity,
7 seismic, 8 IceBoost and 10 multibeam.[^idbmg4-user-guide][^nsidc-0756-user-guide]
The dataid variable records the input data source where there is
one: in Greenland 1 GIMP DEM, 2 radar, 7 seismic bathymetry and
10 multibeam bathymetry; in Antarctica, in the Version 4 table's own
words, "0 = no data; 1 = radar seismic multibeam (REMA); 2 = radar;
7 = seismic; 10 = multibeam", where the Version 3 table labelled
value 1 simply "REMA".[^idbmg4-user-guide][^nsidc-0756-user-guide][^nsidc-0756-v3-user-guide] The two
files differ in one convention that matters for a thickness: the
Antarctic surface and thickness are in ice equivalent, that is, with
a firn air content correction applied so that elevations are lower
than they would be with the air column included, and the file carries
that correction as the firn variable, so the REMA snow surface is
surface plus firn; the Greenland file carries no firn variable and its
surface is the GIMP digital elevation model relative to the
geoid.[^nsidc-0756-user-guide][^idbmg4-user-guide] The grids are
polar stereographic metres, so the ground area of a cell varies with
latitude (its own gotcha in this bundle).

**Processing.** Ice thickness is mapped by different methods in
different ice regimes, and the source variable is the record of
which. Mass conservation combines the sparse radar-sounding
thickness with the satellite-derived ice motion and the surface mass
balance to solve the mass conservation equation for thickness while
minimizing the departure from the radar data; it works best in
well-confined fast flow, where errors in flow direction are small and
glaciers slide on the bed, which the Antarctic guide puts at an ice
surface velocity above 30 m per year, and the Greenland algorithm
neglects motion by internal shear, which that guide calls an
excellent approximation above 100 m per
year.[^idbmg4-user-guide][^nsidc-0756-user-guide]
In the slow interior, where errors in flow direction are larger,
Greenland uses kriging for the 1993 to 2016 data and streamline
diffusion from the 2017 data onward, and Antarctica uses ice flow
perturbation analysis, an inverse method that infers the bed from the
ice surface, chosen because kriging, splines and streamline diffusion
struggle to reproduce the roughness seen along radar
profiles.[^idbmg4-user-guide][^nsidc-0756-user-guide] Floating ice
shelves take hydrostatic equilibrium with a calibrated firn depth
correction, gravity inversion and seismic bathymetry supply the
cavity bed beneath the floating ice shelves (the Antarctic guide's
own phrase is gravity inversion and seismic bathymetry for grounded
ice shelves), and the Antarctic
guide states that the individual mass conservation maps are stitched
together, constrained by flight lines along their boundaries, with
inverse distance weighting, and then combined with the streamline
diffusion maps.[^nsidc-0756-user-guide] The bed is the surface digital
elevation model minus the thickness: GIMP in Greenland, REMA in
Antarctica, with the bed over ice-free land being the model
itself.[^idbmg4-user-guide][^nsidc-0756-user-guide] The Greenland
inputs are Operation IceBridge MCoRDS radar posted at 30 to 60 m with
a vertical precision of 30 m plus the other sounders the guide lists,
satellite radar velocity from 2008 and 2009 posted at 150 m with
errors of 10 m per year in speed and 1.5 degrees in direction, a
surface mass balance averaged over 1961 to 1990 and downscaled to
1 km, thickening rates from altimetry differencing between 2003 and
2006, and the GIMP surface and mask; the Antarctic inputs are 47
airborne radar campaigns flown between 1967 and 2020, interferometric
velocity, RACMO2 surface mass balance representative of 1961 to 1990,
thinning rates from Smith and others 2020, REMA and the bathymetric
compilations the guide lists.[^idbmg4-user-guide][^nsidc-0756-user-guide]
The Greenland method paper reports a 150 m map with seamless
transitions at the ice and ocean interface and a total sea level
potential of 7.42 metres with an uncertainty of 0.05 metres; the
Antarctic paper is the reference for the continent-wide bed and its
data campaigns.[^morlighem-2017][^morlighem-2020]

**Land-ice use.** The products exist for ice dynamics: the Greenland
guide names bed topography and fjord bathymetry as controls on
undercutting, calving and flow, and the Antarctic guide states that
mass conservation ensures that grounding-line fluxes are compatible
with snowfall accumulation and thinning rates in the interior without
assuming steady state.[^idbmg4-user-guide][^nsidc-0756-user-guide]
The thickness is the factor a discharge needs beside a velocity from
the mosaics in this bundle, and the mask is the record of where a
gate sits on grounded ice.[^nsidc-0756-user-guide][^idbmg4-user-guide]
The ATL14 and ATL15 processing takes its Greenland ice mask from
BedMachine v3, which is why a per-basin total from those products
names the mask version it rests on (this bundle's boundaries
gotcha).[^basins-gotcha]

## Uncertainty

- **errbed is the product's own error field**, described as the bed
  topography and ice thickness error in Greenland and the ice
  thickness and bed topography error in Antarctica, in metres; the
  Greenland guide illustrates it as a map, and neither guide states
  that it is a formal covariance or that it is
  independent between cells.[^idbmg4-user-guide][^nsidc-0756-user-guide]
- **The sources of error are the inputs to mass conservation**: the
  ice velocity direction and magnitude, the surface mass balance and
  the ice thinning rates.[^idbmg4-user-guide][^nsidc-0756-user-guide]
- **The size of the error follows the radar coverage.** In a trial
  with unusually dense radar coverage the mass-conservation thickness
  error was 36 m, only slightly above that of the radar data; in areas
  less well constrained or constrained by one track it may exceed
  50 m in south Greenland and 200 m in East Antarctica; fjords with
  little or no data in Greenland and areas of sparse ice shelf
  bathymetry in Antarctica may exceed
  500 m.[^idbmg4-user-guide][^nsidc-0756-user-guide]
- **The true resolution is not the grid.** The Greenland guide states
  that the output is generated at 150 m while the true resolution
  varies between 150 m and 5 km.[^idbmg4-user-guide]
- **The thickness is for a nominal year, not for the data's dates.**
  Greenland's nominal year is 2007 and Antarctica's is 2015 (the year
  of REMA), while the radar data span 1993 to 2021 and 1967 to 2020
  and the velocity is from 2008 and 2009 in Greenland; the thinning or
  thickening rates the guides list are how the method reconciles
  them.[^idbmg4-user-guide][^nsidc-0756-user-guide]
- **The Antarctic firn convention.** Thickness and surface are ice
  equivalent, so a comparison with a surface height measured at the
  snow surface (REMA, an altimeter) needs the firn variable added
  back, and the correction is itself a firn model
  input.[^nsidc-0756-user-guide]
- **The floating ice thickness is hydrostatic**, inferred from the
  surface with a calibrated firn correction rather than sounded,
  which the source variable records as hydrostatic
  equilibrium.[^nsidc-0756-user-guide][^idbmg4-user-guide]

## Known issues

- [bedmachine-thickness-is-interpolated](../gotchas/bedmachine-thickness-is-interpolated.md):
  thickness between flight lines is mass conservation or an
  interpolation, and source, dataid and errbed say which and how well.
- [bedmachine-mask-and-grounding-line](../gotchas/bedmachine-mask-and-grounding-line.md):
  the mask separates grounded ice, floating ice, land and ocean, and
  a discharge gate sits on grounded ice upstream of the grounding line.
- [polar-stereographic-not-latlon](../gotchas/polar-stereographic-not-latlon.md):
  the grids are EPSG 3413 and 3031 metres; a cell's ground area is
  not the grid spacing squared.
- [velocity-mosaic-epochs-and-gaps](../gotchas/velocity-mosaic-epochs-and-gaps.md):
  a discharge multiplies a velocity mosaic with its own epoch by this
  thickness with its own nominal year.
- [ice-sheet-boundaries-and-drainage-basins](../gotchas/ice-sheet-boundaries-and-drainage-basins.md):
  the BedMachine mask is one of the boundary definitions a per-basin
  number can rest on.

**Verification.** The two product pages, the two Version 6 and
Version 4 user guides and the retired Version 5 and Version 3 pages
were read on 2026-09-15, the retired Version 5 and Version 3 user
guides were read the same day for their mask and dataid tables, and
the CMR collection and granule records were read the same day; no
granule was opened from the drafting session, so the variable names
and codes above come from the guides' parameter tables, and whether a
Version 6 Greenland file still holds any pixel at mask value 4 is not
confirmed here.[^idbmg4-page][^idbmg4-user-guide][^nsidc-0756-page][^nsidc-0756-user-guide][^idbmg4-v5-page][^nsidc-0756-v3-page][^idbmg4-v5-user-guide][^nsidc-0756-v3-user-guide][^cmr-idbmg4][^cmr-nsidc-0756]
The Antarctic page and guide give two spans for the source data: the
temporal coverage is 1 January 1970 to 1 October 2019 on the page and
in the guide's temporal information section, and the guide's
acquisition section says the 47 radar campaigns were flown between
1967 and 2020; this concept reports both with their
sources.[^nsidc-0756-page][^nsidc-0756-user-guide]
The two guides do not state the same thing about the Greenland
interior method's history: the processing section says kriging for
the 1993 to 2016 data and streamline diffusion from the 2017 data,
and the Version 4 history entry says streamline diffusion was
implemented in the interior beginning January 2017; this concept
reads them as one statement.[^idbmg4-user-guide] Morlighem and others
2017 and 2020 were verified against the Crossref registry (title,
authors, journal, year, volume and pages) on 2026-09-15; the 2017
abstract is on the registry record and is what this concept quotes,
while the Wiley and Nature journal pages were not read from the
drafting session (the Wiley page returned a bot check; the Nature
page is outside the domains the seed was permitted to read), so the
2020 paper is cited on its record and on the guide's account of the
method.[^morlighem-2017][^morlighem-2020]

[^idbmg4-page]: NSIDC product page, IceBridge BedMachine Greenland Version 6
[^idbmg4-user-guide]: IceBridge BedMachine Greenland Version 6 user guide, NSIDC
[^nsidc-0756-page]: NSIDC product page, MEaSUREs BedMachine Antarctica Version 4
[^nsidc-0756-user-guide]: MEaSUREs BedMachine Antarctica Version 4 user guide, NSIDC
[^idbmg4-v5-page]: NSIDC product page, IceBridge BedMachine Greenland Version 5 (retired)
[^nsidc-0756-v3-page]: NSIDC product page, MEaSUREs BedMachine Antarctica Version 3 (retired)
[^idbmg4-v5-user-guide]: IceBridge BedMachine Greenland Version 5 user guide (retired), NSIDC
[^nsidc-0756-v3-user-guide]: MEaSUREs BedMachine Antarctica Version 3 user guide (retired), NSIDC
[^cmr-idbmg4]: CMR collection record for IDBMG4
[^cmr-nsidc-0756]: CMR collection record for NSIDC-0756
[^morlighem-2017]: Morlighem and others, 2017, Geophysical Research Letters, doi:10.1002/2017GL074954
[^morlighem-2020]: Morlighem and others, 2020, Nature Geoscience, doi:10.1038/s41561-019-0510-8
[^basins-gotcha]: This bundle's ice sheet boundaries and drainage basins gotcha
