# nsidc bundle: change log

Newest first. One line per change: date, concept path, what changed, who.

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
  extent change; NASA Technical Memorandum 104647 (searched, its
  spillover threshold only); the G02135 tree on
  noaadata.apps.nsidc.org with the daily and monthly CSV headers and
  the rows quoted in the concepts; the product DOIs resolved through
  doi.org; Cavalieri and others 1999, Comiso and others 1997,
  Cavalieri and others 2012, Meier and others 2011, Comiso and Nishio
  2008 and Cavalieri and others 1991 verified against the Crossref
  registry. Not read from the drafting session: the AGU, Wiley,
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
