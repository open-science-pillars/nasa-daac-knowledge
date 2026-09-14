---
type: dataset-gotcha
spheres: [atmosphere, hydrosphere]
title: "PRECTOTCORR is the observation-corrected precipitation the land surface saw and PRECTOT is the atmosphere's own: a water budget that mixes them carries the correction as a residual"
description: "MERRA-2 forces its land surface, outside the high latitudes, with precipitation corrected toward gauge and satellite products (PRECTOTCORR), while the atmospheric water budget is closed by the model's own precipitation (PRECTOT); the two differ by the whole correction, which is largest in the tropics, blends to zero between 42.5 and 62.5 degrees of latitude and is absent poleward of that. A land budget closed with PRECTOT, an atmospheric budget closed with PRECTOTCORR, or a land-plus-atmosphere budget with either, returns a residual that is the correction, not a storage change, and nothing in the files raises an error because both fields sit side by side in the same collection with the same units."
tags: [merra-2, merra2, precipitation, prectotcorr, prectot, water-budget, land-surface, cpcu, cmap, gesdisc]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:30:00Z }
severity: high
dataset: ../datasets/merra-2.md
eval_case: merra2-prectotcorr-versus-prectot
status: draft
stale_after: 2027-03-14
sources:
  - id: filespec
    resource: https://gmao.gsfc.nasa.gov/media/publications/zbly36ziNFDFbmYmvhQeVqPhUo/Bosilovich785.pdf
    title: "Bosilovich, Lucchesi and Suarez, 2016, MERRA-2: File Specification, GMAO Office Note No. 9 (version 1.1), read 2026-09-14: the introduction's paragraph on the observation-based precipitation forcing and its mass-balance warning, the FLX variable table with PRECTOT and PRECTOTCORR, the LFO table with the corrected components PRECCUCORR, PRECLSCORR and PRECSNOCORR and no total, and the land water budget equation in the budget section"
  - id: reichle-liu-2014
    resource: https://gmao.gsfc.nasa.gov/pubs/docs/Reichle734.pdf
    title: "Reichle and Liu, 2014, Observation-Corrected Precipitation Estimates in GEOS-5, NASA Technical Report Series on Global Modeling and Data Assimilation volume 35, read 2026-09-14: the disaggregation method, the latitude tapering (option T) and Africa (option X) rules, the MERRA-2 rows of Table 3 and the paragraph on use in the coupled system"
  - id: reichle-2017
    resource: https://doi.org/10.1175/JCLI-D-16-0570.1
    title: "Reichle, Liu, Koster, Draper, Mahanama and Partyka, 2017, Land Surface Precipitation in MERRA-2, Journal of Climate 30, 1643 to 1664 (record and abstract read on the Crossref registry 2026-09-14: the corrected precipitation against GPCP and TRMM, the self-consistency of the near-surface meteorology; the journal page sits behind a bot check)"
  - id: reichle-2017b
    resource: https://doi.org/10.1175/JCLI-D-16-0720.1
    title: "Reichle, Draper, Liu, Girotto, Mahanama, Koster and De Lannoy, 2017, Assessment of MERRA-2 Land Surface Hydrology Estimates, Journal of Climate 30, 2937 to 2960 (record and abstract read on the Crossref registry 2026-09-14: the GRACE comparison that reflects known errors in the correcting observations; the journal page sits behind a bot check)"
  - id: bosilovich-2015
    resource: https://gmao.gsfc.nasa.gov/pubs/docs/Bosilovich803.pdf
    title: "Bosilovich and others, 2015, MERRA-2: Initial Evaluation of the Climate, NASA TM-2015-104606 volume 43, read 2026-09-14: the introduction's description of the correction and the land surface section on where the correction matches the observations and where the adjustments are largest"
  - id: bosilovich-2017
    resource: https://doi.org/10.1175/JCLI-D-16-0338.1
    title: "Bosilovich, Robertson, Takacs, Molod and Mocko, 2017, Atmospheric Water Balance and Variability in the MERRA-2 Reanalysis, Journal of Climate 30, 1177 to 1196 (record and abstract read on the Crossref registry 2026-09-14: the atmospheric water balance with the analysis increment; the journal page sits behind a bot check)"
  - id: gesdisc-m2t1nxflx
    resource: https://disc.gsfc.nasa.gov/datasets/M2T1NXFLX_5.12.4/summary
    title: "GES DISC collection page for M2T1NXFLX 5.12.4 (fetched 2026-09-14, text read from its CMR record: the collection lists total precipitation and bias corrected total precipitation among its surface flux diagnostics)"
  - id: gmao-faq
    resource: https://gmao.gsfc.nasa.gov/gmao-products/merra-2/faq_merra-2/
    title: "GMAO MERRA-2 FAQ, read 2026-09-14: the LND collection holds land-only values not weighted by land fraction, the other collections grid-box averages over all tiles"
  - id: dataset
    resource: ../datasets/merra-2.md
    title: "This bundle's MERRA-2 dataset concept, which names the correction in its structure and lists this trap among the known issues"
---

# PRECTOTCORR versus PRECTOT

