---
type: dataset-gotcha
spheres: [cryosphere]
title: "The 15 percent threshold defines extent, and extent is not area: the two series answer different questions and are not interchangeable"
description: "Sea ice extent is the summed true area of every grid cell whose concentration is 15 percent or more, with the Arctic pole hole counted as ice; sea ice area is the same sum with each cell weighted by its concentration and the pole hole left out, so area is always the smaller. The threshold is a convention the Sea Ice Index calls somewhat arbitrary, concentration inside the edge carries the larger errors (plus or minus 15 percent in the melt season against plus or minus 5 in winter), and a monthly value is the average of daily totals rather than a total of the monthly mean map. A number quoted as ice cover without the quantity, the threshold, the pole hole treatment and the averaging order named is not comparable with another."
tags: [sea-ice, sea-ice-extent, sea-ice-area, 15-percent, threshold, g02135, sea-ice-index, nsidc-0051, nasa-team, pole-hole]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:30:00Z }
severity: medium
# medium: both products document the two definitions on their pages
# and guides, the monthly files carry both columns side by side so the
# gap is visible, and a mismatch is caught by the check that area is
# always below extent; the error is a comparison of unlike quantities
# rather than a silently corrupted number.
dataset: ../datasets/sea-ice-index-g02135.md
status: draft
stale_after: 2027-03-14
sources:
  - id: g02135-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/g02135-v004-userguide.pdf
    title: "Sea Ice Index Version 4 user guide: the extent and area calculations with the cell-area files, the pole hole in each, the monthly average as the average of daily values, the 15 percent cutoff called somewhat arbitrary with 20 and 30 percent giving different numbers, the monthly image made from the monthly mean field, the ambiguity of a monthly mean concentration, and the accuracy figures"
  - id: sii-special-report-19
    resource: https://nsidc.org/sites/default/files/nsidc-special-report-19.pdf
    title: "NSIDC Special Report 19 (2017): Version 3 changed the monthly values to the average of the daily hemisphere-wide values; Version 2 computed them from the monthly mean concentration image; neither is more correct, and the image method is kept for the images"
  - id: nsidc-0051-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/nsidc-0051-v002-userguide.pdf
    title: "NSIDC-0051 Version 2 user guide: the recommendation that extent and area be computed from daily grids and then averaged, not from monthly mean maps; the calibration that minimized extent and area differences; the accuracy figures"
  - id: nsidc-0051-page
    resource: https://nsidc.org/data/nsidc-0051/versions/2
    title: "NSIDC-0051 product page: the limitation that concentration is underestimated in the melt season and for thin ice"
  - id: sensor-change-assessment
    resource: https://nsidc.org/sites/default/files/documents/technical-reference/pm_seaice_assessment_amsr2-ssmis.pdf
    title: "Meier, 2026, sensor-change assessment: the definitions of area and extent, and the differing size of the AMSR2 biases in extent and in area"
  - id: noaadata-g02135
    resource: https://noaadata.apps.nsidc.org/NOAA/G02135/north/monthly/data/
    title: "The Sea Ice Index September monthly file, read 2026-09-14: extent and area side by side"
  - id: dataset
    resource: ../datasets/sea-ice-index-g02135.md
    title: "This bundle's Sea Ice Index concept, which lists this trap among the known issues"
  - id: nsidc-0051-dataset
    resource: ../datasets/nsidc-0051-sea-ice-concentration.md
    title: "This bundle's NSIDC-0051 dataset concept, which lists this trap among the known issues"
  - id: projection-gotcha
    resource: polar-stereographic-not-latlon.md
    title: "This bundle's polar stereographic gotcha: cell area varies with latitude on these grids"
---

# The 15 percent threshold defines extent, and extent is not area

