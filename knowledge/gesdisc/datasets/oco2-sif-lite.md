---
type: dataset
spheres: [biosphere, atmosphere]
title: "OCO-2 and OCO-3 solar-induced fluorescence Lite files: one netCDF-4 file per day of offset-corrected 757 and 771 nm retrievals per sounding, with a derived 740 nm value, a geometric daily correction factor, a three-level quality flag and a one-sigma uncertainty beside every value"
description: "The OCO-2 SIF Lite product (OCO2_L2_Lite_SIF, version 11r to 31 March 2024 and 11.2r from 2 April 2024, DOIs 10.5067/OTRE7KQS8AU8 and 10.5067/8XXUQU7HBGBL) and its OCO-3 sibling (OCO3_L2_Lite_SIF 11r, DOI 10.5067/HC776J71KV41, from 6 August 2019) hold every converged IMAP-DOAS fluorescence sounding of a day that passed the level 1B quality flag: solar-induced chlorophyll fluorescence retrieved in two windows near 757 and 771 nm in the oxygen A-band region, corrected each day by a background over barren surfaces, combined by fixed factors into a 740 nm value, and scaled by a clear-sky geometric factor into a daily average. The values are radiances in W per square metre per steradian per micrometre at footprints of up to about 1.3 by 2.25 km, sparse in space and single-overpass in time; they are not photosynthesis, not gridded and not error-free, and a one-sigma uncertainty, a quality flag, the observation mode and the barren-surface offset statistics ship with every file."
tags: [oco-2, oco-3, sif, solar-induced-fluorescence, chlorophyll-fluorescence, oco2_l2_lite_sif, oco3_l2_lite_sif, imap-doas, gpp, gesdisc, biosphere, atmosphere]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T18:10:00Z }
resource: https://disc.gsfc.nasa.gov/datasets/OCO2_L2_Lite_SIF_11.2r/summary
version: "OCO-2 Lite SIF version 11r (C2248652649-GES_DISC, DOI 10.5067/OTRE7KQS8AU8, 3274 daily files from 2014-09-06 to 2024-03-30, build B11012Ar) and version 11.2r (C2912084771-GES_DISC, DOI 10.5067/8XXUQU7HBGBL, ends-at-present, 818 daily files from 2024-04-02 to 2026-07-27, builds B11217Ar and B11218Ar); OCO-3 Lite SIF version 11r (C2910085832-GES_DISC, DOI 10.5067/HC776J71KV41, ends-at-present, 2069 daily files from 2019-08-06 to 2026-06-28); concept ids, DOIs, extents and counts CMR-verified 2026-09-15, the file structure read from the July 2025 user guide (version 3.0 revision A) and from the DAP4 metadata of the 2024-04-02 OCO-2 granule the same day"
sources:
  - id: cmr-oco-sif
    resource: https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=OCO2_L2_Lite_SIF&provider=GES_DISC
    title: "CMR collection, UMM and granule records for OCO2_L2_Lite_SIF 11r and 11.2r and OCO3_L2_Lite_SIF 11r at provider GES_DISC (read 2026-09-15: concept ids, DOIs, entry titles, temporal extents, the related URLs to the user guide, README, ATBD, known-issues list and OPeNDAP, the first and newest granule of each collection with their sizes of 15 to 23 MB, the granule counts, and the two services associated with each collection, Cloud OPeNDAP and the level 2 Harmony subsetter)"
  - id: ug-v11
    resource: https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_SIF_v11.2_OCO3_v11_Data_Users_Guide_20250707.pdf
    title: "Kurosu, Frankenberg, Payne and Osterman, 2025, Orbiting Carbon Observatory-2 and -3 Solar Induced Chlorophyll Fluorescence Data User's Guide, Lite File Version 11 and 11.2, version 3.0 revision A, 7 July 2025, JPL (the user's guide the CMR records link; read in full 2026-09-15: the overview, the version 11 changes including the April 2024 meteorology switch and the retrieval window change, the version 10 quality flag and offset correction, the 740 nm conversion, the daily correction factor, the negative-value guidance, and the file structure tables for every group)"
  - id: ug-b10
    resource: https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO23_SIF_B10_Product_Description.pdf
    title: "OCO-2 and OCO-3 Solar Induced Chlorophyll Fluorescence Data User's Guide for the build 10 Lite files (version 2.1, February 2021; the general documentation link on the OCO-3 record, read 2026-09-15: the same quality flag, offset correction and daily correction text as the 2025 guide, which supersedes it)"
  - id: readme-oco2
    resource: https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/README.OCO2.pdf
    title: "Savtchenko, 2021, README Document for Orbiting Carbon Observatory Products, GES DISC, revised 18 February 2021 (read 2026-09-15: the eight soundings over the 0.8 degree swath every 0.333 s with footprints under 2.25 km along track and 0.1 to 1.3 km across at nadir, the retrospective r versions against the forward stream, the one-file-per-day Lite granularity and the Lite file naming)"
  - id: release-112
    resource: https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L2_Lite_SIF.11.2r/doc/OCO2_L2_Data_Release_Statement_v11.2_V2_RevA.pdf
    title: "OCO-2 Data Release Statement, Version 11.2 Lite File Data Release, 1 October 2024, version 2.0 revision A (in the collection's document directory on the GES DISC OPeNDAP server, read 2026-09-15: the version 11 changes including the SIF throughput improvement and the target-mode SIF fix, and the April 2024 boundary between the v11.1 and v11.2 processing)"
  - id: oco3-release
    resource: https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO3_L2_Data_Release_Statement_v11_V1_RevA.pdf
    title: "OCO-3 Level 2 Data Release Statement, version 11, version 1 revision A (the product quality assessment link on the OCO-3 record, read 2026-09-15: OCO-3 on the International Space Station since May 2019, science data from August 2019, storage from November 2023 to July 2024, the version 11 pointing and geolocation improvements for the snapshot area maps)"
  - id: oco3-kdi
    resource: https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO-3_Known_Data_Issues.pdf
    title: "OCO-3 Known Data Issues (read 2026-09-15: the table of data gaps of ten orbits or longer caused by station activities, decontamination cycles and anomalies, 2021 to 2023)"
  - id: opendap-dmr
    resource: https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L2_Lite_SIF.11.2r/2024/oco2_LtSIF_240402_B11217Ar_241023161757s.nc4.dmr
    title: "DAP4 metadata of the first version 11.2r OCO-2 granule on the GES DISC on-premises OPeNDAP server (read 2026-09-15 without a credential: 216914 soundings in the day, the dimensions, the flattened group names, the units, descriptions and formulas in the variable attributes, and the global attributes date_time_coverage, product_version B11217Ar, InputBuildId B11.0.08 and B11.2.05, sensor and DOI)"
  - id: oco2-datacenter
    resource: https://ocov2.jpl.nasa.gov/science/oco-2-data-center/
    title: "OCO-2 project, OCO-2 Data Center page (read 2026-09-15: the Lite products are posted at GES DISC, the retrospective Lite SIF v11r and v11.2r are the reference records, the forward-stream OCO2_L2_Fwd_SIF is removed as retrospective data arrive, the acknowledgement text and the 10 km ground track; the project site carries no separate SIF product page, its product-info and science/sif paths answer 404, and its publications page lists SIF papers without product documentation)"
  - id: gesdisc-alerts
    resource: https://disc.gsfc.nasa.gov/information/alerts?title=OCO-3%20v11r%20February-June%202025%20Data%20Reprocessing
    title: "GES DISC alerts naming the SIF Lite collections (read 2026-09-15 through the site's alerts feed: the OCO-3 v11r February to June 2025 reprocessing of August 2025, the November 2025 OCO-2 instrument stand-by with no science data, and the 2020 advisory on the Aqua anomaly's effect on the aerosol priors, to which SIF is not highly sensitive)"
  - id: doughty-2022
    resource: https://doi.org/10.5194/essd-14-1513-2022
    title: "Doughty, Kurosu, Parazoo, Köhler, Wang, Sun and Frankenberg, 2022, Global GOSAT, OCO-2, and OCO-3 solar-induced chlorophyll fluorescence datasets, Earth System Science Data 14, 1513 to 1529 (the product paper the user guide names; record and abstract read on the Crossref registry 2026-09-15: daily netCDF Lite files, retrieval noise, sun-sensor geometry, the indirect relationship between SIF and photosynthesis, the target and snapshot area modes giving hundreds to thousands of retrievals at a site in one overpass)"
  - id: sun-2018
    resource: https://doi.org/10.1016/j.rse.2018.02.016
    title: "Sun, Frankenberg, Jung, Joiner, Guanter, Köhler and Magney, 2018, Overview of Solar-Induced chlorophyll Fluorescence (SIF) from the Orbiting Carbon Observatory-2: Retrieval, cross-mission comparison, and global monitoring for GPP, Remote Sensing of Environment 209, 808 to 823 (record read on the Crossref registry 2026-09-15, which carries no abstract for this article; the publisher page sits behind a bot check; the user guide cites it for the wavelength dependence of absolute fluorescence)"
  - id: sun-2017
    resource: https://doi.org/10.1126/science.aam5747
    title: "Sun and others, 2017, OCO-2 advances photosynthesis observation from space via solar-induced chlorophyll fluorescence, Science 358, 6360 (record and structured abstract read on the Crossref registry 2026-09-15: the airborne validation with slope 1.02 and R squared 0.71, the flux-site SIF-GPP relationships more consistent across biomes than previously suggested, and the statement that a universal relationship cannot be dismissed and needs process studies)"
  - id: frankenberg-2011b
    resource: https://doi.org/10.1029/2011GL048738
    title: "Frankenberg and others, 2011, New global observations of the terrestrial carbon cycle from GOSAT: Patterns of plant fluorescence with gross primary productivity, Geophysical Research Letters 38, L17706 (the paper the user guide cites for the retrieval and the reference-target bias correction; record read on the Crossref registry 2026-09-15, no abstract carried)"
  - id: frankenberg-2012
    resource: https://doi.org/10.5194/amt-5-2081-2012
    title: "Frankenberg, O'Dell, Guanter and McDuffie, 2012, Remote sensing of near-infrared chlorophyll fluorescence from space in scattering atmospheres, Atmospheric Measurement Techniques 5, 2081 to 2094 (record and abstract read on the Crossref registry 2026-09-15: about 80 percent of the surface fluorescence reaches the top of the atmosphere even under cloud optical thickness 2 to 5, and a Fraunhofer-line retrieval is robust to scattering)"
  - id: frankenberg-2014
    resource: https://doi.org/10.1016/j.rse.2014.02.007
    title: "Frankenberg and others, 2014, Prospects for chlorophyll fluorescence remote sensing from the Orbiting Carbon Observatory-2, Remote Sensing of Environment 147, 1 to 12 (record read on the Crossref registry 2026-09-15, no abstract carried)"
  - id: parazoo-2019
    resource: https://doi.org/10.1029/2019JG005289
    title: "Parazoo and others, 2019, Towards a Harmonized Long-Term Spaceborne Record of Far-Red Solar-Induced Fluorescence, Journal of Geophysical Research Biogeosciences 124, 2518 to 2539 (record and abstract read on the Crossref registry 2026-09-15: the corrections for time of day, wavelength, sun-sensor geometry, cloud effects and footprint area between sensors, and retrieval window choice as the main driver of magnitude differences)"
  - id: magney-2019
    resource: https://doi.org/10.1029/2019JG005029
    title: "Magney and others, 2019, Disentangling Changes in the Spectral Shape of Chlorophyll Fluorescence: Implications for Remote Sensing of Photosynthesis, Journal of Geophysical Research Biogeosciences 124, 1491 to 1507 (the paper the user guide cites for the wavelength conversion; record and abstract read on the Crossref registry 2026-09-15: one spectral shape explains 84 percent of the variance across species and the shape is stable beyond 740 nm)"
