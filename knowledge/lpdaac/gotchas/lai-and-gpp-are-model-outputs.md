---
type: dataset-gotcha
spheres: [biosphere, geosphere]
title: "MOD15 LAI and FPAR and MOD17 GPP and NPP are model outputs, not measurements: a look-up table inversion by biome and a light use efficiency model with fixed biome parameters and reanalysis weather, each with a quality layer that says which algorithm path or which filled input produced the value, and with land cover codes stored inside the data type above the valid range"
description: "MOD15A2H LAI and FPAR are the mean of the radiative transfer solutions consistent with the pixel's red and near-infrared reflectance for its assigned biome, or a regression on NDVI when no solution is found, and the guide states that the algorithm runs irrespective of input quality and that the SCF_QC path in FparLai_QC is the key quality indicator. MOD17A2H GPP is that FPAR times 0.45 times reanalysis shortwave radiation times a biome light use efficiency ramped by reanalysis temperature and vapour pressure deficit, with contaminated FPAR and LAI replaced by a five-year climatology since Collection 6.1, and its quality byte is the MOD15 byte passed through; MOD17A3HGF recomputes the year with LAI and FPAR interpolated across periods that failed their quality label and reports the share of growing-season days so filled as Npp_QC_500m. Pixels without a retrieval hold land cover codes (249 to 255, 32761 to 32767, 65529 to 65535) that lie inside the data type above the valid range; the MOD17 guide states that the file attribute names one fill value while seven exist, the product pages render one, and the CMR variable records list all seven. A script that scales these bytes, averages an LAI series without the path flag, uses MOD17 GPP as an independent check on a model driven by the same weather or FPAR, or reads an eight-day anomaly where the climatology was substituted reports the model and its fills as the land surface."
tags: [mod15, mod15a2h, mod17, mod17a2h, mod17a3hgf, modis, lai, fpar, gpp, npp, quality, fill-value, model-output, lpdaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T17:50:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-15T18:34:53Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/172 }
severity: medium
dataset: ../datasets/mod15-lai-fpar.md
status: stable
stale_after: 2027-03-15
sources:
  - id: lai-guide
    resource: https://lpdaac.usgs.gov/documents/926/MOD15_User_Guide_V61.pdf
    title: "MODIS Collection 6.1 LAI/FPAR Product User's Guide, April 2020, read 2026-09-15: section 3 (the look-up table inversion, the acceptable solutions and their mean and dispersion, saturation flagged, the backup on NDVI, the algorithm path as a key quality indicator), section 6.1 (the algorithm is executed irrespective of input quality; the quality layers select reliable retrievals; SCF_QC is the key indicator; the worked example of the byte 64), Table 4 (uint8 layers, valid range 0 to 100, fills 249 to 255 and 248 to 255), Table 5 (the FparLai_QC bits) and Tables 6 and 7 (the land cover meaning of 249 to 255 and 248 for backup pixels)"
  - id: gpp-guide
    resource: https://lpdaac.usgs.gov/documents/972/MOD17_User_Guide_V61.pdf
    title: "MOD17 User's Guide for Collection 6.1, March 2021, read 2026-09-15: sections 1.3 (GPP as light use efficiency times APAR, the temperature and vapour pressure deficit ramps, the eight-day sums with 46 periods and a short last period), 2.1 and 2.2 (the land cover dependence at 65 to 80 per cent accuracy and the fixed BPLUT as arguably the most significant assumption), 2.3 (leaf area held constant within each period), 2.4 (the Collection 6.1 climatology backup, its bias, the year-end gap filling by linear interpolation, the caution for the first mission years), 2.5 (the reanalysis, larger uncertainty in the tropics), 4.1 (Table 4.1, the seven fill codes 32761 to 32767, Psn_QC_500m inheriting FparLai_QC, exclude cloud-contaminated cells in MOD17A2H, ignore the quality layer of the gap-filled products but use the valid range) and 4.2 (Table 4.2, the codes 65529 to 65535 and 249 to 255, Npp_QC_500m as a percentage)"
  - id: mod15-page
    resource: https://lpdaac.usgs.gov/products/mod15a2hv061/
    title: "LP DAAC product page for MOD15A2H v061, read 2026-09-15: the variables table naming 249 as the fill of Fpar_500m and Lai_500m and 248 as the fill of the standard deviation layers"
  - id: a2h-page
    resource: https://lpdaac.usgs.gov/products/mod17a2hv061/
    title: "LP DAAC product page for MOD17A2H v061, read 2026-09-15: the variables table naming 32761 as the fill of Gpp_500m and PsnNet_500m, the temporal extent 2021-01-01 to present, and the version description naming the climatology backup"
  - id: a3hgf-page
    resource: https://lpdaac.usgs.gov/products/mod17a3hgfv061/
    title: "LP DAAC product page for MOD17A3HGF v061, read 2026-09-15: the variables table naming 65529, 32761 and 249 as the fills, and the description of the year-end gap filling by quality label and linear interpolation"
  - id: cmr-vars-15
    resource: https://cmr.earthdata.nasa.gov/search/variables.umm_json?concept_id[]=V3144112793-LPCLOUD&concept_id[]=V3144112802-LPCLOUD&concept_id[]=V3144112836-LPCLOUD&concept_id[]=V3144112838-LPCLOUD&concept_id[]=V3144112811-LPCLOUD&concept_id[]=V3144112833-LPCLOUD
    title: "CMR variable records associated with the MOD15A2H v061 collection (V3144112793, V3144112802, V3144112836, V3144112838, V3144112811 and V3144112833, all LPCLOUD, revisions of August 2024), read 2026-09-15: Fpar_500m and Lai_500m carry the seven science fill values 249 to 255 with their land cover descriptions, the two standard deviation layers 248 to 255 with 248 as the backup method code, and the two quality bytes 255"
  - id: cmr-vars-17
    resource: https://cmr.earthdata.nasa.gov/search/variables.umm_json?concept_id[]=V3151335752-LPCLOUD&concept_id[]=V3151335789-LPCLOUD&concept_id[]=V3151335815-LPCLOUD&concept_id[]=V3151347144-LPCLOUD&concept_id[]=V3151347163-LPCLOUD&concept_id[]=V3151347206-LPCLOUD
    title: "CMR variable records associated with the MOD17A2H and MOD17A3HGF v061 collections (V3151335752, V3151335789, V3151335815, V3151347144, V3151347163 and V3151347206, all LPCLOUD, revisions of August 2024), read 2026-09-15: Gpp_500m, PsnNet_500m and Npp_500m carry the seven science fill values 32761 to 32767, the annual Gpp_500m 65529 to 65535 and Npp_QC_500m 249 to 255, each with its land cover description"
  - id: mod15
    resource: ../datasets/mod15-lai-fpar.md
    title: "This bundle's MOD15 concept, with the retrieval, the layer table, the fill legend and the quality bits"
  - id: mod17
    resource: ../datasets/mod17-gpp-npp.md
    title: "This bundle's MOD17 concept, with the model, its inputs, the layer table, the fill codes and the two quality layers"
  - id: index-gotcha
    resource: index-is-not-a-state-variable.md
    title: "This bundle's gotcha on the indices, which the MOD15 backup path regresses on"
