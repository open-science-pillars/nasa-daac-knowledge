---
type: dataset-gotcha
spheres: [atmosphere]
title: "The OMI row anomaly has removed cross-track rows since June 2007, growing in 2008 and 2009 and changing since: the level 2 flag names the rows, the level 3 grids drop them, and a series across the onset mixes a change in sampling with a change in the atmosphere"
description: "From 25 June 2007 a blockage in OMI's viewing port attenuated the radiance in cross-track positions 53 and 54, from 11 May 2008 in positions 37 to 44, from 24 January 2009 in 27 to 44, with further changes in July and August 2011 and a dynamic extent since; the affected pixels carry a nonzero XTrackQualityFlags (and, in the version 5.0 NO2 product, the team's XTrackQualityFlagsModified), the OMNO2 column fields are fill where the version's flag is set, and OMNO2d and OMTO3d exclude the flagged pixels before gridding. The grids still look complete, but in some periods half the fields of view are rejected, the daily coverage has gaps, a cell's weight and its mix of nadir and swath-edge pixels differ before and after, and the NO2 team says a trend spanning the onset is sampled differently on each side of it."
tags: [omi, aura, row-anomaly, xtrackqualityflags, omno2d, omto3d, omno2, omto3, sampling, trend, gesdisc, atmosphere]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T13:30:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-15T13:59:41Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/161 }
severity: high
dataset: ../datasets/omi-no2-and-ozone.md
eval_case: omi-row-anomaly
status: draft
stale_after: 2027-03-15
sources:
  - id: omi-dug
    resource: https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.2_ProductRequirements_Designs/README.OMI_DUG.pdf
    title: "OMI Team, 2012, Ozone Monitoring Instrument (OMI) Data User's Guide, OMI-DUG-5.0, 5 January 2012 (read 2026-09-15: section 4.15 with Table 12 of the five cross-track anomalies, their onset dates and 0-based positions, the note that the anomaly has been dynamic since the third event, the recommendation not to use affected scenes, the statement that level 3 products are produced after filtering them, and the per-product notes on OMCLDO2, OMNO2 and OMO3PR)"
  - id: omno2-readme-v5
    resource: https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level3/OMNO2d.004/doc/README.OMNO2.c4v5.pdf
    title: "OMI Nitrogen Dioxide Algorithm Team, December 2024, OMNO2 README Document, Collection 4 Version 5.0, document version 10.0 (read 2026-09-15: section 2.4 on the row anomaly and its four effects, the XTrackQualityFlags and XTrackQualityFlagsModified field descriptions, the limitations paragraph on up to 50 percent rejection and on trend analyses across anomaly and non-anomaly periods, the OMNO2d screening table with the flag at 0 or 255, and the known-issues note on residual anomaly patterns)"
  - id: omno2-readme-v4
    resource: https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level3/OMNO2d.003/doc/README.OMNO2.pdf
    title: "OMI Nitrogen Dioxide Algorithm Team, December 2019, OMNO2 README Document, Version 4.0, document version 9.0 (read 2026-09-15: the same row anomaly section, in 4.0 XTrackQualityFlags is the only row anomaly field, with the team's additional flagging folded into it so that it is not identical to the same-named field in other products, it is fill before June 2007, the column fields are fill where it is nonzero, and OMNO2d screens on it at 0 or 255)"
  - id: omto3d-readme-v3
    resource: https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level3/OMTO3d.003/doc/OMTO3d_OSIPS_README_V003.doc
    title: "Leonard, 2009, README for OMTO3d, 31 May 2009 (read 2026-09-15 as extracted text: exclusion criterion A5, level 2 observations with the row anomaly flag, bit 6 of the quality flags, set are excluded from the grid)"
  - id: schenkeveld-2017
    resource: https://doi.org/10.5194/amt-10-1957-2017
    title: "Schenkeveld and others, 2017, In-flight performance of the Ozone Monitoring Instrument, Atmospheric Measurement Techniques 10, 1957 to 1986 (the paper the NO2 README names for the anomaly's onset; record and abstract read on the Crossref registry 2026-09-15: the slowly unravelling row anomaly and the instrument's stability outside it)"
  - id: levelt-2018
    resource: https://doi.org/10.5194/acp-18-5699-2018
    title: "Levelt and others, 2018, The Ozone Monitoring Instrument: overview of 14 years in space, Atmospheric Chemistry and Physics 18, 5699 to 5745 (record and abstract read on the Crossref registry 2026-09-15)"
  - id: cmr-omi
    resource: https://cmr.earthdata.nasa.gov/search/collections.json?short_name=OMNO2d&provider=GES_DISC
    title: "CMR collection and UMM records for OMNO2d and OMTO3d 003 and 004 (read 2026-09-15: the abstracts' statement that only good-quality level 2 pixels are gridded, and the 2004-10-01 start of every record, so that the first two and a half years of each are anomaly-free)"
  - id: aura
    resource: https://aura.gsfc.nasa.gov/
    title: "Aura project page named on the OMI records (fetched 2026-09-15: redirects to science.nasa.gov/mission/aura and carries no row anomaly page; the OMI team's detailed anomaly pages are at KNMI, outside the sources read, and are named here only as the pointer the user's guide gives)"
  - id: dataset
    resource: ../datasets/omi-no2-and-ozone.md
    title: "This bundle's OMI level 3 dataset concept, which describes the screening and lists this trap"
