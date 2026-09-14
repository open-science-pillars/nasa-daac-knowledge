---
type: dataset
spheres: [biosphere, geosphere]
title: "HLS S30 version 2.0: Sentinel-2 nadir BRDF-adjusted surface reflectance, bandpass-adjusted to Landsat, on 30 m MGRS tiles"
description: "HLSS30 v2.0 is the Sentinel-2 half of the Harmonized Landsat and Sentinel-2 surface reflectance suite: Sentinel-2A, 2B and 2C MSI Level-1C data atmospherically corrected with LaSRC, resampled from 10, 20 and 60 m to 30 m, normalized to a nadir view with a MODIS-derived c-factor, and in the seven bands that OLI shares adjusted by a linear fit to the OLI bandpasses. Thirteen spectral layers keep the MSI numbering (B01 to B12 with B8A), so B05 to B07 are red-edge bands and B11 and B12 the shortwave infrared, beside a bit-packed Fmask layer and four angle layers. The record starts 2015-11-28 and covers the global land except Antarctica."
tags: [hls, hlss30, s30, sentinel-2, msi, surface-reflectance, nbar, bandpass, mgrs, lpdaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:40:00Z }
resource: https://lpdaac.usgs.gov/products/hlss30v002/
version: "Product version 2.0 (DOI 10.5067/HLS/HLSS30.002), CMR collection C2021957295-LPCLOUD (provider LPCLOUD, short name HLSS30, version 2.0), verified 2026-09-14: temporal extent 2015-11-28 to present with the ends-at-present flag set, platforms Sentinel-2A, 2B and 2C, 21,845,492 granules listed on the product page that day; the user guide read is the product version 2.0 guide last updated April 2026 and the known issues list is the April 2026 edition"
status: draft
stale_after: 2027-03-14
citation:
  access_date_required: true
  authority: https://lpdaac.usgs.gov/
  data: "Neigh, C., Ju, J., Roger, J.-C., Skakun, S., Vermote, E., Claverie, M., Dungan, J., Yin, Z., Freitag, B., and Justice, C. (2021). HLS Sentinel-2 Multi-spectral Instrument Surface Reflectance Daily Global 30m v2.0 [Dataset]. NASA Land Processes Distributed Active Archive Center, accessed {access_date}, 10.5067/HLS/HLSS30.002"
  doi: "10.5067/HLS/HLSS30.002"
  note: "the citation text is the one the LP DAAC product page renders; the access date matters because forward processing has been corrected several times (the image quality mask since June 2025, the swath-edge correction since March 2025) without reprocessing the archive"
sources:
  - id: s30-page
    resource: https://lpdaac.usgs.gov/products/hlss30v002/
    title: "LP DAAC product page for HLSS30 v2.0, read 2026-09-14: DOI, CMR concept id, temporal extent, granule count, the variables table (data type, fill, scale per layer), the citation, and the documents it links"
  - id: user-guide
    resource: https://lpdaac.usgs.gov/documents/1698/HLS_User_Guide_V2.pdf
    title: "HLS Product User Guide, product version 2.0, last updated April 2026 (Ju, Neigh, Sridhar, Claverie, Skakun, Roger, Vermote, Dungan, Ashokkumar), read in full 2026-09-14: Tables 2, 3, 5, 7, 8, 9 and 11, sections 3.1, 3.5, 4.2 to 4.5, 6.1 and 6.3, and Appendix A"
  - id: s30-known-issues
    resource: https://lpdaac.usgs.gov/documents/2435/HLS_v2.0_S30_known_issues_April2026.pdf
    title: "HLS S30 V2.0 Known Issues, April 2026, read in full 2026-09-14: twelve open issues and three resolved in forward processing"
  - id: hls-s30-page
    resource: https://hls.gsfc.nasa.gov/products-description/s30/
    title: "HLS project site, S30 product description, read 2026-09-14: the band matchup table, the three resampling rules by input resolution, the layer table with its bandpass and BRDF adjustment columns"
  - id: hls-products
    resource: https://hls.gsfc.nasa.gov/products-description/
    title: "HLS project site, Product Description, read 2026-09-14: S30 is OLI-like except NIR B08 and the red-edge bands, which stay original MSI"
  - id: hls-algorithms
    resource: https://hls.gsfc.nasa.gov/algorithms/
    title: "HLS project site, Algorithms page, read 2026-09-14: the harmonization steps, the BRDF coefficient table, the bandpass adjustment coefficients for Sentinel-2A, 2B and 2C"
  - id: cmr-s30
    resource: https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=HLSS30&version=2.0
    title: "CMR collection record for HLSS30 v2.0 (concept C2021957295-LPCLOUD), read 2026-09-14: DOI, platforms, temporal extent, version description and the related documents"
  - id: claverie-2018
    resource: https://doi.org/10.1016/j.rse.2018.09.002
    title: "Claverie, Ju, Masek, Dungan, Vermote, Roger, Skakun and Justice (2018), The Harmonized Landsat and Sentinel-2 surface reflectance data set, Remote Sensing of Environment 219, 145 to 161: the paper the user guide cites for the bandpass residual; the publisher page sits behind a bot check, so the paper is cited on its registry record"
  - id: claverie-2018-crossref
    resource: https://api.crossref.org/works/10.1016/j.rse.2018.09.002
    title: "Crossref record for 10.1016/j.rse.2018.09.002, read 2026-09-14: title, the eight authors, journal, volume 219, pages 145 to 161, issued December 2018"
  - id: l30
    resource: hls-l30.md
    title: "This bundle's HLS L30 concept, the Landsat half of the suite on the same grid"
