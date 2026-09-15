---
type: dataset
spheres: [geosphere]
title: "NASADEM version 1: SRTM reprocessed with ICESat control and void-filled from ASTER GDEM and ALOS PRISM, on 1 arc second tiles with EGM96 heights"
description: "NASADEM_HGT is the void-filled digital elevation model of the MEaSUREs NASADEM project: the February 2000 Shuttle Radar Topography Mission raw radar data reprocessed with improved phase unwrapping, corrected against ICESat GLAS ground control and modelled ocean topography, converted from WGS84 ellipsoid heights to EGM96 geoid heights, and filled where SRTM is void with an error-suppressed ASTER GDEM built from GDEM3, GDEM2 and ALOS PRISM AW3D30. It is delivered as one degree tiles of 3601 by 3601 integer metres with a companion NUM layer that says where each height came from and an updated SRTM water body mask; the SRTM-only floating-point ellipsoid heights and their precision are a separate collection, NASADEM_SHHP. Coverage is the land between 60 degrees north and 56 degrees south."
tags: [nasadem, nasadem-hgt, nasadem-shhp, srtm, dem, elevation, egm96, measures, lpdaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T13:40:00Z }
resource: https://lpdaac.usgs.gov/products/nasadem_hgtv001/
version: "Product version 001 (DOI 10.5067/MEASURES/NASADEM/NASADEM_HGT.001), CMR collection C2763264762-LPCLOUD (provider LPCLOUD, short name NASADEM_HGT, version 001), verified 2026-09-15: temporal extent 2000-02-11 to 2000-02-21, collection progress COMPLETE, released 2020-02-13, 14,520 granules on the product page that day; the user guide read is version 1.3 of January 2025"
status: draft
stale_after: 2027-03-15
citation:
  access_date_required: true
  authority: https://lpdaac.usgs.gov/
  data: "NASA JPL (2020). NASADEM Merged DEM Global 1 arc second V001 [Dataset]. NASA Land Processes Distributed Active Archive Center, accessed {access_date}, 10.5067/MEASURES/NASADEM/NASADEM_HGT.001"
  doi: "10.5067/MEASURES/NASADEM/NASADEM_HGT.001"
  note: "the citation text is the one the LP DAAC product page renders on 2026-09-15; the CMR record names Sean Buckley as creator and the user guide lists fifteen authors led by Buckley; the product DOI is a DataCite DOI, so the Crossref API returns no record for it and it was verified by its resolution at doi.org"