status: draft
stale_after: 2027-03-15
---

# OCO-2 and OCO-3 SIF Lite files

**Identity.** The Orbiting Carbon Observatory-2, launched 2 July
2014 into a near-polar orbit and joining the A-Train that August, carries three high-resolution spectrometers that
measure reflected sunlight in the oxygen A-band near 0.76 micrometres
and in two carbon dioxide bands near 1.61 and 2.06 micrometres; the
A-band spectra, taken to retrieve column carbon dioxide, also carry
the in-filling of solar Fraunhofer lines by chlorophyll fluorescence,
and the mission retrieves that fluorescence with the IMAP-DOAS
preprocessor as a by-product of its primary target, a prospect
assessed before launch.[^readme-oco2][^sun-2017][^frankenberg-2011b][^frankenberg-2014] The SIF Lite
files (LtSIF) are the product a user meets: a post-processing of the
IMAP-DOAS level 2 files that keeps the converged soundings passing
the level 1B quality flag, applies a daily background correction
derived over non-fluorescing surfaces, assigns a quality flag, and
merges cloud-screening fields from the A-band preprocessor and
meteorology interpolated to each footprint, in one netCDF-4 file per
day that had at least one retrieved sounding.[^ug-v11] The OCO-2
record is two CMR collections split at the April 2024 switch of the
JPL processing from GEOS-5 FP-IT to GEOS-IT meteorology: version 11r
(C2248652649-GES_DISC, DOI 10.5067/OTRE7KQS8AU8) covers 6 September
2014 to 30 March 2024 in 3274 daily files, and version 11.2r
(C2912084771-GES_DISC, DOI 10.5067/8XXUQU7HBGBL) runs from 2 April
2024 with the ends-at-present flag, 818 daily files to 27 July 2026
on the day of reading; the OCO-2 project names these retrospective
Lite files its reference record and removes the forward-stream
OCO2_L2_Fwd_SIF files as the retrospective ones
arrive.[^cmr-oco-sif][^ug-v11][^oco2-datacenter][^readme-oco2]
OCO-3, an instrument of the same design operating on the International
Space Station since May 2019, has its own Lite SIF collection
OCO3_L2_Lite_SIF version 11r (C2910085832-GES_DISC, DOI
10.5067/HC776J71KV41) from 6 August 2019, 2069 daily files to 28
June 2026, with the same file structure as OCO-2's, the same offset
adjustment and quality logic, and the observing sensor named in the
global attributes; its record has a hole from November 2023 to July
2024, when the instrument was in storage on the station, and gaps of
ten orbits or more from station activities and decontamination
cycles are tabulated in its known-issues
list.[^cmr-oco-sif][^ug-v11][^oco3-release][^oco3-kdi] The user
guide is JPL-authored and hosted on the GES DISC document server;
the OCO-2 project site has no product page for SIF of its own, and
its data center page points to GES DISC.[^ug-v11][^oco2-datacenter]

