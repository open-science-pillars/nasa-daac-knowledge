---
type: dataset
spheres: [atmosphere, hydrosphere]
title: "MERRA-2: the GMAO atmospheric reanalysis, 1980 onward, as the file collections a user meets at GES DISC"
description: "The Modern-Era Retrospective analysis for Research and Applications, version 2, produced by the Global Modeling and Assimilation Office with GEOS-5 version 5.12.4 and archived at GES DISC as about a hundred file collections on one 0.625 by 0.5 degree grid: hourly, three-hourly, daily-statistic, monthly and monthly-diurnal, instantaneous or time-averaged, each with its own short name, DOI and CMR concept id. No error fields ship; what stands in is the analysis increment, the documented observing-system epochs and the four production streams."
tags: [merra-2, merra2, reanalysis, gmao, gesdisc, atmosphere, precipitation, m2t1nxslv, m2t1nxflx, m2tmnxslv]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:30:00Z }
resource: https://disc.gsfc.nasa.gov/datasets/M2T1NXSLV_5.12.4/summary
version: "GEOS-5 version 5.12.4 is the assimilation system and the collection version of every MERRA-2 collection; concept ids CMR-verified 2026-09-14, DOIs read from the GMAO citing page the same day: M2T1NXSLV C1276812863-GES_DISC (DOI 10.5067/VJAFPLI1CSIV), M2T1NXFLX C1276812838-GES_DISC (10.5067/7MCPBJ41Y0K6), M2TMNXSLV C1276812859-GES_DISC (10.5067/AP1B0BA5PD2K), M2TMNXFLX C1276812868-GES_DISC, M2I1NXASM C1276812820-GES_DISC (10.5067/3Z173KIE2TPD), M2IMNXASM C1276812823-GES_DISC, M2T1NXINT C1276812846-GES_DISC, M2T1NXLND C1276812861-GES_DISC, M2TMNXLND C1276812856-GES_DISC, M2SDNXSLV C1276812843-GES_DISC, M2TUNXSLV C1276812878-GES_DISC, M2I3NPASM C1276812879-GES_DISC, M2IMNPASM C1276812904-GES_DISC, M2T3NVASM C1276812925-GES_DISC; every record begins 1980-01-01 with the ends-at-present flag, and the newest M2T1NXSLV granule that day covered 2026-08-01"
sources:
  - id: cmr-merra2
    resource: https://cmr.earthdata.nasa.gov/search/collections.json?short_name=M2T1NXSLV&provider=GES_DISC
    title: "CMR collection search by short name (read 2026-09-14 for M2T1NXSLV and seventeen sibling short names: the concept id, version, DOI, temporal extent, abstract and related URLs of each; the same day the granule search gave the first and newest M2T1NXSLV granules and the stream prefix on the granules at the stream boundaries)"
  - id: gesdisc-m2t1nxslv
    resource: https://disc.gsfc.nasa.gov/datasets/M2T1NXSLV_5.12.4/summary
    title: "GES DISC collection page for M2T1NXSLV 5.12.4 (fetched 2026-09-14; the page is rendered by script, so its text was read from the CMR record it is built from, which carries the abstract, the time-stamp sentence and the document links)"
  - id: gesdisc-m2t1nxflx
    resource: https://disc.gsfc.nasa.gov/datasets/M2T1NXFLX_5.12.4/summary
    title: "GES DISC collection page for M2T1NXFLX 5.12.4 (fetched 2026-09-14, text read from its CMR record: the surface flux collection with total and bias-corrected precipitation, the model surface layer at about 60 m, the 00:30 time stamp)"
  - id: gesdisc-m2tmnxslv
    resource: https://disc.gsfc.nasa.gov/datasets/M2TMNXSLV_5.12.4/summary
    title: "GES DISC collection page for M2TMNXSLV 5.12.4 (fetched 2026-09-14, text read from its CMR record: the monthly time-averaged single-level diagnostics, with variances of certain parameters, and the roughly three-week latency after the end of a month)"
  - id: gesdisc-m2i1nxasm
    resource: https://disc.gsfc.nasa.gov/datasets/M2I1NXASM_5.12.4/summary
    title: "GES DISC collection page for M2I1NXASM 5.12.4 (fetched 2026-09-14, text read from its CMR record: the hourly instantaneous single-level diagnostics stamped on the hour from 00:00 UTC)"
  - id: filespec
    resource: https://gmao.gsfc.nasa.gov/media/publications/zbly36ziNFDFbmYmvhQeVqPhUo/Bosilovich785.pdf
    title: "Bosilovich, Lucchesi and Suarez, 2016, MERRA-2: File Specification, GMAO Office Note No. 9 (version 1.1, 21 March 2016), read in full 2026-09-14: the grid, the time stamping, the file naming and stream convention, the ESDT short-name rule, every collection's variable table (the FLX table with PRECTOT and PRECTOTCORR, the LFO table with PRECCUCORR, PRECLSCORR and PRECSNOCORR), the budget equations and the precipitation correction note"
  - id: readme
    resource: https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T1NXSLV.5.12.4/doc/MERRA2.README.pdf
    title: "GES DISC README Document for MERRA-2 Data Products (last revised 1 March 2021), read 2026-09-14: the introduction, the collection tables with their frequency lines, the DOI tables and the reference list"
  - id: reproc
    resource: https://docserver.gesdisc.eosdis.nasa.gov/public/project/MERRA/Records_MERRA-2_Data_Reprocessing_and_Service_Changes.pdf
    title: "GES DISC, Records of MERRA-2 Data Reprocessing and Service Changes, read 2026-09-14: the reprocessed periods and their MERRA2_401 prefix, the service changes through April 2026 and the observing-system alert of June 2025"
  - id: gmao-doc
    resource: https://gmao.gsfc.nasa.gov/gmao-products/merra-2/documentation_merra-2/
    title: "GMAO MERRA-2 documentation page, read 2026-09-14: the links to the file specification, the technical memoranda and the journal collection"
  - id: gmao-citing
    resource: https://gmao.gsfc.nasa.gov/gmao-products/merra-2/citing-merra-2-data_merra-2/
    title: "GMAO, Citing MERRA-2 Data, read 2026-09-14: one DOI per file collection, in the hourly, monthly and monthly-diurnal tables"
  - id: gmao-faq
    resource: https://gmao.gsfc.nasa.gov/gmao-products/merra-2/faq_merra-2/
    title: "GMAO MERRA-2 FAQ, read 2026-09-14: the land collection as land-only values against the grid-box averages of the other collections, the monthly release timing, the undefined below-ground pressure-level points and the soil moisture and snow conventions"
  - id: gelaro-2017
    resource: https://doi.org/10.1175/JCLI-D-16-0758.1
    title: "Gelaro and others, 2017, The Modern-Era Retrospective Analysis for Research and Applications, Version 2 (MERRA-2), Journal of Climate 30, 5419 to 5454 (the overview paper; record and abstract read on the Crossref registry 2026-09-14, the journal page sits behind a bot check)"
  - id: bosilovich-2015
    resource: https://gmao.gsfc.nasa.gov/pubs/docs/Bosilovich803.pdf
    title: "Bosilovich and others, 2015, MERRA-2: Initial Evaluation of the Climate, NASA Technical Report Series on Global Modeling and Data Assimilation volume 43, read 2026-09-14 in the sections on the precipitation correction, the streams and land spin-up, the global constraints, the water cycle and the observing-system effects"
  - id: mccarty-2016
    resource: https://gmao.gsfc.nasa.gov/pubs/docs/McCarty885.pdf
    title: "McCarty and others, 2016, MERRA-2 Input Observations: Summary and Assessment, NASA Technical Report Series on Global Modeling and Data Assimilation volume 46, read 2026-09-14: Table 1, the observation types with their dates of use"
  - id: reichle-liu-2014
    resource: https://gmao.gsfc.nasa.gov/pubs/docs/Reichle734.pdf
    title: "Reichle and Liu, 2014, Observation-Corrected Precipitation Estimates in GEOS-5, NASA Technical Report Series on Global Modeling and Data Assimilation volume 35, read 2026-09-14: the correction method, the tapering and Africa options and the MERRA-2 rows of Table 3"
  - id: reichle-2017
    resource: https://doi.org/10.1175/JCLI-D-16-0570.1
    title: "Reichle, Liu, Koster, Draper, Mahanama and Partyka, 2017, Land Surface Precipitation in MERRA-2, Journal of Climate 30, 1643 to 1664 (record and abstract read on the Crossref registry 2026-09-14; the journal page sits behind a bot check)"
  - id: reichle-2017b
    resource: https://doi.org/10.1175/JCLI-D-16-0720.1
    title: "Reichle, Draper, Liu, Girotto, Mahanama, Koster and De Lannoy, 2017, Assessment of MERRA-2 Land Surface Hydrology Estimates, Journal of Climate 30, 2937 to 2960 (record and abstract read on the Crossref registry 2026-09-14: the GRACE terrestrial water storage comparison that reflects known errors in the correcting observations; the journal page sits behind a bot check)"
  - id: bosilovich-2017
    resource: https://doi.org/10.1175/JCLI-D-16-0338.1
    title: "Bosilovich, Robertson, Takacs, Molod and Mocko, 2017, Atmospheric Water Balance and Variability in the MERRA-2 Reanalysis, Journal of Climate 30, 1177 to 1196 (record and abstract read on the Crossref registry 2026-09-14; the journal page sits behind a bot check)"
