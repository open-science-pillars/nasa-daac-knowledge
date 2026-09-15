---
type: dataset
spheres: [hydrosphere, atmosphere]
title: "ASCAT scatterometer ocean surface winds at PO.DAAC: the OSI SAF operational Level 2 streams, the MetOp-A climate data records and the JPL MEaSUREs inter-calibrated ESDR"
description: "PO.DAAC distributes two families of ASCAT wind products: the EUMETSAT OSI SAF Level 2 wind vectors retrieved at KNMI (near-real-time 25 km and coastal 12.5 km streams for MetOp-A, -B and -C, of which B and C are ongoing, plus two reprocessed MetOp-A climate data records) and the JPL MEaSUREs Earth System Data Record that re-retrieves MetOp-A and -B with a QuikSCAT-harmonized model function and adds true 10 m winds, wind stress, per-cell uncertainties and a quality indicator. Every wind is a 10 m equivalent-neutral wind relative to the moving surface unless a field says otherwise, and every file carries flags for rain, sea ice and coast that decide which cells are winds."
tags: [ascat, scatterometer, ocean-winds, metop, osi-saf, knmi, measures, esdr, wind-stress, level2, level3, podaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T13:30:00Z }
resource: https://podaac.jpl.nasa.gov/dataset/ASCATB-L2-25km
version: "CMR-verified 2026-09-15 with granule ranges from first-and-last granule searches the same day. OSI SAF operational streams (version Operational/Near-Real-Time, no DOI by the producer's DOI policy): ASCATB-L2-25km (C2075141559-POCLOUD, 2012-10-29 through 2026-09-15 and ongoing, 71808 granules), ASCATB-L2-Coastal (C2075141605-POCLOUD, 2012-10-29 through 2026-09-15, 71802), ASCATC-L2-25km (C2075141638-POCLOUD, 2019-10-22 through 2026-09-15, 35626), ASCATC-L2-Coastal (C2075141684-POCLOUD, 2019-10-22 through 2026-09-15, 35622), ASCATA-L2-25km (C2075141524-POCLOUD, 2007-03-28 through 2021-11-15, complete, 75417) and ASCATA-L2-Coastal (C1996881752-POCLOUD, 2010-08-18 through 2021-11-15, complete, 57983). MetOp-A climate data records version 1.0: ASCATA_L2_25KM_CDR (C2491772100-POCLOUD, DOI 10.15770/EUM_SAF_OSI_0006) and ASCATA_L2_COASTAL_CDR (C2036877686-POCLOUD, DOI 10.15770/EUM_SAF_OSI_0007), both 2007-01-01 through 2014-04-01, 37307 granules each. JPL MEaSUREs ESDR: Level 2 wind and stress version 1.1 for MetOp-A (ASCATA_ESDR_L2_WIND_STRESS_V1.1, C2730520815-POCLOUD, DOI 10.5067/ESASA-L2W11, 2007-01-01 through 2014-04-01, 35303 granules) and MetOp-B (ASCATB_ESDR_L2_WIND_STRESS_V1.1, C2706513160-POCLOUD, DOI 10.5067/ESASB-L2W11, 2013-08-01 through 2022-05-30, 44568), Level 3 daily gridded version 1.0 for MetOp-A (ASCATA_ESDR_L3_WIND_STRESS_V1.0, C3402062729-POCLOUD, DOI 10.5067/ESASA-L3W10, 2481 granules) and MetOp-B (ASCATB_ESDR_L3_WIND_STRESS_V1.0, C3403169610-POCLOUD, DOI 10.5067/ESASB-L3W10, 3080), with matching version 1.1 ancillary collections (ASCATA_ESDR_ANCILLARY_L2_V1.1, C2705728324-POCLOUD; ASCATB_ESDR_ANCILLARY_L2_V1.1, C2706510710-POCLOUD) and version 1.0 spatial-derivative collections (ASCATA_ESDR_L2_WSDERIV_V1.0, C3401738510-POCLOUD; ASCATB_ESDR_L2_WSDERIV_V1.0, C3401765750-POCLOUD); the MEaSUREs user guide is dated 1 December 2022 and the Level 2 README 12 June 2024"
status: draft
stale_after: 2027-03-15
sources:
  - id: cmr-search
    resource: https://cmr.earthdata.nasa.gov/search/collections.json?provider=POCLOUD&keyword=ASCAT&page_size=100
    title: "CMR collection search for ASCAT at the POCLOUD provider, run 2026-09-15: the sixteen ASCAT collections named above (plus CCMP, QuikSCAT, SCATSAT-1 and MWOW collections the search also matched), with short names, versions and temporal extents"
  - id: cmr-b25
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2075141559-POCLOUD.umm_json
    title: "CMR collection record for ASCATB-L2-25km: abstract (25 km sampling, 50 km effective resolution, CMOD.n model function, Hamming filter, one full orbit per netCDF3 file built from 3-minute granules, about 2 hours latency, EUMETSAT copyright), the DOI missing-reason (data producer DOI ownership), the KNMI product manual and PO.DAAC archive links, additional attributes and the Verspeek 2010 reference (read 2026-09-15)"
  - id: cmr-bcoastal
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2075141605-POCLOUD.umm_json
    title: "CMR collection record for ASCATB-L2-Coastal: abstract (12.5 km sampling, 25 km effective resolution, box filter over a 15 km radius on full-resolution sigma-0 with non-sea retrievals discarded first, winds to about 15 km from the coast against a static land mask of about 35 km in the standard product, CMOD5.n) and the Verhoef 2012 reference (read 2026-09-15)"
  - id: cmr-c25
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2075141638-POCLOUD.umm_json
    title: "CMR collection record for ASCATC-L2-25km: abstract (CMOD7.n) and the Stoffelen 2017 reference; the MetOp-C coastal record C2075141684-POCLOUD was read the same way (read 2026-09-15)"
  - id: cmr-a25
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2075141524-POCLOUD.umm_json
    title: "CMR collection record for ASCATA-L2-25km: abstract (CMOD7.n at the record's last revision), the closed temporal extent ending 2021-11-15 and the COMPLETE progress; the MetOp-A coastal record C1996881752-POCLOUD was read the same way (read 2026-09-15)"
  - id: cmr-cdr
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2491772100-POCLOUD.umm_json
    title: "CMR collection record for ASCATA_L2_25KM_CDR: abstract (first historically reprocessed MetOp-A record, CMOD7, orbit files beginning near the South Pole, 25 km less noisy than 12.5 km but with less small-scale and coastal information), the EUMETSAT DOI, the KNMI CDR user guide and validation report links and the PO.DAAC README; the coastal CDR record C2036877686-POCLOUD was read the same way, with its Verhoef 2017 reference (read 2026-09-15)"
  - id: cmr-esdr-b
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2706513160-POCLOUD.umm_json
    title: "CMR collection record for ASCATB_ESDR_L2_WIND_STRESS_V1.1: abstract (equivalent neutral and true 10 m winds and stress at 12.5 km on the swath, inter-calibrated with MetOp-A, ScatSat-1 and QuikSCAT for an unbroken 1999 to 2022 record, version 1.1 changes, science evaluation by the IOVWST as the stated purpose), DOI, NASA/JPL as processor, the MEaSUREs/OSWV project and the guide and README links; the MetOp-A record C2730520815-POCLOUD, the two Level 3 records (C3402062729 and C3403169610), the two ancillary records (C2705728324 and C2706510710) and the two derivative records (C3401738510 and C3401765750) were read the same way (read 2026-09-15)"
  - id: cmr-granules
    resource: https://cmr.earthdata.nasa.gov/search/granules.json?collection_concept_id=C2075141559-POCLOUD&page_size=1&sort_key=start_date
    title: "CMR granule searches, run 2026-09-15 for each of the fourteen wind collections with sort_key=start_date and sort_key=-start_date and the CMR-Hits header: the first and last granule names, dates and counts quoted in the version field; for the MetOp-B 25 km stream the first granule is ascat_20121029_010001_metopb_00588_eps_o_250_2101_ovw.l2 and the last ascat_20260915_102100_metopb_72608_eps_o_250_3301_ovw.l2"
  - id: podaac-b25
    resource: https://podaac.jpl.nasa.gov/dataset/ASCATB-L2-25km
    title: "PO.DAAC collection page, ASCATB-L2-25km: description, the variable table (bs_distance, ice_age, ice_prob, lat, lon, model_dir, model_speed, time in seconds since 1990-01-01, wind_dir, wind_speed, wvc_index, wvc_quality_flag), documentation links and the citation; the pages for ASCATB-L2-Coastal, ASCATC-L2-25km, ASCATC-L2-Coastal, ASCATA-L2-25km, ASCATA-L2-Coastal, ASCATA_L2_25KM_CDR and ASCATA_L2_COASTAL_CDR were read the same day and carry the same variable table (read 2026-09-15)"
  - id: podaac-esdr-b
    resource: https://podaac.jpl.nasa.gov/dataset/ASCATB_ESDR_L2_WIND_STRESS_V1.1
    title: "PO.DAAC collection page, ASCATB_ESDR_L2_WIND_STRESS_V1.1: the variable table (en_wind speed, direction, u, v with errors and uncorrected fields, real_wind speed, direction, u, v with errors, wind_stress magnitude, direction, u, v with errors, flags, quality_indicator, rain_speed_bias, nudge_wind_speed and direction, distance_from_coast, time in seconds since 1999-01-01), DOI and citation; the MetOp-A page and the two Level 3 pages (whose variable table adds coverage_date, number_of_samples, orbit and overlap and drops the direction fields) were read the same day (read 2026-09-15)"
  - id: podaac-osvw
    resource: https://podaac.jpl.nasa.gov/MEaSUREs-OSVW
    title: "PO.DAAC project page, MEaSUREs Ocean Surface Vector Winds and Wind Stress: the four scatterometers cross-calibrated (MetOp-A ASCAT, MetOp-B ASCAT, QuikSCAT SeaWinds, SCATSAT-1 OSCAT-2) for an unbroken record from October 1999 to May 2022, the four groups of data sets, and the statement that the full record needs all four data sets in a group (read 2026-09-15)"
  - id: doi-esdr-b
    resource: https://doi.org/10.5067/ESASB-L2W11
    title: "The MetOp-B ESDR Level 2 product DOI, resolved 2026-09-15 (HTTP 302) to the Earthdata catalog record; the MetOp-A Level 2 DOI, the two Level 3 DOIs and the two EUMETSAT CDR DOIs (which resolve to the EUMETSAT user portal catalogue) were resolved the same way; no target page was read"
  - id: measures-guide
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/measures_ocean_surface_wind_vectors/open/docs/2022_12_02_MEASURES_NewDataGuide_v17_accepted.pdf
    title: "MEaSUREs project user's guide, Creating an extended and consistent ESDR of the ocean surface winds, stress and their dynamically-significant derivatives for the period 1999-2022, Hristova-Veleva and others, JPL, 1 December 2022, the document the ESDR collection records link as the user's guide (34 pages, read in full 2026-09-15 from the PO.DAAC document archive): goals, product types, the Level 2 file content and flags, data sources (JPL retrieval, NCEP nudging, the CMOD7JPL model function fitted to QuikSCAT), the stress and drag coefficient, the true 10 m winds by COARE 3.5 and GlobCurrent, the quality indicator categories with their ASCAT definitions, the triple-collocation uncertainty and the buoy evaluation"
  - id: esdr-readme
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/measures_ocean_surface_wind_vectors/open/docs/README_latest_measures_v1.1_l2_ascat_scatsat_readmes_2024_06_12_SHV_v08.docx
    title: "MEaSUREs ESDR Level 2 README, version 1.1 products, last modified 12 June 2024, the document the ESDR records link as the README (read 2026-09-15 from the PO.DAAC document archive): the definitions of equivalent neutral and true 10 m winds, the inter-calibration statement, the version 1.1 changes, the ancillary file content and the file naming"
  - id: calval
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ascat/preview/L2/docs/ASCAT_calval_250.pdf
    title: "OSI SAF technical note SAF/OSI/KNMI/TEC/TN/163, Calibration and Validation of ASCAT Winds, version 4.0, 25 November 2008, Verspeek, Portabella, Stoffelen and Verhoef, the document the operational collection records link as calibration and validation (31 pages, read in full 2026-09-15 from the PO.DAAC document archive): the ocean calibration against the CMOD5 cone, CMOD5.n as CMOD5 with a 0.7 m/s input shift for neutral winds, the 0.2 m/s bias of neutral against real 10 m ECMWF winds, and the maximum-likelihood quality control with its 0.4 to 0.5 percent rejection rate"
  - id: cdr-readme
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ascat/open/L2/metop_a/cdr/25km/README.txt
    title: "PO.DAAC README for the 25 km MetOp-A CDR, last updated 20 April 2018 (read 2026-09-15): the directory layout by year and day of year, the file naming convention and the MD5 checksum files"
  - id: verspeek-2010
    resource: https://doi.org/10.1109/TGRS.2009.2027896
    title: "Verspeek, Stoffelen, Portabella, Bonekamp, Anderson and Saldana, 2010, Validation and Calibration of ASCAT Using CMOD5.n, IEEE Transactions on Geoscience and Remote Sensing 48, 386 to 395: the reference the 25 km MetOp-A and MetOp-B records carry (registry record verified 2026-09-15; the record carries no abstract and the article was not read)"
  - id: verhoef-2012
    resource: https://doi.org/10.1109/TGRS.2011.2175001
    title: "Verhoef, Portabella and Stoffelen, 2012, High-Resolution ASCAT Scatterometer Winds Near the Coast, IEEE Transactions on Geoscience and Remote Sensing 50, 2481 to 2487: the reference the MetOp-B coastal record carries (registry record verified 2026-09-15; the record carries no abstract and the article was not read)"
  - id: stoffelen-2017
    resource: https://doi.org/10.1109/JSTARS.2017.2681806
    title: "Stoffelen, Verspeek, Vogelzang and Verhoef, 2017, The CMOD7 Geophysical Model Function for ASCAT and ERS Wind Retrievals, IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing 10, 2123 to 2134: the reference the MetOp-C records carry and the model function the MEaSUREs guide adjusted (registry record verified 2026-09-15; the record carries no abstract and the article was not read)"
  - id: verhoef-2017
    resource: https://doi.org/10.1109/JSTARS.2016.2615873
    title: "Verhoef, Vogelzang, Verspeek and Stoffelen, 2017, Long-Term Scatterometer Wind Climate Data Records, IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing 10, 2186 to 2194: the reference the coastal CDR record carries and the MEaSUREs guide cites for the KNMI reprocessing (registry record verified 2026-09-15; the record carries no abstract and the article was not read)"
  - id: ricciardulli-2021
    resource: https://doi.org/10.3390/rs13183678
    title: "Ricciardulli and Manaster, 2021, Intercalibration of ASCAT Scatterometer Winds from MetOp-A, -B, and -C, for a Stable Climate Data Record, Remote Sensing 13, 3678: the RSS ASCAT record the MEaSUREs guide names as the other climate-quality ASCAT record and CCMP assimilates (registry record verified and abstract read there 2026-09-15; the article was not read)"
  - id: wentz-2017
    resource: https://doi.org/10.1109/JSTARS.2016.2643641
    title: "Wentz and others, 2017, Evaluating and Extending the Ocean Wind Climate Data Record, IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing 10, 2165 to 2185: the science-team statement the MEaSUREs guide cites for the need of several independent records (registry record verified 2026-09-15; the record carries no abstract and the article was not read)"
  - id: ccmp
    resource: ../datasets/ccmp-wind-analysis.md
    title: "This bundle's CCMP dataset concept (read 2026-09-15): the Level 4 analysis that assimilates the RSS ASCAT-A and ASCAT-B records and withholds ASCAT-C"
