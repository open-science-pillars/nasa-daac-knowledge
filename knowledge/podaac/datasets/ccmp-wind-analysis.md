---
type: dataset
spheres: [hydrosphere, atmosphere]
title: "CCMP version 3.1 ocean surface wind analysis (RSS, 6-hourly and monthly)"
description: "Level 4 gridded 10 m neutral-stability ocean vector winds at 0.25 degrees from 1993 onward, produced by Remote Sensing Systems by variationally combining inter-calibrated radiometer and scatterometer winds with an adjusted ERA5 background; PO.DAAC distributes version 3.1 as a 6-hourly and a monthly collection. The files carry a nobs field that says where satellites contributed and no uncertainty field; where nobs is zero the value is the adjusted background."
tags: [ccmp, ocean-winds, wind-analysis, level4, era5, scatterometer, radiometer, rss, measures, podaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T13:30:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-15T14:22:23Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/163 }
resource: https://podaac.jpl.nasa.gov/dataset/CCMP_WINDS_10M6HR_L4_V3.1
version: "Version 3.1 from Remote Sensing Systems in two POCLOUD collections, CMR-verified 2026-09-15 with granule ranges from a first-and-last granule search the same day: 6-hourly CCMP_WINDS_10M6HR_L4_V3.1 (C2916514952-POCLOUD, DOI 10.5067/CCMP-6HW10M-L4V31, daily files from 1993-01-02 through 2026-07-20, 12240 granules) and monthly CCMP_WINDS_10MMONTHLY_L4_V3.1 (C2916529935-POCLOUD, DOI 10.5067/CCMP-MW10M-L4V31, monthly files from 1993-01 through 2026-06, 402 granules); both records open-ended, released at PO.DAAC 2024-07-01; the user guide is dated 15 July 2024"
status: stable
stale_after: 2027-03-15
sources:
  - id: podaac-6hr
    resource: https://podaac.jpl.nasa.gov/dataset/CCMP_WINDS_10M6HR_L4_V3.1
    title: "PO.DAAC collection page, CCMP_WINDS_10M6HR_L4_V3.1: description, DOI, platform list, variable table (latitude, longitude, nobs, time, uwnd, vwnd, ws), the user guide link, the S3 prefixes and the citation (read 2026-09-15)"
  - id: podaac-monthly
    resource: https://podaac.jpl.nasa.gov/dataset/CCMP_WINDS_10MMONTHLY_L4_V3.1
    title: "PO.DAAC collection page, CCMP_WINDS_10MMONTHLY_L4_V3.1: description, DOI and variable table (nobs, u, u_anom, v, v_anom, w, w_anom) (read 2026-09-15)"
  - id: cmr-6hr
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2916514952-POCLOUD.umm_json
    title: "CMR collection record for the 6-hourly collection: abstract, open-ended temporal extent from 1993-01-01 at 6-hour resolution, bounding rectangle 80S to 80N, sixteen platforms, processing level 4, RSS as processor and PO.DAAC as archiver, the MEaSUREs project, the two publication references, MetadataDates (created 2024-04-01, updated 2024-07-22) and the S3 prefixes (read 2026-09-15)"
  - id: cmr-monthly
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2916529935-POCLOUD.umm_json
    title: "CMR collection record for the monthly collection: abstract, open-ended temporal extent from 1993-01-01, the same platforms, references and dates as the 6-hourly record (read 2026-09-15)"
  - id: cmr-search
    resource: https://cmr.earthdata.nasa.gov/search/collections.json?provider=POCLOUD&keyword=CCMP
    title: "CMR collection search for CCMP at the POCLOUD provider, run 2026-09-15: the two version 3.1 collections are the only CCMP collections PO.DAAC holds; a search of the legacy PODAAC provider returned none, and a keyword search across all providers found only these two and an NCAR catalogue entry for the pre-3.1 record"
  - id: cmr-granules-6hr
    resource: https://cmr.earthdata.nasa.gov/search/granules.json?collection_concept_id=C2916514952-POCLOUD&page_size=1&sort_key=start_date
    title: "CMR granule search for the 6-hourly collection, run 2026-09-15 with sort_key=start_date and again with sort_key=-start_date: first granule CCMP_Wind_Analysis_19930102_V03.1_L4 (1993-01-02), last granule CCMP_Wind_Analysis_20260720_V03.1_L4 (2026-07-20); the CMR-Hits header read 12240"
  - id: cmr-granules-monthly
    resource: https://cmr.earthdata.nasa.gov/search/granules.json?collection_concept_id=C2916529935-POCLOUD&page_size=1&sort_key=start_date
    title: "CMR granule search for the monthly collection, run 2026-09-15 with sort_key=start_date and with sort_key=-start_date: first granule CCMP_Wind_Analysis_199301_monthly_mean_V03.1_L4, last granule CCMP_Wind_Analysis_202606_monthly_mean_V03.1_L4; the CMR-Hits header read 402"
  - id: doi-6hr
    resource: https://doi.org/10.5067/CCMP-6HW10M-L4V31
    title: "The 6-hourly product DOI, resolved 2026-09-15 (HTTP 302) to the Earthdata catalog record for the collection; the target page was not read"
  - id: doi-monthly
    resource: https://doi.org/10.5067/CCMP-MW10M-L4V31
    title: "The monthly product DOI, resolved 2026-09-15 (HTTP 302) to the Earthdata catalog record for the collection; the target page was not read"
  - id: guide
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ccmp/open/L4_V3.1/docs/User_Guide_3.1.r1.pdf
    title: "CCMP Ocean Surface Wind Velocity Product User Guide, Version 3.1, 15 July 2024, Mears and Henze, the document the collection pages link as the user's guide (14 pages, read in full 2026-09-15 from the PO.DAAC document archive): abstract, version history table, processing flow, assimilated data, pre-analysis adjustments and quality control, the daily and monthly file structure tables, the validation against ASCAT-C and moored buoys with its two statistics tables, and the caveats on tropical cyclones and long-term trends"
  - id: mears-2022
    resource: https://doi.org/10.3390/rs14174230
    title: "Mears, Lee, Ricciardulli, Wang and Wentz, 2022, Improving the Accuracy of the Cross-Calibrated Multi-Platform (CCMP) Ocean Vector Winds, Remote Sensing 14, 4230: the version 3.0 method paper the guide and the collection records cite (registry record verified and abstract read there 2026-09-15; the article was not read)"
  - id: atlas-2011
    resource: https://doi.org/10.1175/2010BAMS2946.1
    title: "Atlas, Hoffman, Ardizzone, Leidner, Jusem, Smith and Gombos, 2011, A Cross-calibrated, Multiplatform Ocean Surface Wind Velocity Product for Meteorological and Oceanographic Applications, Bulletin of the American Meteorological Society 92, 157 to 174: the variational analysis the guide cites for the method (registry record verified 2026-09-15; the record carries no abstract and the article was not read)"
  - id: ricciardulli-2021
    resource: https://doi.org/10.3390/rs13183678
    title: "Ricciardulli and Manaster, 2021, Intercalibration of ASCAT Scatterometer Winds from MetOp-A, -B, and -C, for a Stable Climate Data Record, Remote Sensing 13, 3678: the RSS ASCAT wind record version 3.1 assimilates, cross-calibrated to about 0.1 m/s at the global monthly scale (registry record verified and abstract read there 2026-09-15; the article was not read)"
  - id: manaster-2019
    resource: https://doi.org/10.1175/jtech-d-18-0116.1
    title: "Manaster, Ricciardulli and Meissner, 2019, Validation of High Ocean Surface Winds from Satellites Using Oil Platform Anemometers, Journal of Atmospheric and Oceanic Technology 36, 803 to 818: the high-wind validation the guide cites, whose abstract reports the analyses of the time (ECMWF, NCEP and the then-current CCMP) significantly lower than anemometer winds with biases growing with wind speed (registry record verified and abstract read there 2026-09-15; the article was not read)"
  - id: oscar
    resource: ../datasets/oscar-v2.md
    title: "This bundle's OSCAR dataset concept (read 2026-09-15): the surface current product the guide names, without a collection, as the input for the moving-surface adjustment of the ERA5 background; its final and interim collections compute the wind-driven term from ERA5 winds, the near-real-time one from NCEP/NCAR Reanalysis 1, and its values are averages over the top 30 m"
