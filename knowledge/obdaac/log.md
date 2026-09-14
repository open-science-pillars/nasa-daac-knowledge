# obdaac bundle: change log

Newest first. One line per change: date, concept path, what changed, who.

- 2026-09-14 · REVISED the six seeded concepts on the coordinator's
  lint, applied by the coordinator because the seed session ran out of
  usage: the log's reason for dropping the orbit-drift gotcha now
  names the Aqua Project Science page and the missing effect on the
  record; datasets/modis-aqua-l3-chlorophyll.md gains the drift as a
  platform fact in Known issues with a new source (aqua-project) and
  footnote, and its cmr-granules source title loses a record count;
  index.md says where the eval cases for the high-severity gotchas
  live; gotchas/chlor-a-is-not-biomass.md loses an uncited
  parenthetical on the variable's history; the PACE record is now
  described as five versions (four reprocessings) in
  gotchas/chlor-a-one-reprocessing-per-series.md and
  datasets/pace-oci-l3-chlorophyll.md, and the MODIS-Aqua file name is
  said to carry no version token; gotchas/chlor-a-blended-ocx-and-ci.md
  notes the ATBD's 0.25 and 0.35 edges beside Hu 2019's 0.25 to 0.40;
  gotchas/chlor-a-composite-sampling-gaps.md says low-sun retrievals
  are flagged and masked rather than not attempted. Digest
  re-rendered. (coordinator/claude, issue #138)
- 2026-09-14 · SEEDED the bundle's first six concepts, all draft:
  datasets/modis-aqua-l3-chlorophyll.md (MODISA_L3m_CHL 2022.0,
  C3380709133-OB_CLOUD) and datasets/pace-oci-l3-chlorophyll.md
  (PACE_OCI_L3M_BGC 3.2, C4184125847-OB_CLOUD); gotchas
  chlor-a-blended-ocx-and-ci (high, eval case of the same name),
  chlor-a-composite-sampling-gaps (medium),
  chlor-a-one-reprocessing-per-series (medium) and
  chlor-a-is-not-biomass (medium). The Aqua orbit-drift gotcha in the
  seed brief was dropped: the Aqua Project Science page
  (https://aqua.nasa.gov/, read 2026-09-14) states that Aqua has been
  in free drift since its last drag make-up maneuver in December 2021
  and is drifting to later equatorial crossing times, but no reachable
  producer source states the effect of the drift on the chlorophyll
  record, which is what a gotcha's mechanism needs, so the drift is
  recorded as a platform fact in the MODIS-Aqua dataset concept and
  not as a gotcha. Sources read:
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