status: draft
stale_after: 2027-03-14
---

# MERRA-2

**Identity.** MERRA-2 is NASA's global atmospheric reanalysis of the
satellite era, produced by the Global Modeling and Assimilation
Office (GMAO) with the Goddard Earth Observing System model and
analysis, version 5.12.4, from January 1980 to within a few weeks of
the present; it replaces MERRA, whose assimilation system was frozen
in 2008 and could not ingest the newer sounders.[^gelaro-2017][^readme]
Production began in June 2014 in four processing streams and
converged to one near-real-time stream in mid 2015; each new month is
released to GES DISC after quality checking, about three weeks after
the month ends.[^gelaro-2017][^gmao-faq][^gesdisc-m2tmnxslv] The
archive at GES DISC is the reanalysis as a user meets it: about a
hundred file collections, each a fixed set of variables at one
frequency, and each with its own nine-character short name, DOI and
CMR concept id.[^gmao-citing][^cmr-merra2] The ones most users
reach first are the hourly single-level diagnostics M2T1NXSLV
(tavg1_2d_slv_Nx: 2 m and 10 m temperature and wind, sea level and
surface pressure, precipitable water), the hourly surface fluxes
M2T1NXFLX (tavg1_2d_flx_Nx: precipitation in its model and
bias-corrected forms, evaporation, the turbulent fluxes, stresses,
boundary layer height), and their monthly means M2TMNXSLV and
M2TMNXFLX; beside them sit the hourly instantaneous states M2I1NXASM
(inst1_2d_asm_Nx) and its monthly mean M2IMNXASM, the vertically
integrated budget terms M2T1NXINT, the land-only diagnostics
M2T1NXLND and M2TMNXLND, the daily statistics M2SDNXSLV (statD_2d_slv_Nx,
the daily maximum, minimum and mean 2 m temperature), the monthly
diurnal means M2TUNXSLV, and the three-dimensional assimilated
fields on 42 pressure levels (M2I3NPASM three-hourly instantaneous,
M2IMNPASM monthly) and on the 72 model layers
(M2T3NVASM).[^gesdisc-m2t1nxslv][^gesdisc-m2t1nxflx][^gesdisc-m2tmnxslv][^gesdisc-m2i1nxasm][^filespec][^cmr-merra2]
The hydrology plugin's own concepts for IMERG version 07
(knowledge/datasets/imerg-v07.md in that plugin) and NLDAS-2 forcing
(knowledge/datasets/nldas2-forcing.md) are the observational
precipitation and the land forcing a MERRA-2 comparison usually
reaches for; they are not restated here.

