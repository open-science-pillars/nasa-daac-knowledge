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
- [RAPID-MOCHA transports at 26.5N (observational reference)](datasets/rapid-mocha.md), status: stable

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
- [Curl on the native grid needs a SECOND rotation](gotchas/ecco-curl-second-rotation.md), severity high, status: stable
- [MASS-suffixed velocities are already mass-weighted: hFac double-counts](gotchas/ecco-velmass-hfac-double-count.md), severity high, status: stable
- [Geostrophic velocity needs the density factor](gotchas/ecco-geostrophic-density-factor.md), severity high, status: stable
- [Daily granules overlap at midnight](gotchas/ecco-daily-granule-midnight-overlap.md), severity medium, status: stable
- [Geostrophic velocity from PHIHYD alone omits the surface pressure](gotchas/ecco-phihyd-surface-pressure.md), severity high, status: stable
- [A trend fit without an effective-sample-size correction overstates certainty](gotchas/ecco-trend-without-effective-n.md), severity high, status: draft
- [Deseasonalize jointly with the trend, or the climatology keeps part of it](gotchas/ecco-trend-deseasonalize-jointly.md), severity high, status: draft

## recipes

- [Geostrophic velocity and thermal wind on the native grid](recipes/ecco-geostrophic-balance.md), status: stable
- [Closed heat budget on the ECCO v4r4 native grid](recipes/ecco-heat-budget.md), status: stable
- [Meridional heat transport at 26.5N from ECCO v4r4](recipes/ecco-mht-26n.md), status: stable
- [Closing a heat budget over a region of ECCO v4r4](recipes/ecco-regional-heat-budget.md), status: stable
- [Transport across a section of the ECCO v4r4 native grid](recipes/ecco-section-transport.md), status: stable
- [Splitting a flux into mean and eddy parts without an argument](recipes/ecco-flux-decomposition.md), status: stable
- [Global ocean heat content and its change from ECCO v4r4](recipes/ecco-ocean-heat-content.md), status: stable
- [Closed salt budget on the ECCO v4r4 native grid](recipes/ecco-salt-budget.md), status: stable
- [Steric height and its trend from ECCO v4r4 density](recipes/ecco-steric-height.md), status: stable
- [Closed volume budget on the ECCO v4r4 native grid](recipes/ecco-volume-budget.md), status: stable
- [Wind-stress curl and Ekman pumping on the native grid](recipes/ecco-wind-stress-curl.md), status: stable
- [A trend with an honest interval from any ECCO monthly series](recipes/ecco-trend-ci.md), status: draft
- [ECCO overturning at 26.5N confronted with the RAPID array](recipes/ecco-rapid-amoc-26n.md), status: stable (the first confrontation pair: the other side is an observation at a fixed version)
- Sea level from altimetry against ECCO SSH: the second confrontation pair, queued and not built; no recipe, computation or attester exists for it yet and nothing states a score

## tutorial companion (every claim footnotes its tutorial page)

