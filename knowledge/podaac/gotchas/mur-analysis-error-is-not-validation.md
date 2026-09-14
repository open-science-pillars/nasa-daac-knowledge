---
type: dataset-gotcha
spheres: [hydrosphere]
title: "MUR analysis_error is the analysis system's own estimate of its error standard deviation, not a comparison against independent measurements: quoted as the accuracy of a value, or divided by root N for a regional mean, it says something the product never measured"
description: "The GHRSST Level 4 format defines analysis_error as the error standard deviation estimate from the analysis system, documented by the producer, and MUR's variable is the estimated error standard deviation of analysed_sst. It is a product of the interpolation, larger where the inputs were sparse, and the in situ observations MUR ingests are the same iQuam data a buoy comparison would use, so the mean residual (bias) against them is near zero and is not independent validation. The field carries no retrieval bias and no smoothing error, and it is spatially correlated, so a regional error from root N is far too small. An accuracy statement about a MUR value rests on an independent comparison with its scope stated, not on this field."
tags: [ghrsst, mur, sst, analysis_error, uncertainty, validation, buoy, iquam, level4]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:30:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-14T12:15:35Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/141 }
severity: medium
dataset: ../datasets/ghrsst-mur.md
status: stable
stale_after: 2027-03-14
sources:
  - id: gds-2-0-r5
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ghrsst/open/docs/GDS20r5.pdf
    title: "GHRSST Data Processing Specification version 2.0 revision 5 (2012), the document the PO.DAAC collection page links as the user's guide (read 2026-09-14, the Level 4 product specification): analysis_error as the error standard deviation estimate from the analysis system, with the data provider responsible for documenting how it is determined"
  - id: podaac-collection
    resource: https://podaac.jpl.nasa.gov/dataset/MUR-JPL-L4-GLOB-v4.1
    title: "PO.DAAC collection page, MUR-JPL-L4-GLOB-v4.1 (read 2026-09-14): the variable table (analysis_error, estimated error standard deviation of analysed_sst, kelvin) and the description naming the NOAA iQuam in situ observations among the analysis inputs"
  - id: mur-project
    resource: https://podaac.jpl.nasa.gov/MEaSUREs-MUR
    title: "PO.DAAC MUR project page (read 2026-09-14): each file contains an estimate of SST uncertainty for each SST value provided"
  - id: chin-2017
    resource: https://doi.org/10.1016/j.rse.2017.07.029
    title: "Chin, Vazquez-Cuervo and Armstrong, 2017, A multi-scale high-resolution analysis of global sea surface temperature, Remote Sensing of Environment 200, 154-169: the analysis paper (registry record verified on Crossref 2026-09-14 for title, authors, journal and year; no abstract on the registry and the publisher page behind a bot check, so the article was not read here; its residual statistics are quoted through the bundle's validity domain below)"
  - id: validity-domain
    resource: ../validity-domains/mur-basin-mean-state.md
    title: "This bundle's draft validity domain for MUR (read 2026-09-14), which quotes the analysis paper's residual statistics against the ingested iQuam data (bias minus 0.003 C, RMS 0.489 C) and against the GHRSST multi-product ensemble and states that neither is independent validation"
  - id: dataset
    resource: ../datasets/ghrsst-mur.md
    title: "This bundle's MUR dataset concept (read 2026-09-14), whose uncertainty section states that analysis_error is the product's own estimate, omits systematic retrieval biases and the smoothing, and does not average down by root N"
---

# MUR analysis_error is not a validation

**Mechanism.** The Level 4 format defines analysis_error as the error
standard deviation estimate from the analysis system, and leaves it to
the data provider to document how it is determined; MUR's variable is
the estimated error standard deviation of analysed_sst, in
kelvin.[^gds-2-0-r5][^podaac-collection] It is a quantity the
interpolation produces about itself: an estimate that grows where the
observations were sparse or distant and shrinks where they were
dense, an uncertainty of the analysis with respect to its
inputs.[^mur-project][^dataset] Nothing independent enters it. The
in situ observations that MUR ingests are the NOAA iQuam data, the
same in situ record a match-up would draw on, so the product's mean
residual (bias) against those data is near zero and, as the analysis
paper states through this bundle's validity domain, is not an
independent validation, and neither is the agreement with the
GHRSST multi-product ensemble, which is an ensemble of peer
analyses.[^podaac-collection][^chin-2017][^validity-domain] The
field carries no term for a systematic retrieval bias in the inputs
and none for the smoothing the interpolation imposes, and it is
spatially correlated, so it does not fall by root N over a
region.[^dataset]

**Wrong-result mode.** A sentence of the form "the accuracy of MUR at
this point is the analysis_error value" quotes the interpolation's
confidence in itself as if it had been checked against the sea. A
comparison of MUR against buoys that draws its error bar from
analysis_error, or that reports a near-zero mean residual (bias)
against iQuam data as validation, closes a circle, because those buoys are inputs
to the field being tested.[^podaac-collection][^validity-domain] A
regional mean with an uncertainty of the mean analysis_error divided
by the square root of the pixel count claims a precision of
millikelvin that the correlated field does not support; the honest
regional uncertainty stays near the regional mean of the
field.[^dataset] A low analysis_error read as a low error at a coast,
under a sensor bias or in the summer Arctic reports the density of
inputs, not their correctness.[^dataset][^validity-domain]

**Correct approach.** analysis_error is reported beside any MUR-derived
number as what it is, the analysis's own estimate of its error
standard deviation, and it is the right field to read for where the
field is interpolation rather than observation.[^gds-2-0-r5][^dataset]
An accuracy statement rests on an independent comparison with its
scope stated: a reference not among the analysis inputs, matched by
SST type to the foundation temperature, over a named region and
period, with the residual's bias and spread reported as the
comparison's result rather than as a property of the product; a
published validation is cited with the same scope, and the analysis
paper's residual statistics against ingested data are cited as what
the paper calls them.[^chin-2017][^validity-domain] A regional
uncertainty is stated at the level of the regional mean of
analysis_error, or from an independent comparison, never from root
N.[^dataset]

**Verification.** The specification's definition of analysis_error
and the responsibility it places on the provider were read on
2026-09-14 from the PO.DAAC archive copy the collection page links,
and the collection page's variable table and description were read
the same day.[^gds-2-0-r5][^podaac-collection] The project page
states that every file carries an uncertainty estimate for each SST
value.[^mur-project] The analysis paper's registry record was
verified on Crossref the same day (title, three authors, Remote
Sensing of Environment, volume 200, 2017); its residual statistics
are quoted here through the bundle's validity domain, which verified
them against the typeset article, and the article was not read for
this concept.[^chin-2017][^validity-domain] The dataset concept's
uncertainty section carries the correlation and the missing-terms
caveats.[^dataset]

[^gds-2-0-r5]: GHRSST Data Processing Specification version 2.0 revision 5, PO.DAAC archive copy
[^podaac-collection]: PO.DAAC collection page, MUR-JPL-L4-GLOB-v4.1
[^mur-project]: PO.DAAC MUR project page
[^chin-2017]: Chin, Vazquez-Cuervo and Armstrong, 2017, Remote Sensing of Environment, doi:10.1016/j.rse.2017.07.029
[^validity-domain]: This bundle's MUR validity domain, mur-basin-mean-state
[^dataset]: This bundle's MUR dataset concept
