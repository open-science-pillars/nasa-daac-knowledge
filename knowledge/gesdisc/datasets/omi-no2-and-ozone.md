---
type: dataset
spheres: [atmosphere]
title: "OMI level 3 nitrogen dioxide and total ozone: the daily OMNO2d 0.25 degree grid with its Weight field and the daily TOMS-like OMTO3d 1 degree grid, gridded from row-anomaly-screened level 2 retrievals since October 2004"
description: "The Ozone Monitoring Instrument on Aura, gridded at GES DISC into two daily level 3 products: OMNO2d, the 0.25 by 0.25 degree total and tropospheric nitrogen dioxide columns with and without a 30 percent cloud screen plus a Weight field that is the only record of how much data a cell rests on, in collection 3 (product version 4.0) and collection 4 (product version 5.0, the forward stream since 2025); and OMTO3d, the 1 by 1 degree TOMS-like total ozone column with radiative cloud fraction, UV aerosol index and the two zenith angles, in versions 003 and 004 both in production, with OMTO3e and OMDOAO3e as the 0.25 degree best-pixel and DOAS siblings. Both are weighted averages of the level 2 pixels overlapping a cell after the row anomaly rows, the descending node and the poor-quality flags are excluded; no uncertainty field ships in either."
tags: [omi, aura, omno2d, omto3d, omto3e, omdoao3e, nitrogen-dioxide, no2, ozone, total-ozone, level-3, row-anomaly, gesdisc, atmosphere]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T13:30:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-15T13:59:41Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/161 }
resource: https://disc.gsfc.nasa.gov/datasets/OMNO2d_004/summary
version: "Concept ids and DOIs CMR-verified 2026-09-15, the DOIs resolving on doi.org the same day to the GES DISC pages: OMNO2d 004 C3333493715-GES_DISC (DOI 10.5067/Aura/OMI/DATA3407, product version 5.0 on collection 4 level 1B, first granule produced 2025-10-14, newest 2026-09-05) and OMNO2d 003 C1266136111-GES_DISC (DOI 10.5067/Aura/OMI/DATA3007, product version 4.0, newest granule 2026-03-15); OMTO3d 004 C3377057241-GES_DISC (DOI 10.5067/Aura/OMI/DATA3401, PGE 1.0.12, first granule produced 2024-10-18, newest 2026-09-13) and OMTO3d 003 C1266136070-GES_DISC (DOI 10.5067/Aura/OMI/DATA3001, PGE 1.0.7, newest granule 2026-09-13); OMTO3e 004 C3377057279-GES_DISC (10.5067/Aura/OMI/DATA3402); OMDOAO3e 003 C1266136037-GES_DISC (10.5067/Aura/OMI/DATA3005); the level 2 parents OMNO2 004 C3333494968-GES_DISC, OMTO3 004 C3377057082-GES_DISC and OMDOAO3 004 C3454342622-GES_DISC; every record begins 2004-10-01 with no end date"
sources:
  - id: cmr-omi
    resource: https://cmr.earthdata.nasa.gov/search/collections.json?short_name=OMNO2d&provider=GES_DISC
    title: "CMR collection search for OMNO2d, OMTO3d, OMTO3e, OMDOAO3e, OMNO2, OMTO3 and OMDOAO3 under the GES_DISC provider and the UMM records of each version (read 2026-09-15: concept ids, DOIs, the 2004-10-01 start with no end, the gridded resolutions, the abstracts, the document links and the publication references; the same day the granule search gave the first and newest granules of OMNO2d 003 and 004 and OMTO3d 003 and 004)"
  - id: gesdisc-omno2d
    resource: https://disc.gsfc.nasa.gov/datasets/OMNO2d_004/summary
    title: "GES DISC collection page for OMNO2d 004 (fetched 2026-09-15; the page is rendered by script, so its text was read from the CMR record: good-quality pixels binned and averaged into 0.25 degree cells, total and tropospheric columns for all conditions and for cloud fraction below 30 percent, HDF-EOS5, the daylit portion of about 14 orbits per file)"
  - id: gesdisc-omto3d
    resource: https://disc.gsfc.nasa.gov/datasets/OMTO3d_004/summary
    title: "GES DISC collection page for OMTO3d 004 (fetched 2026-09-15, text read from its CMR record: the TOMS-like product gridded and averaged from good-quality OMTO3 swath data on the enhanced TOMS version 8 algorithm, about 15 orbits per file, HDF-EOS5)"
  - id: omno2-readme-v5
    resource: https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level3/OMNO2d.004/doc/README.OMNO2.c4v5.pdf
    title: "OMI Nitrogen Dioxide Algorithm Team, December 2024, OMNO2 README Document, Data Product Collection 4 Version 5.0, document version 10.0 (read in full 2026-09-15: the instrument and its coverage, the row anomaly section, the algorithm, the level 2 fields and flags, the limitations, and section 6 on OMNO2d with its screening table, weighting equations, Weight field and limitations)"
  - id: omno2-readme-v4
    resource: https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level3/OMNO2d.003/doc/README.OMNO2.pdf
    title: "OMI Nitrogen Dioxide Algorithm Team, December 2019, OMNO2 README Document, Data Product Version 4.0, document version 9.0 (read 2026-09-15 in its row anomaly, flag, limitations and OMNO2d sections: the version 4.0 flag rule of XTrackQualityFlags 0 or 255 and the same weighting scheme)"
  - id: omno2d-filespec
    resource: https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.2_ProductRequirements_Designs/OMNO2d_FileSpec_V003.pdf
    title: "OMI NO2 Algorithm Team, 2013, OMNO2d File Specification, document version 1.1, product version 2.1 (read 2026-09-15: the 1440 by 720 grid, the five fields, the fill values, the file naming and the field-level Description attribute that records the screening)"
  - id: omto3d-filespec-v3
    resource: https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.2_ProductRequirements_Designs/OMTO3d_FileSpec_V003.pdf
    title: "Leonard, 2013, OMTO3d file specification, PFS version 1.0.7.1, 16 February 2013 (read 2026-09-15: the 1 degree grid, the weighted average by fractional overlap, the exclusion of zoom modes and the five data fields)"
  - id: omto3d-fs-v4
    resource: https://docserver.gesdisc.eosdis.nasa.gov/public/project/OMI/OMTO3d_004.fs
    title: "Leonard, 2024, OMTO3d file specification, PFS version 1.0.12, 12 September 2024 (read 2026-09-15: the same five fields, ColumnAmountO3 in Dobson units, RadiativeCloudFraction, SolarZenithAngle, UVAerosolIndex and ViewingZenithAngle, the 1 degree cell since version 0.9.31 and the aerosol index cutoff of 0.5 since version 1.0.7)"
  - id: omto3d-readme-v3
    resource: https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level3/OMTO3d.003/doc/OMTO3d_OSIPS_README_V003.doc
    title: "Leonard, 2009, README for OMTO3d, 31 May 2009 (a Word document, read 2026-09-15 as extracted text: the TOMS level 3 day defined by local calendar date and built from three consecutive OMTO3G files, and the exclusion criteria A1 to A5, B6 and B7, among them the row anomaly flag and the descending node)"
  - id: omi-dug
    resource: https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.2_ProductRequirements_Designs/README.OMI_DUG.pdf
    title: "OMI Team, 2012, Ozone Monitoring Instrument (OMI) Data User's Guide, OMI-DUG-5.0, 5 January 2012 (read 2026-09-15 in its level 3 section 3.5, the row anomaly notes on OMCLDO2, OMNO2 and OMO3PR, and section 4.15 with Table 12 of the five cross-track anomalies and their dates)"
  - id: omi-atbd-02
    resource: https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithm/ATBD-OMI-02.pdf
    title: "Bhartia (editor), 2002, OMI Algorithm Theoretical Basis Document Volume II, OMI Ozone Products, ATBD-OMI-02 version 2.0, August 2002 (read 2026-09-15 in its preface: the TOMS total ozone algorithm and the DOAS algorithm as the two total ozone products)"
  - id: aura
    resource: https://aura.gsfc.nasa.gov/
    title: "Aura project page named on every OMI collection record (fetched 2026-09-15: the host redirects to science.nasa.gov/mission/aura, whose instrument and data pages carry no row anomaly documentation; the OMI team's row anomaly pages live at KNMI, outside the sources read, so the anomaly is documented here from the GES DISC user's guide and READMEs)"
  - id: lamsal-2021
    resource: https://doi.org/10.5194/amt-14-455-2021
    title: "Lamsal and others, 2021, Ozone Monitoring Instrument (OMI) Aura nitrogen dioxide standard product version 4.0 with improved surface and cloud treatments, Atmospheric Measurement Techniques 14, 455 to 479 (the reference on both OMNO2d records; record and abstract read on the Crossref registry 2026-09-15)"
  - id: levelt-2006
    resource: https://doi.org/10.1109/TGRS.2006.872333
    title: "Levelt and others, 2006, The ozone monitoring instrument, IEEE Transactions on Geoscience and Remote Sensing 44, 1093 to 1101 (the instrument paper; title, authors, journal and year verified on the Crossref registry 2026-09-15, no abstract carried there)"
  - id: dobber-2006
    resource: https://doi.org/10.1109/TGRS.2006.869987
    title: "Dobber and others, 2006, Ozone monitoring instrument calibration, IEEE Transactions on Geoscience and Remote Sensing 44, 1209 to 1238 (on the OMTO3d records; verified on the Crossref registry 2026-09-15)"
  - id: schenkeveld-2017
    resource: https://doi.org/10.5194/amt-10-1957-2017
    title: "Schenkeveld and others, 2017, In-flight performance of the Ozone Monitoring Instrument, Atmospheric Measurement Techniques 10, 1957 to 1986 (named by the NO2 README for the row anomaly's onset; record and abstract read on the Crossref registry 2026-09-15: the launch on 15 July 2004, the 264 to 504 nm range, the slowly unravelling row anomaly and the 3 to 8 percent irradiance degradation outside it)"
  - id: levelt-2018
    resource: https://doi.org/10.5194/acp-18-5699-2018
    title: "Levelt and others, 2018, The Ozone Monitoring Instrument: overview of 14 years in space, Atmospheric Chemistry and Physics 18, 5699 to 5745 (record and abstract read on the Crossref registry 2026-09-15)"
