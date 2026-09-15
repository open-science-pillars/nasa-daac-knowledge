---
type: dataset-gotcha
spheres: [cryosphere]
title: "ATL10 freeboard is not sea ice thickness: total freeboard is the air and snow interface above the sea surface, and the conversion to thickness needs a snow depth and three densities the product does not carry"
description: "ATL10 gives total freeboard, the height of the air and snow interface above the local sea surface, per ATL07 segment and per beam. Ice thickness follows only through the hydrostatic balance, which scales the freeboard by the water and ice densities and subtracts a snow load term that needs the snow depth and the snow density, all from outside the product; the ICESat-2 mission produces no routine thickness product, the ATBD states that the snow depth is an external input and that the densities vary in space and time, and the Antarctic two-layer model is stated to be undemonstrated. A thickness formed from freeboard by a fixed factor, or a freeboard trend read as a thickness trend, carries the snow load assumption as its result."
tags: [icesat2, atl10, atl07, sea-ice, freeboard, total-freeboard, thickness, snow-depth, snow-load, hydrostatic, density, arctic, antarctic]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T13:30:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-15T14:22:23Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/162 }
severity: high
# high: the product's variable is called freeboard, nothing in it
# resists a multiplication by a factor, and a thickness so formed is
# silently wrong by the snow load, which is not in the product; the
# eval case tests whether an agent names the snow depth and density
# inputs and their uncertainty before quoting a thickness.
dataset: ../datasets/icesat2-atl10-freeboard.md
eval_case: atl10-freeboard-is-not-thickness
status: draft
stale_after: 2027-03-15
sources:
  - id: sea-ice-atbd
    resource: https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl07_10_20_21_atbd_v007.pdf
    title: "Kwok and others, ICESat-2 ATBD for Sea Ice Products, Release 007, 15 May 2025 (DOI 10.5067/KPMXUOH7TNIY): the background section's definition of total freeboard, the two-layer model, the Antarctic caveat, the hydrostatic thickness equation with its density scalings, the statement that snow depth is an external input and that no thickness product is routine, and the constraints section on subsurface scattering, read 2026-09-15"
  - id: atl10-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/atl10-v007-userguide.pdf
    title: "ATL10 Version 7 user guide: the background paragraph on total freeboard and the two-layered system, the freeboard estimation section, and the quality section on multiple scattering and the external snow correction, read in full 2026-09-15"
  - id: atl10-data-dict
    resource: https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl10_data_dict_v007.pdf
    title: "ATL10 data dictionary, Version 7: beam_fb_height as freeboard relative to beam_refsurf_height, beam_fb_unc as the combined uncertainty of the segment and reference surface sigmas, and the absence of any thickness, snow depth or density variable, read 2026-09-15"
  - id: atl07-10-known-issues
    resource: https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl07_10_known_issues_v007_0.pdf
    title: "ATL07 and ATL10 notes to users and known issues, release 007: the release 3 change to specular leads that raised composite freeboard means by 0 to 3 cm, and the length weighting of spatial statistics, read in full 2026-09-15"
  - id: kwok-2019-jgr
    resource: https://doi.org/10.1029/2019JC015486
    title: "Kwok and others, 2019, Surface Height and Sea Ice Freeboard of the Arctic Ocean From ICESat-2: Characteristics and Early Results, Journal of Geophysical Research: Oceans 124, 6942 to 6959: the first winter of surface heights and freeboards, record and abstract verified against the Crossref registry 2026-09-15"
  - id: dataset
    resource: ../datasets/icesat2-atl10-freeboard.md
    title: "This bundle's ATL10 dataset concept, which lists this trap among the known issues"
---

# ATL10 freeboard is not sea ice thickness