---

# LAI and GPP are model outputs

**Mechanism.** Three of the layers a land carbon analysis reaches for
first, MOD15 leaf area index and FPAR and MOD17 GPP and NPP, are
outputs of models run on every land pixel whether or not the inputs
were good, and each file says so in a quality layer rather than in the
value. The MOD15 guide describes the retrieval: for each pixel the
main algorithm compares the observed red and near-infrared
reflectances with a look-up table of radiative transfer solutions for
the biome type the land cover product assigns, takes every canopy and
soil pattern within the assumed reflectance uncertainty as an
acceptable solution, and reports the mean of those solutions as the
LAI and FPAR and their dispersion as the standard deviation layers;
in dense canopies the reflectances saturate, the dispersion is large
and the retrieval is flagged; when no solution is found, a backup
regression on NDVI is used and the standard deviation layers hold
248.[^lai-guide] The guide states that the algorithm is executed
irrespective of input quality, that the quality layers are therefore
the means of selecting reliable retrievals, and that the SCF_QC field
in bits 5 to 7 of FparLai_QC, the algorithm path, is the key
indicator: 000 main method without saturation, 001 main method with
saturation, 010 and 011 the backup after a failure of geometry or of
something else, 100 not produced. Its worked example is the byte 64,
binary 01000000, a pixel whose bits 5 to 7 read 010, the backup after
a geometry failure, with every other bit zero ([this bundle's MOD15
concept](../datasets/mod15-lai-fpar.md)).[^lai-guide][^mod15]

