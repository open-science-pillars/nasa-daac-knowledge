---
type: dataset-gotcha
spheres: [cryosphere]
title: "The firn air content correction is a spread between models, not a measured term: it sets the uncertainty of an altimetric mass rate and it changes sign inside the record"
description: "Converting an ice sheet volume change into a mass change subtracts the change in firn air content and multiplies the remainder by a density. Neither firn field this bundle reads ships a usable error: the Greenland product ships none and its own paper substitutes the difference between two firn models, and the Antarctic error field is not a firn air content error in the units a budget needs. The resulting term is large enough to set the formal error of the altimetric mass rate, and the anomaly changes sign inside the record, so the correction adds to a loss over some windows and cancels it over others. A mass rate quoted with only the height or volume error omits the term that dominates it, and a closure residual then reads as a disagreement between observing systems."
tags: [firn, firn-air-content, fac, gemb, gsfc-fdm, its-live, atl15, mass-balance, density, model-spread, uncertainty, greenland, antarctica, cryosphere]
generated: { by: knowledge-seeder/claude, at: 2026-09-19T05:30:00Z }
severity: high
dataset: ../datasets/firn-model-air-content.md
eval_case: firn-air-content-spread-dominates-the-altimetric-mass-rate
status: draft
stale_after: 2027-03-19
sources:
  - id: firn-concept
    resource: ../datasets/firn-model-air-content.md
    title: "Bundle dataset concept: the firn air content term as the two ITS_LIVE elevation change products distribute it, with its versions, domains, forcing and what its uncertainty rests on"
  - id: nilsson-2026-pdf
    resource: https://essd.copernicus.org/articles/18/1729/2026/essd-18-1729-2026.pdf
    title: "Nilsson and Gardner, 2026, Elevation change of the Greenland Ice Sheet and its peripheral glaciers 1992 to 2023, Earth System Science Data 18, 1729 to 1745, read in full 2026-09-19: firn air content errors are outside the study's scope and the difference between the two firn models is taken as the error"
  - id: nilsson-2026
    resource: https://doi.org/10.5194/essd-18-1729-2026
    title: "The registry record of the Greenland product's paper, verified on Crossref 2026-09-19"
  - id: gsfc-fdm
    resource: https://doi.org/10.5194/tc-16-3971-2022
    title: "Medley, Neumann, Zwally, Smith and Stevens, 2022, Simulations of firn processes over the Greenland and Antarctic ice sheets, The Cryosphere 16, 3971 to 4011, read in full 2026-09-19: firn air content defined as depth-integrated porosity, the seasonal volume changes it carries against those from surface mass fluxes, and the model's own perturbation uncertainty"
  - id: nsidc-0792-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/nsidc-0792-v001-userguide.pdf
    title: "NSIDC-0792 Version 1 user guide, read 2026-09-19: fac, fac_err and fac_mean in metres, and the GEMB run forced with 3-hourly ERA5"
  - id: data-root
    resource: ../references/retrieval/ice-sheet-balance-root/firn-stamp.json
    title: "The firn stamp of the committed ice sheet balance data root: the uncertainty basis for each domain, the Antarctic error field's statistics, and the committed firn.csv series read for the sign statements below"
  - id: computation
    resource: ../computations/ice-sheet-balance.md
    title: "Bundle attested computation: the ice sheet mass balance closure, whose receipted Greenland run states the altimetric rate's formal error and what sets it"
  - id: gotcha-height
    resource: ./atl15-height-change-is-not-mass-change.md
    title: "Bundle gotcha: a height change is not a mass change; this gotcha is about the uncertainty of the correction that conversion requires"
  - id: atl15
    resource: ../datasets/icesat2-atl15.md
    title: "Bundle dataset concept: ICESat-2 ATL15, whose error fields are surface-fit errors and carry no firn term"
---

# The firn air content correction is a spread between models

**Mechanism.** A mass change from altimetry is the measured volume
change less the change in firn air content, multiplied by a density of
ice; the firn air content is the depth-integrated porosity of the
column, in metres of air, and its change is height that carries no
mass.[^gsfc-fdm][^gotcha-height] The term is not a small correction.
Its authors report that seasonal volume changes associated with firn
air content are on average about 2.5 times larger over Antarctica and
1.5 times larger over Greenland than those associated with surface mass
fluxes, and that averaged over several years the ice and air volume
fluctuations inside the column are of comparable
magnitude.[^gsfc-fdm] What the products distribute, however, is a model
output without a usable error beside it. The Greenland elevation change
product ships no firn error field, and its own paper states that
estimating firn air content errors is an active area of research and
outside its scope, taking instead the difference in firn air content
change between GEMB version 1.3.0 and GSFC-FDM version 1.2.1 as the
measure of error, propagated as the root mean square error of the
volume difference between the two models over the interval and added in
quadrature to the volume change error before the ice density is
applied.[^nilsson-2026-pdf][^nilsson-2026][^firn-concept] The Antarctic
ice shelf product does ship fac_err, but this bundle's firn stamp
records that it does not read as a firn air content error a budget can
use, carrying tens of metres at the median, a fill of 9999 where it has
none and a units attribute of metres of ice per year, so the loader
substitutes a noise floor and records the field's
statistics.[^data-root][^nsidc-0792-user-guide] The consequence is
arithmetic: a term with no measurement error enters the mass rate with
a model spread in its place, and in this bundle's receipted Greenland
run over 2003 through 2016 it is that floored firn spread that sets the
altimetric rate's formal error of 44.83 gigatonnes per
year.[^computation][^data-root] The uncertainty on the firn term is
wide enough to cross zero: the reference run the repository's check
routine reruns on the committed data root reports the Greenland firn
rate over 2003 through 2016 as minus 55.359 cubic kilometres of air per
year with a 95 percent interval of minus 118.062 to plus 7.345, so the
sign of the correction over that window is not established by the
interval the run itself carries.[^computation][^data-root] The term
also changes sign inside the record. In the committed Greenland series the ice sheet's area-weighted
firn air content anomaly runs from 0.35936 metres of air at 1992-01 to
minus 0.211243 at 2023-12, with a maximum of 0.5683 at 1998-04 and a
minimum of minus 0.281387 at 2023-09, so the correction subtracts from
a measured lowering over some windows and adds to it over
others.[^data-root]

