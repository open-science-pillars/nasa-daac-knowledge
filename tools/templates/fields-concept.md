---
# Fields concept template (knowledge/podaac/fields/ecco-v4r4/<slug>.md)
# The <slug> MUST match a family slug in data/ecco_v4r4_families.yaml;
# add the family to the manifest first if it is new (single source of truth).
type: Data Collection
title: <family title from the manifest>
description: <one sentence: what the family carries and what it is for>
tags: [ecco, v4r4, <topical tags from the manifest>]
resource: https://podaac.jpl.nasa.gov/dataset/<PRIMARY_SHORTNAME>
status: draft
# generated.by: the actor that drafted this file (agent actor for scout
# drafts, human:<id> for hand authorship). Do not add a verified event
# yourself: verify_cmr.py --sign adds the process event when every
# ShortName checks out, and the steward adds the human event at promotion.
generated: { by: <actor>, at: <ISO 8601> }
stale_after: <YYYY-MM-DD, the next re-verification sweep>
sources:
  - id: podaac-landing
    resource: https://podaac.jpl.nasa.gov/dataset/<PRIMARY_SHORTNAME>
    title: PO.DAAC dataset landing page
  - id: cmr-sweep
    resource: all ECCO_L4_*V4R4* collections in CMR (provider POCLOUD)
    title: CMR ShortName sweep, tools/verify_cmr.py
  - id: variable-catalog
    resource: https://github.com/open-science-pillars/ocean-science/blob/main/skills/ecco/references/variable-catalog.md
    title: OSP ECCO variable catalog (sweep of 2026-07-04)
    author: human:PaulMRamirez
---

# <Family title>

<Two to four declarative sentences: what the family is, its role, its
period and grids. Facts only; no imperatives (SPEC 5.8). Cite sources
with [^id] footnotes.>

# Schema

<One row per variable. The first column MUST be the backticked variable
name (check_fields.py reads it). Provenance column values:
granule-verified YYYY-MM-DD, or user guide (verify at first load).>

| Variable | Units | Grid point | Description | Provenance |
|---|---|---|---|---|
| `<NAME>` | <units> | <c center / w face / s face / z corner> | <one line> | <provenance> |

# Variants

<One line per ShortName the family claims, cadence and grid stated;
V4R4B lines carry the release-mixing caveat as a fact.>

- `<SHORTNAME>`: <grid>, <cadence>.

# Known issues

<Links to the gotcha concepts that constrain this family, if any.>

[^podaac-landing]: PO.DAAC dataset landing page
