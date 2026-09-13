---
type: dataset-gotcha
spheres: [hydrosphere]
title: "OSCAR is a diagnosed geostrophic plus Ekman current, not a measured total current: tides, inertial motion and the rest of the ageostrophic flow are absent by construction, and the equatorial band is the model's own solution"
description: "OSCAR velocities are an analytical solution of a quasi-steady, linear surface-layer momentum balance driven by altimetric height gradients, reanalysis wind stress and SST gradients, averaged over the top 30 m. Anything that lives in the local acceleration or the nonlinear terms, tides, inertial oscillations, submesoscale and other ageostrophic flow beyond the wind-driven term, is not in the product, and the equator is handled by a separate equatorial solution within five degrees. A comparison against drifters, moorings or ADCPs that treats OSCAR as the total current attributes the missing physics to product error or to the ocean, and the L4 grid gives no hint of it."
tags: [oscar, surface-currents, geostrophic, ekman, thermal-wind, tides, inertial, ageostrophic, equator, drifters, validation]
generated: { by: knowledge-seeder/claude, at: 2026-09-13T21:00:00Z }
severity: high
dataset: ../datasets/oscar-v2.md
eval_case: oscar-is-geostrophic-plus-ekman
status: draft
stale_after: 2027-03-13
sources:
  - id: guide
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/oscar/open/L4/oscar_v2.0/docs/oscarv2guide.pdf
    title: "OSCAR v2.0 User's Handbook, Dohan, October 2021 (read in full 2026-09-13): the model outline (quasi-steady linear flow, wind-dependent eddy viscosity, Stommel boundary condition, 30 m average), the known problems (no local acceleration or nonlinearity, geostrophy invalid at the equator, inaccurate within 100 km of the coast, weakest meridional component near the equator) and the version 2 equatorial solution within five degrees"
  - id: podaac-final
    resource: https://podaac.jpl.nasa.gov/dataset/OSCAR_L4_OC_FINAL_V2.0
    title: "PO.DAAC collection page, OSCAR_L4_OC_FINAL_V2.0: the abstract's statement of the inputs and the model, and the variable list (u, v, ug, vg) (read 2026-09-13)"
  - id: bonjean-2002
    resource: https://doi.org/10.1175/1520-0485(2002)032<2938:DMAAOT>2.0.CO;2
    title: "Bonjean and Lagerloef, 2002, Diagnostic model and analysis of the surface currents in the tropical Pacific Ocean, Journal of Physical Oceanography 32, 2938 to 2954: the diagnostic model the handbook builds on (registry record verified; the journal page was not read)"
  - id: lagerloef-1999
    resource: https://doi.org/10.1029/1999JC900197
    title: "Lagerloef, Mitchum, Lukas and Niiler, 1999, Tropical Pacific near-surface currents estimated from altimeter, wind, and drifter data, Journal of Geophysical Research: Oceans 104: steady geostrophic and Ekman dynamics calibrated by 15 m drogued drifters, with geostrophy passing from a beta-plane form at the equator to an f-plane form at two to three degrees (abstract read on the registry record)"
  - id: dohan-2017
    resource: https://doi.org/10.1002/2017JC012961
    title: "Dohan, 2017, Ocean surface currents from satellite data, Journal of Geophysical Research: Oceans: the project's own account that OSCAR calculates global currents from satellite observations with simplified physics (abstract read on the registry record)"
  - id: dataset
    resource: ../datasets/oscar-v2.md
    title: "This bundle's OSCAR dataset concept: the file layout, the 30 m average and the absence of an uncertainty field"
---

# OSCAR is a diagnosed geostrophic plus Ekman current

