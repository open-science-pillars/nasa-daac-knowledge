---
type: dataset-gotcha
spheres: [hydrosphere, atmosphere]
title: "A wind analysis is not an observation: CCMP is complete everywhere because its background model fills every gap, and where no satellite fell in the window, in rain, at the sea ice edge and inside tropical cyclones the value is the adjusted ERA5 field, which nothing but the nobs field marks"
description: "CCMP combines satellite winds with an adjusted ERA5 background by a variational analysis that ties the field to the satellites where they exist and relaxes smoothly to the background with distance from a swath. The daily files' nobs field is zero wherever no satellite observation fell inside the 6-hour window, and there the value is the background; rain-flagged and sea-ice-influenced retrievals are excluded before the analysis, so the background also stands in under rain and near ice; the guide states the product does not resolve tropical cyclones and that large-scale decadal changes are comparable to its own long-term errors. A study that treats the grid as observed wind, validates a model with it, or reads a case study or a trend from it without carrying nobs reports the background model and the changing satellite constellation as if they were measurements."
tags: [ccmp, wind-analysis, level4, era5, background, nobs, data-assimilation, observation, validation, trends, tropical-cyclones]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T13:30:00Z }
severity: high
dataset: ../datasets/ccmp-wind-analysis.md
eval_case: wind-analysis-is-not-observation
status: draft
stale_after: 2027-03-15
sources:
  - id: guide
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ccmp/open/L4_V3.1/docs/User_Guide_3.1.r1.pdf
    title: "CCMP Version 3.1 User Guide, Mears and Henze, 15 July 2024 (read in full 2026-09-15): the analysis description (cost function, satellite winds where available, smooth transition to the adjusted background), the pre-analysis adjustments of ERA5, the rain and sea ice exclusions, the nobs definition in the daily and monthly file tables, the validation split into SAT and NOSAT collocations with its two tables, and the caveats on tropical cyclones and long-term trends"
  - id: cmr-6hr
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2916514952-POCLOUD.umm_json
    title: "CMR collection record, C2916514952-POCLOUD (read 2026-09-15): the abstract's description of CCMP as a combination of satellite retrievals and a reanalysis background field, the version 3.1 statement on minimized spurious trends from the interaction of satellite availability with satellite and model biases, and the processing level 4"
  - id: podaac-6hr
    resource: https://podaac.jpl.nasa.gov/dataset/CCMP_WINDS_10M6HR_L4_V3.1
    title: "PO.DAAC collection page, CCMP_WINDS_10M6HR_L4_V3.1 (read 2026-09-15): the variable table naming nobs as the number of observations used to derive the wind vector components"
  - id: mears-2022
    resource: https://doi.org/10.3390/rs14174230
    title: "Mears, Lee, Ricciardulli, Wang and Wentz, 2022, Improving the Accuracy of the Cross-Calibrated Multi-Platform (CCMP) Ocean Vector Winds, Remote Sensing 14, 4230: the abstract's statement that earlier versions were systematically too low at high winds where no collocated satellite measurement was available, and that version 2.0 showed spurious interannual to decadal variations from the interaction of satellite and model bias with the varying number of satellites (registry record verified and abstract read there 2026-09-15; the article was not read)"
  - id: atlas-2011
    resource: https://doi.org/10.1175/2010BAMS2946.1
    title: "Atlas and others, 2011, A Cross-calibrated, Multiplatform Ocean Surface Wind Velocity Product for Meteorological and Oceanographic Applications, Bulletin of the American Meteorological Society 92, 157 to 174: the variational analysis the guide cites (registry record verified 2026-09-15; the record carries no abstract and the article was not read)"
  - id: manaster-2019
    resource: https://doi.org/10.1175/jtech-d-18-0116.1
    title: "Manaster, Ricciardulli and Meissner, 2019, Validation of High Ocean Surface Winds from Satellites Using Oil Platform Anemometers, Journal of Atmospheric and Oceanic Technology 36, 803 to 818: the abstract's finding that the ECMWF, NCEP and CCMP analyses of the time were significantly lower than anemometer winds with biases growing with wind speed (registry record verified and abstract read there 2026-09-15; the article was not read)"
  - id: measures-guide
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/measures_ocean_surface_wind_vectors/open/docs/2022_12_02_MEASURES_NewDataGuide_v17_accepted.pdf
    title: "MEaSUREs OSVW user's guide, Hristova-Veleva and others, 1 December 2022 (read in full 2026-09-15): the distinction between Level 3 grids, which hold data only where a swath fell and involve no model, and Level 4 products, which use models and data assimilation to remove gaps and so carry model-specific characteristics, and the four error sources it names for quantities derived from blended Level 4 winds"
  - id: dataset
    resource: ../datasets/ccmp-wind-analysis.md
    title: "This bundle's CCMP dataset concept (read 2026-09-15): the collections, the file layout, the validation statistics and the absence of an uncertainty field"
  - id: ascat
    resource: ../datasets/ascat-winds.md
    title: "This bundle's ASCAT dataset concept (read 2026-09-15): the swath products and the ESDR Level 3 grids that hold only observed cells"