**Structure.** Every collection is on the same regular
longitude-latitude grid, 576 by 361 points at 0.625 degrees by 0.5
degrees with the origin (index 1, 1) at 180 W, 90 S, interpolated from
the model's native cubed sphere of roughly 50 km; vertical fields
come on 42 pressure levels or the 72 hybrid model layers (73 edges),
indexed top down, with the layer pressures to be taken from the
reported DELP and PTOP rather than reconstructed.[^filespec] Files
are netCDF-4 (classic model, HDF-5 storage), one day per file for the
hourly and three-hourly collections and one month per file for the
monthly ones, named runid.collection.timestamp: the runid MERRA2_SVv
carries the production stream S (1 to 4) and a version Vv that is 00
for the original processing and 01 where a period was reprocessed;
the collection name reads freq_dims_group_HV, and the short name
compresses it as M2 plus a time-description letter (I instantaneous,
T time-averaged, C constant, S statistics), a frequency character (1,
3, 6, M, D, U), N for native horizontal resolution, a vertical letter
(X two-dimensional, P pressure, V model layer, E model edge) and a
three-letter group.[^filespec] Instantaneous collections are stamped
on the hour (00:00, 01:00, and so on); time-averaged collections
carry a continuous sequence of averages stamped at the centre of the
interval, 00:30, 01:30 and so on for hourly data and 01:30, 04:30 and
so on for three-hourly, with the time coordinate in minutes since the
first time in the file and the first time named in the global
attributes.[^filespec][^gesdisc-m2t1nxslv][^gesdisc-m2i1nxasm] The
four streams begin in the files on 1980-01-01 (MERRA2_100),
1992-01-01 (MERRA2_200), 2001-01-01 (MERRA2_300) and 2011-01-01
(MERRA2_400), each after a one-year spin-up from MERRA initial
conditions that is not released; granules for September 2020 and
June through September 2021 carry MERRA2_401 because those periods
were reprocessed (an AIRS data issue, and a warm bias in the
near-surface temperatures).[^filespec][^reproc][^cmr-merra2] Over
land outside the high latitudes the land surface is forced with an
observation-corrected precipitation (the total as PRECTOTCORR in the
FLX collections, and its bias-corrected components, convective
PRECCUCORR, large-scale PRECLSCORR and snowfall PRECSNOCORR, in the
LFO land forcing collections, whose table lists no total), built from
the CPCU daily gauge analysis,
or CMAP over Africa and the oceans, disaggregated to hourly with the
model's own precipitation and tapered to pure model precipitation
between 42.5 and 62.5 degrees of latitude; the atmosphere's own
precipitation stays in PRECTOT.[^filespec][^reichle-liu-2014][^reichle-2017]
The land collections (LND) hold values per unit land area from the
land model alone, while FLX, RAD and the rest are grid-box averages
over all surface tiles weighted by their fractions.[^gmao-faq]

