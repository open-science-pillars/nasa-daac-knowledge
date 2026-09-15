---
type: dataset-gotcha
spheres: [hydrosphere, atmosphere]
title: "Scatterometer rain and sea ice flags decide which cells are winds: a rainy cell or an ice-edge cell carries a plausible wind vector, the two ASCAT product families flag them differently, and a series or a climatology built without the flags, or with all of them, measures the flagging"
description: "Rain and sea ice change the backscatter a scatterometer reads as wind. The OSI SAF files carry a wind vector cell quality flag, an ice probability, an ice age parameter and a backscatter distance; the JPL ESDR carries 23 quality bits (rain, ice edge, ice nearby, coastal, high and low wind among them) and a six-level quality indicator, with rain neither detected nor corrected for ASCAT in that retrieval. CCMP excludes every rain-flagged and ice-influenced retrieval before its analysis. A wind used without its flags includes ice-edge and rain-affected cells as ocean wind; a climatology that drops every flagged cell removes the rainy, convective, high-wind cases, which the MEaSUREs guide reports as more damaging to derivative climatologies than keeping corrected cells; and an ice-edge series is a series of ice decisions."
tags: [scatterometer, ascat, rain, sea-ice, quality-flags, wvc_quality_flag, ice_prob, quality-indicator, coastal, climatology, ccmp]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T13:30:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-15T14:22:23Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/163 }
severity: medium
dataset: ../datasets/ascat-winds.md
status: stable
stale_after: 2027-03-15
sources:
  - id: podaac-b25
    resource: https://podaac.jpl.nasa.gov/dataset/ASCATB-L2-25km
    title: "PO.DAAC collection page, ASCATB-L2-25km (read 2026-09-15): the variable table with wvc_quality_flag (wind vector cell quality), ice_prob (ice probability), ice_age (a-parameter, dB) and bs_distance (backscatter distance); the other OSI SAF pages carry the same table"
  - id: cmr-bcoastal
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2075141605-POCLOUD.umm_json
    title: "CMR collection record, C2075141605-POCLOUD (read 2026-09-15): the coastal retrieval that discards all non-sea full-resolution backscatter before the box average and retrieves winds to about 15 km from the coast where the standard product's static land mask keeps about 35 km"
  - id: cmr-b25
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2075141559-POCLOUD.umm_json
    title: "CMR collection record, C2075141559-POCLOUD (read 2026-09-15): the KNMI product manual linked as the user's guide and the advice to check it for known problems, and the KNMI anomaly page linked for reported modifications"
  - id: measures-guide
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/measures_ocean_surface_wind_vectors/open/docs/2022_12_02_MEASURES_NewDataGuide_v17_accepted.pdf
    title: "MEaSUREs OSVW user's guide, Hristova-Veleva and others, 1 December 2022 (read in full 2026-09-15): the 23 flag bit meanings, the quality indicator categories for QuikSCAT and their ASCAT differences (rain neither detected nor corrected, coastal retrieval not attempted, ice edge as indicator 3), the percentages per category, the remark that excluding rain-contaminated data is more detrimental to derivative climatologies than including corrected data, the uncertainty scaling for indicator 2 and 3 cells, and the rain-flagged gaps named as an error source of blended products"
  - id: podaac-esdr-b
    resource: https://podaac.jpl.nasa.gov/dataset/ASCATB_ESDR_L2_WIND_STRESS_V1.1
    title: "PO.DAAC collection page, ASCATB_ESDR_L2_WIND_STRESS_V1.1 (read 2026-09-15): the variable table with flags, quality_indicator, rain_speed_bias, en_wind_speed_uncorrected (without rain corrections) and distance_from_coast"
  - id: ccmp-guide
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ccmp/open/L4_V3.1/docs/User_Guide_3.1.r1.pdf
    title: "CCMP Version 3.1 User Guide, Mears and Henze, 15 July 2024 (read in full 2026-09-15): the quality control section (radiometer winds dropped above 0.18 mm total cloud water, scatterometer retrievals flagged for rain by the retrieval's rain detection dropped, no retrieval influenced by sea ice used) and the tropical cyclone caveat that satellite data are often missing there through rain contamination"
  - id: calval
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ascat/preview/L2/docs/ASCAT_calval_250.pdf
    title: "OSI SAF technical note TN/163, Calibration and Validation of ASCAT Winds, version 4.0, 2008 (read in full 2026-09-15): the ice line drawn beside the wind cone in measurement space, the exclusion of all cells poleward of 55 degrees from the normalisation to avoid ice contamination, the conservative filtering of land and ice in the comparisons, and the maximum-likelihood quality control rejecting about 0.4 to 0.5 percent of cells, rising toward the outer swath"
  - id: dataset
    resource: ../datasets/ascat-winds.md
    title: "This bundle's ASCAT dataset concept (read 2026-09-15): the two product families, their flag fields and the ESDR quality classes"
  - id: ccmp
    resource: ../datasets/ccmp-wind-analysis.md
    title: "This bundle's CCMP dataset concept (read 2026-09-15): the analysis that receives only unflagged retrievals"
  - id: smap-ice
    resource: ../gotchas/smap-sss-coastal-and-sea-ice-contamination.md
    title: "This bundle's SMAP salinity gotcha on coasts and the sea ice edge (read 2026-09-15): the same shape of trap for a radiometer, where a series near ice is a series of the product's exclusion decisions"
