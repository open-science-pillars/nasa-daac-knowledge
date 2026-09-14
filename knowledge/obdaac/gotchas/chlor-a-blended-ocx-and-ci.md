---
type: dataset-gotcha
spheres: [biosphere, hydrosphere]
title: "The standard chlor_a is two algorithms blended between 0.25 and 0.35 mg per cubic metre: a threshold, histogram, gradient or front inside that range measures the switch between the color index and the band ratio, and the transition itself moved between reprocessings"
description: "NASA's standard chlorophyll-a for every ocean color sensor is the OCI blend: the three-band color index (CI) of Hu, Lee and Franz for retrievals below 0.25 mg per cubic metre, the OCx blue-to-green band-ratio polynomial above 0.35, and a linear weighting of the two in between, with coefficients retuned in 2019 and adopted in the R2022 reprocessing that also moved the transition from 0.15 to 0.2 up to 0.25 to 0.35. Inside the transition a pixel's value is a weighted mix of two empirical fits to two different reflectance quantities, and where a field crosses it the blend, not the water, shapes the histogram, the gradient and the position of any contour or front placed there. The two components respond differently to atmospheric-correction error and to optically complex water, and the collection descriptions state that coastal and inland retrievals may carry higher uncertainty, with no per-pixel uncertainty in the mapped files to say by how much."
tags: [chlorophyll, chlor_a, oci-algorithm, ocx, oc3m, oc4, color-index, band-ratio, transition, threshold, oligotrophic, coastal, turbid, modis, aqua, pace, oci, obdaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:30:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-14T12:17:15Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/147 }
severity: high
dataset: ../datasets/modis-aqua-l3-chlorophyll.md
eval_case: chlor-a-blended-ocx-and-ci
status: draft
stale_after: 2027-03-14
sources:
  - id: atbd
    resource: https://oceancolor.gsfc.nasa.gov/files/atbd/atbd-obdaac-chlorophyll-a.pdf
    title: "Chlorophyll a, Algorithm Theoretical Basis Document version 1.1, 6 November 2023, Werdell, O'Reilly, Hu, Feng, Lee, Franz, Bailey, Proctor and Wang, DOI 10.5067/JCQB8QALDOYD, 18 pages, read in full 2026-09-14 (the OB.DAAC URL redirects to the same file on the OB.DAAC data host): the scientific theory (section 3.1), the mathematical theory with the CI equation, the OCx polynomial, the sensor coefficient table and the blending equation with its edges at 0.25 and 0.35 (section 3.2), the previous-versions paragraph with the 0.15 to 0.2 transition used since R2014, the usage constraint on local validation (section 5) and the validation uncertainties (section 6)"
  - id: hu-2012
    resource: https://doi.org/10.1029/2011JC007395
    title: "Hu, Lee and Franz, 2012, Chlorophyll a algorithms for oligotrophic oceans, a novel approach based on three-band reflectance difference, Journal of Geophysical Research: Oceans 117, C01011 (registry record verified on Crossref and abstract read there 2026-09-14; the publisher page returned 403 to this environment and the article was not read): the color index proposed for chlorophyll at or below 0.25 mg per cubic metre, about 78 percent of the ocean area, its tighter relation to chlorophyll than band ratios in low-chlorophyll water, its tolerance to changes in the chlorophyll-specific backscattering coefficient, and its much lower sensitivity than band ratios to instrument noise and imperfect atmospheric correction"
  - id: hu-2019
    resource: https://doi.org/10.1029/2019JC014941
    title: "Hu, Feng, Lee, Franz, Bailey, Werdell and Proctor, 2019, Improving satellite global chlorophyll a data products through algorithm refinement and data recovery, Journal of Geophysical Research: Oceans 124, 1524 to 1543 (registry record verified on Crossref and abstract read there 2026-09-14; the publisher page returned 403 and the article was not read): the OCI2 revision, lower estimates than OCI1 below 0.05 mg per cubic metre, a smoother transition between 0.25 and 0.40, the cross-sensor difference in monthly oligotrophic chlorophyll reduced from about 10 percent with OCx to 1 to 2 percent, and the straylight mask relaxed from 7 by 5 to 3 by 3 pixels with a 39 percent average increase in data quantity"
  - id: oreilly-werdell-2019
    resource: https://doi.org/10.1016/j.rse.2019.04.021
    title: "O'Reilly and Werdell, 2019, Chlorophyll algorithms for ocean color sensors, OC4, OC5 and OC6, Remote Sensing of Environment 229, 32 to 47 (registry record verified on Crossref 2026-09-14; the record carries no abstract, the publisher page was not reachable and the article was not read): the OCx coefficients the ATBD adopts"
  - id: cmr-modis
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C3380709133-OB_CLOUD.umm_json
    title: "CMR collection record for MODISA_L3m_CHL version 2022.0 (read 2026-09-14): the abstract's statement that retrievals in optically complex coastal and inland waters may carry higher uncertainty, with a pointer to the OCx and OCI documentation; the PACE_OCI_L3M_BGC record (C4184125847-OB_CLOUD) carries the same sentence"
  - id: modis-file
    resource: https://oceandata.sci.gsfc.nasa.gov/opendap/MODISA/L3SMI/2024/0601/AQUA_MODIS.20240601_20240630.L3m.MO.CHL.chlor_a.4km.nc.das
    title: "The attribute listing (OPeNDAP .das, metadata only) of the June 2024 MODIS-Aqua monthly 4 km file, read 2026-09-14: chlor_a's long name Chlorophyll Concentration, OCI Algorithm, its reference attribute citing Hu and others 2019 and O'Reilly and Werdell 2019, processing_version R2022.0.3, the l2_flag_names list including CHLWARN, CHLFAIL and COCCOLITH, and the absence of any uncertainty, count or flag variable; the June 2024 PACE OCI monthly 4 km BGC file's listing read the same way shows the same long name, a reference attribute citing Hu, Lee and Franz 2012, and no uncertainty variable"
  - id: dataset
    resource: ../datasets/modis-aqua-l3-chlorophyll.md
    title: "This bundle's MODIS-Aqua Level 3 chlorophyll-a dataset concept: the collection, the file structure and the Uncertainty section; the PACE OCI dataset concept beside it carries the same algorithm with the OC4 coefficients"