---

# ASCAT scatterometer ocean surface winds at PO.DAAC

**Identity.** The Advanced Scatterometer (ASCAT) is a C-band,
vertically polarized fan-beam radar on the EUMETSAT MetOp satellites,
with three beams on each side of the ground track giving two swaths of
backscatter from which a wind vector is retrieved in each wind vector
cell.[^cmr-b25][^podaac-osvw][^calval] PO.DAAC distributes ASCAT winds
in two families that differ in producer, retrieval and
content.[^cmr-search] The first is the EUMETSAT Ocean and Sea Ice
Satellite Application Facility (OSI SAF) Level 2 product retrieved at
the Royal Netherlands Meteorological Institute (KNMI): an operational
near-real-time stream at 25 km sampling (50 km effective resolution)
and a coastal stream at 12.5 km sampling (25 km effective resolution)
for each of MetOp-A, MetOp-B and MetOp-C, plus two reprocessed MetOp-A
climate data records at 25 km and 12.5 km coastal sampling covering
2007-01-01 to 2014-04-01.[^cmr-b25][^cmr-bcoastal][^cmr-cdr] The
MetOp-A operational streams end on 2021-11-15 and are marked complete;
the MetOp-B and MetOp-C streams were still receiving orbits on
2026-09-15, the day of the granule search, at a stated latency of
about two hours.[^cmr-a25][^cmr-granules][^cmr-b25] The second family
is the JPL MEaSUREs Ocean Surface Vector Winds Earth System Data Record
(ESDR), which re-retrieves the MetOp-A and MetOp-B backscatter with
JPL's algorithm so that ASCAT winds are consistent with QuikSCAT and
SCATSAT-1 across an unbroken 1999 to 2022 record, and adds fields the
OSI SAF product does not carry: true 10 m winds, wind stress, per-cell
uncertainties, a quality indicator, and separate gridded, ancillary and
spatial-derivative collections.[^cmr-esdr-b][^podaac-osvw][^measures-guide]
The full ESDR record needs all four scatterometers' collections in a
group; the ASCAT ones cover MetOp-A from 2007-01-01 to 2014-04-01 and
MetOp-B from 2013-08-01 to 2022-05-30.[^podaac-osvw][^cmr-granules]
The `resource` above is the MetOp-B 25 km operational stream, the
longest ASCAT stream still receiving data; the version field names
every collection.[^cmr-granules]

