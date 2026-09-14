# ornldaac bundle: change log

Newest first. One line per change: date, concept path, what changed, who.

- 2026-09-14 · STEWARD SIGNING of
  knowledge/ornldaac/datasets/daymet-v4.md,
  knowledge/ornldaac/gotchas/daymet-lcc-projection-and-cell-area.md,
  knowledge/ornldaac/gotchas/daymet-station-sparse-error.md,
  knowledge/ornldaac/gotchas/daymet-tiles-mosaics-regions.md,
  knowledge/ornldaac/gotchas/daymet-v4-r1-correction.md,
  knowledge/ornldaac/gotchas/daymet-365-day-year.md: maintainer's review
  of PR 143 recorded on the maintainer's standing instruction for round
  two of seeding; the non-high concepts promoted to stable;
  daymet-365-day-year (high severity) keeps draft with this first review
  until a second human review, per the two-review rule. The verified
  event is written on the steward's word. The verified event is written
  on the steward's word. (steward)

- 2026-09-14 · concepts revised on the coordinator's lint, applied by the
  coordinator because the seed session ran out of usage:
  gotchas/daymet-lcc-projection-and-cell-area.md (the sign and
  magnitudes of the cell-count area bias in the wrong-result paragraph
  and the severity comment now follow the areal scale factors; the
  subset box is rectangular, not square, in the projection);
  gotchas/daymet-365-day-year.md (the title now names a positional or
  generated-date join as what misaligns, since a calendar-date join is
  the fix; the description says the positional join fails on a 365-day
  assumption); gotchas/daymet-v4-r1-correction.md (R1 changed no
  earlier year rather than nothing else, since 2022 onward exists only
  in R1); datasets/daymet-v4.md (the R1 description and known-issues
  lines match the new wording, and the Version 3 parenthetical says
  1.75 was the tmax error, tmin unchanged); index.md lines match the
  new titles. All still drafts, no signatures. (coordinator)

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