---

# CCMP version 3.1 ocean surface wind analysis

**Identity.** The Cross-Calibrated Multi-Platform (CCMP) ocean vector
wind analysis is a Level 4 product from Remote Sensing Systems (RSS)
that combines satellite retrievals of ocean surface wind with a
background wind field from a numerical weather prediction model by a
variational method, giving a spatially complete estimate of near-global
ocean vector winds at six-hour intervals on a 0.25 degree
grid.[^guide][^cmr-6hr][^mears-2022] PO.DAAC holds version 3.1 in two
collections and no other CCMP version: a 6-hourly collection with one
file per day and a monthly-mean collection with one file per month,
both from 1993-01-01 and open-ended, with RSS as processor and PO.DAAC
as archiver and distributor.[^cmr-search][^cmr-6hr][^cmr-monthly] The
6-hourly collection's first granule found by a start-date search is
dated 1993-01-02, one day after the record's stated start; the
collection abstract gives an expected latency of two to three months
for new files, and the last granules found on 2026-09-15 were
2026-07-20 (6-hourly) and June 2026
(monthly).[^cmr-granules-6hr][^cmr-granules-monthly][^cmr-6hr] The
inputs are RSS retrievals from most of the wind-sensing U.S., Japanese
and European microwave satellites flown to date (the records list
sixteen platforms: SSM/I and SSMIS on eight DMSP satellites, TMI,
AMSR-E, AMSR2, GMI, WindSat, SeaWinds on QuikSCAT and ASCAT on MetOp-A
and MetOp-B) and a background of ERA5 10 m neutral-stability
winds.[^cmr-6hr][^podaac-6hr][^guide] Version 3.1 differs from 3.0
only in adding ASCAT-B to the assimilated data; ASCAT-C and buoy winds
are withheld as independent validation.[^guide] The earlier versions
ran on ERA-40 and ERA-Interim backgrounds, assimilated buoys and
applied no pre-analysis adjustments; version 1.0 was led from Goddard
under the MEaSUREs program, and version 3.1 is produced and maintained
by RSS under a NASA grant.[^guide][^cmr-6hr][^atlas-2011]

