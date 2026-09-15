---
type: connector
title: "GES DISC subsetting and OPeNDAP access to MERRA-2, AIRS and the OCO SIF Lite files: Cloud OPeNDAP by granule URL with a DAP4 constraint, the Harmony enterprise subsetter by collection, bounding box, variables and time, and an Earthdata Login bearer token on every data request; the on-premises subsetter and OPeNDAP servers retire in September 2026"
description: "Three routes take a window of a GES DISC collection off the archive without the whole file. Cloud OPeNDAP at opendap.earthdata.nasa.gov serves each granule under its CMR collection concept id, short name and version, and a DAP4 constraint expression (variables and index ranges, groups preserved) appended as .dap.nc4?dap4.ce= returns a netCDF-4 subset. The Harmony enterprise subsetter at harmony.earthdata.nasa.gov takes a collection, a bounding box or shape, variables and a time range and stages netCDF-4 files or OPeNDAP URLs, with Giovanni time series and averaging services beside it for the gridded collections; it replaces the GES DISC Level 2 subsetter (discontinued no earlier than 15 July 2026) and the Level 3 and 4 regridder and subsetter (no earlier than 15 September 2026), whose JSON-WSP service at disc.gsfc.nasa.gov/service/subset/jsonwsp offered diurnal aggregation and regridding that the replacement does not. Every data request carries an Earthdata Login token in an Authorization Bearer header, after a one-time authorization of the NASA GESDISC DATA ARCHIVE application (Hyrax in the Cloud for OPeNDAP) on the account; CMR search needs no credential. What leaves the machine is the token, the collection and granule identifiers, variable names, index ranges or a bounding box and a time range; no local data does. The on-premises hosts under gesdisc.eosdis.nasa.gov, which still serve metadata without a credential, lose public access between 7 and 30 September 2026, and directory listings are replaced by CMR granule queries."
tags: [connector, gesdisc, opendap, dap4, cloud-opendap, harmony, subsetter, earthdata-login, bearer-token, merra-2, airs, oco-2, sif, cmr]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T18:45:00Z }
status: draft
citation:
  access_date_required: true
  authority: https://disc.gsfc.nasa.gov/
  data: "the dataset concept's citation, by collection DOI, with the retrieval date; the service is not the thing cited"
  note: "an access date is integral because the MERRA-2 collections carry reprocessed months, the OCO-3 record was withdrawn and reprocessed for February to June 2025, and the routes themselves change in September 2026"
