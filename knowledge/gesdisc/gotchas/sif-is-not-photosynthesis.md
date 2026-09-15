---
type: dataset-gotcha
spheres: [biosphere, atmosphere]
title: "OCO-2 SIF is a radiance emitted by chlorophyll, not a photosynthesis rate: the file carries no gross primary production, the SIF to GPP relation is empirical, scale-dependent and varies with biome and physiology, and a SIF value read as GPP is a number with an unstated slope"
description: "The SIF Lite fields are solar-induced chlorophyll fluorescence in W per square metre per steradian per micrometre at 757, 771 or a derived 740 nm, retrieved from Fraunhofer-line in-filling and corrected to a daily barren-surface background; nothing in the file is gross primary production, light-use efficiency or carbon uptake. Fluorescence is emitted from the photosynthetic apparatus and has been linked to GPP empirically at flux sites and in global patterns, with the slope depending on the ratio of the light-use efficiencies of carbon assimilation and of fluorescence, which vary with plant type, season and stress; the OCO-2 flux-site comparison found the relation more consistent across biomes than earlier work suggested, and the mission's own guide states that the instantaneous overpass value cannot be compared directly with GPP. A SIF map presented as photosynthesis, or a GPP number formed from SIF by an unstated conversion, is therefore silently wrong: it carries a slope, a wavelength, an illumination correction and a background choice that the reader cannot see."
tags: [oco-2, oco-3, sif, gpp, photosynthesis, light-use-efficiency, chlorophyll-fluorescence, oco2_l2_lite_sif, gesdisc, biosphere]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T18:20:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-15T18:36:49Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/173 }
severity: high
dataset: ../datasets/oco2-sif-lite.md
eval_case: sif-is-not-photosynthesis
status: draft
stale_after: 2027-03-15
sources:
  - id: ug-v11
    resource: https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_SIF_v11.2_OCO3_v11_Data_Users_Guide_20250707.pdf
    title: "Kurosu, Frankenberg, Payne and Osterman, 2025, OCO-2 and OCO-3 Solar Induced Chlorophyll Fluorescence Data User's Guide, Lite File Version 11 and 11.2, version 3.0 revision A, 7 July 2025 (read 2026-09-15: section 2.10 on relative fluorescence as the retrieved quantity and the barren-surface background, section 2.11 on the 740 nm reference and the wavelength dependence of absolute fluorescence, section 3.1 stating that the 13:30 overpass value cannot be compared directly with GPP, the quality-flag rationale calling the retrievals accurate but imprecise, and Table 4-1, the complete field list, which has no GPP or photosynthesis field)"
  - id: opendap-dmr
    resource: https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L2_Lite_SIF.11.2r/2024/oco2_LtSIF_240402_B11217Ar_241023161757s.nc4.dmr
    title: "DAP4 metadata of the OCO-2 Lite SIF granule of 2024-04-02 (read 2026-09-15: the units attribute W/m^2/sr/micrometre and the long names Solar Induced Fluorescence at 740 nm and Daily Corrected Solar Induced Fluorescence on every SIF variable, and the full variable list; the on-premises URL is retired after September 2026 and the durable form of the same metadata is the Cloud OPeNDAP .dmr.xml of the granule behind Earthdata Login)"
  - id: doughty-2022
    resource: https://doi.org/10.5194/essd-14-1513-2022
    title: "Doughty, Kurosu, Parazoo, Köhler, Wang, Sun and Frankenberg, 2022, Global GOSAT, OCO-2, and OCO-3 solar-induced chlorophyll fluorescence datasets, Earth System Science Data 14, 1513 to 1529 (record and abstract read on the Crossref registry 2026-09-15: the paper names the indirect relationship between SIF and photosynthesis among the considerations a user needs for proper interpretation)"
  - id: sun-2017
    resource: https://doi.org/10.1126/science.aam5747
    title: "Sun and others, 2017, OCO-2 advances photosynthesis observation from space via solar-induced chlorophyll fluorescence, Science 358, 6360 (record and structured abstract read on the Crossref registry 2026-09-15: SIF is emitted from the core of the photosynthetic machinery, the flux-site SIF-GPP relationships were more consistent across biomes than previously suggested, a universal relationship cannot be dismissed but process-based studies are needed, and the coordinated dynamics of the light-use efficiencies of CO2 assimilation and of fluorescence emission are of critical importance)"
  - id: magney-2019-pnas
    resource: https://doi.org/10.1073/pnas.1900278116
    title: "Magney and others, 2019, Mechanistic evidence for tracking the seasonality of photosynthesis with solar-induced fluorescence, Proceedings of the National Academy of Sciences 116, 11640 to 11645 (record and abstract read on the Crossref registry 2026-09-15: SIF has been empirically linked to GPP at large spatial scales; at one winter-dormant conifer forest SIF and GPP correlate with R squared 0.62 to 0.92 and an invariant slope over hourly to weekly timescales, and the seasonal variation of SIF yield reflects photoprotective pigments and photosystem II operating efficiency)"
  - id: frankenberg-2011b
    resource: https://doi.org/10.1029/2011GL048738
    title: "Frankenberg and others, 2011, New global observations of the terrestrial carbon cycle from GOSAT: Patterns of plant fluorescence with gross primary productivity, Geophysical Research Letters 38, L17706 (the origin of the satellite SIF to GPP comparison the user guide cites; record read on the Crossref registry 2026-09-15, no abstract carried)"
  - id: sun-2018
    resource: https://doi.org/10.1016/j.rse.2018.02.016
    title: "Sun, Frankenberg, Jung, Joiner, Guanter, Köhler and Magney, 2018, Overview of Solar-Induced chlorophyll Fluorescence (SIF) from the Orbiting Carbon Observatory-2: Retrieval, cross-mission comparison, and global monitoring for GPP, Remote Sensing of Environment 209, 808 to 823 (record read on the Crossref registry 2026-09-15; the registry carries no abstract and the publisher page sits behind a bot check, so this concept rests on its title and on the user guide's citation of it)"
  - id: dataset
    resource: ../datasets/oco2-sif-lite.md
    title: "This bundle's OCO-2 and OCO-3 SIF Lite dataset concept, which describes the fields and lists this trap"
