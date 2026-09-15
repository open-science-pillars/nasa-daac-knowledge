# ornldaac bundle: change log

Newest first. One line per change: date, concept path, what changed, who.

- 2026-09-15 · GEDI concepts revised on the coordinator's fix round
  (pull request 168): gotchas/gedi-latitude-limits.md (the off-track
  pointing margin is a fraction of a degree, the 56 north and 53 south
  rectangle is a catalog extent no source read explains, and the
  wrong-result trap is a search box lying wholly north of about 52);
  datasets/gedi-l4b-gridded-biomass.md (names L4A Version 2.1 as the
  footprint input the Version 2 guide cites, states by the publication
  dates that the Version 2.1 grid predates the Version 3 models and
  flags, cites the Version 3 guide directly for the beam sensitivity
  thresholds, records the 35 stratum codes against the 32 modeled
  strata, and separates the zero cells from the -9999 no-data value);
  gotchas/gedi-quality-and-degrade-flags.md (title and correct approach
  now say degrade_include_flag names the codes the L4B algorithm admits
  rather than that the shipped grid was built on that sample; the
  l4a_quality_flag_rel3 definition quotes the guide's spelling; a
  wrong-version filter fails on the missing dataset);
  gotchas/gedi-biomass-is-a-model-output.md (the 50.7 percent figure is
  the global land-area-weighted figure, not per stratum; the L4B 2.1
  grid predates the Version 3 refit); gotchas/gedi-footprint-is-not-a-pixel.md
  and gotchas/gedi-l4b-standard-error.md (Patterson and others' 20
  percent under-statement stated as a simulation result at six United
  States sites; the sentences that extend it are marked as this
  bundle's reasoning); datasets/gedi-l4a-footprint-biomass.md (the 35
  combinations against 32 strata, the flag definition spelling, the L4B
  2.1 grid's date). The L4B Version 2.1 user guide PDF remained
  unreadable (content delivery host blocked; the daac.ornl.gov data
  path requires an Earthdata login this seed does not use). All still
  drafts, no signatures. (seeder)

- 2026-09-15 · GEDI L4A and L4B biomass, round three of seeding
  (nasa-daac-knowledge issue 155): two dataset concepts
  (datasets/gedi-l4a-footprint-biomass.md for Version 3, with Version
  2.1 recorded as the complete prior collection, and
  datasets/gedi-l4b-gridded-biomass.md for Version 2.1) and five
  gotchas (gedi-footprint-is-not-a-pixel at severity high with its eval
  case drafted in agent-evals under gedi/cases/, unregistered in any
  suite manifest until the coordinator's follow-up;
  gedi-l4b-standard-error, gedi-quality-and-degrade-flags and
  gedi-biomass-is-a-model-output at severity medium; gedi-latitude-limits
  at severity low): all drafts, no signatures. Sources read the same
  day: the ORNL DAAC user guide for GEDI L4A Version 3 (revision
  2026-09-02) and the L4A Version 3 landing page; the L4A Version 2.1
  and L4B Version 2.1 landing pages, read at their Earthdata catalog
  redirects; the ORNL DAAC user guide for GEDI L4B Version 2 (revision
  2022-04-26, the readable layer documentation); the CMR collection
  search for GEDI at ORNL_CLOUD, the collection records and granule
  searches for L4A Version 3, L4A Version 2.1 and L4B Version 2.1, and
  the collection record for the circumpolar boreal biomass product from
  ICESat-2; the doi.org handle records for the three dataset DOIs; the
  Crossref records, with abstracts, for Dubayah and others 2022
  (Environmental Research Letters), Kellner and others 2023 (Earth and
  Space Science) and Patterson and others 2019 (Environmental Research
  Letters). Not readable from the drafting session: the L4A Version 3
  and L4B Version 2.1 user guide PDFs, the L4A and L4B algorithm
  theoretical basis documents and the data dictionaries on
  data.ornldaac.earthdata.nasa.gov (they redirect to a content delivery
  host the environment blocks; the versioned guide URLs on
  daac.ornl.gov redirect there too), the DataCite metadata behind
  doi.org content negotiation, and the journal article pages. (seeder)

- 2026-09-14 · STEWARD RE-SIGNING of
  knowledge/ornldaac/gotchas/daymet-365-day-year.md: second maintainer
  review recorded on the maintainer's explicit instruction in the
  coordinator session, the maintainer having reviewed the concept;
  promoted to stable under the two-review rule for high severity, with
  the playbook's preference for a different second reviewer noted, and a
  provider confirmation still invited The new verified event is appended
  on the steward's word, the earlier events kept as history. (steward)

- 2026-09-14 · STEWARD SIGNING of
  knowledge/ornldaac/datasets/daymet-v4.md,
  knowledge/ornldaac/gotchas/daymet-lcc-projection-and-cell-area.md,
  knowledge/ornldaac/gotchas/daymet-station-sparse-error.md,
  knowledge/ornldaac/gotchas/daymet-tiles-mosaics-regions.md,
  knowledge/ornldaac/gotchas/daymet-v4-r1-correction.md,
  knowledge/ornldaac/gotchas/daymet-365-day-year.md: maintainer's review
  of PR 143 recorded on the maintainer's standing instruction for round
  two of seeding; the non-high concepts promoted to stable;
  daymet-365-day-year (high severity) keeps draft with this first review
  until a second human review, per the two-review rule. The verified
  event is written on the steward's word. The verified event is written
  on the steward's word. (steward)

- 2026-09-14 · concepts revised on the coordinator's lint, applied by the
  coordinator because the seed session ran out of usage:
  gotchas/daymet-lcc-projection-and-cell-area.md (the sign and
  magnitudes of the cell-count area bias in the wrong-result paragraph
  and the severity comment now follow the areal scale factors; the
  subset box is rectangular, not square, in the projection);
  gotchas/daymet-365-day-year.md (the title now names a positional or
  generated-date join as what misaligns, since a calendar-date join is
  the fix; the description says the positional join fails on a 365-day
  assumption); gotchas/daymet-v4-r1-correction.md (R1 changed no
  earlier year rather than nothing else, since 2022 onward exists only
  in R1); datasets/daymet-v4.md (the R1 description and known-issues
  lines match the new wording, and the Version 3 parenthetical says
  1.75 was the tmax error, tmin unchanged); index.md lines match the
  new titles. All still drafts, no signatures. (coordinator)

- 2026-09-14 · first concepts of the bundle, Daymet Version 4 (release
  R1): one dataset concept (datasets/daymet-v4.md) and five gotchas
  (daymet-365-day-year at severity high with its eval case drafted in
  agent-evals under daymet/cases/, unregistered in any suite manifest
  until the coordinator's follow-up; daymet-lcc-projection-and-cell-area,
  daymet-tiles-mosaics-regions and daymet-v4-r1-correction at severity
  medium; daymet-station-sparse-error at severity low): all drafts, no
  signatures. Sources read the same day: the ORNL DAAC user guides for
  Daymet Daily Version 4 and for the Version 4 station-level
  cross-validation dataset, the Version 4 landing page with its
  superseding notice; the Daymet project site's description, get data,
  web services, citations and tile selection tool retirement pages; the
  CMR collection search for Daymet, the collection records for the R1
  daily and cross-validation collections and the R1 daily granule
  search; Thornton and others 2021 in Scientific Data, read in full at
  nature.com and verified against its Crossref record. Not reachable
  from the drafting session: the Version 4 R1 landing pages, user guide
  PDFs and dataset lister (the DAAC redirects them to earthdata.nasa.gov
  hosts outside the sources consulted, and the proxy refuses those
  hosts), a separate R1 release notes document (none found on
  daac.ornl.gov; the R1 statement rests on the CMR abstracts and the
  Version 4 landing page), and the THREDDS catalogs (redirected to
  opendap.earthdata.nasa.gov); no data file was opened. The projection
  gotcha's cell-area figures are computed from the guide's PROJ string
  with PROJ 9.5.1, not quoted from a Daymet document. (drafted by the
  knowledge seeder; coordinator review, eval registration and roadmap
  reconciliation pending)

- 2026-09-14 · bundle scaffolded empty by tools/scaffold_bundle.py: the index
  with its sections, this log, the check lines and the CODEOWNERS line
  for ornldaac-stewards; no concepts yet. (maintainer)
