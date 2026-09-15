# nsidc bundle: change log

Newest first. One line per change: date, concept path, what changed, who.

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
