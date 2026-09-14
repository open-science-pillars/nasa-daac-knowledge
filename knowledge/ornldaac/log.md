# ornldaac bundle: change log

Newest first. One line per change: date, concept path, what changed, who.

- 2026-09-14 · first concepts of the bundle, Daymet Version 4 (release
  R1): one dataset concept (datasets/daymet-v4.md) and five gotchas
  (daymet-365-day-year at severity high with its eval case drafted in
  agent-evals under daymet/cases/, unregistered in any suite manifest
  until the coordinator's follow-up; daymet-lcc-projection-and-cell-area,
  daymet-tiles-mosaics-regions and daymet-v4-r1-correction at severity
  medium; daymet-station-sparse-error at severity low): all drafts, no
  signatures. Sources read the same day: the ORNL DAAC user guides for
  Daymet Daily Version 4 and for the Version 4 station-level
  cross-validation dataset, the Version 4 landing page with its
  superseding notice; the Daymet project site's description, get data,
  web services, citations and tile selection tool retirement pages; the
  CMR collection search for Daymet, the collection records for the R1
  daily and cross-validation collections and the R1 daily granule
  search; Thornton and others 2021 in Scientific Data, read in full at
  nature.com and verified against its Crossref record. Not reachable
  from the drafting session: the Version 4 R1 landing pages, user guide
  PDFs and dataset lister (the DAAC redirects them to earthdata.nasa.gov
  hosts outside the sources consulted, and the proxy refuses those
  hosts), a separate R1 release notes document (none found on
  daac.ornl.gov; the R1 statement rests on the CMR abstracts and the
  Version 4 landing page), and the THREDDS catalogs (redirected to
  opendap.earthdata.nasa.gov); no data file was opened. The projection
  gotcha's cell-area figures are computed from the guide's PROJ string
  with PROJ 9.5.1, not quoted from a Daymet document. (drafted by the
  knowledge seeder; coordinator review, eval registration and roadmap
  reconciliation pending)

- 2026-09-14 · bundle scaffolded empty by tools/scaffold_bundle.py: the index
  with its sections, this log, the check lines and the CODEOWNERS line
  for ornldaac-stewards; no concepts yet. (maintainer)