---

# Scatterometer rain and ice flags

**Mechanism.** A scatterometer reads wind from backscatter, and rain
and sea ice both change the backscatter: the two scatterometer bands
have different sensitivity to rain, C-band the less sensitive, and sea
ice returns a signal that in the OSI SAF measurement space lies on its
own ice line beside the wind cone.[^measures-guide][^calval] Every
ASCAT file at PO.DAAC therefore carries fields that say which cells
are winds. The OSI SAF Level 2 files carry `wvc_quality_flag` (the
wind vector cell quality), `ice_prob` (an ice probability), `ice_age`
(the a-parameter, in decibels) and `bs_distance` (the backscatter
distance), and the 2008 calibration note for MetOp-A with CMOD5 describes a
quality control that rejected cells whose normalised distance to the
model function cone exceeded a threshold tuned, at that time, for a
rejection rate of about 0.4 to 0.5 percent, higher toward the outer
swath; the coastal stream discards every non-sea backscatter
sample before averaging so that it can retrieve to about 15 km from
the coast where the standard product keeps a static mask of about 35
km.[^podaac-b25][^calval][^cmr-bcoastal] The bit meanings of
`wvc_quality_flag` are defined in the KNMI product manual, which the
collection records link as the user's guide and advise reading for
known problems; that manual lies on a host outside this concept's
sources and was not read, so the bit meanings are not stated
here.[^cmr-b25] The JPL ESDR files carry a 23-bit `flags` mask whose
named bits include adequate sigma-0 and azimuth diversity, poor
coastal processing, coastal, ice edge, ice nearby, high and low wind
speed, rain impact, rain impact not usable, rain nearby, large and
significant rain correction, rain correction applied and not applied,
missing look and lake winds, plus a `quality_indicator` from 0 (no
retrieval corruption) through 1 (insignificantly corrupted), 2
(possible significant error), 3 (likely significant error), 4 (no
winds retrieved due to quality control) and 5 (no data over liquid
water), and the fields `rain_speed_bias` and
`en_wind_speed_uncorrected`.[^measures-guide][^podaac-esdr-b] For
ASCAT in that retrieval, rain contamination is neither detected nor
corrected and coastal retrieval is not attempted, so the ASCAT
indicator classes are set by swath position, missing looks and ice
alone: 92.4 percent of retrieved cells are indicator 0, 7.2 percent
indicator 1, 1.4 percent indicator 2 (near but not on the ice edge)
and 0.4 percent indicator 3 (on the ice edge), with indicator 2 and 3
uncertainties scaled to about twice and about 1.5 times the base
error.[^measures-guide] For the Ku-band QuikSCAT product in the same
family, indicator 2 holds cells where rain was detected in the cell or
its 7 by 7 neighbourhood and a correction of less than 15 m/s was
applied, and the guide reports that several studies found excluding
rain-contaminated data more detrimental to the accuracy of wind
derivative climatologies than including corrected data, because the
excluded cells sit in the most dynamic regions.[^measures-guide] CCMP
applies the flags before its analysis: scatterometer retrievals
flagged for rain by the retrieval's own rain detection are not used,
radiometer winds are dropped where total cloud water exceeds 0.18 mm,
and no retrieval influenced by sea ice is used, so the analysis under
rain and near ice is background and the guide names rain contamination
as one reason tropical cyclones are missing from the satellite
input.[^ccmp-guide][^ccmp] The MEaSUREs guide lists biases from
missing observations in rain-flagged areas among the four error
sources of quantities derived from blended products.[^measures-guide]
The same shape of trap holds for the SMAP salinity radiometer at
coasts and the ice edge, where the bundle's gotcha records that a
series near ice is a series of the product's exclusion decisions.[^smap-ice]

