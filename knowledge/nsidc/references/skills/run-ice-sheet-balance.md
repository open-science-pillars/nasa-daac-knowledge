---
type: Reference
spheres: [cryosphere]
title: "Run instructions: attested ice sheet mass balance closure"
description: "Executor instructions for the ice sheet mass balance closure: the fixture command, the data-root layout for real inputs and which loader produces each file, the refusal rule, the attester command."
generated: { by: knowledge-seeder/claude, at: 2026-09-15T20:00:00Z }
status: draft
stale_after: 2027-03-15
---

# Run instructions: attested ice sheet mass balance closure

The executor contract for
[the ice sheet mass balance computation](../../computations/ice-sheet-balance.md):
a runner binds VALUES for `ice_sheet`, `window`, `altimetry` and
`ice_density` (and, across the inter-mission gap, `bridge`), names the
runtime that ran it, and never edits the computation; the attester
hashes it. Receipts and verdicts are runtime artifacts, never
committed to the bundle; nothing is committed under a fixtures
directory either, since the fixture is generated at run time.

## 1. The fixture run (the reference)

```bash
uv run references/computations/ice_sheet_balance.py \
  --fixture --seed 7 --ice-sheet greenland --window 2019-01:2022-12 --altimetry atl15 \
  --runtime claude-code --receipt /tmp/ice-sheet-balance-receipt.json
```

The fixture is regenerated deterministically from the seed (a
hash-based Gaussian stream, no numeric library in the path); its
digest is in the receipt and the attester regenerates it. It carries a
Greenland-like sheet whose altimetric rate exceeds its gravimetric
rate by a planted +5 Gt per year, both altimetry products (a monthly
ITS_LIVE-shaped volume from 1992 and a quarterly ATL15-shaped one from
2019), firn uncertainties that cross zero, the mascon months the real
record lacks removed, and an Antarctic-like sheet with no grounded
firn term. Knobs: `--seed N` (default 7), `--altimetry itslive|atl15`
(default itslive), `--ice-density KG_M3` (default 917), and
`--capability-root DIR` for a capability whose golden invokes this
executor. The headline line prints the two rates, the residual against
the bar and the verdict; the receipt carries exactly the declared
fields, with the four series at full precision, the four rate blocks,
the combined uncertainty with the selection systematic stated
separately, the verdict and the bookkeeping table. A second fixture
run, `--window 2003-01:2016-12 --altimetry itslive`, is the long
monthly case the registry keeps beside it.

## 2. The refusal rule

A window outside the overlap of the terms the run needs refuses:

```bash
uv run references/computations/ice_sheet_balance.py \
  --fixture --ice-sheet greenland --window 2019-01:2025-12 --altimetry atl15 \
  --runtime claude-code --receipt /tmp/refusal.json
echo $?   # 3, and the receipt says refused: true with the reason
```

The other refusals: a window shorter than two years or a term with too
few epochs in it; an ice sheet whose firn term does not cover the
altimetry domain (`--ice-sheet antarctica` on this root, since the
firn term covers the floating ice shelves only); an altimetry product
the root does not carry (`--altimetry atl15` on the committed root);
a window whose mass months lie on both sides of the GRACE to GRACE-FO
gap (2017-07 through 2018-05) with no `--bridge TEXT`; and a rate
whose interval cannot be stated. A refusal receipt attests PASS as a
refusal (the verdict line reads `PASS refusal`) and is never a number.

## 3. A data root, for a real run

The real run's tree is committed at
references/retrieval/ice-sheet-balance-root, built by the loaders
under references/loaders (isb_firn_gemb.py and isb_smb_gemb.py for the
GEMB terms, isb_mass_mascons.py for the mascon grid,
isb_volume_itslive.py for the ITS_LIVE elevation change,
isb_volume_atl15.py for ATL15 when its granules can be fetched, each
with `--selftest`) and stamped by isb_data_root.py, which writes
RECORD.json with the bookkeeping and closure tables from the loaders'
stamps; SOURCES.json records the downloads and the granules that could
not be fetched. This is the layout the computation reads.
`--data-root DIR` in place of `--fixture`:

