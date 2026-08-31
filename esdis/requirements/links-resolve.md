---
type: requirement
title: Related URLs resolve without error
description: "ARC correctness practice: URLs are responsive and do not redirect."
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

# Related URLs resolve without error

Recorded URLs are responsive: the ARC criteria include "URLs are
responsive and do not redirect".[^arc-paper] The class is SHOULD with
ARC attribution.

**Check binding.** pyQuARC candidates, proposed and pending Science
Enabling Team confirmation: url_check, secure_url_check. Link
resolution is beyond the structural sweeper by design; it belongs to
the pyQuARC harness.[^pyquarc-readme]

[^pyquarc-readme]: pyQuARC README on the ARC framework basis
[^arc-paper]: Bugbee et al. 2021, assessment criteria
