---
type: requirement
title: Related URLs present
description: "ARC completeness practice: documentation, access, and citation URLs are recorded, with access URLs pointing as directly to the data as possible."
tags: [requirement, urls, metadata, cross-archive]
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
---

# Related URLs present

Related URLs for documentation, access, and citation are recorded in
collection metadata; the ARC criteria include "Data access URLs point
as directly to the data as possible", within a framework whose
dimensions are correctness, completeness, and
consistency.[^arc-paper][^pyquarc-readme] The class is SHOULD with ARC
attribution.

**Check binding.** Structural: related-urls-present (cmr-structural,
the observatory sweeper). pyQuARC candidates, proposed and pending
Science Enabling Team confirmation: online_access_url_presence_check,
get_data_url_check.

[^pyquarc-readme]: pyQuARC README on the ARC framework basis
[^arc-paper]: Bugbee et al. 2021, assessment criteria
