---
type: dataset-gotcha
spheres: [geosphere, biosphere]
title: "MOD11 Emis_31 and Emis_32 are assigned from land cover class, not retrieved: they change only when the class, the snow cover or the arid-zone adjustment changes, and they are the emissivity the temperature retrieval assumed"
description: "The band 31 and 32 emissivity layers in MOD11A1 and MOD11A2 come from the classification-based emissivity method: a look-up by land cover type from the MODIS land cover product and the daily snow cover, with a Collection 6 adjustment of up to 0.0063 in arid and semi-arid areas. They are inputs the generalized split-window algorithm needed to retrieve the temperature, stored as uint8 with a scale of 0.002 and an offset of 0.49, and the swath product's quality byte labels them inferred from land cover type. Retrieved emissivities exist in the 6 km MOD11B1 product from the day/night algorithm, not here. A script that reads Emis_31 as a measured surface property, differences it between dates as a change in the surface, or uses it to validate an emissivity retrieval, is reading a classification."
tags: [mod11, mod11a1, mod11a2, modis, terra, emissivity, land-cover, classification, split-window, lpdaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T13:40:00Z }
severity: low
dataset: ../datasets/mod11-land-surface-temperature.md
status: draft
stale_after: 2027-03-15
sources:
  - id: user-guide
    resource: https://lpdaac.usgs.gov/documents/715/MOD11_User_Guide_V61.pdf
    title: "Collection-6 MODIS LST Products Users' Guide (Wan, June 2019) with the Collection 6.1 cover note, read 2026-09-15: section 2.1 (emissivity in bands 31 and 32 estimated by the classification-based method from the land cover and snow inputs of Table 2, the arid-zone adjustment of up to 0.0063), Table 8 (the swath QC emissivity flag, 00 inferred from land cover type), Table 9 and Table 14 (Emis_31 and Emis_32 as uint8, scale 0.002, offset 0.49, fill 0), Table 13 (the emissivity error classes) and section 5 (retrieved emissivities in MOD11B1 from the day/night algorithm)"
  - id: atbd
    resource: https://lpdaac.usgs.gov/documents/119/MOD11_ATBD.pdf
    title: "MODIS LST Algorithm Theoretical Basis Document, version 3.3, April 1999 (Wan), read 2026-09-15: section 3.1.1.1, the classification-based emissivity look-up table derived from land cover types and dynamic and seasonal factors used in the generalized split-window algorithm, and land cover, snow and vegetation index used to infer band average emissivities; section 3.1.5.3, the emissivity knowledge base uncertainty of about 0.005 for most land cover types; section 2.1, the 0.02 specification for bands 29, 31 and 32"
  - id: a1-page
    resource: https://lpdaac.usgs.gov/products/mod11a1v061/
    title: "LP DAAC product page for MOD11A1 v061, read 2026-09-15: bands 31 and 32 emissivities from land cover types; the variables table with Emis_31 and Emis_32"
  - id: a2-page
    resource: https://lpdaac.usgs.gov/products/mod11a2v061/
    title: "LP DAAC product page for MOD11A2 v061, read 2026-09-15: the same statement and layers on the eight-day product"
  - id: mod11
    resource: ../datasets/mod11-land-surface-temperature.md
    title: "This bundle's MOD11 concept, with the layer table and the uncertainty statement"
---

# MOD11 Emis_31 and Emis_32 are assigned from land cover class

**Mechanism.** The generalized split-window algorithm that produces
the MOD11 temperature needs the band 31 and 32 emissivities as inputs,
and the guide says where they come from: they are estimated by the
classification-based emissivity method (Snyder and others 1998)
according to the land cover types in the pixel, determined from the
MODIS land cover product MCDLC1KM and the daily snow cover product
MOD10_L2, both listed among the algorithm's inputs.[^user-guide] The
algorithm document describes the same design: a classification-based
emissivity look-up table derived from land cover types and dynamic and
seasonal factors, with the land cover, snow and vegetation index
products used to infer band average emissivities, so that a pixel of
dense evergreen canopy, lake surface or snow takes the knowledge base
value for its class.[^atbd] The product pages say it in five words,
emissivities from land cover types.[^a1-page][^a2-page] The swath
product's quality byte has a two-bit emissivity flag whose value 00
reads inferred from land cover type and 01 MODIS retrieved; the daily
and eight-day tiles do not carry that flag, only the emissivity error
classes.[^user-guide]

Collection 6 added one departure from the pure look-up: because the
classified values carry a large uncertainty in semi-arid and arid
areas, a prototype adjustment compares the observed band 31 minus
band 32 brightness temperature difference with a simulated one and
moves the band 31 emissivity by up to 0.0063 and the band 32
emissivity by the same amount the other way.[^user-guide] Retrieved
emissivities do exist in the MOD11 family, in the 6 km MOD11B1
product, where the day/night algorithm solves for emissivity in seven
bands from paired daytime and nighttime observations; that is a
different product with its own constraints.[^user-guide] The layers
are stored as uint8 with a scale of 0.002 and an offset of 0.49, so
the representable values run from 0.492 to 1.0 in steps of 0.002, with
0 as fill.[^user-guide][^a1-page]

**Wrong-result mode.** A script that treats Emis_31 as a measured
surface emissivity reads the land cover map through a look-up table.
A difference of the layer between two dates shows change where the
land cover class, the snow cover or the arid-zone adjustment changed
and nothing elsewhere, so a map of emissivity change is a map of
classification change. A study that uses the layer to validate an
emissivity retrieval from another sensor compares the retrieval with
an assumption. A correlation of Emis_31 with vegetation or soil
moisture recovers the class boundaries. And since the temperature was
retrieved with these values as inputs, an error in the class is
already inside the temperature: the algorithm document's 1 K accuracy
holds for land cover types with known emissivities, and the guide's
own reason for the arid-zone adjustment is that the classified values
are least certain where bare soil dominates.[^atbd][^user-guide] None
of this fails, because the layer is a valid raster of values inside
the representable range of 0.492 to 1.0.[^user-guide]

**Correct approach.** The two layers are read as the emissivity the
retrieval assumed for the pixel's class on that day, useful for
reconstructing the surface-leaving radiance the algorithm saw or for
knowing which class a pixel was taken to be, and not as an
observation of the surface. The emissivity error class in bits 4 and
5 of QC_Day and QC_Night is the product's own statement of how far
the assumption may be off. Where a retrieved emissivity is the
quantity wanted, the MOD11B1 product or another retrieval is the
source.[^user-guide][^mod11]

**Verification.** A histogram of Emis_31 over a tile is a small set
of discrete values, one or a few per land cover class, rather than a
continuum, and a time series of the layer at one cell is flat between
changes of class or snow cover apart from the arid-zone
adjustment.[^user-guide][^atbd] The spatial pattern of the layer
follows the boundaries of the land cover map the guide names as its
input.[^user-guide]

[^user-guide]: Collection-6 MODIS LST Products Users' Guide, June 2019, section 2.1, Tables 2, 8, 9, 13 and 14, section 5
[^atbd]: MODIS LST Algorithm Theoretical Basis Document, version 3.3, April 1999, sections 2.1, 3.1.1.1 and 3.1.5.3
[^a1-page]: LP DAAC product page, MOD11A1 v061, read 2026-09-15
[^a2-page]: LP DAAC product page, MOD11A2 v061, read 2026-09-15
[^mod11]: this bundle's MOD11 concept
