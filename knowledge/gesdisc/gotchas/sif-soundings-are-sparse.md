---
type: dataset-gotcha
spheres: [biosphere, atmosphere]
title: "OCO-2 SIF soundings are footprints under 1.3 by 2.25 km along a 10 km ground track, imprecise one by one and sampled once per overpass: a gridded mean is a mean of however many samples fell in the cell, it needs its count and standard error, and negative values belong in it"
description: "The Lite file is a list of soundings, eight across a swath 0.8 degrees wide every 0.333 s, not a grid; the mission's own maps are means over 0.2 or 0.5 degree cells of the flag 0 and 1 soundings of a season, and the guide states that the retrievals are accurate but imprecise, that averaging n soundings reduces the noise by the square root of n, and that negative values are statistically valid and their removal biases every average. Nadir, glint, target and, on OCO-3, snapshot area map modes sample differently, target and area modes stacking hundreds to thousands of soundings on one site in one overpass; OCO-3 coverage shifts with the station's altitude and its record has documented gaps. A cell value without its count and standard error, a mean with negatives dropped, or a comparison between cells or dates resting on very different numbers of soundings reads sampling as vegetation."
tags: [oco-2, oco-3, sif, sampling, footprint, gridding, count, standard-error, negative-values, target-mode, snapshot-area-map, oco2_l2_lite_sif, gesdisc, biosphere]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T18:30:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-15T18:36:49Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/173 }
severity: medium
dataset: ../datasets/oco2-sif-lite.md
status: stable
stale_after: 2027-03-15
sources:
  - id: ug-v11
    resource: https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_SIF_v11.2_OCO3_v11_Data_Users_Guide_20250707.pdf
    title: "Kurosu, Frankenberg, Payne and Osterman, 2025, OCO-2 and OCO-3 Solar Induced Chlorophyll Fluorescence Data User's Guide, Lite File Version 11 and 11.2, version 3.0 revision A, 7 July 2025 (read 2026-09-15: Figure 1-1 gridded to 0.2 by 0.2 degrees from flags 0 and 1 with coverage differences from the station's altitude, Figure 1-2 a snapshot area map at single-sounding level, section 2.9 calling the retrievals accurate but imprecise and requiring averaging, section 3.2 on negative values and the square root of n, Table 4-2 with sounding_dim and footprint_dim of 8, Table 4-8 with MeasurementMode and FootprintId, and section 4.11 on the Sequences group)"
  - id: readme-oco2
    resource: https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/README.OCO2.pdf
    title: "Savtchenko, 2021, README Document for Orbiting Carbon Observatory Products, GES DISC, revised 18 February 2021 (read 2026-09-15: eight soundings over the 0.8 degree swath every 0.333 s, footprints under 2.25 km along track and 0.1 to 1.3 km across at nadir, one Lite file per day)"
  - id: oco2-datacenter
    resource: https://ocov2.jpl.nasa.gov/science/oco-2-data-center/
    title: "OCO-2 project, OCO-2 Data Center page (read 2026-09-15: the instrument data are characterised by large gaps in coverage from the narrow 10 km ground track and the inability to see through clouds and thick aerosols, which is why the gridded level 3 CO2 products are assimilation products)"
  - id: opendap-dmr
    resource: https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L2_Lite_SIF.11.2r/2024/oco2_LtSIF_240402_B11217Ar_241023161757s.nc4.dmr
    title: "DAP4 metadata of the OCO-2 Lite SIF granule of 2024-04-02 (read 2026-09-15: sounding_dim of 216914 for the day, the corner arrays on vertex_dim of 4, and the MeasurementMode description naming nadir, glint, target, area map and transition; the on-premises URL is retired after September 2026 and the durable form of the same metadata is the Cloud OPeNDAP .dmr.xml of the granule behind Earthdata Login)"
  - id: cmr-oco-sif
    resource: https://cmr.earthdata.nasa.gov/search/granules.json?collection_concept_id=C2910085832-GES_DISC&sort_key=start_date&page_size=2
    title: "CMR granule records for OCO3_L2_Lite_SIF 11r and OCO2_L2_Lite_SIF 11.2r (read 2026-09-15: 2069 OCO-3 daily files from 2019-08-06, of which 22 fall between November 2023 and July 2024; 818 OCO-2 version 11.2r files from 2024-04-02, of which 17 fall in November 2025)"
  - id: oco3-release
    resource: https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO3_L2_Data_Release_Statement_v11_V1_RevA.pdf
    title: "OCO-3 Level 2 Data Release Statement, version 11 (read 2026-09-15: science data from August 2019, storage on the station from November 2023 to July 2024, and the version 11 reduction of snapshot area map geolocation error from 0.32 km with a spread of 0.70 km to 0 with a spread of 0.34 km)"
  - id: oco3-kdi
    resource: https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO-3_Known_Data_Issues.pdf
    title: "OCO-3 Known Data Issues (read 2026-09-15: the table of gaps of ten orbits or longer from station operations, decontamination cycles and instrument anomalies)"
  - id: gesdisc-alerts
    resource: https://disc.gsfc.nasa.gov/information/alerts?title=Interruption%20of%20OCO-2%20Data%20Delivery%20due%20to%20Instrument%20Anomaly%3A%20No%20Science%20Data
    title: "GES DISC alert of 17 November 2025 (read 2026-09-15 through the site's alerts feed: the OCO-2 instrument locked in stand-by on 5 November 2025 with no science data until the week of 17 November)"
  - id: doughty-2022
    resource: https://doi.org/10.5194/essd-14-1513-2022
    title: "Doughty and others, 2022, Global GOSAT, OCO-2, and OCO-3 solar-induced chlorophyll fluorescence datasets, Earth System Science Data 14, 1513 to 1529 (record and abstract read on the Crossref registry 2026-09-15: OCO-2 and OCO-3 have the highest spatial resolution of spaceborne SIF retrievals, and the target and snapshot area modes provide hundreds to thousands of retrievals at a site in one overpass)"
  - id: l3-count
    resource: ../gotchas/l3-count-field-bounds-a-cell.md
    title: "This bundle's gotcha on level 3 cells as averages of however many retrievals fell in them, the same principle for the AIRS and OMI grids"
  - id: dataset
    resource: ../datasets/oco2-sif-lite.md
    title: "This bundle's OCO-2 and OCO-3 SIF Lite dataset concept, which describes the fields and lists this trap"
