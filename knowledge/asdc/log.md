# asdc bundle: change log

Newest first. One line per change: date, concept path, what changed, who.

- 2026-09-14 · STEWARD SIGNING of
  knowledge/asdc/datasets/ceres-ebaf-ed4-2.md,
  knowledge/asdc/gotchas/ebaf-clear-sky-definitions.md,
  knowledge/asdc/gotchas/ebaf-climatology-baseline.md,
  knowledge/asdc/gotchas/ebaf-surface-fluxes-are-modelled.md,
  knowledge/asdc/gotchas/ebaf-versus-syn1deg-versus-ssf.md,
  knowledge/asdc/gotchas/ebaf-imbalance-anchored-to-ocean-heating.md:
  maintainer's review of PR 146 recorded on the maintainer's standing
  instruction for round two of seeding; the dataset concept and the four
  non-high gotchas promoted to stable;
  ebaf-imbalance-anchored-to-ocean-heating (high severity) keeps draft
  with this first review until a second human review, per the two-review
  rule. The verified event is written on the steward's word. The
  verified event is written on the steward's word. (steward)

- 2026-09-14 · coordinator's lint of the seed pull request applied to
  all six concepts: the data quality summary source pinned to the
  versioned V7 copy (byte-identical to what was read; the listed V8 is
  served nowhere and was not read), the podaac recipe named by bundle
  path instead of a relative link, the Kato and others 2025 Terra-only
  period (through July 2002) noted against the summary's June 2002, the
  DOI cross-resolution observation added to the dataset concept's
  access paragraph, the edition that introduced the total-region
  clear-sky flux quoted from the summary, and the January 2024 revision
  cited to the summary alone (the data page's notice is inside an HTML
  comment). Statuses unchanged, no signatures. (knowledge-seeder)

- 2026-09-14 · first concepts seeded: one dataset concept
  (datasets/ceres-ebaf-ed4-2.md, CERES EBAF Edition 4.2 and its 4.2.1
  update, the edition CMR carries) and five gotchas
  (gotchas/ebaf-imbalance-anchored-to-ocean-heating.md at severity high
  with its eval case drafted in agent-evals under ceres/cases/,
  unregistered in any suite manifest until the coordinator's follow-up;
  gotchas/ebaf-clear-sky-definitions.md,
  gotchas/ebaf-surface-fluxes-are-modelled.md and
  gotchas/ebaf-versus-syn1deg-versus-ssf.md at severity medium;
  gotchas/ebaf-climatology-baseline.md at severity low): all drafts, no
  signatures. Sources read the same day: the CERES data products and
  documentation pages, the CERES_EBAF_Ed4.2 and Ed4.2.1 Data Quality
  Summary version 7 (2026-07-01; the documentation page lists a version
  8 posted 2026-09-09 but the file served is version 7), the Edition
  4.1, 4.0 and 2.8 summaries for the anchoring and climatology history,
  the ASDC EBAF-TOA data set abstract, the ASDC collection pages for
  CERES_EBAF and CERES_EBAF-TOA Edition4.2.1 (which redirect to the
  Earthdata catalog), the CMR records C3880496704-LARC_CLOUD and
  C3880497643-LARC_CLOUD plus the SYN1deg Edition4B and SSF1deg
  collections, and the Crossref registry records and abstracts of Loeb
  and others 2018, Kato and others 2018, Loeb and others 2020, Loeb and
  Doelling 2020, Loeb and others 2024, Kato and others 2025 and Johnson
  and others 2016 (the journal pages were not read). Observed the same
  day and left for the reviewer: the two Edition4.2.1 DOIs resolve to
  each other's catalog page. (knowledge-seeder)

- 2026-09-14 · bundle scaffolded empty by tools/scaffold_bundle.py: the index
  with its sections, this log, the check lines and the CODEOWNERS line
  for asdc-stewards; no concepts yet. (maintainer)
