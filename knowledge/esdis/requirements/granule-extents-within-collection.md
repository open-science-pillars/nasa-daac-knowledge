---
type: requirement
title: Granule extents present and inside the collection's extents
description: "Granule temporal and spatial extents are recommended, not schema-required, in UMM-G; the wiki's CMR validation sections and the UMM-G requirements base state that an ingested granule's extents must lie within the collection's, and ARC reviews the containment with dated tolerances."
tags: [requirement, temporal, spatial, granule, consistency, metadata, cross-archive]
verified: { by: human:PaulMRamirez, at: 2026-09-14T12:12:43Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/142 }
status: stable
class: SHOULD
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:27:36Z }
stale_after: 2027-03-14
sources:
  - id: umm-g-schema
    resource: https://cdn.earthdata.nasa.gov/umm/granule/v1.6.6/umm-g-json-schema.json
    title: "UMM-G JSON schema v1.6.6: top-level required array, TemporalExtentType, SpatialExtentType"
  - id: umm-g-schema-167
    resource: https://cdn.earthdata.nasa.gov/umm/granule/v1.6.7/umm-g-json-schema.json
    title: "UMM-G JSON schema v1.6.7, top-level required array (the latest version the CMR ingest documentation accepts)"
  - id: umm-g-reqs
    resource: "https://wiki.earthdata.nasa.gov/download/attachments/49448405/EED3-TP-007_Rev04_UMM-G%20%281%29.pdf?api=v2"
    title: "ESDIS-SDS-REQ-0015, Revision D, Appendix C, Metadata Requirements Base Reference for UMM-G (the cover's own numbering; attached to the CMR wiki's UMM Documents page as EED3-TP-007_Rev04_UMM-G.pdf, approved 2026-07-16), sections C.2.7 Temporal Extent and C.2.8 Spatial Extent"
  - id: wiki-temporal-extents
    resource: https://wiki.earthdata.nasa.gov/spaces/CMR/pages/115937354/Temporal+Extents
    title: "CMR wiki, Temporal Extents (collection): best practices, CMR Validation and ARC priority matrix"
  - id: wiki-spatial-extent
    resource: https://wiki.earthdata.nasa.gov/spaces/CMR/pages/115936441/Spatial+Extent
    title: "CMR wiki, Spatial Extent (collection): best practices, CMR Validation and ARC priority matrix"
  - id: wiki-temporal-extent-granule
    resource: https://wiki.earthdata.nasa.gov/spaces/CMR/pages/382274521/Temporal+Extent+Granule
    title: "CMR wiki, Temporal Extent (Granule): element specification and ARC priority matrix"
  - id: wiki-spatial-extent-granule
    resource: https://wiki.earthdata.nasa.gov/spaces/CMR/pages/391316263/Spatial+Extent+Granule
    title: "CMR wiki, Spatial Extent (Granule): best practices and ARC priority matrix"
  - id: cmr-ingest-api
    resource: https://cmr.earthdata.nasa.gov/ingest/site/docs/ingest/api.html
    title: "CMR Ingest API documentation: validation sections and the list of latest acceptable UMM schema versions"
---

# Granule extents present and inside the collection's extents

A granule record states when and where its data were acquired, and
both extents lie inside the extents its collection declares. This
refines the collection-side rules
[temporal extent](temporal-extent.md) and
[spatial extent](spatial-extent.md), which are MUST on the UMM-C
required array, and it is the one concrete case of
[collection and granule agreement](collection-granule-consistency.md)
that has a written containment rule. The class is SHOULD, for two
reasons that the sources carry.