status: stable
stale_after: 2027-03-15
---

# OMI level 3 nitrogen dioxide and total ozone

**Identity.** The Ozone Monitoring Instrument (OMI) is the
Dutch-Finnish ultraviolet and visible imaging spectrograph on NASA's
Aura satellite, launched 15 July 2004, measuring 264 to 504 nm at 60
simultaneous cross-track positions of 13 by 24 km at nadir, so that
14 to 15 orbits of 99 minutes cover the sunlit Earth about
daily, a combination of resolution and daily coverage the
mission's overview paper calls unprecedented.[^schenkeveld-2017][^levelt-2006][^omno2-readme-v5][^levelt-2018] GES DISC
archives its level 2 orbit files and the daily level 3 grids the
teams build from them, all beginning 1 October 2004.[^cmr-omi] The
two level 3 products this concept covers are OMNO2d, the nitrogen
dioxide grid of the NASA OMI NO2 team, and OMTO3d, the TOMS-like
total ozone grid of the US OMI science team; their siblings are
OMTO3e, which keeps the best (shortest path) pixel per 0.25 degree
cell rather than an average, and OMDOAO3e, the 0.25 degree grid of
the KNMI DOAS total ozone, the second of the two total ozone
algorithms the instrument was designed with.[^cmr-omi][^omi-atbd-02][^omi-dug]

