---
type: dataset-gotcha
spheres: [cryosphere]
title: "The BedMachine mask separates ocean, ice-free land, grounded ice and floating ice, and a discharge gate sits on grounded ice upstream of the grounding line, where the thickness is mass conservation and not hydrostatic"
description: "BedMachine's mask is 0 ocean, 1 ice-free land, 2 grounded ice and 3 floating ice (Antarctica adds 4 for Lake Vostok), and the thickness field is made by different methods on either side of the 2 to 3 boundary: mass conservation constrained by radar on grounded ice, hydrostatic equilibrium from the surface with a firn correction on floating ice. The bed under ocean is bathymetry, the bed under ice-free land is the surface model itself, and the Antarctic surface and thickness are ice equivalent with the firn air content removed. An ice-sheet discharge is the flux across the grounding line, so its gate sits on grounded ice (mask 2) upstream of the transition to floating ice; a gate on the shelf multiplies a hydrostatic thickness by a shelf velocity and counts ice that has already crossed the line."
tags: [bedmachine, idbmg4, nsidc-0756, mask, grounded-ice, floating-ice, grounding-line, ice-shelf, hydrostatic, discharge, flux-gate, firn-air-content, greenland, antarctica]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T13:30:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-15T14:22:23Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/162 }
severity: medium
# medium: the mask codes and the method per regime are in the guides'
# parameter tables and processing sections, and the source field marks
# hydrostatic pixels; the error bites through a gate placed by eye on a
# map rather than through a silently wrong number from the product
# alone; no eval case is required.
dataset: ../datasets/bedmachine-greenland-antarctica.md
status: stable
stale_after: 2027-03-15
sources:
  - id: idbmg4-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/idbmg4-v006-userguide.pdf
    title: "IceBridge BedMachine Greenland Version 6 user guide: the mask codes, the source code 5 for hydrostatic equilibrium, the surface as the GIMP model relative to the geoid and the bed as that model minus the thickness, read in full 2026-09-15"
  - id: nsidc-0756-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/nsidc-0756-v004-userguide.pdf
    title: "MEaSUREs BedMachine Antarctica Version 4 user guide: the mask codes including Lake Vostok, hydrostatic equilibrium with a calibrated firn correction on floating ice shelves and continuity across the grounding line, the ice equivalent convention and the firn variable, the bed over ice-free land as REMA, and the statement that mass conservation keeps grounding-line fluxes compatible with accumulation and thinning, read in full 2026-09-15"
  - id: idbmg4-v5-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/idbmg4-v005-userguide.pdf
    title: "IceBridge BedMachine Greenland Version 5 user guide (retired version): its parameter table, whose mask carries 4 for non-Greenland land, read 2026-09-15 for that table"
  - id: gardner-2018
    resource: https://doi.org/10.5194/tc-12-521-2018
    title: "Gardner and others, 2018, Increased West Antarctic and unchanged East Antarctic ice discharge over the last 7 years, The Cryosphere 12, 521 to 547: the abstract's discharge through an optimized flux gate and the flow accelerations across the grounding lines that account for its increase, record and abstract verified against the Crossref registry 2026-09-15"
  - id: morlighem-2017
    resource: https://doi.org/10.1002/2017GL074954
    title: "Morlighem and others, 2017, BedMachine v3, Geophysical Research Letters 44: the abstract's statement that bed topography is a primary control on grounding line migration and that the map has seamless transitions at the ice and ocean interface, record and abstract verified against the Crossref registry 2026-09-15"
  - id: dataset
    resource: ../datasets/bedmachine-greenland-antarctica.md
    title: "This bundle's BedMachine dataset concept, which lists this trap among the known issues"
---

# The BedMachine mask and the grounding line

**Mechanism.** Both BedMachine files carry a mask with the values
0 ocean, 1 ice-free land, 2 grounded ice and 3 floating ice, and the
Antarctic file adds 4 for Lake Vostok; the retired Greenland
Version 5 guide's table used 4 for non-Greenland land, a value the
Version 6 table no longer
lists.[^idbmg4-user-guide][^nsidc-0756-user-guide][^idbmg4-v5-user-guide]
The boundary between 2 and 3 is where the thickness field changes
method: on grounded ice it is mass conservation constrained by the
radar lines (or the interior interpolation methods), and on floating
ice it is hydrostatic equilibrium, the thickness inferred from the
surface elevation with a calibrated firn depth correction that the
Antarctic guide states is applied to keep the inferred thicknesses
consistent with the available ice shelf thickness data and to ensure
continuity across the grounding line; the Greenland source code 5
and the Antarctic source code 4 mark those
pixels.[^nsidc-0756-user-guide][^idbmg4-user-guide] Beyond the ice
the bed is still defined: under mask 0 it is the ocean bathymetry
compiled from soundings and the bathymetric charts, and under mask 1
it is the surface model itself (GIMP in Greenland, REMA in
Antarctica), so the bed variable is continuous from the interior to
the fjord and the shelf cavity, which the Greenland method paper
describes as seamless transitions at the ice and ocean
interface.[^idbmg4-user-guide][^nsidc-0756-user-guide][^morlighem-2017]
In Antarctica the surface and the thickness are in ice equivalent,
with the firn air content removed and carried separately as the firn
variable, so the surface of the snow is surface plus
firn.[^nsidc-0756-user-guide] The Antarctic guide states the purpose
of the mass conservation construction as ensuring that the
grounding-line fluxes are compatible with snowfall accumulation and
thinning rates in the interior, and the discharge that closes an ice
sheet mass budget is that flux across the grounding line: Gardner and
others 2018 compute the Antarctic discharge through an optimized flux
gate and attribute its increase to flow accelerations across the
grounding lines of the sectors they name.[^nsidc-0756-user-guide][^gardner-2018]