```
DIR/
  RECORD.json           the stamp: record name, manifest_sha256, verified_utc,
                        terms_present, terms_absent, the loaders' stamps and the
                        bookkeeping table with its closure section
  mass.csv              ice_sheet, domain (land_mascons), month, value_gt,
                        uncertainty_gt, ...   one row per ice sheet and solution month
  firn.csv              ice_sheet, domain, month, value_m, uncertainty_m, volume_km3,
                        area_km2, ...          the firn root of the earlier seed
  volume-itslive.csv    ice_sheet, domain, month, value_km3, uncertainty_km3,
                        uncertainty_correlated_km3, area_km2, ..., sampling, product
  volume-atl15.csv      the same columns from ATL15, quarterly; absent from the
                        committed root, and RECORD.json says why
  smb.csv               the surface mass balance term (ice shelves only; not read
                        by this computation)
  <term>-stamp.json     one stamp per term file
  SOURCES.json          the downloads, with URL, hash and time
```

Months are `YYYY-MM`, unique per ice sheet and domain; a quarterly row
is one product epoch labelled by its month. The executor reads only
these files, never a product file, and copies the RECORD summary, its
digest and the term file digests into the receipt; the data root is
recorded package-relative so the run id is the same on any machine.
`RECORD.json` must carry, under `bookkeeping`, the mass term's `gia`,
`low_degree`, `reference_frame`, `effective_smoothing`, `selection`
and `uncertainty_basis`, the volume term's `reference`, `mask`,
`uncertainty_basis` and `not_mass`, the firn term's `reference`,
`uncertainty_basis`, `gemb_version` and `forcing`, and a `closure`
table for both ice sheets; the attester refuses a receipt missing any
of them.

```bash
uv run references/computations/ice_sheet_balance.py \
  --data-root references/retrieval/ice-sheet-balance-root \
  --ice-sheet greenland --window 2003-01:2016-12 --altimetry itslive \
  --runtime claude-code --receipt /tmp/ice-sheet-balance-record.json
```

Which loader produces each file:

- `mass.csv`: the CRI-filtered mascon grid summed over the ice sheet's
  land mascons per solution month, in gigatonnes, with the per-mascon
  formal error in quadrature; the Greenland set is the land mascons
  whose land is at least a quarter Greenland ice by the ITS_LIVE mask,
  the Antarctic set every land mascon south of 60 S, and the stamp
  records the selection's sensitivity and the comparison with the
  provider's own series ([the mascon concept in the podaac bundle](../../../podaac/datasets/grace-fo-mascons.md)).
- `firn.csv` and `smb.csv`: the GEMB firn air content and surface
  mass balance terms of the earlier seed, unchanged in value.
- `volume-itslive.csv`: the ITS_LIVE surface elevation change summed
  to a volume anomaly over the same cell sets as the firn term
  (Greenland) and over the grounded Antarctic product's cells from
  2003 on ([the velocity and elevation change products](../../datasets/its-live-ice-velocity.md)
  are the same project's).
- `volume-atl15.csv`: the ATL15 10 km delta_h summed with ice_area
  ([the ATL15 concept](../../datasets/icesat2-atl15.md)); the loader
  needs an Earthdata Login and a route to the NSIDC cloud archive.

## 4. Attest the receipt

```bash
uv run references/attesters/ice_sheet_balance_check.py /tmp/ice-sheet-balance-receipt.json \
  [--data-root references/retrieval/ice-sheet-balance-root] [--out /tmp/attestation.json]
```

PASS requires every declared field, the sanctioned code hash, this
bundle's package name, version and release lock digest in the `bundle`
block and a well-formed `capability` block, a named runtime, the
fixture regenerated at the receipt's seed hashing to the receipt's
digest (or the RECORD stamp and file digests for a data root, checked
against the tree when `--data-root` is given), the four series well
formed with the altimetric mass equal to the density times the volume
less the firn air at every epoch and the firn uncertainties floored,
every rate, interval, formal error, the per-term uncertainties, the
selection systematic, the bar, the residual and the verdict recomputed
from the series, the bookkeeping complete with the gap handling
agreeing with the mass months, and on the fixture the known truth (on
a data root, each rate inside stated plausibility bounds). The output
is one `PASS name` or `FAIL name: reason` line per check and a verdict
line; `--out` writes the attestation for a qualification record.
`--selftest` runs the pass, the tampers, the wrong release, the
refusals, a bridged run across the gap, and the data-root path on the
fixture written as a root.