**Structure of OMNO2d.** One HDF-EOS5 grid file per day, named
OMI-Aura_L3-OMNO2d_<yyyy>m<mmdd>_v<version>-<production>.he5, on a
0.25 by 0.25 degree grid of 1440 by 720 cells whose first cell has
its edges at 180 W and 90 S, with five fields in molecules per
square centimetre: ColumnAmountNO2, ColumnAmountNO2CloudScreened,
ColumnAmountNO2Trop, ColumnAmountNO2TropCloudScreened and
Weight; a file holds the daylit portion of about 14 orbits, and
the collection record describes it as good-quality pixels binned
and averaged.[^omno2d-filespec][^omno2-readme-v5][^gesdisc-omno2d] Each column field is the
area-weighted average of the level 2 fields of view that overlap the
cell after screening: solar zenith angle below 85 degrees, the
ascending (daylit) orbit with the summary quality bit clear, the
row-anomaly flag at 0 or fill (XTrackQualityFlagsModified in
version 5.0, XTrackQualityFlags in version 4.0), and, for the two
cloud-screened fields, an effective cloud fraction below 30 percent,
a threshold the team calls a compromise between quality and
quantity.[^omno2-readme-v5][^omno2-readme-v4] The weight of a field
of view in a cell is the product of a term linear in the pixel's
area (larger pixels weigh less) and its fractional overlap with the
cell, and Weight is the sum of those weights, provided so that
several files or cells can be combined into a longer or wider
average by weighting each cell's value with it.[^omno2-readme-v5][^omno2d-filespec]
The fill value for an empty cell is about minus 1.27 times ten to
the thirtieth, and each field's Description attribute records the
level 2 inputs and the screening that produced it.[^omno2d-filespec]
Two versions sit side by side in CMR: version 003 carries product
version 4.0 on collection 3 level 1B radiances (released December
2019, its last granule 15 March 2026), and version 004 carries
product version 5.0 on collection 4 radiances (released December
2024, produced from October 2025 and the forward stream
since).[^cmr-omi][^omno2-readme-v5][^omno2-readme-v4] The tropospheric
column comes from a stratosphere-troposphere separation that fills
the stratospheric field from a window of about seven orbits either
side with a model estimate of the tropospheric part subtracted, so
over clean regions the tropospheric column is essentially
model-driven, and the retrieval allows negative columns, which the
team says belong in any average.[^omno2-readme-v5][^lamsal-2021]

