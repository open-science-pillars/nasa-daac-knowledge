---
type: convention
title: "The llc compact binary format and read_llc_to_tiles"
description: "Tutorial-companion facts: MITgcm compact files pack the 13 tiles unintuitively; read_llc_to_tiles reorganizes them into the 13-tile layout."
tags: [ecco, tutorial-companion, binary, llc90]
generated: { by: claude-code/fable-5, at: 2026-08-30T21:40:00Z }
status: draft
stale_after: 2027-01-04
sources:
  - id: tut-compact
    resource: https://ecco-v4-python-tutorial.readthedocs.io/ECCO_v4_Loading_LLC_compact_binary_files.html
    title: "ECCO v4 Python Tutorial: Loading llc binary files in the compact format"
    author: team:ecco-consortium
---

# The llc compact binary format and read_llc_to_tiles

When the MITgcm writes diagnostics and other fields it uses the
compact format, which distributes the 13 lat-lon-cap tiles in a
non-obvious arrangement (the chapter shows the rearrangement into 5
faces); `ecco_v4_py.read_llc_to_tiles` reads compact files of any
dimension and reorganizes them into the familiar 13-tile
layout.[^tut-compact] This is the exact route the geothermal ancillary
file takes into heat budgets
([ecco-geothermal-flux](../gotchas/ecco-geothermal-flux.md) records
the trap; the sanctioned computation uses the same call), and the tile
geometry the layout lands on is
[the geometry concept](../fields/ecco-v4r4/geometry.md).

[^tut-compact]: ECCO v4 Python Tutorial: Loading llc binary files in the compact format