---

# The standard chlor_a is two algorithms blended between 0.25 and 0.35 mg per cubic metre

**Mechanism.** The chlor_a variable in the OB.DAAC Level 3 files of
every NASA ocean color sensor is the output of one procedure with two
empirical components. The color index is the difference between the
remote sensing reflectance in the green band and a reference drawn
linearly between the blue and red bands, converted to chlorophyll with
two coefficients; the OCx band ratio is a fourth-order polynomial in
the log of the ratio of the greatest of two or three blue reflectances
to the green reflectance, with sensor-specific coefficients (OC3M for
MODIS, OC4 for PACE OCI).[^atbd] Both are computed for every pixel;
below 0.25 mg per cubic metre the CI value is kept, above 0.35 the OCx
value, and between the two edges the product is a linear weighting of
the two by the CI value's position in the interval.[^atbd] The CI
component was designed for low-chlorophyll water, at or below 0.25 mg
per cubic metre, which its authors put at about 78 percent of the
ocean area; in situ data show it more tightly related to chlorophyll
there than band ratios, and simulations show it more tolerant of
changes in the chlorophyll-specific backscattering coefficient and
much less sensitive to instrument noise and imperfect atmospheric
correction, including sun glint and whitecap
corrections.[^hu-2012] The 2019 revision retuned both components and
the transition on a merged HPLC and fluorometric data set, giving
lower values than the original OCI below 0.05 mg per cubic metre and a
smoother transition between 0.25 and 0.40 (the edges the ATBD gives
for the implementation are 0.25 and 0.35), and reported the mean
cross-sensor difference in monthly oligotrophic chlorophyll falling
from about 10 percent with OCx alone to 1 to 2 percent; the R2022
reprocessing adopted it, and the ATBD states that from R2014 until
then the blend used a transition of 0.15 to 0.2 with the 2012
parameterization.[^hu-2019][^atbd] The mapped files record
the procedure only as the long name "Chlorophyll Concentration, OCI
Algorithm" and a reference attribute (the MODIS-Aqua file cites the
2019 papers, the PACE OCI file the 2012 paper); nothing in the file
marks which component or which mix produced a given
pixel.[^modis-file] The ATBD states that the empirical forms partly
compensate for reflectance input errors because those errors are
spectrally related, that validation shows good overall performance
with regional differences that can be large, and that validation for
a local study area may be necessary; the collection descriptions
state that retrievals in optically complex coastal and inland waters
may carry higher uncertainty, and the mapped files carry no per-pixel
uncertainty to quantify it.[^atbd][^cmr-modis][^modis-file]