**Structure of OMTO3d.** One HDF-EOS5 grid file per day on a 1 by 1
degree grid of 360 by 180 cells (the first centred at 179.5 W, 89.5
S) with five fields: ColumnAmountO3 in Dobson units,
RadiativeCloudFraction, SolarZenithAngle, UVAerosolIndex and
ViewingZenithAngle; there is no count, weight or standard deviation
field; a file holds about 15 orbits.[^omto3d-fs-v4][^omto3d-filespec-v3][^gesdisc-omto3d] Its day is the TOMS level
3 day, the set of pixels whose centres share a local calendar date,
which covers the whole sunlit globe once and puts the near-24-hour
discontinuity at the antimeridian, and which needs three consecutive
daily OMTO3G files to fill.[^omto3d-readme-v3] A cell's ozone is the
weighted average, by fractional area of overlap, of the level 2
OMTO3 pixels that survive the exclusions: outside the 48-hour
window, the wrong local date, a possible solar eclipse, the row
anomaly flag (bit 6 of the level 2 quality flags), the descending
node, any quality value other than good or glint-corrected, and,
where a cell's path-index range exceeds 14, the longer-path half of
its pixels; the aerosol index grid applies stricter angle, path and
glint criteria and drops values below 0.5.[^omto3d-readme-v3][^omto3d-fs-v4]
Versions 003 (PGE 1.0.7) and 004 (PGE 1.0.12, collection 4, produced
from October 2024) were both producing files dated 13 September 2026
when read.[^cmr-omi][^omto3d-fs-v4][^omto3d-filespec-v3]

**Access.** Every version is its own CMR collection with its own
DOI; the level 3 READMEs and file specifications are on the GES
DISC data tree and document server, the OMTO3d and OMTO3e version
004 README text files sitting behind an access prompt when fetched.
The Aura project page the records name redirects to NASA Science and
carries no product documentation; the references the OMTO3d
records carry are the instrument's calibration and level 0 to 1B
processing papers rather than a level 3 description.[^cmr-omi][^aura][^dobber-2006]

## Uncertainty

- **No uncertainty field ships in either level 3 product.** The
  level 2 OMNO2 file carries standard deviation fields per column,
  which the README says are to be used with caution and not for
  quality assessment; OMNO2d carries none of them, only Weight, and
  OMTO3d carries nothing beyond the five fields.[^omno2-readme-v5][^omto3d-fs-v4]
  The NO2 slant column fitting error is about 0.3 to 1 times ten to
  the fifteenth molecules per square centimetre, and the team's
  evaluation against independent instruments is the published
  record.[^omno2-readme-v5][^lamsal-2021]
