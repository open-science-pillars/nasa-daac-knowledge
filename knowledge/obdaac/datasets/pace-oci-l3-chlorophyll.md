---
type: dataset
spheres: [biosphere, hydrosphere]
title: "PACE OCI Level 3 mapped chlorophyll-a (OB.DAAC, the BGC suite, version 3.2)"
description: "The Ocean Biology Processing Group's Level 3 mapped chlorophyll-a from the Ocean Color Instrument on PACE: since version 3.2 the chlor_a variable lives in the OC_BGC suite file beside phytoplankton carbon, particulate organic carbon and particulate inorganic carbon, on 4 km and 0.1 degree equidistant cylindrical grids as daily, 8-day and monthly composites from 5 March 2024 onward, at provisional maturity, from the same blended OCI algorithm as the heritage sensors with OC4 coefficients; the record has been through five versions (1, 2, 3, 3.1 and 3.2, four reprocessings) since the first release on 11 April 2024, and the catalogue keeps only version 3.2."
tags: [pace, oci, chlorophyll, chlor_a, ocean-color, level3, mapped, obdaac, obpg, bgc, provisional, oci-algorithm]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:30:00Z }
resource: https://cmr.earthdata.nasa.gov/search/concepts/C4184125847-OB_CLOUD.umm_json
version: "Version 3.2 (the April 2026 reprocessing; files carry processing_version 3.2), CMR-verified 2026-09-14: PACE_OCI_L3M_BGC version 3.2 (C4184125847-OB_CLOUD, DOI 10.5067/PACE/OCI/L3M/OC_BGC/3.2, 2000 granule records, temporal extent from 2024-03-05 with no end, first daily granule 2024-03-05, last 2026-07-31) and the near-real-time collection PACE_OCI_L3M_BGC_NRT version 3.2 (C4184125829-OB_CLOUD, no DOI, last daily granule 2026-09-12); no collection with a CHL short name and no binned BGC collection was catalogued on that date"
status: draft
stale_after: 2027-03-14
sources:
  - id: cmr-pace
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C4184125847-OB_CLOUD.umm_json
    title: "CMR collection record for PACE_OCI_L3M_BGC version 3.2 (read 2026-09-14): entry title, DOI, temporal extent from 2024-03-05 ending at present, platform PACE and instrument OCI, the abstract describing the PIC, POC, CHL and CARBON products with the coastal and inland water caveat, and the related links to the OPeNDAP service, the direct data access directory, the four ATBDs and the version 1, 2 and 3 release notes"
  - id: cmr-pace-nrt
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C4184125829-OB_CLOUD.umm_json
    title: "CMR collection record for PACE_OCI_L3M_BGC_NRT version 3.2 (read 2026-09-14): no DOI because it is a near-real-time dataset, and the abstract stating that near-real-time products use the best available ancillary data and a calibration that are less than optimal"
  - id: cmr-collections
    resource: https://cmr.earthdata.nasa.gov/search/collections.json?short_name=PACE_OCI_L3M_*&options[short_name][pattern]=true&page_size=100
    title: "CMR collection searches run 2026-09-14: the short-name pattern PACE_OCI_L3M_* lists the mapped suites (AOP, IOP, KD, PAR and BGC at version 3.2; AER_UAA, CLOUD, LANDVI, SFREFL, UVAI_UAA and CLOSE at 3.1; TRGAS at 3.0, each with a near-real-time twin), exact searches for PACE_OCI_L3M_CHL and PACE_OCI_L3B_CHL return nothing, and the pattern PACE_OCI_L3B_* lists no BGC binned collection"
  - id: cmr-granules
    resource: https://cmr.earthdata.nasa.gov/search/granules.json?collection_concept_id=C4184125847-OB_CLOUD&temporal=2024-06-15T12:00:00Z,2024-06-15T12:00:01Z&page_size=500
    title: "CMR granule searches run 2026-09-14 on C4184125847-OB_CLOUD: the six granules whose period contains 2024-06-15 (DAY, 8D and MO at 4km and 0p1deg), the granules of calendar 2025 counted by period and grid (363 daily, 46 8-day and 12 monthly per grid), the first granules by start date (2024-03-05) and the last (2026-07-31), the CMR-Hits header (2000), and the same search on the near-real-time collection (last daily granule 2026-09-12)"
  - id: pace-file
    resource: https://oceandata.sci.gsfc.nasa.gov/opendap/PACE_OCI/L3SMI/2024/0601/PACE_OCI.20240601_20240630.L3m.MO.BGC.V3_2.4km.nc.das
    title: "The attribute listing (OPeNDAP .das, metadata only, no data read) of the June 2024 monthly 4 km BGC file, read 2026-09-14 through the OPeNDAP service the CMR record lists: the variables poc, pic, chlor_a and carbon_phyto with their long names, units, fill values, valid ranges and reference attributes (chlor_a cites Hu, Lee and Franz 2012), the grid attributes, temporal_range month, measure Mean, processing_version 3.2, date_created 2026-05-16, the l3mapmerge history and the product DOI; the same listing read for the daily 0.1 degree file of 2026-07-31 (1800 by 3600 cells, 11.13 km, created 2026-08-26)"
  - id: catalog-pace
    resource: https://doi.org/10.5067/PACE/OCI/L3M/OC_BGC/3.2
    title: "The product DOI, which resolved on 2026-09-14 to the Earthdata catalog page for PACE_OCI_L3M_BGC version 3.2 (read there): the description, the concept id, netCDF-4 format and the temporal extent 2024-03-05 to present"
  - id: pace-v3-notes
    resource: https://oceancolor.gsfc.nasa.gov/files/reprocessing/PACE_OCI_V3_Release_Notes.pdf
    title: "PACE OCI V3 Processing Notes, release date April 2026, 22 pages, read in full 2026-09-14 (the OB.DAAC URL redirects to the same file on the OB.DAAC data host, where the CMR record links it): the version history from 1 to 3.2, the OCI Level 1 changes and known issues, the OC_AOP, OC_IOP and OC_BGC suite changes and known issues, the Level 3 product list and the appendix on data levels, composites, grids and maturity levels, with the version 2 notes appended"
  - id: pace-v2-notes
    resource: https://oceancolor.gsfc.nasa.gov/files/reprocessing/PACE_Science_Data_V2_Release_Notes.pdf
    title: "PACE Science Data Reprocessing, Version 2, 13 pages, read 2026-09-14: the first full-mission reprocessing, its calibration changes, the Level 2 flagging and Level 3 masking changes and the BGC suite's chlor_a and chlor_a_unc products"
  - id: pace-v1-notes
    resource: https://oceancolor.gsfc.nasa.gov/files/reprocessing/PACE_Science_Data_V1_Release_Notes.pdf
    title: "PACE Science Data Initial Release Notes, 9 pages, read 2026-09-14: launch on 8 February 2024, commissioning completed 5 April 2024, the version 1 release with its caution, the processing levels and granule organization"
  - id: atbd
    resource: https://oceancolor.gsfc.nasa.gov/files/atbd/atbd-obdaac-chlorophyll-a.pdf
    title: "Chlorophyll a, Algorithm Theoretical Basis Document version 1.1, 6 November 2023, Werdell, O'Reilly, Hu, Feng, Lee, Franz, Bailey, Proctor and Wang, DOI 10.5067/JCQB8QALDOYD, 18 pages, read in full 2026-09-14: the blended OCI algorithm, the sensor coefficient table with the PACE OCI row (OC4, the greatest of the 442, 490 and 510 nm reflectances over 555 nm), the 0.25 to 0.35 transition, the validation method, the accuracy goals and the statement that the PACE mission adopted more rigorous reflectance uncertainties"
  - id: ancillary
    resource: https://oceancolor.gsfc.nasa.gov/files/obdaac-ancillary-data-sources.pdf
    title: "Ancillary Data at OB.DAAC (8 pages, read 2026-09-14): the two-step processing, near-real-time with the best ancillary data available at the time and refined processing once the optimal ancillary data exist"
  - id: werdell-2019
    resource: https://doi.org/10.1175/BAMS-D-18-0056.1
    title: "Werdell and others, 2019, The Plankton, Aerosol, Cloud, ocean Ecosystem mission, status, science, advances, Bulletin of the American Meteorological Society 100, 1775 to 1794 (registry record verified on Crossref and abstract read there 2026-09-14; the publisher page was not reachable from this environment and the article was not read): the mission overview, the primary instrument as a spectrometer from the ultraviolet to the shortwave infrared with a 1 km ground sample distance at nadir, and the two multi-angle polarimeters"
  - id: hu-2012
    resource: https://doi.org/10.1029/2011JC007395
    title: "Hu, Lee and Franz, 2012, Chlorophyll a algorithms for oligotrophic oceans, a novel approach based on three-band reflectance difference, Journal of Geophysical Research: Oceans 117, C01011 (registry record verified on Crossref and abstract read there 2026-09-14; the publisher page returned 403 and the article was not read): the color index the file's reference attribute cites"
  - id: hu-2019
    resource: https://doi.org/10.1029/2019JC014941
    title: "Hu, Feng, Lee, Franz, Bailey, Werdell and Proctor, 2019, Improving satellite global chlorophyll a data products through algorithm refinement and data recovery, Journal of Geophysical Research: Oceans 124, 1524 to 1543 (registry record verified on Crossref and abstract read there 2026-09-14; the article was not read): the OCI2 parameterization the ATBD names as current"
