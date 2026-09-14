---
type: requirement
title: Data format stated on the collection
description: "A collection names the format its files are distributed in, through ArchiveAndDistributionInformation, where Format is required inside an optional block, with a value from the KMS data format vocabulary; the block is Recommended, so the rule is reviewed practice."
tags: [requirement, data-format, distribution, metadata, cross-archive]
status: draft
class: SHOULD
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:27:36Z }
stale_after: 2027-03-14
sources:
  - id: umm-c-schema
    resource: https://cdn.earthdata.nasa.gov/umm/collection/v1.18.4/umm-c-json-schema.json
    title: "UMM-C JSON schema v1.18.4: top-level required array, ArchiveAndDistributionInformationType, FileArchiveInformationType and FileDistributionInformationType (Format required in each alternative)"
  - id: umm-cmn-schema
    resource: https://cdn.earthdata.nasa.gov/umm/collection/v1.18.4/umm-cmn-json-schema.json
    title: "UMM common schema v1.18.4, GetDataType on a RelatedUrl (Format, KMS-controlled)"
  - id: umm-c-reqs
    resource: "https://wiki.earthdata.nasa.gov/download/attachments/49448405/EED3-TP-010_Rev04_UMM-C%20%281%29.pdf?api=v2"
    title: "ESDIS-SDS-REQ-0014 Revision D, Metadata Requirements Base Reference for UMM-C, section B.2.2.23 Archive And Distribution Information (PDF attached to the CMR wiki's UMM Documents page)"
  - id: wiki-archive-collections
    resource: https://wiki.earthdata.nasa.gov/spaces/CMR/pages/135827296/Archive+and+Distribution+Information+for+Collections
    title: "CMR wiki, Archive and Distribution Information for Collections: best practices and element specification"
  - id: wiki-umm-c-representation
    resource: https://wiki.earthdata.nasa.gov/spaces/CMR/pages/91358888/UMM-C+Schema+Representation
    title: "CMR wiki, UMM-C Schema Representation: the Required column per element"
  - id: cmr-ingest-api
    resource: https://cmr.earthdata.nasa.gov/ingest/site/docs/ingest/api.html
    title: "CMR Ingest API documentation, the Cmr-Validate-Keywords header field list and the fields always checked"
  - id: cmr-search-api
    resource: https://cmr.earthdata.nasa.gov/search/site/docs/search/api.html
    title: "CMR Search API documentation, the granule_data_format collection search parameter"
---

# Data format stated on the collection

A collection tells its users what format its files come in. The
place for that statement is ArchiveAndDistributionInformation, whose
FileDistributionInformation entries each require a Format; the block
itself is optional, so the rule is a reviewed practice and the class
is SHOULD. It is drafted apart from
[processing level](processing-level-stated.md) because the two halves
of the briefed rule sit on different sides of the schema's required
array.

**Where the schema puts it.** ArchiveAndDistributionInformation is not
in the UMM-C top-level required array. Inside it, the type is an
anyOf requiring FileArchiveInformation or FileDistributionInformation,
and every alternative of FileArchiveInformationType and of
FileDistributionInformationType has Format in its required array, as a
string of 1 to 80 characters with no enumeration in the
schema.[^umm-c-schema] The wiki's UMM-C Schema Representation table
marks Archive and Distribution Information "No" in its Required
column,[^wiki-umm-c-representation] and the requirements base
reference gives the block cardinality 0..1 with the tag "Recommended",
lists FileDistributionInformation/Format with cardinality 1, and says
the format is "strongly recommended" to come from the GCMD Data
Format vocabulary.[^umm-c-reqs] The wiki page names
FileDistributionInformation as "the preferred location for providing
the data format since this should specify the format data are being
distributed in to the end user" and states the vocabulary constraint
as a must: "The format must be selected from the GCMD Granule Data
Format vocabulary list in order to adhere to the UMM-C
schema".[^wiki-archive-collections] The schema itself does not carry
that enumeration, so the constraint is the KMS check described next
and not a schema failure. A second, narrower place for a format is
the GetData block on a RelatedUrl, whose Format is likewise
KMS-controlled.[^umm-cmn-schema]

**How the CMR treats the value.** The Ingest API lists "Data Format -
Archival and Distribution File Format, and GetData Format" among the
fields validated against KMS when the Cmr-Validate-Keywords header
is true, and notes that the granule data format "was previously
checked against the JSON Schema, but starting with version 1.15.5
CMR will use KMS" among the fields always checked.[^cmr-ingest-api]
The requirements base reference records "CMR Validation: N/A" for
the collection block beyond field lengths, and its ARC report is red
when "No data format is provided" or "The data format provided is
incorrect", yellow when the format is correct but could be more
specific ("NetCDF" where "NetCDF-4" is meant, "ASCII" where "CSV" is
meant).[^umm-c-reqs] The Search API exposes the value as the
granule_data_format collection parameter.[^cmr-search-api]

**Check binding.** Structural candidate for the observatory sweeper
(cmr-structural), proposed with this concept: data-format-present,
satisfied by a Format on any FileDistributionInformation or
FileArchiveInformation entry, or, failing those, on a RelatedUrl's
GetData block, with the KMS data format lookup as a second grade.
pyQuARC candidate, already named as adjacent in the platform and
instrument keyword concept and proposed here for the vocabulary
grade, pending confirmation by the Application Support and Science
Enabling Team (ASSET): data_format_gcmd_check.

[^umm-c-schema]: UMM-C v1.18.4 required array, ArchiveAndDistributionInformationType anyOf, FileArchiveInformationType and FileDistributionInformationType required arrays, fetched 2026-09-14
[^umm-cmn-schema]: UMM common schema v1.18.4 GetDataType Format description, fetched 2026-09-14
[^umm-c-reqs]: ESDIS-SDS-REQ-0014 Rev D, B.2.2.23 Archive And Distribution Information, element specification, best practices, validation, ARC report, cardinality and tags, read 2026-09-14
[^wiki-archive-collections]: Archive and Distribution Information for Collections wiki page, best practices and element specification, page last updated 2025-05-20, read 2026-09-14
[^wiki-umm-c-representation]: UMM-C Schema Representation wiki page, Required column, page last updated 2026-07-14, read 2026-09-14
[^cmr-ingest-api]: CMR Ingest API documentation, Cmr-Validate-Keywords header field list and "the following fields are always checked", read 2026-09-14
[^cmr-search-api]: CMR Search API documentation, "Find collections matching 'granule_data_format' param value", read 2026-09-14
