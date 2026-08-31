---
type: requirement
title: Platform and instrument keywords resolve in GCMD KMS
description: "ARC conformance practice: platform and instrument names conform to GCMD conventions, governed by the GCMD keyword governance process."
tags: [requirement, gcmd, keywords, metadata, cross-archive]
status: draft
class: SHOULD
generated: { by: claude-code/fable-5, at: 2026-08-31T02:09:11Z }
stale_after: 2027-02-28
sources:
  - id: pyquarc-readme
    resource: https://github.com/NASA-IMPACT/pyQuARC
    title: "pyQuARC README: the ARC framework is the basis for its checks"
  - id: arc-paper
    resource: https://datascience.codata.org/articles/10.5334/dsj-2021-017
    title: "Bugbee et al. 2021, Improving Discovery and Use of NASA's Earth Observation Data Through Metadata Quality Assessments (doi 10.5334/dsj-2021-017)"
  - id: gcmd-governance
    resource: https://www.earthdata.nasa.gov/news/nasas-gcmd-releases-keyword-governance-community-guide-document-version-10
    title: "GCMD Keyword Governance and Community Guide v1.0 announcement (the governance process for keyword changes)"
---

# Platform and instrument keywords resolve in GCMD KMS

Platform and instrument keywords in collection metadata resolve in the
GCMD Keyword Management System. The ARC criteria state that "Earth
observation platform and instrument names conform to GCMD conventions"
and that science keywords conform to GCMD conventions or ISO 19115
topic categories,[^arc-paper] and the keyword set itself is governed:
the Keyword Governance and Community Guide describes the structures and
process for reviewing proposed changes.[^gcmd-governance] The class is
SHOULD with ARC attribution.

**Check binding.** pyQuARC candidates, proposed and pending Science
Enabling Team confirmation: platform_short_name_gcmd_check,
instrument_short_name_gcmd_check; adjacent if the scope widens:
science_keywords_gcmd_check, organization_short_name_gcmd_check,
data_format_gcmd_check.[^pyquarc-readme]

[^pyquarc-readme]: pyQuARC README on the ARC framework basis
[^arc-paper]: Bugbee et al. 2021, assessment criteria
[^gcmd-governance]: GCMD governance guide v1.0 announcement
