---
type: dataset-gotcha
spheres: [cryosphere]
title: "BedMachine thickness between flight lines is mass conservation or an interpolation, not a measurement: source, dataid and errbed say which method made each pixel and how far to trust it"
description: "The radar flight lines are sparse; BedMachine fills the space between them with mass conservation where the ice flows fast, with kriging, streamline diffusion or ice flow perturbation analysis in the slow interior, and with hydrostatic equilibrium on floating ice, then stitches the pieces with inverse distance weighting. The thickness at any pixel is therefore a model value whose error the errbed field gives, from 36 m under dense radar coverage to more than 50 m in south Greenland, more than 200 m in East Antarctica and more than 500 m where nothing was sounded, and the source and dataid fields say which method and which data stand behind it. A thickness, a bed depth, a trough or a discharge read from the grid without those fields carries an error that can be a large fraction of the value, and reads a stated 150 m or 500 m grid as a resolution the guide puts at 150 m to 5 km."
tags: [bedmachine, idbmg4, nsidc-0756, ice-thickness, mass-conservation, interpolation, kriging, errbed, source, dataid, flight-lines, discharge, flux-gate, greenland, antarctica]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T13:30:00Z }
severity: high
# high: nothing in the thickness field marks a pixel as inferred rather
# than sounded, the grid spacing reads as a resolution, and a discharge
# or a bed depth read without errbed, source and dataid is silently
# wrong by an amount the product itself states; the eval case tests
# whether an agent reads the three fields beside the thickness.
dataset: ../datasets/bedmachine-greenland-antarctica.md
eval_case: bedmachine-thickness-is-interpolated
status: draft
stale_after: 2027-03-15
sources:
  - id: idbmg4-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/idbmg4-v006-userguide.pdf
    title: "IceBridge BedMachine Greenland Version 6 user guide: the parameter table with the source and dataid codes and errbed, the true resolution of 150 m to 5 km, the processing section (mass conservation in fast flow, kriging then streamline diffusion in the interior) and the error statement, read in full 2026-09-15"
  - id: nsidc-0756-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/nsidc-0756-v004-userguide.pdf
    title: "MEaSUREs BedMachine Antarctica Version 4 user guide: the parameter table with the source and dataid codes and errbed, the methods by ice regime, the stitching of the mass conservation maps with inverse distance weighting, the error statement and the 47 radar campaigns, read in full 2026-09-15"
  - id: morlighem-2017
    resource: https://doi.org/10.1002/2017GL074954
    title: "Morlighem and others, 2017, BedMachine v3: Complete Bed Topography and Ocean Bathymetry Mapping of Greenland From Multibeam Echo Sounding Combined With Mass Conservation, Geophysical Research Letters 44: the abstract's statement that the compilation assimilates bathymetry and thickness data through a mass conservation approach, record and abstract verified against the Crossref registry 2026-09-15"
  - id: morlighem-2020
    resource: https://doi.org/10.1038/s41561-019-0510-8
    title: "Morlighem and others, 2020, Deep glacial troughs and stabilizing ridges unveiled beneath the margins of the Antarctic ice sheet, Nature Geoscience 13, 132 to 137: the paper the Antarctic guide cites for the error figures and the campaign table, record verified against the Crossref registry 2026-09-15"
  - id: gardner-2018
    resource: https://doi.org/10.5194/tc-12-521-2018
    title: "Gardner and others, 2018, Increased West Antarctic and unchanged East Antarctic ice discharge over the last 7 years, The Cryosphere 12, 521 to 547: the abstract's Antarctic discharge through an optimized flux gate with its stated uncertainty, record and abstract verified against the Crossref registry 2026-09-15"
  - id: dataset
    resource: ../datasets/bedmachine-greenland-antarctica.md
    title: "This bundle's BedMachine dataset concept, which lists this trap among the known issues"
---

# BedMachine thickness between flight lines is mass conservation or an interpolation

**Mechanism.** BedMachine's thickness field is continuous over each
ice sheet, but the measurements behind it are airborne radar
soundings along flight lines: Operation IceBridge MCoRDS and the
other sounders in Greenland, 47 campaigns flown between 1967 and 2020
in Antarctica.[^idbmg4-user-guide][^nsidc-0756-user-guide] Between
the lines the thickness is computed. Where the ice flows fast the
method is mass conservation, which combines the sparse radar
thickness with the satellite ice motion and the surface mass balance
to solve the mass conservation equation while minimizing the
departure from the radar data; the guides state that it works best in
well-confined fast flow (above 30 m per year in the Antarctic guide's
words) where errors in flow direction are small and the glacier
slides on its bed.[^idbmg4-user-guide][^nsidc-0756-user-guide] In the
slow interior, where flow direction errors are larger, Greenland
uses kriging for the 1993 to 2016 data and streamline diffusion from
the 2017 data, and Antarctica uses ice flow perturbation analysis, an
inversion of the surface for the bed adopted because kriging, splines
and streamline diffusion do not reproduce the roughness seen along
radar profiles; floating ice takes hydrostatic equilibrium, and
beneath grounded ice shelves gravity inversion and seismic
bathymetry stand in.[^idbmg4-user-guide][^nsidc-0756-user-guide] The
Antarctic guide states that the individual mass conservation maps
are then stitched together, constrained by flight lines along their
boundaries, using inverse distance weighting, and combined with the
streamline diffusion maps.[^nsidc-0756-user-guide] The file records
all of this per pixel: source gives the method (in Greenland 2 mass
conservation, 3 synthetic, 4 interpolation, 5 hydrostatic
equilibrium, 6 kriging, 9 IceBoost, among others; in Antarctica
2 mass conservation, 3 interpolation, 4 hydrostatic, 5 ice flow
perturbation analysis, 6 gravity, 7 seismic, 8 IceBoost), dataid
gives the input data where there is one (radar, seismic, multibeam,
or none), and errbed gives the bed topography and ice thickness
error in metres.[^idbmg4-user-guide][^nsidc-0756-user-guide] The
guides put that error at 36 m in a trial with unusually dense radar
coverage, only slightly above the radar data's own, above 50 m in
areas of south Greenland constrained by one track or less, above
200 m in such areas of East Antarctica, and above 500 m in Greenland
fjords with little or no data and where ice shelf bathymetry is
sparse; the Greenland guide states that the output is generated at
150 m while the true resolution varies between 150 m and
5 km.[^idbmg4-user-guide][^nsidc-0756-user-guide] The method papers
describe the same construction, a compilation that assimilates
bathymetry and thickness data through mass
conservation.[^morlighem-2017][^morlighem-2020]

