# nsidc bundle: change log

Newest first. One line per change: date, concept path, what changed, who.

- 2026-09-20 · 5 concepts (assessment-method-groups-are-not-independent.md, firn-model-air-content.md, ice-sheet-balance.md, ice-sheet-input-output.md, imbie-ice-sheet-assessment.md) · re-signed after the computations moved into the capabilities that run them: each cites the method at its package path instead of the bundle path it used to carry, and the coordinator compared every number in all of them against the copy from before the move, finding none changed · human:PaulMRamirez
- 2026-09-20 · THE COMPUTATIONS LEAVE THE BUNDLE (ADR E, a computation
  is a skill). Deleted, every one of them copied into land-ice by its
  pull request 9 and present on that repository's main before the
  deletion: knowledge/nsidc/computations/ice-sheet-balance.md and
  ice-sheet-input-output.md, now land-ice's
  knowledge/computations/ice-sheet-balance.md and
  knowledge/computations/ice-sheet-input-output.md; the fourteen
  scripts under knowledge/nsidc/references/, which are the two
  executors, the two attesters and the ten loaders, now in the scripts
  directories of the land-ice skills ice-mass-change and
  ice-sheet-input-output; and the two stamped data roots under
  knowledge/nsidc/references/retrieval/, sixteen files, now under
  land-ice's knowledge/references/retrieval/. Both concepts are
  re-signed and stable in land-ice as of its pull request 10. No number
  changed and no knowledge was deleted: the datasets, the gotchas and
  the two recipes stay, and each one that named an executor, an
  attester, a loader or a computation concept by bundle path now names
  it by land-ice package path, for example
  land-ice/knowledge/computations/ice-sheet-balance.md where it said
  computations/ice-sheet-balance.md, and
  land-ice/knowledge/references/retrieval/ice-sheet-balance-root/RECORD.json
  where it said references/retrieval/ice-sheet-balance-root/RECORD.json.
  The index says the bundle carries no attested computation and where
  the two went. In tools/, run_checks.sh loses the five ice sheet
  chains and their loader selftests and root checks, which are two
  goldens under land-ice's verification/ now.
  (migration seed, for the coordinator)

- 2026-09-19 · STEWARD RE-SIGNING of
  knowledge/nsidc/computations/ice-sheet-balance.md: Re-signed after the
  ATL15 term landed in the committed root. The environment's egress
  policy was changed to allow the NSIDC distribution host, the same five
  granules the two earlier attempts record were fetched unchanged, and
  the concept now carries both altimetry terms rather than one and a
  reason the other is missing. The reference run section gains the pair
  over the window they share, Greenland 2019-01 through 2023-10: the
  gravimetric side is identical on both, the altimetric rates differ by
  80 Gt per year, and the verdict turns on which is used. It is read as
  support for the boundaries' suspicion of the ITS_LIVE term and not as
  a measured discrepancy, because the two rates' intervals overlap over
  most of their length. The recorded pre-2019 run reproduces every
  number it always did; only its run identifier moved, because the
  identifier binds the data root's manifest and the root gained a term.
  No executor, attester or loader is edited. The new verified event is
  appended on the steward's word, the earlier events kept as history.
  (steward)

- 2026-09-19 · STEWARD RE-SIGNING of
  knowledge/nsidc/computations/ice-sheet-balance.md,
  knowledge/nsidc/computations/ice-sheet-input-output.md: Re-signed
  after the wrap: each concept declares the skill that runs it in the
  land ice capability, promoted the same day as a wrap-only release, and
  the paragraph in each that said the capability was planned and the
  computation unwrapped now names the skill. The executors are not
  edited, so no digest either concept quotes has moved and no reference
  run changed; the closure's usage text that still names a retired path
  is revised with the next reference run, for that reason. The new
  verified event is appended on the steward's word, the earlier events
  kept as history. (steward)

