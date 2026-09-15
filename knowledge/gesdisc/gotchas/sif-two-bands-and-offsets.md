---
type: dataset-gotcha
spheres: [biosphere, atmosphere]
title: "OCO-2 SIF is two retrievals, at 757 and 771 nm, each corrected by a daily barren-surface offset, and the 740 nm field is formed from them by fixed factors: values at different wavelengths, adjusted against unadjusted, and version 10 against version 11 are different quantities"
description: "The Lite file retrieves fluorescence in two windows in the oxygen A-band region, near 757 and 771 nm, the 771 nm value being typically about 1.5 times smaller; the 740 nm value is not retrieved but is 0.75 times the sum of SIF_757nm and 1.5 times SIF_771nm, chosen because 740 nm is near the far-red emission peak and is the reference other sensors report. Every retrieved value is offset-adjusted by subtracting the mean SIF over barren surfaces in a three-day window, per footprint, and the unadjusted values, the relative (fraction of continuum) values and the offset statistics are kept in the file. Version 11 moved the 757 nm window away from the detector edge and made both windows consistent between OCO-2 and OCO-3, so version 11 values differ slightly from version 10. A series or a comparison that mixes wavelengths, mixes adjusted with unadjusted or relative values, or joins version 10 to version 11 files carries a step or a scale factor that is not vegetation."
tags: [oco-2, oco-3, sif, 757nm, 771nm, 740nm, offset-correction, bias-correction, retrieval-window, version-11, oco2_l2_lite_sif, gesdisc, biosphere]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T18:25:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-15T18:36:49Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/173 }
severity: medium
dataset: ../datasets/oco2-sif-lite.md
status: stable
stale_after: 2027-03-15
sources:
  - id: ug-v11
    resource: https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_SIF_v11.2_OCO3_v11_Data_Users_Guide_20250707.pdf
    title: "Kurosu, Frankenberg, Payne and Osterman, 2025, OCO-2 and OCO-3 Solar Induced Chlorophyll Fluorescence Data User's Guide, Lite File Version 11 and 11.2, version 3.0 revision A, 7 July 2025 (read 2026-09-15: section 2.4 on the version 11 change of the retrieval windows, section 2.10 on relative fluorescence, absolute SIF and the barren-surface offset correction, section 2.11 on the 740 nm reference and conversion, Table 4-4 with the 740 nm formula and the statement that 771 nm is typically about 1.5 times smaller than 757 nm, Table 4-10 on the Offset group and Table 4-11 on the Science group's adjusted, unadjusted and relative fields)"
  - id: ug-b10
    resource: https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO23_SIF_B10_Product_Description.pdf
    title: "OCO-2 and OCO-3 SIF Data User's Guide for the build 10 Lite files, version 2.1, February 2021 (read 2026-09-15: the same offset correction and 740 nm conversion in version 10, before the window change)"
  - id: opendap-dmr
    resource: https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L2_Lite_SIF.11.2r/2024/oco2_LtSIF_240402_B11217Ar_241023161757s.nc4.dmr
    title: "DAP4 metadata of the OCO-2 Lite SIF granule of 2024-04-02 (read 2026-09-15: the description attributes carrying the formulas SIF_740nm = 0.75 * (sif_757nm + 1.5 * sif_771nm) and the uncertainty combination, the long names Offset-Adjusted and Raw on the Science group fields, and the Offset group's per-footprint statistics on 227 signal bins; the on-premises URL is retired after September 2026 and the durable form of the same metadata is the Cloud OPeNDAP .dmr.xml of the granule behind Earthdata Login)"
  - id: parazoo-2019
    resource: https://doi.org/10.1029/2019JG005289
    title: "Parazoo and others, 2019, Towards a Harmonized Long-Term Spaceborne Record of Far-Red Solar-Induced Fluorescence, Journal of Geophysical Research Biogeosciences 124, 2518 to 2539 (record and abstract read on the Crossref registry 2026-09-15: sensors and algorithms differ in wavelength, time of day, geometry, cloud effects and footprint area; GOME-2 retrieval methods differ by up to a factor of two in magnitude, attributed largely to retrieval window choice; the assumed spectral shape has negligible effect)"
  - id: magney-2019
    resource: https://doi.org/10.1029/2019JG005029
    title: "Magney and others, 2019, Disentangling Changes in the Spectral Shape of Chlorophyll Fluorescence, Journal of Geophysical Research Biogeosciences 124, 1491 to 1507 (the paper the guide cites for the wavelength conversion; record and abstract read on the Crossref registry 2026-09-15: one spectral shape explains 84 percent of the variance across species and the far-red shape beyond 740 nm is stable)"
  - id: frankenberg-2011b
    resource: https://doi.org/10.1029/2011GL048738
    title: "Frankenberg and others, 2011, New global observations of the terrestrial carbon cycle from GOSAT, Geophysical Research Letters 38, L17706 (the reference-target bias correction strategy the guide says it follows; record read on the Crossref registry 2026-09-15)"
  - id: dataset
    resource: ../datasets/oco2-sif-lite.md
    title: "This bundle's OCO-2 and OCO-3 SIF Lite dataset concept, which describes the fields and lists this trap"
---

# Two bands and their offsets