**Wrong-result mode.** The thickness variable looks the same at a
sounded pixel and at a kriged one: both are metres on the same grid,
and no fill value marks the difference. A thickness read at a point
between flight lines, a bed depth or the depth of a trough read from
bed, a bed slope or a retrograde reach inferred from the grid, an ice
volume summed over a basin, or a discharge that multiplies a velocity
by this thickness across a gate, each carries the errbed of the
pixels it used, and where those pixels are one-track or no-data
pixels that error is tens to hundreds of metres.[^idbmg4-user-guide][^nsidc-0756-user-guide]
A gate placed in the slow interior sits where the thickness is
kriging, streamline diffusion or a perturbation inversion rather than
mass conservation, so the flux there is a model quantity that the
method was not designed to conserve.[^idbmg4-user-guide][^nsidc-0756-user-guide]
A feature narrower than the local true resolution, which reaches
5 km in Greenland, is not resolved whatever the 150 m posting
suggests.[^idbmg4-user-guide] A discharge quoted with the velocity
mosaic's error alone, or with no error, omits the thickness term that
the reference computation carries: Gardner and others 2018 report
Antarctic discharge through an optimized flux gate as 1929 gigatonnes
per year in 2015 with an uncertainty of 40, a figure that includes
the thickness at the gate.[^gardner-2018]

**Correct approach.** A number read from BedMachine is read with its
three companion fields: source at the same pixels (which method),
dataid (which data, or none) and errbed (how far to trust it), and
the statement names the product, its version and its nominal year
(2007 for Greenland, 2015 for Antarctica) beside the
value.[^idbmg4-user-guide][^nsidc-0756-user-guide] A discharge gate
sits where source is mass conservation, near the flight lines that
constrain it, on the fast-flowing trunk the method was built for,
and the thickness error along the gate enters the discharge
uncertainty as its own term beside the velocity error, which is how
Gardner and others 2018 voice their flux-gate
discharge.[^nsidc-0756-user-guide][^idbmg4-user-guide][^gardner-2018]
A bed feature is stated with the local errbed and the source code of
the pixels it spans, and a feature narrower than the true resolution
the guide gives is not a claim the product
supports.[^idbmg4-user-guide] A volume or a mean thickness over a
region is voiced with the fraction of its pixels that are sounded
(dataid) and with errbed summed over the region as an error whose
spatial correlation the guides do not
state.[^idbmg4-user-guide][^nsidc-0756-user-guide]

**Verification.** The Greenland guide's parameter table gives the
source, dataid and errbed definitions, its resolution section gives
150 m to 5 km, its processing section gives mass conservation,
kriging and streamline diffusion by regime and its quality section
gives 36 m, 50 m and 500 m; the Antarctic guide's parameter table
gives its own source and dataid codes, its processing section gives
the methods by regime and the inverse distance weighting stitch, and
its quality section gives 36 m, 200 m and 500 m; both read in full on
2026-09-15.[^idbmg4-user-guide][^nsidc-0756-user-guide] Morlighem
and others 2017 and 2020 and Gardner and others 2018 are cited on
their Crossref records (title, authors, journal, year, volume and
pages verified 2026-09-15) and, for 2017 and 2018, on their registry
abstracts; the Wiley journal page returned a bot check and the
Nature and Copernicus pages were not read from the drafting
session.[^morlighem-2017][^morlighem-2020][^gardner-2018] No granule
was opened, so the codes come from the guides' tables. The dataset
concept lists this trap among the product's known
issues.[^dataset]

[^idbmg4-user-guide]: IceBridge BedMachine Greenland Version 6 user guide, NSIDC
[^nsidc-0756-user-guide]: MEaSUREs BedMachine Antarctica Version 4 user guide, NSIDC
[^morlighem-2017]: Morlighem and others, 2017, Geophysical Research Letters, doi:10.1002/2017GL074954
[^morlighem-2020]: Morlighem and others, 2020, Nature Geoscience, doi:10.1038/s41561-019-0510-8
[^gardner-2018]: Gardner and others, 2018, The Cryosphere, doi:10.5194/tc-12-521-2018
[^dataset]: This bundle's BedMachine dataset concept
