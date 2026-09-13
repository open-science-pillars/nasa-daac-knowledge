---
type: Reference
spheres: [hydrosphere, cryosphere]
title: "Run instructions: attested sea level budget closure"
description: "Executor instructions for the sea level budget closure: the fixture command, the data-root layout for real inputs and which loader produces each file, the refusal rule, the attester command."
generated: { by: knowledge-seeder/claude, at: 2026-09-13T21:00:00Z }
status: draft
---

# Run instructions: attested sea level budget closure

The executor contract for
[the sea level budget computation](../../computations/sea-level-budget.md):
a runner binds VALUES for `period` and, across the inter-mission gap,
`bridge`, names the runtime that ran it, and never edits the
computation; the attester hashes it. Receipts and verdicts are runtime
artifacts, never committed to the bundle; nothing is committed under a
fixtures directory either, since the fixture is generated at run time.

## 1. The fixture run (the reference, and the only run that exists)

```bash
uv run references/computations/sea_level_budget.py \
  --fixture --seed 7 --period 2005-01:2016-12 --runtime claude-code \
  --receipt /tmp/sea-level-budget-receipt.json
```

The fixture is regenerated deterministically from the seed (a
hash-based Gaussian stream, no numeric library in the path); its
digest is in the receipt and the attester regenerates it. Knobs:
`--seed N` (default 7), `--fixture-offset MM` (an inter-mission offset
injected into the mass series after the gap, zero by default), and
`--capability-root DIR` for a capability whose golden invokes this
executor and whose release the receipt is evidence for (the `bundle`
block always names this bundle). The headline line prints the residual
trend, the closure gap against the bar, and the verdict; the receipt
carries exactly the declared fields, with the three series, their
uncertainties and the residual at full precision, the four trend
blocks, the combined uncertainty, the verdict and the bookkeeping
table.

## 2. The refusal rule

A period that crosses the GRACE to GRACE-FO gap (mass months on both
sides of 2017-07 through 2018-05) refuses without `--bridge TEXT`, a
citation of the independent continuity evidence:

```bash
uv run references/computations/sea_level_budget.py \
  --fixture --period 2016-01:2019-12 --runtime claude-code \
  --receipt /tmp/refusal.json
echo $?   # 3, and the receipt says refused: true with the reason
```

The other refusals are a term with fewer than 24 months in the period,
a period outside the record, and a term whose interval the chain
refuses to state. A refusal receipt attests PASS as a refusal (the
verdict line carries the word refusal) and is never a number.

## 3. A data root, for a real run

The first real run's tree is committed at
references/retrieval/sea-level-budget-root, built by the loaders under
references/loaders (slb_altimetry_nasa_ssh.py for the NASA-SSH grids,
slb_steric_rg.py for the Roemmich and Gilson product, slb_mass_mascons.py
for the mascon grid, each with `--selftest`) and stamped by
slb_data_root.py, which writes RECORD.json with the corrections table
from the loaders' stamps; SOURCES.json records the downloads. This is
the layout the computation reads. `--data-root DIR` in place of
`--fixture`:

```
DIR/
  RECORD.json      the stamp: record name, manifest_sha256, verified_utc,
                   and the corrections table under "bookkeeping"
  altimetry.csv    month,value_mm,uncertainty_mm   one row per calendar month
  steric.csv       month,value_mm,uncertainty_mm
  mass.csv         month,value_mm,uncertainty_mm   missing months absent, never filled
```

Months are `YYYY-MM`, unique and in order; values are global means in
millimeters against each product's own baseline (the trend does not
care about the baseline, and the receipt records the values as read).
`bookkeeping` must carry `gia.altimetry`, `gia.mass`,
`inverse_barometer.altimetry`, `inverse_barometer.mass`,
`reference_frame.altimetry`, `reference_frame.mass`,
`effective_smoothing.altimetry`, `effective_smoothing.mass`,
`low_degree.mass`, `deep_steric.sampled_depth_floor_m` and
`deep_steric.steric_source`, each a statement in words read from the
product documentation at loading time; the executor refuses a stamp
that lacks any of them. The receipt copies the stamp and the three
file digests.

Which loader produces each file:

- `altimetry.csv`: the global mean per calendar month of the NASA-SSH
  simple grids in the stamped record
  ([the dataset concept](../../datasets/nasa-ssh.md) and the record
  note it cites), the grids of a month averaged (they share passes),
  the dynamic atmospheric correction as the product applies it.
- `steric.csv`: the ocean mean of a gridded Argo steric height
  (Roemmich and Gilson, or a successor) over its sampled depth range,
  the floor written into `deep_steric.sampled_depth_floor_m`.
  Regionally, from profiles through core's observations connector
  (`argo_search`, then `argo_profile` for each float and cycle): that
  loader lives outside the gate, since a gate never depends on a
  connector, and its output is the same CSV.
- `mass.csv`: the CRI-filtered mascon grids summed over the ocean
  mascons with their true areas and converted to millimeters of sea
  level equivalent per
  [the mass recipe](../../recipes/grace-mass-to-sea-level.md), the
  product's formal uncertainty combined per its guidance on
  correlated mascon errors; the months the product lacks are absent
  from the file.

## 4. Attest the receipt

```bash
uv run references/attesters/sea_level_budget_check.py /tmp/sea-level-budget-receipt.json \
  [--out /tmp/attestation.json]
```

PASS requires every declared field, the sanctioned code hash, this
bundle's package name, version and release lock digest in the
`bundle` block and a well-formed `capability` block, a named runtime,
the fixture regenerated at the receipt's seed hashing to the receipt's
digest (or the stamp for a data root), the series and the months used
and missing as the regenerated fixture yields them, every trend,
interval, formal error, the combined uncertainty and the verdict
recomputed from the series, the corrections table complete with the
gap handling agreeing with the months (a bridge where the period
crosses the gap), and on the fixture the known truth. `--out` writes
the attestation (verdict, refusal flag, digests, the capability,
bundle and runtime blocks, every check) for a qualification record.
`--selftest` runs the pass, the tampers, the wrong release, the
refusals and the stripped bridge. The repository's check routine runs
the selftest and the end-to-end fixture run and refusal on every
change.