**Mechanism.** The retrieval fits fluorescence in two narrow windows
of the oxygen A-band region, near 757 and 771 nm, where solar
Fraunhofer lines are in-filled by the emission; it retrieves the
relative fluorescence, the fraction of the continuum radiance, and
the Lite post-processing forms the absolute value from it, so the
Science group holds SIF_757nm and SIF_771nm together with
SIF_Relative_757nm and SIF_Relative_771nm and the continuum radiances
at both wavelengths.[^ug-v11][^opendap-dmr] The fluorescence spectrum
falls across this range, and the 771 nm value is typically about 1.5
times smaller than the 757 nm value.[^ug-v11] Because sensors with
moderate spectral resolution report at 740 nm, near the far-red
emission peak, and absolute fluorescence varies greatly between 740
and 771 nm, the product adds a 740 nm field, formed and not
retrieved: SIF_740nm is 0.75 times the sum of SIF_757nm and 1.5
times SIF_771nm, and SIF_Uncertainty_740nm combines the two
one-sigma uncertainties by the same factors; the guide carries two
formulas, that one in Table 4-4 and, in section 2.11, 1.5 times the
sum of SIF_757nm and twice SIF_771nm divided by two, which puts a
weight one third larger on 771 nm, and the file's own description
attribute on SIF_740nm carries the Table 4-4 form; the conversion rests on
leaf-level evidence that one far-red spectral shape explains most of
the variance across species.[^ug-v11][^opendap-dmr][^magney-2019]
Biases from the per-footprint instrument line shape and detector
linearity are removed by an offset correction in the manner of the
GOSAT reference-target method: the mean SIF over non-fluorescing
surfaces, identified since version 10 from a 0.2 degree table of the
2018 MODIS IGBP barren and snow classes and near-zero VPM GPP, is
computed over three days centred on the day, per footprint, and
subtracted from every value; the Offset group records the means,
medians and standard deviations of adjusted and unadjusted values on
227 signal-level bins, and the Science group keeps the unadjusted
values as SIF_Unadjusted_757nm and SIF_Unadjusted_771nm and their
relative forms.[^ug-v11][^frankenberg-2011b][^opendap-dmr] Version 11
changed the windows: the 757 nm window was moved away from the
detector edge, toward longer wavelengths, to reduce retrieval
failures, and both windows were made consistent between OCO-2 and
OCO-3, which the guide says gives slight differences from version 10
and better consistency between the two instruments.[^ug-v11][^ug-b10]

**Wrong-result mode.** A series that switches field between files or
between products takes a step that is the spectral slope, not the
vegetation: 757 nm against 771 nm differ by about a factor of 1.5,
740 nm against 757 nm by the fixed conversion, and a comparison with
another sensor's 740 nm value that uses the OCO-2 757 nm field
compares different points on the emission spectrum; among GOME-2
retrieval methods magnitudes differ by up to a factor of two,
largely attributed to retrieval window choice.[^ug-v11][^parazoo-2019] A series that joins
version 10 files to version 11 files, or reads the unadjusted or
relative fields beside the adjusted ones, carries the window change
or the daily background inside it; the unadjusted value differs from
the adjusted one by a per-footprint offset that varies from day to
day, so a footprint-by-footprint comparison of unadjusted values
sees the instrument as much as the surface.[^ug-v11] A difference
between the 757 and 771 nm values read as a spectral signal of the
canopy is mostly the fixed shape of the far-red emission, which is
stable beyond 740 nm.[^magney-2019]

**Correct approach.** One field, named by its wavelength and by
whether it is adjusted, unadjusted or relative, is carried through a
series, and the version (11r, 11.2r, or an earlier 10r) is part of
the name of the record; the 740 nm field is treated as a fixed
transform of the two retrievals, useful for comparison with sensors
that report at 740 nm and carrying no information the two retrievals
do not; and a comparison with another mission states both
wavelengths and the conversion or the retrieval windows on each
side.[^ug-v11][^parazoo-2019] The Offset group is the record of what
was subtracted on each day and footprint, so the size and variation
of the correction is read there rather than inferred from the
adjusted values.[^ug-v11][^opendap-dmr]

**Verification.** The guide's Table 4-4 carries the 740 nm formula
and the 1.5 ratio, section 2.4 the window change, and section 2.10
the offset method; the DAP4 metadata of any granule shows the Table
4-4 formula in the description attribute of SIF_740nm and the long
names Offset-Adjusted and Raw on the Science fields, and the
recomputation check below distinguishes the Table 4-4 form from the
section 2.11 form, whose 771 nm weight differs by a third; the
attribute was read on the on-premises server on 15 September 2026
and is confirmed on the Cloud OPeNDAP copy once that is read behind
Earthdata Login.[^ug-v11][^opendap-dmr]
The check a reader runs: on one granule, SIF_740nm recomputed from
the two Science fields by the Table 4-4 form matches the root field
to the least significant digit and the section 2.11 form does not, the median of SIF_757nm divided by SIF_771nm over
the good soundings of a vegetated day is near the guide's typical
1.5, and the difference between SIF_Unadjusted_757nm and SIF_757nm
is the day's background for that footprint and signal level, whose
statistics are the Offset group's.[^ug-v11]
The cross-mission magnitude statement is the harmonisation paper's,
verified on the registry.[^parazoo-2019] The dataset concept lists
this trap.[^dataset]

[^ug-v11]: Kurosu and others, 2025, OCO-2 and OCO-3 SIF Data User's Guide, Lite file version 11 and 11.2
[^ug-b10]: OCO-2 and OCO-3 SIF Data User's Guide for the build 10 Lite files, 2021
[^opendap-dmr]: DAP4 metadata of the OCO-2 Lite SIF granule of 2024-04-02, read 2026-09-15
[^parazoo-2019]: Parazoo and others, 2019, Journal of Geophysical Research Biogeosciences, doi:10.1029/2019JG005289
[^magney-2019]: Magney and others, 2019, Journal of Geophysical Research Biogeosciences, doi:10.1029/2019JG005029
[^frankenberg-2011b]: Frankenberg and others, 2011, Geophysical Research Letters, doi:10.1029/2011GL048738
[^dataset]: This bundle's OCO-2 and OCO-3 SIF Lite dataset concept