**Presence is recommended, not schema-required.** The UMM-G JSON
schema's top-level required array holds GranuleUR, ProviderDates,
CollectionReference and MetadataSpecification only; TemporalExtent
(a oneOf of RangeDateTime, with BeginningDateTime required, or
SingleDateTime) and SpatialExtent (anyOf GranuleLocalities,
HorizontalSpatialDomain, VerticalSpatialDomains) are optional
properties, in v1.6.6 and again in v1.6.7.[^umm-g-schema][^umm-g-schema-167]
The UMM-G requirements base reference gives both elements cardinality
0..1 and the tags "Recommended, Search API, Validated", and carries no
[R] marker on either, where GranuleUR, Provider Dates, Collection
Reference and Metadata Specification do.[^umm-g-reqs] The wiki's
granule pages put absence at the top of the ARC priority matrix:
"There is no provided temporal extent" and "There is no provided
spatial extent" are both red findings.[^wiki-temporal-extent-granule][^wiki-spatial-extent-granule]

**Containment is written as a validation rule, and not yet verified as
one.** The collection Temporal Extents page's CMR Validation section
states "For any granules that are ingested for the collection, the
granules temporal extent must exist within the collection's temporal
extent",[^wiki-temporal-extents] the collection Spatial Extent page
states the same for the spatial extent and adds, as best practice,
"The spatial extent of the granules should always fall within the
spatial extent specified in the collection level metadata (and vice
versa)",[^wiki-spatial-extent] and the UMM-G requirements base says of
the temporal extent that it "is validated against the collection's
temporal extent to make sure that it exists within the collection's
temporal extent".[^umm-g-reqs] The CMR Ingest API documentation
fetched on 2026-09-14 describes schema, UMM and spatial-geometry
validation and does not list this containment rule,[^cmr-ingest-api]
and no ingest was exercised for this draft, so the rule is recorded
as the wiki states it and the class stays SHOULD until an ingest
rejection is produced and cited. That verification is the promotion
path.

**The reviewed tolerances.** ARC grades a temporal discrepancy
between collection and granule dates red when it exceeds one day,
yellow when the collection extent fails to include the full granule
extent by less than one day, and blue when the collection includes
the granules and the times differ by less than one
day.[^wiki-temporal-extents] A granule spatial extent more than 1.0
decimal degree outside the collection's is red, and one outside by
less than 1.0 degree is yellow.[^wiki-spatial-extent] The granule
Temporal Extent page also allows different representations across
levels (a SingleDateTime on the granule under a RangeDateTime on the
collection) "as long as it makes logical sense", with the collection
extent "in sync" with its granules.[^wiki-temporal-extent-granule]

**Check binding.** Structural candidate for the observatory sweeper
(cmr-structural), proposed with this concept:
granule-extents-within-collection, sampling granules per collection
through the CMR search API, requiring both extents present, and
comparing them against the collection's extents with the ARC
thresholds above as the finding grades. pyQuARC: unmapped in this
draft; the pyQuARC mapping was not re-read for this round, and the
collection-granule consistency concept already records that no
current check id covers cross-record containment. The mapping awaits
the working knowledge of the Application Support and Science
Enabling Team (ASSET).

[^umm-g-schema]: UMM-G v1.6.6 required array and the TemporalExtentType and SpatialExtentType definitions, fetched 2026-09-14
[^umm-g-schema-167]: UMM-G v1.6.7 required array, identical, fetched 2026-09-14
[^umm-g-reqs]: ESDIS-SDS-REQ-0015 Rev D, C.2.7 (cardinality 0..1, tags, the validation sentence) and C.2.8 (cardinality 0..1, tags), read 2026-09-14
[^wiki-temporal-extents]: Temporal Extents (collection) wiki page, CMR Validation and ARC Priority Matrix sections, page last updated 2026-07-27, read 2026-09-14
[^wiki-spatial-extent]: Spatial Extent (collection) wiki page, best practices, CMR Validation and ARC Priority Matrix sections, page last updated 2025-05-20, read 2026-09-14
[^wiki-temporal-extent-granule]: Temporal Extent (Granule) wiki page, best practices and ARC Priority Matrix, page last updated 2026-06-03, read 2026-09-14
[^wiki-spatial-extent-granule]: Spatial Extent (Granule) wiki page, ARC Priority Matrix, page last updated 2025-07-31, read 2026-09-14
[^cmr-ingest-api]: CMR Ingest API documentation, validation sections, read 2026-09-14