**Access.** Each collection is one CMR collection under the GES_DISC
provider, searchable by short name and served through Earthdata
Search, the GES DISC data tree, OPeNDAP (Cloud OPeNDAP for the
collections migrated since 2023) and the GES DISC subsetter; the GrADS
Data Server was discontinued in April 2026 and the older subsetting
interfaces before it.[^cmr-merra2][^reproc] Citation is per
collection by its DOI, in the form the GMAO and README pages
give.[^gmao-citing][^readme] The GMAO documentation page is the
index to the file specification and the technical memoranda the
concepts of this bundle rest on.[^gmao-doc]

## Uncertainty

- **No error field ships with any MERRA-2 collection.** A reanalysis
  is a model integration corrected toward observations, and its
  products carry the state and its budget terms, not an uncertainty;
  the monthly collections add variances of some variables, which
  describe variability within the month, not error.[^filespec][^gesdisc-m2tmnxslv]
- **What stands in is the analysis increment.** The vertically
  integrated budget collections (INT) carry the increment terms, so
  the water budget closes as storage plus transport divergence equals
  evaporation minus precipitation plus the analysis increment, and
  the size of the increment is the measure of how far the model was
  pulled by the observations; MERRA-2 constrains the global mean of
  the dry-mass and moisture increments so that global precipitation
  balances evaporation on annual scales, which reduces but does not
  remove the local imprint of observing-system changes.[^filespec][^bosilovich-2015][^bosilovich-2017]
- **The observing system is the largest structured error source.**
  The instruments assimilated enter and leave on documented dates
  (SSM/I July 1987 to November 2009, ATOVS microwave from November
  1998, AIRS from September 2002, GPS radio occultation from July
  2004, MLS temperature above 5 hPa from August 2004, IASI from
  September 2008, ATMS from November 2011, CrIS from April 2012), and
  the evaluation documents the imprints that remain: the land water
  vapour increment and precipitation over land step up with AIRS in
  2003, the high-altitude temperatures change character when MLS
  assimilation begins, and the Southern Ocean increment steps between
  1989 and 1992 and again around 2000.[^mccarty-2016][^bosilovich-2015]
  The stream-boundary gotcha below carries the dates.
