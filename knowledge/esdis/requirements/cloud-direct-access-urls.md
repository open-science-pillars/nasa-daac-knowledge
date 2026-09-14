---
type: requirement
title: Cloud-hosted collections carry direct access URLs and S3 distribution information
description: "For a collection the CMR counts as cloud hosted, the collection record carries DirectDistributionInformation and its granules carry an S3 URL typed GET DATA VIA DIRECT ACCESS; the type exists in the UMM-G enumeration, the element is Recommended, and no source mandates the granule URL."
tags: [requirement, urls, cloud, s3, metadata, cross-archive]
verified: { by: human:PaulMRamirez, at: 2026-09-14T12:12:43Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/142 }
status: stable
class: SHOULD
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:27:36Z }
stale_after: 2027-03-14
sources:
  - id: umm-g-schema
    resource: https://cdn.earthdata.nasa.gov/umm/granule/v1.6.6/umm-g-json-schema.json
    title: "UMM-G JSON schema v1.6.6: RelatedUrlType (URL and Type required) and RelatedUrlTypeEnum"
  - id: umm-c-schema
    resource: https://cdn.earthdata.nasa.gov/umm/collection/v1.18.4/umm-c-json-schema.json
    title: "UMM-C JSON schema v1.18.4: top-level required array and DirectDistributionInformationType"
  - id: umm-c-reqs
    resource: "https://wiki.earthdata.nasa.gov/download/attachments/49448405/EED3-TP-010_Rev04_UMM-C%20%281%29.pdf?api=v2"
    title: "ESDIS-SDS-REQ-0014, Revision D, Appendix B, Metadata Requirements Base Reference for UMM-C (the cover's own numbering; attached to the CMR wiki's UMM Documents page as EED3-TP-010_Rev04_UMM-C.pdf, approved 2026-07-16), section B.2.2.24 Direct Distribution Information"
  - id: wiki-ddi
    resource: https://wiki.earthdata.nasa.gov/spaces/CMR/pages/202808820/Direct+Distribution+Information
    title: "CMR wiki, Direct Distribution Information: description, element specification, ARC priority matrix and UMM version history"
  - id: wiki-related-urls-granules
    resource: https://wiki.earthdata.nasa.gov/spaces/CMR/pages/138875957/Related+URLs+Granules
    title: "CMR wiki, Related URLs (Granules): best practices, element specification and the UMM-G version history"
  - id: cmr-search-api
    resource: https://cmr.earthdata.nasa.gov/search/site/docs/search/api.html
    title: "CMR Search API documentation, the cloud_hosted collection search parameter"
  - id: cmr-ingest-api
    resource: https://cmr.earthdata.nasa.gov/ingest/site/docs/ingest/api.html
    title: "CMR Ingest API documentation, the Cmr-Validate-Keywords header and the fields always checked against KMS"
---

# Cloud-hosted collections carry direct access URLs and S3 distribution information

A collection whose files live in Earthdata Cloud says so twice in its
metadata: the collection record carries DirectDistributionInformation
(the AWS region, the S3 bucket or object prefix names, the credentials
endpoint and its documentation URL), and each granule record carries
its S3 URL as a RelatedUrl typed GET DATA VIA DIRECT ACCESS. This
refines [related URLs present](related-urls-present.md) for the
cloud-hosted case. The class is SHOULD: the model provides the
elements and the CMR keys its cloud-hosted notion on one of them, and
no fetched source mandates the granule URL.