**Wrong-result mode.** A wind statistic computed from an OSI SAF file
on `wind_speed` alone, without `wvc_quality_flag` and `ice_prob`,
counts ice-edge cells and quality-rejected cells as ocean wind, and
the file gives them a plausible vector; the same on an ESDR file
without `flags` or `quality_indicator` counts the indicator 2 and 3
cells whose stated uncertainty is 1.5 to 2 times the base
error.[^podaac-b25][^measures-guide] A wind climatology that drops
every flagged cell drops the rainy, convective and high-wind cases
from the regions where they matter most, which the guide reports as
worse for derivative climatologies than keeping corrected cells, so
the choice of flag policy is itself a bias with a sign that depends on
the quantity.[^measures-guide] A series at the ice edge follows the
seasonal advance and retreat of the flagged region: the cells that
enter and leave the series are chosen by `ice_prob` or by the ice
bits, so a trend or a seasonal cycle there measures the ice mask as
much as the wind.[^podaac-b25][^measures-guide][^smap-ice] A
comparison of the OSI SAF product with the ESDR that does not align
their flag policies compares a retrieval with rain-flagged cells
removed by one rule against a retrieval in which rain is not detected
at all.[^measures-guide] A comparison of CCMP with a scatterometer
swath under rain compares the background with an excluded retrieval,
since CCMP received no rain-flagged cells.[^ccmp-guide] A coastal
wind statistic that mixes the standard and coastal streams mixes a 35
km mask with a 15 km one.[^cmr-bcoastal] None of this raises an error:
the flagged cells hold numbers in the valid range.[^dataset]

**Correct approach.** A result from an ASCAT product names the flag
policy it applied: which `wvc_quality_flag` bits or which
`quality_indicator` classes were kept, what `ice_prob` threshold was
used, and whether rain-flagged cells were kept, corrected or dropped,
with the reason given in terms of the quantity (a mean wind, a
derivative climatology, an extreme-wind statistic) rather than as a
default.[^measures-guide][^podaac-b25] The bit meanings for the OSI
SAF flag come from the KNMI product manual the collection records
link, and a policy stated without having read it is stated as
such.[^cmr-b25] A series near the ice edge or the coast carries the
flagged fraction of its cells through time, and a series that spans
the operational and ESDR families, or an ASCAT family and CCMP, states
that their rain and ice treatments differ.[^measures-guide][^ccmp-guide]
A statistic that keeps indicator 2 or 3 cells uses the per-cell
uncertainty fields that the ESDR scales for them.[^measures-guide][^podaac-esdr-b]

**Verification.** The OSI SAF collection page's variable table and the
coastal record's abstract were read on 2026-09-15; the KNMI product
manual and anomaly pages the records link were not read, and no bit
meaning of `wvc_quality_flag` is stated here for that
reason.[^podaac-b25][^cmr-bcoastal][^cmr-b25] The MEaSUREs guide's
file-content, quality-indicator and uncertainty sections, which list
the ESDR bits and classes, their percentages and the ASCAT differences,
were read in full the same day, as were the ESDR collection page's
variable table, the CCMP guide's quality-control section and the 2008
calibration note.[^measures-guide][^podaac-esdr-b][^ccmp-guide][^calval]
No granule was opened, so the flag encodings and fill values are not
stated beyond the guide's listing.[^dataset][^ccmp]

[^podaac-b25]: PO.DAAC collection page, ASCATB-L2-25km
[^cmr-bcoastal]: CMR collection record, C2075141605-POCLOUD
[^cmr-b25]: CMR collection record, C2075141559-POCLOUD
[^measures-guide]: MEaSUREs OSVW user's guide, Hristova-Veleva and others, 1 December 2022
[^podaac-esdr-b]: PO.DAAC collection page, ASCATB_ESDR_L2_WIND_STRESS_V1.1
[^ccmp-guide]: CCMP Version 3.1 User Guide, Mears and Henze, 15 July 2024
[^calval]: OSI SAF technical note TN/163, Calibration and Validation of ASCAT Winds, version 4.0, 2008
[^dataset]: This bundle's ASCAT dataset concept
[^ccmp]: This bundle's CCMP dataset concept
[^smap-ice]: This bundle's SMAP salinity coastal and sea ice gotcha