**Wrong-result mode.** A volume change is converted to mass, the firn
model is named in a sentence, and the number is then quoted with the
height or volume error alone, because that is the error the altimetry
product ships and the firn field ships none; the stated interval then
omits the term that dominates it. Where the firn spread is carried but
treated as a formal error it is combined as though the two models were
two measurements of the column, which they are not: they differ in
forcing and in physics, and the product's paper reports large spatial
differences in their firn air content rates and a temporal divergence
around 2005 as melt becomes more prevalent, so the spread is a
disagreement whose size says nothing about where the truth lies inside
it.[^nilsson-2026-pdf] Because the anomaly changes sign, a correction
calibrated or sanity-checked on one window carries the wrong sign on
another, and folding the firn term into an effective column density,
which is the shortcut the absence of an error field invites, fixes its
sign for the whole record.[^data-root] Downstream, the failure is read
as physics rather than bookkeeping: a closure between gravimetry and
firn-corrected altimetry whose residual moves with the firn term reads
as a disagreement between two observing systems, and this bundle's own
receipted run shows the shape of it, where over one window the firn
correction cancels most of the surface lowering and the altimetric loss
comes out far smaller than the mascon loss.[^computation]

**Correct approach.** A mass rate derived from a height or volume
change names the firn model and its version, the domain and sampling of
the run that supplied the term, and the forcing where the product
states one, and carries the firn term's uncertainty as a term of its
own beside the propagated height error rather than inside
it.[^firn-concept][^gotcha-height] Where that uncertainty is a spread
between two model runs, it is voiced as a spread between named models
and not as a measurement error, and where only one model is available
the number carries a floor and says that it is a floor rather than a
spread.[^nilsson-2026-pdf][^data-root] The sign and size of the firn
contribution over the specific window are stated beside the mass rate,
because the anomaly changes sign inside the record and a reader cannot
recover it from the total.[^data-root] A comparison of an altimetric
mass rate against a gravimetric one, or against a published assessment,
states which firn model stands behind the altimetric side, since that
is the term the two do not share.[^computation][^atl15]

**Verification.** The Greenland product's paper was fetched from the
publisher and read in full on 2026-09-19, which is where the statement
that firn errors are outside its scope, the two model versions, the
error construction and the note on the models' divergence come from;
its record was verified against the Crossref registry the same
day.[^nilsson-2026-pdf][^nilsson-2026] The GSFC-FDM description was
fetched and read in full on 2026-09-19 for the definition of firn air
content and the ratio of seasonal firn volume changes to surface mass
flux changes.[^gsfc-fdm] The NSIDC-0792 user guide was read on
2026-09-19 for the Antarctic firn variables and their
units.[^nsidc-0792-user-guide] The sign statements were read on
2026-09-19 from the committed firn.csv of this bundle's stamped data
root, taking the greenland rows whose domain is ice_sheet: 384 monthly
epochs from 1992-01 to 2023-12, first, last, maximum and minimum as
quoted, and the two-model spread exceeding the magnitude of the anomaly
itself at 26 of those epochs.[^data-root] The formal error the firn
spread sets is the one the closure's reference run records, and the
firn rate and its interval quoted above are the ones that run prints
when the repository's check routine reruns it against the committed
data root, which it did on 2026-09-19.[^computation][^data-root]

[^firn-concept]: This bundle's firn air content dataset concept
[^nilsson-2026-pdf]: Nilsson and Gardner, 2026, read in full 2026-09-19
[^nilsson-2026]: Nilsson and Gardner, 2026, doi:10.5194/essd-18-1729-2026
[^gsfc-fdm]: Medley and others, 2022, doi:10.5194/tc-16-3971-2022
[^nsidc-0792-user-guide]: NSIDC-0792 Version 1 user guide, read 2026-09-19
[^data-root]: The firn stamp and firn.csv of this bundle's committed data root
[^computation]: This bundle's attested ice sheet mass balance closure
[^gotcha-height]: This bundle's gotcha that height change is not mass change
[^atl15]: This bundle's ATL15 dataset concept
