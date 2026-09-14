---
type: dataset-gotcha
spheres: [biosphere, geosphere]
title: "HLS reflectance is harmonized, not native: a nadir BRDF adjustment on both products and a bandpass adjustment on S30 make it differ from Landsat Collection 2 and Sentinel-2 surface reflectance"
description: "HLS L30 and S30 are nadir BRDF-adjusted reflectance: every reflective band except the cirrus and water vapour bands is normalized with a global set of MODIS-derived c-factor coefficients to a zero view zenith and to a solar zenith that is the mean of the Landsat and Sentinel-2 overpass values at the tile centre for the day. S30 is then adjusted in its seven OLI-equivalent bands by a per-satellite linear fit to the OLI bandpasses, leaving the red-edge, broad NIR, water vapour and cirrus bands as original MSI. So HLS is not the USGS Collection 2 surface reflectance and not the ESA Level-2A product, a comparison against either measures the adjustments, and the residual after adjustment is under 2 per cent with a standard deviation under 0.005 reflectance units, which a study of changes at that scale has to carry."
tags: [hls, hlsl30, hlss30, nbar, brdf, bandpass, c-factor, harmonization, lpdaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:40:00Z }
severity: medium
dataset: ../datasets/hls-s30.md
status: draft
stale_after: 2027-03-14
sources:
  - id: user-guide
    resource: https://lpdaac.usgs.gov/documents/1698/HLS_User_Guide_V2.pdf
    title: "HLS Product User Guide, product version 2.0, April 2026, read in full 2026-09-14: section 2 (what changed in the BRDF adjustment), Table 2 (which bands are BRDF and bandpass adjusted), section 4.4 with Table 4 (the c-factor method, the coefficients, the solar zenith rule), section 4.5 with Table 5 (the bandpass fit and its residual), section 6.3 (the angle layers exist so a user can do the correction differently), Table 11 (NBAR_SOLAR_ZENITH and the per-band slope and offset in the metadata)"
  - id: hls-algorithms
    resource: https://hls.gsfc.nasa.gov/algorithms/
    title: "HLS project site, Algorithms page, read 2026-09-14: the six-part definition of harmonized, the BRDF normalization section with Table 1, the bandpass adjustment section with Table 2, and the statement that L30 is the NBAR and S30 is the bandpass-adjusted NBAR"
  - id: hls-products
    resource: https://hls.gsfc.nasa.gov/products-description/
    title: "HLS project site, Product Description, read 2026-09-14: S30 spectral content is OLI-like except NIR B08 and the red-edge bands"
  - id: hls-s30-page
    resource: https://hls.gsfc.nasa.gov/products-description/s30/
    title: "HLS project site, S30 product description, read 2026-09-14: the layer table's bandpass and BRDF adjustment columns"
  - id: claverie-2018
    resource: https://doi.org/10.1016/j.rse.2018.09.002
    title: "Claverie, Ju, Masek, Dungan, Vermote, Roger, Skakun and Justice (2018), The Harmonized Landsat and Sentinel-2 surface reflectance data set, Remote Sensing of Environment 219, 145 to 161: the source the guide cites for the under 2 per cent and under 0.005 residual; the publisher page sits behind a bot check, so the paper is cited on its registry record"
  - id: claverie-2018-crossref
    resource: https://api.crossref.org/works/10.1016/j.rse.2018.09.002
    title: "Crossref record for 10.1016/j.rse.2018.09.002, read 2026-09-14: title, the eight authors, journal, volume, pages and year verified"
  - id: l30-known-issues
    resource: https://lpdaac.usgs.gov/documents/2434/HLS_v2.0_L30_known_issues_April2026.pdf
    title: "HLS L30 v2.0 Known Issues, April 2026, read 2026-09-14: issue 4, Landsat and Sentinel-2 snow reflectance remain highly inconsistent after harmonization"
  - id: l30
    resource: ../datasets/hls-l30.md
    title: "This bundle's HLS L30 concept: L30 is the reference bandpass and carries the BRDF adjustment only"
  - id: s30
    resource: ../datasets/hls-s30.md
    title: "This bundle's HLS S30 concept: the layer table with its adjusted and unadjusted bands"
---

# HLS reflectance is harmonized, not native

**Mechanism.** Two adjustments sit between the LaSRC surface
reflectance and the HLS layers, and the project site names both in
its definition of harmonized: normalization to a nadir-view geometry
through a BRDF estimate, and spectral bandpass adjustment of one
sensor group to the other.[^hls-algorithms]