---

# A wind analysis is not an observation

**Mechanism.** CCMP is a Level 4 analysis: a variational method
combines satellite wind retrievals with a background wind field from a
numerical weather prediction model, minimizing a cost function that
constrains the differences between the inputs and the product and the
smoothness of those differences, so the field is very close to the
satellite winds at the places and times they exist and transitions
smoothly to the adjusted background with increasing distance from a
swath.[^guide][^atlas-2011][^cmr-6hr] The background is ERA5
neutral-stability wind, adjusted before the analysis for the moving
surface, by a multiplicative speed correction fitted to scatterometer
histograms and by seasonal bias maps in the components; it is still a
model field, and the analysis is what stands wherever no satellite
constrains it.[^guide] The daily files say where that is: `nobs` is
the number of satellites assimilated at each grid cell, and a value of
zero means no satellite observation was available inside the 6-hour
assimilation window, so the wind there is the adjusted
background.[^guide][^podaac-6hr] The exclusions widen that region:
radiometer winds are dropped where total cloud water exceeds 0.18 mm,
scatterometer retrievals flagged for rain are dropped, and no retrieval
influenced by sea ice is used, so under rain and near the ice edge the
satellites are absent by rule and the background fills in; whether
the files carry a value or a fill under sea ice itself was not read
from a granule.[^guide][^dataset] The monthly files redefine `nobs` as the number of time
steps averaged at each cell, so the monthly product carries no count
of satellite contributions at all.[^guide] The guide's own validation
measures the difference between the two regimes: against the withheld
ASCAT-C the wind-speed standard deviation is 0.75 m/s where at least
one satellite was assimilated and 1.25 m/s where none was, and
against moored buoys 0.97 m/s against 1.45 m/s, with the caution that
many no-satellite collocations sit at high latitudes where winds are
higher.[^guide] The version history is the history of the model side
as much as the satellite side: ERA-40, ERA-Interim and then ERA5
backgrounds, and a version 2.0 that showed spurious interannual to
decadal variations caused by the interaction of satellite and model
bias with the number of satellites available as missions began and
ended, which version 3.0 and 3.1 set out to minimize by adjusting the
sources to match each other before combining
them.[^guide][^mears-2022][^cmr-6hr] The guide states two limits of
its own: tropical cyclones and other intense compact wind events are
not well resolved in ERA5 and the satellite data are often missing
there through rain contamination, so the product is not for the
analysis of those events; and at global and basin scales decadal
wind-speed changes are expected to be small or comparable to the
product's long-term errors, so large-scale long-term changes call for
caution while regional changes larger than a few tenths of a metre
per second should be usable.[^guide] Earlier CCMP versions were also
systematically too low at high winds where no collocated satellite
measurement existed, and the oil-platform validation found the
analyses of the time significantly lower than anemometer winds with
biases growing with speed.[^mears-2022][^manaster-2019] The MEaSUREs
scatterometer project states the same distinction from the other side:
a Level 3 grid holds data only where a swath fell that day and
involves no model, while a Level 4 product uses models and data
assimilation to remove the gaps and so carries model-specific
characteristics into the final field.[^measures-guide][^ascat]