stale_after: 2026-12-15
sources:
  - id: opendap-cloud-doc
    resource: https://disc.gsfc.nasa.gov/information/howto?title=OPeNDAP%20In%20The%20Cloud
    title: "GES DISC, OPeNDAP In The Cloud (last published 2026-04-01; read 2026-09-15 through the site's content API, the page itself being script-rendered: the Cloud OPeNDAP URL structure of collection concept id plus short name and version, the DAP4 constraint form .dap.nc4?dap4.ce=/T2M;/T2MDEW against the on-premises ?T2M,T2MDEW, the DAP2 flattening of group names with underscores against DAP4's preserved paths, the OCO2_L2_Lite_FP example of flattened names, the absence of directory catalogs in the cloud, the DMR++ sidecar, the .dmr.html and .dmr.xml request forms, and the 400 error on a netCDF-3 encoding of a file with UInt64 or grouped content)"
  - id: howto-wget-curl
    resource: https://disc.gsfc.nasa.gov/information/howto?title=How%20to%20Access%20GES%20DISC%20Data%20Using%20wget%20and%20curl
    title: "GES DISC, How to Access GES DISC Data Using wget and curl (last published 2026-08-26; read 2026-09-15 through the content API: the Authorization Bearer token header on every download, --content-disposition for Cloud OPeNDAP subset URLs, URL lists in a text file from the enterprise subsetting services, and the statement that directory wildcards on the file servers are no longer supported)"
  - id: howto-l34
    resource: https://disc.gsfc.nasa.gov/information/howto?title=How%20to%20use%20the%20Level%203%20and%204%20Subsetter%20and%20Regridder
    title: "GES DISC, How to use the Level 3 and 4 Subsetter and Regridder (last published 2026-04-29; read 2026-09-15 through the content API: the Subset / Get Data dialog on a MERRA-2 landing page, the date range, region, variables, time-of-day range with a mean, minimum or maximum statistic, the remapping type and target grid, the output format, and the download links list for wget or curl)"
  - id: howto-l2-enterprise
    resource: https://disc.gsfc.nasa.gov/information/howto?title=How%20to%20Subset%20Level%202%20Data%20with%20the%20Earthdata%20Enterprise%20Subsetter
    title: "GES DISC, How to Subset Level 2 Data with the Earthdata Enterprise Subsetter (last published 2026-07-24; read 2026-09-15 through the content API: the Data Access dialog requiring an Earthdata Login, Get Original Files against Transform Data, the M2T1NXSLV service list of staged netCDF, OPeNDAP URL, Giovanni point and area time series and time-averaged GeoTIFF, the results as a file list, a Python script using harmony and earthaccess, and the Harmony job JSON naming failed granules)"
  - id: doc-l2-replaced
    resource: https://disc.gsfc.nasa.gov/information/documents?title=GES%20DISC%20Level%202%20Subsetter%20Replaced%20with%20Enterprise%20Level%202%20Subsetter
    title: "GES DISC, GES DISC Level 2 Subsetter Replaced with Enterprise Level 2 Subsetter (last published 2026-03-31; read 2026-09-15 through the content API: bounding box, point-radius, shape or polygon, variables, index variables and temporal subsetting supported; subset by dimension, recurring time of day and vector output no longer supported; access through the landing page dialog, the Harmony API with harmony-py or OGC URLs, and Earthdata Search, all requiring an Earthdata Login)"
  - id: alert-l34rs
    resource: https://disc.gsfc.nasa.gov/information/alerts?title=The%20GES%20DISC%20Level%203%20and%204%20Regridder%20and%20Subsetter%20Service%20(L34RS)%20will%20be%20discontinued%20no%20earlier%20than%20September%2015%2C%202026
    title: "GES DISC alert of 25 August 2026 (read 2026-09-15 through the alerts feed: the Level 3 and 4 Regridder and Subsetter Service will be discontinued no earlier than 15 September 2026, its data available through https and the enterprise subsetting services)"
  - id: alert-l2s
    resource: https://disc.gsfc.nasa.gov/information/alerts?title=The%20GES%20DISC%20Level%202%20Subsetting%20Service%20(L2S)%20will%20be%20discontinued%20no%20earlier%20than%20July%2015%2C%202026
    title: "GES DISC alert of 2 July 2026 (read 2026-09-15: the Level 2 Subsetter will be discontinued no earlier than 15 July 2026; a sibling alert the same day retires the SUBSET_AIRS_L1L2 service no earlier than 31 July 2026 in favour of Cloud OPeNDAP)"
  - id: alert-opendap
    resource: https://disc.gsfc.nasa.gov/information/alerts?title=OPeNDAP%20Retirement%20Notice
    title: "GES DISC alert of 23 July 2026 (read 2026-09-15: all on-premises OPeNDAP services are turned off between 7 August and 30 September 2026; Cloud OPeNDAP URLs are organised by CMR collection concept id, short name and version rather than by the local directory tree)"
  - id: alert-migration-207
    resource: https://disc.gsfc.nasa.gov/information/alerts?title=Migration%20of%20OPeNDAP%20services%20to%20Earthdata%20cloud%20for%20207%20collections
    title: "GES DISC alert of 25 June 2026 (read 2026-09-15: the cloud OPeNDAP migration of 207 collections between 25 June and 15 July 2026, the list naming the AIRS level 3 daily and monthly collections AIRS3SPD and AIRS3SPM at version 7.0, AIRX3STD and OMTO3d and OMTO3e at version 004 among others; earlier alerts of March 2024 and April 2025 record M2T1NXSLV and 53 further MERRA-2 collections moving to Cloud OPeNDAP)"
  - id: alert-servers
    resource: https://disc.gsfc.nasa.gov/information/alerts?title=Retirement%20of%20GES%20DISC%20Data%20Servers%20by%20September%2030%2C%202026
    title: "GES DISC alert of 14 September 2026 (read 2026-09-15: HTTPS access to the on-premises servers under gesdisc.eosdis.nasa.gov ends by 30 September 2026 in phases; data remain free from data.gesdisc.earthdata.nasa.gov; recursive directory download is not available there and granule URL lists come from CMR queries; the GrADS Data Server was discontinued in May 2026 and the THREDDS server no earlier than 31 July 2026 by sibling alerts)"
  - id: jsonwsp
    resource: https://disc.gsfc.nasa.gov/service/subset/jsonwsp/description
    title: "The GES DISC UUI subsetting service, JSON-WSP description (read 2026-09-15: methods subset, GetStatus, GetResult and Dismiss; subset parameters box, lat, lon, radius, start, end, data with datasetId, variable and dimension slices, diurnalFrom, diurnalTo, diurnalAggregation, grid, mapping, presentation, format, crop, agent, url and role; results as job status and a paged list of links with s3url and polygons)"
  - id: howto-prereq
    resource: https://disc.gsfc.nasa.gov/information/howto?title=How%20to%20Generate%20Earthdata%20Prerequisite%20Files
    title: "GES DISC, How to Generate Earthdata Prerequisite Files (last published 2024-09-24; read 2026-09-15: the .netrc, .urs_cookies and .dodsrc files for the on-premises routes, updated to use earthaccess and a generated token)"
  - id: howto-resolve
    resource: https://disc.gsfc.nasa.gov/information/howto?title=How%20To%20resolve%20data%20download%20problems
    title: "GES DISC, How To resolve data download problems (last published 2026-04-23; read 2026-09-15: a failed download is resolved by enabling the NASA GESDISC DATA ARCHIVE application, or Hyrax in the Cloud for OPeNDAP, under Authorized Apps at urs.earthdata.nasa.gov, and by wget 1.18 or curl 7.45 or later)"
  - id: doc-register
    resource: https://disc.gsfc.nasa.gov/information/documents?title=How%20to%20register%20for%20an%20Earthdata%20Login%20and%20obtain%20access%20to%20NASA%20GES%20DISC%20data
    title: "GES DISC, How to register for an Earthdata Login and obtain access to NASA GES DISC data (last published 2025-08-21; read 2026-09-15: the registration, the Approve More Applications step for NASA GESDISC DATA ARCHIVE, and the end-user licence agreements)"
  - id: glossary-token
    resource: https://disc.gsfc.nasa.gov/information/glossary?title=Token%20authentication
    title: "GES DISC glossary, Token authentication and Harmony (read 2026-09-15: a token obtained with the Earthdata username and password gives one hour of S3 bucket credentials, regenerable; Harmony is the EOSDIS service merging the DAACs' on-premises subsetters into one cloud service)"
  - id: howto-data-access
    resource: https://disc.gsfc.nasa.gov/information/howto?keywords=data%20access&title=Data%20Access
    title: "GES DISC, Data Access (last published 2026-04-29; read 2026-09-15: the tools and services list, Harmony as the subsetting API across DAACs, Cloud OPeNDAP as the GES DISC-managed URL subsetting service, the Giovanni time series API, and CMR as the discovery API behind Earthdata Search)"
  - id: faq-opendap-url
    resource: https://disc.gsfc.nasa.gov/information/faqs?title=How%20can%20I%20access%20GES%20DISC%20data%20using%20OPeNDAP%20URLs%3F
    title: "GES DISC FAQ, How can I access GES DISC data using OPeNDAP URLs, and the 2021 FAQ on subsetting a large amount of MERRA-2 data (read 2026-09-15: the on-premises URL convention server/path/file.format?subset with .ascii, .nc, .nc4 or .dods, and the older route of OPeNDAP subsets against the GES DISC Subsetter with daily statistics and regridding)"
  - id: cmr-services
    resource: https://cmr.earthdata.nasa.gov/search/services.umm_json?concept_id=S2874702816-XYZ_PROV
    title: "CMR service records associated with M2T1NXSLV 5.12.4, AIRS3STD 7.0 and the OCO-2 and OCO-3 Lite SIF collections (read 2026-09-15: the Hyrax OPeNDAP service S2874702816 on all four; on the gridded MERRA-2 and AIRS collections the Harmony OPeNDAP SubSetter with MaskFill S2164732315 (variables, bounding box, GeoJSON shape, temporal, netCDF-4), the Harmony OPeNDAP URL Service S4057306097 returning an OPeNDAP URL instead of a file, the Cloud Giovanni time series S2739607260 (point, up to 100000 granules, CSV) and averaging S3385907677 (bounding box, CSV or GeoTIFF); on the SIF Lite collections the level 2 Harmony subsetter S1962070864 (variables, bounding box, ESRI, KML or GeoJSON shapes, temporal, netCDF-4))"
  - id: cmr-granule
    resource: https://cmr.earthdata.nasa.gov/search/granules.json?collection_concept_id=C2912084771-GES_DISC&sort_key=start_date&page_size=2
    title: "CMR granule record of the OCO-2 Lite SIF granule of 2024-04-02 (read 2026-09-15: the archive URL on data.gesdisc.earthdata.nasa.gov, the S3 URL and DMR++ sidecar, the s3credentials endpoint, the Cloud OPeNDAP service URL under collections/C2912084771-GES_DISC/granules/, and the on-premises data tree URL)"
  - id: probe-cloud
    resource: https://opendap.earthdata.nasa.gov/collections/C2912084771-GES_DISC/granules/OCO2_L2_Lite_SIF.11.2r%3Aoco2_LtSIF_240402_B11217Ar_241023161757s.nc4.dmr.xml
    title: "Cloud OPeNDAP DAP4 metadata request for the 2024-04-02 OCO-2 SIF granule, probed 2026-09-15 with no credential: HTTP 302 to https://opendap.earthdata.nasa.gov/login/urs, no metadata returned"
  - id: probe-onprem
    resource: https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L2_Lite_SIF.11.2r/2024/oco2_LtSIF_240402_B11217Ar_241023161757s.nc4.dmr
    title: "On-premises Hyrax 1.17.1 DAP4 metadata for the same granule, probed 2026-09-15 with no credential: HTTP 200, the DMR with group names flattened to underscores (Science_daily_correction_factor, Meteo_surface_pressure), and the collection's contents page listing year directories and a doc directory"
  - id: merra2
    resource: ../datasets/merra-2.md
    title: "This bundle's MERRA-2 dataset concept: the collections, their concept ids, and their access paragraph naming Cloud OPeNDAP and the GES DISC subsetter"
  - id: airs
    resource: ../datasets/airs-l3-temperature-humidity.md
    title: "This bundle's AIRS version 7 level 3 dataset concept, whose collections the subsetter and OPeNDAP serve"
  - id: omi
    resource: ../datasets/omi-no2-and-ozone.md
    title: "This bundle's OMI level 3 dataset concept, whose OMTO3d and OMTO3e collections are in the July 2026 Cloud OPeNDAP migration list"
  - id: sif
    resource: ../datasets/oco2-sif-lite.md
    title: "This bundle's OCO-2 and OCO-3 SIF Lite dataset concept, the level 2 sounding files the level 2 Harmony subsetter and Cloud OPeNDAP serve"
