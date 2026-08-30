---
type: convention
title: "Gradients and curl on the native llc grid"
description: "Tutorial-companion facts: tile x/y axes do not align with parallels and meridians; SN and CS take their expected values on unrotated tiles; edge connectivity drives native differencing."
tags: [ecco, tutorial-companion, grid, llc90]
generated: { by: claude-code/fable-5, at: 2026-08-30T21:45:00Z }
status: draft
stale_after: 2027-01-04
sources:
  - id: tut-grad
    resource: https://ecco-v4-python-tutorial.readthedocs.io/ECCO_v4_Gradient_calc_on_native_grid.html
    title: "ECCO v4 Python Tutorial: Calculating gradients and curl on the ECCO native grid (Fenty, Delman ed.)"
    author: team:ecco-consortium
---

# Gradients and curl on the native llc grid

Some of the 13 llc tiles are rotated relative to each other, and the
model x and y axes do not align with parallels and meridians, so zonal
and meridional gradients require the rotation machinery: the chapter
plots `SN` and `CS` and shows they take the expected values on the
unrotated tiles (sin of theta 0 and cos of theta 1 where theta is
zero), and it works the logical connection between geographically
adjacent tile edges that native differencing relies
on.[^tut-grad] The rotation fields themselves are granule-verified on
[the geometry concept](../fields/ecco-v4r4/geometry.md), and the
misuse trap is
[ecco-vector-orientation](../gotchas/ecco-vector-orientation.md).

[^tut-grad]: ECCO v4 Python Tutorial: Calculating gradients and curl on the ECCO native grid (Fenty, Delman ed.)
