# nsidc bundle: change log

Newest first. One line per change: date, concept path, what changed, who.

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
