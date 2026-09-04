---
okf_version: "0.2"
---

# esdis bundle (cross-archive requirements)

Cross-archive metadata requirement concepts: what a rule demands, where
it is written, how it is checked, and honestly which of those is a
mandate versus a reviewed practice. Consumed by the archive-observatory
sweeper and harness; stewarded separately from podaac/ via CODEOWNERS
scoping. Scaffolded ahead of the co-build; Science Enabling Team
signatures land at the co-build, never before.

## requirements

- [Temporal extent is a required collection field](requirements/temporal-extent.md), class MUST, status: draft
- [Spatial extent is a required collection field](requirements/spatial-extent.md), class MUST, status: draft
- [Registered DOI on public collections](requirements/doi-registered.md), class SHOULD, status: draft
- [Abstract present and informative](requirements/abstract-informative.md), class SHOULD, status: draft
- [Related URLs present](requirements/related-urls-present.md), class SHOULD, status: draft
- [Platform and instrument keywords resolve in GCMD KMS](requirements/gcmd-keywords-valid.md), class SHOULD, status: draft
- [Related URLs resolve without error](requirements/links-resolve.md), class SHOULD, status: draft
- [Collection and granule metadata agree on shared fields](requirements/collection-granule-consistency.md), class SHOULD, status: draft
