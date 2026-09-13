---
type: dataset-gotcha
spheres: [cryosphere]
title: "An annual velocity mosaic is a composite of image pairs with its own effective date and count, and a discharge needs ice thickness from another product"
description: "An annual ITS_LIVE or MEaSUREs velocity mosaic is an error-weighted synthesis of every image pair that overlapped the year, so its value at a pixel represents whatever dates the pairs happened to cover, with a count of pairs (and, in NSIDC-0725, a temporal offset) recording how well; before 2013 many regions have few pairs or none. A flux computed from a mosaic states the mosaic's year, its effective date where the product gives one, and its coverage, and an ice discharge multiplies velocity by ice thickness at the gate, which comes from BedMachine, a product this bundle does not yet describe."
tags: [its-live, measures, ice-velocity, velocity-mosaic, flux-gate, discharge, ice-thickness, bedmachine, count, effective-date, greenland, antarctica]
generated: { by: knowledge-seeder/claude, at: 2026-09-13T20:30:00Z }
severity: medium
# medium: the guides document the compositing, the count field and
# the coverage limits; the error bites through an unstated epoch or a
# missing thickness product rather than a silently wrong number from
# the product alone; no eval case is required.
dataset: ../datasets/its-live-ice-velocity.md
status: draft
stale_after: 2027-03-13
sources:
  - id: nsidc-0776-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/nsidc-0776-v002-userguide.pdf
    title: "NSIDC-0776 Version 2 user guide: the annual composite as an error-weighted least-squares fit of all image pairs overlapping the year, the count field, the coverage note for years before 2013, and the map-unit statement's flux-gate implication"
  - id: its-live-v1-description
    resource: https://its-live-data.s3.amazonaws.com/documentation/ITS_LIVE-Regional-Glacier-and-Ice-Sheet-Surface-Velocities.pdf
    title: "ITS_LIVE regional velocities product description, version 1 (June 2019): the date (effective date), dt (effective image-pair separation) and count parameters"
  - id: nsidc-0725-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/nsidc-0725-v005-userguide.pdf
    title: "NSIDC-0725 user guide: the 1 December to 30 November measurement year, the temporal offset dT and its 183-day bound, the statement that the mosaics are not true annual averages, and the interior caution"
  - id: nsidc-0670-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/nsidc-0670-v001-userguide.pdf
    title: "NSIDC-0670 user guide: the multi-year mosaic is an error-weighted average over 1995 to 2015 at each point, not a uniform average"
  - id: gardner-2018
    resource: https://doi.org/10.5194/tc-12-521-2018
    title: "Gardner and others, 2018, Increased West Antarctic and unchanged East Antarctic ice discharge over the last 7 years, The Cryosphere 12, 521 to 547: Antarctic discharge through an optimized flux gate from Landsat velocities spanning 2013 to 2015, compared with the earlier radar mapping"
  - id: cmr-bedmachine
    resource: https://cmr.earthdata.nasa.gov/search/collections.json?short_name=NSIDC-0756
    title: "CMR collection record for MEaSUREs BedMachine Antarctica (NSIDC-0756, Version 4, concept C3973022985-NSIDC_CPRD); the Greenland counterpart is IceBridge BedMachine Greenland (IDBMG4, Version 6, concept C3903728370-NSIDC_CPRD)"
  - id: dataset
    resource: ../datasets/its-live-ice-velocity.md
    title: "This bundle's velocity mosaic concept, which lists this trap among the known issues"
---

# An annual velocity mosaic is a composite with its own effective date and count

