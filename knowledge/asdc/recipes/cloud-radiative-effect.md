---
type: Recipe
spheres: [atmosphere]
title: "Computing a cloud radiative effect from CERES EBAF: choosing the clear-sky convention, weighting the region and reading the residual"
description: "The terms of a top-of-atmosphere cloud radiative effect over a window and a region, which field supplies each, which concept holds each term's trap (the two clear-sky conventions the product carries and the effect's inheritance of whichever is subtracted; the zonal geodetic weights the product's own global means are formed with; the absence of any surface type mask in the fields read), the rule that the convention is declared and never inferred, and how the result is read: the terms as the convention's, the decomposition residual as a check on the product's fields, the contrast with the other convention as the price of the choice."
tags: [ceres, ebaf, cloud-radiative-effect, clear-sky, total-region, cloud-free-area, convention, radiation-budget, recipe]
generated: { by: knowledge-seeder/claude, at: 2026-09-19T07:10:00Z }
inputs:
  - dataset: ../datasets/ceres-ebaf-ed4-2.md
  - all_sky: "the all-sky outgoing shortwave, outgoing longwave and net downward TOA fluxes per calendar month on the one degree grid (toa_sw_all_mon, toa_lw_all_mon, toa_net_all_mon) from the CERES EBAF Edition 4.2.1 file, the edition and release date stated"
  - clear_sky: "the clear-sky triple of the declared convention from the same file: the _clr_t_ fields for total-region, the _clr_c_ fields for cloud-free-area; the long names in the file say which is which, and the product's own cloud radiative effect variables read uses Clear-Sky for total region"
  - weights: "the CERES one degree zonal geodetic weights, the weights the product's own global means are formed with, applied to the zones of the region"
  - method: "the attested computation ../computations/cloud-radiative-effect.md: three terms in watts per square metre of the region, the decomposition residual, the combined uncertainty, the verdict, the contrast with the other convention, the distance from the published global mean where the run is of its region, convention and period"
expected:
  - quantity: "the identity"
    statement: "the net cloud radiative effect equals the sum of its shortwave and longwave parts; the residual of that decomposition is compared with a stated tolerance of 0.01 W m-2, which is the granularity of the product's fields and not a sampling bar"
  - quantity: "numeric anchor"
    statement: "global, cloud-free-area, 2005-07 through 2015-06 on the stamped data root (120 of 120 months): shortwave -45.8232, longwave +27.9340, net -17.8894 W m-2, residual -1.1e-04 against a bar of 0.01, decomposition closes; recorded with its loader, its stamp and its run id in ../computations/cloud-radiative-effect.md"
  - quantity: "the published global mean"
    statement: "the CERES_EBAF_Ed4.0 Data Quality Summary's global mean TOA fluxes for July 2005 through June 2015, a shortwave cloud radiative effect of -45.8, a longwave one of 28.0 and a net one of -17.9 W m-2 on the cloud-free-area definition, which the anchored run sits -0.023, -0.066 and +0.011 from, all inside the 0.1 W m-2 the table is rounded to"
  - quantity: "the price of the convention"
    statement: "the same window and region on the total-region convention gives a net effect of -19.6352 W m-2, 1.7458 from the cloud-free-area one; over the Antarctic band the difference reverses sign, -10.9951 on total-region against -12.6639 on cloud-free-area"
expected_uncertainty:
  - quantity: "each term"
    statement: "the larger of the 95 percent sampling half width of the window mean under a lag-1 autocorrelated residual about the calendar-month means and the formal error the per-month floor propagates; the product ships no uncertainty field, so the floor is measured on the series and the published regional monthly flux uncertainties are quoted in the stamp beside it, never mixed into it"
  - quantity: "the convention difference"
    statement: "not an uncertainty. It is a difference between two defined quantities, stated as a contrast and never folded into a bar; a statement that does not name its convention has no uncertainty that covers it"
  - quantity: "the decomposition residual"
    statement: "not a physical closure. The net flux is the solar irradiance minus the two outgoing fluxes, so the decomposition is an identity of the product's own fields and the residual measures whether the stored fields keep it"