**The OSI SAF Level 2 product.** Each file holds one full orbit
assembled from 3-minute granules, in netCDF version 3, beginning at
the first wind vector cell north of the Equator on the ascending node
(the CDR files begin near the South Pole instead).[^cmr-b25][^cmr-cdr]
The variable table on every OSI SAF collection page is the same:
`wind_speed` and `wind_dir` at 10 m, `model_speed` and `model_dir`
(the collocated numerical weather prediction wind), `wvc_quality_flag`,
`ice_prob` (ice probability), `ice_age` (the a-parameter, in dB),
`bs_distance` (backscatter distance), `wvc_index` and `time` in
seconds since 1990-01-01.[^podaac-b25] The retrieval averages the
Level 1B backscatter with a Hamming filter for the 25 km stream and,
for the coastal stream, with a box filter over all full-resolution
backscatter within a 15 km radius of the cell centre after discarding
non-sea measurements, which brings winds to about 15 km from the coast
where the standard product's static land mask keeps about 35
km.[^cmr-b25][^cmr-bcoastal][^verhoef-2012] The geophysical model
function named in the records is CMOD5.n for the MetOp-B streams and
CMOD7.n for MetOp-C and for the last revision of the MetOp-A streams;
CMOD5.n is CMOD5 with a 0.7 m/s shift in input wind speed so that the
retrieved wind is a neutral wind, and the 2008 calibration note
describes the ocean calibration of the backscatter against the CMOD5
cone and a maximum-likelihood quality control tuned to reject about
0.4 to 0.5 percent of cells.[^cmr-b25][^cmr-c25][^cmr-a25][^calval][^verspeek-2010][^stoffelen-2017]
The CDRs use CMOD7 and are described as the first historically
reprocessed MetOp-A record, with the 25 km product less noisy than
12.5 km but carrying less small-scale and coastal
information.[^cmr-cdr][^verhoef-2017] The operational collections
carry no DOI, which the records attribute to the data producer's DOI
ownership; the CDRs carry EUMETSAT DOIs; the products are EUMETSAT
copyright, free to use with the credit line the abstract
gives.[^cmr-b25][^cmr-cdr] The KNMI product manual, which the records
link as the user's guide and which defines the quality flag bits, lies
on a host outside this concept's sources and was not read; the flag
list here is from the collection pages and the calibration note only.[^podaac-b25][^cmr-b25]

