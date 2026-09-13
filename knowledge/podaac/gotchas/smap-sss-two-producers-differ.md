---
type: dataset-gotcha
spheres: [hydrosphere]
title: "JPL CAP and RSS SMAP salinity are two products from one radiometer: different input calibration, algorithm, smoothing, ancillary data, coverage and uncertainty, so a series does not mix them and an anomaly does not borrow the other's climatology"
description: "PO.DAAC archives two Level 3 SMAP salinity lines. JPL CAP version 5.0 fits salinity and wind to version 5 brightness temperatures by maximum likelihood and grids to about 60 km with a likelihood-width uncertainty; RSS version 6.0 interpolates version 6 antenna temperatures to 40 km, smooths to about 70 km, uses CCMP winds, an AMSR2 sea-ice scheme and a nine-term formal error budget, and starts a month earlier. Their versions were released three years apart with different bias corrections at high latitude and in the early mission. A series that switches between them, or an anomaly of one against the other's mean, carries those differences as signal, and the spread between them is not an uncertainty for either."
tags: [smap, salinity, sss, jpl, cap, rss, producers, algorithm, versions, climatology, anomaly]
generated: { by: knowledge-seeder/claude, at: 2026-09-13T21:00:00Z }
severity: medium
# medium: both products are documented and separately catalogued and
# the trap bites through mixing or cross-comparison rather than through
# a silently wrong single-product statistic; no eval case is required
# at this severity.
dataset: ../datasets/smap-sss-jpl.md
status: draft
stale_after: 2027-03-13
sources:
  - id: jpl-guide
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/docs/JPL-CAP_V5/SMAP-SSS_JPL_V5.0_Documentation.pdf
    title: "SMAP Salinity and Wind Speed Data User's Guide, Version 5.0, JPL, November 2020 (read in full 2026-09-13): the version history, the pre-processing and ancillary data, the retrieval and its uncertainty, the L3 gridding and the validation"
  - id: rss-release
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/docs/V6/Release_V6.0.pdf
    title: "RSS SMAP Salinity Version 6.0 release notes, RSS Technical Report 011624 (read 2026-09-13): the summary and version changes, the release date, latency, resolution and smoothing, known issues and missing periods, ancillary inputs, flags, L3 processing, the formal uncertainty budget and the near-real-time variant"
  - id: cmr-jpl
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2208423975-POCLOUD.umm_json
    title: "CMR collection record for the JPL monthly product (with the 8-day record C2208422957-POCLOUD): abstracts and granule ranges on 2026-09-13"
  - id: cmr-rss
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2832226365-POCLOUD.umm_json
    title: "CMR collection record for the RSS monthly product (with the 8-day record C2832227567-POCLOUD): abstracts, the version 6 change list and granule ranges on 2026-09-13"
  - id: podaac-jpl
    resource: https://podaac.jpl.nasa.gov/dataset/SMAP_JPL_L3_SSS_CAP_MONTHLY_V5
    title: "PO.DAAC collection page, SMAP_JPL_L3_SSS_CAP_MONTHLY_V5: release date 2020-12-11 and the variable table (read 2026-09-13)"
  - id: podaac-rss
    resource: https://podaac.jpl.nasa.gov/dataset/SMAP_RSS_L3_SSS_SMI_MONTHLY_V6
    title: "PO.DAAC collection page, SMAP_RSS_L3_SSS_SMI_MONTHLY_V6: release date 2024-03-26 at PO.DAAC and the variable table (read 2026-09-13)"
  - id: fore-2016
    resource: https://doi.org/10.1109/TGRS.2016.2601486
    title: "Fore, Yueh, Tang, Stiles and Hayashi, 2016, Combined active/passive retrievals of ocean vector wind and sea surface salinity with SMAP, IEEE Transactions on Geoscience and Remote Sensing 54, 7396 to 7404: the JPL algorithm (registry record verified 2026-09-13; the record carries no abstract and the article was not read)"
  - id: meissner-2018
    resource: https://doi.org/10.3390/rs10071121
    title: "Meissner, Wentz and Le Vine, 2018, The salinity retrieval algorithms for the NASA Aquarius version 5 and SMAP version 3 releases, Remote Sensing 10, 1121: the RSS algorithm line, its formal error estimates by input perturbation, and its adaptation from Aquarius to SMAP (registry record verified and abstract read there 2026-09-13; the article was not read)"
  - id: dataset
    resource: ../datasets/smap-sss-jpl.md
    title: "This bundle's SMAP salinity dataset concept: both products' collections, DOIs and granule ranges on the verification date"
---

# JPL CAP and RSS SMAP salinity are two products