- 2026-09-19 · knowledge/nsidc/computations/ice-sheet-balance.md,
  knowledge/nsidc/computations/ice-sheet-input-output.md: each gains
  its executor.skill key, naming the wrapping skill in the cryosphere
  sphere capability that the wrapping rule sends it to,
  land-ice/ice-mass-change and land-ice/ice-sheet-input-output.
  Nothing else changes: no executor, attester, loader or data root is
  touched, and no number moves. Both concepts are stable and signed,
  the input-output computation having been promoted the same day, so
  both owe a re-sign. The capability's first
  release is the pull request these keys resolve against, and the
  placement audit stops reporting the two as unwrapped once it
  merges. Two sentences in the concept bodies, each saying that the
  capability is planned and the computation unwrapped for now, go
  stale with this key and are corrected at the maintainer's re-sign
  rather than here · claude

- 2026-09-19 · STEWARD SIGNING of
  knowledge/nsidc/computations/ice-sheet-input-output.md,
  knowledge/nsidc/recipes/ice-sheet-input-output.md: Coordinator review
  of the attested input-output balance on the maintainer's behalf: the
  attester selftest, the fixture run and its attestation, the window
  refusal exiting 3 and attesting as a refusal, all four loader
  selftests, the data root check and the record run were reproduced,
  every headline number matching the pull request; a tampered discharge
  rate and an edited executor were both rejected with a nonzero exit.
  The record run refuses, because the thickness term sits behind a
  distribution host this environment's egress policy refuses and no NASA
  archive distributes a gridded surface mass balance over grounded ice;
  the concept states both gaps rather than quoting a fixture as an
  anchor, which is why it is promoted on the fixture chain alone, as the
  sea level budget was. The gate set is derived by a recorded rule from
  the velocity mosaics and nothing was placed by hand. Two provider
  findings are carried in the concept and the stamp rather than invented
  as gotchas: the Greenland mosaics carry no floating ice cell, so a
  margin gate is not a grounding line gate; and the user guide's flux
  gate sentence cannot be reconciled with the geometry, so the executor
  divides by the areal scale, states the ground flux, and carries the
  scale per node so the guide's reading can be recovered. The verified
  event is written on the steward's word. (steward)

- 2026-09-19 · knowledge/nsidc/computations/ice-sheet-input-output.md,
  knowledge/nsidc/recipes/ice-sheet-input-output.md,
  knowledge/nsidc/references/computations/ice_sheet_input_output.py,
  knowledge/nsidc/references/attesters/ice_sheet_input_output_check.py,
  knowledge/nsidc/references/loaders/iio_velocity_itslive.py,
  knowledge/nsidc/references/loaders/iio_thickness_bedmachine.py,
  knowledge/nsidc/references/loaders/iio_smb_gemb.py,
  knowledge/nsidc/references/loaders/iio_data_root.py,
  knowledge/nsidc/references/retrieval/ice-sheet-input-output-root/:
  the third estimate of an ice sheet's mass balance, the input-output
  method, as an attested computation with its recipe, its three
  loaders, its stamped data root and its registry entries. The
  executor differences a surface mass balance over the grounded
  domain against a discharge formed node by node across a named flux
  gate set as the ice density times the velocity normal to the gate
  times the node width over the projection's areal scale times the
  thickness; each rate is the mean of its annual epochs with an
  interval on the effective sample size, the mass rate is their
  difference epoch by epoch, the bar is its own half width plus the
  stated gate systematic, and the verdict is whether the rate is
  distinguishable from zero. Ten refusal codes, exit 3 and never a
  number, cover a missing term, a missing gate set, a missing
  velocity epoch family, a gate set that does not span the grounded
  margin, a gate node whose thickness is an interpolation, a gate
  node the thickness mask does not call grounded, a missing grounded
  surface mass balance, a window outside the epochs, too few epochs
  and an interval that cannot be stated. The attester recomputes the
  discharge and the annualisation from the term rows by a second
  implementation, then every rate block, the systematic, the bar and
  the verdict, and its selftest covers two fixture passes, thirteen
  tampers, two wrong releases, all eight fixture refusals, a forged
  refusal and the
  data-root path with its drift, its rewritten manifest and two
  data-root refusals. Fixture anchor (seed 7, Greenland, gate set
  synthetic-outlets, 2005-01 through 2014-12): surface mass balance
  +400.086 and discharge +490.809 gigatonnes per year, mass rate
  minus 90.723 against a bar of 67.518, significant, recovering a
  planted minus 89.0. There is no real-data anchor and the concept
  says so: the committed root carries the real gate velocity term (12
  gates, 286 nodes, 11 annual ITS_LIVE mosaics of 2014 through 2024
  sampled and deleted, only the derived CSV and stamp kept) and
  declares its other two terms absent, so the record run refuses with
  term-not-in-root and attests as a refusal. The two reasons are
  different in kind and both are recorded with their status codes and
  searches in SOURCES.json: the BedMachine granules for both ice
  sheets answered 302 without the Earthdata Login token and 303 with
  it to a content distribution host this environment's egress policy
  refuses at the connection with 403 to the CONNECT, an access gap;
  and no gridded surface mass balance over grounded ice is
  distributed by any NASA archive for either ice sheet, a
  distribution gap. Read on 2026-09-19: the ITS_LIVE Version 2 user
  guide at nsidc.org in full, the project's mosaic catalogue and the
  annual and static listings in the its-live-data bucket, the
  collection and granule records of NSIDC-0776, IDBMG4 and NSIDC-0756
  at cmr.earthdata.nasa.gov, the DataCite resolutions of their three
  DOIs, and the Crossref records of Gardner and others 2018,
  Morlighem and others 2017 and Otosaka and others 2023. The
  published assessment's numbers are cited from this bundle's own
  dataset concept and not restated. Both concepts are drafts with no
  verified event; the computation carries no executor.skill, because
  the land ice capability that would wrap it is still planned, and
  the placement gate reports it as unwrapped. (knowledge-seeder)