---

# OMI row anomaly

**Mechanism.** OMI's detector images the whole swath at once, so
one cross-track position is one row of the CCD, and from 25 June
2007 an anomaly appeared in the level 1B radiances of certain rows:
positions 53 and 54 (numbered from 0) first, then from 11 May 2008
positions 37 to 44 toward the northern end of the orbit, from 24
January 2009 positions 27 to 44, and from 5 July and 9 August 2011
positions 42 to 45 and 41 to 45; since the third event the affected
rows and the degree of effect vary with time.[^omi-dug][^omno2-readme-v5]
The NO2 team's README names four effects: a blockage that lowers the
radiance, assumed to be a partial obstruction of the viewing port;
sunlight scattered into the port by the obstruction; a wavelength
shift from the inhomogeneous illumination of the slit; and radiance
received from outside the nominal field of view; and it cites the
in-flight performance paper for an onset presumably earlier than
the first flagged date.[^omno2-readme-v5][^schenkeveld-2017] The
level 1B processing flags the rows, and the flag reaches the level
2 products as XTrackQualityFlags, nonzero where the radiance is
affected and fill before June 2007. Which flag drives the fill
differs by NO2 product version. In version 4.0 XTrackQualityFlags is
the only row anomaly field: the team found the level 1B detection
sometimes missed clearly affected rows beside flagged ones, folded
its additional flagging into that field (so that, the README says,
it is not identical to the same-named field in other products), and
set the column amount fields to fill wherever it is
nonzero.[^omno2-readme-v4] Version 5.0 keeps XTrackQualityFlags as
delivered and adds XTrackQualityFlagsModified with the team's own
assessment, and there the modified flag drives the fill: the column
fields are fill wherever it is nonzero, only data where it is zero
or fill are to be used, and the README advises caution where the two
flags differ.[^omno2-readme-v5] The level 3 grids exclude the rows
before averaging: OMNO2d takes only pixels whose flag is 0 or 255
(fill), XTrackQualityFlags in version 4.0 and
XTrackQualityFlagsModified in version 5.0, and OMTO3d excludes any
level 2 observation with the row anomaly flag, bit 6 of the quality
flags, set; the user's guide states the general rule that level 3
products are produced after filtering the affected scenes, and that
all rows not listed and all data before the onset are of optimal
quality.[^omno2-readme-v5][^omto3d-readme-v3][^omi-dug] Every OMI
record begins 1 October 2004, so each carries two years and nine months
of anomaly-free record followed by a record whose swath narrows in
steps.[^cmr-omi]

