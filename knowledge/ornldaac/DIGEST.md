# What this bundle claims about your products

The `ornldaac` bundle, concept by concept, grouped by the product each one names. Rendered by `tools/digest.py` from the concepts' frontmatter; never edited by hand (the check routine fails when this page is stale).

If you know one of these products, each row's last link opens an issue with the concept and product filled in: say whether the claim is right, and correct it if not. Your answer is recorded on the concept as a verified event in your name, with a link to your reply. A row marked Asked already has an open issue (the maintainer asked someone); answer there.

## Summary

6 concepts, 1 products.

- unverified: 6
- machine-confirmed: 0
- human-reviewed: 0
- provider-confirmed: 0

A tier reads the concept's verified events: unverified (none), machine-confirmed (process events only), human-reviewed (a person signed), provider-confirmed (a person from the organization that produces the data confirmed it).

## Daymet Version 4 (release R1): daily surface weather on a 1 km grid for North America, Hawaii and Puerto Rico

[datasets/daymet-v4.md](datasets/daymet-v4.md): 6 concepts.

| Concept | Type | Severity | Status | Tier | Latest verified | Sources | |
|---|---|---|---|---|---|---|---|
| [Daymet Version 4 (release R1): daily surface weather on a 1 km grid for North America, Hawaii and Puerto Rico](datasets/daymet-v4.md) | dataset |  | draft | unverified |  | 12 | [Confirm or correct](https://github.com/open-science-pillars/nasa-daac-knowledge/issues/new?template=confirm_concept.yml&title=Confirm%3A+knowledge%2Fornldaac%2Fdatasets%2Fdaymet-v4.md&concept=knowledge%2Fornldaac%2Fdatasets%2Fdaymet-v4.md&product=Daymet+Version+4+%28release+R1%29%3A+daily+surface+weather+on+a+1+km+grid+for+North+America%2C+Hawaii+and+Puerto+Rico) |
| [Every Daymet year has 365 days: leap years keep February 29 and drop December 31, so a calendar-date join misaligns after February in a leap year](gotchas/daymet-365-day-year.md) | dataset-gotcha | high | draft | unverified |  | 4 | [Confirm or correct](https://github.com/open-science-pillars/nasa-daac-knowledge/issues/new?template=confirm_concept.yml&title=Confirm%3A+knowledge%2Fornldaac%2Fgotchas%2Fdaymet-365-day-year.md&concept=knowledge%2Fornldaac%2Fgotchas%2Fdaymet-365-day-year.md&product=Daymet+Version+4+%28release+R1%29%3A+daily+surface+weather+on+a+1+km+grid+for+North+America%2C+Hawaii+and+Puerto+Rico) |
| [The Daymet grid is Lambert conformal conic meters, not latitude and longitude: a cell is one square kilometer only on the standard parallels, and a lat/lon subset comes back as a projected box](gotchas/daymet-lcc-projection-and-cell-area.md) | dataset-gotcha | medium | draft | unverified |  | 5 | [Confirm or correct](https://github.com/open-science-pillars/nasa-daac-knowledge/issues/new?template=confirm_concept.yml&title=Confirm%3A+knowledge%2Fornldaac%2Fgotchas%2Fdaymet-lcc-projection-and-cell-area.md&concept=knowledge%2Fornldaac%2Fgotchas%2Fdaymet-lcc-projection-and-cell-area.md&product=Daymet+Version+4+%28release+R1%29%3A+daily+surface+weather+on+a+1+km+grid+for+North+America%2C+Hawaii+and+Puerto+Rico) |
| [Daymet values are interpolated from stations, and the error is not the domain average: station-sparse and high-relief regions carry larger error, which the cross-validation files quantify and the derived variables lack](gotchas/daymet-station-sparse-error.md) | dataset-gotcha | low | draft | unverified |  | 6 | [Confirm or correct](https://github.com/open-science-pillars/nasa-daac-knowledge/issues/new?template=confirm_concept.yml&title=Confirm%3A+knowledge%2Fornldaac%2Fgotchas%2Fdaymet-station-sparse-error.md&concept=knowledge%2Fornldaac%2Fgotchas%2Fdaymet-station-sparse-error.md&product=Daymet+Version+4+%28release+R1%29%3A+daily+surface+weather+on+a+1+km+grid+for+North+America%2C+Hawaii+and+Puerto+Rico) |
| [Tiles, mosaics and region files are three cuts of one estimate: the 2-degree tiles are mosaicked into the per-region files, and the three regions differ in extent, start year and service coverage](gotchas/daymet-tiles-mosaics-regions.md) | dataset-gotcha | medium | draft | unverified |  | 8 | [Confirm or correct](https://github.com/open-science-pillars/nasa-daac-knowledge/issues/new?template=confirm_concept.yml&title=Confirm%3A+knowledge%2Fornldaac%2Fgotchas%2Fdaymet-tiles-mosaics-regions.md&concept=knowledge%2Fornldaac%2Fgotchas%2Fdaymet-tiles-mosaics-regions.md&product=Daymet+Version+4+%28release+R1%29%3A+daily+surface+weather+on+a+1+km+grid+for+North+America%2C+Hawaii+and+Puerto+Rico) |
| [Version 4 R1 re-derived every 2020 and 2021 file with corrected Canadian station inputs and changed nothing else: a Version 4 file for those years is a different estimate under a different DOI](gotchas/daymet-v4-r1-correction.md) | dataset-gotcha | medium | draft | unverified |  | 6 | [Confirm or correct](https://github.com/open-science-pillars/nasa-daac-knowledge/issues/new?template=confirm_concept.yml&title=Confirm%3A+knowledge%2Fornldaac%2Fgotchas%2Fdaymet-v4-r1-correction.md&concept=knowledge%2Fornldaac%2Fgotchas%2Fdaymet-v4-r1-correction.md&product=Daymet+Version+4+%28release+R1%29%3A+daily+surface+weather+on+a+1+km+grid+for+North+America%2C+Hawaii+and+Puerto+Rico) |

## Concepts that name no product

Conventions, requirements, method concepts and anything whose claim is not about one product. The same link applies: confirm or correct.

None.