**The MEaSUREs ESDR.** The Level 2 files hold one orbital revolution
starting at the southernmost point of the ascending node, at a nominal
12.5 km on the swath, in netCDF4 with ACDD 1.3 and CF 1.8 metadata and
time in seconds since 1999-01-01.[^measures-guide][^esdr-readme] The
retrieval runs JPL's algorithm on the EUMETSAT Level 1B full-resolution
backscatter with NCEP fields for ambiguity nudging and a model function
called CMOD7JPL, CMOD7 modified by a polynomial mapping so that ASCAT
speeds match collocated QuikSCAT retrievals, the main change an
increase of ASCAT winds above 15 m/s.[^measures-guide] Each file
carries three wind kinds and their uncertainties: the equivalent
neutral (EN) wind, relative to the moving surface and calibrated to 10
m under neutral stability; the wind stress, computed from the EN wind
by a linear drag coefficient; and the true 10 m wind, computed from the
EN wind with the COARE 3.5 algorithm run backwards using ERA5 analysis
fields, then with GlobCurrent surface currents added back as a vector
sum.[^measures-guide][^esdr-readme][^podaac-esdr-b] It also carries the
bit-mask `flags` (23 named bits including rain, ice edge, ice nearby,
coastal, high and low wind speed and missing look), the `quality_indicator`
from 0 (no retrieval corruption) to 5 (no data over liquid water),
`rain_speed_bias`, `en_wind_speed_uncorrected`, `nudge_wind_speed` and
`nudge_wind_direction` from the model, and `distance_from_coast`.[^measures-guide][^podaac-esdr-b]
Version 1.1 extended the record to the whole science-quality mission,
improved quality control and added revolution number and equator
crossing attributes; the Level 3 version 1.0 daily grids at 12.5 km
are derived from Level 2 version 1.1 and hold data only where a swath
fell that day, with `number_of_samples`, `orbit` and `overlap` and
without the direction fields.[^cmr-esdr-b][^esdr-readme][^podaac-esdr-b]
The ancillary collections carry ERA5 short-term forecast winds and
stress (forecast rather than analysis, so that scatterometer winds
already assimilated do not enter the comparison), ERA5 analysis SST,
2 m temperature, pressure and boundary layer height, IMERG
precipitation and GlobCurrent currents, all interpolated to the swath,
with the Level 2 flags copied in.[^measures-guide][^esdr-readme] The
collection records state the ESDR's primary purpose as science
evaluation by the NASA International Ocean Vector Winds Science
Team.[^cmr-esdr-b] The other climate-quality ASCAT record, produced
at RSS with its own model function and cross-calibrated across
MetOp-A, -B and -C, is not a PO.DAAC collection but is the ASCAT input
to CCMP.[^ricciardulli-2021][^measures-guide][^ccmp]