**What the analysis does.** The analysis minimizes a cost function
that constrains both the differences between the inputs and the final
product and the smoothness of those differences, so the field is very
close to the satellite winds where and when they exist and transitions
smoothly to the adjusted background with distance from a
swath.[^guide][^atlas-2011] Before the analysis, ERA5 neutral winds
are adjusted for the moving ocean surface with the OSCAR surface
current product, then scaled by a multiplicative speed adjustment
whose form was found by matching wind-speed histograms of ERA5 against
collocated scatterometer winds (ERA5 winds run lower than satellite
winds, especially at high speed), then corrected by subtracting
seasonally varying smoothed bias maps in the u and v components;
radiometer wind speeds are adjusted by small additive, time- and
location-dependent terms to agree with scatterometer
winds.[^guide][^mears-2022][^oscar] Radiometers measure scalar speed
only, so wind direction in the analysis comes from the scatterometers
(QuikSCAT, ASCAT-A, ASCAT-B) and from the background; WindSat's
direction is not used.[^guide] The ASCAT input is the RSS
ASCAT record cross-calibrated across MetOp-A, -B and -C to about 0.1
m/s at the global monthly scale, of which the MetOp-C part is
withheld; QuikSCAT is the other scatterometer
input.[^ricciardulli-2021][^guide] Radiometer
retrievals are excluded where total cloud water exceeds 0.18 mm (rain
likely), scatterometer retrievals flagged for rain by the retrieval's
own rain detection are excluded, and no retrieval influenced by sea
ice is used.[^guide]

