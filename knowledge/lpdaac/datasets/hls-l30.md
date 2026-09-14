---
type: dataset
spheres: [biosphere, geosphere]
title: "HLS L30 version 2.0: Landsat 8 and 9 nadir BRDF-adjusted surface reflectance on 30 m MGRS tiles"
description: "HLSL30 v2.0 is the Landsat half of the Harmonized Landsat and Sentinel-2 surface reflectance suite: Landsat 8 and 9 OLI surface reflectance from Collection 2 L1TP input, atmospherically corrected with LaSRC, normalized to a nadir view with a MODIS-derived c-factor, gridded into the Sentinel-2 MGRS tiling at 30 m, and delivered as one Cloud Optimized GeoTIFF per layer: seven reflective NBAR bands, a cirrus top-of-atmosphere band, two TIRS brightness temperature bands, a bit-packed Fmask quality layer and four angle layers. The record starts 2013-04-11 and covers the global land except Antarctica."
tags: [hls, hlsl30, l30, landsat, oli, tirs, surface-reflectance, nbar, mgrs, lpdaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:40:00Z }
resource: https://lpdaac.usgs.gov/products/hlsl30v002/
version: "Product version 2.0 (DOI 10.5067/HLS/HLSL30.002), CMR collection C2021957657-LPCLOUD (provider LPCLOUD, short name HLSL30, version 2.0), verified 2026-09-14: temporal extent 2013-04-11 to present with the ends-at-present flag set, 15,972,585 granules listed on the product page that day; the user guide read is the product version 2.0 guide last updated April 2026 and the known issues list is the April 2026 edition"
status: draft
stale_after: 2027-03-14
citation:
  access_date_required: true
  authority: https://lpdaac.usgs.gov/
  data: "Neigh, C., Ju, J., Roger, J.-C., Skakun, S., Vermote, E., Claverie, M., Dungan, J., Yin, Z., Freitag, B., and Justice, C. (2021). HLS Operational Land Imager Surface Reflectance and TOA Brightness Daily Global 30m v2.0 [Dataset]. NASA Land Processes Distributed Active Archive Center, accessed {access_date}, 10.5067/HLS/HLSL30.002"
  doi: "10.5067/HLS/HLSL30.002"
  note: "the citation text is the one the LP DAAC product page renders; the access date matters because forward processing has been corrected several times without reprocessing the archive, so two downloads of the same tile and day can differ by their production date"
sources:
  - id: l30-page
    resource: https://lpdaac.usgs.gov/products/hlsl30v002/
    title: "LP DAAC product page for HLSL30 v2.0, read 2026-09-14: DOI, CMR concept id, temporal extent, granule count, the variables table (data type, fill, scale per layer), the citation, and the documents it links"
  - id: user-guide
    resource: https://lpdaac.usgs.gov/documents/1698/HLS_User_Guide_V2.pdf
    title: "HLS Product User Guide, product version 2.0, last updated April 2026 (Ju, Neigh, Sridhar, Claverie, Skakun, Roger, Vermote, Dungan, Ashokkumar), read in full 2026-09-14: Tables 2, 3, 6, 8, 9 and 11, sections 3.5, 4.2 to 4.5, 6.1 and 6.3, and Appendix A"
  - id: l30-known-issues
    resource: https://lpdaac.usgs.gov/documents/2434/HLS_v2.0_L30_known_issues_April2026.pdf
    title: "HLS L30 v2.0 Known Issues, April 2026, read in full 2026-09-14: sixteen issues from the bright-target aerosol failure to the high-latitude gridding fault"
  - id: hls-l30-page
    resource: https://hls.gsfc.nasa.gov/products-description/l30/
    title: "HLS project site, L30 product description, read 2026-09-14: the layer table with its saturation flag column and the cubic convolution resampling statement"
  - id: hls-algorithms
    resource: https://hls.gsfc.nasa.gov/algorithms/
    title: "HLS project site, Algorithms page, read 2026-09-14: atmospheric correction, cloud masking and the QA band, spatial co-registration, BRDF normalization with its coefficient table, bandpass adjustment"
  - id: cmr-l30
    resource: https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=HLSL30&version=2.0
    title: "CMR collection record for HLSL30 v2.0 (concept C2021957657-LPCLOUD), read 2026-09-14: DOI, platforms, temporal extent, version description and the related documents"
  - id: claverie-2018
    resource: https://doi.org/10.1016/j.rse.2018.09.002
    title: "Claverie, Ju, Masek, Dungan, Vermote, Roger, Skakun and Justice (2018), The Harmonized Landsat and Sentinel-2 surface reflectance data set, Remote Sensing of Environment 219, 145 to 161: the paper the user guide cites for the bandpass residual; the publisher page sits behind a bot check, so the paper is cited on its registry record"
  - id: claverie-2018-crossref
    resource: https://api.crossref.org/works/10.1016/j.rse.2018.09.002
    title: "Crossref record for 10.1016/j.rse.2018.09.002, read 2026-09-14: title, the eight authors, journal, volume 219, pages 145 to 161, issued December 2018"
  - id: s30
    resource: hls-s30.md
    title: "This bundle's HLS S30 concept, the Sentinel-2 half of the suite on the same grid"
