---
type: convention
title: "The OSNAP chapter: section masks from great-circle arcs"
description: "Tutorial-companion facts: transport and overturning along the approximate OSNAP lines via great-circle-arc masks, streamfunction in depth space, compared against OSNAP observations."
tags: [ecco, tutorial-companion, transport, osnap]
generated: { by: claude-code/fable-5, at: 2026-08-30T21:45:00Z }
status: draft
stale_after: 2027-01-04
sources:
  - id: tut-osnap
    resource: https://ecco-v4-python-tutorial.readthedocs.io/ECCO_v4_Example_OSNAP.html
    title: "ECCO v4 Python Tutorial: Compute MOC along the approximate OSNAP array from ECCO"
    author: team:ecco-consortium
---

# The OSNAP chapter: section masks from great-circle arcs

The chapter computes volumetric transport along the approximate OSNAP
lines in depth space and compares against the OSNAP observations: it
derives section masks as the great-circle arc between two points,
computes transport and the overturning streamfunction across the
section, and reports West, East, and Total averages with
uncertainties in Sverdrups.[^tut-osnap] Inputs are the geometry plus
the 3D volume and temperature flux collections
([volume-flux-3d](../fields/ecco-v4r4/volume-flux-3d.md),
[temperature-flux-3d](../fields/ecco-v4r4/temperature-flux-3d.md)).
The section machinery generalizes the 26.5N pattern owned by
[the MHT recipe](../recipes/ecco-mht-26n.md); no bundle concept yet
records OSNAP expected values, so the chapter is the sole cited source
for that comparison today.

[^tut-osnap]: ECCO v4 Python Tutorial: Compute MOC along the approximate OSNAP array from ECCO