**What the model provides.** The UMM-G RelatedUrlTypeEnum is a closed
list of nine values, DOWNLOAD SOFTWARE, EXTENDED METADATA, GET DATA,
GET DATA VIA DIRECT ACCESS, GET RELATED VISUALIZATION, GOTO WEB TOOL,
PROJECT HOME PAGE, USE SERVICE API and VIEW RELATED INFORMATION, and
a granule RelatedUrl requires URL and Type;[^umm-g-schema] the wiki's
version history records that GET DATA VIA DIRECT ACCESS was added to
the enumeration in UMM-G 1.6.2 on 2021-04-21.[^wiki-related-urls-granules]
On the collection side, DirectDistributionInformation is an optional
top-level property (it is not in the UMM-C required array) whose type
requires Region, S3CredentialsAPIEndpoint and
S3CredentialsAPIDocumentationURL, with S3BucketAndObjectPrefixNames
optional, and Region is a schema enumeration of us-east-1, us-east-2,
us-west-1 and us-west-2 in v1.18.4;[^umm-c-schema] the requirements
base reference gives it
cardinality 0..1 and the tags "Recommended, Normalize", calls it "an
optional element", and shows a bucket prefix of the form
s3://lp-prod-protected/MOD11A1.061 as its example; its CMR
validation note lists us-west-2 and us-east-2 as the valid regions,
a narrower list than the schema's four.[^umm-c-reqs] The
wiki page dates the element to UMM-C 1.16.0 (2021-03-24) and states
what it is for: the sub-elements describe "the information that is
necessary to pull out data products that are stored in the AWS cloud
using a S3 URL that is located inside each granule's (data product
file's) metadata".[^wiki-ddi] That sentence is the closest any fetched
source comes to requiring the granule S3 URL, and it presumes rather
than mandates it.

**What cloud hosted means to the CMR.** The Search API's cloud_hosted
parameter, when true, restricts results to the collections that have
a DirectDistributionInformation element or that carry the tag
gov.nasa.earthdatacloud.s3.[^cmr-search-api] That disjunction is the
sweeper's population: a collection the CMR returns for
cloud_hosted=true is the one this rule applies to, and a collection
found only by the tag, with no DirectDistributionInformation, is a
finding under the first half of the rule.

**What is reviewed.** The wiki's ARC priority matrix for
DirectDistributionInformation is red when any of the three required
sub-elements is missing, when Region is outside the valid values,
when the credentials documentation URL is broken
or points at an FTP server, and blue when it is http or
redirects.[^wiki-ddi][^umm-c-reqs] At ingest, related URL content
type, type and subtype are always checked against KMS, whether or not
the Cmr-Validate-Keywords header is set,[^cmr-ingest-api] so a
mistyped direct access URL is caught at the door and a missing one is
not.

**Check binding.** Structural candidate for the observatory sweeper
(cmr-structural), proposed with this concept:
cloud-direct-access-urls, over the collections the CMR returns for
cloud_hosted=true: DirectDistributionInformation present with its
three required sub-elements, and, on sampled granules, at least one
RelatedUrl whose Type is GET DATA VIA DIRECT ACCESS and whose URL
uses the s3 scheme. pyQuARC: unmapped in this draft; the mapping
awaits the Application Support and Science Enabling Team (ASSET).

[^umm-g-schema]: UMM-G v1.6.6 RelatedUrlTypeEnum and RelatedUrlType required array, fetched 2026-09-14
[^umm-c-schema]: UMM-C v1.18.4 required array, DirectDistributionInformationType required array and DirectDistributionInformationRegionEnum, fetched 2026-09-14
[^umm-c-reqs]: ESDIS-SDS-REQ-0014 Rev D, B.2.2.24 Direct Distribution Information (best practices, CMR validation, cardinality, tags), read 2026-09-14
[^wiki-ddi]: Direct Distribution Information wiki page, description, ARC Priority Matrix and UMM Versioning history, page last updated 2026-06-02, read 2026-09-14
[^wiki-related-urls-granules]: Related URLs (Granules) wiki page, UMM Versioning history entry for 1.6.2, page last updated 2026-06-03, read 2026-09-14
[^cmr-search-api]: CMR Search API documentation, "Find collections by cloud_hosted", read 2026-09-14
[^cmr-ingest-api]: CMR Ingest API documentation, Cmr-Validate-Keywords header, "the following fields are always checked", read 2026-09-14