- 2026-09-19 · STEWARD SIGNING of
  knowledge/nsidc/datasets/imbie-ice-sheet-assessment.md,
  knowledge/nsidc/datasets/firn-model-air-content.md,
  knowledge/nsidc/gotchas/assessment-method-groups-are-not-independent.md,
  knowledge/nsidc/gotchas/firn-air-content-spread-dominates-the-altimetric-mass-rate.md:
  Maintainer review of the land ice anchors seeded in round four: the
  published multi-method assessment and the firn model air content
  product as dataset concepts, and the two gotchas that qualify them.
  The two datasets and the method-independence gotcha are promoted to
  stable; the high-severity firn spread gotcha carries this first review
  and stays draft for a second. The verified event is written on the
  steward's word. The verified event is written on the steward's word.
  (steward)

- 2026-09-19 · knowledge/nsidc/datasets/imbie-ice-sheet-assessment.md,
  knowledge/nsidc/datasets/firn-model-air-content.md,
  knowledge/nsidc/gotchas/firn-air-content-spread-dominates-the-altimetric-mass-rate.md,
  knowledge/nsidc/gotchas/assessment-method-groups-are-not-independent.md:
  four new drafts, the anchors a land ice capability wrapping the ice
  sheet mass balance closure consults. The first states what the third
  IMBIE assessment reports for each ice sheet over each of its six
  periods and over 1992 to 2020, with its uncertainties, its three
  technique groups and its aggregation; the second states the firn
  model air content term the closure subtracts as the two ITS_LIVE
  elevation change files distribute it, with the model versions
  (GEMB 1.3.0 and GSFC-FDM 1.2.1 for Greenland, a GEMB run forced with
  3-hourly ERA5 for the Antarctic ice shelves), the domains, the
  variable and what its uncertainty rests on. The two gotchas state
  that the firn spread between models is the dominant uncertainty of an
  altimetric mass rate and that the term changes sign inside the record
  (high, with the eval case named on it), and that an assessment's
  method groups share corrections, records and, in one direction, their
  observations, and do not cover the same ice (medium). Sources read on
  2026-09-19: the assessment at essd.copernicus.org in full; the
  Greenland elevation change product's paper at essd.copernicus.org in
  full; the GSFC-FDM description at tc.copernicus.org in full (that host
  is reachable from this session, where the 2026-09-13 entry below
  records it was not from that one, so a reachability note in a log
  entry is a dated observation about one session); the
  NSIDC-0792 version 1 user guide and the NSIDC pages for NSIDC-0792,
  ATL15 version 5 and NSIDC-0776 version 2; the ITS_LIVE project site;
  the Crossref records for the assessment, the Greenland product's
  paper, the ice shelf product's paper, GEMB and GSFC-FDM; and the DOI
  resolutions for the Greenland product, the archived assessment series
  and the assessment software. The GEMB model description at
  gmd.copernicus.org refused the connection at first and was reachable
  later the same day, once the domain was allowed; it was then read in
  full, and the firn concept and the high-severity gotcha carry what it
  says: the model's structure and the choices a run makes, the
  uncertainty sources it names, its firn air content comparison against
  another firn model forced with the same climate data (the two agreeing
  on seasonal and interannual variation and disagreeing on the
  long-term trend, with opposite signs over Antarctica after 2008), and
  its statement that no objective way yet exists to say which model is
  closer to the truth, the test it proposes being the comparison this
  bundle's closure makes. It describes the model as of version 1.0,
  which is not the version either product ran, and the concepts say so.
  The two reference concepts are filed under datasets/ rather
  than directly under references/, which the specification reserves for
  sanctioned code and data roots; the pull request says so for the
  reviewer. Drafts, unsigned. (knowledge-seeder)