**Mechanism.** The OSCAR velocity is an analytical solution of a
simplified momentum equation for an upper-ocean turbulent mixed
layer: quasi-steady, linear, with turbulent mixing parameterized by
an eddy viscosity that is constant in depth and depends on the wind,
with a Stommel boundary condition (shear going to zero at depth), a
layer depth H of 125 m, and the current reported as the average of the
solution over the top 30 m.[^guide] The total velocity has three
terms: a geostrophic term from the gradient of the gridded absolute
dynamic topography, a wind-driven term in which wind stress sets the
shear through the eddy viscosity, and a thermal-wind contribution to
the vertical shear from horizontal SST gradients.[^guide][^podaac-final]
The files carry the total (`u`, `v`) and the geostrophic part alone
(`ug`, `vg`), so the difference between them is the model's wind-driven
plus thermal-wind term, not an observed ageostrophic
residual.[^guide][^dataset] The handbook states what the formulation
leaves out: local acceleration and nonlinearities are not represented,
the geostrophic assumption is not valid at the equator, and the
currents are inaccurate within about 100 km of the coast.[^guide]
Tidal currents and inertial oscillations are local-acceleration
phenomena, and any ageostrophic flow beyond the wind-driven Ekman-like
term (submesoscale fronts, nonlinear eddy motion, wave-driven flow) has
no term in the balance, so none of them is in the product; the
gridded inputs and the gradient calculation smooth the fields further,
and velocities above 3 m/s are removed.[^guide] The equatorial band
has its own treatment: the original model passes geostrophy from a
beta-plane form at the equator to an f-plane form at two to three
degrees, with a Gaussian transition of about the Rossby radius, and
version 2 uses an equatorial solution within five degrees of the
equator with the turbulence parameterization blended from equatorial
empirical values to global ones; the handbook names the meridional
component in strong zonal flows near the equator as one of the two
places the product performs worst.[^lagerloef-1999][^guide] The model
line runs from the 1999 tropical Pacific estimate through the 2002
diagnostic model to the global product, and the project describes
itself as calculating currents from satellite observations with
simplified physics.[^lagerloef-1999][^bonjean-2002][^dohan-2017]

**Wrong-result mode.** A comparison of OSCAR against an hourly ADCP or
current-meter record, or against drifter velocities, that treats OSCAR
as the total current measures the sum of the omitted physics and the
product's error, and attributes it to one or the other: the tidal and
inertial variance of the in situ record appears as OSCAR error, and a
"good agreement" after monthly averaging hides that the two quantities
never contained the same terms. A drifter drogued at 15 m samples one
depth and every scale of motion, while OSCAR is a 30 m layer average
of a steady linear solution, so their difference is not an error bar
on either.[^lagerloef-1999][^guide] Subtracting `ug` from `u` and
calling the remainder "the ageostrophic current" or "the Ekman
current" reports the model's own wind-driven term as if it had been
observed. Within five degrees of the equator, a meridional velocity or
a divergence computed from `v` rests on the component the product
documents as its weakest, and the geostrophic fields there are the
equatorial solution, not the midlatitude balance. Within 100 km of a
coast the handbook's own statement is that the currents are
inaccurate. None of this raises an error: the grid is complete and the
values plausible everywhere.[^guide]

**Correct approach.** A result from OSCAR names what OSCAR is: a
diagnosed geostrophic plus Ekman plus thermal-wind current averaged
over the top 30 m, with no tides, no inertial motion and no other
ageostrophic flow, inaccurate within about 100 km of coasts, and on an
equatorial solution within five degrees of the equator.[^guide] A
comparison against in situ velocity says which part it compares: the
in situ record low-pass filtered to subinertial, detided time scales
for the total, or the geostrophic fields `ug` and `vg` against a
geostrophic estimate from the same altimetry, with the 15 m drogue
depth or instrument depth stated beside the product's 30 m
average.[^guide][^lagerloef-1999] A question about tides, inertial
oscillations, submesoscale flow or the near-coastal circulation is
outside what the product contains, and a question in the equatorial
band carries the product's own statement about the meridional
component.[^guide] The absence of an uncertainty field is stated with
any number quoted from the product.[^dataset]

**Verification.** The handbook's model outline and known-problems
sections are the product's own statement of the formulation and its
omissions, and its differences section states the version 2
equatorial solution; both were read in full on 2026-09-13.[^guide] The
collection abstract repeats the three-term model and the 30 m
average.[^podaac-final] The two model papers' records were verified
against the Crossref registry the same day (title, authors, journal,
year); the 1999 abstract, read there, states the beta-plane to f-plane
transition and the drifter calibration, and the 2017 abstract states
the simplified-physics formulation; the 2002 paper's abstract is not
on the registry record and the journal pages sit behind a bot
check.[^lagerloef-1999][^dohan-2017][^bonjean-2002] The producer's
validation page, which the handbook names as the place where version 2
validation results live, was unreachable from the drafting session
(the host is blocked by the network policy), so no validation
statistic is quoted here.[^guide]

[^guide]: OSCAR v2.0 User's Handbook, Dohan, October 2021
[^podaac-final]: PO.DAAC collection page, OSCAR_L4_OC_FINAL_V2.0
[^bonjean-2002]: Bonjean and Lagerloef, 2002, Journal of Physical Oceanography, doi:10.1175/1520-0485(2002)032<2938:DMAAOT>2.0.CO;2
[^lagerloef-1999]: Lagerloef and others, 1999, Journal of Geophysical Research: Oceans, doi:10.1029/1999JC900197
[^dohan-2017]: Dohan, 2017, Journal of Geophysical Research: Oceans, doi:10.1002/2017JC012961
[^dataset]: This bundle's OSCAR dataset concept
