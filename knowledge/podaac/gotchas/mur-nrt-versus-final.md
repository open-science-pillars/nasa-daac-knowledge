---
type: dataset-gotcha
spheres: [hydrosphere]
title: "MUR near-real-time and retrospective files share one collection and are told apart only by a global attribute: the one-day and four-day analyses of the same date can differ in value, so a series across the latency boundary changes file kind without saying so"
description: "The MUR v4.1 collection is produced as a retrospective dataset with a four-day latency and a near-real-time dataset with a one-day latency, and the collection page says to read the file's global history attribute to tell which a granule is. The collection page states the two latencies and nothing about the input windows; this concept's reading is that a near-real-time analysis cannot contain observations that arrived after its first day, so its inputs are a subset of the retrospective file's and its values can differ for the same day. A result computed from the latest days without recording the file kind is not reproducible against the archive later, and a series that ends at today mixes the two kinds at its end."
tags: [ghrsst, mur, sst, nrt, near-real-time, retrospective, latency, reproducibility, history, level4]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:30:00Z }
severity: low
dataset: ../datasets/ghrsst-mur.md
status: draft
stale_after: 2027-03-14
sources:
  - id: podaac-collection
    resource: https://podaac.jpl.nasa.gov/dataset/MUR-JPL-L4-GLOB-v4.1
    title: "PO.DAAC collection page, MUR-JPL-L4-GLOB-v4.1 (read 2026-09-14): the description stating that the analysis is produced as a retrospective dataset with four-day latency and a near-real-time dataset with one-day latency, and that the file global metadata history attribute is the way to determine whether a granule is near-real-time or retrospective"
  - id: doi-product
    resource: https://doi.org/10.5067/GHGMR-4FJ04
    title: "The product DOI, resolved on 2026-09-14 to the Earthdata catalog record for MUR-JPL-L4-GLOB-v4.1, which carries the same two-latency description under the one collection"
  - id: gds-2-0-r5
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ghrsst/open/docs/GDS20r5.pdf
    title: "GHRSST Data Processing Specification version 2.0 revision 5 (2012), the document the PO.DAAC collection page links as the user's guide (read 2026-09-14, the Level 4 overview): Level 4 products are ideally available within 24 hours, and the file carries a global history attribute"
  - id: dataset
    resource: ../datasets/ghrsst-mur.md
    title: "This bundle's MUR dataset concept (read 2026-09-14), which names the collection and its version"
---

# MUR near-real-time versus retrospective files

**Mechanism.** The collection page describes the MUR v4.1 analysis as
produced twice: as a retrospective dataset with a four-day latency
and as a near-real-time dataset with a one-day latency, both under
the one collection MUR-JPL-L4-GLOB-v4.1, and it states that the way
to determine whether a granule is near-real-time or retrospective is
the file's global metadata history
attribute.[^podaac-collection][^doi-product] The specification asks
for Level 4 products within 24 hours and defines the history global
attribute in the file header, which is where the producer records
the processing.[^gds-2-0-r5] The collection page states the two
latencies and nothing about the input windows; what follows is this
concept's reading of them.[^podaac-collection] A one-day analysis is
made from the observations that had arrived within a day of the
analysis time; a four-day analysis has three more days for late
observations to arrive, and an interpolation with more inputs is a
different interpolation, so the two files for one date can differ in
value. Which kind sits in the archive for a given
date at a given moment is a property of that moment, and the
collection page names no other marker of it than the
attribute.[^podaac-collection]

**Wrong-result mode.** A series read up to the present has
near-real-time files at its end and retrospective files before, so
its last days differ in inputs from the rest, and an anomaly, a
maximum or a heatwave onset detected in those days is detected on the
one-day analysis. A value quoted for a recent date from the file
available at the time is not reproduced by the file the archive
holds later, and a workflow that caches files without their history
attribute cannot say which analysis it used.[^podaac-collection] A
comparison of the same date across two downloads that differ in file
kind reads the input difference as a change in the
product.[^podaac-collection][^doi-product]

**Correct approach.** Every MUR file used is recorded with its history
attribute, so the analysis kind is part of the provenance of any
number derived from it.[^podaac-collection] A series that has to be
retrospective throughout ends where the retrospective files end, at
the four-day latency, and a series carried to the present states
where the near-real-time files begin.[^podaac-collection] A result
computed on near-real-time files is recomputed when the retrospective
files for those dates exist, or is stated as a near-real-time
result.[^dataset]

**Verification.** The collection page's description was read on
2026-09-14 and is the source for the two latencies and for the
history attribute as the marker; the product DOI resolved the same
day to the Earthdata catalog record carrying the same
description.[^podaac-collection][^doi-product] The specification's
Level 4 overview and its sample header, read the same day, carry the
24-hour target and the history attribute.[^gds-2-0-r5] No granule
was opened for this concept, so how large the difference between the
two kinds is for a given date is not quantified here; what the
sources state is two latencies under one collection, and the input
window reasoning above is this concept's own.

[^podaac-collection]: PO.DAAC collection page, MUR-JPL-L4-GLOB-v4.1
[^doi-product]: Product DOI 10.5067/GHGMR-4FJ04, resolved to the Earthdata catalog record
[^gds-2-0-r5]: GHRSST Data Processing Specification version 2.0 revision 5, PO.DAAC archive copy
[^dataset]: This bundle's MUR dataset concept