- 2026-09-16 · STEWARD RE-SIGNING of
  knowledge/nsidc/computations/ice-sheet-balance.md: Re-signed after the
  placement migration (ADR C): the concept names its executor script in
  executor.resource and carries the data-root layout as its own section;
  the run-instruction reference is retired; no receipt, run id, executor
  or attester changed. The verified event is written on the steward's
  word. The new verified event is appended on the steward's word, the
  earlier events kept as history. (steward)

- 2026-09-16 · knowledge/nsidc/computations/ice-sheet-balance.md: the
  run instructions reference references/skills/run-ice-sheet-balance.md
  is retired under the placement rule (ADR C in the marketplace
  repository: a procedure is a skill in the sphere capability, never a
  signed reference). executor.resource now names the executor script
  itself, whose usage text is the contract; the data-root layout, the
  one part of the retired reference that is contract and not procedure,
  moved into the concept as its own section. The wrapping skill belongs
  to the land-ice capability when that package exists (roadmap
  c6-unwrapped-computations); until then the computation is unwrapped
  and the placement gate reports it so. Status unchanged; the edited
  stable concept is re-signed below on the maintainer's word.
  (coordinator)

- 2026-09-16 · STEWARD SIGNING of
  knowledge/nsidc/computations/ice-sheet-balance.md,
  knowledge/nsidc/recipes/ice-sheet-balance.md,
  knowledge/nsidc/references/skills/run-ice-sheet-balance.md: Maintainer
  review of the attested ice sheet mass balance closure (JPL mascon
  gravimetry against the ITS_LIVE altimetric volume change with the GEMB
  firn term, ATL15 as the intended product awaiting a fetchable
  granule), its recipe and its run skill, merged in PR #176 after the
  coordinator's review of the chain and a fix round (the provider
  comparison sign, the window-dependent closure and the spike
  attribution stated, the data root bound to its RECORD manifest, the
  refusal selftests, the registry runs under the nsidc bundle key).
  Promoted to stable; the check chain is wired into run_checks.sh. The
  verified events are written on the steward's word. The verified event
  is written on the steward's word. (steward)

