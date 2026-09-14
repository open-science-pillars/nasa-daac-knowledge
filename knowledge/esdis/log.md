# esdis bundle: change log

Newest first. One line per change: date, concept path, what changed, who.

- 2026-09-14 · requirements round two, six new draft concepts:
  granule-extents-within-collection (SHOULD), cloud-direct-access-urls
  (SHOULD), science-keywords-valid (SHOULD), version-and-doi-agree
  (SHOULD), processing-level-stated (MUST) and data-format-stated
  (SHOULD); index.md lists them and DIGEST.md is re-rendered. The
  briefed processing-level-and-format concept was split in two because
  ProcessingLevel is in the UMM-C required array and
  ArchiveAndDistributionInformation is not. Sources read: the UMM-C
  JSON schemas v1.18.4 and v1.18.7 and the UMM common schema v1.18.4,
  the UMM-G JSON schemas v1.6.6 and v1.6.7, the ESDIS Metadata
  Requirements Base References for UMM-C (ESDIS-SDS-REQ-0014 Rev D)
  and UMM-G (ESDIS-SDS-REQ-0015 Rev D) as attached to the CMR wiki's
  UMM Documents page, the CMR wiki element pages for Temporal Extents,
  Spatial Extent, Temporal Extent (Granule), Spatial Extent (Granule),
  Direct Distribution Information, Related URLs (Granules), Science
  Keywords, Version, DOI, Processing Level, Archive and Distribution
  Information for Collections and the UMM-C and UMM-G Schema
  Representation tables, and the CMR Ingest and Search API
  documentation. The pyQuARC mapping was not re-read; new check ids
  are proposed only where the bundle already names them. Every
  concept is a draft, no signatures. (knowledge-seeder/claude)

- 2026-09-04 · index.md and the five requirement concepts that name the
  team (doi-registered, related-urls-present,
  collection-granule-consistency, spatial-extent, temporal-extent):
  the Science Enabling Teams are being renamed the Application Support
  and Science Enabling Teams (ASSETs), and the concepts say so. Wording
  only; no rule, class, or check mapping changed, and every concept
  stays a draft. Earlier entries keep the name in use when they were
  written. (claude-code/fable-5)

- 2026-08-30 · bundle scaffolded with eight requirement concepts, drafted
  ahead of the Science Enabling Team co-build: all drafts, no
  signatures, and the incoming stewards' names reserved for signing
  time. Standards-librarian provenance pass drove every class:
  temporal-extent and spatial-extent promoted to MUST on the UMM-C
  v1.18.4 required array (fetched and quoted); the five ARC rules stay
  SHOULD with attribution resolved to the pyQuARC README and Bugbee et
  al. 2021. The catch of the session: req-doi FAILED its MUST
  promotion. Every fetched source is eligibility, should, or plan
  level, and the UMM common schema's DoiType accepts MissingReason in
  place of a registered DOI, so the seed's MUST candidate was exactly
  the wrong MUST register R2 exists to prevent; doi-registered.md
  records the failed promotion as the concept's central fact. pyQuARC
  check-id mappings recorded as proposals pending SET confirmation;
  collection-granule-consistency is unmapped in v1.3.0. (drafted by
  claude-code/fable-5; librarian pass by the standards-librarian agent)