---

# Soundings are sparse

**Mechanism.** OCO-2 collects eight soundings across a swath 0.8
degrees wide every 0.333 s, so a day's file is a list of footprints
under 2.25 km along track and 0.1 to 1.3 km across at nadir strung
along a ground track about 10 km wide, and the arrays are indexed by
sounding, 216914 of them in the file of 2 April 2024, with corner
coordinates for each; there is no grid, no cell and no count in the
product.[^readme-oco2][^opendap-dmr][^oco2-datacenter] The retrievals
are, in the guide's words, accurate but imprecise: the one-sigma
uncertainty of a single sounding is substantial, negative values
arise from retrieval noise and are statistically valid, and the
guide states that multiple soundings need to be averaged to reduce
the noise by the square root of their number; its own global maps
are seasonal means on 0.2 or 0.5 degree cells of the flag 0 and 1
soundings.[^ug-v11] The soundings come in modes that sample
differently, recorded per sounding in MeasurementMode: nadir and
glint along the track, target mode over a site, and on OCO-3 the
snapshot area map, so that target and area modes place hundreds to
thousands of soundings on one site in one overpass while the nadir
and glint tracks, about 10 km wide, leave most of the surface
unsampled on any day.[^ug-v11][^opendap-dmr][^doughty-2022] OCO-3 flies on the
International Space Station, so its coverage pattern changes with
the station's altitude, its record has a hole from November 2023 to
July 2024 (22 daily files in those nine months) and gaps of ten
orbits or more from station activities, decontamination cycles and
anomalies; OCO-2 itself lost the first half of November 2025 to an
instrument stand-by.[^ug-v11][^oco3-release][^oco3-kdi][^cmr-oco-sif][^gesdisc-alerts]