---

# GES DISC subsetter and OPeNDAP

The archive of MERRA-2, AIRS, OMI and the OCO Lite files is reached
for a window, rather than a whole file, by three routes: Cloud
OPeNDAP, the Harmony enterprise subsetter, and, until September
2026, the GES DISC's own on-premises subsetter and OPeNDAP servers.
This concept names what each does, the shape of a request, what
leaves the machine, the credential, and how each fails; the
hydrology plugin's connector concept for GES DISC through
earthaccess (knowledge/connectors/gesdisc-earthaccess.md in that
plugin) records the IMERG and NLDAS-2 pulls over the same Cloud
OPeNDAP route and the three failure shapes of an unauthorised
account, and is not restated here.[^howto-data-access]

**What the services are.** Cloud OPeNDAP is the Hyrax server at
opendap.earthdata.nasa.gov, one endpoint for every DAAC's
OPeNDAP-enabled granules, which serves a granule's metadata and any
subset of its variables and index ranges by URL; it is associated in
CMR with every collection this bundle covers, and the MERRA-2 hourly
single-level collection moved to it in March 2024, 53 more MERRA-2
collections in April 2025, and 207 further collections including the
AIRS level 3 daily and monthly grids and the OMI OMTO3d and OMTO3e
grids between 25 June and 15 July 2026.[^opendap-cloud-doc][^cmr-services][^alert-migration-207]
The enterprise subsetter is Harmony, the EOSDIS service at
harmony.earthdata.nasa.gov that merged the DAACs' subsetters into one
cloud service; on the gridded MERRA-2 and AIRS collections it runs
the Harmony OPeNDAP SubSetter with MaskFill (variables, a bounding
box or GeoJSON shape and a time range, netCDF-4 out), a variant that
returns an OPeNDAP URL instead of a staged file, and the Cloud
Giovanni time series (a point, CSV out, up to 100000 granules) and
area-averaging services (a bounding box, CSV or GeoTIFF out); on the
OCO SIF Lite files, which are level 2 sounding lists, it runs the
level 2 subsetter (variables, a bounding box or an ESRI, KML or
GeoJSON shape, a time range, netCDF-4 out).[^glossary-token][^cmr-services][^howto-l2-enterprise]
The GES DISC's own services are retiring: the Level 2 Subsetter is
discontinued no earlier than 15 July 2026, the AIRS level 1 and 2
channel subsetter no earlier than 31 July 2026, the Level 3 and 4
Regridder and Subsetter no earlier than 15 September 2026, the
GrADS Data Server was discontinued in May 2026 and the THREDDS server
no earlier than 31 July 2026, and all on-premises OPeNDAP services
are turned off between 7 August and 30 September 2026, with HTTPS
access to the on-premises hosts under gesdisc.eosdis.nasa.gov ending
by 30 September 2026.[^alert-l2s][^alert-l34rs][^alert-opendap][^alert-servers]
The retired Level 3 and 4 service is the one the MERRA-2 how-tos and
FAQ describe: a date range, a region, variables, a time-of-day range
within the day with a mean, minimum or maximum statistic, a
remapping type and target grid, and an output format, returning a
list of staged files; the enterprise replacement supports a bounding
box, point-radius, shape, variables, index variables and temporal
subsetting, and no longer supports subsetting by dimension, by
recurring time of day, or vector output, so a daily mean of an hourly
MERRA-2 collection or a regrid is no longer a service and is done
after the pull.[^howto-l34][^faq-opendap-url][^doc-l2-replaced]