- **The precipitation correction is an observation product with its
  own errors.** PRECTOTCORR is as good as CPCU and CMAP where they
  apply; against GPCP monthly it beats the model precipitation, its
  diurnal amplitude is better but its phasing less realistic than the
  model's,[^reichle-2017] and the land hydrology evaluation against
  GRACE reflects known errors in the observations used for the
  correction.[^reichle-2017b]
- **Stream spin-up.** High-latitude land moisture and the snow mass
  of the ice sheets carry discontinuities at the stream boundaries,
  because the land restarts came from an offline spin-up forced
  differently; the evaluation bounds the near-surface consequences at
  about 0.5 K in 2 m temperature and 10 W per square metre in daily
  maximum latent heat flux during the overlap years, as upper
  limits.[^bosilovich-2015]
- **Below-ground pressure-level points are undefined**, not
  extrapolated, so an area average on a pressure level that
  intersects terrain is not comparable with reanalyses that
  extrapolate.[^gmao-faq]

## Known issues

- [merra2-prectotcorr-versus-prectot](../gotchas/merra2-prectotcorr-versus-prectot.md):
  PRECTOTCORR is the observation-corrected precipitation the land
  saw and PRECTOT the atmosphere's own; a budget that mixes them
  carries the correction as a residual.
- [merra2-time-stamp-conventions](../gotchas/merra2-time-stamp-conventions.md):
  time-averaged collections are stamped at the half hour and
  instantaneous ones on the hour; a join on the stamp alone is half
  an hour off.
- [merra2-stream-boundaries-and-discontinuities](../gotchas/merra2-stream-boundaries-and-discontinuities.md):
  the four production streams, the reprocessed periods and the
  observing-system epochs with documented imprints.
- [merra2-grid-weights](../gotchas/merra2-grid-weights.md): the
  0.625 by 0.5 degree grid has cells whose area falls with latitude,
  and no area variable ships.
- [merra2-collection-short-names](../gotchas/merra2-collection-short-names.md):
  the short name encodes frequency, time treatment, dimension and
  group; the same variable name lives in several collections with
  different meanings.

[^cmr-merra2]: CMR collection and granule search, GES_DISC provider, read 2026-09-14
[^gesdisc-m2t1nxslv]: GES DISC collection page and CMR record, M2T1NXSLV 5.12.4
[^gesdisc-m2t1nxflx]: GES DISC collection page and CMR record, M2T1NXFLX 5.12.4
[^gesdisc-m2tmnxslv]: GES DISC collection page and CMR record, M2TMNXSLV 5.12.4
[^gesdisc-m2i1nxasm]: GES DISC collection page and CMR record, M2I1NXASM 5.12.4
[^filespec]: Bosilovich, Lucchesi and Suarez, 2016, MERRA-2: File Specification, GMAO Office Note 9, version 1.1
[^readme]: GES DISC README Document for MERRA-2 Data Products, revised 2021-03-01
[^reproc]: GES DISC, Records of MERRA-2 Data Reprocessing and Service Changes
[^gmao-doc]: GMAO MERRA-2 documentation page
[^gmao-citing]: GMAO, Citing MERRA-2 Data: the per-collection DOI tables
[^gmao-faq]: GMAO MERRA-2 FAQ
[^gelaro-2017]: Gelaro and others, 2017, Journal of Climate, doi:10.1175/JCLI-D-16-0758.1
[^bosilovich-2015]: Bosilovich and others, 2015, MERRA-2: Initial Evaluation of the Climate, NASA TM-2015-104606 volume 43
[^mccarty-2016]: McCarty and others, 2016, MERRA-2 Input Observations, NASA TM-2016-104606 volume 46
[^reichle-liu-2014]: Reichle and Liu, 2014, Observation-Corrected Precipitation Estimates in GEOS-5, NASA TM-2014-104606 volume 35
[^reichle-2017]: Reichle and others, 2017, Journal of Climate, doi:10.1175/JCLI-D-16-0570.1
[^reichle-2017b]: Reichle and others, 2017, Journal of Climate, doi:10.1175/JCLI-D-16-0720.1
[^bosilovich-2017]: Bosilovich and others, 2017, Journal of Climate, doi:10.1175/JCLI-D-16-0338.1