## Uncertainty

- **OSI SAF files carry no per-cell error.** Their quality
  information is `wvc_quality_flag`, `bs_distance`, `ice_prob` and
  `ice_age`, plus the collocated model wind for comparison; the
  calibration note's product-level statistics (for example a 0.23 m/s
  standard deviation between two calibration versions and a 0.2 m/s
  neutral-versus-real bias against ECMWF) are for 2008 MetOp-A
  data.[^podaac-b25][^calval]
- **ESDR files carry per-cell uncertainties from triple collocation.**
  Speed and direction errors were estimated by triple collocation of
  QuikSCAT, ASCAT-A and ERA5 first-guess winds over 2007 to 2010 using
  only quality indicator 0 and 1 cells, tabulated for ASCAT as a
  function of wind speed only (cross-track dependence is a stated
  future item), propagated to the components, scaled by bulk factors
  for indicator 2 and 3 cells (about twice and about 1.5 times the
  base error), and copied unchanged to the true wind fields; the
  stress direction error equals the wind direction error and the
  stress magnitude error comes from the same triple
  collocation.[^measures-guide]
- **Buoy evaluation for 2008.** Against NDBC buoys the JPL ASCAT-A
  retrieval with CMOD7JPL has a mean difference of -0.02 m/s and a root
  mean square difference of 1.05 m/s (12064 collocations), against
  -0.04 and 1.07 m/s for the KNMI CMOD7 retrieval, with quality
  flagging lowering both to 0.95 m/s; the guide calls the three ASCAT-A
  variants' differences minuscule.[^measures-guide]