**Wrong-result mode.** A threshold placed inside the transition (an
oligotrophic mask at 0.3 mg per cubic metre, a bloom criterion at
0.3) classifies pixels by a value that is a weighted mix of two fits,
so the area above or below it, and any trend in that area, contain the
algorithm's transition behavior beside the ocean's. A histogram of
chlor_a over a region that straddles the transition has a shape
between 0.25 and 0.35 that reflects the blending rather than the
distribution of pigment; a front, contour or gradient located there is
partly the place where the product switches from one fit to the other.
The same analysis on a pre-R2022 series (transition 0.15 to 0.2, the
2012 coefficients) and on the R2022 series (0.25 to 0.35, the 2019
coefficients) places the feature in different
ranges.[^atbd][^hu-2019] Because the two components respond
differently to atmospheric-correction error and noise, the noise
level of the field also changes across the transition: the CI side is
smoother by design, so a variance, anomaly or eddy-detection statistic
compared between oligotrophic and mesotrophic water compares two
algorithms' noise as well as two regimes.[^hu-2012] In coastal, shelf
and inland water the band-ratio component reads the whole reflectance
spectrum as chlorophyll, and the product's own documentation says only
that such retrievals may carry higher uncertainty and that local
validation may be necessary; a coastal chlorophyll series or a
river-plume map from the standard product is therefore an unvalidated
quantity whose error is not in the file.[^atbd][^cmr-modis]

**Correct approach.** A classification, histogram or feature
analysis on the standard chlor_a is defined with its thresholds
outside the transition (below 0.25 or above 0.35 for R2022 and PACE
version 3.2), or, when a threshold inside it is the scientific
requirement, with the sensitivity of the result to the threshold
stated by repeating the analysis at the two edges and reporting the
spread; either way the analysis names the reprocessing whose
transition applies, since the edges are properties of a
reprocessing.[^atbd][^hu-2019] A statistic that compares low- and
high-chlorophyll regimes states that the two are retrieved by
different components with different noise
characteristics.[^hu-2012] A coastal or inland analysis carries the
collection's caveat as its error statement and, where a local
validation exists, cites it; where none exists, the result is reported
as the standard product's value with the caveat, not as a validated
chlorophyll concentration.[^cmr-modis][^atbd] What the standard
chlor_a therefore is: a near-surface pigment concentration from one
blended empirical procedure, continuous across the ocean but built
from two fits whose seam lies between 0.25 and 0.35 mg per cubic
metre, with an accuracy goal of 35 percent in the open ocean and no
per-pixel error in the mapped file.[^dataset][^atbd]

**Verification.** The ATBD's algorithm section is the producer's own
statement of the two components, the blending equation, the edges at
0.25 and 0.35 and the earlier 0.15 to 0.2 transition, read in full on
2026-09-14; the coefficient table there names OC3M for MODIS and OC4
for PACE OCI.[^atbd] The two Hu papers' registry records were
verified against Crossref the same day (title, authors, journal, year,
volume) and their abstracts read there: the 2012 abstract states the
range, the ocean fraction and the tolerances of the color index, and
the 2019 abstract states the retuning, the smoother 0.25 to 0.40
transition and the cross-sensor figures; the publisher pages returned
403 and the articles were not read.[^hu-2012][^hu-2019] The
O'Reilly and Werdell record was verified on Crossref the same day and
carries no abstract.[^oreilly-werdell-2019] The two collection
records' caveat sentence and the two files' attribute listings (long
name, reference attribute, flag list, and the absence of an
uncertainty variable) were read the same day.[^cmr-modis][^modis-file]

[^atbd]: Chlorophyll a ATBD version 1.1, OB.DAAC, 6 November 2023
[^hu-2012]: Hu, Lee and Franz, 2012, Journal of Geophysical Research: Oceans, doi:10.1029/2011JC007395
[^hu-2019]: Hu and others, 2019, Journal of Geophysical Research: Oceans, doi:10.1029/2019JC014941
[^oreilly-werdell-2019]: O'Reilly and Werdell, 2019, Remote Sensing of Environment, doi:10.1016/j.rse.2019.04.021
[^cmr-modis]: CMR collection records, C3380709133-OB_CLOUD and C4184125847-OB_CLOUD
[^modis-file]: Attribute listings of the June 2024 MODIS-Aqua and PACE OCI monthly 4 km files, read through OPeNDAP on 2026-09-14
[^dataset]: This bundle's MODIS-Aqua Level 3 chlorophyll-a dataset concept