- 2026-09-15 · ICE SHEET MASS BALANCE CLOSURE seeded (issue 158):
  knowledge/nsidc/computations/ice-sheet-balance.md (type Attested
  Computation, draft), knowledge/nsidc/recipes/ice-sheet-balance.md
  (draft), knowledge/nsidc/references/skills/run-ice-sheet-balance.md,
  the executor references/computations/ice_sheet_balance.py (fixture
  and data-root modes, refusal exit 3), the attester
  references/attesters/ice_sheet_balance_check.py (selftest, and
  --data-root verification of a receipt against the tree), the loaders
  references/loaders/isb_mass_mascons.py (the JPL mascon sum per ice
  sheet with the Greenland selection by the ITS_LIVE ice mask and the
  provider cross-check), isb_volume_atl15.py (ATL15 delta_h summed
  with ice_area; selftest only, the granules being unreachable from
  the drafting environment) and isb_volume_itslive.py (the ITS_LIVE
  elevation change summed over the firn term's cell sets), the
  data-root tool isb_data_root.py extended to the mass and volume
  terms with a closure table, the root
  references/retrieval/ice-sheet-balance-root regenerated with
  mass.csv, volume-itslive.csv, their stamps, RECORD.json and
  SOURCES.json (the firn and smb CSVs byte-identical, their stamps'
  aggregation strings aligned with the loaders' code and the Greenland
  DOI written bare), the bundle-keyed registry entries in
  tools/reference_runs.yaml, and the index's computations and recipes
  sections. Sources read: the JPL mascon CRI granule and the
  provider's Greenland and Antarctica mass series from the PO.DAAC
  archive; the ITS_LIVE Greenland, Antarctic ice shelf and grounded
  Antarctic elevation change files from the ITS_LIVE bucket; the CMR
  records of ATL15 and of the mascon time series collections; Otosaka
  and others 2023 (the IMBIE 2023 assessment) in full through its
  Crossref record and the DOI's landing page; the Crossref records of
  Otosaka and others 2023 and Smith and others 2020. The Greenland
  closure over 2003 through 2016 is anchored to the assessment's
  reconciled rate and technique spread; the Antarctic run refuses for
  want of a grounded firn term and the input-output method is stated
  as an omission. (knowledge seeder)

- 2026-09-15 · STEWARD RE-SIGNING of
  knowledge/nsidc/datasets/bedmachine-greenland-antarctica.md,
  knowledge/nsidc/datasets/icesat2-atl10-freeboard.md,
  knowledge/nsidc/gotchas/bedmachine-thickness-is-interpolated.md,
  knowledge/nsidc/gotchas/bedmachine-mask-and-grounding-line.md,
  knowledge/nsidc/gotchas/atl10-freeboard-is-not-thickness.md,
  knowledge/nsidc/gotchas/atl10-strong-versus-weak-beams.md,
  knowledge/nsidc/gotchas/velocity-mosaic-epochs-and-gaps.md,
  knowledge/nsidc/datasets/its-live-ice-velocity.md: Maintainer review
  of the BedMachine and ATL10 concepts seeded in PR #162 after the
  coordinator's lint and fix round; the two datasets and the two medium
  gotchas promoted to stable, the two high-severity gotchas keep draft
  until a second review; the velocity mosaic gotcha and the ITS_LIVE
  dataset concept re-signed after their text was updated to point at the
  BedMachine concept. The new verified event is appended on the
  steward's word, the earlier events kept as history. (steward)

- 2026-09-15 · coordinator's fix round applied to the BedMachine and
  ATL10 concepts (nasa-daac-knowledge pull request 162, agent-evals
  pull request 24): the gravity inversion and seismic bathymetry are
  now said to supply the cavity bed beneath the floating ice shelves
  (the Antarctic guide's own phrase, gravity inversion and seismic
  bathymetry for grounded ice shelves, is quoted beside it); the
  thickness gotcha's two statements about Gardner and others 2018 are
  reduced to what the registry abstract bears (a discharge is velocity
  times thickness, so its interval carries both factors; the
  reference flux-gate computation is that paper); the mask gotcha no
  longer attributes budget terms to that abstract; the Antarctic
  source data span is given twice with its sources (1970 to 2019 on
  the page and in the guide's temporal section, 1967 to 2020 in the
  guide's campaign table) and recorded as a disagreement; the
  Antarctic dataid line quotes the Version 4 table verbatim and the
  Version 3 label beside it; the retired Greenland Version 5 guide was
  read and its mask value 4 (non-Greenland land), which the Version 6
  table no longer lists, is recorded in the dataset concept and the
  mask gotcha, with a note that no granule was opened to confirm the
  Version 6 file; the 30 m per year mass conservation threshold is
  added to the dataset concept; the ATL10 concept names the Version 7
  geodetic frame in the guide's words with the release 6.1 ITRF2014
  reprocessing kept as history, says which G10016 is which in the
  known issues note's words, states that the near-real-time gotcha it
  links does not name G10016, and states the four-month granule lag
  as observed (the guide's few-updates-a-year note, no pause in the
  known issues note); the strong and weak beam gotcha's incidence
  angle and telemetry window sentences are restated in the note's
  words and footnoted to it; the index introduction now says the six
  new concepts are drafts and the rest are stable. Two stable, signed
  concepts were edited in their text only, status and verified events
  untouched, for the coordinator to re-sign:
  gotchas/velocity-mosaic-epochs-and-gaps.md (description, body and a
  new source entry now point at the BedMachine concept instead of
  saying the bundle does not yet describe it) and
  datasets/its-live-ice-velocity.md (its known-issues line now links
  the BedMachine concept). The seed entry below stands; its eval
  cases are agent-evals pull request 24. (knowledge seeder, on the
  coordinator's fix round)

- 2026-09-15 · BedMachine ice thickness and ICESat-2 ATL10 freeboard
  seeded: two dataset concepts
  (datasets/bedmachine-greenland-antarctica.md,
  datasets/icesat2-atl10-freeboard.md) and four gotchas
  (bedmachine-thickness-is-interpolated and
  atl10-freeboard-is-not-thickness at severity high with their eval
  cases drafted in agent-evals under nsidc/cases/ on the branch
  claude/r3-nsidc-bedmachine-atl10 (agent-evals pull request 24),
  unregistered in any suite manifest until the coordinator's
  follow-up;
  bedmachine-mask-and-grounding-line and
  atl10-strong-versus-weak-beams at severity medium): all drafts, no
  signatures; the index gains a line per concept and its introduction
  now names BedMachine and ATL10 and no longer says BedMachine is
  absent. The brief named BedMachine Greenland Version 5 and
  Antarctica Version 3; both are retired pages (13 January 2026 and
  24 February 2026 in the guides), so the concepts describe Version 6
  (11 December 2025) and Version 4 (21 January 2026) and cite the
  retired pages as such. Sources read the same day: the NSIDC product
  pages for IDBMG4 versions 5 (retired) and 6, NSIDC-0756 versions 3
  (retired) and 4 and ATL10 version 7, with the IDBMG4 Version 6,
  NSIDC-0756 Version 4 and ATL10 Version 7 user guides; the ICESat-2
  sea ice products ATBD release 007 (its background, instrument,
  ATL10 algorithm, multibeam and constraints sections), the ATL07 and
  ATL10 known issues note updated 7 January 2026 and the ATL10
  Version 7 data dictionary; the CMR collection and granule records
  for the three collections; Morlighem and others 2017 and 2020,
  Kwok and others 2019 in JGR Oceans and in GRL and Gardner and
  others 2018 verified against the Crossref registry, with the
  registry abstracts of the 2017, the two 2019 and the 2018 papers
  quoted where a concept quotes them. Not read from the drafting
  session: the Wiley journal pages (bot check), the Nature page
  (outside the domains the seed was permitted to read) and the
  Copernicus page; no granule was opened, so variable names, codes
  and group names come from the guides and the data dictionary.
  Source disagreements recorded in the concepts: the Greenland
  guide's processing section and Version 4 history entry on when
  streamline diffusion replaced kriging (read as one statement); the
  ATL10 guide's coverage section (AMSR2 AU_SI12 by default) against
  the known issues note's 15 January 2026 switch to G10016 Version 4
  (both reported). Kept from the brief as sourced: all four gotchas
  and both datasets, with the strong and weak beam gotcha widened to
  the sc_orient mapping and the beam 3 energy the sources carry.
  (drafted by the knowledge seeder; coordinator review, eval
  registration and roadmap reconciliation pending)

- 2026-09-14 · STEWARD RE-SIGNING of
  knowledge/nsidc/gotchas/sea-ice-pole-hole-by-sensor.md,
  knowledge/nsidc/gotchas/atl15-height-change-is-not-mass-change.md:
  second maintainer review recorded on the maintainer's explicit
  instruction in the coordinator session, the maintainer having reviewed
  the concept; promoted to stable under the two-review rule for high
  severity, with the playbook's preference for a different second
  reviewer noted, and a provider confirmation still invited The new
  verified event is appended on the steward's word, the earlier events
  kept as history. (steward)

- 2026-09-14 · STEWARD SIGNING of
  knowledge/nsidc/datasets/nsidc-0051-sea-ice-concentration.md,
  knowledge/nsidc/datasets/sea-ice-index-g02135.md,
  knowledge/nsidc/gotchas/sea-ice-extent-is-not-area.md,
  knowledge/nsidc/gotchas/sea-ice-nasa-team-versus-bootstrap.md,
  knowledge/nsidc/gotchas/sea-ice-nrt-versus-final.md,
  knowledge/nsidc/gotchas/sea-ice-sensor-transitions.md,
  knowledge/nsidc/gotchas/sea-ice-pole-hole-by-sensor.md: maintainer's
  review of PR 148 recorded on the maintainer's standing instruction for
  round two of seeding; the non-high concepts promoted to stable;
  sea-ice-pole-hole-by-sensor (high severity) keeps draft with this
  first review until a second human review, per the two-review rule. The
  verified event is written on the steward's word. The verified event is
  written on the steward's word. (steward)

- 2026-09-14 · coordinator's lint applied to the sea ice concepts
  (datasets/nsidc-0051-sea-ice-concentration.md,
  datasets/sea-ice-index-g02135.md,
  gotchas/sea-ice-nasa-team-versus-bootstrap.md, this log): the winter
  1987 to 1988 gap is corrected against the Northern Hemisphere daily
  file (N_seaice_extent_daily_v4.0.csv, fetched the same day), which
  carries rows for 1 and 2 December 1987 and resumes on 13 January
  1988, so the NSIDC-0051 concept now dates the unfilled period from
  3 December 1987 (not 2 December) and the Sea Ice Index concept ends
  it on 12 January 1988 (not 13 January), with the Version 4 guide's
  own wording of the gap and the file's rows recorded as a source
  disagreement in that concept's Verification paragraph; the Sea Ice
  Index identity paragraph now states the daily record from
  26 October 1978 and the monthly record from November 1978, as its
  description, version string and the daily file already did; the
  NASA Team gotcha's statement that NSIDC-0803 is a NASA Team product
  is now footnoted to the Sea Ice Index Version 4 guide, which says
  both of its input products are created with the NASA Team
  algorithm, with the Sea Ice Index and NSIDC-0081 left on the help
  article that lists them; the seed entry below now says that NASA
  Technical Memorandum 104647, Comiso and Nishio 2008 and Cavalieri
  and others 1991 were read and are cited by no concept. No title,
  status or signature changed; the digest is re-rendered. Applied by
  the coordinator because the seed session ran out of usage.
  (coordinator; steward review, eval registration and roadmap
  reconciliation pending)

- 2026-09-14 · sea ice concentration and the Sea Ice Index seeded:
  two dataset concepts (datasets/nsidc-0051-sea-ice-concentration.md,
  datasets/sea-ice-index-g02135.md) and five gotchas
  (sea-ice-pole-hole-by-sensor at severity high with its eval case
  drafted in agent-evals under nsidc/cases/ on the branch
  claude/seed-nsidc-sea-ice, unregistered in any suite manifest until
  the coordinator's follow-up; sea-ice-extent-is-not-area,
  sea-ice-nrt-versus-final, sea-ice-nasa-team-versus-bootstrap and
  sea-ice-sensor-transitions at severity medium): all drafts, no
  signatures; the index gains a line per concept and its heading and
  introduction now name sea ice beside land ice. Sources read the
  same day: the NSIDC product pages for NSIDC-0051 version 2,
  NSIDC-0081 version 2 (retired 18 June 2026), NSIDC-0079 version 4,
  NSIDC-0803 version 2 and G02135 versions 3 (retired) and 4, with the
  NSIDC-0051, NSIDC-0081, NSIDC-0079 and G02135 version 3 and 4 user
  guides; NSIDC Special Report 28 and the summary of Special Report
  19; Meier's June 2026 assessment of the AMSR2 sensor change; the
  SMMR, SSM/I and SSMIS sensors summary; the NSIDC help articles on
  the NASA Team and Bootstrap algorithms and on the month-boundary
  extent change; the G02135 tree on noaadata.apps.nsidc.org with the
  daily and monthly CSV headers and the rows quoted in the concepts;
  the product DOIs resolved through doi.org; Cavalieri and others
  1999, Comiso and others 1997, Cavalieri and others 2012 and Meier
  and others 2011 verified against the Crossref registry. Read the
  same day and cited by no concept: NASA Technical Memorandum 104647
  (searched for its spillover threshold only), Comiso and Nishio 2008
  and Cavalieri and others 1991 (both verified against the Crossref
  registry). Not read from the drafting session: the AGU, Wiley,
  Elsevier and IEEE journal pages (bot checks; the papers are cited
  on their registry records and, for Cavalieri 1999, its abstract),
  and no granule or GeoTIFF was opened, so variable names, flag values
  and grid dimensions come from the user guides. Source disagreements
  recorded in the concepts: the SMMR to SSM/I pole hole mask date
  (June/July 1987 in the NSIDC-0051 guide, July/August in the Sea Ice
  Index guide); the NSIDC-0081 coverage start (2024 on the page, 2023
  in the guide); the Sea Ice Index guide's instrument table ending
  F17 at 2022 and its coverage note at 2020 against its data sources
  section and the files carrying NSIDC-0051 through December 2024.
  Kept from the brief as sourced: all five gotchas; the near-real-time
  gotcha is widened to the NSIDC-0803 join because NSIDC-0081 is
  retired and the Sea Ice Index now joins NSIDC-0051 to AMSR2. (drafted
  by the knowledge seeder; coordinator review, eval registration and
  roadmap reconciliation pending)

- 2026-09-13 · STEWARD SIGNING of
  knowledge/nsidc/datasets/icesat2-atl15.md,
  knowledge/nsidc/datasets/its-live-ice-velocity.md,
  knowledge/nsidc/gotchas/atl15-delta-h-reference-epoch.md,
  knowledge/nsidc/gotchas/polar-stereographic-not-latlon.md,
  knowledge/nsidc/gotchas/velocity-mosaic-epochs-and-gaps.md,
  knowledge/nsidc/gotchas/ice-sheet-boundaries-and-drainage-basins.md,
  knowledge/nsidc/gotchas/atl15-height-change-is-not-mass-change.md:
  maintainer's review of PR 129 recorded on the maintainer's
  instruction; the two dataset concepts and the four medium gotchas
  promoted to stable; atl15-height-change-is-not-mass-change (high
  severity) keeps draft with this first review until a second human
  review, per the two-review rule The verified event is written on the
  steward's word. (steward)

- 2026-09-13 · bundle scaffolded with two dataset concepts
  (datasets/icesat2-atl15.md, datasets/its-live-ice-velocity.md) and
  five gotchas (atl15-height-change-is-not-mass-change at severity
  high with its eval case drafted in agent-evals pull request 14 under
  nsidc/cases/, unregistered in any suite manifest until the
  coordinator's follow-up,
  atl15-delta-h-reference-epoch, polar-stereographic-not-latlon,
  velocity-mosaic-epochs-and-gaps and
  ice-sheet-boundaries-and-drainage-basins at severity medium): all
  drafts, no signatures. Sources read the same day: the NSIDC product
  pages for ATL15 version 5, NSIDC-0776 version 2, NSIDC-0725 version
  5, NSIDC-0478 version 2, NSIDC-0484 version 2, NSIDC-0670 version 1
  and NSIDC-0709 version 2 with their user guides; the ATL14/ATL15
  ATBD release 005, the ATL15 data dictionary and the ATL14/15 known
  issues note; the ITS_LIVE project site with its version 1 product
  description and known issues documents; NSIDC's polar stereographic
  projection guide; the GSFC Zwally drainage systems page; the two
  IMBIE assessments in Nature; Smith and others 2020 from the NASA
  technical reports server with its supplement; every DOI against the
  Crossref registry; the CMR collection and granule records. Not
  reachable from the drafting session: science.org, tc.copernicus.org
  (Gardner and others 2018 is cited on its Crossref record and
  abstract), imbie.org, and the Earthdata Cloud granule host, so no
  granule was opened and the ATL15 variable names come from the data
  dictionary. One source disagreement recorded: the ATL15 version 5
  user guide dates the end of cycles 1 and 2 to April 2020 and the
  ATBD release 005 to April 2019; the concepts follow the ATBD. (drafted by the knowledge seeder; coordinator review,
  eval registration and roadmap reconciliation pending)
