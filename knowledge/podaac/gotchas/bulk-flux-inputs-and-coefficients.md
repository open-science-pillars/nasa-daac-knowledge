---
type: dataset-gotcha
spheres: [hydrosphere, atmosphere]
title: "A wind stress or air-sea flux computed by a bulk formula carries its inputs' errors and its formula's coefficients: the ESDR stress is one linear drag law on the equivalent neutral wind, a stress from averaged or blended winds is biased low by the nonlinearity, and no product's stress is an observation of stress"
description: "The MEaSUREs ESDR computes wind stress as air density times a drag coefficient times the equivalent neutral wind speed times the vector, with a linear drag coefficient (7.94e-5 times the wind speed plus 6.12e-4) chosen for agreement with COARE 3.5 up to 20 m/s; the guide records that the Large et al. 1994 formulation would underestimate stress above about 8 m/s, that candidate coefficient models differ most above 10 m/s, and that stress from averaged winds is underestimated because the relation is nonlinear. Its true 10 m winds rest on ERA5 stability inputs and GlobCurrent currents. CCMP carries no stress, and a stress or a heat flux computed from CCMP monthly means, or from any product, inherits the wind product's error where the satellites were absent, the chosen coefficient, the assumed density and the stability and humidity inputs. Two stresses from different coefficients differ by construction, and a flux difference between products is not a measured difference."
tags: [wind-stress, bulk-formula, drag-coefficient, coare, air-sea-flux, esdr, ccmp, scatterometer, ekman, wind-stress-curl]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T13:30:00Z }
severity: medium
dataset: ../datasets/ascat-winds.md
status: draft
stale_after: 2027-03-15
sources:
  - id: measures-guide
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/measures_ocean_surface_wind_vectors/open/docs/2022_12_02_MEASURES_NewDataGuide_v17_accepted.pdf
    title: "MEaSUREs OSVW user's guide, Hristova-Veleva and others, 1 December 2022 (read in full 2026-09-15): the stress section (the bulk relation, the neutral drag coefficient needing no stability adjustment, the candidate models Large et al. 1994, Liu and Tang 1996, COARE 3.5 and the KNMI linear model, the Gulf of Maine flux-buoy comparison across 3 to 15 m/s, the chosen coefficients a and b), the four error sources of stress from blended Level 4 winds and the underestimation from averaged winds, the true-wind section with its COARE 3.5 inputs from ERA5 and GlobCurrent, and the uncertainty section (stress direction error equals wind direction error; stress magnitude error from triple collocation)"
  - id: podaac-esdr-b
    resource: https://podaac.jpl.nasa.gov/dataset/ASCATB_ESDR_L2_WIND_STRESS_V1.1
    title: "PO.DAAC collection page, ASCATB_ESDR_L2_WIND_STRESS_V1.1 (read 2026-09-15): the variable table with wind_stress_magnitude, direction, u and v in N m-2 and their uncertainty fields, labelled estimated ocean surface wind stress"
  - id: esdr-readme
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/measures_ocean_surface_wind_vectors/open/docs/README_latest_measures_v1.1_l2_ascat_scatsat_readmes_2024_06_12_SHV_v08.docx
    title: "MEaSUREs ESDR Level 2 README, 12 June 2024 (read 2026-09-15): the ancillary files' purpose of providing the information needed for future estimation of surface fluxes, and their ERA5 SST, surface pressure, 2 m temperature and relative humidity fields"
  - id: edson-2013
    resource: https://doi.org/10.1175/JPO-D-12-0173.1
    title: "Edson and others, 2013, On the Exchange of Momentum over the Open Ocean, Journal of Physical Oceanography 43, 1589 to 1610: the COARE 3.5 paper the guide cites, whose abstract states the refinement of COARE 3.0 from direct covariance stress in four field experiments, a wind-speed-dependent Charnock coefficient, and significant improvement above 13 m/s (registry record verified and abstract read there 2026-09-15; the article was not read)"
  - id: large-1994
    resource: https://doi.org/10.1029/94RG01872
    title: "Large, McWilliams and Doney, 1994, Oceanic vertical mixing: A review and a model with a nonlocal boundary layer parameterization, Reviews of Geophysics 32, 363 to 403: the reference the guide names for the drag formulation many scatterometer stress applications use and that its flux-buoy comparison finds underestimating stress above about 8 m/s (registry record verified and abstract read there 2026-09-15; the abstract concerns the mixing parameterization and the article was not read)"
  - id: portabella-2009
    resource: https://doi.org/10.1175/2008JTECHO578.1
    title: "Portabella and Stoffelen, 2009, On Scatterometer Ocean Stress, Journal of Atmospheric and Oceanic Technology 26, 368 to 382: the abstract's finding that two commonly used surface-layer models with different roughness and stability parameterizations show little difference in stress estimation, that the uncertainty of the NWP dataset is generally larger than that of the buoy and scatterometer datasets, and that scatterometer winds can be reliably transformed to stress (registry record verified and abstract read there 2026-09-15; the article was not read)"
  - id: de-kloe-2017
    resource: https://doi.org/10.1109/JSTARS.2017.2685242
    title: "de Kloe, Stoffelen and Verhoef, 2017, Improved Use of Scatterometer Measurements by Using Stress-Equivalent Reference Winds, IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing 10, 2340 to 2347: the source of the linear drag model the guide adopts and of the stress, friction velocity and equivalent neutral wind review (registry record verified 2026-09-15; the record carries no abstract and the article was not read)"
  - id: ccmp-guide
    resource: https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ccmp/open/L4_V3.1/docs/User_Guide_3.1.r1.pdf
    title: "CCMP Version 3.1 User Guide, Mears and Henze, 15 July 2024 (read in full 2026-09-15): the file tables (no stress or flux field), the monthly file note that the average wind speed can be very different from the magnitude of the averaged components, the validation with and without satellites, and the high-wind bias by design"
  - id: dataset
    resource: ../datasets/ascat-winds.md
    title: "This bundle's ASCAT dataset concept (read 2026-09-15): the ESDR's stress fields, uncertainties and ancillary inputs"
  - id: ccmp
    resource: ../datasets/ccmp-wind-analysis.md
    title: "This bundle's CCMP dataset concept (read 2026-09-15): a Level 4 wind analysis with no stress or flux field and no uncertainty field"
  - id: ecco-curl
    resource: ../recipes/ecco-wind-stress-curl.md
    title: "This bundle's ECCO wind-stress curl recipe (read 2026-09-15): a curl computed from the model's own oceTAUX and oceTAUY, the stress the state estimate applied, which is a third convention beside a scatterometer stress and a bulk stress from an analysis"
