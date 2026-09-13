---
type: dataset-gotcha
spheres: [cryosphere]
title: "ATL15 height change is not mass change: the conversion needs a firn model and a density assumption the product does not carry"
description: "ATL15 delta_h and dhdt are changes in the height of the ice sheet surface. A mass change follows only after the change in firn air content is removed with a firn densification model and the remainder is multiplied by an assumed density, and each step carries an uncertainty the product's error fields do not contain. A dh/dt sum quoted in gigatonnes without a named firn model and its uncertainty is a volume change with a density label, and it misstates the mass balance wherever accumulation or melt has changed the firn."
tags: [icesat2, atl15, height-change, mass-balance, firn, firn-air-content, density, sea-level, greenland, antarctica]
generated: { by: knowledge-seeder/claude, at: 2026-09-13T20:30:00Z }
severity: high
dataset: ../datasets/icesat2-atl15.md
eval_case: atl15-height-change-is-not-mass-change
status: draft
stale_after: 2027-03-13
sources:
  - id: atl14-15-atbd
    resource: https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl14_atl15_atbd_v005.pdf
    title: "Smith and others, ICESat-2 ATBD for Land Ice DEM (ATL14) and Land Ice Height Change (ATL15), release 005, November 2025: what the product corrects (tides, dynamic atmosphere on floating ice) and the absence of any firn, density or isostatic term"
  - id: atl15-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/atl15-v005-userguide.pdf
    title: "ATL15 Version 5 user guide: the product is land ice height change and change rates; delta_h_sigma and data_count are the quality fields"
  - id: atl15-data-dict
    resource: https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl15_data_dict_v5.pdf
    title: "ATL15 data dictionary, version 5: delta_h in metres relative to the 1 January 2020 surface, delta_h_sigma its estimated error, ice_area in square metres"
  - id: smith-2020
    resource: https://doi.org/10.1126/science.aaz5845
    title: "Smith and others, 2020, Pervasive ice sheet mass loss reflects competing ocean and atmosphere processes, Science 368, 1239 to 1242: height change from ICESat and ICESat-2 combined with a new firn model gives grounded and floating mass change"
  - id: smith-2020-ntrs
    resource: https://ntrs.nasa.gov/api/citations/20210011704/downloads/Pervasive%20row%2033.pdf
    title: "The NASA technical reports server copy of Smith and others 2020 (record 20210011704), read in full: the corrections applied to obtain equivalent changes in mass"
  - id: smith-2020-supplement
    resource: https://ntrs.nasa.gov/api/citations/20210011704/downloads/supplementary%20row%2033.pdf
    title: "Supplementary materials of Smith and others 2020 (NASA technical reports server copy): the firn air content correction, the firn model it needs, and the correlated error term for firn air content trends"
  - id: dataset
    resource: ../datasets/icesat2-atl15.md
    title: "This bundle's ATL15 dataset concept, which lists this trap among the known issues"
---

# ATL15 height change is not mass change

**Mechanism.** ATL15 gives the height of the ice sheet surface
relative to the ATL14 reference surface at each quarterly epoch, and
the rates of that height over quarterly to six-year windows; delta_h
and dhdt are in metres and their errors are errors of a surface height
fit.[^atl15-user-guide][^atl15-data-dict] The algorithm removes ocean
tides and the dynamic atmosphere from floating ice and applies no
other geophysical correction: the ATBD contains no firn, density or
glacial isostatic adjustment term, and its abstract describes the
error estimates as intended to allow error propagation for mass-change
estimates, which is to say the propagation is the user's.[^atl14-15-atbd]
The surface of an ice sheet moves for reasons that carry no ice mass:
the firn's thickness and air content change with anomalies in snow
accumulation, skin temperature and surface melt, which are the three
forcings a firn densification model takes, and the column-averaged
density changes with them.[^smith-2020-supplement] Converting a height change
into a mass change therefore means computing the change in the total
firn air content over the interval with a firn densification model
driven by a climate forcing, removing it from the measured height
change, and multiplying what remains by a density; Smith and others
2020 did exactly this for ICESat and ICESat-2, with a customized firn
correction beside glacial isostatic adjustment, elastic compensation,
tides and the inverse barometer, because published firn model runs did
not reach the ICESat-2 epoch.[^smith-2020][^smith-2020-ntrs][^smith-2020-supplement]
The firn air content trend has its own uncertainty, which that study
carried as a correlated error term beside the altimetry bias and the
isostatic adjustment error; its firn simulations were run at a
temporal resolution chosen so that the resulting error in the firn air
content trend stayed below 0.4 centimetres per year, the ICESat-2
science requirement it matched to the height change itself.[^smith-2020-supplement]