**The request shape.** A Cloud OPeNDAP granule URL is built from
the CMR collection concept id, the short name and version, and the
file name, as the granule record's service link gives it:
`https://opendap.earthdata.nasa.gov/collections/C2912084771-GES_DISC/granules/OCO2_L2_Lite_SIF.11.2r:oco2_LtSIF_240402_B11217Ar_241023161757s.nc4`,
and for MERRA-2
`.../collections/C1276812863-GES_DISC/granules/M2T1NXSLV.5.12.4:MERRA2_100.tavg1_2d_slv_Nx.19800101.nc4`;
appending `.dmr.xml` or `.dmr.html` returns the DAP4 metadata or
request form, and appending `.dap.nc4?dap4.ce=/T2M;/T2MDEW` returns a
netCDF-4 file of the named variables, with index ranges in square
brackets on each variable for a window and with group paths kept,
so a Lite SIF variable is `/Science/daily_correction_factor` under
DAP4 where the on-premises DAP2 server flattened it to
`Science_daily_correction_factor`.[^opendap-cloud-doc][^cmr-granule][^probe-onprem]
There is no directory to browse in the cloud: the granule names come
from a CMR granule search by collection concept id and temporal
range, or from the CMR virtual directory, which the GES DISC
landing-page subsetter also uses to emit a list of Cloud OPeNDAP
subset URLs for a date range and variables.[^opendap-cloud-doc][^alert-servers]
A Harmony request names the collection, a bounding box or shape,
the variables and a time range, through the landing page's Data
Access dialog, through harmony-py, or as an OGC coverages URL; the
result is a job whose JSON lists each granule's request and any
failure, and whose output is a file list for wget or curl, a Python
script using harmony and earthaccess, or staged files.[^howto-l2-enterprise][^doc-l2-replaced]
The retiring GES DISC subsetter is a JSON-WSP service at
`https://disc.gsfc.nasa.gov/service/subset/jsonwsp` whose subset
method takes a box (west, south, east, north), or a lat, lon and
radius, a start and end in RFC 3339, a data list of dataset id,
variable and dimension slices, and the diurnal, grid, mapping,
presentation, format and crop options, and whose GetStatus and
GetResult methods poll a job id and page through the resulting
links; its description document still answers, and the service is
discontinued no earlier than 15 September 2026.[^jsonwsp][^alert-l34rs]
The on-premises OPeNDAP form, `server/path/file.nc4?VAR1,VAR2` with
`.ascii`, `.nc`, `.nc4` or `.dods` encodings, is the one the older
how-tos and scripts use and the one that stops answering by 30
September 2026.[^faq-opendap-url][^alert-opendap]