---

# Bulk flux inputs and coefficients

**Mechanism.** No PO.DAAC wind product measures stress. The ESDR
estimates it from the scatterometer equivalent neutral wind by the
bulk relation tau equals air density times the neutral drag
coefficient times the wind speed times the wind vector, the neutral
coefficient chosen because an equivalent neutral wind needs no
adjustment for boundary layer stability; the guide names the air
density as a term of the relation and gives no value or source for
it.[^measures-guide][^de-kloe-2017]
The coefficient is a choice, and the guide records the choice and the
alternatives: many scatterometer stress applications use the Large et
al. 1994 formulation, more recent field data (Edson et al. 2013 among
them) differ considerably from it above 10 m/s, the project evaluated
Large et al. 1994, Liu and Tang 1996, COARE 3.5 and a linear model
from de Kloe et al. 2017 that KNMI uses for its ASCAT stress products
against buoy eddy-covariance stress, found that Large et al. would
underestimate stress above about 8 m/s while the linear model agreed
with COARE 3.5 well enough to be equivalent up to 20 m/s, and adopted
the linear model, Cd equals a times the wind speed plus b with a equal
to 7.94e-5 and b to 6.12e-4, as a first version that performed well
against Gulf of Maine flux-buoy stress across 3 to 15 m/s and can be
changed in future versions once a larger flux-buoy dataset
exists.[^measures-guide][^large-1994][^edson-2013] COARE 3.5 itself
is a refinement of COARE 3.0 from direct covariance stress in four
field experiments, with a wind-speed-dependent Charnock coefficient
and its main improvement above 13 m/s.[^edson-2013] The stress
uncertainty in the files follows from the wind uncertainty: the stress
direction error equals the equivalent neutral wind direction error,
and the stress magnitude error comes from the same triple collocation
of QuikSCAT, ASCAT-A and ERA5.[^measures-guide][^podaac-esdr-b] The
guide names four error sources of a stress computed from blended Level
4 winds: the blending of sources with different representativeness
and error, biases from missing observations in rain-flagged areas,
biases from estimating stress from averaged products, and aliasing
from model output acting as a smoother, and it states that using
averaged winds to estimate the average stress underestimates it
because the relation is nonlinear, which is why the ESDR computes
stress on the swath before any gridding.[^measures-guide] The true
10 m wind, the other derived quantity, rests on inputs the guide
lists: ERA5 2 m air temperature, surface pressure, SST and boundary
layer height, a relative humidity by the Magnus approximation, and
GlobCurrent total currents, run through COARE 3.5 in reverse, with
files missing where an input was unavailable.[^measures-guide] CCMP
carries no stress or flux field and no uncertainty field, and its
monthly files note that the average wind speed can be very different
from the magnitude of the averaged components; a stress from CCMP is
the user's own bulk computation on an analysis whose wind-speed
standard deviation against the withheld ASCAT-C is 0.75 m/s where a
satellite contributed and 1.25 m/s where none did, and against moored
buoys 0.97 against 1.45 m/s.[^ccmp-guide][^ccmp] The
triple-collocation study of scatterometer stress found two commonly
used surface-layer models showing little difference in stress and the
numerical weather prediction dataset generally more uncertain than
the buoy and scatterometer datasets, a statement about those two
models and that dataset, not about the coefficient choices the guide
lists.[^portabella-2009] A state estimate's stress, such as the ECCO
fields the bundle's curl recipe differentiates, is a third thing: the
stress the model applied, consistent with the model's own forcing and
adjustments.[^ecco-curl] The ESDR ancillary files exist, by the
README's statement, to provide the information needed for future
estimation of surface fluxes, which is to say that the flux inputs
(SST, pressure, temperature, humidity) ship beside the wind rather than
inside a flux product.[^esdr-readme]