- **Sample sizes in the ASCAT quality classes.** For ASCAT in the ESDR,
  92.4 percent of retrieved cells are indicator 0, 7.2 percent
  indicator 1 (suboptimal swath part or missing looks), 1.4 percent
  indicator 2 (near but not on the ice edge) and 0.4 percent indicator
  3 (on the ice edge); rain is neither detected nor corrected in the
  ASCAT ESDR retrieval, and coastal retrieval is not attempted, so the
  rain and poor-coastal bits do not set for ASCAT.[^measures-guide]

## Known issues

- [scatterometer-rain-and-ice-flags](../gotchas/scatterometer-rain-and-ice-flags.md):
  which cells are winds is decided by the flags, differently in the two
  families; a series at the ice edge or in a rainy region is a series
  of those decisions.
- [neutral-versus-stress-equivalent-wind](../gotchas/neutral-versus-stress-equivalent-wind.md):
  the OSI SAF `wind_speed` and the ESDR `en_wind_speed` are 10 m
  equivalent-neutral winds relative to the moving surface; the ESDR
  `real_wind_*` fields are the only true 10 m winds.
- [bulk-flux-inputs-and-coefficients](../gotchas/bulk-flux-inputs-and-coefficients.md):
  the ESDR stress is the EN wind through one linear drag coefficient
  and a constant air density, and the true wind rests on ERA5 and
  GlobCurrent inputs.