**The token, and what leaves the machine.** Every data request to
the cloud hosts carries an Earthdata Login token in the header
`Authorization: Bearer <token>` (wget and curl how-tos), generated on
the Earthdata Login site; the account must have authorised the NASA
GESDISC DATA ARCHIVE application, and Hyrax in the Cloud for
OPeNDAP, under Authorized Apps, a one-time step only the account
holder can take, and the older `.netrc`, `.urs_cookies` and `.dodsrc`
files serve the on-premises routes and DAP clients.[^howto-wget-curl][^howto-resolve][^doc-register][^howto-prereq]
A token exchanged at the s3credentials endpoint gives one hour of
direct S3 read access, regenerable, for work inside the same cloud
region.[^glossary-token][^cmr-granule] What goes to
opendap.earthdata.nasa.gov, harmony.earthdata.nasa.gov and
data.gesdisc.earthdata.nasa.gov is therefore the token, the
collection concept id and granule names, the variable names, and
either index ranges or a bounding box, shape and time range, which
disclose the window of interest and nothing else; what goes to
cmr.earthdata.nasa.gov is the short name or concept id and the
temporal and spatial bounds, with no credential; no file, path or
data held locally goes to any of them, and a Harmony job JSON, which
records the request, is readable afterwards by the account that made
it.[^howto-wget-curl][^howto-l2-enterprise][^howto-data-access]
The token is never part of a URL, a log or a committed file; it is
a header.[^howto-wget-curl]