**Structure.** The daily files, named
`CCMP_Wind_Analysis_YYYYMMDD_V03.1_L4.nc`, are CF-compliant netCDF4
with four analysis times (00, 06, 12 and 18 UTC) on a 720 by 1440
grid, carrying `uwnd` and `vwnd` (10 m neutral zonal and meridional
wind, m/s), `ws` (10 m neutral wind speed, m/s), `nobs` (the number of
satellites assimilated at each grid cell, zero where no satellite
observation fell inside the 6-hour assimilation window) and `time` in
hours since 1987-01-01.[^guide][^podaac-6hr] The monthly files, named
`CCMP_Wind_Analysis_YYYYMM_monthly_mean_V03.1_L4.nc`, carry the
monthly average speed `w` and components `u` and `v`, anomalies
`w_anom`, `u_anom` and `v_anom` relative to a 1995 to 2014
climatology, and `nobs` redefined as the number of time steps averaged
at each cell; the guide notes that the average wind speed can be very
different from the magnitude of the averaged
components.[^guide][^podaac-monthly] The collection records give the
bounding rectangle as 80S to 80N while the file grid has 720 latitude
cells; both statements are the sources' own and the bundle does not
reconcile them.[^cmr-6hr][^guide] The records' S3 prefixes for both
collections read `CCMP_RSS_L3.0_WIND_VECTORS_V2.0`, a bucket name from
an earlier version that the version 3.1 records still
carry.[^cmr-6hr][^cmr-monthly][^podaac-6hr]

## Uncertainty

- **No uncertainty field ships with the product.** The daily files
  carry the three wind fields and `nobs`, the monthly files the means,
  anomalies and `nobs`; nothing in the files estimates the error of a
  value.[^guide][^podaac-6hr][^podaac-monthly]
- **What stands in.** `nobs` is the product's own statement of whether
  a value rests on satellites or on the adjusted background, and the
  guide's validation shows the difference: against the withheld
  ASCAT-C over 2019-07 to 2023-05 the wind-speed difference (CCMP
  minus ASCAT-C) has a mean of 0.08 m/s and a standard deviation of
  0.88 m/s over all collocations, 0.75 m/s where at least one satellite
  was assimilated and 1.25 m/s where none was; against NDBC moored
  buoys over 1993 to 2022 (about 3.6 million collocations, hour-long
  buoy averages, TAO winds multiplied by 0.9 after their instrument
  change) the wind-speed bias is -0.02 m/s with a standard deviation of
  1.13 m/s overall, 0.97 m/s with satellites and 1.45 m/s
  without.[^guide] The guide adds that the with-and-without contrast
  may be overstated because many of the no-satellite collocations are
  at high latitudes where winds are higher.[^guide]
- **High winds are biased high by design.** Above roughly 15 to 18 m/s
  version 3.1 runs higher than both ASCAT-C and the buoys; the guide
  states this is intended and supported by comparisons against
  airborne radiometers, dropsondes, saildrones, oil-platform
  anemometers and L-band radiometers, and the oil-platform study it
  cites found the earlier analyses, CCMP included, significantly lower
  than anemometer winds with the bias growing with
  speed.[^guide][^manaster-2019] Buoy winds above about 15 m/s are
  themselves biased low by wave shadowing, platform tilt and spray.[^guide]
- **The value is a 10 m neutral-stability wind.** The background is
  ERA5 neutral winds, chosen because both satellite wind types respond
  to wind-induced roughness, which follows stress and so
  neutral-stability wind speed; the gotcha on neutral versus
  stress-equivalent winds carries what that means for a comparison
  against an anemometer or a real 10 m wind.[^guide]

## Known issues

- [wind-analysis-is-not-observation](../gotchas/wind-analysis-is-not-observation.md):
  the field is complete everywhere, but where `nobs` is zero the value
  is the adjusted ERA5 background, in rain the satellite input was
  excluded, and the guide states the product does not resolve tropical
  cyclones and that large-scale long-term changes are comparable to
  its own long-term errors.
- [neutral-versus-stress-equivalent-wind](../gotchas/neutral-versus-stress-equivalent-wind.md):
  the winds are 10 m neutral-stability winds on an ERA5 neutral
  background adjusted for surface currents, not real 10 m winds.