sources:
  - id: hgt-page
    resource: https://lpdaac.usgs.gov/products/nasadem_hgtv001/
    title: "LP DAAC product page for NASADEM_HGT v001, read 2026-09-15 (the lpdaac.usgs.gov address redirects to the NASA Earthdata data catalog page for C2763264762-LPCLOUD): description, DOI, CMR concept id, temporal and spatial extent, granule count, the layer table (DEM int16 metres, NUM uint8 class, SWB uint8 class), the file name convention, the citation, and the documents it links"
  - id: shhp-page
    resource: https://lpdaac.usgs.gov/products/nasadem_shhpv001/
    title: "LP DAAC product page for NASADEM_SHHP v001, read 2026-09-15 (redirects to the Earthdata catalog page for C2763266322-LPCLOUD): the two layers, HGT_SRTMONLY (HGTS) floating-point metres with fill -32768 and ERR in millimetres with fill 32769, the file name convention and the citation"
  - id: user-guide
    resource: https://lpdaac.usgs.gov/documents/2237/NASADEM_User_Guide_V13.pdf
    title: "NASADEM user guide, version 1.3, January 2025 (Buckley, Agram, Belz, Crippen, Gurrola, Hensley, Kobrick, Lavalle, Martin, Neumann, Nguyen, Rosen, Shimada, Simard, Tung; NASA JPL), read in full 2026-09-15: sections 1 to 3 (products, Table 1 and Table 2), 4.1 (phase unwrapping), 4.2 (height ripple error correction), 4.3 (height precision), 5.1 (ellipsoid to geoid conversion, water masking, unwrapping error removal, void filling, GDEM error masking) and 5.2 (slope and curvature)"
  - id: dem-guide
    resource: https://lpdaac.usgs.gov/documents/642/DEM_Comparison_Guide.pdf
    title: "LP DAAC Digital Elevation Model Product Comparison Guide, read in full 2026-09-15: the specification table (datum WGS84/EGM96 for SRTM and NASADEM, resampling methods, acquisition periods) and the known observations, including the limited NASADEM data around the antimeridian"
  - id: srtm-guide
    resource: https://lpdaac.usgs.gov/documents/179/SRTM_User_Guide_V3.pdf
    title: "SRTM Collection User Guide, revised October 2015, read 2026-09-15 for the tile geometry statement: file name coordinates refer to the centre of the lower left pixel and every edge pixel is centred on a whole-degree line, so 1 arc second tiles have 3,601 lines and samples"
  - id: cmr-hgt
    resource: https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=NASADEM_HGT
    title: "CMR collection record for NASADEM_HGT v001 (concept C2763264762-LPCLOUD, revision 40 of 2026-01-16), read 2026-09-15: DOI, platform OV-105 and instrument SRTM, temporal extent, the geodetic model WGS84/EGM96, the HGT native format at 7.1 MB average and 103,565.8 MB total, the distribution over HTTPS and the Earthdata Cloud, the S3 buckets and credentials endpoint, and the Earthdata Search and AppEEARS access links"
  - id: cmr-shhp
    resource: https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=NASADEM_SHHP
    title: "CMR collection record for NASADEM_SHHP v001 (concept C2763266322-LPCLOUD, revision 35 of 2026-01-14), read 2026-09-15: binary native format at 60.2 MB average, the same extent, distribution and buckets"
  - id: cmr-nc
    resource: https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=NASADEM_NC
    title: "CMR collection record for NASADEM_NC v001 (concept C2763264764-LPCLOUD), read 2026-09-15: the merged DEM in netCDF-4 at 24.8 MB average"
  - id: cmr-numnc
    resource: https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=NASADEM_NUMNC
    title: "CMR collection record for NASADEM_NUMNC v001 (concept C2763264768-LPCLOUD), read 2026-09-15: the merged DEM source layer in netCDF-4"
  - id: cmr-sc
    resource: https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=NASADEM_SC
    title: "CMR collection record for NASADEM_SC v001 (concept C2763264770-LPCLOUD), read 2026-09-15: the slope and curvature grouping"
  - id: cmr-sim
    resource: https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=NASADEM_SIM
    title: "CMR collection record for NASADEM_SIM v001 (concept C2763266325-LPCLOUD), read 2026-09-15: the SRTM image mosaic grouping"
  - id: doi-hgt
    resource: https://doi.org/10.5067/MEASURES/NASADEM/NASADEM_HGT.001
    title: "The product DOI, resolved 2026-09-15 to the Earthdata catalog page for NASADEM_HGT; a DataCite DOI, for which the Crossref API holds no record"
  - id: datum-gotcha
    resource: ../gotchas/nasadem-orthometric-versus-ellipsoidal.md
    title: "This bundle's gotcha on the two vertical references in the NASADEM collections"
  - id: void-gotcha
    resource: ../gotchas/nasadem-void-fill-and-source-layer.md
    title: "This bundle's gotcha on the void fill and the NUM source layer"
---

# NASADEM version 1

**Identity.** NASADEM is the modernization of the Shuttle Radar
Topography Mission (SRTM) digital elevation model, produced under the
NASA Making Earth System Data Records for Use in Research Environments
(MEaSUREs) program at the Jet Propulsion Laboratory and released by the
LP DAAC in February 2020.[^user-guide][^dem-guide] The height product
is NASADEM_HGT, "NASADEM Merged DEM Global 1 arc second V001", CMR
collection C2763264762-LPCLOUD (provider LPCLOUD, short name
NASADEM_HGT, version 001, DOI 10.5067/MEASURES/NASADEM/NASADEM_HGT.001),
platform OV-105 (the orbiter Endeavour), instrument SRTM, temporal
extent 2000-02-11 to 2000-02-21, the eleven days of the mission, and
collection progress COMPLETE.[^cmr-hgt][^hgt-page] The DOI resolves at
doi.org to the Earthdata catalog page for the collection.[^doi-hgt] The
product page listed 14,520 granules on 2026-09-15, one per one degree
tile.[^hgt-page]

The original SRTM raw signal data were reprocessed with improved
algorithms and with two data sets that did not exist at the original
processing: ICESat Geoscience Laser Altimeter System (GLAS) lidar
elevations, used as ground control, and the ASTER Global DEM, used as
fill.[^user-guide] The guide names the processing changes in order:
phase unwrapping with a hybrid of the original residue method and
SNAPHU plus shifted patch boundaries, which unwrapped more than half of
the strip-level void area of the original SRTM; a height ripple error
correction driven by ICESat GLAS and modelled ocean topography, which
removes ripples of a few metres with along-track scales of tens of
kilometres caused by uncompensated mast motion after Shuttle attitude
manoeuvres; an improved height precision estimate; and a finishing
chain of geoid conversion, water masking, unwrapping error removal,
void filling by a delta surface fill, and slope and curvature
products.[^user-guide]