---

# SIF is not photosynthesis

**Mechanism.** Solar-induced chlorophyll fluorescence is light
re-emitted by chlorophyll in the red and far-red after absorption of
sunlight, and OCO-2 measures it as the fractional in-filling of solar
Fraunhofer lines in two narrow windows near 757 and 771 nm; the
retrieval's state variable is that fraction of the continuum
radiance, and the Lite processing turns it into an absolute radiance,
subtracts a daily background estimated over barren surfaces, and
reports the result in W per square metre per steradian per
micrometre, with a derived 740 nm value and a clear-sky daily
scaling.[^ug-v11][^opendap-dmr] The signal is emitted from the
photosynthetic apparatus, and satellite SIF has been linked to gross
primary production since the first GOSAT maps were compared with
flux-tower based GPP; the OCO-2 science paper describes SIF as
integrating plant physiological function in vivo and finds, at eddy
covariance sites near the orbital tracks, SIF to GPP relationships
more consistent across biomes than earlier studies had suggested,
while stating that the possibility of a universal relationship
cannot be dismissed and that process-based studies are needed to
unravel the covariation, whose critical term is the coordinated
dynamics of two light-use efficiencies, that of carbon assimilation
and that of fluorescence emission.[^frankenberg-2011b][^sun-2017] At
the leaf and canopy the link is mechanistic but not fixed: at a
winter-dormant conifer forest SIF and GPP track each other with R
squared between 0.62 and 0.92 and an invariant slope over hourly to
weekly timescales, and the seasonal change of the fluorescence yield
reflects photoprotective pigments and the operating efficiency of
photosystem II, which is why SIF captures the seasonality of
photosynthesis where reflectance indices do not.[^magney-2019-pnas]
The product paper for the Lite files lists the indirect relationship
between SIF and photosynthesis among the things a user needs to
know, beside retrieval noise and sun-sensor geometry, and the user
guide states that the 13:30 local overpass value, particularly at
high latitude, cannot be compared directly with GPP because length
of day and the solar zenith angle enter, which is the reason the
daily correction factor exists.[^doughty-2022][^ug-v11] The file
itself carries fluorescence radiances, their uncertainties,
continuum radiances, geometry, flags and meteorology, and no
variable named for GPP, photosynthesis or light-use
efficiency.[^ug-v11][^opendap-dmr]