- [bulk-flux-inputs-and-coefficients](../gotchas/bulk-flux-inputs-and-coefficients.md):
  a stress or flux computed from these winds, and from the monthly
  means in particular, carries the analysis error and the chosen
  transfer coefficient.
- Version 3.1's stated improvements over 2.0 are better agreement with
  satellite winds at high speed, minimized spurious trends caused by
  the interaction between the varying number of satellite measurements
  and the satellite and model biases, and better quality after 2012;
  the 3.0 paper's abstract describes the spurious interannual to
  decadal variations in version 2.0 that the adjustments were designed
  to remove.[^cmr-6hr][^mears-2022]
- The guide's own caveats: tropical cyclones and other intense compact
  wind events are not well resolved in ERA5 and the satellite data are
  often missing there through rain contamination, and the guide states
  the product is not for the analysis of these events; at global and
  basin scales decadal wind-speed changes are expected to be small or
  comparable to the product's long-term errors, so the guide asks for
  caution with large-scale long-term changes and calls regional
  changes larger than a few tenths of a metre per second usable.[^guide]
- ERA5 enters CCMP twice: as the background, and inside the OSCAR
  surface current used to adjust that background, because OSCAR's
  wind-driven term is computed from ERA5 10 m winds in its final and
  interim collections (the near-real-time collection uses NCEP/NCAR
  Reanalysis 1 winds). The guide names the product as OSCAR without
  saying which collection, and an OSCAR value is an average over the
  top 30 m rather than a surface current.[^guide][^oscar]

**Verification.** The two CMR collection records, the collection
search, the granule searches and the two PO.DAAC collection pages were
read on 2026-09-15, the user guide was read in full the same day, and
the two product DOIs were resolved the same day; every file-level fact
above is from the guide's file-structure tables or the collection
pages' variable tables, and every range and count from the CMR
searches.[^cmr-6hr][^cmr-search][^cmr-granules-6hr][^cmr-granules-monthly][^podaac-6hr][^guide][^doi-6hr][^doi-monthly]
The four papers' registry records were verified on 2026-09-15 (title,
authors, journal, year) and the abstracts of the 2019, 2021 and 2022
papers read there; the 2011 paper's record carries no abstract and no
journal page was read.[^mears-2022][^atlas-2011][^ricciardulli-2021][^manaster-2019]
No granule was opened, so the file attributes beyond the guide's
tables and the pages' variable lists are not stated here.

[^podaac-6hr]: PO.DAAC collection page, CCMP_WINDS_10M6HR_L4_V3.1
[^podaac-monthly]: PO.DAAC collection page, CCMP_WINDS_10MMONTHLY_L4_V3.1
[^cmr-6hr]: CMR collection record, C2916514952-POCLOUD
[^cmr-monthly]: CMR collection record, C2916529935-POCLOUD
[^cmr-search]: CMR collection search, POCLOUD provider, keyword CCMP, 2026-09-15
[^cmr-granules-6hr]: CMR granule search, 6-hourly collection, first and last granule, 2026-09-15
[^cmr-granules-monthly]: CMR granule search, monthly collection, first and last granule, 2026-09-15
[^doi-6hr]: Product DOI 10.5067/CCMP-6HW10M-L4V31, resolved 2026-09-15
[^doi-monthly]: Product DOI 10.5067/CCMP-MW10M-L4V31, resolved 2026-09-15
[^guide]: CCMP Version 3.1 User Guide, Mears and Henze, 15 July 2024
[^mears-2022]: Mears and others, 2022, Remote Sensing, doi:10.3390/rs14174230
[^atlas-2011]: Atlas and others, 2011, Bulletin of the American Meteorological Society, doi:10.1175/2010BAMS2946.1
[^ricciardulli-2021]: Ricciardulli and Manaster, 2021, Remote Sensing, doi:10.3390/rs13183678
[^manaster-2019]: Manaster, Ricciardulli and Meissner, 2019, Journal of Atmospheric and Oceanic Technology, doi:10.1175/jtech-d-18-0116.1
[^oscar]: This bundle's OSCAR dataset concept