## The collections

The guide's Table 1 groups the outputs into product groupings, each a
CMR collection at the LP DAAC:[^user-guide]

| Collection | CMR concept | Layers |
|---|---|---|
| NASADEM_HGT | C2763264762-LPCLOUD | hgt (void-filled merged DEM, 2-byte signed integer, metres relative to the EGM96 geoid, valid -32767 to 32767), num (source and scene count, byte, classes of Table 2), swb (updated SRTM water body data, byte, 0 land and 255 water) |
| NASADEM_SHHP | C2763266322-LPCLOUD | hgt_srtmOnly (hgts: SRTM-only floating-point DEM, 4-byte real, metres relative to the WGS84 ellipsoid, fill -32768), err (height error, 2-byte unsigned integer, millimetres, 32769 void) |
| NASADEM_SC | C2763264770-LPCLOUD | slope and aspect (hundredths of degrees, 0 water), plan and profile curvature (inverse metres), swbd |
| NASADEM_SIM | C2763266325-LPCLOUD | img_comb (radar combined images, DN plus 128), img_comb_num |
| NASADEM_NC and NASADEM_NUMNC | C2763264764-LPCLOUD and C2763264768-LPCLOUD | the merged DEM and its source layer in netCDF-4 |

The guide's Table 1 also lists a subswath grouping NASADEM_SSP
(correlation, individual images and incidence angles); no CMR
collection was queried for it here.[^user-guide] The netCDF
collections are the same merged DEM and NUM data in another format,
at 24.8 MB per file.[^cmr-nc][^cmr-numnc][^hgt-page] The product page
layer table for NASADEM_HGT lists DEM (int16, metres), NUM (uint8,
class) and SWB (uint8, class), and for NASADEM_SHHP lists
HGT_SRTMONLY (floating point, fill -32768) and ERR (uint16,
millimetres, fill 32769).[^hgt-page][^shhp-page]

The two height layers are on different vertical references: the
integer heights of the merged void-free DEM are relative to the EGM96
geoid, the floating-point heights of the SRTM-only DEM are relative to
the WGS84 ellipsoid, and the guide says so in one sentence set in
bold.[^user-guide] The CMR records and the LP DAAC comparison guide
write the datum as WGS84/EGM96 for the collection as a
whole.[^cmr-hgt][^dem-guide] The conversion was done last in the
processing: the SRTM reprocessing and the ICESat control were on the
ellipsoid, and a conversion array from a standard EGM96 database at
15 arc second postings, resampled to 1 arc second by bilinear
interpolation, was subtracted from each ellipsoid-referenced quad
([the datum gotcha](../gotchas/nasadem-orthometric-versus-ellipsoidal.md)).[^user-guide][^datum-gotcha]

## Tiles and files

Every product is a flat binary file in big endian byte order with 3601
rows and 3601 columns, one file per one degree by one degree tile,
named by the geographic coordinate of the tile's southwest corner
(NASADEM_HGT_n04w075.zip in the guide, s01w047.hgt on the product
page, s06w059.hgts for the SRTM-only height).[^user-guide][^hgt-page][^shhp-page]
The spacing is 1 arc second, which the product pages and the CMR
records render as 30 m.[^hgt-page][^cmr-hgt] The 3601 count means the
edge row and column of a tile sit on the whole-degree lines and are
shared with the neighbouring tile: the SRTM guide says the file name
coordinates refer to the centre of the lower left pixel and all edge
pixels are centred on whole-degree lines, and the NASADEM guide
describes its quads as 3601 by 3601 with overlap at quad edges, in
contrast to the PRISM AW3D30 DEM's 3600 by 3600 with no overlap and
pixel centres offset by half a pixel.[^srtm-guide][^user-guide] A
mosaic that concatenates tiles without dropping the shared edge
duplicates one row and one column per seam.

## Processing, in the order the guide gives it