**Wrong-result mode.** A map of SIF_740nm or Daily_SIF_740nm labelled
photosynthesis, or a GPP figure obtained by multiplying SIF by one
slope, presents a radiance as a carbon flux. The number then carries
choices the reader cannot see: which wavelength (the 757, 771 and
740 nm values differ by fixed factors and the absolute fluorescence
varies strongly across this spectral range), whether the
instantaneous or the daily-corrected field was used, which quality
flags were kept, that the value is relative to a background
estimated over barren surfaces in a three-day window, and above all
which SIF to GPP slope was assumed and from which biome and scale it
came.[^ug-v11][^sun-2017] Because the slope is the ratio of two
light-use efficiencies that respond to environment, season and
canopy, a slope taken from one biome or one season applied to
another is a different quantity; a change in SIF across a drought or
a growing season is a change in absorbed light, in canopy and in the
physiological yield together, and reading it as a change in GPP
alone attributes the whole of it to
photosynthesis.[^sun-2017][^magney-2019-pnas] The trap is silent: no
field is missing, no flag is set, and a regression of SIF on a GPP
product will return a slope and a correlation whatever the biome
mix, so the analysis runs to completion with the conversion
unexamined.[^doughty-2022]

**Correct approach.** SIF is reported as what it is: a fluorescence
radiance at a named wavelength, instantaneous or daily-corrected,
under a named quality screen, with its one-sigma uncertainty, and a
statement about GPP or photosynthesis is a separate claim that names
the empirical relation used, the biome and spatial and temporal
scale it was fitted at, and its source, so that the slope is a
visible assumption rather than a hidden one.[^ug-v11][^sun-2017] Where
the question is seasonality or relative change, SIF can be compared
with GPP as a proxy whose slope is held constant within one site or
biome, which is the setting in which the mechanistic evidence
supports an invariant slope; where the question is an absolute flux
or a comparison across biomes, the light-use efficiency ratio is
part of the answer and its variation is part of the
uncertainty.[^magney-2019-pnas][^sun-2017] Cross-mission or
cross-scale statements name the wavelength, the time-of-day
correction and the background convention of each
product.[^ug-v11][^doughty-2022]

**Verification.** The guide's Table 4-1 is the complete list of
groups and variables in a Lite file and contains no GPP or
photosynthesis field; its section 3.1 carries the sentence that the
overpass value cannot be compared directly with GPP; and the DAP4
metadata of any granule shows the units attribute W per square metre
per steradian per micrometre and long names beginning Solar Induced
Fluorescence on every SIF variable.[^ug-v11][^opendap-dmr] The
registry abstracts of the Science paper and of the product paper
carry the statements on cross-biome consistency, the universal
relationship question, the light-use efficiencies and the indirect
relationship in the words quoted above, and the conifer-forest
paper the R squared range and the yield
mechanism.[^sun-2017][^doughty-2022][^magney-2019-pnas] The check a
reader runs: a regression of gridded Daily_SIF_740nm on any gridded
GPP product returns one slope, and the same regression on the
instantaneous SIF_740nm or on the 757 nm field returns another,
which is the illumination and wavelength dependence of the number
made visible.[^ug-v11] The overview paper on
retrieval, cross-mission comparison and global monitoring for GPP is
the mission's own treatment of the question, verified on the
registry by title, authors, journal and year.[^sun-2018] The dataset
concept lists this trap.[^dataset]

[^ug-v11]: Kurosu and others, 2025, OCO-2 and OCO-3 SIF Data User's Guide, Lite file version 11 and 11.2
[^opendap-dmr]: DAP4 metadata of the OCO-2 Lite SIF granule of 2024-04-02, read 2026-09-15
[^doughty-2022]: Doughty and others, 2022, Earth System Science Data, doi:10.5194/essd-14-1513-2022
[^sun-2017]: Sun and others, 2017, Science, doi:10.1126/science.aam5747
[^magney-2019-pnas]: Magney and others, 2019, Proceedings of the National Academy of Sciences, doi:10.1073/pnas.1900278116
[^frankenberg-2011b]: Frankenberg and others, 2011, Geophysical Research Letters, doi:10.1029/2011GL048738
[^sun-2018]: Sun and others, 2018, Remote Sensing of Environment, doi:10.1016/j.rse.2018.02.016
[^dataset]: This bundle's OCO-2 and OCO-3 SIF Lite dataset concept
