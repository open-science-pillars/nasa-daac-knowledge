# What this bundle claims about your products

The `obdaac` bundle, concept by concept, grouped by the product each one names. Rendered by `tools/digest.py` from the concepts' frontmatter; never edited by hand (the check routine fails when this page is stale).

If you know one of these products, each row's last link opens an issue with the concept and product filled in: say whether the claim is right, and correct it if not. Your answer is recorded on the concept as a verified event in your name, with a link to your reply. A row marked Asked already has an open issue (the maintainer asked someone); answer there.

## Summary

6 concepts, 2 products.

- unverified: 0
- machine-confirmed: 0
- human-reviewed: 6
- provider-confirmed: 0

A tier reads the concept's verified events: unverified (none), machine-confirmed (process events only), human-reviewed (a person signed), provider-confirmed (a person from the organization that produces the data confirmed it).

## MODIS-Aqua Level 3 mapped chlorophyll-a (OB.DAAC, reprocessing R2022)

[datasets/modis-aqua-l3-chlorophyll.md](datasets/modis-aqua-l3-chlorophyll.md): 5 concepts.

| Concept | Type | Severity | Status | Tier | Latest verified | Sources | |
|---|---|---|---|---|---|---|---|
| [MODIS-Aqua Level 3 mapped chlorophyll-a (OB.DAAC, reprocessing R2022)](datasets/modis-aqua-l3-chlorophyll.md) | dataset |  | stable | human-reviewed | 2026-09-14 | 14 | [Confirm or correct](https://github.com/open-science-pillars/nasa-daac-knowledge/issues/new?template=confirm_concept.yml&title=Confirm%3A+knowledge%2Fobdaac%2Fdatasets%2Fmodis-aqua-l3-chlorophyll.md&concept=knowledge%2Fobdaac%2Fdatasets%2Fmodis-aqua-l3-chlorophyll.md&product=MODIS-Aqua+Level+3+mapped+chlorophyll-a+%28OB.DAAC%2C+reprocessing+R2022%29) |
| [The standard chlor_a is two algorithms blended between 0.25 and 0.35 mg per cubic metre: a threshold, histogram, gradient or front inside that range measures the switch between the color index and the band ratio, and the transition itself moved between reprocessings](gotchas/chlor-a-blended-ocx-and-ci.md) | dataset-gotcha | high | stable | human-reviewed | 2026-09-14 | 7 | [Confirm or correct](https://github.com/open-science-pillars/nasa-daac-knowledge/issues/new?template=confirm_concept.yml&title=Confirm%3A+knowledge%2Fobdaac%2Fgotchas%2Fchlor-a-blended-ocx-and-ci.md&concept=knowledge%2Fobdaac%2Fgotchas%2Fchlor-a-blended-ocx-and-ci.md&product=MODIS-Aqua+Level+3+mapped+chlorophyll-a+%28OB.DAAC%2C+reprocessing+R2022%29) |
| [A Level 3 chlorophyll composite is the mean of the observations that survived the flags in the period, with no count in the mapped file: a monthly mean is a mean of the sampled days, high latitudes have no winter value, cloudy seasons have few, and a climatology is re-cut every month](gotchas/chlor-a-composite-sampling-gaps.md) | dataset-gotcha | medium | stable | human-reviewed | 2026-09-14 | 7 | [Confirm or correct](https://github.com/open-science-pillars/nasa-daac-knowledge/issues/new?template=confirm_concept.yml&title=Confirm%3A+knowledge%2Fobdaac%2Fgotchas%2Fchlor-a-composite-sampling-gaps.md&concept=knowledge%2Fobdaac%2Fgotchas%2Fchlor-a-composite-sampling-gaps.md&product=MODIS-Aqua+Level+3+mapped+chlorophyll-a+%28OB.DAAC%2C+reprocessing+R2022%29) |
| [chlor_a is a near-surface pigment concentration that the producer calls a proxy for phytoplankton biomass: it is not biomass, not carbon and not primary production, which the same producer distributes as separate products with their own algorithms](gotchas/chlor-a-is-not-biomass.md) | dataset-gotcha | medium | stable | human-reviewed | 2026-09-14 | 6 | [Confirm or correct](https://github.com/open-science-pillars/nasa-daac-knowledge/issues/new?template=confirm_concept.yml&title=Confirm%3A+knowledge%2Fobdaac%2Fgotchas%2Fchlor-a-is-not-biomass.md&concept=knowledge%2Fobdaac%2Fgotchas%2Fchlor-a-is-not-biomass.md&product=MODIS-Aqua+Level+3+mapped+chlorophyll-a+%28OB.DAAC%2C+reprocessing+R2022%29) |
| [A reprocessing rewrites the whole chlorophyll record and the catalogue keeps one version: a series comes from one reprocessing, files fetched before and after a reprocessing are two products, and the near-real-time tail is a third](gotchas/chlor-a-one-reprocessing-per-series.md) | dataset-gotcha | medium | stable | human-reviewed | 2026-09-14 | 10 | [Confirm or correct](https://github.com/open-science-pillars/nasa-daac-knowledge/issues/new?template=confirm_concept.yml&title=Confirm%3A+knowledge%2Fobdaac%2Fgotchas%2Fchlor-a-one-reprocessing-per-series.md&concept=knowledge%2Fobdaac%2Fgotchas%2Fchlor-a-one-reprocessing-per-series.md&product=MODIS-Aqua+Level+3+mapped+chlorophyll-a+%28OB.DAAC%2C+reprocessing+R2022%29) |

## PACE OCI Level 3 mapped chlorophyll-a (OB.DAAC, the BGC suite, version 3.2)

[datasets/pace-oci-l3-chlorophyll.md](datasets/pace-oci-l3-chlorophyll.md): 5 concepts.

| Concept | Type | Severity | Status | Tier | Latest verified | Sources | |
|---|---|---|---|---|---|---|---|
| [PACE OCI Level 3 mapped chlorophyll-a (OB.DAAC, the BGC suite, version 3.2)](datasets/pace-oci-l3-chlorophyll.md) | dataset |  | stable | human-reviewed | 2026-09-14 | 14 | [Confirm or correct](https://github.com/open-science-pillars/nasa-daac-knowledge/issues/new?template=confirm_concept.yml&title=Confirm%3A+knowledge%2Fobdaac%2Fdatasets%2Fpace-oci-l3-chlorophyll.md&concept=knowledge%2Fobdaac%2Fdatasets%2Fpace-oci-l3-chlorophyll.md&product=PACE+OCI+Level+3+mapped+chlorophyll-a+%28OB.DAAC%2C+the+BGC+suite%2C+version+3.2%29) |
| [The standard chlor_a is two algorithms blended between 0.25 and 0.35 mg per cubic metre: a threshold, histogram, gradient or front inside that range measures the switch between the color index and the band ratio, and the transition itself moved between reprocessings](gotchas/chlor-a-blended-ocx-and-ci.md) | dataset-gotcha | high | stable | human-reviewed | 2026-09-14 | 7 | [Confirm or correct](https://github.com/open-science-pillars/nasa-daac-knowledge/issues/new?template=confirm_concept.yml&title=Confirm%3A+knowledge%2Fobdaac%2Fgotchas%2Fchlor-a-blended-ocx-and-ci.md&concept=knowledge%2Fobdaac%2Fgotchas%2Fchlor-a-blended-ocx-and-ci.md&product=PACE+OCI+Level+3+mapped+chlorophyll-a+%28OB.DAAC%2C+the+BGC+suite%2C+version+3.2%29) |
| [A Level 3 chlorophyll composite is the mean of the observations that survived the flags in the period, with no count in the mapped file: a monthly mean is a mean of the sampled days, high latitudes have no winter value, cloudy seasons have few, and a climatology is re-cut every month](gotchas/chlor-a-composite-sampling-gaps.md) | dataset-gotcha | medium | stable | human-reviewed | 2026-09-14 | 7 | [Confirm or correct](https://github.com/open-science-pillars/nasa-daac-knowledge/issues/new?template=confirm_concept.yml&title=Confirm%3A+knowledge%2Fobdaac%2Fgotchas%2Fchlor-a-composite-sampling-gaps.md&concept=knowledge%2Fobdaac%2Fgotchas%2Fchlor-a-composite-sampling-gaps.md&product=PACE+OCI+Level+3+mapped+chlorophyll-a+%28OB.DAAC%2C+the+BGC+suite%2C+version+3.2%29) |
| [chlor_a is a near-surface pigment concentration that the producer calls a proxy for phytoplankton biomass: it is not biomass, not carbon and not primary production, which the same producer distributes as separate products with their own algorithms](gotchas/chlor-a-is-not-biomass.md) | dataset-gotcha | medium | stable | human-reviewed | 2026-09-14 | 6 | [Confirm or correct](https://github.com/open-science-pillars/nasa-daac-knowledge/issues/new?template=confirm_concept.yml&title=Confirm%3A+knowledge%2Fobdaac%2Fgotchas%2Fchlor-a-is-not-biomass.md&concept=knowledge%2Fobdaac%2Fgotchas%2Fchlor-a-is-not-biomass.md&product=PACE+OCI+Level+3+mapped+chlorophyll-a+%28OB.DAAC%2C+the+BGC+suite%2C+version+3.2%29) |
| [A reprocessing rewrites the whole chlorophyll record and the catalogue keeps one version: a series comes from one reprocessing, files fetched before and after a reprocessing are two products, and the near-real-time tail is a third](gotchas/chlor-a-one-reprocessing-per-series.md) | dataset-gotcha | medium | stable | human-reviewed | 2026-09-14 | 10 | [Confirm or correct](https://github.com/open-science-pillars/nasa-daac-knowledge/issues/new?template=confirm_concept.yml&title=Confirm%3A+knowledge%2Fobdaac%2Fgotchas%2Fchlor-a-one-reprocessing-per-series.md&concept=knowledge%2Fobdaac%2Fgotchas%2Fchlor-a-one-reprocessing-per-series.md&product=PACE+OCI+Level+3+mapped+chlorophyll-a+%28OB.DAAC%2C+the+BGC+suite%2C+version+3.2%29) |

## Concepts that name no product

Conventions, requirements, method concepts and anything whose claim is not about one product. The same link applies: confirm or correct.

None.