**Mechanism.** In the Sea Ice Index, and in the passive microwave
record generally, extent is the area covered by at least 15 percent
concentration ice and area is the total surface area covered by ice:
daily extent counts each grid cell as either zero or its true area
depending on whether it passes the 15 percent cutoff, and daily area
multiplies each passing cell's true area by its concentration, so a
600 km2 cell at 75 percent contributes 600 km2 to extent and 450 km2
to area.[^g02135-user-guide][^sensor-change-assessment] The true area
comes from the NSIDC-0771 cell-area files, 382 to 664 km2 in the north
and 443 to 664 km2 in the south rather than the nominal 625 km2,
because the grids are polar stereographic (the projection gotcha in
this bundle).[^g02135-user-guide][^projection-gotcha] The region
under the Arctic pole hole is assumed to be ice above 15 percent and
counted in extent, and is left out of area, so area is always less
than extent and the two differ by more than the concentration
deficit alone; the September 2025 row of the monthly file reads
4.75 million km2 of extent against 3.08 of
area.[^g02135-user-guide][^noaadata-g02135] The 15 percent contour is
the convention for the ice edge because a March 1988 aircraft
comparison found that it matched the observed edge, and the Index's
guide states that the cutoff is somewhat arbitrary, that 20 or
30 percent gives different numbers with similar trends, that values
below 15 percent are too uncertain to use and are treated as zero, and
that an individual extent value has uncertain
significance.[^g02135-user-guide] The monthly values are a further
convention: since Version 3 the monthly extent and area are the
averages of the daily hemisphere-wide values, whereas Version 2 took
them from the monthly mean concentration map with the cutoff applied,
and the two methods give different numbers, neither more correct; the
monthly images are still made by the map method, and the NSIDC-0051
guide's own recommendation is that extent and area be computed from
daily grids and then averaged because the monthly mean map can bias
the series.[^sii-special-report-19][^g02135-user-guide][^nsidc-0051-user-guide]
The two quantities also carry different errors: the concentration
inside the edge is accurate to about plus or minus 5 percent in
winter and plus or minus 15 percent in the Arctic melt season and is
underestimated over melting and thin ice, while the edge itself rests
on the large emissivity contrast between water and ice, which is why
the Index calls its extent images more reliable than its
concentration images; the AMSR2 assessment shows the same asymmetry,
with Arctic area biased low by a consistent 100,000 to 200,000 km2
where extent is biased low only in
summer.[^g02135-user-guide][^nsidc-0051-page][^sensor-change-assessment]

**Wrong-result mode.** An area series set beside an extent series, a
model's ice area compared with the Index's extent, or a climatology
built from one and an anomaly from the other, reads the definitional
gap of roughly a third of the September value as a discrepancy or a
trend.[^noaadata-g02135] An extent computed with a different cutoff,
or from a monthly mean map instead of daily grids, differs from the
Index's value for the same month while carrying the same name, and the
difference is not a data error on either side.[^g02135-user-guide][^sii-special-report-19]
An area trend read as an extent trend, or the reverse, mixes a signal
that concentration errors and melt ponds affect strongly with one they
affect weakly, and an Arctic area series crosses the pole hole
discontinuities that extent does not (its own
gotcha).[^g02135-user-guide][^nsidc-0051-page] A monthly mean
concentration of 50 percent read as half-covered ice may be full cover
for half the month and open water for the other half.[^g02135-user-guide]

**Correct approach.** A sea ice cover number states its quantity
(extent or area), its threshold, its pole hole treatment and, for a
monthly value, whether it is the average of daily totals or a total of
the monthly mean map, and a comparison holds all four fixed on both
sides; the Sea Ice Index's monthly files carry both quantities under
one definition, and the NSIDC-0051 daily grids with the NSIDC-0771 cell
areas reproduce them.[^g02135-user-guide][^nsidc-0051-user-guide] The
sensor intercalibration of NSIDC-0051 was tuned on hemispheric extent
and area, so those are the totals the record was built to keep
continuous, and a regional or concentration-weighted statement inherits
less of that tuning.[^nsidc-0051-user-guide]

**Verification.** The extent and area processing steps, the pole hole
treatment, the cutoff caveat and the accuracy figures were read in the
Version 4 guide on 2026-09-14, the Version 3 change in Special
Report 19's summary the same day, and the recommendation on daily
versus monthly computation in the NSIDC-0051 guide; the September
monthly file was read from the NOAA archive and area is below extent
in every row inspected.[^g02135-user-guide][^sii-special-report-19][^nsidc-0051-user-guide][^noaadata-g02135]
The two dataset concepts list this trap among their known
issues.[^dataset][^nsidc-0051-dataset]

[^g02135-user-guide]: Sea Ice Index Version 4 user guide, NSIDC
[^sii-special-report-19]: Windnagel and others, 2017, NSIDC Special Report 19
[^nsidc-0051-user-guide]: NSIDC-0051 Version 2 user guide, NSIDC
[^nsidc-0051-page]: NSIDC product page, NSIDC-0051 Version 2
[^sensor-change-assessment]: Meier, 2026, sensor-change assessment, NSIDC DAAC
[^noaadata-g02135]: The Sea Ice Index monthly files on the NOAA at NSIDC archive
[^dataset]: This bundle's Sea Ice Index concept
[^nsidc-0051-dataset]: This bundle's NSIDC-0051 dataset concept
[^projection-gotcha]: This bundle's polar stereographic gotcha
