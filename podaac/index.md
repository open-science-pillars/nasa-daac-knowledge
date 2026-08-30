---
okf_version: "0.2"
---

# podaac bundle (CANONICAL, SPEC v0.6 §5.7)

The PO.DAAC arc knowledge bundle: ECCO, SWOT, GRACE-FO, GHRSST MUR.
OKF v0.2 conformant (okf_version: "0.2"; the vendored spec text lives in marketplace docs/upstream). This is the canonical home; the
ocean-science and hydrology plugins embed pinned snapshots of these
concepts (SPEC §5.7).

## datasets

- [ECCO v4 Release 4 ocean state estimate](datasets/ecco-v4r4.md), status: stable
- [SWOT KaRIn Level 2 Low Rate SSH](datasets/swot-karin.md), status: stable
- [GRACE/GRACE-FO JPL mascon solutions](datasets/grace-fo-mascons.md), status: stable
- [GHRSST MUR Level 4 SST](datasets/ghrsst-mur.md), status: stable
- [RAPID-MOCHA transports at 26.5N (observational reference)](datasets/rapid-mocha.md), status: stable (live-ingested Session 10)

## gotchas

- [ECCO budgets and transports close only on the native llc90 grid](gotchas/ecco-native-vs-regridded.md), severity high, status: stable
- [ECCO heat budgets need the geothermal flux, which is not a PO.DAAC collection](gotchas/ecco-geothermal-flux.md), severity high, status: stable
- [SWOT orbit phases: cal/val and science data are not one record](gotchas/swot-calval-orbit-phases.md), severity high, status: stable
- [GRACE mascon coastal leakage: land signal bleeds into ocean mascons](gotchas/grace-coastal-leakage.md), severity high, status: stable
- [GRACE GIA correction: a model choice already baked into the product](gotchas/grace-gia-correction.md), severity medium, status: stable
- [ECCO V4R4 vs V4R4B: mixing releases conflates corrections with signal](gotchas/ecco-release-mixing.md), severity high, status: stable
- [ECCO meridional heat transport: no basin mask means the full latitude circle](gotchas/ecco-mht-basin-scope.md), severity high, status: stable
- [SWOT KaRIn ssha_karin: crossover calibration arrives UNAPPLIED](gotchas/swot-crossover-unapplied.md), severity high, status: stable
- [ECCO native velocities are grid-relative: UVEL and VVEL are not east and north](gotchas/ecco-vector-orientation.md), severity high, status: draft

## recipes

- [Closed heat budget on the ECCO v4r4 native grid](recipes/ecco-heat-budget.md), status: stable
- [Meridional heat transport at 26.5N from ECCO v4r4](recipes/ecco-mht-26n.md), status: stable
- [Closed salt budget on the ECCO v4r4 native grid](recipes/ecco-salt-budget.md), status: stable
- [Closed volume budget on the ECCO v4r4 native grid](recipes/ecco-volume-budget.md), status: stable

## computations (OKF v0.2 section 10)

- [Heat budget closure on the ECCO v4r4 native grid (attested)](computations/ecco-heat-budget.md), status: stable
- [Salt budget closure on the ECCO v4r4 native grid (attested, draft)](computations/ecco-salt-budget.md), status: draft
- [Volume budget closure on the ECCO v4r4 native grid (attested, draft)](computations/ecco-volume-budget.md), status: draft
- [Meridional heat transport at 26.5N from ECCO v4r4 (attested, draft)](computations/ecco-mht-26n.md), status: draft
