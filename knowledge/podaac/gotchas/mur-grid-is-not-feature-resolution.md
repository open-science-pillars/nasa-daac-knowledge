---
type: dataset-gotcha
spheres: [hydrosphere]
title: "The MUR 0.01 degree grid is the posting of an interpolation: the scale a feature is resolved at is set by the observations available that day at that place, so a front's width or a gradient read from the grid is a property of the analysis, not a measurement"
description: "MUR posts a gap-free field at 0.01 degree, about one kilometre, by a wavelet multi-scale interpolation of infrared retrievals at kilometre scale, microwave retrievals at about 25 km and in situ points. The producer states that every fine-scale feature comes from the measurements and that the resolution of the map is its internal resolution, not its grid, and the analysis paper states that the feature resolution is often much lower than the grid resolution. Where cloud removed the infrared input the constrained scales are the microwave scales, so a front width, a gradient magnitude or a small-scale statistic read at grid scale varies with the input coverage rather than with the ocean, and a series or a map of such quantities carries the cloud history in it."
tags: [ghrsst, mur, sst, resolution, interpolation, front, gradient, cloud, dt_1km_data, level4]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:30:00Z }
severity: high
dataset: ../datasets/ghrsst-mur.md
eval_case: mur-grid-is-not-feature-resolution
status: draft
stale_after: 2027-03-14
sources:
  - id: mur-project
    resource: https://podaac.jpl.nasa.gov/MEaSUREs-MUR
    title: "PO.DAAC MUR project page (read 2026-09-14): the 0.01 degree posting at roughly one kilometre, the input resolutions (microwave about 25 km, infrared to one kilometre with cloud voids), the multi-resolution variational analysis on wavelets, the statement that all high-resolution features are due to the measurements, and the statement that a map's resolution is its internal resolution measured by the power spectral density and not its grid"
  - id: podaac-collection
    resource: https://podaac.jpl.nasa.gov/dataset/MUR-JPL-L4-GLOB-v4.1
    title: "PO.DAAC collection page, MUR-JPL-L4-GLOB-v4.1 (read 2026-09-14): the description (wavelets as basis functions in an optimal interpolation on a global 0.01 degree grid; the instruments; the dt_1km_data variable, hours to the nearest infrared measurement per pixel, present from 2015-10-04) and the variable table"
  - id: chin-2017
    resource: https://doi.org/10.1016/j.rse.2017.07.029
    title: "Chin, Vazquez-Cuervo and Armstrong, 2017, A multi-scale high-resolution analysis of global sea surface temperature, Remote Sensing of Environment 200, 154-169: the analysis paper (registry record verified on Crossref 2026-09-14 for title, authors, journal and year; the registry carries no abstract and the publisher page sits behind a bot check, so the article was not read here; its feature-resolution statement is quoted through the bundle's validity domain below)"
  - id: validity-domain
    resource: ../validity-domains/mur-basin-mean-state.md
    title: "This bundle's draft validity domain for MUR, which quotes the analysis paper's statement that the analysed SST feature resolution is often much lower than the grid resolution and keeps gradient-class claims outside the supported domain"
  - id: dataset
    resource: ../datasets/ghrsst-mur.md
    title: "This bundle's MUR dataset concept: Level 4 means every pixel has a value because interpolation filled it, and analysis_error rises where observations were sparse"
---

# The MUR grid is not the feature resolution

