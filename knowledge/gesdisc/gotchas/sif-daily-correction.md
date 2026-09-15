---
type: dataset-gotcha
spheres: [biosphere, atmosphere]
title: "The Daily_SIF fields are the instantaneous retrievals times a clear-sky geometric factor: the daily correction factor is the ratio of the day's integrated cosine of the solar zenith angle to its value at the overpass, not an observed daily mean, and an instantaneous and a daily field are different quantities"
description: "Each sounding carries a daily_correction_factor computed from the cosine of the solar zenith angle at the observation and its integral over the day in ten-minute steps, under cloud-free conditions and ignoring Rayleigh scattering and gas absorption; Daily_SIF_757nm, Daily_SIF_771nm and Daily_SIF_740nm are the corresponding instantaneous fields multiplied by it. The correction exists because the 13:30 local overpass value of OCO-2, particularly at high latitude, cannot be compared directly with a daily quantity such as GPP; it is a first-order length-of-day scaling whose error is not in the uncertainty fields. A series or comparison that mixes SIF and Daily_SIF, or reads Daily_SIF as a measured daily average, carries a latitude- and season-dependent factor as signal."
tags: [oco-2, oco-3, sif, daily-correction-factor, daily_sif, solar-zenith-angle, length-of-day, overpass-time, oco2_l2_lite_sif, gesdisc, biosphere]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T18:35:00Z }
severity: low
dataset: ../datasets/oco2-sif-lite.md
status: draft
stale_after: 2027-03-15
sources:
  - id: ug-v11
    resource: https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_SIF_v11.2_OCO3_v11_Data_Users_Guide_20250707.pdf
    title: "Kurosu, Frankenberg, Payne and Osterman, 2025, OCO-2 and OCO-3 Solar Induced Chlorophyll Fluorescence Data User's Guide, Lite File Version 11 and 11.2, version 3.0 revision A, 7 July 2025 (read 2026-09-15: section 3.1 on the daily correction factor, its cosine-of-solar-zenith-angle derivation in ten-minute steps under cloud-free conditions ignoring Rayleigh scattering and gas absorption, its purpose for the 13:30 overpass at high latitude, and Table 4-4 with the Daily_SIF formulas)"
  - id: opendap-dmr
    resource: https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L2_Lite_SIF.11.2r/2024/oco2_LtSIF_240402_B11217Ar_241023161757s.nc4.dmr
    title: "DAP4 metadata of the OCO-2 Lite SIF granule of 2024-04-02 (read 2026-09-15: the description attributes of Daily_SIF_740nm, SIF_740 times /Science/daily_correction_factor, and of daily_correction_factor, a correction factor to estimate daily average SIF from instantaneous SIF using pure geometric incoming light scaling)"
  - id: parazoo-2019
    resource: https://doi.org/10.1029/2019JG005289
    title: "Parazoo and others, 2019, Towards a Harmonized Long-Term Spaceborne Record of Far-Red Solar-Induced Fluorescence, Journal of Geophysical Research Biogeosciences 124, 2518 to 2539 (record and abstract read on the Crossref registry 2026-09-15: time of day and sun-sensor geometry are among the instrument differences corrected before sensors agree)"
  - id: oco3-release
    resource: https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO3_L2_Data_Release_Statement_v11_V1_RevA.pdf
    title: "OCO-3 Level 2 Data Release Statement, version 11 (read 2026-09-15: OCO-3 has operated on the International Space Station since May 2019, with science data from August 2019)"
  - id: dataset
    resource: ../datasets/oco2-sif-lite.md
    title: "This bundle's OCO-2 and OCO-3 SIF Lite dataset concept, which describes the fields and lists this trap"
---

# The daily correction factor

**Mechanism.** Fluorescence at the time of an overpass is a strong
function of the illumination, and OCO-2 observes at about 13:30
local solar time, so the guide provides a factor to estimate a daily
average from the instantaneous value: under cloud-free conditions,
ignoring Rayleigh scattering and gas absorption, the downwelling
solar radiation scales with the cosine of the solar zenith angle,
and the first-order daily average is the observed value scaled by
the ratio of the cosine integrated over the day to the cosine at the
observation time, the integral being sampled numerically in
ten-minute steps.[^ug-v11] The factor is stored per sounding as
/Science/daily_correction_factor, as a function of latitude,
longitude and time, and the root-level Daily_SIF_757nm,
Daily_SIF_771nm and Daily_SIF_740nm are the corresponding instantaneous
fields multiplied by it, as the description attributes
state.[^ug-v11][^opendap-dmr] The guide's stated reason is that the
overpass value, particularly at high latitude, cannot be compared
directly with GPP because length of day and the variation of the
solar zenith angle enter.[^ug-v11] OCO-3 flies on the International
Space Station and the factor is computed per sounding from its own
time, so the two instruments' factors differ for the same place and
day wherever their observation times differ.[^oco3-release][^ug-v11]

**Wrong-result mode.** SIF_740nm and Daily_SIF_740nm differ by a
factor that depends on latitude, day of year and observation time,
so a series that switches between them, or a comparison of one
instrument's Daily_SIF with another's instantaneous value, carries
that geometry as signal.[^ug-v11] Read as a measured daily mean, the
Daily_SIF field claims more than it is: the scaling is geometric and
clear-sky, so on a cloudy afternoon or under a diurnal cycle of
stress it is an estimate whose error is not in
SIF_Uncertainty_740nm, which is the retrieval noise alone scaled by
the same factor.[^ug-v11] Between sensors, time of day is one of the
differences corrected before their records agree, and the factor
does part of that work between OCO-2 and OCO-3.[^parazoo-2019][^oco3-release]

**Correct approach.** An analysis uses one of the two forms and
names it: the instantaneous field for anything compared with a
measurement at the overpass time or with another sensor after its
own time-of-day correction, and the daily-corrected field for a
comparison with a daily quantity, with the statement that the
correction is geometric and clear-sky; the factor itself is
available per sounding and its range over a region and season is a
stated part of the method.[^ug-v11][^parazoo-2019]

**Verification.** The guide's section 3.1 carries the derivation and
the ten-minute sampling, and Table 4-4 the product formulas; the
DAP4 metadata of any granule shows the same formula in the
description of Daily_SIF_740nm and the words pure geometric incoming
light scaling on daily_correction_factor.[^ug-v11][^opendap-dmr] The
check a reader runs: on one granule Daily_SIF_740nm divided by
SIF_740nm equals daily_correction_factor to the least significant
digit, and the factor varies with latitude across one day's soundings
and, at one latitude, with day of year across the record.[^ug-v11] The dataset
concept lists this trap.[^dataset]

[^ug-v11]: Kurosu and others, 2025, OCO-2 and OCO-3 SIF Data User's Guide, Lite file version 11 and 11.2
[^opendap-dmr]: DAP4 metadata of the OCO-2 Lite SIF granule of 2024-04-02, read 2026-09-15
[^parazoo-2019]: Parazoo and others, 2019, Journal of Geophysical Research Biogeosciences, doi:10.1029/2019JG005289
[^oco3-release]: OCO-3 Level 2 Data Release Statement, version 11
[^dataset]: This bundle's OCO-2 and OCO-3 SIF Lite dataset concept
