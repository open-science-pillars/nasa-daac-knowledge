# gesdisc bundle: change log

Newest first. One line per change: date, concept path, what changed, who.

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