sources:
  - id: computation
    resource: ../computations/cloud-radiative-effect.md
    title: "The attested computation this recipe walks: the terms, the convention parameter, the weighting, the bookkeeping, the fixture, the refusal rule, the reference runs"
  - id: convention
    resource: ../conventions/ceres-clear-sky-conventions.md
    title: "This bundle's convention concept: the four quantities the CERES products call clear-sky and which convention each field carries"
  - id: gotcha-clear-sky
    resource: ../gotchas/ebaf-clear-sky-definitions.md
    title: "This bundle's gotcha: the two EBAF definitions, the cloud radiative effect's definition change at Edition 4.1, and the published size of the adjustment between them"
  - id: dataset
    resource: ../datasets/ceres-ebaf-ed4-2.md
    title: "This bundle's EBAF dataset concept: the product, its editions, its uncertainties and the satellite transitions"
  - id: dqs
    resource: https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_EBAF_Ed4.2_DQS.pdf
    title: "CERES_EBAF_Ed4.2 and Ed4.2.1 Data Quality Summary, version 8, 2026-09-10, read 2026-09-19: the cloud radiative effect definition and its change at Edition 4.2, the sign rule, the unphysical signs under the cloud-free-area definition, and the zonal geodetic weighting of global means"
  - id: dqs-ed4-0
    resource: https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_EBAF_Ed4.0_DQS.pdf
    title: "CERES_EBAF_Ed4.0 Data Quality Summary, 2018-01-17, read 2026-09-19: Table 6-1, the global mean TOA fluxes and cloud radiative effects for July 2005 through June 2015, the published anchor"
  - id: loeb-2020
    resource: https://doi.org/10.1175/JCLI-D-19-0381.1
    title: "Loeb and others (2020), Toward a Consistent Definition between Satellite and Model Clear-Sky Radiative Fluxes, Journal of Climate 33, 61 to 75 (the registry record, 2026-09-19): the total-region methodology and the size and regional shape of the adjustment"
  - id: data-root
    resource: ../references/retrieval/cloud-radiative-effect-root/RECORD.json
    title: "The stamped data root the real run reads: the loader's stamp, the coverage table and the bookkeeping table"
status: draft
stale_after: 2027-03-19
---

# Computing a cloud radiative effect from CERES EBAF

**The arithmetic is one line and the bookkeeping is the work.** A
cloud radiative effect at the top of the atmosphere is the all-sky
flux minus the clear-sky flux, and both data quality summaries define
it exactly that way.[^dqs] The trouble is that the definition says
nothing about which clear-sky field is subtracted, and the energy
balanced product carries two: the traditional flux over the cloud-free
portions of a region, filled where no cloud-free footprint was
observed, and the flux for the total region with its cloudy portions
included, which is the definition climate models use and which the
product's own cloud radiative effect variables have been computed from
since Edition 4.1.[^convention][^gotcha-clear-sky][^dqs] The effect
inherits whichever one went in, and nothing in the resulting number
records which that was.

**The steps.**

1. **Name the convention before reading a field.** The four quantities
   the CERES products call clear-sky, and which convention each field
   carries, are the bundle's convention concept; read it first.[^convention]
   In the energy balanced product the choice is between the `_clr_t_`
   triple (total region) and the `_clr_c_` triple (cloud-free areas of
   region), and the file's own long names spell both out. A `pristine`
   or a computed cloud-removed clear-sky flux is a SYN1deg quantity
   and this product has no such field, so an effect against one of
   those is not available here and is not approximated.[^convention]
2. **Take the all-sky triple from the same file, edition and month.**
   The shortwave and longwave fields are outgoing fluxes and the net
   field is downward minus upward, so the effect is the clear-sky
   minus the all-sky flux in the shortwave and the longwave and the
   all-sky minus the clear-sky flux in the net.[^dqs] Getting that
   backwards puts a plus sign on a cooling.
3. **Weight the region the way the product weights the globe.** Global
   means in this product are formed with the CERES one degree zonal
   geodetic weights, an oblate spheroid with the solar division factor
   4.0034 rather than 4.[^dqs] A cos-latitude mean is a different
   number. A region that is a band of whole one degree zones is the
   same weighted mean restricted to those zones; a region that needs a
   land, ocean or sea ice mask needs a field the flux subset does not
   carry, and the attested computation refuses one rather than
   guessing.[^computation]
