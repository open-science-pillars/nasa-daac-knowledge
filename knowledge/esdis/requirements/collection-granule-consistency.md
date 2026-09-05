---
type: requirement
title: Collection and granule metadata agree on shared fields
description: "ARC consistency practice: metadata describes the same concepts in the same manner across collection and granule records."
tags: [requirement, consistency, metadata, cross-archive]
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

# Collection and granule metadata agree on shared fields

Information common to a collection record and its granule records is
consistent. The ARC framework defines consistency as "the extent to
which metadata describes the same semantic concepts and information in
the same manner across multiple records" and assesses each collection
against a randomly selected corresponding granule record,[^arc-paper]
and pyQuARC "ensures that information common to both the data product
and the file-level metadata are consistent and
compatible".[^pyquarc-readme] The class is SHOULD with ARC attribution.

**Check binding.** Unmapped in pyQuARC v1.3.0: no check id in the
current mapping covers cross-record consistency broadly (the closest,
granule_spatial_representation_check, covers one shared field and is
too narrow to propose). The mapping awaits the working knowledge of the
Application Support and Science Enabling Team (ASSET).

[^pyquarc-readme]: pyQuARC README, common-information consistency sentence
[^arc-paper]: Bugbee et al. 2021, consistency definition and granule sampling
