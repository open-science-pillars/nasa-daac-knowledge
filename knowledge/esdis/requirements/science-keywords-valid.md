---
type: requirement
title: Science keywords resolve in GCMD KMS
description: "A collection's science keyword hierarchies (Category, Topic, Term and the optional variable levels) are values of the KMS science keyword scheme; presence and the three-level minimum are schema-required, and the KMS resolution is a CMR ingest warning and an ARC red finding."
tags: [requirement, gcmd, keywords, science-keywords, metadata, cross-archive]
status: draft
class: SHOULD
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:27:36Z }
stale_after: 2027-03-14
sources:
  - id: umm-c-schema
    resource: https://cdn.earthdata.nasa.gov/umm/collection/v1.18.4/umm-c-json-schema.json
    title: "UMM-C JSON schema v1.18.4: top-level required array and the ScienceKeywords property"
  - id: umm-cmn-schema
    resource: https://cdn.earthdata.nasa.gov/umm/collection/v1.18.4/umm-cmn-json-schema.json
    title: "UMM common schema v1.18.4, ScienceKeywordType (Category, Topic, Term required)"
  - id: umm-c-reqs
    resource: "https://wiki.earthdata.nasa.gov/download/attachments/49448405/EED3-TP-010_Rev04_UMM-C%20%281%29.pdf?api=v2"
    title: "ESDIS-SDS-REQ-0014 Revision D, Metadata Requirements Base Reference for UMM-C, section B.2.3.2 Science Keywords [R] (PDF attached to the CMR wiki's UMM Documents page)"
  - id: wiki-science-keywords
    resource: https://wiki.earthdata.nasa.gov/spaces/CMR/pages/107387205/Science+Keywords
    title: "CMR wiki, Science Keywords: description, best practices, element specification, CMR Validation and ARC priority matrix"
  - id: cmr-ingest-api
    resource: https://cmr.earthdata.nasa.gov/ingest/site/docs/ingest/api.html
    title: "CMR Ingest API documentation, the Cmr-Validate-Keywords header and its notes"
---

# Science keywords resolve in GCMD KMS

Every science keyword hierarchy on a collection is a path in the
Keyword Management System's science keyword scheme, populated from
Category through Term at least and with no position skipped. The
existing [platform and instrument keyword](gcmd-keywords-valid.md)
concept covers the platform and instrument schemes; this one covers
the science keyword hierarchy, where the sources say more. The class
is SHOULD because the resolution itself is a warning at the door.

**What the schema requires.** ScienceKeywords is in the UMM-C
top-level required array with minItems 1, and its description names
the KMS as the controlled vocabulary;[^umm-c-schema] each
ScienceKeywordType requires Category, Topic and Term, with
VariableLevel1 to VariableLevel3 and DetailedVariable
optional.[^umm-cmn-schema] The requirements base reference marks the
element [R] and states the best practice as a must: "At a minimum,
one science keyword hierarchy must be provided, and this hierarchy
must go down to the 'Term' level of detail", "All positions in the
science keyword hierarchy must be populated until the desired level
of detail is reached", and "Skipping or leaving blank a position in
the keyword hierarchy will render the keyword invalid"; DetailedVariable
"is the only science keyword element that is not controlled by the
KMS".[^umm-c-reqs] Presence and the three-level minimum are
therefore MUST-grade facts; a collection missing them is invalid
against the model.

**What the CMR does with the vocabulary.** The same document's CMR
Validation list reads "All science keyword sub elements except for
DetailedVariable must be valid according to the keyword management
system. Currently the CMR issues a warning if this constraint is
violated",[^umm-c-reqs] and the wiki page carries the identical
sentence.[^wiki-science-keywords] The Ingest API documentation
describes the mechanism: with the Cmr-Validate-Keywords header set to
true, science keywords (category, topic, term, variable levels 1 to 3)
are validated against GCMD KMS as a known combination, and without
the header science keywords are still validated "except that
validation errors will be returned to users as
warnings".[^cmr-ingest-api] A keyword outside the KMS therefore lands
in the CMR with a warning, which is why this concept is SHOULD while
the presence rule above is not.

**Where the valid values are, and one trap.** The wiki page names
the scheme's CSV export on the KMS as the valid list and warns that
the "EARTH SCIENCE SERVICES" keywords at the top of that file are not
science keywords: valid ones start with the EARTH SCIENCE
Category.[^wiki-science-keywords] Science keywords are not case
sensitive.[^umm-c-reqs] The ARC priority matrix is red when no
science keyword is provided, when a keyword does not exist in the
KMS, when a level is missing from the hierarchy, when a keyword sits
in the wrong position (a VariableLevel2 value in the VariableLevel1
field), or when the keyword is inappropriate for the dataset; a
recommendation to add or deepen a keyword is
yellow.[^wiki-science-keywords]

**Check binding.** Structural candidate for the observatory sweeper
(cmr-structural), proposed with this concept: science-keywords-valid,
resolving each Category, Topic, Term and variable-level path against
the KMS science keyword scheme and flagging a skipped position or a
path under EARTH SCIENCE SERVICES. pyQuARC candidate, already named
as adjacent in the platform and instrument keyword concept and
proposed here as the primary binding, pending confirmation by the
Application Support and Science Enabling Team (ASSET):
science_keywords_gcmd_check.

[^umm-c-schema]: UMM-C v1.18.4 required array and ScienceKeywords property (minItems 1, KMS named in the description), fetched 2026-09-14
[^umm-cmn-schema]: UMM common schema v1.18.4 ScienceKeywordType required array, fetched 2026-09-14
[^umm-c-reqs]: ESDIS-SDS-REQ-0014 Rev D, B.2.3.2 Science Keywords [R], best practices and CMR Validation, read 2026-09-14
[^wiki-science-keywords]: Science Keywords wiki page, description, CMR Validation and ARC Priority Matrix, page last updated 2025-05-20, read 2026-09-14
[^cmr-ingest-api]: CMR Ingest API documentation, Cmr-Validate-Keywords header and notes, read 2026-09-14
