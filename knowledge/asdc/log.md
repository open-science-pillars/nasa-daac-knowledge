# asdc bundle: change log

Newest first. One line per change: date, concept path, what changed, who.

- 2026-09-19 · STEWARD RE-SIGNING of
  knowledge/asdc/computations/energy-budget.md,
  knowledge/asdc/computations/cloud-radiative-effect.md: Re-signed after
  the wrap: each concept declares the skill that runs it in the
  atmospheric-physics capability, promoted the same day as a wrap-only
  release, and the paragraph that said the capability was planned and
  the computation unwrapped now says which skill runs it. The executors
  are not edited, so no digest this concept quotes has moved and no
  reference run changed; the usage text that still names a retired path
  is revised with the next reference run, for that reason. The new
  verified event is appended on the steward's word, the earlier events
  kept as history.
  (steward)

- 2026-09-19 · knowledge/asdc/computations/energy-budget.md,
  knowledge/asdc/computations/cloud-radiative-effect.md: each gains
  its executor.skill key, naming the wrapping skill in the atmosphere
  sphere capability that the wrapping rule sends it to,
  atmospheric-physics/energy-budget-closure and
  atmospheric-physics/cloud-radiative-effect. Nothing else changes:
  no executor, attester, loader or data root is touched, and no
  number moves. Both concepts are stable and signed, so both owe a
  re-sign; the capability's first release is the pull request this
  key resolves against, and the placement audit stops reporting the
  two as unwrapped once it merges · claude

- 2026-09-19 · STEWARD SIGNING of
  knowledge/asdc/computations/cloud-radiative-effect.md,
  knowledge/asdc/recipes/cloud-radiative-effect.md: Coordinator review
  of the attested cloud radiative effect on the maintainer's behalf: the
  attester selftest, the fixture run and its attestation, the convention
  refusal exiting 3 and attesting as a refusal, both loader selftests,
  the data root check and the anchored record run were all reproduced,
  every headline number matching the pull request to the digit; a
  tampered receipt value and an edited executor were both rejected by
  the attester with a nonzero exit. The run lands 0.011 watts per square
  metre from the published global mean net effect, inside the rounding
  of the published table, and the receipt states that the distance
  carries that rounding and the edition change and is not a measurement
  of either. Promoted to stable; the check chain is wired into
  run_checks.sh. The verified event is written on the steward's word.
  (steward)

- 2026-09-19 · cloud radiative effect seeded (issue 188): the attested
  computation computations/cloud-radiative-effect.md with its executor
  references/computations/cloud_radiative_effect.py and attester
  references/attesters/cloud_radiative_effect_check.py, the recipe
  recipes/cloud-radiative-effect.md, the loaders
  references/loaders/cre_ceres_fluxes.py and
  references/loaders/cre_data_root.py, and the stamped data root
  references/retrieval/cloud-radiative-effect-root
  (cloud-radiative-effect-root-2026-09-19: the all-sky and clear-sky
  flux means of eight regions under both clear-sky conventions for the
  315 months 2000-03 through 2026-05). The clear-sky convention is a
  declared parameter bound to the two the energy balanced product
  carries, and a convention it does not carry (pristine, computed
  cloud-removed, total-sky-no-aerosol) is refused with its reason; the
  receipt also carries the same terms under the other convention, so
  the price of the choice is a receipt fact. The real-data anchor is
  the global cloud-free-area run over July 2005 through June 2015
  (shortwave -45.8232, longwave +27.9340, net -17.8894 W m-2), which
  sits -0.023, -0.066 and +0.011 from the published global mean cloud
  radiative effect in Table 6-1 of the Edition 4.0 data quality
  summary, inside the 0.1 W m-2 that table is rounded to; the same
  window and region on the total-region convention gives -19.6352, and
  over the Antarctic band the difference between the two conventions
  reverses sign. Sources read 2026-09-19: the CERES_EBAF_Ed4.2 and
  Ed4.2.1 data quality summary version 8 of 9/10/2026, the
  CERES_EBAF_Ed4.0 data quality summary of 1/17/2018 for the published
  table, the CERES one degree zonal geodetic weights, the granule's
  OPeNDAP metadata response for the variable long names that fix which
  convention each field carries, the netCDF-4 subset of
  CERES_EBAF_Edition4.2.1_200003-202605.nc read through the ASDC
  OPeNDAP endpoint with the Earthdata token, the CMR collection and
  granule records, and Crossref records for Loeb and others 2020, 2018
  and 2024. Both concepts are drafts; the computation names no
  executor.skill, because the atmospheric physics capability that will
  wrap it is still a planned repository, so the placement gate reports
  it unwrapped. (knowledge-seeder)

- 2026-09-19 · STEWARD SIGNING of
  knowledge/asdc/datasets/ceres-syn1deg.md,
  knowledge/asdc/conventions/ceres-clear-sky-conventions.md,
  knowledge/asdc/gotchas/syn1deg-geostationary-artifacts.md,
  knowledge/asdc/gotchas/syn1deg-surface-fluxes-are-modelled-not-measured.md,
  knowledge/asdc/gotchas/syn1deg-refuses-long-term-trend-use.md:
  Maintainer review of the synoptic radiation concepts seeded in round
  four: the dataset, the clear-sky conventions (moved from the
  references tree to conventions, where the provider bundles keep a
  convention concept), and the three gotchas. The dataset, the
  convention and the geostationary artifacts gotcha are promoted to
  stable; the two high-severity gotchas carry this first review and stay
  draft for a second. The three provider-facing discrepancies the seed
  recorded (the two summaries disagreeing on the net imbalance, the two
  attribution DOIs that do not resolve, and the absent three-hourly
  collection in the registry) stand as recorded and go to the archive
  contact. The verified event is written on the steward's word. (steward)