**Wrong-result mode.** A study that reads the CCMP grid as observed
wind treats the background as a measurement wherever `nobs` is zero
and wherever rain or ice removed the satellites: a wind statistic
under a convective region, at the ice edge or in a swath gap is a
statistic of adjusted ERA5, and a case study of a tropical cyclone
from CCMP describes a field the guide says does not resolve the
event.[^guide] A model evaluation against CCMP that scores a model in
a region where CCMP is background compares two models, one of them
ERA5 with adjustments, and a study that validates against both
ERA5 and CCMP compares against one field twice wherever no satellite
contributed, since CCMP is the adjusted ERA5 background
there.[^guide][^cmr-6hr] A
trend from the record, especially across the years when satellites
entered and left the constellation, carries the satellite-model bias
interaction the product's own versions were built to suppress, and
the guide states that basin-scale decadal changes are comparable to
its own long-term errors.[^mears-2022][^guide] A high-wind statistic
in a no-satellite region inherits the background's low bias at high
speed in earlier versions and the deliberate high bias of version 3.1
above about 15 to 18 m/s.[^mears-2022][^guide] The monthly product
gives no way to tell which cells rested on satellites, so a monthly
mean quoted without the daily `nobs` cannot say how much of it was
observed.[^guide] None of this raises an error: the grid is gap-free,
the values are plausible everywhere, and the files carry no
uncertainty field.[^dataset]

**Correct approach.** A result from CCMP names what CCMP is: a Level
4 variational analysis of satellite winds on an adjusted ERA5
background, with the value where `nobs` is zero being that
background.[^guide][^cmr-6hr] A statistic from the daily files carries
the fraction of contributing cells with `nobs` greater than zero, or
is computed on those cells alone when the question is about observed
wind, and a monthly figure is accompanied by that fraction from the
daily files of the same month.[^guide][^podaac-6hr] A question about
observed winds only (a scatterometer validation, a wind field free of
model characteristics) goes to the swath products or to a Level 3
grid such as the ESDR daily grids, which hold data only where a swath
fell.[^measures-guide][^ascat] A question about a tropical cyclone or
another intense compact event is outside what the guide says the
product resolves, and a large-scale decadal trend from the record is
stated beside the guide's own caution and the version history of the
background.[^guide][^mears-2022] A comparison against ERA5 or against
a model that assimilates the same satellites states that CCMP's
background is ERA5 and its inputs are the assimilated
satellites.[^guide]

**Verification.** The guide's sections on the processing methodology,
the background field, the pre-analysis adjustments, the file structure,
the validation and the caveats are the product's own statements of the
analysis, the exclusions, the meaning of `nobs`, the SAT and NOSAT
statistics and the limits; they were read in full on
2026-09-15.[^guide] The collection record and page repeat the
combination of satellite winds with a reanalysis background, the
version 3.1 trend statement and the `nobs` definition.[^cmr-6hr][^podaac-6hr]
The 2022 paper's abstract, read on the registry record on 2026-09-15,
states the version 2.0 spurious variations and the high-wind low bias
where no satellite was collocated; the 2011 paper's record was
verified the same day and carries no abstract; the 2019 abstract
states the analyses' low bias against anemometers.[^mears-2022][^atlas-2011][^manaster-2019]
The MEaSUREs guide's Level 3 against Level 4 statement was read in
full the same day.[^measures-guide] No granule was opened, so the
`nobs` fill and encoding, and whether ice-covered cells hold a value
or a fill, are not stated here beyond the guide's tables.[^dataset]

[^guide]: CCMP Version 3.1 User Guide, Mears and Henze, 15 July 2024
[^cmr-6hr]: CMR collection record, C2916514952-POCLOUD
[^podaac-6hr]: PO.DAAC collection page, CCMP_WINDS_10M6HR_L4_V3.1
[^mears-2022]: Mears and others, 2022, Remote Sensing, doi:10.3390/rs14174230
[^atlas-2011]: Atlas and others, 2011, Bulletin of the American Meteorological Society, doi:10.1175/2010BAMS2946.1
[^manaster-2019]: Manaster, Ricciardulli and Meissner, 2019, Journal of Atmospheric and Oceanic Technology, doi:10.1175/jtech-d-18-0116.1
[^measures-guide]: MEaSUREs OSVW user's guide, Hristova-Veleva and others, 1 December 2022
[^dataset]: This bundle's CCMP dataset concept
[^ascat]: This bundle's ASCAT dataset concept