**Phase unwrapping.** The original SRTM used a residue-based unwrapper
that masked large areas as unreliable, and a 15 arc second
low-resolution database from pre-mission DEMs for ambiguity
resolution. NASADEM runs the residue method first and SNAPHU where the
residue solution's correlation and coverage fall below thresholds,
keeps the SNAPHU result where its coverage and boundary phase variance
improve, resolves ambiguities against a new low-resolution database
built from SRTM Version 3 (SRTM Plus) with a one degree northward
extension, and merges alternative solutions from shifted patch
boundaries. The guide's Table 3 gives strip-level coverage rising from
about 90 to 95 per cent to about 96 to 98 per cent by continent, with
52 to 63 per cent of the original strip voids filled by the new
unwrapping.[^user-guide]

**Height ripple error correction.** Imprecise knowledge of the
interferometric baseline roll angle, excited by thruster firings about
every 8 seconds or 60 km along the orbit, produces height errors that
grow linearly with ground range, up to a few metres, and other
systematic errors. The correction fits a linear range model in 1 km
along-track windows to the difference between SRTM heights and ground
control points, smooths the parameters along track with a
Savitzky-Golay filter over adaptive windows of 6 km near manoeuvres and
30 to 50 km elsewhere, and applies it to each strip in radar geometry
before mosaicking. The control points are ICESat GLAS shots over land
(GLA14, signal to noise above 50, differences above 80 m from the
original SRTM rejected, glaciers masked with the Randolph Glacier
Inventory, snow seasons excluded by MODIS snow cover) and modelled
ocean topography over the sea; ICESat heights, on the TOPEX/Poseidon
ellipsoid, were shifted to WGS84 by a latitude-dependent offset of
about 70 cm on average. Over North America the weighted root mean
square difference against the control fell from 5.0 to 4.0 m and the
unweighted from 6.1 to 5.3 m.[^user-guide]

**Vegetation.** SRTM C-band does not reach the ground under forest.
The guide's Table 4 compares the SRTM phase centre with ICESat
waveform metrics over 349 vegetated areas: the closest metric is rh50,
the height at which half the returned energy sits, with a mean bias of
-0.48 m; the ground return rh0 differs by -6.28 m and the canopy top
rh100 by 11.94 m, with standard deviations of 7 to 10 m. The phase
centre therefore lies inside the canopy, and its position depends on
canopy density and on incidence angle (about 70 cm per ten degrees).
Vegetated shots were kept as control because bare ground shots are too
sparse under forest, with their uncertainty enlarged to down-weight
them.[^user-guide]

**Finishing.** After the geoid conversion, the SRTM Water Body Data
(SWBD) shoreline vectors were rasterized and repaired against the
GDEM3 water mask in about 140 quads; oceans are set to zero, lakes and
river segments were adjusted vertically to fit the new terrain (some
rivers lost the monotonic stepping SRTM Version 2 had enforced), and
shoreline pixels touching water were set to the water height plus one
metre if not already higher. Any pixel differing from the average of
its eight neighbours by more than 100 m was replaced by that average.
Unwrapping errors, typically areas nearly surrounded by void and more
than 120 m above GDEM2, were found in 158 quads and voided by hand.
The remaining voids were filled from an error-suppressed void-free
GDEM3 built for the purpose from draft GDEM3, GDEM2 and PRISM AW3D30
(GMTED2010 was not used) by a modified delta surface fill
([the void fill gotcha](../gotchas/nasadem-void-fill-and-source-layer.md)).[^user-guide][^void-gotcha]
Slope, aspect and the two curvatures are computed from a weighted
quadric fit at each posting, with the NUM file used to weight sources.[^user-guide]

## Coverage

All land between 60 degrees north and 56 degrees south, about 80 per
cent of the global landmass, in tiles bounded by 60 N, 56 S, 180 W and
180 E.[^hgt-page][^cmr-hgt][^user-guide] The comparison guide records
that NASADEM filled voids near the edges of the SRTM extent that the
SRTM products left open, that SRTM had more voids than ASTER GDEM in
mountains, and that there are limited NASADEM data around the
antimeridian at 180 degrees longitude.[^dem-guide] The void fill
sources were acquired long after SRTM: the comparison guide gives the
ASTER GDEM version 3 input as scenes from 2000-03-01 to
2013-11-30.[^dem-guide]

## Access

