---
type: requirement
title: Collection version and DOI agree across versions
description: "The Version on a collection matches its landing page and documentation, a new version's DOI is its own with the prior version reachable through DOI/PreviousVersion, and a DOI shared by two CMR collection versions is a reviewed finding rather than an ingest error."
tags: [requirement, doi, version, metadata, cross-archive]
status: draft
class: SHOULD
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:27:36Z }
stale_after: 2027-03-14
sources:
  - id: umm-c-schema
    resource: https://cdn.earthdata.nasa.gov/umm/collection/v1.18.4/umm-c-json-schema.json
    title: "UMM-C JSON schema v1.18.4: top-level required array (Version and DOI present in it)"
  - id: umm-cmn-schema
    resource: https://cdn.earthdata.nasa.gov/umm/collection/v1.18.4/umm-cmn-json-schema.json
    title: "UMM common schema v1.18.4: DoiType (DOI or MissingReason) and PreviousVersionType (Version, Description, DOI, Published)"
  - id: umm-c-reqs
    resource: "https://wiki.earthdata.nasa.gov/download/attachments/49448405/EED3-TP-010_Rev04_UMM-C%20%281%29.pdf?api=v2"
    title: "ESDIS-SDS-REQ-0014, Revision D, Appendix B, Metadata Requirements Base Reference for UMM-C (the cover's own numbering; attached to the CMR wiki's UMM Documents page as EED3-TP-010_Rev04_UMM-C.pdf, approved 2026-07-16), sections B.2.2.2 Version [R] and B.2.2.4 DOI [R]"
  - id: wiki-version
    resource: https://wiki.earthdata.nasa.gov/spaces/CMR/pages/107382970/Version
    title: "CMR wiki, Version: best practices, CMR Validation and ARC priority matrix"
  - id: wiki-doi
    resource: https://wiki.earthdata.nasa.gov/spaces/CMR/pages/107385989/DOI
    title: "CMR wiki, DOI: best practices for DOI/PreviousVersion and DOI/MissingReason, ARC priority matrix"
  - id: cmr-search-api
    resource: https://cmr.earthdata.nasa.gov/search/site/docs/search/api.html
    title: "CMR Search API documentation, the doi collection search parameter"
---

# Collection version and DOI agree across versions

A collection's Version is the version its landing page and
documentation state, and its DOI identifies that version: a new
version of a product carries its own DOI and points back at the
previous one through DOI/PreviousVersion. This refines
[registered DOI on public collections](doi-registered.md), which
records why the DOI itself is SHOULD and not MUST; the agreement rule
here inherits that class, and its sources are best practice and
review criteria rather than a mandate.

**Version.** Version is in the UMM-C required array,[^umm-c-schema]
and the requirements base reference marks it [R], adds that "The
short name and version ID combination must be unique per provider",
and states the agreement as best practice: "The version should be
consistent throughout the metadata record. The version in the
metadata should be identical to the version specified on the dataset
landing page and in dataset documentation", with the examples that
1.1 on the landing page is 1.1 in the metadata (not 1.10) and
3.4.2004 is 3.4.2004 (not 03.04.2004).[^umm-c-reqs] The wiki page
carries the same text, and its ARC priority matrix is red when "The
Version is incorrect for the dataset".[^wiki-version]

**DOI across versions.** The common schema's DoiType is a oneOf of a
registered DOI (with Authority and PreviousVersion optional beside
it) or a MissingReason; PreviousVersionType carries Version,
Description, DOI and Published, with DOI required, and its
description reads "Provides a DOI of the previous version of this
collection. This allows users to find historical data for this
collection".[^umm-cmn-schema] The wiki adds "If the PreviousVersion
element is used, then the DOI must be provided".[^wiki-doi] The
requirements base reference and the wiki both name "datasets that
will soon be replaced by a new version" as a case where MissingReason
is appropriate, with the worked explanation "This version will be
removed from CMR, and the new version will be assigned a
DOI"[^wiki-doi] (the requirements base reference's copy reads "from
the CMR" without the comma),[^umm-c-reqs] which is the model's own
statement that a version and its DOI go together. The ARC matrix for the DOI is red
when "The incorrect DOI is listed for the dataset" and when "The
dataset has a DOI but the metadata indicates that it does
not".[^wiki-doi]

**What follows for two versions, this concept's inference.** The
paragraph that follows is drawn from the sources above and is not a
rule any of them states. Two CMR collection records with
different Version values and the same DOI cannot both satisfy the
Version rule against one landing page unless that page states both
versions, so a DOI shared across ShortName and Version pairs is a
finding for review, not an error the sweeper decides: the landing
page is the arbiter, and the sources put that judgment with the
reviewer ("Check that the version value is appropriate for the
dataset" is the manual review step).[^wiki-version] No fetched source
states a rule that each version must be registered separately; the
claim stays at what the model and the review criteria carry.

**Check binding.** Structural candidate for the observatory sweeper
(cmr-structural), proposed with this concept: version-doi-agree,
grouping collections by DOI through the Search API's doi
parameter[^cmr-search-api] and raising a DOI held by more than one
ShortName and Version pair, a DOI/PreviousVersion whose DOI matches
no CMR collection, and a Version absent from the landing page's text
where the sweeper can read it. pyQuARC candidate, already named in
the DOI concept and pending confirmation by the Application Support
and Science Enabling Team (ASSET): doi_validity_check, for the DOI's
resolution; the version agreement itself is a manual ARC review step
in the sources.

[^umm-c-schema]: UMM-C v1.18.4 required array (Version and DOI present in it), fetched 2026-09-14
[^umm-cmn-schema]: UMM common schema v1.18.4 DoiType oneOf and PreviousVersionType (DOI required), fetched 2026-09-14
[^umm-c-reqs]: ESDIS-SDS-REQ-0014 Rev D, B.2.2.2 Version [R] (description, best practices, CMR validation) and B.2.2.4 DOI [R] (PreviousVersion and MissingReason best practices, examples), read 2026-09-14
[^wiki-version]: Version wiki page, best practices, GCMD manual review and ARC Priority Matrix, page last updated 2025-05-20, read 2026-09-14
[^wiki-doi]: DOI wiki page, PreviousVersion and MissingReason best practices with the worked explanation, ARC Priority Matrix, page last updated 2025-05-20, read 2026-09-14
[^cmr-search-api]: CMR Search API documentation, "Find collections by doi value", read 2026-09-14
