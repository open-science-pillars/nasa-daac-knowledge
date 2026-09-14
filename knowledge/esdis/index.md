---
okf_version: "0.2"
---

# esdis bundle (cross-archive requirements)

Cross-archive metadata requirement concepts: what a rule demands, where
it is written, how it is checked, and honestly which of those is a
mandate versus a reviewed practice. The archive-observatory repository's
metadata sweeper and its harness read these requirements; the bundle is
stewarded separately from podaac/ through CODEOWNERS scoping. Every
concept is a draft today; the steward promotes one once it has been
reviewed, and a confirmation from the Application Support and Science
Enabling Team (ASSET) is invited on each and never required.

What this bundle claims, for the people who know the data: [DIGEST.md](DIGEST.md).

## requirements

- [Temporal extent is a required collection field](requirements/temporal-extent.md), class MUST, status: draft
- [Spatial extent is a required collection field](requirements/spatial-extent.md), class MUST, status: draft
- [Registered DOI on public collections](requirements/doi-registered.md), class SHOULD, status: draft
- [Abstract present and informative](requirements/abstract-informative.md), class SHOULD, status: draft
- [Related URLs present](requirements/related-urls-present.md), class SHOULD, status: draft
- [Platform and instrument keywords resolve in GCMD KMS](requirements/gcmd-keywords-valid.md), class SHOULD, status: draft
- [Related URLs resolve without error](requirements/links-resolve.md), class SHOULD, status: draft
- [Collection and granule metadata agree on shared fields](requirements/collection-granule-consistency.md), class SHOULD, status: draft
- [Granule extents present and inside the collection's extents](requirements/granule-extents-within-collection.md), class SHOULD, status: draft
- [Cloud-hosted collections carry direct access URLs and S3 distribution information](requirements/cloud-direct-access-urls.md), class SHOULD, status: draft
- [Science keywords resolve in GCMD KMS](requirements/science-keywords-valid.md), class SHOULD, status: draft
- [Collection version and DOI agree across versions](requirements/version-and-doi-agree.md), class SHOULD, status: draft
- [Processing level is a required collection field](requirements/processing-level-stated.md), class MUST, status: draft
- [Data format stated on the collection](requirements/data-format-stated.md), class SHOULD, status: draft