**Mechanism.** An NSIDC-0776 annual value at a pixel is the optimal
fit, in an error-weighted least-squares sense, of every valid
image-pair velocity whose span overlaps the year, each pair entering
with the fraction of the year it covers and a weight of one over the
square of its displacement error; the count variable is the number of
image pairs in that fit, and the guide states that data scarcity and
low radiometric quality limit coverage for many regions in the earlier
years, with annual coverage nearly complete only after
2013.[^nsidc-0776-user-guide] The version 1 product description
carried this further with an explicit date field, the effective date of
the composite, and dt, the effective image-pair separation, beside
count.[^its-live-v1-description] The Greenland SAR mosaics say the same
thing in their own terms: NSIDC-0725 aggregates all data in a
measurement year from 1 December to 30 November, weighted by error,
and reports dT, the number of days between the weighted measurement
date and the midpoint of the year; data with a skew beyond half the
interval are discarded, so the time-stamp error is at most about 183
days, and the guide states that the mosaics do not represent true
annual averages because summer Landsat availability or clouds can
weight one season over another.[^nsidc-0725-user-guide] The
multi-year NSIDC-0670 mosaic is likewise an error-weighted average of
whatever sources covered each point between 1995 and 2015, which its
guide states is not a uniformly averaged velocity for the twenty
years.[^nsidc-0670-user-guide] Ice discharge across a gate is the
velocity normal to the gate times the ice thickness there, integrated
along the gate, and no velocity mosaic carries a thickness variable;
Gardner and others 2018 computed Antarctic discharge through an
optimized flux gate from Landsat velocities spanning 2013 to 2015 and
compared it with the earlier radar mapping.[^nsidc-0776-user-guide][^gardner-2018] At
NSIDC that product is BedMachine (NSIDC-0756 for Antarctica, IDBMG4
for Greenland), which this bundle does not yet describe.[^cmr-bedmachine]

**Wrong-result mode.** A discharge labelled with the mosaic's year is
in fact the discharge at the composite's effective date, which on a
glacier imaged mostly in summer sits months from the year's midpoint,
and a change between two annual mosaics on such a glacier mixes a
seasonal cycle with the inter-annual change; NSIDC-0725's guide states
outright that its mosaics are not to be used for inter-annual change
in the interior above about 2,000 m and that changes in the
intermediate elevations that follow a satellite swath boundary are
artefacts.[^nsidc-0725-user-guide] A time series of a pixel across
years with few or zero pairs early in the record (count of zero is the
fill) reads a coverage change as a velocity change unless count is
read beside it.[^nsidc-0776-user-guide] A flux quoted from the
velocity alone, or with a thickness of unstated origin and date, is
not a discharge; and a discharge that combines a map-space Version 2
velocity with a ground-measured gate length, or a ground-corrected
velocity with a map-space gate, carries the projection scale error on
one factor (its own gotcha).[^nsidc-0776-user-guide]

**Correct approach.** A flux statement from a mosaic names the product
and version, the mosaic year, the effective date where the product
gives one (date in ITS_LIVE version 1, dT in NSIDC-0725) and otherwise
the compositing window, and the count at the gate; a comparison
between years states the count in each and, for the SAR mosaics, that
the guide's interior caution applies.[^nsidc-0776-user-guide][^its-live-v1-description][^nsidc-0725-user-guide]
A discharge names the thickness product, its version and its date
beside the velocity mosaic, and treats the thickness as a separate
uncertainty term; the reference computation is Gardner and others
2018's flux gate.[^gardner-2018][^cmr-bedmachine] The velocity errors
are voiced as the guides voice them: qualitative in NSIDC-0776,
average behaviour and spatially correlated in NSIDC-0725.[^nsidc-0776-user-guide][^nsidc-0725-user-guide]

**Verification.** The NSIDC-0776 guide's processing section gives the
compositing protocol, the parameter table gives count, and the
temporal coverage note gives the 2013 threshold; the version 1 product
description's parameter table gives date and dt; the NSIDC-0725 guide
gives dT, the 183-day bound and the quality cautions; the NSIDC-0670
guide gives the non-uniform average statement; all read on
2026-09-13.[^nsidc-0776-user-guide][^its-live-v1-description][^nsidc-0725-user-guide][^nsidc-0670-user-guide]
Gardner and others 2018 is cited on its Crossref record (title,
authors, journal, year, volume and pages verified 2026-09-13) and its
abstract, which states the flux gate, the 2013 to 2015 velocity span
and the comparison with the radar mapping; the journal site was not
reachable from the drafting session.[^gardner-2018] The BedMachine
collection records were read from CMR the same day.[^cmr-bedmachine]
The dataset concept lists this trap among the product's known
issues.[^dataset]

[^nsidc-0776-user-guide]: NSIDC-0776 Version 2 user guide
[^its-live-v1-description]: ITS_LIVE regional velocities product description, version 1
[^nsidc-0725-user-guide]: NSIDC-0725 user guide
[^nsidc-0670-user-guide]: NSIDC-0670 user guide
[^gardner-2018]: Gardner and others, 2018, The Cryosphere, doi:10.5194/tc-12-521-2018
[^cmr-bedmachine]: CMR collection records for BedMachine Antarctica and Greenland
[^dataset]: This bundle's velocity mosaic concept