MOD17 runs a second model on that output. Daily GPP is a biome
maximum light use efficiency, ramped down by the day's minimum
temperature and daytime vapour pressure deficit from the GMAO
reanalysis, times the MOD15 FPAR times 0.45 times the reanalysis
shortwave radiation; net photosynthesis subtracts leaf and fine root
maintenance respiration computed from the MOD15 LAI and the biome's
specific leaf area; the eight-day file holds the sums.[^gpp-guide] The
biome parameters come from one look-up table column per land cover
class, invariant in space and time, which the guide calls arguably
the most significant assumption in the logic, on a land cover map it
states to be 65 to 80 per cent accurate; the reanalysis is coarse and
interpolated, with larger errors in the tropics; and leaf area is
held constant within each eight-day period because the input is
composited.[^gpp-guide] Since Collection 6.1, where the MOD15A2H FPAR
and LAI are contaminated, the operational eight-day product
substitutes a five-year climatology of the best values for that
period, which the guide says raises GPP most where cloud is frequent
and can bias the result because it smooths out interannual
variability, disturbance and recovery.[^gpp-guide][^a2h-page] The
year-end gap-filled products instead remove the periods whose MOD15
quality label fails, interpolate LAI and FPAR linearly between the
passing neighbours and recompute the year; the guide notes that some
periods have low values with good labels and that the label is
nonetheless the only quality control there is, and that the first
mission year was filled from a start in late February.[^gpp-guide][^a3hgf-page]
The quality layers follow the same logic: Psn_QC_500m on the
eight-day product is the MOD15 FparLai_QC byte passed through, so it
describes the FPAR input's path and cloud state, not the GPP; and
Npp_QC_500m on the annual product is not a bit field but the
percentage of growing-season days on which filled inputs were used,
expected to be high in humid forests ([this bundle's MOD17
concept](../datasets/mod17-gpp-npp.md)).[^gpp-guide][^mod17]

The fills are numbers. On MOD15 the LAI and FPAR bytes hold 255 for
fill proper and 254 to 249 for water, barren, snow and ice, wetland,
urban and unclassified land cover, all inside the uint8 range above
the valid 0 to 100; on MOD17 the int16 layers hold 32767 and 32766 to
32761 in the same order, the uint16 annual GPP 65535 to 65529 and the
uint8 quality layer 255 to 249, again above the valid ranges. The
MOD17 guide states the trap directly: the file attributes list one
fill value while seven exist. The product pages render one value per
layer as the fill, 249, 248, 32761, 65529, the lowest code of each
range, and the CMR variable records for the collections, from which
the catalog's layer tables come, list all seven codes with their land
cover meanings.[^lai-guide][^gpp-guide][^mod15-page][^a2h-page][^a3hgf-page][^cmr-vars-15][^cmr-vars-17]

