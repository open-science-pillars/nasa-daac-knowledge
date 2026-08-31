---
type: requirement
title: Registered DOI on public collections
description: "The DOI expectation for public collections: recommended, reviewed, and near-universal, but not schema-mandated; the UMM-C DOI element accepts a MissingReason."
tags: [requirement, doi, metadata, cross-archive]
status: draft
class: SHOULD
generated: { by: claude-code/fable-5, at: 2026-08-31T02:09:11Z }
stale_after: 2026-11-30
sources:
  - id: umm-c-schema
    resource: https://cdn.earthdata.nasa.gov/umm/collection/v1.18.4/umm-c-json-schema.json
    title: UMM-C JSON schema v1.18.4, top-level required array
  - id: umm-cmn-doitype
    resource: https://cdn.earthdata.nasa.gov/umm/collection/v1.18.4/umm-cmn-json-schema.json
    title: "UMM common schema v1.18.4, DoiType: oneOf requires DOI or MissingReason"
  - id: doi-process
    resource: https://www.earthdata.nasa.gov/engage/doi-process
    title: "NASA Earthdata DOI process, Data Requirements section (eligibility criteria)"
  - id: dpdg-rfc041
    resource: https://www.earthdata.nasa.gov/s3fs-public/2025-03/ESDS-RFC-041-DPDG%20V2.0.1.pdf
    title: "ESDS-RFC-041 Data Product Development Guide v2.0.1, category Suggested Practice"
  - id: ramapriyan-2017
    resource: https://datascience.codata.org/articles/10.5334/dsj-2017-015
    title: "Ramapriyan et al. 2017, NASA EOSDIS Data Identifiers (mandatory registration stated as a plan)"
---

# Registered DOI on public collections

Public EOSDIS collections carry registered DOIs as reviewed practice
and near-universal reality, and machine citation depends on the DOI
recorded in CMR metadata. The class of this rule is SHOULD, not MUST,
because a promotion attempt on 2026-08-30 failed on the sources: the
Earthdata DOI process page states eligibility criteria rather than a
mandate,[^doi-process] the Data Product Development Guide says
producers "should work with the assigned DAAC to obtain DOIs" and is
itself stamped Suggested Practice,[^dpdg-rfc041] mandatory registration
appears in the 2017 identifiers paper as a plan,[^ramapriyan-2017] and
the UMM-C schema, whose required array does include the DOI
element,[^umm-c-schema] defines that element as satisfiable by a
MissingReason of "Not Applicable" or "Unknown" in place of a registered
DOI.[^umm-cmn-doitype] A wrong MUST here is the exact failure the rule
classes exist to prevent; the class rises only when an authoritative
mandate is produced and cited.

**Check binding.** Structural: doi-present (cmr-structural, the
observatory sweeper, reading the UMM DOI.DOI value). pyQuARC
candidates, proposed and pending Science Enabling Team confirmation:
doi_validity_check, doi_authority_presence_check,
eosdis_doi_authority_check, doi_missing_reason_enumeration_check. The
last exists because a missing DOI is an anticipated schema state, which
corroborates the SHOULD class.

[^umm-c-schema]: UMM-C v1.18.4 required array (DOI element present in it)
[^umm-cmn-doitype]: UMM common schema v1.18.4 DoiType oneOf: required DOI or required MissingReason, enum Not Applicable, Unknown
[^doi-process]: Earthdata DOI process, "ESDIS has established criteria to identify its products and supporting documents eligible for a DOI"
[^dpdg-rfc041]: ESDS-RFC-041 v2.0.1, "Data producers should work with the assigned DAAC to obtain DOIs for their data products"
[^ramapriyan-2017]: "The plan to make DOI registration a mandatory requirement for the metadata submitted to the Common Metadata Repository"