**Wrong-result mode.** A grid built from the soundings looks like a
field, and each cell is the mean of whatever fell in it: one nadir
pass, part of a swath, a whole area map, or nothing on most days.
Cells then differ in precision by the square root of their counts,
a cell holding a target sequence is a different measurement from
its neighbours holding a nadir pass, and a difference between two
cells or two dates can be a difference in sampling.[^ug-v11][^doughty-2022]
A mean that drops negative values is biased high, the more so where
the true signal is small, because the noise is symmetric and the
truncation is not; a mean of few soundings in a low-signal cell can
be negative and still correct.[^ug-v11] A seasonal or interannual
series of a cell or a region carries the sampling changes: the OCO-3
coverage shift with station altitude, the storage gap, the OCO-2
stand-by, and the day-to-day variation in which footprints crossed
the cell.[^ug-v11][^oco3-release][^cmr-oco-sif] The same principle
holds for the AIRS and OMI level 3 grids of this bundle, whose count
and weight fields are the only bound on a cell.[^l3-count]

**Correct approach.** A gridded or regional SIF value carries the
number of soundings that entered it and a standard error, the
propagated one-sigma uncertainties divided by the square root of the
count or the spread of the soundings, whichever the analysis states;
negative soundings stay in the mean, with the guide's rule applied
only to extreme values (a sounding is valid when its value plus two
sigma is at least zero, questionable between two and three sigma,
and most likely invalid beyond three sigma); the quality screen is
stated (flags 0 and 1 together in the guide's maps); and the modes
are separated or the mix is stated, target and area map sequences
being read through the Sequences group as observations of a site
rather than as a swath.[^ug-v11] A series states the period and the
gaps it spans, and a comparison between cells or dates rests on
comparable counts or reports them.[^oco3-kdi][^cmr-oco-sif]

**Verification.** The README carries the footprint dimensions and
the eight-by-0.8-degree sampling; the guide's section 3.2 the
negative-value rule and the square root of n, section 2.9 the phrase
accurate but imprecise, and Figure 1-1 the 0.2 degree seasonal maps
with the coverage differences from the station's
altitude.[^readme-oco2][^ug-v11] The check a reader runs: one day's
OCO-2 file gridded to 0.5 degrees leaves most land cells empty and
the filled ones with counts from one to several hundred; a month
gridded the same way shows the count varying by an order of
magnitude between neighbouring cells; and, by construction of the
offset correction rather than as a statement of the guide's, the
mean of Daily_SIF_740nm over a barren region is near zero with
negative and positive soundings in roughly equal numbers.[^ug-v11] The OCO-3 storage gap
is visible as 22 daily files between November 2023 and July 2024 in
the CMR granule listing, and the geolocation improvement for the
area maps is the release statement's.[^cmr-oco-sif][^oco3-release]
The dataset concept lists this trap.[^dataset]

[^ug-v11]: Kurosu and others, 2025, OCO-2 and OCO-3 SIF Data User's Guide, Lite file version 11 and 11.2
[^readme-oco2]: Savtchenko, 2021, README Document for Orbiting Carbon Observatory Products, GES DISC
[^oco2-datacenter]: OCO-2 project, OCO-2 Data Center page, read 2026-09-15
[^opendap-dmr]: DAP4 metadata of the OCO-2 Lite SIF granule of 2024-04-02, read 2026-09-15
[^cmr-oco-sif]: CMR granule records for the OCO-3 and OCO-2 Lite SIF collections, read 2026-09-15
[^oco3-release]: OCO-3 Level 2 Data Release Statement, version 11
[^oco3-kdi]: OCO-3 Known Data Issues
[^gesdisc-alerts]: GES DISC alert on the November 2025 OCO-2 instrument anomaly
[^doughty-2022]: Doughty and others, 2022, Earth System Science Data, doi:10.5194/essd-14-1513-2022
[^l3-count]: This bundle's gotcha on the level 3 count field
[^dataset]: This bundle's OCO-2 and OCO-3 SIF Lite dataset concept
