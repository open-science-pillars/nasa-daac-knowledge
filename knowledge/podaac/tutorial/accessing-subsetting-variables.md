---
type: convention
title: "Accessing and subsetting ECCO variables"
description: "Tutorial-companion pointer: dot and dictionary access, and the bracket, sel, isel, and where subsetting routes; xarray-generic procedure with no ECCO-specific trap."
tags: [ecco, tutorial-companion, loading]
generated: { by: claude-code/fable-5, at: 2026-08-30T21:45:00Z }
status: draft
stale_after: 2027-01-04
sources:
  - id: tut-subset
    resource: https://ecco-v4-python-tutorial.readthedocs.io/ECCO_v4_Accessing_and_Subsetting_Variables.html
    title: "ECCO v4 Python Tutorial: Accessing and Subsetting Variables"
    author: team:ecco-consortium
---

# Accessing and subsetting ECCO variables

The chapter teaches the two access methods (dot and dictionary, with
attributes needing their own route) and the four subsetting syntaxes
(brackets, `sel`, `isel`, `where`) on ECCO Datasets and
DataArrays.[^tut-subset] These are xarray-generic procedures; the
chapter states no ECCO-specific dataset fact beyond its worked
ShortNames, so this companion is deliberately a cited pointer rather
than a restatement (the single-source rule; procedure lives with the
tutorial and the skills layer).

[^tut-subset]: ECCO v4 Python Tutorial: Accessing and Subsetting Variables