**Wrong-result mode.** A stress or an Ekman transport computed from
CCMP monthly means underestimates the stress by the nonlinearity the
guide names, and a stress from the 6-hourly analysis carries the
background wherever `nobs` is zero, so a stress map has the same
observed-and-modelled patchwork as the wind map, and because stress
goes as the square of the speed a relative wind error enters the
stress at roughly twice its size.[^measures-guide][^ccmp-guide] A
comparison of the ESDR stress against a stress computed from another
wind product with another drag law, or against a model's applied
stress, reports the coefficient difference as a physical difference:
Large et al. 1994 against the linear law differ above about 8 m/s by
the guide's own comparison, and the 1.5 to 2 times uncertainty
scaling of indicator 2 and 3 cells propagates into the stress
fields.[^measures-guide] A stress computed from the ESDR
`real_wind_*` fields with the same neutral coefficient, or from the
`en_wind_*` fields with a stability-dependent coefficient, applies the
stability correction twice or not at all.[^measures-guide] A latent or
sensible heat flux computed by a bulk formula from any of these winds
carries, beside the wind product's error, the transfer coefficient's
own uncertainty and the SST, air temperature and humidity inputs,
and a flux difference between two wind products is the wind
difference passed through one formula, not a measured flux
difference.[^measures-guide][^esdr-readme] A high-wind stress from
CCMP inherits the analysis's deliberate high bias above about 15 to
18 m/s at roughly twice its relative size.[^ccmp-guide] None of this raises an error: a stress
field in N m-2 looks the same whichever coefficient produced it.[^podaac-esdr-b]

**Correct approach.** A stress or flux result names the wind product
and its convention, the coefficient model with its coefficients or its
citation, the assumed air density or its source, and, for a flux, the
SST, temperature and humidity inputs.[^measures-guide][^esdr-readme] A
stress from the ESDR is quoted as that product's stress with its
per-cell uncertainty and its stated coefficient, and a comparison
against another stress converts both to one coefficient or states that
they differ by the coefficient.[^measures-guide][^podaac-esdr-b] A
stress from an analysis such as CCMP is computed from the highest
time resolution available rather than from monthly means, carries the
`nobs` fraction of its cells, and is stated as a bulk estimate on an
analysis with no uncertainty field.[^measures-guide][^ccmp-guide][^ccmp]
A wind-stress curl or Ekman quantity compared with a state estimate's
own stress names the state estimate's stress as the model's applied
forcing.[^ecco-curl]

**Verification.** The MEaSUREs guide's stress, true-wind and
uncertainty sections are the product's own statement of the bulk
relation, the coefficient evaluation, the chosen coefficients, the
inputs and the error sources; they were read in full on
2026-09-15.[^measures-guide] The ESDR collection page's variable table
and the README were read the same day.[^podaac-esdr-b][^esdr-readme]
The CCMP guide's file tables and monthly note were read in full the
same day.[^ccmp-guide] The four papers' registry records were verified
on 2026-09-15 (title, authors, journal, year); the 2013, 1994 and 2009
abstracts were read there and the 2017 record carries no abstract; no
journal page was read, so the coefficient values are quoted from the
guide and not from the papers.[^edson-2013][^large-1994][^portabella-2009][^de-kloe-2017]
No granule was opened, and the guide gives no value for the air
density, so the density used in the files is not stated here.[^dataset]

[^measures-guide]: MEaSUREs OSVW user's guide, Hristova-Veleva and others, 1 December 2022
[^podaac-esdr-b]: PO.DAAC collection page, ASCATB_ESDR_L2_WIND_STRESS_V1.1
[^esdr-readme]: MEaSUREs ESDR Level 2 README, 12 June 2024
[^edson-2013]: Edson and others, 2013, Journal of Physical Oceanography, doi:10.1175/JPO-D-12-0173.1
[^large-1994]: Large, McWilliams and Doney, 1994, Reviews of Geophysics, doi:10.1029/94RG01872
[^portabella-2009]: Portabella and Stoffelen, 2009, Journal of Atmospheric and Oceanic Technology, doi:10.1175/2008JTECHO578.1
[^de-kloe-2017]: de Kloe, Stoffelen and Verhoef, 2017, IEEE JSTARS, doi:10.1109/JSTARS.2017.2685242
[^ccmp-guide]: CCMP Version 3.1 User Guide, Mears and Henze, 15 July 2024
[^dataset]: This bundle's ASCAT dataset concept
[^ccmp]: This bundle's CCMP dataset concept
[^ecco-curl]: This bundle's ECCO wind-stress curl recipe