**The failure modes.** Without a token, Cloud OPeNDAP answers a
metadata request with an HTTP 302 to its Earthdata Login page, as
probed on 15 September 2026 for the OCO-2 SIF granule of 2 April
2024, while the on-premises Hyrax server returned the same granule's
DAP4 metadata with a 200 and no credential; without the application
authorisation, a download fails and the how-to's remedy is the
Authorized Apps step.[^probe-cloud][^probe-onprem][^howto-resolve] A
request for a netCDF-3 encoding of a file holding UInt64 variables
or groups, which the OCO Lite files do (sounding_id is UInt64),
returns a 400 error and the remedy is the netCDF-4 encoding; a DAP2
request to a grouped file returns flattened names.[^opendap-cloud-doc]
A wget or curl over a directory wildcard on the archive host is not
supported, and a script that builds URLs from the on-premises
directory tree, or calls the JSON-WSP subsetter, stops working as
each host is turned off between August and September
2026.[^howto-wget-curl][^alert-servers][^alert-l34rs] A Harmony job
that fails for some granules records them in its job JSON and
delivers the rest, so a file list shorter than the granule count is
read against the job rather than taken as the archive's
coverage.[^howto-l2-enterprise] A Cloud OPeNDAP subset URL fetched
without `--content-disposition` lands under the encoded URL as its
file name.[^howto-wget-curl]

