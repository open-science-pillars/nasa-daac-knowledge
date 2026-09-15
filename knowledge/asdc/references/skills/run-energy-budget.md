---
type: Reference
spheres: [atmosphere, hydrosphere]
title: "Run instructions: attested energy budget closure"
description: "Executor instructions for the energy budget closure: the fixture command, the data-root layout for real inputs and which loader produces each file, where the Argo receipt comes from, the refusal rule, the attester command."
generated: { by: knowledge-seeder/claude, at: 2026-09-15T18:30:00Z }
status: draft
stale_after: 2027-03-15
---

# Run instructions: attested energy budget closure

The executor contract for
[the energy budget computation](../../computations/energy-budget.md):
a runner binds a VALUE for `window`, names the runtime that ran it,
and never edits the computation; the attester hashes it. Receipts and
verdicts are runtime artifacts, never committed to the bundle; nothing
is committed under a fixtures directory either, since the fixture is
generated at run time. The commands below run from the repository
root.

## 1. The fixture run

```bash
uv run knowledge/asdc/references/computations/energy_budget.py \
  --fixture --seed 7 --window 2006-01:2020-12 --runtime claude-code \
  --receipt /tmp/energy-budget-receipt.json
```

The fixture is regenerated deterministically from the seed (a
hash-based Gaussian stream, no numeric library in the path); its
digest is in the receipt and the attester regenerates it. Knobs:
`--seed N` (default 7) and `--capability-root DIR` for a package whose
golden invokes this executor and whose release the receipt is evidence
for (the `bundle` block always names this repository's package). The
headline line prints the four terms, the residual against the bar and
the verdict, and above it the anomaly trend with its interval against
the published one; the receipt carries exactly the declared fields,
with the series at full precision (the cos-latitude mean, the
product's geodetic mean, the per-month floor and the anomaly), the
five term blocks, the residual, the combined uncertainty, the verdict,
the energy over the window, the published imbalance, the bookkeeping
table, and on a fixture the planted truth beside what was recovered.

## 2. The refusal rule

A window the radiation record does not cover refuses:

```bash
uv run knowledge/asdc/references/computations/energy_budget.py \
  --fixture --seed 7 --window 1998-01:2005-12 --runtime claude-code \
  --receipt /tmp/refusal.json
echo $?   # 3, and the receipt says refused: true with the reason
```

The other refusals are an Argo receipt whose window is not the window
asked for (`ohc-window-mismatch`; the rate is a whole-window quantity),
an Argo receipt that is itself a refusal, fewer than 24 months in the
window, and a window mean or anomaly trend whose interval cannot be
stated. A refusal receipt attests PASS as a refusal (the verdict line
reads `PASS refusal`) and is never a number.

## 3. A data root, for a real run

The real run's tree is committed at
references/retrieval/energy-budget-root, built by the loader under
references/loaders (eb_ceres_ebaf.py for the EBAF file, with
`--selftest` on a synthetic grid and `--fetch` for the download) and
stamped by eb_data_root.py, which writes RECORD.json with the
bookkeeping table from the loader's stamp and the Argo receipt;
SOURCES.json records the download, the documents read and the
receipt's provenance. This is the layout the computation reads.
`--data-root DIR` in place of `--fixture`, with `--ohc-receipt PATH`
naming the Argo receipt (default `DIR/ohc-2000-receipt.json`):

```
DIR/
  RECORD.json             the stamp: record name, the manifest of every file,
                          manifest_sha256, verified_utc, the loader's stamp,
                          the Argo receipt's identity, and the bookkeeping
                          table under "bookkeeping"
  toa-net.csv             month,value_W_m2,uncertainty_W_m2,product_global_W_m2
                          one row per calendar month: the cos-latitude mean,
                          the per-month floor, the product's geodetic mean
  toa-net-stamp.json      what the loader read, from where, when, the product
                          version, the grid, the weights, the mask, the
                          aggregation, the anchoring, the cross-check between
                          the two weightings, the sha256 of the file read
  ohc-2000-receipt.json   the Argo ocean heat content receipt for the window
  SOURCES.json            every file read with its URL, hash and time, and
                          the receipt's provenance
```

Months are `YYYY-MM`, unique and in order. `bookkeeping` must carry
`anchoring.statement`, `weighting.statement`, `edition.statement`,
`uncertainty.basis` and `ocean_input.statement`, each a statement in
words; the executor refuses a stamp that lacks any of them, and checks
every file in the manifest against its hash before it reads a number.
The receipt copies the stamp, the file digests and the Argo receipt's
identity (its computation, code digest, run id, window, bundle and
record).

Which tool produces each file:

- `toa-net.csv` and `toa-net-stamp.json`: the loader, from the
  Edition 4.2.1 file. With `--fetch` it downloads a netCDF-4 subset
  of the granule through the ASDC OPeNDAP endpoint into the path
  `--product` names (outside the tree), first without credentials and
  then once with the Earthdata Login bearer token from
  `EARTHDATA_TOKEN` as a request header, which it never writes down;
  a full product file from the ordering tool works the same way:

  ```bash
  uv run knowledge/asdc/references/loaders/eb_ceres_ebaf.py --fetch \
    --product ~/ebaf-cache/CERES_EBAF_Edition4.2.1_200003-202605.subset.nc \
    --out DIR/toa-net.csv --stamp-out DIR/toa-net-stamp.json
  ```

- `ohc-2000-receipt.json`: the ocean-science plugin's computation on
  its committed data root, run in a clone of that plugin beside this
  repository, no network; its window must be the budget's window:

  ```bash
  uv run knowledge/references/computations/argo_ohc.py \
    --data-root knowledge/references/retrieval/argo-ohc-root \
    --window 2006-01:2020-12 --depth 2000 --runtime claude-code \
    --receipt DIR/ohc-2000-receipt.json
  uv run knowledge/references/attesters/argo_ohc_check.py DIR/ohc-2000-receipt.json \
    --data-root knowledge/references/retrieval/argo-ohc-root
  ```

- `RECORD.json`: the stamp assembler, after SOURCES.json is written:

  ```bash
  uv run knowledge/asdc/references/loaders/eb_data_root.py --root DIR --record NAME
  uv run knowledge/asdc/references/loaders/eb_data_root.py --root DIR --check
  ```

Then the run:

```bash
uv run knowledge/asdc/references/computations/energy_budget.py \
  --data-root knowledge/asdc/references/retrieval/energy-budget-root \
  --ohc-receipt knowledge/asdc/references/retrieval/energy-budget-root/ohc-2000-receipt.json \
  --window 2006-01:2020-12 --runtime claude-code --receipt /tmp/energy-budget-record.json
```

The data root and the receipt path are recorded package-relative when
they sit under this repository, so the run id reproduces on any
machine.

## 4. Attest the receipt

```bash
uv run knowledge/asdc/references/attesters/energy_budget_check.py /tmp/energy-budget-receipt.json \
  [--data-root DIR] [--out /tmp/attestation.json]
```

PASS requires every declared field, the sanctioned code hash, this
repository's package name, version and release lock digest in the
`bundle` block and a well-formed `capability` block, a named runtime,
the fixture regenerated at the receipt's seed hashing to the receipt's
digest (or, for a data root, the record, the files, the stamp and the
Argo receipt's identity present, and with `--data-root` hashing to the
tree), the months and the anomaly well formed, the window mean, the
anomaly trend, the four terms, the residual, the combined uncertainty,
the verdict, the energy over the window and the published distances
recomputed from the receipt, the bookkeeping complete with the
sanctioned anchor block, and the stated plausibility bounds, with the
known truth on the fixture. One line per check, `PASS name` or
`FAIL name: reason`, then the verdict line. `--out` writes the
attestation (verdict, refusal flag, digests, the capability, bundle
and runtime blocks, every check) for a qualification record.
`--selftest` runs the pass, the tampers, the wrong release, the
refusals, a synthetic data root and a fabricated one. The repository's
check routine runs the selftest, the fixture run and its refusal, the
loaders' selftests, the data root's manifest check and the record run
attested against the tree on every change.
