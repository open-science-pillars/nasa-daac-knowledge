---
type: dataset-gotcha
spheres: [hydrosphere]
title: "SMAP salinity in cold water: the radiometer's sensitivity to salinity falls with sea surface temperature, both producers flag SST below 5 C, and high-latitude values carry errors several times the tropical figures"
description: "The L-band brightness temperature changes less per unit of salinity in cold water than in warm water, so the same error in an input (wind speed, galaxy, calibration) becomes a larger salinity error at high latitudes. Both SMAP products carry this in their own terms: the JPL CAP quality flag marks SST below 5 C and its predicted uncertainty includes the cold-water effect; the RSS product flags SST below 5 C as moderate to strong degradation and its perturbation-based uncertainty grows with it. The validation numbers of a few tenths of a salinity unit are tropical and subtropical; the JPL group's own Arctic assessment finds differences to in situ near one salinity unit north of 50N and larger north of 65N, and the RSS notes report high-latitude biases that changed between versions and one still growing near 60S."
tags: [smap, salinity, sss, sst, cold-water, sensitivity, high-latitude, arctic, southern-ocean, uncertainty]
generated: { by: knowledge-seeder/claude, at: 2026-09-13T21:00:00Z }
severity: medium
# medium: the degradation is documented, flagged in the products'
# Level 2 records and visible in their Level 3 uncertainty fields, so
# it bites through ignoring the uncertainty field and the flag
# thresholds rather than through a field that looks right; no eval
# case is required at this severity.
dataset: ../datasets/smap-sss-jpl.md
status: draft
stale_after: 2027-03-13
sources:
  - id: jpl-guide
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/docs/JPL-CAP_V5/SMAP-SSS_JPL_V5.0_Documentation.pdf
    title: "SMAP Salinity and Wind Speed Data User's Guide, Version 5.0, JPL, November 2020 (read in full 2026-09-13): the uncertainty estimate that includes the effects of cold water (section 3.4.1), the high-latitude brightness-temperature bias adjustment (3.2.3), the quality flag bit for SST below 5 C (6.2.24) and the validation scope of 40S to 40N (4.1)"
  - id: rss-release
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/docs/V6/Release_V6.0.pdf
    title: "RSS SMAP Salinity Version 6.0 release notes, RSS Technical Report 011624 (read 2026-09-13): the low-SST flag (section 6, bit 11), the formal uncertainty method (8), the cold-water zone error in the sea-ice table (5.3), the high-latitude biases changed in version 6 and the growing bias near 60S (2.7 and 2.11), and the typical Level 2 RMS (10)"
  - id: aquarius-atbd
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/docs/V6/ATBD_EOM_final.pdf
    title: "Aquarius salinity retrieval algorithm theoretical basis document, end of mission version, Meissner, Wentz and Le Vine, RSS Technical Report 120117, 1 December 2017 (the file the RSS SMAP collections link as their ATBD; the uncertainty chapter read 2026-09-13): the same input error yields a much larger salinity uncertainty in cold water, where the sensitivity of brightness temperature to salinity is low, and the SST of the scene is a major driver of the salinity uncertainty"
  - id: tang-2018
    resource: https://doi.org/10.3390/rs10060869
    title: "Tang and others, 2018, The potential and challenges of using SMAP sea surface salinity to monitor Arctic Ocean freshwater changes, Remote Sensing 10, 869: RMS difference to in situ under about one salinity unit north of 50N with correlation 0.82, and about 1.2 north of 65N, from nearly 20,000 daily collocations within 12.5 km (abstract read on the registry record)"
  - id: meissner-2018
    resource: https://doi.org/10.3390/rs10071121
    title: "Meissner, Wentz and Le Vine, 2018, The salinity retrieval algorithms for the NASA Aquarius version 5 and SMAP version 3 releases, Remote Sensing 10, 1121: formal error estimates by perturbing the algorithm's inputs, and the Aquarius difference to Argo within 0.1 when stratified by SST (abstract read on the registry record)"
  - id: dataset
    resource: ../datasets/smap-sss-jpl.md
    title: "This bundle's SMAP salinity dataset concept: the uncertainty field and the low-latitude validation figures"
---

# SMAP salinity in cold water