**Wrong-result mode.** A script that scales before it screens turns
the codes into data: an urban pixel's 250 becomes an LAI of 25.0 and
an FPAR of 2.5, a water pixel's 32766 becomes 3.28 kg C per square
metre in eight days, and a mean over a tile that includes a coast or
a city is pulled by exactly the pixels the model did not run on; a
script that masks only the file attribute's fill, or the one value the
product page renders, keeps the six other codes the guide and the CMR
variable records list.[^lai-guide][^gpp-guide][^mod15-page][^cmr-vars-15][^cmr-vars-17] A mean or trend of LAI
over evergreen broadleaf forest that ignores the path flag averages
retrievals whose dispersion the guide calls large under saturation
with backup values regressed on an index that has itself stopped
responding, and reports the result as a canopy change ([the index
gotcha](index-is-not-a-state-variable.md)).[^lai-guide][^index-gotcha]
A study that uses MOD17 GPP to validate a land surface model driven by
the same GMAO reanalysis, the same land cover map or the same MOD15
FPAR compares the model with a second run of shared inputs and calls
the agreement independent confirmation. An interannual anomaly of
eight-day GPP in a cloudy region reads, where the climatology was
substituted, as an anomaly of the five-year mean rather than of the
year, and the substitution is not marked in the value.[^gpp-guide] A
daily rate obtained by dividing every eight-day sum by eight is wrong
for the last period of each year, which holds five or six
days.[^gpp-guide] A request for the operational eight-day product
before 2021 finds no Collection 6.1 files, because that record begins
2021-01-01 and the earlier years are in the gap-filled eight-day
collection.[^a2h-page] None of this raises an error: every code is a
valid integer, the quality byte is a separate layer, and a GPP map
looks like a measurement.[^lai-guide][^gpp-guide]

**Correct approach.** The valid range is the test that separates data
from code, applied to the stored integer before scaling: 0 to 100 on
the MOD15 bytes, 0 to 30000 and -30000 to 30000 on the eight-day
int16 layers, 0 to 65500 and -30000 to 32700 on the annual layers,
with everything above kept as the land cover class it
encodes.[^lai-guide][^gpp-guide] An LAI or FPAR series carries its
SCF_QC path, with the main algorithm without saturation as the
reference class, saturated retrievals marked as such, backup pixels
either excluded or labelled, and the standard deviation layers read
where they exist.[^lai-guide] The eight-day GPP is used with
cloud-contaminated cells excluded by the inherited cloud state, as
the guide suggests, and the annual or complete record is taken from
the gap-filled products, whose quality layer is read as a fraction of
filled days rather than as bits; a model comparison states which
inputs the two sides share.[^gpp-guide] An analysis of interannual
variability in a cloudy region is stated to rest on a product in
which contaminated periods carry a climatology, and the year-end
product is preferred for it.[^gpp-guide][^mod17]

**Verification.** On any MOD15A2H tile that includes water or a city,
a histogram of the raw Lai_500m byte shows a cluster at 249 to 255
above the valid maximum of 100, and the raw FparLai_QC byte decoded by
bits 5 to 7 shows the share of pixels on each algorithm path, with
248 in LaiStdDev_500m wherever that share is the backup.[^lai-guide]
On a MOD17A2H tile the raw Gpp_500m holds values at 32761 to 32767
above the valid maximum of 30000 in the same non-vegetated pixels. For
a tile in a cloudy region, the same year's MOD17A2H sum and the
gap-filled eight-day and annual products differ where the MOD15
quality label failed, and Npp_QC_500m on the annual file is high over
the humid forest and low over dry grassland, as the guide
expects.[^gpp-guide]

[^lai-guide]: MODIS Collection 6.1 LAI/FPAR Product User's Guide, April 2020, sections 3 and 6.1, Tables 4 to 7
[^gpp-guide]: MOD17 User's Guide for Collection 6.1, March 2021, sections 1.3, 2.1 to 2.5, 4.1 and 4.2
[^mod15-page]: LP DAAC product page, MOD15A2H v061, read 2026-09-15
[^cmr-vars-15]: CMR variable records for the MOD15A2H v061 collection, read 2026-09-15
[^cmr-vars-17]: CMR variable records for the MOD17A2H and MOD17A3HGF v061 collections, read 2026-09-15
[^a2h-page]: LP DAAC product page, MOD17A2H v061, read 2026-09-15
[^a3hgf-page]: LP DAAC product page, MOD17A3HGF v061, read 2026-09-15
[^mod15]: this bundle's MOD15 concept
[^mod17]: this bundle's MOD17 concept
[^index-gotcha]: this bundle's gotcha on indices as empirical measures
