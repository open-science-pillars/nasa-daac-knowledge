# gesdisc bundle: change log

Newest first. One line per change: date, concept path, what changed, who.

- 2026-09-15 · third seed, OCO-2 solar-induced fluorescence and the
  GES DISC subsetter: one dataset concept (datasets/oco2-sif-lite.md,
  the OCO2_L2_Lite_SIF 11r and 11.2r and OCO3_L2_Lite_SIF 11r daily
  sounding files with their two retrieval bands, the derived 740 nm
  field, the barren-surface offset, the quality flag, the daily
  correction factor and the one-sigma uncertainties), four gotchas
  (sif-is-not-photosynthesis at severity high with its eval case
  drafted in agent-evals under oco2/cases/, unregistered in any suite
  manifest until the coordinator's follow-up; sif-two-bands-and-offsets
  and sif-soundings-are-sparse at severity medium;
  sif-daily-correction at severity low) and one connector concept
  (connectors/gesdisc-subsetter-opendap.md: Cloud OPeNDAP, the Harmony
  enterprise subsetter, the retiring JSON-WSP subsetter and
  on-premises OPeNDAP, the bearer token, what leaves the machine and
  the failure modes, with stale_after set three months out to match
  the September 2026 retirements): all drafts, no signatures. Sources
  read the same day: the CMR collection, UMM, granule and service
  records for OCO2_L2_Lite_SIF 11r and 11.2r, OCO3_L2_Lite_SIF 11r,
  M2T1NXSLV and AIRS3STD 7.0 (GES_DISC provider); the JPL SIF Data
  User's Guide for Lite file version 11 and 11.2 (July 2025) and the
  build 10 product description (2021), the GES DISC OCO README
  (2021), the OCO-2 v11.2 and OCO-3 v11 data release statements and
  the OCO-3 known data issues, all on the GES DISC document server or
  the collection's OPeNDAP document directory; the DAP4 metadata of
  the OCO-2 granule of 2024-04-02 on the on-premises Hyrax server and
  the credential redirect of the same request on Cloud OPeNDAP; the
  GES DISC how-tos, alerts, glossary, FAQ and documents on OPeNDAP in
  the cloud, wget and curl with a bearer token, the Level 3 and 4
  subsetter, the enterprise Level 2 subsetter, prerequisite files,
  download problems, Earthdata Login registration, and the 2026
  retirement and migration notices, read through the site's content
  API because the pages are script-rendered; the JSON-WSP description
  of the subsetting service; the OCO-2 project's data center and
  publications pages; and the Crossref registry records of Doughty
  and others 2022, Sun and others 2017 and 2018, Frankenberg and
  others 2011 (the GOSAT patterns paper), 2012 and 2014, Parazoo and others 2019 and
  Magney and others 2019 (both). Not reached: the OCO-2 project's own
  SIF product page (the site has none; its product-info and
  science/sif paths answer 404), the publisher pages of the Elsevier
  and AGU papers (bot check, or a 403 from the proxy on doi.org
  redirects; records and abstracts read on Crossref instead, the Sun
  2018 record carrying no abstract), and the GES DISC how-to
  notebooks hosted on GitHub (outside the source list). The MERRA-2,
  AIRS and OMI concepts are linked from the connector, not restated.
  (knowledge-seeder)

- 2026-09-15 · STEWARD SIGNING of
  knowledge/gesdisc/datasets/airs-l3-temperature-humidity.md,
  knowledge/gesdisc/datasets/omi-no2-and-ozone.md,
  knowledge/gesdisc/gotchas/airs-pressure-levels-and-surface-mask.md,
  knowledge/gesdisc/gotchas/omi-row-anomaly.md,
  knowledge/gesdisc/gotchas/airs-ascending-descending-nodes.md,
  knowledge/gesdisc/gotchas/l3-count-field-bounds-a-cell.md,
  knowledge/gesdisc/gotchas/anomaly-names-its-climatology-period.md:
  Maintainer review of the AIRS and OMI concepts seeded in PR #161 after
  the coordinator's lint and fix round; the two datasets and the medium
  and low gotchas promoted to stable, the two high-severity gotchas keep
  draft until a second review. The verified event is written on the
  steward's word. (steward)