---

# HLS L30 version 2.0

**Identity.** HLSL30 is the Landsat product of the Harmonized Landsat
and Sentinel-2 (HLS) project: 30 m nadir BRDF-adjusted surface
reflectance (NBAR) derived from Landsat 8 and Landsat 9 Operational
Land Imager (OLI) data, with the two Thermal Infrared Sensor (TIRS)
bands carried as top-of-atmosphere brightness temperature.[^l30-page]
The CMR collection is C2021957657-LPCLOUD (short name HLSL30, version
2.0, DOI 10.5067/HLS/HLSL30.002), platforms LANDSAT-8 and LANDSAT-9,
instrument OLI, temporal extent 2013-04-11 to the present.[^cmr-l30] The
input is the USGS Collection 2 Level-1 Terrain Precision-corrected
(L1TP) product, top of atmosphere; Landsat 9 data enter from 2021.[^user-guide]
On 2026-09-14 the product page listed 15,972,585 granules.[^l30-page]

The project's own statement of what "harmonized" means is a list of
six operations: atmospheric correction to surface reflectance, cloud
and cloud shadow masking, normalization to a nadir view through a
BRDF estimate, spectral bandpass adjustment of one sensor group to the
other, gridding to a common resolution, projection and tile, and a
standard presentation of data and metadata.[^hls-algorithms] L30 has
all of these except the bandpass adjustment: the OLI bandpasses are the
reference to which S30 is adjusted, so the L30 reflective bands are
BRDF-normalized but not spectrally adjusted.[^user-guide] The two
products share the grid and are, in the product page's word,
stackable; the same 30 m MGRS pixel in an L30 and an S30 granule is
the same place ([this bundle's S30 concept](hls-s30.md)).[^l30-page][^s30]

## Layers

One Cloud Optimized GeoTIFF per layer, internally deflate-compressed,
in a directory named like `HLS.L30.T17SLU.2020209T155956.v2.0`, where
T17SLU is the MGRS tile and 2020209T155956 the year, day of year and
UTC time. The user guide's Table 6 lists the layers:[^user-guide]

| Layer | Source band | Content | Nominal wavelength (micrometres) | Type | Scale | Fill |
|---|---|---|---|---|---|---|
| B01 | OLI 1 | coastal aerosol, NBAR | 0.43 to 0.45 | int16 | 0.0001 | -9999 |
| B02 | OLI 2 | blue, NBAR | 0.45 to 0.51 | int16 | 0.0001 | -9999 |
| B03 | OLI 3 | green, NBAR | 0.53 to 0.59 | int16 | 0.0001 | -9999 |
| B04 | OLI 4 | red, NBAR | 0.64 to 0.67 | int16 | 0.0001 | -9999 |
| B05 | OLI 5 | NIR narrow, NBAR | 0.85 to 0.88 | int16 | 0.0001 | -9999 |
| B06 | OLI 6 | SWIR 1, NBAR | 1.57 to 1.65 | int16 | 0.0001 | -9999 |
| B07 | OLI 7 | SWIR 2, NBAR | 2.11 to 2.29 | int16 | 0.0001 | -9999 |
| B09 | OLI 9 | cirrus, top-of-atmosphere reflectance, not BRDF adjusted | 1.36 to 1.38 | int16 | 0.0001 | -9999 |
| B10 | TIRS 10 | thermal infrared 1, top-of-atmosphere brightness temperature in degrees Celsius | 10.60 to 11.19 | int16 | 0.01 | -9999 |
| B11 | TIRS 11 | thermal infrared 2, top-of-atmosphere brightness temperature in degrees Celsius | 11.50 to 12.51 | int16 | 0.01 | -9999 |
| Fmask | | bit-packed quality assessment | | uint8 | none | 255 |
| SZA, SAA, VZA, VAA | | sun and view zenith and azimuth, degrees | | uint16 | 0.01 | 40000 |

There is no B08 layer: the file list in the guide's section 6.1 runs
B01 to B07, then B09, B10, B11.[^user-guide] The product page and the
CMR abstract say the product includes eleven bands plus the QA band
and four angle bands, while the guide's Table 6 lists ten spectral
layers; the layer table above follows the guide.[^l30-page][^cmr-l30][^user-guide]
The band code names keep the OLI numbering, so L30 B05 is the near
infrared and B06 and B07 are the shortwave infrared, which is not what
the same codes mean in S30
([the band-name gotcha](../gotchas/hls-band-names-differ.md)).[^user-guide]
The project site's L30 layer table adds a saturation flag value of
12000 for the reflective bands, a column the user guide does not
carry.[^hls-l30-page] The thermal bands are not atmospherically
corrected; they are rescaled to apparent brightness temperature.[^user-guide]
The angle layers are the Collection 2 angles, derived for the red band
and taken to represent every band.[^user-guide]

The UTC timestamp in an L30 name is the sensing time at the centre of
the input Landsat scene; after gridding it does not describe the tile,
and where two scenes overlap a tile the time of one of them is chosen
by chance, so it is a unique identifier rather than an observation
time.[^user-guide] The LP DAAC product page describes the same field as
the date and time of production; the guide is followed here.[^l30-page]
The guide's own example directory name carries `V2.0` in capitals while
the CMR browse links and the known issues documents write
`v2.0`.[^user-guide][^cmr-l30][^l30-known-issues]

## Processing, in the order the guide gives it

Atmospheric correction is LaSRC, version 3.5.5 in a USGS C
implementation, based on the 6SV radiative transfer code, with aerosol
optical thickness retrieved from the image under a continental aerosol
model and ozone and water vapour from MODIS 0.05 degree ancillary data
before May 2024 and VIIRS after.[^user-guide] Cloud, cloud shadow, snow
and ice and water come exclusively from Fmask 4.7; the cloud and shadow
masks are dilated by 150 m (five pixels) and the dilation is labelled
adjacent to cloud or shadow; the LaSRC aerosol level joins the same
byte ([the Fmask gotcha](../gotchas/hls-fmask-is-bit-packed.md)).[^user-guide][^hls-algorithms]
Gridding into the MGRS tiles needs a resampling even when the Landsat
scene is in the tile's UTM zone, because the USGS places the UTM origin
at a pixel centre and the MGRS system at a pixel corner; the spectral
data are resampled by cubic convolution and reprojected first when the
scene's zone is the neighbouring one.[^user-guide][^hls-l30-page] The
BRDF normalization is the c-factor method with one global set of
MODIS-derived Ross-Li coefficients per band, the view zenith set to
nadir and the solar zenith set to the mean of the Landsat and
Sentinel-2 overpass values at the tile centre for the day
([the harmonization gotcha](../gotchas/hls-harmonized-not-native.md)).[^user-guide]

## Coverage

All global land except Antarctica, on a land mask derived from the
NOAA GSHHG shoreline data; Antarctica is excluded because low solar
elevations compromise the plane-parallel atmospheric correction, some
small islands are not acquired regularly, latitudes above 82 degrees
are beyond the sensors, and high-latitude winter is not
acquired.[^user-guide] The combined Landsat and Sentinel-2 record gives
a global land observation every 1.6 days on average at 30 m.[^l30-page]
Data are produced continuously and are typically available within one
to two days of acquisition.[^user-guide]

## Uncertainty

The product carries no per-pixel reflectance uncertainty field. What
stands in:

- **The aerosol level in the QA byte.** Bits 6 and 7 record the LaSRC
  aerosol optical thickness level; both bits set means high aerosol,
  which is where the atmospheric correction is least trusted, and the
  known issues document says the spectral data under it should be
  discarded.[^user-guide][^l30-known-issues]
- **The atmospheric correction's own validation.** LaSRC was assessed
  for Landsat 8 within the CEOS Atmospheric Correction Intercomparison
  Exercise; the guide cites the exercise and gives no per-band error
  figure of its own.[^user-guide]
- **The bandpass residual, on the S30 side only.** Once S30 is
  adjusted to the OLI bandpasses, the spectral difference between the
  MSI and OLI bands is under 2 per cent with a residual standard
  deviation under 0.005 reflectance units; L30 is the reference and
  carries no such adjustment.[^user-guide][^claverie-2018][^claverie-2018-crossref]
- **Geolocation.** Only Collection 2 L1TP scenes are used; within
  L1TP, Tier 2 scenes carry geolocation error up to 30 m in x or y and
  make up about 5 per cent of the category.[^user-guide]
- **Snow.** Landsat and Sentinel-2 snow reflectance is highly
  inconsistent, Landsat generally higher in the visible on same-day
  pairs, from aerosol retrieval mistakes over snow.[^l30-known-issues]

## Known issues

The April 2026 known issues document lists sixteen; the ones that
change a result rather than a file:[^l30-known-issues]

- Pixels next to bright targets (buildings, snow and ice, cloud) can
  receive an unrealistically high aerosol retrieval and hence a
  reflectance that is too low; below a reflectance of -0.2 the pixel
  is set to the -9999 fill and its QA to 255
  ([the scale and fill gotcha](../gotchas/hls-scale-and-fill.md)).
- Aerosol is not retrieved over water; the nearest land retrieval is
  used, and a wrong one makes dark plumes over lakes and bays.
- Atmospheric correction and Fmask run on the WRS-2 scene before
  gridding, so a path/row boundary can show as an abrupt change in
  reflectance or in the cloud mask inside a tile; rare.
- The Fmask layer before April 2022 has water omission errors where
  spectral detection is hard and shadow errors in high relief; for two
  to three months in 2021 Fmask ran without its DEM and surface water
  auxiliaries.
- Some granules lack the scale_factor and offset tags in their COGs,
  so automatic scaling fails and the scaling has to be explicit; the
  code is fixed and the granules are not reprocessed.
- The map projection metadata labels every tile as northern hemisphere
  (HLS keeps southern y coordinates negative with a false northing of
  zero), and the L30 angle layers use a false northing of ten million
  metres although their metadata says zero, which positions southern
  angle data in the wrong hemisphere
  ([the tile gotcha](../gotchas/hls-mgrs-tile-overlap.md)).
- For a short period in 2024 L1GT scenes were processed; they are
  mostly cloud or snow, and the cmr.xml metadata names the input
  scene. Granules from May to July 2023 built on L1GT input were
  removed from the archive.
- The UTC date in the file name can be the day before the local date
  over eastern Australia and New Zealand, two overpasses a local day
  apart can share a UTC day, and on such days the atmospheric ancillary
  data can be from the day before.
- Landsat 9 scenes from October 2021 to March 2023 were reprocessed by
  the USGS with overpass times changed by a fraction of a second, and
  because the time is in the file name the older granules were not
  overwritten: duplicates exist.
- At and above 80 degrees north, two consecutive overpasses can be
  gridded into one tile, or one overpass split into two files.

The podaac bundle's OPERA DSWx-HLS surface water concept
(`knowledge/podaac/datasets/opera-dswx-hls.md`) derives from this
product and S30; its snow and cloud classes come from this Fmask
layer, and it is named here rather than restated.

[^l30-page]: LP DAAC product page, HLSL30 v2.0, read 2026-09-14
[^user-guide]: HLS Product User Guide, product version 2.0, April 2026
[^l30-known-issues]: HLS L30 v2.0 Known Issues, April 2026
[^hls-l30-page]: HLS project site, L30 product description
[^hls-algorithms]: HLS project site, Algorithms page
[^cmr-l30]: CMR collection record C2021957657-LPCLOUD, read 2026-09-14
[^claverie-2018]: Claverie and others 2018, Remote Sensing of Environment 219, doi:10.1016/j.rse.2018.09.002, cited on its Crossref record
[^claverie-2018-crossref]: Crossref record for 10.1016/j.rse.2018.09.002, read 2026-09-14
[^s30]: this bundle's HLS S30 concept