**Wrong-result mode.** A dh/dt field summed over an ice sheet and
multiplied by the density of ice reads as a mass balance in
gigatonnes per year, and nothing in the product objects: the fields
are in metres, the errors are surface-fit errors, and no variable is
named firn. Where accumulation has risen, the firn thickens and the
surface rises at a density well below ice, so the ice-density product
overstates a mass gain; where melt has increased, the firn compacts
and the surface falls without ice leaving, so it overstates a mass
loss; the firn's thickness and air content follow the anomalies of
the surface climate, and the interiors of both ice sheets are where
Smith and others 2020 found the gains from increased snow
accumulation that partially offset the coastal
losses.[^smith-2020-supplement][^smith-2020]
The number then carries only delta_h_sigma propagated through the sum,
while the reference conversion carries the firn air content trend
error as its own correlated term beside the altimetry bias and the
isostatic adjustment error, so the stated interval omits a term the
conversion requires as well as the value being
biased.[^atl15-data-dict][^smith-2020-supplement] A comparison of such a number with a
GRACE mascon mass trend attributes the firn signal to a disagreement
between the two observing systems.

**Correct approach.** A mass statement from ATL15 names the firn model
that supplied the firn air content change over the same epochs and
region, the density applied to the firn-corrected height change, the
glacial isostatic adjustment model and any elastic correction, and
carries the firn air content uncertainty as a term beside the
propagated delta_h_sigma; Smith and others 2020 is the reference for
the conversion and for each of its terms, and this bundle carries no
firn air content product, so the firn model is an input the analysis
supplies and declares.[^smith-2020][^smith-2020-supplement] A volume
change, delta_h or dhdt times ice_area summed over cells, is the
statement ATL15 supports on its own, and it is voiced as a volume
change in cubic metres or cubic kilometres, with its epoch and lag
group, never as gigatonnes.[^atl15-data-dict][^atl14-15-atbd] The
mass side of the land ice budget is the GRACE mascon product in this
repository's podaac bundle; the altimetry and gravimetry numbers meet
only after the firn conversion, and their difference is a check on
that conversion rather than noise to be averaged away.

**Verification.** The ATBD's text was searched for firn, density and
isostatic terms and contains none; its corrections are the tide and
dynamic atmosphere models applied to floating ice, and its abstract
states the intent that users propagate the errors into mass-change
estimates.[^atl14-15-atbd] The data dictionary lists delta_h,
delta_h_sigma and ice_area with their units and no mass or density
variable.[^atl15-data-dict] Smith and others 2020 was read in full
from the NASA technical reports server copy (main text and
supplement) on 2026-09-13, which is where the list of corrections, the
firn air content method and its error term come from; the journal
page itself sits behind a bot check and was not reachable, and the
paper's record (title, authors, journal, year, volume and pages) was
verified against the Crossref registry the same
day.[^smith-2020][^smith-2020-ntrs][^smith-2020-supplement] The dataset
concept lists this trap among the product's known issues.[^dataset]

[^atl14-15-atbd]: ATL14/ATL15 ATBD, release 005
[^atl15-user-guide]: ATL15 Version 5 user guide, NSIDC
[^atl15-data-dict]: ATL15 data dictionary, version 5
[^smith-2020]: Smith and others, 2020, Science, doi:10.1126/science.aaz5845
[^smith-2020-ntrs]: Smith and others, 2020, NASA technical reports server copy
[^smith-2020-supplement]: Smith and others, 2020, supplementary materials
[^dataset]: This bundle's ATL15 dataset concept
