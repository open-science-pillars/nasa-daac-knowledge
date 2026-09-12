---
type: field-state
spheres: [hydrosphere]
title: "Whether the Atlantic overturning has weakened over the observational era is disputed"
description: "Four positions on whether the Atlantic meridional overturning circulation has weakened since the mid twentieth century and where the direct record at 26.5N stands: a proxy fingerprint that reads a weakening, a 30-year reconstruction and the array record that show no decline, a reading of the proxy evidence as inconsistent, and an early-warning analysis that projects collapse. Read on 2026-09-05; the signature, when given, attests the state of discourse and takes no side."
tags: [ecco, amoc, rapid, overturning, discourse, field-state]
verified: { by: human:PaulMRamirez, at: 2026-09-06T00:34:32Z }
status: stable
load_bearing: medium
generated: { by: claude-code/fable-5, at: 2026-09-05T00:00:00Z }
stale_after: 2027-03-05
question: "Has the Atlantic meridional overturning circulation weakened over the observational era?"
as_of: 2026-09-05
state: disputed
positions:
  - id: fingerprint-weakening
    statement: "A sea surface temperature fingerprint (a cooling subpolar gyre beside a warming Gulf Stream region) indicates the overturning has weakened by about fifteen percent since the mid twentieth century"
    held_by: ["Caesar, Rahmstorf, Robinson, Feulner and Saba (2018)"]
    sources: [caesar-2018]
  - id: no-decline-at-26n
    statement: "A reconstruction of the overturning at 26.5N over 1981 to 2016 shows no decline, and the array record since 2004 shows a decline in its first decade followed by a pending recovery, consistent with decadal variability rather than a trend"
    held_by: ["Worthington and co-authors (2021)", "Moat and co-authors (2020)"]
    sources: [worthington-2021, moat-2020]
  - id: proxy-evidence-inconsistent
    statement: "The proxy reconstructions disagree with one another on the timing and sign of twentieth-century change, so the claim of a long-term weakening remains uncertain"
    held_by: ["Kilbourne and co-authors (2022)"]
    sources: [kilbourne-2022]
  - id: collapse-warning
    statement: "Early-warning statistics of the fingerprint series indicate an approach to a tipping point, with a collapse projected within this century"
    held_by: ["Ditlevsen and Ditlevsen (2023)"]
    sources: [ditlevsen-2023]
bears_on:
  - /computations/ecco-amoc-26n.md
  - /recipes/ecco-rapid-amoc-26n.md
sources:
  - id: caesar-2018
    resource: https://doi.org/10.1038/s41586-018-0006-5
    title: "Caesar, L., Rahmstorf, S., Robinson, A., Feulner, G., Saba, V. (2018). Observed fingerprint of a weakening Atlantic Ocean overturning circulation. Nature 556, 191 to 196"
  - id: worthington-2021
    resource: https://doi.org/10.5194/os-17-285-2021
    title: "Worthington, E. L., et al. (2021). A 30-year reconstruction of the Atlantic meridional overturning circulation shows no decline. Ocean Science 17, 285 to 299"
  - id: moat-2020
    resource: https://doi.org/10.5194/os-16-863-2020
    title: "Moat, B. I., et al. (2020). Pending recovery in the strength of the meridional overturning circulation at 26N. Ocean Science 16, 863 to 874"
  - id: kilbourne-2022
    resource: https://doi.org/10.1038/s41561-022-00896-4
    title: "Kilbourne, K. H., et al. (2022). Atlantic circulation change still uncertain. Nature Geoscience 15, 165 to 167"
  - id: ditlevsen-2023
    resource: https://doi.org/10.1038/s41467-023-39810-w
    title: "Ditlevsen, P., Ditlevsen, S. (2023). Warning of a forthcoming collapse of the Atlantic meridional overturning circulation. Nature Communications 14, 4254"
---

# Whether the Atlantic overturning has weakened over the observational era is disputed

# Question

Has the Atlantic meridional overturning circulation weakened over the
observational era? The question is asked of the bundle whenever a
reader computes the overturning at 26.5N from the model and wants to
know what a trend in it would mean. This concept records where the
field stands on the date above. It does not answer the question, and a
signature on it does not either.

# Positions

Caesar and co-authors read a weakening of about fifteen percent since
the mid twentieth century from a sea surface temperature fingerprint,
a cooling subpolar gyre beside a warming Gulf Stream region, calibrated
against a model ensemble.[^caesar-2018]

Worthington and co-authors reconstruct the overturning at 26.5N over
1981 to 2016 from hydrographic and other observations and find no
decline; Moat and co-authors, reading the array record from 2004, find
a decline in the first decade followed by a pending recovery, which they
place within decadal variability rather than a
trend.[^worthington-2021][^moat-2020]

Kilbourne and co-authors argue that the proxy reconstructions disagree
with one another on the timing and sign of twentieth-century change, so
the evidence for a long-term weakening is inconsistent and the question
stays open.[^kilbourne-2022]

Ditlevsen and Ditlevsen apply early-warning statistics to the
fingerprint series and report an approach to a tipping point, with a
collapse projected within this century; the method and the projection
are contested within the field, and the position is recorded here as
held, not as accepted.[^ditlevsen-2023]

# Bearing

The bundle produces the model's overturning at 26.5N month by month
over 1992 to 2017 and confronts it with the array over 2004 to 2017,
where the model runs about three sverdrups low with a correlation near
0.8. A trend fitted to the model's 26-year series sits inside the
disputed period, and a reader who quotes such a trend as evidence for
or against weakening has taken a side in this dispute without saying
so. The bearing is on how the transport and the confrontation are
voiced: as the model's own record and its agreement with one array,
never as a verdict on the observational-era question.

# What would move this

A longer direct record at 26.5N (the array now spans two decades), a
reconciliation of the proxy reconstructions with one another, or an
independent transport record at another latitude that agrees with one
position over the others. Any of these changes the state; a change in
the state is a new field-state that supersedes this one, never an edit
of this one after signature.

[^caesar-2018]: Caesar et al. (2018), Nature, doi:10.1038/s41586-018-0006-5
[^worthington-2021]: Worthington et al. (2021), Ocean Science, doi:10.5194/os-17-285-2021
[^moat-2020]: Moat et al. (2020), Ocean Science, doi:10.5194/os-16-863-2020
[^kilbourne-2022]: Kilbourne et al. (2022), Nature Geoscience, doi:10.1038/s41561-022-00896-4
[^ditlevsen-2023]: Ditlevsen and Ditlevsen (2023), Nature Communications, doi:10.1038/s41467-023-39810-w