- The operational MetOp-A and MetOp-B records list CMOD5.n (MetOp-B)
  and CMOD7.n (MetOp-A) as the model function "currently" used, and
  the records' `latest_granule_end_time` attributes read 2021-08-03
  for the operational streams and 2021-02-01 for the MetOp-B ESDR while
  the granule searches found orbits through 2026-09-15 and 2022-05-30:
  the additional attributes are stale metadata, and the KNMI anomaly
  pages the records link for processing changes were not
  read.[^cmr-b25][^cmr-a25][^cmr-esdr-b][^cmr-granules]
- The MetOp-A operational 25 km stream's record states a start of
  2007-03-27 17:00 while the first granule found starts 2007-03-28
  00:00, and the coastal stream begins in 2010 while the coastal CDR
  begins in 2007;
  the CDR abstracts point back to the operational streams for data
  after 2014-04-01, so a MetOp-A series across 2014 changes from a
  reprocessed to an operational product.[^cmr-granules][^cmr-cdr][^cmr-a25]
- The ESDR true-wind product has missing files where an input was
  unavailable, sporadically in time and always in some inland seas,
  the Mediterranean named.[^measures-guide]
- The CDRs and the ESDR are two different reprocessings of the same
  MetOp-A years (KNMI CMOD7 against JPL CMOD7JPL harmonized to
  QuikSCAT), and the science team's own statement is that several
  independent records are needed to understand retrieval
  differences.[^cmr-cdr][^measures-guide][^wentz-2017]