---

# PACE OCI Level 3 mapped chlorophyll-a

**Identity.** The Plankton, Aerosol, Cloud, ocean Ecosystem
observatory launched on 8 February 2024 and completed commissioning
on 5 April 2024; its primary instrument, the Ocean Color Instrument,
is a spectrometer spanning the ultraviolet to the shortwave infrared
with a 1 km ground sample distance at nadir, flown with two
multi-angle polarimeters.[^pace-v1-notes][^werdell-2019] The Ocean
Biology Processing Group's Level 3 mapped chlorophyll-a from OCI is,
since version 3.2, one variable of the Ocean Color Biogeochemical
suite: the collection PACE_OCI_L3M_BGC version 3.2
(C4184125847-OB_CLOUD, DOI 10.5067/PACE/OCI/L3M/OC_BGC/3.2, temporal
extent from 5 March 2024 with no end), whose files carry `chlor_a`
beside `carbon_phyto`, `poc` and `pic`; before 3.2 each product was
distributed as a separate Level 3 mapped product, and on 2026-09-14
CMR catalogued no collection with a CHL short name, no binned BGC
collection and no earlier version of the mapped
suite.[^cmr-pace][^pace-v3-notes][^cmr-collections] A near-real-time
twin, PACE_OCI_L3M_BGC_NRT (C4184125829-OB_CLOUD), carries no DOI and
is processed with ancillary data and a calibration the producer
describes as less than optimal, later replaced by the refined
processing.[^cmr-pace-nrt][^ancillary] The chlorophyll algorithm is
the same blended OCI algorithm applied to every NASA ocean color
sensor, with the PACE OCI coefficients of the OC4 form (the greatest
of the 442, 490 and 510 nm reflectances over the 555 nm reflectance)
and the color index below 0.25 mg per cubic metre; the file's
`chlor_a` reference attribute cites the 2012 color index paper, where
the MODIS-Aqua file cites the 2019
retuning.[^atbd][^pace-file][^hu-2012][^hu-2019] The products are
released at provisional maturity, which the processing notes define
as reviewed and in family with heritage products or other
expectations but not yet validated and possibly still containing
significant errors.[^pace-v3-notes]