4. **Form the net term from the net fields, not from the other two.**
   That makes the decomposition a check rather than a tautology: the
   net flux is the solar irradiance minus the two outgoing fluxes, so
   the three terms must satisfy an identity the stored fields can
   break, and the residual says whether they do.[^computation]
5. **State the convention with the number, and state what the other
   one gives.** Over July 2005 through June 2015 the global net cloud
   radiative effect is -17.889 W m-2 on the cloud-free-area convention
   and -19.635 on the total-region one.[^data-root] A number quoted
   without its convention is ambiguous by 1.7 W m-2 in the global
   mean, and by more regionally and with the opposite sign at high
   latitude, where the total-region effect is the less negative of the
   two.[^loeb-2020][^gotcha-clear-sky]

**What the anchor does not carry.** The product's global mean net TOA
flux is adjusted once to an in situ ocean heating estimate, which is
the caveat on every absolute flux from this product. It does not reach
a cloud radiative effect: the adjustment enters the all-sky and the
clear-sky field of the same month, so it cancels in their difference.
These terms are differences, never levels.[^computation]

**How the result is read.** The three terms are the effect of clouds
on the radiation budget as the atmosphere was, over the months used
and the zones of the region, on the convention named. They are not a
cloud feedback, which is the response of clouds to warming and a
different quantity. The residual of the decomposition inside its
tolerance says the product's net field agrees with its shortwave and
longwave fields, nothing more. The distance from a published global
mean is stated only where the run is of that number's region,
convention and period, and carries both the published rounding and the
edition change; a distance across conventions would compare two
different quantities and the computation states no such
distance.[^computation][^dqs-ed4-0]

**Where a comparison goes wrong.** A cloud radiative effect from an
Edition 4.0 file placed beside one from Edition 4.2 mixes the two
definitions and reads the definition change as a change in clouds; the
bundle's gotcha owns that failure mode and the size of the difference,
and this recipe does not restate it.[^gotcha-clear-sky] A comparison
with a climate model uses the total-region definition on both sides,
because a model's clear-sky flux is by construction a total-region
one.[^loeb-2020] A window that crosses the Terra-only, Terra plus Aqua
and NOAA-20-only boundaries carries the climatology adjustments the
record is stitched with, which the dataset concept owns.[^dataset]

**The attested form.** The computation walks these steps with the
convention, the weighting and the region as receipt facts, three
terms, a residual, a verdict and a contrast the attester recomputes;
its real-data run over July 2005 through June 2015 on the
cloud-free-area convention lands 0.011 W m-2 from the published net
cloud radiative effect, and is the anchor quoted in the expectations
above.[^computation]

**Provenance.** Every number quoted from this recipe names the product
edition and release date, the file read and its hash, the clear-sky
convention and the variable it came from, the weights, the region and
its latitude band, the window and the months missing. The two data
quality summaries and the zonal geodetic weights were read on
2026-09-19, the granule read the same day through the archive's
subsetting service, and every DOI verified against the Crossref
registry that day; the journal pages sit behind a bot check and were
not read.[^dqs][^dqs-ed4-0][^loeb-2020]

[^computation]: computations/cloud-radiative-effect.md
[^convention]: conventions/ceres-clear-sky-conventions.md
[^gotcha-clear-sky]: gotchas/ebaf-clear-sky-definitions.md
[^dataset]: datasets/ceres-ebaf-ed4-2.md
[^dqs]: CERES_EBAF_Ed4.2 and Ed4.2.1 Data Quality Summary, version 8, 2026-09-10
[^dqs-ed4-0]: CERES_EBAF_Ed4.0 Data Quality Summary, 2018-01-17, Table 6-1
[^loeb-2020]: Loeb and others (2020), Journal of Climate 33, doi:10.1175/JCLI-D-19-0381.1
[^data-root]: references/retrieval/cloud-radiative-effect-root/RECORD.json
