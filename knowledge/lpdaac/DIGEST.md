# What this bundle claims about your products

The `lpdaac` bundle, concept by concept, grouped by the product each one names. Rendered by `tools/digest.py` from the concepts' frontmatter; never edited by hand (the check routine fails when this page is stale).

If you know one of these products, each row's last link opens an issue with the concept and product filled in: say whether the claim is right, and correct it if not. Your answer is recorded on the concept as a verified event in your name, with a link to your reply. A row marked Asked already has an open issue (the maintainer asked someone); answer there.

## Summary

7 concepts, 2 products.

- unverified: 0
- machine-confirmed: 0
- human-reviewed: 7
- provider-confirmed: 0

A tier reads the concept's verified events: unverified (none), machine-confirmed (process events only), human-reviewed (a person signed), provider-confirmed (a person from the organization that produces the data confirmed it).

## HLS L30 version 2.0: Landsat 8 and 9 nadir BRDF-adjusted surface reflectance on 30 m MGRS tiles

[datasets/hls-l30.md](datasets/hls-l30.md): 6 concepts.

| Concept | Type | Severity | Status | Tier | Latest verified | Sources | |
|---|---|---|---|---|---|---|---|
| [HLS L30 version 2.0: Landsat 8 and 9 nadir BRDF-adjusted surface reflectance on 30 m MGRS tiles](datasets/hls-l30.md) | dataset |  | stable | human-reviewed | 2026-09-14 | 11 | [Confirm or correct](https://github.com/open-science-pillars/nasa-daac-knowledge/issues/new?template=confirm_concept.yml&title=Confirm%3A+knowledge%2Flpdaac%2Fdatasets%2Fhls-l30.md&concept=knowledge%2Flpdaac%2Fdatasets%2Fhls-l30.md&product=HLS+L30+version+2.0%3A+Landsat+8+and+9+nadir+BRDF-adjusted+surface+reflectance+on+30+m+MGRS+tiles) |
| [HLS L30 and S30 keep their sensors' band numbers: B05, B06, B07, B09, B10 and B11 name different wavelengths in the two products](gotchas/hls-band-names-differ.md) | dataset-gotcha | medium | stable | human-reviewed | 2026-09-14 | 7 | [Confirm or correct](https://github.com/open-science-pillars/nasa-daac-knowledge/issues/new?template=confirm_concept.yml&title=Confirm%3A+knowledge%2Flpdaac%2Fgotchas%2Fhls-band-names-differ.md&concept=knowledge%2Flpdaac%2Fgotchas%2Fhls-band-names-differ.md&product=HLS+L30+version+2.0%3A+Landsat+8+and+9+nadir+BRDF-adjusted+surface+reflectance+on+30+m+MGRS+tiles) |
| [The HLS Fmask layer is bit-packed: cloud, shadow, snow, water and aerosol are bits to mask, not class values to compare](gotchas/hls-fmask-is-bit-packed.md) | dataset-gotcha | high | draft | human-reviewed | 2026-09-14 | 7 | [Confirm or correct](https://github.com/open-science-pillars/nasa-daac-knowledge/issues/new?template=confirm_concept.yml&title=Confirm%3A+knowledge%2Flpdaac%2Fgotchas%2Fhls-fmask-is-bit-packed.md&concept=knowledge%2Flpdaac%2Fgotchas%2Fhls-fmask-is-bit-packed.md&product=HLS+L30+version+2.0%3A+Landsat+8+and+9+nadir+BRDF-adjusted+surface+reflectance+on+30+m+MGRS+tiles) |
| [HLS reflectance is harmonized, not native: a nadir BRDF adjustment on both products and a bandpass adjustment on S30 make it differ from Landsat Collection 2 and Sentinel-2 surface reflectance](gotchas/hls-harmonized-not-native.md) | dataset-gotcha | medium | stable | human-reviewed | 2026-09-14 | 9 | [Confirm or correct](https://github.com/open-science-pillars/nasa-daac-knowledge/issues/new?template=confirm_concept.yml&title=Confirm%3A+knowledge%2Flpdaac%2Fgotchas%2Fhls-harmonized-not-native.md&concept=knowledge%2Flpdaac%2Fgotchas%2Fhls-harmonized-not-native.md&product=HLS+L30+version+2.0%3A+Landsat+8+and+9+nadir+BRDF-adjusted+surface+reflectance+on+30+m+MGRS+tiles) |
| [HLS MGRS tiles overlap, each in its own UTM zone: a mosaic or an area sum that concatenates tiles counts the overlap twice](gotchas/hls-mgrs-tile-overlap.md) | dataset-gotcha | medium | stable | human-reviewed | 2026-09-14 | 7 | [Confirm or correct](https://github.com/open-science-pillars/nasa-daac-knowledge/issues/new?template=confirm_concept.yml&title=Confirm%3A+knowledge%2Flpdaac%2Fgotchas%2Fhls-mgrs-tile-overlap.md&concept=knowledge%2Flpdaac%2Fgotchas%2Fhls-mgrs-tile-overlap.md&product=HLS+L30+version+2.0%3A+Landsat+8+and+9+nadir+BRDF-adjusted+surface+reflectance+on+30+m+MGRS+tiles) |
| [HLS reflectance is int16 scaled by 0.0001 with -9999 as fill, the thermal bands by 0.01, the QA byte by nothing with 255 as fill, and some granules do not say so in their tags](gotchas/hls-scale-and-fill.md) | dataset-gotcha | low | stable | human-reviewed | 2026-09-14 | 8 | [Confirm or correct](https://github.com/open-science-pillars/nasa-daac-knowledge/issues/new?template=confirm_concept.yml&title=Confirm%3A+knowledge%2Flpdaac%2Fgotchas%2Fhls-scale-and-fill.md&concept=knowledge%2Flpdaac%2Fgotchas%2Fhls-scale-and-fill.md&product=HLS+L30+version+2.0%3A+Landsat+8+and+9+nadir+BRDF-adjusted+surface+reflectance+on+30+m+MGRS+tiles) |

## HLS S30 version 2.0: Sentinel-2 nadir BRDF-adjusted surface reflectance, bandpass-adjusted to Landsat, on 30 m MGRS tiles

[datasets/hls-s30.md](datasets/hls-s30.md): 6 concepts.

| Concept | Type | Severity | Status | Tier | Latest verified | Sources | |
|---|---|---|---|---|---|---|---|
| [HLS S30 version 2.0: Sentinel-2 nadir BRDF-adjusted surface reflectance, bandpass-adjusted to Landsat, on 30 m MGRS tiles](datasets/hls-s30.md) | dataset |  | stable | human-reviewed | 2026-09-14 | 11 | [Confirm or correct](https://github.com/open-science-pillars/nasa-daac-knowledge/issues/new?template=confirm_concept.yml&title=Confirm%3A+knowledge%2Flpdaac%2Fdatasets%2Fhls-s30.md&concept=knowledge%2Flpdaac%2Fdatasets%2Fhls-s30.md&product=HLS+S30+version+2.0%3A+Sentinel-2+nadir+BRDF-adjusted+surface+reflectance%2C+bandpass-adjusted+to+Landsat%2C+on+30+m+MGRS+tiles) |
| [HLS L30 and S30 keep their sensors' band numbers: B05, B06, B07, B09, B10 and B11 name different wavelengths in the two products](gotchas/hls-band-names-differ.md) | dataset-gotcha | medium | stable | human-reviewed | 2026-09-14 | 7 | [Confirm or correct](https://github.com/open-science-pillars/nasa-daac-knowledge/issues/new?template=confirm_concept.yml&title=Confirm%3A+knowledge%2Flpdaac%2Fgotchas%2Fhls-band-names-differ.md&concept=knowledge%2Flpdaac%2Fgotchas%2Fhls-band-names-differ.md&product=HLS+S30+version+2.0%3A+Sentinel-2+nadir+BRDF-adjusted+surface+reflectance%2C+bandpass-adjusted+to+Landsat%2C+on+30+m+MGRS+tiles) |
| [The HLS Fmask layer is bit-packed: cloud, shadow, snow, water and aerosol are bits to mask, not class values to compare](gotchas/hls-fmask-is-bit-packed.md) | dataset-gotcha | high | draft | human-reviewed | 2026-09-14 | 7 | [Confirm or correct](https://github.com/open-science-pillars/nasa-daac-knowledge/issues/new?template=confirm_concept.yml&title=Confirm%3A+knowledge%2Flpdaac%2Fgotchas%2Fhls-fmask-is-bit-packed.md&concept=knowledge%2Flpdaac%2Fgotchas%2Fhls-fmask-is-bit-packed.md&product=HLS+S30+version+2.0%3A+Sentinel-2+nadir+BRDF-adjusted+surface+reflectance%2C+bandpass-adjusted+to+Landsat%2C+on+30+m+MGRS+tiles) |
| [HLS reflectance is harmonized, not native: a nadir BRDF adjustment on both products and a bandpass adjustment on S30 make it differ from Landsat Collection 2 and Sentinel-2 surface reflectance](gotchas/hls-harmonized-not-native.md) | dataset-gotcha | medium | stable | human-reviewed | 2026-09-14 | 9 | [Confirm or correct](https://github.com/open-science-pillars/nasa-daac-knowledge/issues/new?template=confirm_concept.yml&title=Confirm%3A+knowledge%2Flpdaac%2Fgotchas%2Fhls-harmonized-not-native.md&concept=knowledge%2Flpdaac%2Fgotchas%2Fhls-harmonized-not-native.md&product=HLS+S30+version+2.0%3A+Sentinel-2+nadir+BRDF-adjusted+surface+reflectance%2C+bandpass-adjusted+to+Landsat%2C+on+30+m+MGRS+tiles) |
| [HLS MGRS tiles overlap, each in its own UTM zone: a mosaic or an area sum that concatenates tiles counts the overlap twice](gotchas/hls-mgrs-tile-overlap.md) | dataset-gotcha | medium | stable | human-reviewed | 2026-09-14 | 7 | [Confirm or correct](https://github.com/open-science-pillars/nasa-daac-knowledge/issues/new?template=confirm_concept.yml&title=Confirm%3A+knowledge%2Flpdaac%2Fgotchas%2Fhls-mgrs-tile-overlap.md&concept=knowledge%2Flpdaac%2Fgotchas%2Fhls-mgrs-tile-overlap.md&product=HLS+S30+version+2.0%3A+Sentinel-2+nadir+BRDF-adjusted+surface+reflectance%2C+bandpass-adjusted+to+Landsat%2C+on+30+m+MGRS+tiles) |
| [HLS reflectance is int16 scaled by 0.0001 with -9999 as fill, the thermal bands by 0.01, the QA byte by nothing with 255 as fill, and some granules do not say so in their tags](gotchas/hls-scale-and-fill.md) | dataset-gotcha | low | stable | human-reviewed | 2026-09-14 | 8 | [Confirm or correct](https://github.com/open-science-pillars/nasa-daac-knowledge/issues/new?template=confirm_concept.yml&title=Confirm%3A+knowledge%2Flpdaac%2Fgotchas%2Fhls-scale-and-fill.md&concept=knowledge%2Flpdaac%2Fgotchas%2Fhls-scale-and-fill.md&product=HLS+S30+version+2.0%3A+Sentinel-2+nadir+BRDF-adjusted+surface+reflectance%2C+bandpass-adjusted+to+Landsat%2C+on+30+m+MGRS+tiles) |

## Concepts that name no product

Conventions, requirements, method concepts and anything whose claim is not about one product. The same link applies: confirm or correct.

None.
