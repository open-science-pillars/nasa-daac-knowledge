# lpdaac bundle: change log

Newest first. One line per change: date, concept path, what changed, who.

- 2026-09-15 · STEWARD SIGNING of
  knowledge/lpdaac/datasets/mod13-vegetation-indices.md,
  knowledge/lpdaac/datasets/mod15-lai-fpar.md,
  knowledge/lpdaac/datasets/mod17-gpp-npp.md,
  knowledge/lpdaac/gotchas/composite-day-of-year-layer.md,
  knowledge/lpdaac/gotchas/index-is-not-a-state-variable.md,
  knowledge/lpdaac/gotchas/lai-and-gpp-are-model-outputs.md,
  knowledge/lpdaac/gotchas/sinusoidal-grid-cell-area.md: Maintainer
  review of the MODIS vegetation concepts (MOD13 vegetation indices,
  MOD15 LAI and FPAR, MOD17 GPP and NPP, and four gotchas), merged in PR
  #172 after the coordinator's lint and fix round. Six concepts are
  promoted to stable; the high-severity index-is-not-a-state-variable
  gotcha keeps status draft with this one review until the maintainer's
  second review. Severity calls recorded: the sinusoidal grid gotcha at
  low and the composite day gotcha at medium follow the seed brief
  although both wrong-result modes are silent; raising either later owes
  an eval case. The verified events are written on the steward's word.
  The verified event is written on the steward's word. (steward)

- 2026-09-15 · fix round on the MODIS vegetation drafts (PR 172): the
  index gotcha's arithmetic corrected (0.67 to 0.82 is about 22 per
  cent, the NDVI step for a ratio doubling from 10 to 20 about 0.09,
  0.08 on the ATBD's rounded values); the fill-code statements in the
  model outputs gotcha and the MOD15 and MOD17 concepts now rest on the
  MOD17 guide's statement that the file attribute names one fill while
  seven exist, with the catalog pages re-read (they render one value)
  and the CMR variable records for the collections added as sources
  (they list all seven codes); the day of year gotcha's title softened
  to "the period's date, not the observation's" because the MOD13 guide
  states no start-day convention; the MOD17 BPLUT minimum temperature
  column stated as -8 to -6 with -7 for mixed forest; the annual NPP
  formula parenthesised in the description; a CMR granule query added
  showing no 2000 granules in MOD17A3HGF against the guide's caution
  about 2000; the MOD15 uncertainty opening no longer generalises about
  the product family; the MOD15 gpp-guide source title names section
  2.4.2; the MOD13 tile size carries the projection-metre figure the
  grid gotcha derives. All still drafts. (knowledge-seeder)

- 2026-09-15 · MODIS vegetation indices, LAI and FPAR, GPP and NPP, the
  bundle's third seed (issue 159): three dataset concepts
  (datasets/mod13-vegetation-indices.md, datasets/mod15-lai-fpar.md,
  datasets/mod17-gpp-npp.md) and four gotchas
  (gotchas/index-is-not-a-state-variable.md at severity high with its
  eval case index-is-not-a-state-variable drafted in agent-evals under
  modis-land/cases/ and unregistered in any suite manifest until the
  coordinator's follow-up; gotchas/composite-day-of-year-layer.md and
  gotchas/lai-and-gpp-are-model-outputs.md at severity medium;
  gotchas/sinusoidal-grid-cell-area.md at severity low): all drafts, no
  signatures, spheres biosphere and geosphere. Sources read the same
  day: the LP DAAC product pages for MOD13Q1, MOD13A1, MOD15A2H,
  MOD17A2H and MOD17A3HGF v061 (each redirecting to its Earthdata
  catalog page, the variables tables read for every layer), the MODIS
  Vegetation Index User's Guide version 3.10 (September 2019) with its
  Collection 6.1 cover note, the MOD13 ATBD version 3 (April 1999), the
  Collection 6.1 LAI/FPAR User's Guide (April 2020), the MOD15 ATBD
  version 4.0 (April 1999), the MOD17 User's Guide version 1.1 (March
  2021), the MOD17 ATBD version 3.0 (April 1999), the CMR collection
  records for the five products and, for one field, MOD17A2HGF, the
  doi.org resolution of the five product DOIs (DataCite, no Crossref
  record) and the Crossref records of Huete and others 2002, Myneni and
  others 2002 and Running and others 2004 (the Elsevier and Oxford
  University Press pages are on domains outside the seed's reading
  list and the papers are cited on their registry records). Recorded
  for the reviewer: the Collection 6.1 MOD17A2H record begins
  2021-01-01 on the product page and the CMR record while the guide
  describes eight-day products from 2000, the pre-2021 record being the
  gap-filled MOD17A2HGF collection; the MOD15 guide gives fill ranges
  (249 to 255, 248 to 255) where the product page names one fill per
  layer, and the MOD17 guide seven fill codes per layer where the
  pages name one; the MOD13 guide's cover note names MCD12 and the
  MOD17 guide's text under Table 4.1 gives a net photosynthesis range
  of -3000 to 3000 against the table's -30000 to 30000, both read as
  copying slips; the MOD15 guide dates the Terra record from February
  18, 2000 and the MOD17 guide from 2000-02-28; the sinusoidal cell
  size (463.31 m) and area (0.2147 square kilometres) are derived from
  the guide's sphere radius and tile size and said to be derived; the
  MOD13 period naming (file day is the first day of the period) is
  inferred from the example file names and the MOD17 convention and
  said to be inferred. The LDOPE known issues site and the LAADS file
  specifications are on domains outside the reading list and were not
  read. The hydrology plugin's MOD16 concept is named, not repeated.
  (knowledge-seeder)

- 2026-09-15 · STEWARD SIGNING of knowledge/lpdaac/datasets/nasadem.md,
  knowledge/lpdaac/datasets/mod11-land-surface-temperature.md,
  knowledge/lpdaac/gotchas/nasadem-orthometric-versus-ellipsoidal.md,
  knowledge/lpdaac/gotchas/nasadem-void-fill-and-source-layer.md,
  knowledge/lpdaac/gotchas/mod11-clear-sky-and-view-time.md,
  knowledge/lpdaac/gotchas/mod11-day-and-night-are-different.md,
  knowledge/lpdaac/gotchas/mod11-emissivity-is-classified.md: Maintainer
  review of the NASADEM and MOD11 concepts seeded in PR #164 after the
  coordinator's lint and fix round; the two datasets and the medium and
  low gotchas promoted to stable, the two high-severity gotchas keep
  draft until a second review. The verified event is written on the
  steward's word. (steward)

- 2026-09-15 · fix round on the NASADEM and MOD11 drafts (PR 164): the
  MOD11A2 Clear_sky_days and Clear_sky_nights layers are now described
  as one flag bit per day rather than counts, on the guide's statement
  for the monthly product and the product page's bit field label, with
  the bit-to-day assignment recorded as unconfirmed (the file
  specification is off the reading list); the datum gotcha names the
  ellipsoidal cases (GNSS, ICESat and ICESat-2, altimetry, lidar) in
  place of a generalisation and cites the ASTER GDEM guide for that
  product's geoid reference; the void gotcha's title is qualified to
  the HGT granule and its NUM bands corrected to 231 to 234 and 241 to
  246; the NASADEM concept restricts the flat binary statement to the
  binary groupings and cites the NC and NUMNC file sizes; the
  emissivity gotcha quotes the representable range 0.492 to 1.0; the 15
  arc second EGM96 posting is kept as the guide states it. All still
  drafts. (knowledge-seeder)

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