*The BRDF adjustment, on both products.* L30 and S30 are Nadir
BRDF-Adjusted Reflectance (NBAR). The c-factor method models the
surface with the Ross-Li kernels and one global set of constant
coefficients per band, derived from twelve months of the MODIS 500 m
BRDF product, and multiplies the observed reflectance by the ratio of
the modelled reflectance at the normalization angles to the modelled
reflectance at the observed angles.[^user-guide][^hls-algorithms] The
view zenith is set to zero for every pixel; the solar zenith is
adjusted only slightly, to the mean of the solar zenith angles at the
tile centre for the Landsat overpass and the Sentinel-2 overpass on
that day, one value for the whole tile, which differs from the
latitude-dependent constant of version 1.4.[^user-guide] The
coefficients are the MODIS ones for the bands with a MODIS equivalent
and, for the three Sentinel-2 red-edge bands, values interpolated
between the MODIS red and NIR bands.[^user-guide] The cirrus band of
both products and the water vapour band of S30 are not adjusted, and
the L30 thermal bands are brightness temperature, not reflectance at
all; the layer tables of this bundle's two dataset concepts mark the
adjusted and unadjusted bands.[^user-guide][^l30][^s30]

*The bandpass adjustment, on S30 only.* The OLI bandpasses are the
reference. The S30 NBAR in the seven bands with an OLI equivalent
(coastal aerosol, blue, green, red, NIR narrow, SWIR 1, SWIR 2) is
transformed by a linear slope and intercept fitted on 500 hyperspectral
spectra from 160 Hyperion scenes convolved with each sensor's spectral
response, with separate coefficients for Sentinel-2A, 2B and 2C; the
red-edge, broad NIR, water vapour and cirrus bands keep their MSI
response.[^user-guide][^hls-products][^hls-s30-page] The coefficients
are close to one and zero (the blue slope is 0.9778 for 2A and 2B and
0.9851 for 2C, with intercepts of a few thousandths), and the guide's
Table 5 and the project site's Table 2 list them all; the granule's
cmr.xml carries the applied slope and offset per band and the solar
zenith used for NBAR.[^user-guide][^hls-algorithms]

So the same Landsat scene yields different reflectance in the USGS
Collection 2 Level-2 product and in L30, and the same Sentinel-2
granule yields different reflectance in an ESA Level-2A product and in
S30, before any difference in atmospheric correction is counted.

**Wrong-result mode.** A comparison of HLS against the source
missions' own surface reflectance products reads the adjustments as
error: an L30 minus Collection 2 difference over a forward-scatter
view is the c-factor, and an S30 minus Level-2A difference in the blue
band is the bandpass slope. A physical retrieval calibrated on native
Landsat or Sentinel-2 reflectance, applied to HLS, has its inputs
moved by the same amounts. In the other direction, a study that treats
the two products as identical measurements reads the residual as
signal: after adjustment the spectral difference between MSI and OLI
bands is under 2 per cent with a residual standard deviation under
0.005 reflectance units, and a change detection whose threshold is
smaller than that finds a change at every date where the sensor
switches.[^user-guide][^claverie-2018][^claverie-2018-crossref] The
harmonization also does not reach everywhere: snow reflectance stays
highly inconsistent between the two products, Landsat generally higher
in the visible on same-day pairs, and the red-edge and broad NIR bands
of S30 are unadjusted MSI with no L30 counterpart.[^l30-known-issues][^hls-products]

**Correct approach.** HLS is its own reflectance product and is cited
as one; a comparison against Collection 2 or Level-2A states which
adjustments separate the two. A time series across L30 and S30 dates
carries the product per record and, for changes near the residual,
the 2 per cent and 0.005 figures beside the result.[^user-guide] A user
who needs a different angular normalization has the observed sun and
view angles in the four angle layers, which the guide says are
provided for exactly that case, and the NBAR solar zenith in the
metadata.[^user-guide] Analyses that use the red-edge or broad NIR
bands are S30-only analyses.

**Verification.** The granule's cmr.xml lists a nonzero
MSI_BAND_02_BANDPASS_ADJUSTMENT_SLOPE_AND_OFFSET on an S30 granule and
NBAR_SOLAR_ZENITH on both products; the observed mean solar zenith in
the SZA layer differs from NBAR_SOLAR_ZENITH, and the difference
between them is the solar part of the adjustment.[^user-guide]
Reversing the published slope and intercept on an S30 blue band
recovers the pre-adjustment NBAR to the rounding of the int16
scaling.[^user-guide]

[^user-guide]: HLS Product User Guide, product version 2.0, April 2026, sections 4.4, 4.5, 6.3, Tables 2, 4, 5 and 11
[^hls-algorithms]: HLS project site, Algorithms page
[^hls-products]: HLS project site, Product Description
[^hls-s30-page]: HLS project site, S30 product description
[^claverie-2018]: Claverie and others 2018, Remote Sensing of Environment 219, doi:10.1016/j.rse.2018.09.002, cited on its Crossref record
[^claverie-2018-crossref]: Crossref record for 10.1016/j.rse.2018.09.002, read 2026-09-14
[^l30-known-issues]: HLS L30 v2.0 Known Issues, April 2026, issue 4
[^l30]: this bundle's HLS L30 concept
[^s30]: this bundle's HLS S30 concept