**Structure.** The processing notes state that Level 2 products are
binned onto a quasi-equal-area integerized sinusoidal grid of 4.6 km
or 9.2 km bins and mapped by reprojection onto equirectangular grids;
the catalogue holds the BGC suite at two grids, 4 km (4320 by 8640
cells, 4.638 km, the same grid as the MODIS-Aqua 4 km files) and 0.1
degree (1800 by 3600 cells, 11.13 km), and at three periods, DAY, 8D
and MO, with 363 daily, 46 8-day and 12 monthly records per grid in
calendar 2025 and no rolling, seasonal, annual or climatology
files.[^pace-v3-notes][^pace-file][^cmr-granules] File names read
PACE_OCI.<start>_<end>.L3m.<period>.BGC.V3_2.<4km or 0p1deg>.nc; the
mapped file is assembled by l3mapmerge, carries `temporal_range`,
`measure` "Mean", `processing_version` 3.2, `date_created` (the June
2024 monthly file was created on 2026-05-16, the reprocessing date,
not the month's) and the product DOI, and holds no count, flag or
uncertainty layer.[^pace-file] `chlor_a` is float32 in mg per cubic
metre with fill -32767 and valid range 0.001 to 100; `pic` is
"Calcite Concentration, CI2 algorithm", `poc` the Stramski 2022 hybrid
particulate organic carbon and `carbon_phyto` "Phytoplankton
Carbon".[^pace-file] The collection counted 2000 granule records on
2026-09-14 with the last refined daily granule on 2026-07-31 (created
2026-08-26) and the near-real-time collection's last on
2026-09-12.[^cmr-granules][^pace-file] The version history is short
and dense: version 1 released 11 April 2024 as highly preliminary;
version 2 the first full-mission reprocessing, mainly calibration,
which also added the commissioning-period data from February 2024;
version 3 with a solar-diffuser-only calibration, the first system
vicarious calibration gains, a polarization correction, a
hyperspectral BRDF table and the masking of extreme glint; version
3.1 in August 2025 with a ghosting correction, corrected vicarious
gains in the red and refined gas corrections; version 3.2 in April
2026, which fixed an implementation error in the bidirectional
reflectance correction (the relative azimuth across the scan), with
what the notes call a significant improvement in the accuracy and
cross-track stability of the reflectances, updated vicarious gains and
the consolidation of the suites into single Level 3
files.[^pace-v1-notes][^pace-v2-notes][^pace-v3-notes]

## Uncertainty

- **The Level 2 suite carries chlor_a_unc; the Level 3 mapped file
  does not.** The processing notes list phytoplankton chlorophyll-a
  uncertainties (chlor_a_unc) as a provisional Level 2 product of the
  BGC suite, and the mapped BGC file read on 2026-09-14 holds poc, pic,
  chlor_a and carbon_phyto and no uncertainty
  variable.[^pace-v3-notes][^pace-file]
- **Provisional means unvalidated.** By the producer's definition
  the products have been reviewed and are in family with heritage
  products but have not been validated and may still contain
  significant errors; the notes' known-issues entry for the BGC suite
  reads "TBD".[^pace-v3-notes]
- **Reflectance issues propagate.** The BGC products are derived from
  the reflectances, and the notes' AOP known issues carry over:
  ultraviolet reflectances are unvalidated, residual absorbing-gas
  artifacts remain especially in the red, erroneously elevated red
  reflectance near the scan edge is flagged at Level 2 and masked at
  Level 3 above 60 degrees view zenith, and pixels flagged for
  coccolithophores are masked in the Level 3 ocean color products
  (version 3.2 lifted that mask for the AOP products only, on the
  ground that reflectances at moderate coccolithophore concentration
  are valid).[^pace-v3-notes]
- **The community accuracy goal and the mission's stricter one.** The
  ATBD quotes the generally accepted goals of plus or minus 5 percent
  for water-leaving radiance and plus or minus 35 percent for
  open-ocean chlorophyll and states that the PACE mission adopted more
  rigorous uncertainties for the reflectances retrieved by OCI; neither
  is a measured error of this version.[^atbd]
- **The collection's own caveat.** The collection description states
  that retrievals in optically complex coastal and inland waters may
  carry higher uncertainty.[^cmr-pace][^catalog-pace]

## Known issues

- [chlor-a-blended-ocx-and-ci](../gotchas/chlor-a-blended-ocx-and-ci.md):
  chlor_a is two algorithms blended between 0.25 and 0.35 mg per
  cubic metre; a threshold or gradient inside that range measures the
  blend.
- [chlor-a-composite-sampling-gaps](../gotchas/chlor-a-composite-sampling-gaps.md):
  a composite is the mean of the observations that survived the
  flags, with no count in the mapped file.
- [chlor-a-one-reprocessing-per-series](../gotchas/chlor-a-one-reprocessing-per-series.md):
  five versions in two years, one kept in the catalogue, and a
  near-real-time tail processed differently from the refined record.
- [chlor-a-is-not-biomass](../gotchas/chlor-a-is-not-biomass.md):
  the same file carries phytoplankton carbon as a separate product,
  and net primary production is a separate Level 4 product.
- The processing notes describe the mapped composites as 0.1 degree
  and 1 degree in one place and as 4.6 km, 0.1 degree and 1 degree in
  the appendix; the catalogue holds the BGC suite at 4 km and 0.1
  degree only.[^pace-v3-notes][^cmr-granules]
- The OB.DAAC website redirected to the Ocean Biology DAAC landing
  page on the Earthdata site on 2026-09-14; the release notes and
  ATBDs remain reachable at their /files/ paths by redirect to the
  data host, which is where the CMR record links
  them.[^cmr-pace][^pace-v3-notes]

[^cmr-pace]: CMR collection record, C4184125847-OB_CLOUD
[^cmr-pace-nrt]: CMR collection record, C4184125829-OB_CLOUD
[^cmr-collections]: CMR collection searches, 2026-09-14
[^cmr-granules]: CMR granule searches on the refined and near-real-time collections, 2026-09-14
[^pace-file]: Attribute listings of two PACE OCI L3m BGC files, read through OPeNDAP on 2026-09-14
[^catalog-pace]: The product DOI and the Earthdata catalog page it resolves to, 2026-09-14
[^pace-v3-notes]: PACE OCI V3 Processing Notes, April 2026
[^pace-v2-notes]: PACE Science Data Reprocessing, Version 2
[^pace-v1-notes]: PACE Science Data Initial Release Notes
[^atbd]: Chlorophyll a ATBD version 1.1, OB.DAAC, 6 November 2023
[^ancillary]: Ancillary Data at OB.DAAC
[^werdell-2019]: Werdell and others, 2019, Bulletin of the American Meteorological Society, doi:10.1175/BAMS-D-18-0056.1
[^hu-2012]: Hu, Lee and Franz, 2012, Journal of Geophysical Research: Oceans, doi:10.1029/2011JC007395
[^hu-2019]: Hu and others, 2019, Journal of Geophysical Research: Oceans, doi:10.1029/2019JC014941
