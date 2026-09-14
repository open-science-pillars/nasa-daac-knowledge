# lpdaac bundle: change log

Newest first. One line per change: date, concept path, what changed, who.

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
  check and the paper is cited on its registry record). Recorded for
  the reviewer: the user guide and the project site disagree on the
  within-zone tile overlap (8 to 10 km against 4,900 m), and the LP DAAC
  product page calls the file-name timestamp a production time where
  the guide calls it the input sensing time; the concepts quote both.
  The podaac bundle's OPERA DSWx-HLS concept is named, not repeated.
  (knowledge-seeder)

- 2026-09-14 · bundle scaffolded empty by tools/scaffold_bundle.py: the index
  with its sections, this log, the check lines and the CODEOWNERS line
  for lpdaac-stewards; no concepts yet. (maintainer)