**Structure.** Each sounding is one of eight cross-track footprints
across a swath 0.8 degrees wide, taken every 0.333 s, with
along-track dimensions under 2.25 km and cross-track dimensions of
0.1 to 1.3 km at nadir; the arrays are indexed by sounding_dim
(216914 soundings in the OCO-2 file of 2 April 2024), with
footprint_dim of 8 and vertex_dim of 4 for the footprint
corners.[^readme-oco2][^opendap-dmr][^ug-v11] The root group carries
what most users need: Latitude, Longitude and their Corners,
Delta_Time in seconds since 1990-01-01, the sun and view angles SZA,
SAz, VZA and VAz, the derived SIF_740nm and its SIF_Uncertainty_740nm,
the length-of-day corrected Daily_SIF_757nm, Daily_SIF_771nm and
Daily_SIF_740nm, Quality_Flag (0 best, 1 good, 2 failed, minus 1 not
investigated) and, in OCO-3 files and OCO-2 files from 2 April 2024,
SimplyGoodOrBadQualityFlag (0 for best or good, 1 for
bad).[^ug-v11][^opendap-dmr] The retrieved quantities live in the
Science group: SIF_757nm and SIF_771nm, offset-adjusted, with their
one-sigma uncertainties, the unadjusted values and the relative
fluorescence (the fraction of the continuum radiance, which is the
retrieval's own state variable) in both forms, the continuum
radiances at 757 and 771 nm (multiplied by two for unpolarised
light), daily_correction_factor, sounding_land_fraction and the level
1B flag, renamed sounding_l1b_quality_flag from April 2024 and
sounding_qual_flag before.[^ug-v11] The Cloud group holds the A-band
preprocessor's o2_ratio and co2_ratio used in the quality flag and
its cloud flag, pressure difference and albedo, which are not; the
Meteo group holds GEOS-5 forecast surface pressure, humidity, skin
and 2 m temperature, vapour pressure deficit and wind speed at each
sounding, provided as is and not validated; the Offset group holds
the per-footprint mean, median and standard deviation of adjusted
and unadjusted SIF on 227 signal-level bins from 3 to 229 W per
square metre per steradian per micrometre, the diagnostics of the
day's background correction; the Metadata group holds the
SoundingId, FootprintId 1 to 8, OrbitId and MeasurementMode (0
nadir, 1 glint, 2 target, 3 area map on OCO-3 only, 4 transition);
the Sequences group, new in version 11, names the target and
snapshot-area-map sequences and each sounding's index in them; and
the Diagnostics group, in OCO-3 files and OCO-2 files from April
2024, carries the thresholds and per-test bits behind the quality
flag.[^ug-v11][^opendap-dmr] The two retrieval windows near 757 and
771 nm were moved in version 11, the 757 nm window away from the
detector edge and both made consistent between the two instruments,
so version 11 values differ slightly from version 10 and agree
better between OCO-2 and OCO-3; SIF at 771 nm is typically about 1.5
times smaller than at 757 nm, and the 740 nm value is not retrieved
but formed as 0.75 times the sum of SIF_757nm and 1.5 times
SIF_771nm, with its uncertainty propagated by the same
factors.[^ug-v11][^opendap-dmr] The quality flag is a relaxed screen
compared with the XCO2 Lite files, because clouds and aerosols do
not strongly attenuate fluorescence (about 80 percent of the surface
signal reaches the top of the atmosphere even under cloud optical
thickness 2 to 5): best requires a 757 nm continuum radiance between
28 and 195, fit chi-squared at both windows at most 2.0, an O2 ratio
between 0.85 and 1.5, a CO2 ratio between 0.5 and 4.0, solar zenith
angle at most 70 degrees and a land fraction of 100 percent; good
loosens the chi-squared bound to 3.0, the solar zenith angle to 75
degrees and the land fraction to 80 percent; the guide's own figures
use flags 0 and 1 together, and the build 10 guide describes the same
flag logic and offset method for the version 10 files.[^ug-v11][^frankenberg-2012][^ug-b10] The daily
files are named oco2_LtSIF_yymmdd_Bbuild_productiontime.nc4 and
oco3_LtSIF likewise, with the build in the global attributes
(product_version B11217Ar and input builds B11.0.08 and B11.2.05 on
the 2 April 2024 file).[^readme-oco2][^opendap-dmr]

**Access.** Both instruments' collections are searchable in CMR by
short name under the GES_DISC provider and served from the Earthdata
Cloud archive host, through Cloud OPeNDAP (the DAP4 endpoint each
granule record lists) and through the Harmony level 2 subsetter
associated with the collections; the GES DISC on-premises data and
OPeNDAP servers that also list them are being retired by 30
September 2026, and the collection version and its DOI is what a
citation names, with the retrieval date, because the OCO-3 February
to June 2025 files were withdrawn and reprocessed in August 2025 and
the forward-stream OCO-2 files are replaced by retrospective
ones.[^cmr-oco-sif][^gesdisc-alerts][^oco2-datacenter] The
subsetter and OPeNDAP connector concept of this bundle
([gesdisc-subsetter-opendap](../connectors/gesdisc-subsetter-opendap.md))
carries the request shape, the token and what leaves the machine;
the OCO-2 project asks that publications acknowledge the OCO-2
project at JPL and the archive at GES DISC and cite the mission
papers it lists.[^oco2-datacenter] The product paper for all three
Lite SIF data sets (GOSAT, OCO-2, OCO-3) is Doughty and others
2022.[^doughty-2022]

## Uncertainty

- **A one-sigma retrieval uncertainty ships with every value.**
  SIF_Uncertainty_757nm and SIF_Uncertainty_771nm are the statistical
  one-sigma uncertainties of the fit, and SIF_Uncertainty_740nm is
  their combination by the same fixed factors as the 740 nm value;
  the guide states that the retrievals are accurate but imprecise,
  that the uncertainties can be substantial, that negative values
  are therefore statistically valid and discarding them biases any
  average, and that averaging n soundings reduces the noise by the
  square root of n. It gives a rule for extreme values: a sounding
  whose value plus two sigma is at least zero is valid, one that
  fails that but passes at three sigma is questionable, and one
  whose value plus three sigma is below zero is most likely invalid;
  the Lite processing does not apply this rule when assigning the
  quality flag.[^ug-v11]
- **The background offset is a daily estimate, not a constant.** The
  retrieval's biases from the per-footprint instrument line shape
  and detector linearity are removed by subtracting the mean SIF over
  barren surfaces (a 0.2 degree table built from the 2018 MODIS IGBP
  barren and snow classes and near-zero VPM gross primary production)
  in a three-day window centred on the day, per footprint; the
  Offset group reports the means, medians and standard deviations
  behind it, and the unadjusted values are kept in the Science group,
  so the correction is inspectable and its day-to-day variation is
  part of the record's noise.[^ug-v11]
- **The daily correction is geometric and clear-sky.** The
  daily_correction_factor scales the instantaneous value by the
  ratio of the day's integrated cosine of the solar zenith angle to
  its value at the overpass, computed in ten-minute steps, ignoring
  clouds, Rayleigh scattering and gas absorption; its error is not in
  the uncertainty fields, and the Daily_SIF values inherit
  it.[^ug-v11]
- **Two processing epochs sit inside the OCO-2 record.** From 1
  April 2024 the meteorology switched from GEOS-5 FP-IT to GEOS-IT
  without a reprocessing of the earlier OCO-2 record; the guide bounds
  the resulting change in retrieved SIF at fractions of a percent and
  states that data before and after can be used together, while the
  file contents differ (the Diagnostics group, the simplified flag and
  the renamed level 1B flag are present only after); the OCO-3
  record was fully reprocessed with GEOS-IT.[^ug-v11][^release-112]
- **The 740 nm value and any cross-sensor comparison rest on an
  assumed spectral shape.** The conversion factors and the choice of
  a 740 nm reference follow leaf-level evidence that one far-red
  spectral shape explains most of the variance across species, and
  cross-mission work finds that retrieval window choice, time of day,
  sun-sensor geometry, cloud effects and footprint area each have to
  be corrected before sensors agree; the mission's overview of the
  retrieval and the cross-mission comparison is the paper the guide
  cites for the wavelength dependence.[^ug-v11][^magney-2019][^parazoo-2019][^sun-2018]
- **Sampling is the largest structured limitation.** Each day's file
  is a set of footprints along a roughly 10 km ground track (and, on
  OCO-3, along the station's orbit, whose coverage pattern changes
  with its altitude), so any grid built from
  it is a mean of however many samples fell in the cell; the
  soundings-are-sparse gotcha below carries the consequences.[^oco2-datacenter][^readme-oco2][^doughty-2022]

## Known issues

- [sif-is-not-photosynthesis](../gotchas/sif-is-not-photosynthesis.md):
  the value is a radiance emitted by chlorophyll; its relation to
  gross primary production is empirical, scale- and biome-dependent
  and not carried in the file.
- [sif-two-bands-and-offsets](../gotchas/sif-two-bands-and-offsets.md):
  757 and 771 nm are separate retrievals with a fixed ratio to the
  derived 740 nm value, each offset-corrected by a daily barren-surface
  background, and the windows changed between versions 10 and 11.
- [sif-soundings-are-sparse](../gotchas/sif-soundings-are-sparse.md):
  the product is point soundings, a gridded mean is a mean of samples
  with a count, negative values belong in it, and the observation
  modes sample differently.
- [sif-daily-correction](../gotchas/sif-daily-correction.md): the
  Daily_SIF fields are the instantaneous values times a clear-sky
  geometric factor, not an observed daily mean.

[^cmr-oco-sif]: CMR collection, UMM and granule records for OCO2_L2_Lite_SIF 11r and 11.2r and OCO3_L2_Lite_SIF 11r, read 2026-09-15
[^ug-v11]: Kurosu and others, 2025, OCO-2 and OCO-3 SIF Data User's Guide, Lite file version 11 and 11.2, version 3.0 revision A
[^ug-b10]: OCO-2 and OCO-3 SIF Data User's Guide for the build 10 Lite files, 2021
[^readme-oco2]: Savtchenko, 2021, README Document for Orbiting Carbon Observatory Products, GES DISC
[^release-112]: OCO-2 Data Release Statement, version 11.2 Lite file release, October 2024
[^oco3-release]: OCO-3 Level 2 Data Release Statement, version 11
[^oco3-kdi]: OCO-3 Known Data Issues
[^opendap-dmr]: DAP4 metadata of the OCO-2 Lite SIF granule of 2024-04-02, GES DISC on-premises OPeNDAP, read 2026-09-15
[^oco2-datacenter]: OCO-2 project, OCO-2 Data Center page, read 2026-09-15
[^gesdisc-alerts]: GES DISC alerts naming the SIF Lite collections, read 2026-09-15
[^doughty-2022]: Doughty and others, 2022, Earth System Science Data, doi:10.5194/essd-14-1513-2022
[^sun-2018]: Sun and others, 2018, Remote Sensing of Environment, doi:10.1016/j.rse.2018.02.016
[^sun-2017]: Sun and others, 2017, Science, doi:10.1126/science.aam5747
[^frankenberg-2011b]: Frankenberg and others, 2011, Geophysical Research Letters, doi:10.1029/2011GL048738
[^frankenberg-2012]: Frankenberg and others, 2012, Atmospheric Measurement Techniques, doi:10.5194/amt-5-2081-2012
[^frankenberg-2014]: Frankenberg and others, 2014, Remote Sensing of Environment, doi:10.1016/j.rse.2014.02.007
[^parazoo-2019]: Parazoo and others, 2019, Journal of Geophysical Research Biogeosciences, doi:10.1029/2019JG005289
[^magney-2019]: Magney and others, 2019, Journal of Geophysical Research Biogeosciences, doi:10.1029/2019JG005029
