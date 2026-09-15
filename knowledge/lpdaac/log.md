# lpdaac bundle: change log

Newest first. One line per change: date, concept path, what changed, who.

- 2026-09-15 · NASADEM and MOD11 land surface temperature, the bundle's
  second seed (issue 154): two dataset concepts (datasets/nasadem.md,
  datasets/mod11-land-surface-temperature.md) and five gotchas
  (gotchas/nasadem-orthometric-versus-ellipsoidal.md at severity high
  with its eval case nasadem-orthometric-versus-ellipsoidal and
  gotchas/mod11-clear-sky-and-view-time.md at severity high with its
  eval case mod11-clear-sky-and-view-time, both cases drafted in
  agent-evals under nasadem/cases/ and unregistered in any suite
  manifest until the coordinator's follow-up;
  gotchas/nasadem-void-fill-and-source-layer.md and
  gotchas/mod11-day-and-night-are-different.md at severity medium;
  gotchas/mod11-emissivity-is-classified.md at severity low): all
  drafts, no signatures, spheres geosphere on NASADEM and geosphere and
  biosphere on MOD11. Sources read the same day: the LP DAAC product
  pages for NASADEM_HGT, NASADEM_SHHP, MOD11A1 and MOD11A2 (each
  redirecting to its Earthdata catalog page), the NASADEM user guide
  version 1.3 (January 2025), the LP DAAC DEM Product Comparison Guide,
  the SRTM Collection User Guide (October 2015) and the ASTER GDEM
  version 3 user guide for one statement each, the Collection-6 MODIS
  LST Products Users' Guide (June 2019) with its Collection 6.1 cover
  note, the MODIS LST ATBD version 3.3 (1999), the CMR collection
  records for NASADEM_HGT, NASADEM_SHHP, NASADEM_NC, NASADEM_NUMNC,
  NASADEM_SC, NASADEM_SIM, MOD11A1 and MOD11A2, the doi.org resolution
  of the five product DOIs (DataCite, no Crossref record) and the
  Crossref record of Wan 2014 (the Elsevier page is on a domain outside
  the seed's reading list and the paper is cited on its registry
  record). Recorded for the reviewer: the MOD11 user guide and the
  MOD11A1 product page differ on what a cell holds above 30 degrees
  latitude when several clear observations exist in a day (one
  observation chosen by view angle against an average of all), the
  guide's Table 14 mislabels the eight-day Night_view_time, and no
  source read gives the global range of the EGM96 undulation, so the
  datum gotcha quotes the guide's own coastal example instead of a
  global figure. The LDOPE known issues site and the LAADS file
  specifications are on domains outside the reading list and were not
  read. (knowledge-seeder)

- 2026-09-14 · STEWARD RE-SIGNING of
  knowledge/lpdaac/gotchas/hls-fmask-is-bit-packed.md: second maintainer
  review recorded on the maintainer's explicit instruction in the
  coordinator session, the maintainer having reviewed the concept;
  promoted to stable under the two-review rule for high severity, with
  the playbook's preference for a different second reviewer noted, and a
  provider confirmation still invited The new verified event is appended
  on the steward's word, the earlier events kept as history. (steward)

- 2026-09-14 · STEWARD SIGNING of knowledge/lpdaac/datasets/hls-l30.md,
  knowledge/lpdaac/datasets/hls-s30.md,
  knowledge/lpdaac/gotchas/hls-band-names-differ.md,
  knowledge/lpdaac/gotchas/hls-harmonized-not-native.md,
  knowledge/lpdaac/gotchas/hls-mgrs-tile-overlap.md,
  knowledge/lpdaac/gotchas/hls-scale-and-fill.md,
  knowledge/lpdaac/gotchas/hls-fmask-is-bit-packed.md: maintainer's
  review of PR 145 recorded on the maintainer's standing instruction for
  round two of seeding; the non-high concepts promoted to stable;
  hls-fmask-is-bit-packed (high severity) keeps draft with this first
  review until a second human review, per the two-review rule. The
  verified event is written on the steward's word. The verified event is
  written on the steward's word. (steward)

- 2026-09-14 · the bundle's first concepts, HLS version 2.0: two dataset
  concepts (datasets/hls-l30.md, datasets/hls-s30.md) and five gotchas
  (gotchas/hls-fmask-is-bit-packed.md at severity high with its eval
  case hls-fmask-is-bit-packed drafted in agent-evals under hls/cases/,
  unregistered in any suite manifest until the coordinator's follow-up;
  gotchas/hls-band-names-differ.md, gotchas/hls-harmonized-not-native.md
  and gotchas/hls-mgrs-tile-overlap.md at severity medium;
  gotchas/hls-scale-and-fill.md at severity low): all drafts, no
  signatures, spheres biosphere and geosphere. Sources read the same
  day: the LP DAAC product pages for HLSL30 and HLSS30 v2.0, the HLS
  Product User Guide v2.0 (April 2026), the L30 and S30 known issues
  documents (April 2026), the HLS project site (product description,
  L30, S30, tiling system and algorithms pages), the CMR collection
  records C2021957657-LPCLOUD and C2021957295-LPCLOUD, and the Crossref
  record of Claverie and others 2018 (the Elsevier page is behind a bot
  check and the paper is cited on its registry record), plus the HLS
  Quick Guide for the Earthdata Login requirement. Recorded for
  the reviewer: the user guide and the project site give different
  within-zone tile overlap figures (8 to 10 km against 4,900 m, the
  second half the first, possibly two measures of one geometry), and the LP DAAC
  product page calls the file-name timestamp a production time where
  the guide calls it the input sensing time; the concepts quote both.
  The podaac bundle's OPERA DSWx-HLS concept is named, not repeated.
  (knowledge-seeder)

- 2026-09-14 · bundle scaffolded empty by tools/scaffold_bundle.py: the index
  with its sections, this log, the check lines and the CODEOWNERS line
  for lpdaac-stewards; no concepts yet. (maintainer)
