---
type: requirement
title: Processing level is a required collection field
description: "ProcessingLevel is in the UMM-C schema's required array and its Id is required within it: a collection record without a processing level identifier is invalid against the metadata model; alignment with the EOSDIS levels is reviewed practice."
tags: [requirement, processing-level, metadata, cross-archive]
verified: { by: human:PaulMRamirez, at: 2026-09-14T12:12:43Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/142 }
status: stable
class: MUST
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:27:36Z }
stale_after: 2027-03-14
sources:
  - id: umm-c-schema
    resource: https://cdn.earthdata.nasa.gov/umm/collection/v1.18.4/umm-c-json-schema.json
    title: "UMM-C JSON schema v1.18.4: top-level required array and ProcessingLevelType (Id required)"
  - id: umm-c-schema-1187
    resource: https://cdn.earthdata.nasa.gov/umm/collection/v1.18.7/umm-c-json-schema.json
    title: "UMM-C JSON schema v1.18.7: top-level required array and ProcessingLevelType, re-checked for this concept"
  - id: umm-c-reqs
    resource: "https://wiki.earthdata.nasa.gov/download/attachments/49448405/EED3-TP-010_Rev04_UMM-C%20%281%29.pdf?api=v2"
    title: "ESDIS-SDS-REQ-0014, Revision D, Appendix B, Metadata Requirements Base Reference for UMM-C (the cover's own numbering; attached to the CMR wiki's UMM Documents page as EED3-TP-010_Rev04_UMM-C.pdf, approved 2026-07-16), section B.2.2.16 Processing Level [R]"
  - id: wiki-processing-level
    resource: https://wiki.earthdata.nasa.gov/spaces/CMR/pages/109871916/Processing+Level
    title: "CMR wiki, Processing Level: best practices, element specification and ARC priority matrix"
  - id: cmr-ingest-api
    resource: https://cmr.earthdata.nasa.gov/ingest/site/docs/ingest/api.html
    title: "CMR Ingest API documentation, the Cmr-Validate-Keywords header field list"
  - id: cmr-search-api
    resource: https://cmr.earthdata.nasa.gov/search/site/docs/search/api.html
    title: "CMR Search API documentation, the processing_level_id collection search parameter and facet"
---

# Processing level is a required collection field

Collection metadata states its processing level. The UMM-C JSON
schema, version 1.18.4, lists ProcessingLevel in its top-level
required array, beside ShortName, Version, EntryTitle, Abstract, DOI,
DataCenters, ScienceKeywords, TemporalExtents, SpatialExtent,
Platforms, CollectionProgress and MetadataSpecification, and the
ProcessingLevelType requires Id (a string of 1 to 80 characters) with
ProcessingLevelDescription optional, so a record without a processing
level identifier is invalid against the model
itself;[^umm-c-schema] version 1.18.7, the newest version fetched for this round,
carries the same required array and the same
type.[^umm-c-schema-1187] The requirements base reference marks the
element [R], gives ProcessingLevel/ID cardinality 1, tags it
"Required, Controlled Vocabulary, Search API, Faceted", and says in
its best practices "A processing level Id is required".[^umm-c-reqs]
The class is MUST on the verified schema citation, for the presence
of the identifier; a schema version bump re-verifies it at the next
sweep.

**The value is reviewed, not mandated.** The identifier's alignment
with the EOSDIS processing levels is a recommendation in both
documents ("It is recommended that the processing level align with
the EOSDIS data processing levels if at all possible"), and the two
list the levels differently: the requirements base reference names
0, 1A, 1B, 2, 3, 4 and the wiki page names 0, 1A, 1B, 1C, 2, 2A, 2B,
3, 3A, 4.[^umm-c-reqs][^wiki-processing-level] The requirements base
reference states "CMR Validation: N/A" beyond the field's presence
and length, and the wiki page's CMR Validation section is an unfilled
placeholder; the ARC matrix is red when the Id is missing or empty or "incorrect for
the dataset"; an EOSDIS dataset whose level is not an EOSDIS level
is red in the requirements base reference and yellow on the wiki
page.[^umm-c-reqs][^wiki-processing-level] At ingest, the Ingest API
lists "ProcessingLevel - productlevelid" among the fields checked
against KMS only when the Cmr-Validate-Keywords header is set to
true,[^cmr-ingest-api] so an off-list value is not rejected by
default. The Search API exposes the value as the processing_level_id
parameter and facet.[^cmr-search-api]

**Check binding.** Structural candidate for the observatory sweeper
(cmr-structural), proposed with this concept:
processing-level-present, reading ProcessingLevel.Id and, as a
separate reviewed grade, its membership in the EOSDIS level list the
steward adopts. pyQuARC: unmapped in this draft; the pyQuARC mapping
was not re-read for this round, and the binding awaits the
Application Support and Science Enabling Team (ASSET).

[^umm-c-schema]: UMM-C v1.18.4 top-level required array and ProcessingLevelType required array, fetched 2026-09-14
[^umm-c-schema-1187]: UMM-C v1.18.7 top-level required array and ProcessingLevelType, identical for these fields, fetched 2026-09-14
[^umm-c-reqs]: ESDIS-SDS-REQ-0014 Rev D, B.2.2.16 Processing Level [R], best practices, validation, ARC report, cardinality and tags, read 2026-09-14
[^wiki-processing-level]: Processing Level wiki page, best practices, element specification and ARC Priority Matrix, page last updated 2026-06-02, read 2026-09-14
[^cmr-ingest-api]: CMR Ingest API documentation, Cmr-Validate-Keywords header field list, read 2026-09-14
[^cmr-search-api]: CMR Search API documentation, "Find collections by processing_level_id" and the facet list, read 2026-09-14