**Mechanism.** MERRA-2 produces two total precipitation fields in the
surface flux collections (M2T1NXFLX hourly, M2TMNXFLX monthly); the
LFO land forcing collections carry no total but the bias-corrected
components, convective PRECCUCORR, large-scale PRECLSCORR and
snowfall PRECSNOCORR, per their table in the file
specification.[^filespec] PRECTOT is the precipitation from
the atmospheric model physics, the field that closes the atmospheric
water budget together with evaporation, the transport divergence and
the analysis increment. PRECTOTCORR is the observation-corrected
precipitation: publicly available gauge and satellite products,
the CPCU daily 0.5 degree gauge analysis over land outside Africa
and the CMAP 2.5 degree pentad product over Africa and the oceans,
disaggregated to the model's hourly, 0.5 degree scale with the
model's own background precipitation, so that the corrected field
matches the observations at the observation product's scale and the
model at finer scales.[^filespec][^reichle-liu-2014][^bosilovich-2015]
The correction is tapered with latitude: full corrections equatorward
of 42.5 degrees, a linear blend between 42.5 and 62.5 degrees, and
pure model precipitation poleward of 62.5 degrees, where PRECTOTCORR
equals PRECTOT by construction.[^reichle-liu-2014][^filespec]
Inside the coupled system the corrected field forces the land surface
and modulates aerosol wet removal; the atmospheric water and energy
prognostic variables associated with precipitation are not directly
modified, only indirectly through feedback from the land, so the
atmosphere keeps its own precipitation while the land sees the
corrected one.[^reichle-liu-2014][^bosilovich-2015] The file
specification says it in one sentence: care must be taken in mass
balance studies, because the difference between the observation-based
and model-generated precipitation affects the water budget when land
and atmosphere budgets are combined.[^filespec] The land water budget
the specification writes, WCHANGE equals PRECTOTLAND minus EVLAND
minus RUNOFF minus BASEFLOW plus SPWATR, uses the land collection's
precipitation, which is the corrected forcing per unit land area, not
weighted by land fraction and undefined where the land fraction is
zero.[^filespec][^gmao-faq]

**Wrong-result mode.** Both fields sit in the same file with the same
units (kg per square metre per second) and the same dimensions, so a
budget takes whichever one the analyst reached for and runs. A land
water budget closed with PRECTOT reports the correction, positive or
negative by region and largest in the tropics and over South America,
as a storage change or a runoff error; an atmospheric budget closed
with PRECTOTCORR reports minus the correction as a spurious source
against the analysis increment; a combined land-atmosphere budget
with either field alone does not close by the correction's amount,
and the residual looks like a physical term.[^filespec][^bosilovich-2015][^bosilovich-2017]
A comparison of MERRA-2 precipitation against a gauge product is
circular where PRECTOTCORR is the field compared, because CPCU is
built from gauges; the corrected field's skill against GPCP, and its
diurnal cycle with better amplitude but less realistic phasing than
the model's, are the documented differences, and a study that treats
PRECTOTCORR as an independent reanalysis estimate of precipitation
mis-states what it is.[^reichle-2017] A regional series that spans
the 42.5 to 62.5 degree band is a blend of two products whose weights
change with latitude, and poleward of 62.5 degrees the "corrected"
field carries the model's high-latitude precipitation, which the
evaluation finds high-biased.[^reichle-liu-2014][^bosilovich-2015]
Land hydrology that inherits the correction also inherits its errors:
the GRACE terrestrial water storage comparison reflects known errors
in the observations used to correct the precipitation.[^reichle-2017b]

**Correct approach.** An atmospheric water budget uses PRECTOT with
the increment terms of the INT collections; a land water budget uses
PRECTOTLAND from the LND collection (or PRECTOTCORR from FLX for the
grid-box view) with the land fluxes, per unit land area; a combined
budget states that the two precipitation fields differ and carries
the difference PRECTOTCORR minus PRECTOT as its own term.[^filespec][^gmao-faq]
Any precipitation statement from MERRA-2 names the field, and where
it is PRECTOTCORR names the observation product behind it (CPCU or
CMAP by region) and the latitude band, so that the reader knows
whether they are looking at the model or at a gauge analysis
disaggregated by the model.[^reichle-liu-2014] Validation of
MERRA-2 precipitation against gauges or IMERG compares PRECTOT, and
a validation of PRECTOTCORR is a validation of the correcting
product at the observation scale plus the model's disaggregation
below it.[^reichle-2017]

**Verification.** The two variables and their descriptions are in the
FLX variable table of the file specification, and the collection
abstract names both.[^filespec][^gesdisc-m2t1nxflx] The tapering
rule gives a check any reader can run on one day of M2T1NXFLX:
PRECTOTCORR and PRECTOT differ over tropical land and are identical
at every point poleward of 62.5 degrees, with the difference shrinking
across the band between.[^reichle-liu-2014] The correction method,
its data sources and its use in the coupled system are the 2014
memorandum and the 2017 paper; the paper's registry record was
verified on Crossref on 2026-09-14 (title, authors, journal, year) and
its abstract read there, the journal page itself sitting behind a bot
check.[^reichle-liu-2014][^reichle-2017] The dataset concept names
the correction and lists this trap.[^dataset]

[^filespec]: Bosilovich, Lucchesi and Suarez, 2016, MERRA-2: File Specification, GMAO Office Note 9, version 1.1
[^reichle-liu-2014]: Reichle and Liu, 2014, Observation-Corrected Precipitation Estimates in GEOS-5, NASA TM-2014-104606 volume 35
[^reichle-2017]: Reichle and others, 2017, Journal of Climate, doi:10.1175/JCLI-D-16-0570.1
[^reichle-2017b]: Reichle and others, 2017, Journal of Climate, doi:10.1175/JCLI-D-16-0720.1
[^bosilovich-2015]: Bosilovich and others, 2015, MERRA-2: Initial Evaluation of the Climate, NASA TM-2015-104606 volume 43
[^bosilovich-2017]: Bosilovich and others, 2017, Journal of Climate, doi:10.1175/JCLI-D-16-0338.1
[^gesdisc-m2t1nxflx]: GES DISC collection page and CMR record, M2T1NXFLX 5.12.4
[^gmao-faq]: GMAO MERRA-2 FAQ
[^dataset]: This bundle's MERRA-2 dataset concept