- 2026-09-19 · synoptic radiation product seeded (issue 187): the
  dataset concept datasets/ceres-syn1deg.md (CERES SYN1deg, the
  synoptic one degree product beside the energy balanced one), the
  reference concept references/ceres-clear-sky-conventions.md (type
  convention: the four quantities the radiation products call
  clear-sky, which one each field carries, and why a cloud radiative
  effect inherits the convention of the field it subtracts), and three
  gotchas, gotchas/syn1deg-surface-fluxes-are-modelled-not-measured.md
  (high; the surface and in-atmosphere fluxes are Fu-Liou output and
  the tuned fields the ordering page describes as consistent with the
  observed TOA are the ones the summary advises against using),
  gotchas/syn1deg-refuses-long-term-trend-use.md (high; the product's
  own summary refuses trend use and states it is not of climate
  quality) and gotchas/syn1deg-geostationary-artifacts.md (medium; the
  observed fluxes are normalized against CERES and the computed ones
  are not). Sources read 2026-09-19: the CERES_SYN1deg_Ed4A data
  quality summary version 1 of 5/8/2025 with its TOA and surface
  accuracy and validation companions of 4/8/2021, the CERES data
  products and documentation pages, the ASDC SYN1deg data set
  abstract, the ASDC collection page (which redirects to the Earthdata
  catalog), the CMR collection record for CER_SYN1deg-Month Edition4B
  and a short name pattern search over the family, doi.org resolution
  checks on the Edition4B DOIs and on the DOIs printed in the
  summary's attribution section, the CERES_EBAF_Ed4.2 summary version
  8 served that day for the clear-sky conventions, and Crossref
  records for Rutan and others 2015, Doelling and others 2013,
  Doelling and others 2016 and Loeb and others 2020. All five
  concepts are drafts; the two high-severity gotchas carry eval case
  ids whose cases are proposed under ceres/cases/ in the agent-evals
  repository, and registration in that repository's manifest is the
  coordinator's follow-up. (knowledge-seeder)

- 2026-09-16 · STEWARD RE-SIGNING of
  knowledge/asdc/computations/energy-budget.md: Re-signed after the
  placement migration (ADR C): the concept names its executor script in
  executor.resource and carries the data-root layout as its own section;
  the run-instruction reference is retired; no receipt, run id, executor
  or attester changed. The new verified event is appended on the
  steward's word, the earlier events kept as history. (steward)

- 2026-09-16 · knowledge/asdc/computations/energy-budget.md: the run
  instructions reference references/skills/run-energy-budget.md is
  retired under the placement rule (ADR C in the marketplace repository:
  a procedure is a skill in the sphere capability, never a signed
  reference). executor.resource now names the executor script itself,
  whose usage text is the contract; the data-root layout, the one part
  of the retired reference that is contract and not procedure, moved
  into the concept as its own section. The wrapping skill belongs to the
  atmospheric-physics capability when that package exists (roadmap
  c6-unwrapped-computations); until then the computation is unwrapped
  and the placement gate reports it so. Status unchanged; the edited
  stable concept is re-signed below on the maintainer's word.
  (coordinator)

- 2026-09-15 · STEWARD SIGNING of
  knowledge/asdc/computations/energy-budget.md,
  knowledge/asdc/recipes/energy-budget.md,
  knowledge/asdc/references/skills/run-energy-budget.md: Maintainer
  review of the attested energy budget closure (CERES EBAF net TOA flux
  against Argo ocean heat content), its recipe and its run skill, merged
  in PR #174 after the coordinator's review of the chain and a fix round
  (the attester's window and identity rule, the 90 percent level of the
  atmosphere term, the domain understatement and the consistency-check
  wording). Promoted to stable; the check chain is wired into
  run_checks.sh and the registry runs carry the asdc bundle key. The
  verified events are written on the steward's word. (steward)

- 2026-09-15 · coordinator's fix round applied to the energy budget
  seed (pull request 174): the attester now enforces the window rule
  on the pass path (a new ohc-window check, and the tree's Argo receipt
  must carry the identity copied into the receipt) with the relabel
  and swap tampers, the refused-receipt and interval-not-stated
  refusals attested in the selftest; the atmosphere term's 90 percent
  range scaled to 95 percent (non-ocean 0.0822 plus or minus 0.0175 W
  m-2, the bars unchanged at four digits); the weighting offset range
  corrected to 0.14 to 0.28 W m-2; the domain understatement, the
  make-up of the bar and the consistency-check reading of the anomaly
  trend stated in the concept and the recipe; the record rebuilt and
  the quoted run ids updated. Statuses unchanged, no signatures.
  (knowledge-seeder)

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
  reviewer noted, and a provider confirmation still invited. The new
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
  rule. The verified event is written on the steward's word. (steward)

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