- [The ecco_access library](tutorial/ecco-access-library.md), status: draft
- [Batch downloading with wget](tutorial/wget-download.md), status: draft
- [ECCO in the Earthdata Cloud on AWS](tutorial/aws-cloud-access.md), status: draft
- [NetCDF structure: datasets, granules, xarray objects](tutorial/data-structure-basics.md), status: draft
- [Coordinates and dimensions](tutorial/coordinates-and-dimensions.md), status: draft
- [Loading the grid parameters](tutorial/loading-grid-parameters.md), status: draft
- [Loading state estimate fields](tutorial/loading-state-estimate-fields.md), status: draft
- [The llc compact binary format](tutorial/llc-compact-binaries.md), status: draft
- [Combining datasets across grid points](tutorial/combining-datasets.md), status: draft
- [Accessing and subsetting variables](tutorial/accessing-subsetting-variables.md), status: draft
- [Interpolating llc90 fields to lat-lon](tutorial/interpolating-to-latlon.md), status: draft
- [Gradients and curl on the native grid](tutorial/gradients-and-curl.md), status: draft
- [Heat budget: the tutorial's checkpoints](tutorial/ecco-heat-budget-tutorial-checkpoints.md), status: draft
- [Volume and sea level budget: the tutorial's checkpoints](tutorial/ecco-volume-budget-tutorial-checkpoints.md), status: draft
- [Salt budgets: the tutorial's checkpoints](tutorial/ecco-salt-budget-tutorial-checkpoints.md), status: draft
- [The MHT chapter: scope machinery and a constants inconsistency](tutorial/ecco-mht-tutorial-example.md), status: draft
- [The OSNAP chapter: great-circle section masks](tutorial/ecco-osnap-tutorial-example.md), status: draft
- [Thermal forcing direct from S3: the in-region rule](tutorial/ocean-thermal-forcing-s3.md), status: draft

## conventions

- [Marine heatwave definition (Hobday family)](conventions/mhw-definition-hobday.md), status: draft
- [Consistency versus confrontation](conventions/consistency-versus-confrontation.md), status: stable

## computations (OKF v0.2 section 10)

- [Heat budget closure on the ECCO v4r4 native grid (attested)](computations/ecco-heat-budget.md), status: stable
- [Salt budget closure on the ECCO v4r4 native grid (attested, draft)](computations/ecco-salt-budget.md), status: draft
- [Volume budget closure on the ECCO v4r4 native grid (attested, draft)](computations/ecco-volume-budget.md), status: draft
- [Meridional heat transport at 26.5N from ECCO v4r4 (attested, draft)](computations/ecco-mht-26n.md), status: draft
- [Regional sea level partition from ECCO (attested)](computations/ecco-regional-sea-level.md), status: draft
- [Global ocean heat content from ECCO v4r4 (attested)](computations/ecco-ocean-heat-content.md), status: stable
- [Regional steric height from ECCO v4r4 (attested)](computations/ecco-steric-height.md), status: stable
- [Geostrophic balance and thermal wind from ECCO v4r4 (attested)](computations/ecco-geostrophic-balance.md), status: stable
- [Wind-stress curl and Ekman pumping from ECCO v4r4 (attested)](computations/ecco-wind-stress-curl.md), status: stable
- [Regional heat budget over a control volume from ECCO v4r4 (attested)](computations/ecco-regional-heat-budget.md), status: stable
- [Section transports on the ECCO v4r4 native grid (attested)](computations/ecco-section-transport.md), status: stable
- [Regional salt budget over a control volume from ECCO v4r4 (attested)](computations/ecco-regional-salt-budget.md), status: stable
- [Regional volume budget over a control volume from ECCO v4r4 (attested)](computations/ecco-regional-volume-budget.md), status: stable
- [Reynolds flux decomposition from ECCO v4r4 (attested)](computations/ecco-flux-decomposition.md), status: stable
- [Linear trend with an honest interval from a monthly series (attested)](computations/ecco-trend-ci.md), status: draft
- [Atlantic overturning at 26.5N from ECCO v4r4 (attested)](computations/ecco-amoc-26n.md), status: stable
- [ECCO overturning against RAPID at 26.5N (attested)](computations/ecco-rapid-amoc-confrontation.md), status: stable

## validity-domains

- [Exclusion: budget claims on interpolated ECCO grids](validity-domains/no-budgets-on-interpolated.md), exclusion, status: draft
- [ECCO v4r4 native monthly fields support large-scale statistics over 1992-2017](validity-domains/ecco-large-scale-statistics.md), supporting, status: draft
- [MUR L4 SST supports basin-scale mean-state claims outside the high Arctic](validity-domains/mur-basin-mean-state.md), supporting, status: draft

## connectors

- [NASA Earthdata MCP server (CMR discovery, no login)](connectors/earthdata-mcp.md), status: draft
