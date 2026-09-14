---
type: dataset-gotcha
spheres: [hydrosphere, cryosphere]
title: "MUR at the sea ice edge: the field is gap-free under ice too, where no SST retrieval exists and the analysed value is not an observation, and only the mask and sea_ice_fraction fields say which pixels those are"
description: "A GHRSST Level 4 file has a value in every ocean pixel and a fill value only on land, so MUR carries an analysed_sst under sea ice, where no SST retrieval exists; the producer's one sentence, that the OSI SAF ice concentration is also used for an improved SST parameterization for the high latitudes, is the only account of how the ice product enters the analysed value, and what an ice-covered pixel carries was not read from a granule. The ice-covered pixels are identified by the sea ice flag of the mask and by sea_ice_fraction, both from the ice product, and the set of such pixels changes daily with the ice. A polar box mean, an ice-edge gradient, a marginal-ice-zone time series or a trend in a seasonally ice-covered region that reads analysed_sst without those two fields mixes unobserved values with analysed ones and carries the ice product's decisions as ocean temperature."
tags: [ghrsst, mur, sst, sea-ice, ice-edge, marginal-ice-zone, mask, sea_ice_fraction, osi-saf, arctic, antarctic, level4]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:30:00Z }
severity: medium
dataset: ../datasets/ghrsst-mur.md
status: draft
stale_after: 2027-03-14
sources:
  - id: gds-2-0-r5
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ghrsst/open/docs/GDS20r5.pdf
    title: "GHRSST Data Processing Specification version 2.0 revision 5 (2012), the document the PO.DAAC collection page links as the user's guide (read 2026-09-14, the Level 4 product specification): the gap-free analysed field with the fill value placed on land, the mandatory sea_ice_fraction and mask fields, the mask bit for sea ice, and the statement that sea_ice_fraction quantifies the fraction of an area contaminated with sea ice"
  - id: podaac-collection
    resource: https://podaac.jpl.nasa.gov/dataset/MUR-JPL-L4-GLOB-v4.1
    title: "PO.DAAC collection page, MUR-JPL-L4-GLOB-v4.1 (read 2026-09-14): the description stating that the ice concentration data come from the EUMETSAT OSI SAF High Latitude Processing Center archives and are also used for an improved SST parameterization for the high latitudes, and the variable table (mask as a sea/land field composite mask, sea_ice_fraction between 0 and 1)"
  - id: mur-project
    resource: https://podaac.jpl.nasa.gov/MEaSUREs-MUR
    title: "PO.DAAC MUR project page (read 2026-09-14): each file contains an uncertainty estimate, a land-mask flag and a sea ice concentration for each SST value provided"
  - id: validity-domain
    resource: ../validity-domains/mur-basin-mean-state.md
    title: "This bundle's draft validity domain for MUR (read 2026-09-14), which quotes the analysis paper's statement that SST analysis products disagree with each other in the summer Arctic and caps the supported domain at 66N for that reason"
  - id: dataset
    resource: ../datasets/ghrsst-mur.md
    title: "This bundle's MUR dataset concept (read 2026-09-14): the mask and sea_ice_fraction fields, and analysis_error largest at the ice edge"
---

# MUR at the sea ice edge

**Mechanism.** The Level 4 specification requires four fields in every
file: the analysed SST, its error estimate, a sea ice fraction and a
land, sea and ice mask; the analysed field is gap-free, and the
specification places the fill value in pixels that fall on land, not
on ice.[^gds-2-0-r5] MUR therefore carries an analysed_sst value in
ice-covered pixels, where no SST retrieval exists: the satellite
inputs observe open water, not the water under ice. The producer
states that the ice concentration data come from the EUMETSAT OSI SAF
High Latitude Processing Center and are also used for an improved SST
parameterization for the high latitudes; that sentence is the only
account the documentation read here gives of how the ice product
enters the analysed value, and it does not say what temperature an
ice-covered pixel carries.[^podaac-collection] What such a pixel
carries was not read from a granule for this concept, so the value
under ice is read from the file, not from the documentation. Two
fields identify the pixels concerned. The mask carries a sea ice flag
whose value the Level 4 specification assigns, beside water, land and
the optional lake and river flags; MUR's own flag_meanings were not
read from a granule. sea_ice_fraction carries the ice area fraction
between 0 and 1, which the specification defines as quantifying the
fraction of an area contaminated with sea ice; both are derived from
the ice product, and each file carries them for every SST
value.[^gds-2-0-r5][^podaac-collection][^mur-project] The ice edge
moves daily, so the set of pixels the mask flags and the fraction
each pixel carries change from file to file, and the analysis error
is largest there.[^dataset] In the summer Arctic the analysis
products disagree with one another, as the analysis paper states
through this bundle's validity domain.[^validity-domain]

**Wrong-result mode.** A mean over a polar box that reads analysed_sst
alone averages unobserved values in the ice-covered pixels with
analysed values in the open water, and its seasonal cycle and its
trend contain the fraction of the box the ice product called ice
each day. A time series at a pixel in the marginal ice zone steps when
the mask switches, and the step is the ice product's decision about
that pixel, not a change in the water. A gradient across the ice
edge is the transition between an analysed value and an unobserved
one, so a front detected there is the mask boundary. A warming trend
in a seasonally ice-covered region is partly the change in the number
of open-water days, and a marine heatwave detected on such pixels
against a climatology that includes the unobserved values is
detected against the ice history.[^gds-2-0-r5][^podaac-collection]
None of this raises an error, because the field is complete and the
values under ice sit inside the valid range of the variable.

**Correct approach.** An analysis near the ice reads mask and
sea_ice_fraction beside analysed_sst in every file and states its
rule: pixels with the sea_ice bit set, or with sea_ice_fraction above
a named threshold, are excluded or carried as a separate class, and
the count of open-water pixels contributing to each regional value is
reported with it.[^gds-2-0-r5][^podaac-collection] A series in a
seasonally ice-covered region is a series on the open-water days
with the ice season as its sampling, and a trend there is stated with
the change in open-water coverage beside it. The value MUR carries
under ice, and the ice product that placed it there (OSI SAF, named
on the collection page), are named in any statement that touches
those pixels, since the documentation read here gives one sentence
on the ice product's role and not the number.[^podaac-collection] The bundle's validity domain
keeps its supported region below 66N for the summer Arctic
disagreement among analyses, and a claim above that latitude is
outside it.[^validity-domain]

**Verification.** The specification's Level 4 section defines the
four mandatory fields, the fill on land, the sea_ice bit of the mask
and the meaning of sea_ice_fraction, read on 2026-09-14 from the
PO.DAAC archive copy the collection page links.[^gds-2-0-r5] The
collection page's description carries the producer's statement on the
ice concentration source and its use for an improved SST
parameterization for the high latitudes, and its variable table shows mask and
sea_ice_fraction in the archived files, read the same
day.[^podaac-collection] The project page states that every file
carries the ice concentration and the land-mask flag for every SST
value.[^mur-project] The dataset concept lists the two fields and
names the ice edge among the places where analysis_error is
largest.[^dataset] No granule was opened for this concept, so the
value under ice and MUR's own flag_meanings are reported here as
unread rather than quoted.

[^gds-2-0-r5]: GHRSST Data Processing Specification version 2.0 revision 5, PO.DAAC archive copy
[^podaac-collection]: PO.DAAC collection page, MUR-JPL-L4-GLOB-v4.1
[^mur-project]: PO.DAAC MUR project page
[^validity-domain]: This bundle's MUR validity domain, mur-basin-mean-state
[^dataset]: This bundle's MUR dataset concept
