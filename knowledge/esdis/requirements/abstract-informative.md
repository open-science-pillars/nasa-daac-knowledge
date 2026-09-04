---
type: requirement
title: Abstract present and informative
description: "ARC completeness practice: the abstract accurately describes the data; presence is checkable, informativeness is a reviewed judgment."
tags: [requirement, abstract, metadata, cross-archive]
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

# Abstract present and informative

The abstract is present and accurately describes the data. This is a
reviewed criterion of the ARC metadata quality assessment framework,
"the basis for the metadata checks that have been incorporated into
pyQuARC",[^pyquarc-readme] whose published criteria include "The
abstract accurately describes the data".[^arc-paper] The class is
SHOULD with ARC attribution: a best practice reviewed by the framework,
not a mandate.

**Check binding.** Structural: abstract-present (cmr-structural, the
observatory sweeper). pyQuARC candidate, proposed and pending Science
Enabling Team confirmation: abstract_length_check, a length proxy; the
informativeness judgment itself is a manual ARC review dimension.

[^pyquarc-readme]: pyQuARC README on the ARC framework basis
[^arc-paper]: Bugbee et al. 2021, assessment criteria