**Wrong-result mode.** A gate drawn across a glacier on a map of
speed, without the mask, can land on the floating tongue or the ice
shelf: there the thickness is hydrostatic (source 5 in Greenland,
4 in Antarctica), inferred from the surface and a firn assumption
rather than constrained by radar or by the conservation equation, and
the ice crossing that gate has already crossed the grounding line, so
the flux is a shelf flux, less whatever the shelf lost between the
line and the gate, and it is not the flux across the grounding line
that Gardner and others 2018 compute as the ice sheet's
discharge.[^nsidc-0756-user-guide][^idbmg4-user-guide][^gardner-2018] A mean
thickness or an ice volume summed over a bounding box without the
mask includes floating ice at hydrostatic thickness and, where bed
and surface are read instead of thickness, includes ocean and land
pixels where bed minus surface is not ice; in a Greenland Version 5
file the box also holds pixels at mask value 4, non-Greenland land
(Ellesmere Island and Iceland lie inside the grid's extent), whose
thickness is not the ice sheet's.[^idbmg4-user-guide][^nsidc-0756-user-guide][^idbmg4-v5-user-guide]
An Antarctic surface elevation compared with an altimeter's or with
REMA without adding the firn variable back differs by the firn air
content, which is a metres-scale quantity the file carries for that
reason.[^nsidc-0756-user-guide] A grounding line taken from the mask
is the line of the product's nominal year and its mask sources, not
of the date of the velocity it is combined with, and the method paper
names bed topography as a primary control on where that line
migrates.[^idbmg4-user-guide][^nsidc-0756-user-guide][^morlighem-2017]

**Correct approach.** A discharge gate is placed on pixels whose mask
is 2 and whose source is mass conservation, upstream of the first
mask 3 pixel along the flowline, and the statement names the product
version, the nominal year and the mask it used to place the gate
beside the velocity mosaic's epoch; the flux across the grounding
line is the quantity the Antarctic guide describes the method as
conserving and the quantity the reference computation
reports.[^nsidc-0756-user-guide][^idbmg4-user-guide][^gardner-2018]
A regional thickness, volume or bed statement is masked to the ice
class it means (grounded, floating or both) and says so; a bed depth
under the ocean is a bathymetry with the dataid of its soundings or
none; and an Antarctic surface used beside a snow-surface height is
surface plus firn.[^idbmg4-user-guide][^nsidc-0756-user-guide]

**Verification.** The mask codes come from the parameter tables of
both guides, the hydrostatic method, the firn correction and the
grounding-line continuity from the Antarctic guide's processing
section, the ice equivalent convention from its firn air correction
section, the source codes from both parameter tables, and the bed
over ice-free land from both processing sections; all read in full
on 2026-09-15, and the retired Version 5 Greenland guide's table was
read the same day for its mask value 4.[^idbmg4-user-guide][^nsidc-0756-user-guide][^idbmg4-v5-user-guide] Gardner
and others 2018 and Morlighem and others 2017 are cited on their
Crossref records and registry abstracts (verified 2026-09-15); the
journal pages were not read from the drafting session (the Wiley page
returned a bot check).[^gardner-2018][^morlighem-2017] No granule was
opened. The dataset concept lists this trap among the product's known
issues.[^dataset]

[^idbmg4-user-guide]: IceBridge BedMachine Greenland Version 6 user guide, NSIDC
[^nsidc-0756-user-guide]: MEaSUREs BedMachine Antarctica Version 4 user guide, NSIDC
[^idbmg4-v5-user-guide]: IceBridge BedMachine Greenland Version 5 user guide (retired), NSIDC
[^gardner-2018]: Gardner and others, 2018, The Cryosphere, doi:10.5194/tc-12-521-2018
[^morlighem-2017]: Morlighem and others, 2017, Geophysical Research Letters, doi:10.1002/2017GL074954
[^dataset]: This bundle's BedMachine dataset concept