**Verification.** The sixteen CMR collection records, the collection
search, fourteen granule searches, twelve PO.DAAC collection pages and
the MEaSUREs project page were read on 2026-09-15; the MEaSUREs guide,
the ESDR README, the 2008 calibration note and the CDR README were read
the same day from the PO.DAAC document archive; six product DOIs were
resolved the same day.[^cmr-search][^cmr-granules][^podaac-b25][^podaac-esdr-b][^podaac-osvw][^measures-guide][^esdr-readme][^calval][^cdr-readme][^doi-esdr-b]
The six papers' registry records were verified on 2026-09-15 (title,
authors, journal, year); only the 2021 record carries an abstract, and
no journal page was
read.[^verspeek-2010][^verhoef-2012][^stoffelen-2017][^verhoef-2017][^ricciardulli-2021][^wentz-2017]
No granule was opened, so the attributes and flag bit values beyond
the guide's listing and the pages' variable tables are not stated
here; the KNMI product manual and CDR user guide, on hosts outside
this concept's sources, were not read.

[^cmr-search]: CMR collection search, POCLOUD provider, keyword ASCAT, 2026-09-15
[^cmr-b25]: CMR collection record, C2075141559-POCLOUD
[^cmr-bcoastal]: CMR collection record, C2075141605-POCLOUD
[^cmr-c25]: CMR collection record, C2075141638-POCLOUD
[^cmr-a25]: CMR collection record, C2075141524-POCLOUD
[^cmr-cdr]: CMR collection record, C2491772100-POCLOUD
[^cmr-esdr-b]: CMR collection record, C2706513160-POCLOUD
[^cmr-granules]: CMR granule searches, fourteen ASCAT wind collections, first and last granule, 2026-09-15
[^podaac-b25]: PO.DAAC collection page, ASCATB-L2-25km
[^podaac-esdr-b]: PO.DAAC collection page, ASCATB_ESDR_L2_WIND_STRESS_V1.1
[^podaac-osvw]: PO.DAAC project page, MEaSUREs-OSVW
[^doi-esdr-b]: Product DOI 10.5067/ESASB-L2W11, resolved 2026-09-15
[^measures-guide]: MEaSUREs OSVW user's guide, Hristova-Veleva and others, 1 December 2022
[^esdr-readme]: MEaSUREs ESDR Level 2 README, 12 June 2024
[^calval]: OSI SAF technical note TN/163, Calibration and Validation of ASCAT Winds, version 4.0, 2008
[^cdr-readme]: PO.DAAC README, 25 km MetOp-A CDR, 20 April 2018
[^verspeek-2010]: Verspeek and others, 2010, IEEE Transactions on Geoscience and Remote Sensing, doi:10.1109/TGRS.2009.2027896
[^verhoef-2012]: Verhoef, Portabella and Stoffelen, 2012, IEEE Transactions on Geoscience and Remote Sensing, doi:10.1109/TGRS.2011.2175001
[^stoffelen-2017]: Stoffelen and others, 2017, IEEE JSTARS, doi:10.1109/JSTARS.2017.2681806
[^verhoef-2017]: Verhoef and others, 2017, IEEE JSTARS, doi:10.1109/JSTARS.2016.2615873
[^ricciardulli-2021]: Ricciardulli and Manaster, 2021, Remote Sensing, doi:10.3390/rs13183678
[^wentz-2017]: Wentz and others, 2017, IEEE JSTARS, doi:10.1109/JSTARS.2016.2643641
[^ccmp]: This bundle's CCMP dataset concept