**Mechanism.** The quantity in ATL10 is total freeboard, defined in
the ATBD and the guide as the height of the air and snow interface
above the local sea surface; for the Arctic Ocean it is taken to be a
snow layer superimposed on the freeboard of the floating ice, a
two-layered system in which the total freeboard is the sum of the
snow thickness above the sea surface and the ice freeboard, and the
variable beam_fb_height is that height relative to the beam's
reference surface.[^sea-ice-atbd][^atl10-user-guide][^atl10-data-dict]
The ATBD states that a sea ice thickness product will not be
available as a routine product from the mission and that the science
requirement is to produce the parameters that let future
investigations convert freeboard to thickness; it gives the
conversion as the assumption that the floating ice is in isostatic
balance, so that thickness equals the total freeboard scaled by the
ratio of the seawater density to the difference of the seawater and
ice densities, minus the snow depth scaled by the ratio of the
seawater minus snow density difference to the seawater minus ice
density difference.[^sea-ice-atbd] The ice and snow densities are
stated to be time and space varying, with their residuals a source
of error, and the snow depth required to determine the snow loading
is stated to be an input from an external source.[^sea-ice-atbd] The
lidar's freeboard is the elevation of the air and snow interface on
the assumption of no penetration into the snow; the impact of
multiple scattering within the snow or ice volume is not quantified,
and a height correction for it would have to be determined
independently from external information about the snow
cover.[^sea-ice-atbd][^atl10-user-guide] For Antarctic sea ice, the
ATBD states that layering and snow-ice formation from flooded snow
make the situation more complex and that the efficacy of the simple
two-layer model for the Antarctic ice cover remains to be
demonstrated.[^sea-ice-atbd][^atl10-user-guide] The product carries
beam_fb_height and beam_fb_unc, the combined uncertainty of the
segment height sigma and the reference surface sigma, and no
variable for thickness, snow depth or density.[^atl10-data-dict]

**Wrong-result mode.** A freeboard multiplied by a single factor and
reported as thickness is the hydrostatic equation with the snow term
dropped or fixed: the ratio in front of the freeboard, the seawater
density over the difference of the seawater and ice densities, is
greater than one, so the thickness inherits more than the freeboard
error, and the subtracted snow term carries the snow depth
and snow density that the product does not have, so a thickness so
formed is wrong by the snow load wherever the assumed snow differs
from the real snow.[^sea-ice-atbd] A trend or a difference in
freeboard read as a trend in thickness attributes any change in snow
depth to the ice, because a thicker snow cover raises the air and
snow interface without adding ice; a comparison between regions or
seasons with different snow reads the snow difference as an ice
difference.[^sea-ice-atbd] The processing history is a freeboard
history, not a thickness one: the release 3 change to specular leads
alone raised the composite freeboard means by 0 to 3 cm, an amount a
density ratio multiplies.[^atl07-10-known-issues] In the Antarctic,
where the ATBD states the two-layer model is undemonstrated and
flooded snow forms snow ice, a thickness from the Arctic conversion
is a stronger assumption still.[^sea-ice-atbd] A freeboard whose
statistics are formed without weighting by segment length, which the
note states is how means and standard deviations of these
variable-length segments are to be formed, is biased before any
conversion begins.[^atl07-10-known-issues]

**Correct approach.** ATL10 supports a freeboard statement:
beam_fb_height with beam_fb_unc, the beam and the 10 km section it
belongs to, formed with segment-length weighting when averaged, and
voiced as total freeboard in metres.[^atl10-data-dict][^atl07-10-known-issues]
A thickness statement names the snow depth product or climatology
and the snow, ice and seawater densities it applied, carries the
snow depth and density uncertainties as terms beside the propagated
freeboard uncertainty through the hydrostatic equation, and states
the assumption of no penetration into the snow; in the Antarctic it
states that the two-layer model is the assumption the ATBD calls
undemonstrated.[^sea-ice-atbd] The early-results paper is the
reference for what the product measures, along-track surface heights
and total freeboards with a precision of about 2 cm, and it is a
freeboard paper.[^kwok-2019-jgr] This bundle carries no snow depth
product, so the snow load is an input the analysis supplies and
declares.

**Verification.** The ATBD's background section was read for the
freeboard definition, the two-layer model, the Antarctic caveat, the
hydrostatic equation, the density statement and the external snow
depth, and its constraints section for subsurface scattering; the
guide's background and quality sections say the same in shorter
form; the data dictionary was searched for thickness, snow and
density variables and has none; all read on
2026-09-15.[^sea-ice-atbd][^atl10-user-guide][^atl10-data-dict] The
known issues note gives the 0 to 3 cm change and the length
weighting.[^atl07-10-known-issues] Kwok and others 2019 is cited on
its Crossref record and abstract (verified 2026-09-15); the journal
page returned a bot check from the drafting
session.[^kwok-2019-jgr] The dataset concept lists this trap among
the product's known issues.[^dataset]

[^sea-ice-atbd]: ICESat-2 sea ice products ATBD, release 007, doi:10.5067/KPMXUOH7TNIY
[^atl10-user-guide]: ATL10 Version 7 user guide, NSIDC
[^atl10-data-dict]: ATL10 data dictionary, Version 7
[^atl07-10-known-issues]: ATL07 and ATL10 notes to users and known issues, release 007
[^kwok-2019-jgr]: Kwok and others, 2019, Journal of Geophysical Research: Oceans, doi:10.1029/2019JC015486
[^dataset]: This bundle's ATL10 dataset concept