**Mechanism.** One instrument, two retrievals. The JPL line is the
Combined Active-Passive algorithm carried over from Aquarius: the
input is version 5 of the SMAP Level 1B brightness temperatures, to
which JPL applies its own galaxy correction, a land correction from
look-up tables, and a brightness-temperature bias adjustment by
latitude, day of year and azimuth; the retrieval fits salinity and
wind speed jointly by maximum likelihood to the four looks, with the
wind held near NCEP within 1.5 m/s and the salinity free; the
ancillary fields are HYCOM salinity, NCEP winds, NOAA optimum
interpolation SST and WaveWatch III wave height; the Level 3 is a
Gaussian-weighted gridding to 0.25 degrees at about 60 km resolution
with a likelihood-width uncertainty propagated to the
grid.[^jpl-guide][^fore-2016] The RSS line follows the Aquarius
version 5 retrieval: the input is version 6 of the Level 1B antenna
temperatures (with a lower interference threshold than version 5),
resampled by Backus-Gilbert optimal interpolation to a 40 km product
on the same 0.25-degree grid and then averaged over nine cells to
about 70 km, which the producer names the standard product; the
roughness correction uses CCMP winds (WindSat primarily), the SST is
the Canadian analysis, sea ice is detected from AMSR2 brightness
temperatures by discriminant analysis with a sidelobe correction, and
the uncertainty is a formal budget of nine perturbed inputs with
random and systematic propagation
rules.[^rss-release][^meissner-2018] The two are on different version
cadences: JPL version 5.0 was released in December 2020 and its guide
lists no later version; RSS version 6.0 was validated on 18 January
2024 and, relative to version 5.0, removed a salty bias near
continental shelves in the early mission (until 11 August 2015),
mitigated look-angle-dependent biases and salty biases at high
northern latitudes, and revised the sun-glint flag, while noting an
increasing salty bias near 60S since 2020 that is not
corrected.[^rss-release][^cmr-rss][^podaac-jpl][^podaac-rss] Coverage
differs too: the RSS 8-day record starts on 2015-03-28 and the JPL
one on 2015-04-30; the RSS notes list days with no retrieval (eight
days of incomplete ice masks, two pairs of days without CCMP winds,
and the 2019 and 2022 safeholds with no July 2019 and no August or
September 2022 monthly file), which the JPL guide does not list; and
on 2026-09-13 the last RSS monthly file was May 2026 against August
2026 for JPL.[^rss-release][^cmr-jpl][^cmr-rss][^dataset] The JPL
Level 3 has no flag variable and carries land and ice fractions; the
RSS Level 3 carries gain-weighted and footprint land fractions, an
estimated ice fraction and, in the 8-day files, sea-ice
zones.[^jpl-guide][^podaac-jpl][^podaac-rss]

**Wrong-result mode.** A series that starts on one product and
continues on the other (to reach an earlier start, a later end, or a
missing month) steps between two smoothings, two sets of
high-latitude bias corrections and two ancillary wind products, and
the step reads as a salinity change. An anomaly computed as the JPL
value minus an RSS climatology, or the reverse, contains the
difference of the two products' mean fields, largest where their
corrections differ (high latitudes, coasts, the early mission) and
where their smoothing differs (fronts, plumes). A comparison that
reports the JPL versus RSS difference as the uncertainty of SMAP
salinity reports a producer difference, not an error bar; each
product ships its own uncertainty field, and the two fields are
different quantities (a likelihood width and a perturbation
budget).[^jpl-guide][^rss-release] A statement that "SMAP salinity"
has a given accuracy without naming the producer and version is
unverifiable, because the two products' validations are against
different references over different periods and the RSS version 6
notes defer their validation to a separate presentation.[^rss-release][^jpl-guide]

**Correct approach.** One producer and one version per series, named
by collection short name, DOI and version, with the climatology for
any anomaly computed from that same product over a stated
period.[^dataset] A comparison between the two products is a
producer-difference analysis in its own right, both products named
and their smoothing, resolution and flag treatment stated, and its
result is a difference, not an uncertainty; each product's own
uncertainty field is quoted beside its values.[^jpl-guide][^rss-release]
A gap in one product is a gap, not a splice point. A high-latitude or
early-mission statement names which version 6 corrections the RSS
product carries and that the JPL version 5 product predates
them.[^rss-release]

**Verification.** The JPL guide and the RSS release notes are the two
producers' own descriptions and were read on 2026-09-13; every
algorithm and coverage statement above is theirs.[^jpl-guide][^rss-release]
The CMR records and collection pages give the release dates, the
version 6 change list in the RSS abstract, and the granule ranges on
the verification date.[^cmr-jpl][^cmr-rss][^podaac-jpl][^podaac-rss]
The two algorithm papers' records were verified against the Crossref
registry the same day (title, authors, journal, year) and the 2018
abstract read there; the publisher pages were not
read.[^fore-2016][^meissner-2018]

[^jpl-guide]: SMAP Salinity and Wind Speed Data User's Guide, Version 5.0, JPL, November 2020
[^rss-release]: RSS SMAP Salinity Version 6.0 release notes, RSS Technical Report 011624
[^cmr-jpl]: CMR collection records for the JPL products and their granule ranges
[^cmr-rss]: CMR collection records for the RSS products and their granule ranges
[^podaac-jpl]: PO.DAAC collection page, SMAP_JPL_L3_SSS_CAP_MONTHLY_V5
[^podaac-rss]: PO.DAAC collection page, SMAP_RSS_L3_SSS_SMI_MONTHLY_V6
[^fore-2016]: Fore and others, 2016, IEEE Transactions on Geoscience and Remote Sensing, doi:10.1109/TGRS.2016.2601486
[^meissner-2018]: Meissner, Wentz and Le Vine, 2018, Remote Sensing, doi:10.3390/rs10071121
[^dataset]: This bundle's SMAP salinity dataset concept
