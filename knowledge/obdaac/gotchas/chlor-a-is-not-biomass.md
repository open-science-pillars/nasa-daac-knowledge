---
type: dataset-gotcha
spheres: [biosphere, hydrosphere]
title: "chlor_a is a near-surface pigment concentration that the producer calls a proxy for phytoplankton biomass: it is not biomass, not carbon and not primary production, which the same producer distributes as separate products with their own algorithms"
description: "The chlorophyll-a product is the near-surface concentration of one photosynthetic pigment in mg per cubic metre, retrieved empirically from the color of the sunlit layer, and the ATBD and the collection descriptions call it a proxy metric for phytoplankton biomass. The producer distributes phytoplankton carbon (carbon_phyto) in the same PACE BGC file from a different algorithm, and net primary production as a separate Level 4 product computed from the inherent optical properties and PAR rather than from chlorophyll; the color index component of the retrieval was chosen partly because it tolerates changes in the chlorophyll-specific backscattering, which is the ratio between pigment and particles varying. A chlorophyll map read as a biomass, carbon or productivity map, or a chlorophyll trend read as a change in production or in the standing stock of the water column, carries the varying pigment-to-carbon relation and the surface-only view as if they were the quantity named."
tags: [chlorophyll, chlor_a, biomass, phytoplankton-carbon, carbon_phyto, primary-production, npp, proxy, near-surface, modis, aqua, pace, oci, obdaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:30:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-14T12:17:15Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/147 }
severity: medium
dataset: ../datasets/pace-oci-l3-chlorophyll.md
status: stable
stale_after: 2027-03-14
sources:
  - id: atbd
    resource: https://oceancolor.gsfc.nasa.gov/files/atbd/atbd-obdaac-chlorophyll-a.pdf
    title: "Chlorophyll a, Algorithm Theoretical Basis Document version 1.1, 6 November 2023, read in full 2026-09-14: the abstract and plain-language summary defining the product as the near-surface concentration of the photosynthetic pigment chlorophyll a in the sunlit layer, calculated from empirical relationships between in situ chlorophyll and reflectance, which can in turn be used as a proxy metric for phytoplankton biomass"
  - id: cmr-pace
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C4184125847-OB_CLOUD.umm_json
    title: "CMR collection record for PACE_OCI_L3M_BGC version 3.2 (read 2026-09-14): the abstract describing CHL as a proxy for phytoplankton biomass, POC as surface carbon stocks, PIC as calcite from coccolithophores and CARBON as phytoplankton carbon concentration, each as a separate product of the suite; the MODISA_L3m_CHL record (C3380709133-OB_CLOUD) carries the same proxy sentence"
  - id: pace-file
    resource: https://oceandata.sci.gsfc.nasa.gov/opendap/PACE_OCI/L3SMI/2024/0601/PACE_OCI.20240601_20240630.L3m.MO.BGC.V3_2.4km.nc.das
    title: "The attribute listing (OPeNDAP .das, metadata only) of the June 2024 PACE OCI monthly 4 km BGC file, read 2026-09-14: chlor_a (Chlorophyll Concentration, OCI Algorithm), carbon_phyto (Phytoplankton Carbon, with a reference attribute citing Graff and others 2015 on analytical phytoplankton carbon measurements), poc (Stramski 2022 hybrid) and pic (CI2 algorithm, Mitchell and others 2017) as four variables with four references in one file"
  - id: pace-v3-notes
    resource: https://oceancolor.gsfc.nasa.gov/files/reprocessing/PACE_OCI_V3_Release_Notes.pdf
    title: "PACE OCI V3 Processing Notes, April 2026, read in full 2026-09-14: the OC_BGC suite listing chlor_a, carbon_phyto, poc and pic as separate provisional products, and NPP_CAFE, net primary production from the CAFE model, as a Level 4 product only, derived from the Level 3 IOP and PAR products with other model input"
  - id: hu-2012
    resource: https://doi.org/10.1029/2011JC007395
    title: "Hu, Lee and Franz, 2012, Chlorophyll a algorithms for oligotrophic oceans, a novel approach based on three-band reflectance difference, Journal of Geophysical Research: Oceans 117, C01011 (registry record verified on Crossref and abstract read there 2026-09-14; the article was not read): the color index more tolerant than the band ratio to changes in the chlorophyll-specific backscattering coefficient and performing similarly for different relative contributions of non-phytoplankton absorption"
  - id: dataset
    resource: ../datasets/pace-oci-l3-chlorophyll.md
    title: "This bundle's PACE OCI Level 3 chlorophyll-a dataset concept, whose file holds the carbon products beside chlor_a; the MODIS-Aqua dataset concept carries the same algorithm's chlor_a alone"