- **A cell's value is a weighted average that may match no
  measurement.** The 8 to 10 pixels farthest from nadir are much
  larger than a 0.25 degree cell, so a cell under a swath edge
  carries NO2 from some distance away while a cell under nadir
  resolves it; the day-to-day shift of the ground track within the
  orbit's repeat cycle (what the README calls Aura's precession
  relative to the fixed grid) moves a fixed cell between the two,
  and the Weight field is the only record of which.[^omno2-readme-v5]
- **The row anomaly removes rows.** From 25 June 2007 a blockage in
  the viewing port attenuated the radiance in certain cross-track
  positions, spreading in 2008 and 2009 and changing since; the
  affected pixels are flagged and excluded from both grids, and in
  some periods half the fields of view are rejected, so daily
  coverage and the mix of pixel sizes differ before and after (the
  gotcha below).[^omno2-readme-v5][^omi-dug][^schenkeveld-2017]
- **The tropospheric NO2 column over clean regions is the model's.**
  Where there is no separable tropospheric signal in the slant
  column the stratosphere-troposphere separation leaves a
  model-driven tropospheric field.[^omno2-readme-v5]
- **The instrument degrades slowly.** Outside the anomaly the
  irradiances have degraded by 3 to 8 percent and the radiances
  changed by 1 to 2 percent over the mission, with wavelength
  calibration stable to 0.005 to 0.020 nm.[^schenkeveld-2017]

## Known issues

- [omi-row-anomaly](../gotchas/omi-row-anomaly.md): since June 2007
  a growing set of cross-track rows is flagged and dropped; the grid
  looks complete but its sampling changed, and a trend across the
  onset mixes sampling with signal.
- [l3-count-field-bounds-a-cell](../gotchas/l3-count-field-bounds-a-cell.md):
  OMNO2d's Weight bounds what a cell's average rests on, and OMTO3d
  ships no such field.
- [anomaly-names-its-climatology-period](../gotchas/anomaly-names-its-climatology-period.md):
  an OMI anomaly's base period sits before, across or after the row
  anomaly onset and the collection 4 reprocessing, and the number
  changes with it.

[^cmr-omi]: CMR collection, UMM and granule records for the OMI level 2 and level 3 collections, GES_DISC provider, read 2026-09-15
[^gesdisc-omno2d]: GES DISC collection page and CMR record, OMNO2d 004
[^gesdisc-omto3d]: GES DISC collection page and CMR record, OMTO3d 004
[^omno2-readme-v5]: OMI NO2 Algorithm Team, 2024, OMNO2 README, collection 4 version 5.0, document version 10.0
[^omno2-readme-v4]: OMI NO2 Algorithm Team, 2019, OMNO2 README, version 4.0, document version 9.0
[^omno2d-filespec]: OMI NO2 Algorithm Team, 2013, OMNO2d File Specification, version 1.1
[^omto3d-filespec-v3]: Leonard, 2013, OMTO3d file specification, PFS 1.0.7.1
[^omto3d-fs-v4]: Leonard, 2024, OMTO3d file specification, PFS 1.0.12
[^omto3d-readme-v3]: Leonard, 2009, README for OMTO3d
[^omi-dug]: OMI Team, 2012, OMI Data User's Guide, OMI-DUG-5.0
[^omi-atbd-02]: Bhartia (editor), 2002, OMI ATBD Volume II, Ozone Products
[^aura]: Aura project page, redirecting to NASA Science
[^lamsal-2021]: Lamsal and others, 2021, Atmospheric Measurement Techniques, doi:10.5194/amt-14-455-2021
[^levelt-2006]: Levelt and others, 2006, IEEE Transactions on Geoscience and Remote Sensing, doi:10.1109/TGRS.2006.872333
[^dobber-2006]: Dobber and others, 2006, IEEE Transactions on Geoscience and Remote Sensing, doi:10.1109/TGRS.2006.869987
[^schenkeveld-2017]: Schenkeveld and others, 2017, Atmospheric Measurement Techniques, doi:10.5194/amt-10-1957-2017
[^levelt-2018]: Levelt and others, 2018, Atmospheric Chemistry and Physics, doi:10.5194/acp-18-5699-2018
