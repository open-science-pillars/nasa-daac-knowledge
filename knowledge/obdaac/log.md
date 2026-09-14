# obdaac bundle: change log

Newest first. One line per change: date, concept path, what changed, who.

- 2026-09-14 · SEEDED the bundle's first six concepts, all draft:
  datasets/modis-aqua-l3-chlorophyll.md (MODISA_L3m_CHL 2022.0,
  C3380709133-OB_CLOUD) and datasets/pace-oci-l3-chlorophyll.md
  (PACE_OCI_L3M_BGC 3.2, C4184125847-OB_CLOUD); gotchas
  chlor-a-blended-ocx-and-ci (high, eval case of the same name),
  chlor-a-composite-sampling-gaps (medium),
  chlor-a-one-reprocessing-per-series (medium) and
  chlor-a-is-not-biomass (medium). The Aqua orbit-drift gotcha in the
  seed brief was dropped: no reachable source stated it. Sources read:
  the OB.DAAC chlorophyll ATBD v1.1 (2023-11-06), the PACE OCI version
  1, 2 and 3 processing notes (the last dated April 2026), the OB.DAAC
  ancillary-data document, the CMR collection records and granule
  searches for both products and their near-real-time twins, the
  attribute listings of six mapped files read through OPeNDAP, the
  Earthdata catalog pages the product DOIs resolve to, the Aqua safe
  mode alert, and the Crossref records (with abstracts where present)
  of Hu, Lee and Franz 2012, Hu and others 2019, O'Reilly and Werdell
  2019 and Werdell and others 2019. The OB.DAAC website (product,
  algorithm, reprocessing and R2022 validation pages) redirected to
  the Earthdata landing page and was not read. Index updated, digest
  re-rendered. (knowledge-seeder/claude, issue #138)
- 2026-09-14 · bundle scaffolded empty by tools/scaffold_bundle.py: the index
  with its sections, this log, the check lines and the CODEOWNERS line
  for obdaac-stewards; no concepts yet. (maintainer)