**Wrong-result mode.** A level 3 file looks the same before and
after 2007: the same grid, the same fields, no flag, and a cell is
either a number or fill. What changed is the sampling. The NO2 team
says the anomaly rejects up to 50 percent of the fields of view in
certain periods, so the daily grids have gaps where the missing
rows would have fallen, a cell's Weight is lower, and, because the
dropped rows are on one side of nadir, the mix of near-nadir and
swath-edge pixels feeding a cell differs from before, with the
swath-edge pixels being the large ones whose value carries NO2 from
some distance away.[^omno2-readme-v5] A trend, a seasonal
climatology or a difference between years computed across the 2007
to 2009 onset is therefore sampled from different rows on each
side, and the README states the consequence for trend analyses:
where some data are heavily flagged or filled, the contribution and
weight of each scan position over the period differ, and a
time-series spanning anomaly-affected and unaffected periods is not
comparable across them unless the unaffected period is sampled with
only the positions that survive in the affected one.[^omno2-readme-v5]
The same holds for OMTO3d, whose path-index criterion already
selects by viewing geometry and whose remaining pixels after the
anomaly are a different geometric mix.[^omto3d-readme-v3] On level
2, a user who ignores XTrackQualityFlags in products where the
columns are not filled (the version 3 OMNO2, the OMTO3 swath, the
cloud and profile products the user's guide flags) brings attenuated
and stray-light-contaminated radiances into the average; the user's
guide withdrew the OMO3PR ozone profile product from use after 25
June 2007 on that ground, and the NO2 team's known-issues note says
some rows with residual anomaly patterns may still pass the
flag.[^omi-dug][^omno2-readme-v5]

**Correct approach.** The flag says which rows: on level 2 the
analysis keeps only rows whose flag is zero or fill, XTrackQualityFlags
in the OMTO3 swath and in the version 4.0 NO2 product,
XTrackQualityFlagsModified in the version 5.0 NO2 product (where
the rows on which the two flags differ are the ones the README says
to treat with caution), and on level 3 it carries the Weight field, which records how much the cell rests on
after the rows were dropped.[^omno2-readme-v5][^omno2-readme-v4] A
series across the onset states the anomaly dates and, following the
README, samples the pre-anomaly years with only the cross-track
positions that are unflagged in the later period, so that both
sides of the series see the same rows; a level 3 series does this
at level 2 or level 2G, because the level 3 grid no longer carries
the row.[^omno2-readme-v5] A per-cell time series in OMNO2d is read
beside its Weight, whose drop after 2008 and 2009 and whose orbital
periodicity are the sampling change made visible.[^omno2-readme-v5]

**Verification.** Table 12 of the user's guide carries the five
onset dates and row ranges, and the NO2 README's section 2.4 and
its limitations paragraph carry the four effects, the 50 percent
figure and the trend statement in the words quoted
above.[^omi-dug][^omno2-readme-v5] The OMTO3d README's exclusion
criterion A5 is the ozone grid's filter, and the OMNO2d screening
table is the NO2 grid's.[^omto3d-readme-v3][^omno2-readme-v5] The
check a reader runs: one OMNO2 level 2 orbit from 2010 shows
XTrackQualityFlags nonzero and ColumnAmountNO2 fill across a
contiguous block of the 60 rows, one orbit from 2006 shows the flag
at fill throughout; and the Weight field of an OMNO2d file from
2010 shows a stripe of low weight along every orbit that a 2006
file does not.[^omno2-readme-v5][^omno2-readme-v4] The onset and the
instrument's behaviour outside the anomaly are the in-flight
performance paper's, verified on the registry.[^schenkeveld-2017][^levelt-2018]
The Aura project page the records name does not document the
anomaly.[^aura] The dataset concept lists this trap.[^dataset]

[^omi-dug]: OMI Team, 2012, OMI Data User's Guide, OMI-DUG-5.0
[^omno2-readme-v5]: OMI NO2 Algorithm Team, 2024, OMNO2 README, collection 4 version 5.0
[^omno2-readme-v4]: OMI NO2 Algorithm Team, 2019, OMNO2 README, version 4.0
[^omto3d-readme-v3]: Leonard, 2009, README for OMTO3d
[^schenkeveld-2017]: Schenkeveld and others, 2017, Atmospheric Measurement Techniques, doi:10.5194/amt-10-1957-2017
[^levelt-2018]: Levelt and others, 2018, Atmospheric Chemistry and Physics, doi:10.5194/acp-18-5699-2018
[^cmr-omi]: CMR collection and UMM records for OMNO2d and OMTO3d, read 2026-09-15
[^aura]: Aura project page, redirecting to NASA Science
[^dataset]: This bundle's OMI level 3 dataset concept