- 2026-09-15 · second seed, AIRS profiles and OMI trace gases: two
  dataset concepts (datasets/airs-l3-temperature-humidity.md, the
  version 7 daily and monthly 1 degree grids AIRS3STD and AIRS3STM
  with their nodes, levels, count and standard deviation fields;
  datasets/omi-no2-and-ozone.md, the OMNO2d and OMTO3d daily grids
  with OMTO3e and OMDOAO3e as siblings) and five gotchas
  (airs-pressure-levels-and-surface-mask and omi-row-anomaly at
  severity high with their eval cases drafted in agent-evals under
  airs/cases/, unregistered in any suite manifest until the
  coordinator's follow-up; airs-ascending-descending-nodes and
  l3-count-field-bounds-a-cell at severity medium;
  anomaly-names-its-climatology-period at severity low): all drafts,
  no signatures. Sources read the same day: the CMR collection, UMM
  and granule records for AIRS3STD, AIRS3STM, AIRS3SPD, AIRS3SPM
  (versions 7.0 and 006), OMNO2d, OMTO3d, OMTO3e, OMDOAO3e, OMNO2,
  OMTO3 and OMDOAO3 (GES_DISC provider), the product DOIs resolved on
  doi.org; the GES DISC collection pages for AIRS3STD 7.0, AIRS3STM
  7.0, OMNO2d 004 and OMTO3d 004 (script-rendered, read through their
  CMR records); the JPL AIRS Version 7 Level 3 Product User Guide
  (April 2020), the AIRS documentation index, the deep space
  manoeuvre impact report (December 2025), the DC restore anomaly
  memo (March 2026) and the data outages list (April 2026), all on
  the GES DISC document server because the AIRS JPL product pages
  return 404; the OMI Data User's Guide (2012), the OMNO2 READMEs for
  versions 4.0 (2019) and 5.0 (2024), the OMNO2d and OMTO3d file
  specifications (2013 and 2024) and the OMTO3d README (2009); the
  Crossref registry records of Susskind and others 2014, Kahn and
  others 2014, Ding and others 2020, Lamsal and others 2021, Levelt
  and others 2006 and 2018, Dobber and others 2006 and Schenkeveld
  and others 2017. Not reached: the Aura project site (redirects to
  NASA Science, no row anomaly page), the OMTO3d and OMTO3e version
  004 README text files (access prompt), and the KNMI row anomaly
  pages the OMI documents point to (outside the source list). The
  MERRA-2 concepts are linked where AIRS is compared with the
  reanalysis, not restated. (knowledge-seeder)

- 2026-09-14 · STEWARD RE-SIGNING of
  knowledge/gesdisc/gotchas/merra2-prectotcorr-versus-prectot.md: second
  maintainer review recorded on the maintainer's explicit instruction in
  the coordinator session, the maintainer having reviewed the concept;
  promoted to stable under the two-review rule for high severity, with
  the playbook's preference for a different second reviewer noted, and a
  provider confirmation still invited The new verified event is appended
  on the steward's word, the earlier events kept as history. (steward)

- 2026-09-14 · STEWARD SIGNING of knowledge/gesdisc/datasets/merra-2.md,
  knowledge/gesdisc/gotchas/merra2-collection-short-names.md,
  knowledge/gesdisc/gotchas/merra2-grid-weights.md,
  knowledge/gesdisc/gotchas/merra2-stream-boundaries-and-discontinuities.md,
  knowledge/gesdisc/gotchas/merra2-time-stamp-conventions.md,
  knowledge/gesdisc/gotchas/merra2-prectotcorr-versus-prectot.md:
  maintainer's review of PR 144 recorded on the maintainer's standing
  instruction for round two of seeding; the non-high concepts promoted
  to stable; merra2-prectotcorr-versus-prectot (high severity) keeps
  draft with this first review until a second human review, per the
  two-review rule. The verified event is written on the steward's word.
  The verified event is written on the steward's word. (steward)

- 2026-09-14 · bundle's first concepts: one dataset concept
  (datasets/merra-2.md, the reanalysis as its GES DISC file
  collections with their CMR concept ids and DOIs) and five gotchas
  (merra2-prectotcorr-versus-prectot at severity high with its eval
  case drafted in agent-evals under merra2/cases/, unregistered in any
  suite manifest until the coordinator's follow-up;
  merra2-time-stamp-conventions, merra2-stream-boundaries-and-discontinuities
  and merra2-collection-short-names at severity medium;
  merra2-grid-weights at severity low): all drafts, no signatures.
  Sources read the same day: the CMR collection and granule records
  for eighteen MERRA-2 short names (GES_DISC provider); the GES DISC
  collection pages for M2T1NXSLV, M2T1NXFLX, M2TMNXSLV and M2I1NXASM
  (script-rendered, read through their CMR records); the GES DISC
  README Document for MERRA-2 Data Products (revised 2021-03-01) and
  the Records of MERRA-2 Data Reprocessing and Service Changes; the
  GMAO File Specification (Office Note 9, version 1.1), the GMAO
  documentation, FAQ and citing pages, and three technical memoranda
  (Bosilovich and others 2015 volume 43, McCarty and others 2016
  volume 46, Reichle and Liu 2014 volume 35); the Crossref registry
  records and abstracts of Gelaro and others 2017, Reichle and others
  2017 (both papers) and Bosilovich and others 2017, whose journal
  pages sit behind a bot check. The hydrology plugin's IMERG and
  NLDAS-2 concepts are named, not restated. (knowledge-seeder)

- 2026-09-14 · bundle scaffolded empty by tools/scaffold_bundle.py: the index
  with its sections, this log, the check lines and the CODEOWNERS line
  for gesdisc-stewards; no concepts yet. (maintainer)