---

# chlor_a is a pigment concentration, not biomass, carbon or production

**Mechanism.** The product is defined by its producer as the
near-surface concentration of the photosynthetic pigment chlorophyll
a, in mg per cubic metre, found within phytoplankton in the sunlit
layer, calculated from empirical relationships between in situ
chlorophyll and spectral reflectance, and the ATBD adds that this
concentration can in turn be used as a proxy metric for phytoplankton
biomass; the collection descriptions of both the MODIS-Aqua and the
PACE products repeat the proxy wording.[^atbd][^cmr-pace] Three
things follow from the definition. It is a pigment, and the amount of
pigment per cell or per unit of carbon is not fixed: the color index
component of the retrieval was chosen for low-chlorophyll water partly
because it is more tolerant than the band ratio to changes in the
chlorophyll-specific backscattering coefficient, which is the
producer's own acknowledgment that the relation between pigment and
particles varies across the water the algorithm sees.[^hu-2012] It
is near-surface: the retrieval comes from the light leaving the
sunlit layer, so it says nothing directly about the column below
it.[^atbd] And it is one of several quantities the producer retrieves
separately: the PACE BGC file holds `chlor_a`, `carbon_phyto`
("Phytoplankton Carbon", referencing analytical phytoplankton carbon
measurements), `poc` (particulate organic carbon from a 2022 hybrid
algorithm) and `pic` (calcite from a reflectance-difference algorithm)
as four variables with four references, the processing notes list
them as separate provisional products, and net primary production is
a Level 4 product from the CAFE model computed from the inherent
optical properties and PAR, not from chlorophyll, listed as a
separate product with its own status.[^pace-file][^pace-v3-notes]

**Wrong-result mode.** A chlorophyll map presented as a map of
phytoplankton biomass or carbon substitutes a pigment for a mass and
carries the varying pigment-to-carbon relation into the result as if
it were spatial structure in the stock; a chlorophyll trend reported
as a trend in production or in biomass carries any change in that
relation (with light, season or community) as if it were a change in
the quantity named. A column-integrated quantity (standing stock,
export) built from the surface value alone assigns the surface
concentration to depths the sensor does not see.[^atbd] A comparison
of the standard chlorophyll with a carbon or productivity product, or
a model's carbon field, that treats them as the same variable in
different units compares two retrievals of different quantities by
different algorithms.[^pace-file][^pace-v3-notes]

**Correct approach.** A statement about biomass or carbon from the
PACE record names the carbon product (`carbon_phyto` or `poc`) and
its algorithm; a statement about production names the Level 4
NPP_CAFE product and its inputs; a statement about chlorophyll names
chlorophyll, as the near-surface pigment concentration it is, and,
where it stands in for biomass, says so as the producer does, as a
proxy, with the varying pigment-to-carbon relation among the
uncertainties.[^atbd][^cmr-pace][^pace-file][^pace-v3-notes] What
chlor_a therefore is: the near-surface concentration of one pigment,
retrieved from color, and a proxy for everything else it is used to
stand for.[^dataset][^atbd]

**Verification.** The ATBD's abstract, plain-language summary and
introduction were read in full on 2026-09-14 and define the product
and the proxy relation in the producer's words; the two collection
records read the same day repeat them; the PACE file listing read the
same day through OPeNDAP shows the four separate variables and their
references; the processing notes read the same day list the BGC
products and the Level 4 production product with their derivation;
the Hu 2012 abstract, read on the Crossref registry record, states
the tolerance to changes in the chlorophyll-specific
backscattering.[^atbd][^cmr-pace][^pace-file][^pace-v3-notes][^hu-2012]
No source read states a numerical chlorophyll-to-carbon ratio or its
range, and this concept quotes none.

[^atbd]: Chlorophyll a ATBD version 1.1, OB.DAAC, 6 November 2023
[^cmr-pace]: CMR collection records, C4184125847-OB_CLOUD and C3380709133-OB_CLOUD
[^pace-file]: Attribute listing of the June 2024 PACE OCI monthly 4 km BGC file, read through OPeNDAP on 2026-09-14
[^pace-v3-notes]: PACE OCI V3 Processing Notes, April 2026
[^hu-2012]: Hu, Lee and Franz, 2012, Journal of Geophysical Research: Oceans, doi:10.1029/2011JC007395
[^dataset]: This bundle's PACE OCI Level 3 chlorophyll-a dataset concept