**Mechanism.** The salinity signal in L-band brightness temperature
is the change of the sea surface emissivity with salinity through the
dielectric constant of sea water, and that change is smaller in cold
water than in warm water. The retrieval documentation both SMAP
products rest on states the consequence directly: the same error in
an input, wind speed in the roughness correction or the reflected
galaxy, results in a much larger salinity uncertainty in cold water,
where the sensitivity of brightness temperature to salinity is low,
than in warm water, and the SST of the scene is a major driver of the
size of the salinity uncertainty.[^aquarius-atbd] Both producers act
on it. The JPL CAP Level 2B quality flag has a bit for SST below 5 C
("SST too cold"), the guide names cold water among the effects its
predicted uncertainty includes, and a separate brightness-temperature
bias adjustment by latitude and day of year exists because of a
persistent high-latitude bias.[^jpl-guide] The RSS Level 2 flag has a
bit for SST below 5 C, defined as moderate to strong degradation with
the salinity still retrieved; its formal uncertainty is built by
perturbing each input and propagating the salinity change, so it
grows where the sensitivity falls; its sea-ice table reports 2.2
practical salinity units of RMS difference to HYCOM for cold open
water inside the climatological ice mask at 40 km, against a typical
Level 2 RMS of about 0.6 for the product as a whole; and version 6.0
changed the physical-temperature model of the antenna to mitigate
salty biases at high northern latitudes while reporting an increasing
salty bias near 60S since 2020 whose cause is not
settled.[^rss-release] The validation figures the JPL guide quotes are
for 40S to 40N (bias below 0.03, RMS below 0.3 against gridded Argo)
and for tropical moorings; the JPL group's Arctic assessment finds an
RMS difference to in situ data under about one salinity unit north of
50N and about 1.2 north of 65N, from daily collocations within
12.5 km, with the number of collocations falling by more than 70
percent north of 65N.[^jpl-guide][^tang-2018] Aquarius, from which
both algorithms descend, reaches a difference to Argo within 0.1 when
stratified by SST only after the corrections its version 5 algorithm
carries.[^meissner-2018]

**Wrong-result mode.** A subpolar or polar salinity statistic quoted
with the tropical accuracy (a few tenths of a salinity unit) claims a
precision the product does not have there; the Level 3 field is
complete and smooth at high latitude, the SST flag is a Level 2
property that the Level 3 files do not carry, and only the
uncertainty field shows the degradation. A trend or interannual
anomaly near 60S in the RSS product absorbs the growing salty bias
the producer reports; a high-latitude comparison between JPL version
5 and RSS version 6 compares products with different high-latitude
bias corrections.[^rss-release] An Arctic freshwater statement that
treats a one-salinity-unit difference as ocean signal is inside the
product's own scatter against in situ data.[^tang-2018] Averaging
does not restore the sensitivity: the cold-water error is a property
of the scene, and the RSS budget treats several of its terms as
systematic, without root-N reduction.[^rss-release]

**Correct approach.** A high-latitude salinity value from SMAP is
quoted with the product's own uncertainty field for those cells, with
the SST of the scene (the `anc_sst` or `surtep` field) and the
producers' 5 C threshold beside it, and with the regional validation
numbers (under about one salinity unit north of 50N, about 1.2 north
of 65N for the JPL product) rather than the tropical
figures.[^jpl-guide][^rss-release][^tang-2018] A Southern Ocean series
from the RSS product carries the producer's statement of the growing
bias near 60S as a caveat on any trend.[^rss-release] The product
version is named, because the high-latitude corrections changed
between RSS versions 5.0 and 6.0.[^rss-release] The dataset concept
holds the low-latitude figures with their scope.[^dataset]

**Verification.** The Aquarius end-of-mission ATBD, which the RSS SMAP
collections link as their ATBD, states the cold-water sensitivity
argument in its uncertainty chapter; the JPL guide's flag table,
uncertainty section and validation section, and the RSS release
notes' flag table, uncertainty section, sea-ice table and known
issues, were all read on 2026-09-13 and are the source of every
threshold and number above.[^aquarius-atbd][^jpl-guide][^rss-release]
The two papers' records were verified against the Crossref registry
the same day (title, authors, journal, year) and their abstracts read
there, which is where the Arctic statistics and the SST-stratified
Aquarius result come from; the publisher pages were not
read.[^tang-2018][^meissner-2018]

[^jpl-guide]: SMAP Salinity and Wind Speed Data User's Guide, Version 5.0, JPL, November 2020
[^rss-release]: RSS SMAP Salinity Version 6.0 release notes, RSS Technical Report 011624
[^aquarius-atbd]: Aquarius salinity retrieval ATBD, end of mission version, RSS Technical Report 120117
[^tang-2018]: Tang and others, 2018, Remote Sensing, doi:10.3390/rs10060869
[^meissner-2018]: Meissner, Wentz and Le Vine, 2018, Remote Sensing, doi:10.3390/rs10071121
[^dataset]: This bundle's SMAP salinity dataset concept
