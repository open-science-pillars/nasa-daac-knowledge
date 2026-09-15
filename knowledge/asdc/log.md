# asdc bundle: change log

Newest first. One line per change: date, concept path, what changed, who.

- 2026-09-15 · attested energy budget closure seeded (issue 157): the
  computation concept computations/energy-budget.md (type Attested
  Computation), the recipe recipes/energy-budget.md, the run skill
  references/skills/run-energy-budget.md, the executor
  references/computations/energy_budget.py (fixture and data-root modes,
  five refusal codes, exit 3), the attester
  references/attesters/energy_budget_check.py (selftest, --data-root
  verification), the loaders references/loaders/eb_ceres_ebaf.py (the
  EBAF net TOA flux term, selftest, --fetch) and eb_data_root.py
  (RECORD.json, --check, selftest), the stamped data root
  references/retrieval/energy-budget-root (toa-net.csv and its stamp
  from CERES_EBAF_Edition4.2.1_200003-202605.nc read as an OPeNDAP
  subset, the Argo 0 to 2000 dbar receipt run sha256:0f64c6f9f2f330b6
  from the ocean-science plugin's committed root, SOURCES.json,
  RECORD.json), and the registry entry energy-budget in
  tools/reference_runs.yaml: all drafts, no signatures. Real-data run
  2006-01 through 2020-12: toa_net +0.8746 against an ocean side of
  0.7427 W m-2, residual +0.1319 against a bar of 0.1894, closed within
  uncertainty; anomaly trend +0.3706 W m-2 per decade against the
  published 0.50 plus or minus 0.47. Sources read the same day: the
  CERES_EBAF_Ed4.2 Data Quality Summary version 7 (the pinned copy),
  the CERES geodetic zone weights file and the general product
  information page (the weights reproduce the product's global mean to
  2.4e-4 W m-2; a cos-latitude mean sits 0.22 W m-2 above it), the
  CMR granule listings of CERES_EBAF and CERES_EBAF-TOA Edition 4.2.1,
  the EBAF granule through 2026-05 via the ASDC OPeNDAP endpoint (the
  direct download host answers through a CloudFront distribution this
  environment cannot reach; the TOA-only granule has no OPeNDAP copy),
  von Schuckmann and others 2023 in full on the journal's site, the
  Crossref registry records of Loeb and others 2021 (the journal page
  behind a bot check; its abstract read on the registry), Loeb and
  others 2018, Johnson and others 2016 and Purkey and Johnson 2010.
  Observed and left for the reviewer: the anchor decade mean of the
  product's geodetic global net flux in the file read is 0.7387 W m-2,
  0.03 above the stated 0.71. (knowledge-seeder)

- 2026-09-14 · STEWARD RE-SIGNING of
  knowledge/asdc/gotchas/ebaf-imbalance-anchored-to-ocean-heating.md:
  second maintainer review recorded on the maintainer's explicit
  instruction in the coordinator session, the maintainer having reviewed
  the concept; promoted to stable under the two-review rule for high
  severity, with the playbook's preference for a different second
  reviewer noted, and a provider confirmation still invited The new
  verified event is appended on the steward's word, the earlier events
  kept as history. (steward)

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