---

# HLS S30 version 2.0

**Identity.** HLSS30 is the Sentinel-2 product of the Harmonized
Landsat and Sentinel-2 (HLS) project: 30 m nadir BRDF-adjusted surface
reflectance (NBAR) derived from the MultiSpectral Instrument (MSI) on
Sentinel-2A, 2B and 2C.[^s30-page] The CMR collection is
C2021957295-LPCLOUD (short name HLSS30, version 2.0, DOI
10.5067/HLS/HLSS30.002), temporal extent 2015-11-28 to the
present.[^cmr-s30] The input is the ESA Level-1C top-of-atmosphere
product; Sentinel-2A data enter from 2015, 2B from 2017 and 2C from
2024.[^user-guide] On 2026-09-14 the product page listed 21,845,492
granules.[^s30-page]

S30 is the product that carries the whole harmonization: after
atmospheric correction, resampling and BRDF normalization, the
Sentinel-2 NBAR in the bands OLI shares is adjusted by a linear
transform to the OLI bandpasses, and the adjusted 30 m reflectance is
the final S30.[^hls-algorithms] The project site puts it in one line:
S30 is OLI-like except for the broad NIR B08 and the red-edge bands,
which remain original MSI.[^hls-products] The two products share the
grid and are stackable; the same 30 m MGRS pixel in an S30 and an L30
granule is the same place
([this bundle's L30 concept](hls-l30.md)).[^s30-page][^l30]

## Layers

One Cloud Optimized GeoTIFF per layer, in a directory named like
`HLS.S30.T17SLU.2020117T160901.v2.0`. The user guide's Table 7 lists
the layers, with Table 3 for the band names and wavelengths and Tables
2 and 5 for which bands are adjusted:[^user-guide]

| Layer | MSI band | Content | Nominal wavelength (micrometres) | BRDF adjusted | Bandpass adjusted | Type | Scale | Fill |
|---|---|---|---|---|---|---|---|---|
| B01 | 1 | coastal aerosol, NBAR | 0.43 to 0.45 | yes | yes | int16 | 0.0001 | -9999 |
| B02 | 2 | blue, NBAR | 0.45 to 0.51 | yes | yes | int16 | 0.0001 | -9999 |
| B03 | 3 | green, NBAR | 0.53 to 0.59 | yes | yes | int16 | 0.0001 | -9999 |
| B04 | 4 | red, NBAR | 0.64 to 0.67 | yes | yes | int16 | 0.0001 | -9999 |
| B05 | 5 | red-edge 1, NBAR | 0.69 to 0.71 | yes, interpolated coefficients | no | int16 | 0.0001 | -9999 |
| B06 | 6 | red-edge 2, NBAR | 0.73 to 0.75 | yes, interpolated coefficients | no | int16 | 0.0001 | -9999 |
| B07 | 7 | red-edge 3, NBAR | 0.77 to 0.79 | yes, interpolated coefficients | no | int16 | 0.0001 | -9999 |
| B08 | 8 | NIR broad, NBAR | 0.78 to 0.88 | yes | no | int16 | 0.0001 | -9999 |
| B8A | 8A | NIR narrow, NBAR | 0.85 to 0.88 | yes | yes | int16 | 0.0001 | -9999 |
| B09 | 9 | water vapour, top-of-atmosphere reflectance | 0.93 to 0.95 | no | no | int16 | 0.0001 | -9999 |
| B10 | 10 | cirrus, top-of-atmosphere reflectance | 1.36 to 1.38 | no | no | int16 | 0.0001 | -9999 |
| B11 | 11 | SWIR 1, NBAR | 1.57 to 1.65 | yes | yes | int16 | 0.0001 | -9999 |
| B12 | 12 | SWIR 2, NBAR | 2.11 to 2.29 | yes | yes | int16 | 0.0001 | -9999 |
| Fmask | | bit-packed quality assessment | | | | uint8 | none | 255 |
| SZA, SAA, VZA, VAA | | sun and view zenith and azimuth, degrees | | | | uint16 | 0.01 | 40000 |

The band code names keep the MSI numbering, so S30 B05, B06 and B07
are red-edge bands and the shortwave infrared is B11 and B12, where
L30 uses B05 for the near infrared and B06 and B07 for the shortwave
infrared ([the band-name gotcha](../gotchas/hls-band-names-differ.md)).[^user-guide]
The bandpass adjustment applies to the seven bands with an OLI
equivalent (MSI 1, 2, 3, 4, 8A, 11 and 12), with separate slope and
intercept per satellite; Table 5 of the guide and Table 2 of the
project site give the coefficients for 2A, 2B and 2C.[^user-guide][^hls-algorithms]
The project site's S30 layer table lists the QA layer as int8 where
the guide and the product page say uint8, and adds a saturation flag
value of 12000 for the reflective bands that the guide does not
carry.[^hls-s30-page][^user-guide][^s30-page] The angle layers are
interpolated from the ESA 5 km angle grid, with the view angle of the
second red-edge band used for every band.[^user-guide]

The UTC time in an S30 name is the time the sensor began sensing the
sunlit side of the Earth on that orbit, not the sensing time over the
tile, so two tiles from one orbit can share a timestamp and the field
serves to tell same-day observations at high latitude apart rather
than to time them.[^user-guide] The LP DAAC product page describes the
same field as the date and time of production; the guide is followed
here.[^s30-page]

## Processing, in the order the guide gives it

Atmospheric correction is LaSRC, the same code and ancillaries as
L30.[^user-guide] Cloud, shadow, snow and ice and water come from Fmask
4.7 applied to the Level-1C data, with the cloud and shadow dilated by
150 m and the LaSRC aerosol level added to the same byte
([the Fmask gotcha](../gotchas/hls-fmask-is-bit-packed.md)).[^user-guide][^hls-algorithms]
Resampling to 30 m depends on the input resolution: the project site
gives a simple average for the 10 m bands, an area-weighted average
for the 20 m bands and replication for the 60 m bands, while the guide
says the 10, 20 and 60 m data are resampled with an area-weighted
average; the categorical Fmask labels (derived at 20 m) and aerosol
levels (derived at 10 m) are resampled so that any label among the
overlapping input pixels turns on the output bit and the highest
aerosol level wins.[^hls-s30-page][^user-guide] The BRDF normalization
is the c-factor method with the same global MODIS-derived coefficients
as L30, and for the three red-edge bands, which have no MODIS
equivalent, coefficients interpolated between the MODIS red and NIR
bands ([the harmonization gotcha](../gotchas/hls-harmonized-not-native.md)).[^user-guide]

## Coverage

All global land except Antarctica, as for L30; the combined record
gives a global land observation every 1.6 days on average.[^s30-page][^user-guide]
Before the global use of the Global Reference Image in August 2021 the
Level-1C geolocation uncertainty was 12 m circular error at 90 per
cent, reduced to 5.1 m afterwards; HLS production began in September
2021 before ESA reprocessed the earlier data, so S30 from images
before August 2021 has the poorer geolocation, which the guide calls
acceptable because it is under half a 30 m pixel.[^user-guide]

## Uncertainty

The product carries no per-pixel reflectance uncertainty field. What
stands in:

- **The aerosol level in the QA byte.** Bits 6 and 7 record the LaSRC
  aerosol optical thickness level; both set means high aerosol, and
  the known issues document says the spectral data under it should be
  discarded.[^user-guide][^s30-known-issues]
- **The bandpass residual.** Once adjusted, the spectral difference
  between the MSI and OLI bands is under 2 per cent with a residual
  standard deviation under 0.005 reflectance units, the figure the
  guide attributes to Claverie and others 2018.[^user-guide][^claverie-2018][^claverie-2018-crossref]
- **The atmospheric correction's own validation.** LaSRC was assessed
  for Sentinel-2 within the CEOS Atmospheric Correction
  Intercomparison Exercise; the guide gives no per-band error figure
  of its own.[^user-guide]
- **Geolocation.** 12 m circular error at 90 per cent before August
  2021 inputs, 5.1 m after.[^user-guide]
- **Snow.** Sentinel-2 snow reflectance is generally lower than
  Landsat's in the visible on same-day pairs, and where snow detection
  fails the full aerosol retrieval runs over snow and yields visible
  reflectance as high as 1.6, a prevalent problem in spring at high
  latitudes.[^s30-known-issues]
- **The input archive is not one collection.** Level-1C observations
  before 2022 used for S30 predate ESA's Collection 1 reprocessing,
  and observations to 13 December 2023 were later reprocessed with
  improved calibration; the S30 archive has not been updated from
  either.[^s30-known-issues]

## Known issues

The April 2026 known issues document lists twelve open issues and
three resolved in forward processing only:[^s30-known-issues]

- Pixels next to bright targets can receive an unrealistically high
  aerosol retrieval and a reflectance that is too low; below -0.2 the
  pixel is set to the -9999 fill and its QA to 255
  ([the scale and fill gotcha](../gotchas/hls-scale-and-fill.md)).
- Aerosol is not retrieved over large water bodies; a wrong nearest
  land retrieval makes dark plumes over lakes and bays.
- Cloud masking runs per granule, and a cloud boundary that follows
  the tile boundary in a mosaic of two S30 granules shows a masking
  error in at least one of them.
- For two to three months in 2021 Fmask ran without its DEM and
  surface water auxiliaries.
- Some granules lack the scale_factor and offset tags in their COGs;
  the code is fixed and the granules are not reprocessed.
- The map projection metadata labels every tile as northern
  hemisphere, HLS keeping southern y coordinates negative
  ([the tile gotcha](../gotchas/hls-mgrs-tile-overlap.md)).
- In rare cases an orbit's Level-1C geolocation is significantly off;
  ESA deletes the data on discovery but the S30 built from it stays
  until users report it.
- The UTC date in the file name can be the day before the local date
  over eastern Australia and New Zealand, and on such days the
  atmospheric ancillary data can be from the day before.
- Resolved in forward processing only, not in the archive: the ESA
  image quality mask for packet loss is applied since June 2025 (any
  affected band sets every band of the pixel to fill); atmospheric
  correction at swath edges and at the join of two partial granules
  runs only where every band has data since March 2025.

The podaac bundle's OPERA DSWx-HLS surface water concept
(`knowledge/podaac/datasets/opera-dswx-hls.md`) derives from this
product and L30 and is named here rather than restated.

[^s30-page]: LP DAAC product page, HLSS30 v2.0, read 2026-09-14
[^user-guide]: HLS Product User Guide, product version 2.0, April 2026
[^s30-known-issues]: HLS S30 V2.0 Known Issues, April 2026
[^hls-s30-page]: HLS project site, S30 product description
[^hls-products]: HLS project site, Product Description
[^hls-algorithms]: HLS project site, Algorithms page
[^cmr-s30]: CMR collection record C2021957295-LPCLOUD, read 2026-09-14
[^claverie-2018]: Claverie and others 2018, Remote Sensing of Environment 219, doi:10.1016/j.rse.2018.09.002, cited on its Crossref record
[^claverie-2018-crossref]: Crossref record for 10.1016/j.rse.2018.09.002, read 2026-09-14
[^l30]: this bundle's HLS L30 concept