**Mechanism.** MUR posts one global field a day at 0.01 degree,
roughly one kilometre, and every pixel carries a value because the
analysis is gap-free by construction.[^mur-project][^dataset] The
inputs are of two kinds: microwave retrievals with resolutions of the
order of 25 km, which see through cloud, and infrared retrievals that
resolve to one kilometre but have voids wherever there is cloud,
together with in situ points.[^mur-project][^podaac-collection] The
analysis combines them with a multi-resolution variational method on
wavelet basis functions, an interpolation in which, in the producer's
words, there is no statistical synthesis of any kind and all
high-resolution features are due to the measurements.[^mur-project]
The consequence is the trap: where the infrared measurements are
absent, the scales below the microwave footprint are not constrained
by anything, and the field there is the interpolation of the coarser
inputs written out on the fine grid. The producer states that the
resolution of an SST map is not its grid resolution but its internal
resolution, assessed by a measure such as the power spectral
density,[^mur-project] and the analysis paper, as quoted in this
bundle's validity domain, states that the feature resolution is often
much lower than the grid resolution.[^chin-2017][^validity-domain]
Since 2015-10-04 the files carry dt_1km_data, the time in hours from
each pixel to the nearest infrared measurement, which is the
product's own record of where the fine scales were constrained and
how recently.[^podaac-collection] The analysis error field rises
where observations were sparse.[^dataset]

**Wrong-result mode.** A front width measured as the distance over
which the gridded temperature changes, a gradient magnitude in
kelvin per kilometre, a count of fronts detected by a gradient
threshold, or any statistic at scales of a few kilometres to a few
tens of kilometres, is a property of whichever inputs constrained
that place that day. Under persistent cloud the same front is wider
and weaker in the analysis than in the ocean, and a front that
sharpens and blurs from day to day in the product is tracking the
cloud cover, not the dynamics. A comparison of small-scale variance
between two regions or two seasons with different cloud climatologies
measures the input availability. A spectrum computed from the grid
reads as if it resolved the grid scale everywhere, when the
constrained scales differ from pixel to pixel; and a study that
selects the finest features it can see in the field selects the
cloud-free days without saying so. Nothing in the analysed field
itself marks where the fine scales are interpolation.[^mur-project][^validity-domain]

**Correct approach.** The scale at which a MUR feature is resolved is
read from the product's own coverage record, not from the grid:
dt_1km_data gives the hours to the nearest infrared measurement per
pixel, and analysis_error rises where the inputs were
sparse.[^podaac-collection][^dataset] A front width or gradient
statistic is therefore stated with the coverage that supports it: a
threshold on dt_1km_data or on analysis_error chosen and named, the
statistic computed on the pixels that pass, and the fraction of
pixels that passed reported beside it; on the pixels that do not
pass, the smallest scale the field can carry is the microwave scale
of order 25 km, and a width smaller than that is not a
measurement.[^mur-project] A series of front properties is a series
on cloud-free coverage with the gaps kept as gaps, never a daily
series read straight from the gap-free field. The producer's own
measure of resolution, the power spectral density, is a statement
about the analysis as a whole, not a licence to read grid-scale
features at any one place on any one day.[^mur-project] Before the
dt_1km_data variable exists in the record, analysis_error is the
only coverage indicator in the file.[^podaac-collection]

**Verification.** The project page carries the producer's statements
on the input resolutions, the interpolation method, the origin of the
fine-scale features and the meaning of resolution, read on
2026-09-14.[^mur-project] The collection page names the interpolation
on the 0.01 degree grid and defines dt_1km_data with its start date,
read the same day.[^podaac-collection] The analysis paper's registry
record was verified on Crossref the same day (title, three authors,
Remote Sensing of Environment, volume 200, 2017); its feature
resolution statement is quoted here through the bundle's validity
domain, whose author verified it against the typeset article, and
the article itself was not read for this
concept.[^chin-2017][^validity-domain] The dataset concept states the
same caveat in its uncertainty section.[^dataset]

[^mur-project]: PO.DAAC MUR project page
[^podaac-collection]: PO.DAAC collection page, MUR-JPL-L4-GLOB-v4.1
[^chin-2017]: Chin, Vazquez-Cuervo and Armstrong, 2017, Remote Sensing of Environment, doi:10.1016/j.rse.2017.07.029
[^validity-domain]: This bundle's MUR validity domain, mur-basin-mean-state
[^dataset]: This bundle's MUR dataset concept