**The collections this bundle covers.** MERRA-2
([merra-2](../datasets/merra-2.md)) is served by every route above,
and its access paragraph names Cloud OPeNDAP and the subsetter; the
AIRS version 7 level 3 grids
([airs-l3-temperature-humidity](../datasets/airs-l3-temperature-humidity.md))
and the OMI OMTO3d and OMTO3e grids
([omi-no2-and-ozone](../datasets/omi-no2-and-ozone.md)) moved to
Cloud OPeNDAP in the June and July 2026 migration; and the OCO-2 and
OCO-3 SIF Lite files ([oco2-sif-lite](../datasets/oco2-sif-lite.md))
are level 2 sounding lists, subset by the level 2 Harmony service
by bounding box, shape and variables, or by index range over
sounding_dim through OPeNDAP, where a spatial window is not an index
range and a bounding box is the useful
constraint.[^merra2][^airs][^omi][^sif][^cmr-services][^alert-migration-207]

[^opendap-cloud-doc]: GES DISC, OPeNDAP In The Cloud, read 2026-09-15
[^howto-wget-curl]: GES DISC, How to Access GES DISC Data Using wget and curl, read 2026-09-15
[^howto-l34]: GES DISC, How to use the Level 3 and 4 Subsetter and Regridder, read 2026-09-15
[^howto-l2-enterprise]: GES DISC, How to Subset Level 2 Data with the Earthdata Enterprise Subsetter, read 2026-09-15
[^doc-l2-replaced]: GES DISC, Level 2 Subsetter Replaced with Enterprise Level 2 Subsetter, read 2026-09-15
[^alert-l34rs]: GES DISC alert, Level 3 and 4 Regridder and Subsetter discontinued no earlier than 2026-09-15
[^alert-l2s]: GES DISC alert, Level 2 Subsetting Service discontinued no earlier than 2026-07-15
[^alert-opendap]: GES DISC alert, OPeNDAP Retirement Notice, July 2026
[^alert-migration-207]: GES DISC alert, migration of OPeNDAP services to the Earthdata cloud for 207 collections, June 2026
[^alert-servers]: GES DISC alert, retirement of GES DISC data servers by 2026-09-30
[^jsonwsp]: GES DISC UUI subsetting service, JSON-WSP description, read 2026-09-15
[^howto-prereq]: GES DISC, How to Generate Earthdata Prerequisite Files, read 2026-09-15
[^howto-resolve]: GES DISC, How To resolve data download problems, read 2026-09-15
[^doc-register]: GES DISC, How to register for an Earthdata Login and obtain access to NASA GES DISC data, read 2026-09-15
[^glossary-token]: GES DISC glossary, Token authentication and Harmony, read 2026-09-15
[^howto-data-access]: GES DISC, Data Access, read 2026-09-15
[^faq-opendap-url]: GES DISC FAQ on OPeNDAP URLs and on subsetting MERRA-2, read 2026-09-15
[^cmr-services]: CMR service records associated with the MERRA-2, AIRS and SIF collections, read 2026-09-15
[^cmr-granule]: CMR granule record of the OCO-2 Lite SIF granule of 2024-04-02, read 2026-09-15
[^probe-cloud]: Cloud OPeNDAP metadata probe without a credential, 2026-09-15
[^probe-onprem]: On-premises OPeNDAP metadata probe without a credential, 2026-09-15
[^merra2]: This bundle's MERRA-2 dataset concept
[^airs]: This bundle's AIRS level 3 dataset concept
[^omi]: This bundle's OMI level 3 dataset concept
[^sif]: This bundle's OCO-2 and OCO-3 SIF Lite dataset concept