Cloud-hosted: the product page marks the collection cloud enabled and
the CMR record distributes it over HTTPS and the Earthdata Cloud, in
the HGT native format at 7.1 MB per file and 103,565.8 MB for the
collection, from the buckets `s3://lp-prod-protected/NASADEM_HGT.001`
and `s3://lp-prod-public/NASADEM_HGT.001` in region us-west-2, with
temporary S3 credentials issued at
data.lpdaac.earthdatacloud.nasa.gov/s3credentials.[^hgt-page][^cmr-hgt]
The SRTM-only height collection is distributed the same way at 60.2 MB
per file.[^cmr-shhp] The CMR record's data links are an Earthdata
Search granule search on the collection concept id and AppEEARS, and
the guide names Earthdata Search and the Data Pool.[^cmr-hgt][^user-guide]
The slope and curvature and image mosaic groupings are their own
collections.[^cmr-sc][^cmr-sim]

## Uncertainty

The merged height product carries no per-pixel uncertainty layer. What
stands in:

- **The SRTM mission figures.** The specification was an absolute
  vertical error under 16 m and a relative height error under 10 m at
  the 90 per cent level, with 20 m absolute and 15 m relative
  geolocation; the global assessment of the original SRTM found
  average absolute and relative height errors of about 6.8 m and 7 m
  and an absolute geolocation error of about 9.7 m, smaller than 8 m
  in sparsely vegetated areas. The guide cites these for SRTM and gives
  no equivalent global figure for NASADEM.[^user-guide]
- **The ripple correction residual.** Over North America the linear
  correction reduced the mean absolute difference against control from
  3.46 to 2.81 m and the root mean square from 6.08 to 5.30 m,
  averaged per strip (Table 5).[^user-guide]
- **The err layer of NASADEM_SHHP.** The height precision in
  millimetres is the random component from the interferometric phase
  standard deviation, evaluated from its probability density as a
  function of unbiased correlation and effective looks; it does not
  describe the systematic residuals, the vegetation bias or the fill
  sources, and it belongs to the ellipsoid-referenced SRTM-only
  height.[^user-guide][^shhp-page]
- **Vegetation.** The phase centre sits inside the canopy, near the
  rh50 metric, with a standard deviation of about 7 m against ICESat
  over vegetated areas (Table 4), so under forest the height is
  neither the ground nor the canopy top.[^user-guide]
- **Glaciers and snow.** Glacier control points were excluded, so
  height ripples over glaciers may remain uncorrected; the guide notes
  differences of 5 to 30 m over the Malaspina Glacier between SRTM and
  ICESat from melt in the intervening years, and C-band penetration of
  1 to 2 m into snow.[^user-guide]
- **Filled areas.** Where NUM says the height is not SRTM, the height
  is an optical stereo DEM from years later, vertically shifted by the
  delta surface, and the guide says a fill can look smoother yet be
  less correct.[^user-guide]
- **Water.** Lake and river heights were fitted to the new terrain
  rather than re-edited, and some river monotonicity was lost.[^user-guide]

## Known issues, as the guide and the comparison guide record them

- The mutual dependency of the DEMs: the SRTM reprocessing referenced
  a database containing GDEM2, the GDEMs used SRTM for error checking
  and fill, and PRISM AW3D30 used SRTM for vertical adjustment, so the
  fill is not independent of the product it fills.[^user-guide]
- Limited data around the antimeridian.[^dem-guide]
- Unwrapping errors too low rather than too high, and errors where
  GDEM2 was itself cloud-affected, could not be detected by the
  120 m test and are believed rare.[^user-guide]

[^hgt-page]: LP DAAC product page, NASADEM_HGT v001, read 2026-09-15
[^shhp-page]: LP DAAC product page, NASADEM_SHHP v001, read 2026-09-15
[^user-guide]: NASADEM user guide, version 1.3, January 2025
[^dem-guide]: LP DAAC DEM Product Comparison Guide, read 2026-09-15
[^srtm-guide]: SRTM Collection User Guide, October 2015, tile geometry
[^cmr-hgt]: CMR collection record C2763264762-LPCLOUD, read 2026-09-15
[^cmr-shhp]: CMR collection record C2763266322-LPCLOUD, read 2026-09-15
[^cmr-nc]: CMR collection record C2763264764-LPCLOUD, read 2026-09-15
[^cmr-numnc]: CMR collection record C2763264768-LPCLOUD, read 2026-09-15
[^cmr-sc]: CMR collection record C2763264770-LPCLOUD, read 2026-09-15
[^cmr-sim]: CMR collection record C2763266325-LPCLOUD, read 2026-09-15
[^doi-hgt]: the product DOI resolved at doi.org, 2026-09-15
[^datum-gotcha]: this bundle's gotcha on orthometric versus ellipsoidal heights
[^void-gotcha]: this bundle's gotcha on the void fill and the NUM layer
