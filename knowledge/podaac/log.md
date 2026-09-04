# podaac-arc bundle: change log

Newest first. One line per change: date, concept path, what changed, who.

_Historical note: older entries use build-era shorthand (a "close lint" is a knowledge-linter pass; red/yellow marks are nonconformant/advisory findings; check numbers refer to the linter checks documented in core/agents/knowledge-linter). The decision chains, not the labels, are what teach the standards._

- 2026-09-04 · STEWARD SIGNING: the steward read every diff against
  the last-signed text and signed all 33 at 20:45:44Z. Promoted from
  draft to stable: conventions/ecco-budget-formulation and
  gotchas/ecco-access-static-collections. Re-signed after the
  re-sourcing pass: the three computations (ecco-heat-budget,
  ecco-ocean-heat-content, ecco-section-transport), datasets/ecco-v4r4
  and datasets/swot-karin, the ten fields/ecco-v4r4 concepts, gotchas
  ecco-geothermal-flux, ecco-mht-basin-scope, ecco-native-vs-regridded,
  ecco-release-mixing, swot-calval-orbit-phases and
  swot-crossover-unapplied, and the five recipes (ecco-heat-budget,
  ecco-mht-26n, ecco-salt-budget, ecco-section-transport,
  ecco-volume-budget). Re-signed after their migration: the five
  concepts that moved in from ocean-science. stale_after left as it
  stood on the re-signs, as at the previous mass re-sign. The five
  trend and regional sea level drafts stay drafts. Index rows for the
  two promotions now read stable. (human:PaulMRamirez, recorded by the
  build assistant)
- 2026-09-04 · gotchas/ecco-ssh-ib-variants, gotchas/ecco-boussinesq-global-steric,
  gotchas/ecco-native-density-eos, gotchas/ecco-mxldepth-criterion and
  conventions/sea-level-budget-closure: the five concepts that moved in
  from the ocean-science plugin leave the legacy `timestamp` and
  `evidence` keys behind for the bundle's `generated` and `sources`
  form (the checker's W7 count falls from 10 to 0). Each now cites a
  durable authority with footnotes: the SSH fields concept for the IB
  variants; Greatbatch (1994) and the attested steric computation for
  the Boussinesq caveat; the density collection's own RHOAnoma and
  DRHODR attributes (a modified UNESCO equation of state driven by
  potential temperature at constant pressure, read from the 2009-12
  granule) plus TEOS-10 for the native EOS; the WCRP (2018) budget
  paper for closure; the mixed-layer collection's own MXLDEPTH
  attributes (the Kara et al. 2000 temperature criterion, 0.8 degrees C
  colder than the surface) plus Kara et al. for the MLD criterion,
  which the body now states exactly instead of "generally not". The
  native EOS gotcha's verification paragraph no longer claims a pending
  reproducing check as if the concept were a draft: it says what was
  read from the granule and that no recomputed-versus-shipped check
  exists here yet. Plugin-internal comments (harness rules, plugin
  evals paths) removed. Signatures untouched; all five owe a re-sign at
  the sitting, as they already did. (build assistant)
- 2026-09-04 · CANONICAL CONTENT DRAFTS: this bundle takes over the
  ECCO knowledge that lived only in the ocean-science plugin, and
  every provider concept that cited a plugin file now cites a durable
  authority instead (the rows below; the W9 count of the checker falls
  from 26 to 4, the four survivors being pinned commit URLs to files
  that stay with the plugin by design). Nothing signed here: 27 stable
  concepts changed text (26 of this bundle and one moved-in gotcha) and
  await a steward re-sign; the four byte-identical moves keep their
  signatures (build assistant)
- 2026-09-04 · conventions/ecco-budget-formulation.md (draft): the
  constants, term definitions, sign conventions and discretization
  shared by the heat, salt and volume budgets, sourced to the ECCO
  tutorial notebooks and the sanctioned heat budget code; tolerances
  and residuals stay with the computations and recipes (build
  assistant)
- 2026-09-04 · seven concepts re-sourced from the plugin's formulation
  reference to the convention (computations ecco-heat-budget and
  ecco-ocean-heat-content, gotchas ecco-geothermal-flux and
  ecco-native-vs-regridded, recipes ecco-heat-budget, ecco-salt-budget,
  ecco-volume-budget); the heat baseline paragraph cites the in-bundle
  attester; re-sign owed on all seven (build assistant)
- 2026-09-04 · gotchas/ecco-ssh-ib-variants.md moved into this bundle
  byte-identical from ocean-science at 14a4eea, signature carried as it
  stands (build assistant)
- 2026-09-04 · gotchas/ecco-boussinesq-global-steric.md moved into this
  bundle byte-identical from ocean-science at 14a4eea, signature
  carried as it stands (build assistant)
- 2026-09-04 · gotchas/ecco-native-density-eos.md moved into this
  bundle byte-identical from ocean-science at 14a4eea, signature
  carried as it stands (build assistant)
- 2026-09-04 · conventions/sea-level-budget-closure.md moved into this
  bundle byte-identical from ocean-science at 14a4eea, signature
  carried as it stands (build assistant)
- 2026-09-04 · gotchas/ecco-mxldepth-criterion.md moved into this
  bundle from ocean-science at 14a4eea; its mld-criteria link now pins
  that commit because the MLD criteria convention stays with the
  plugin; re-sign owed (build assistant)
- 2026-09-04 · gotchas/ecco-access-static-collections.md (draft): the
  ecco_access static-collection quirk gets its own concept, sourced to
  the observation record, the ecco-access 0.3.1 release and the
  tutorial access and grid pages; datasets/ecco-v4r4.md and
  fields/ecco-v4r4/geometry.md link it instead of restating it (build
  assistant)
- 2026-09-04 · datasets/ecco-v4r4.md: a Citation section records the
  PO.DAAC prescribed form and ecco_cite --selftest checks its template
  against it; ShortName authority is now the fields index; the hFac
  double-count and static-collection gotchas linked from Structure,
  Access and Known issues; re-sign owed (build assistant)
- 2026-09-04 · fields/ecco-v4r4/geometry.md: the plugin variable
  catalog source retired; the granule name cited to the CMR granule
  record, the merge and coordinate facts to the tutorial pages, the
  access quirk to its gotcha; re-sign owed (build assistant)
- 2026-09-04 · nine ECCO fields concepts (fresh-flux, heat-flux, obp,
  ocean-vel, salinity-flux-3d, ssh, temp-salinity, temperature-flux-3d,
  volume-flux-3d) re-sourced: the plugin variable catalog gives way to
  the family manifest (tools/ecco_v4r4_families.yaml) for the
  granule-verified enumerations, the CMR sweep for ShortName facts, and
  the ECCO tutorial notebooks for the z* scale factor, the geothermal
  ancillary input and the hFac weighting in the MASS velocities;
  temp-salinity dims re-verified against the manifested 2010 fixtures;
  re-sign owed on all nine (build assistant)
- 2026-09-04 · gotchas/ecco-release-mixing.md and recipes/ecco-mht-26n.md
  cite the in-bundle fields concepts instead of the plugin catalog;
  gotchas/ecco-mht-basin-scope.md drops an uncited catalog source;
  re-sign owed on all three (build assistant)
- 2026-09-04 · computations/ecco-section-transport.md and
  recipes/ecco-section-transport.md pin their ocean-science citations
  (the independent transport_analysis.py implementation and the
  meridional-transport skill) to commit 14a4eea; the computation also
  cites the in-bundle recipe for the 1.098 PW anchor; re-sign owed
  (build assistant)
- 2026-09-04 · datasets/swot-karin.md gains a Variants section: ten
  KaRIn L2 LR SSH collections and 22 nadir altimeter collections
  verified by a public CMR sweep with concept ids and DOIs, plus a
  per-family granule holdings probe (Version C from cycle 001 on
  2023-07-26, Version D from cycle 473 on 2023-03-27, the cal/val phase
  only in D); re-sign owed (build assistant)
- 2026-09-04 · gotchas/swot-calval-orbit-phases.md re-sourced: the
  orbit timeline and cycle ranges cite the Version D release note
  (Table 2, section 3), the probe evidence cites the dataset concept;
  re-probed 2026-09-04; re-sign owed (build assistant)
- 2026-09-04 · gotchas/swot-crossover-unapplied.md re-sourced: the
  unapplied height_cor_xover cites the L2_LR_SSH product description
  (D-56407 Rev C, 4.1.8) and the Version D release note known issues;
  the unused plugin citation removed; re-sign owed (build assistant)
- 2026-09-04 · the trend-ci computation, its recipe and the two trend
  gotchas cite computations/ecco-steric-height.md for the full-record
  steric trend and interval instead of quoting the digits; the steric
  and partition receipts own the record, the trend-ci family states
  only its own 2010 reference run (build assistant)
- 2026-09-04 · computations/ecco-regional-sea-level.md sources the sea
  level budget closure convention and the SSH inverse-barometer gotcha
  from this bundle (conventions/sea-level-budget-closure.md,
  gotchas/ecco-ssh-ib-variants.md) instead of the plugin (build
  assistant)
- 2026-09-04 · connectors/earthdata-mcp.md (draft): the local-smoke source
  now cites tools/mcp_smoke.py by path, the tool having landed in this
  repository; the DOI mapping gains its check, ecco_cite --selftest
  cross-checks every DOI quoted in the fields concepts and the family
  manifest against tools/ecco_v4r4_dois.yaml (build assistant)
- 2026-09-03 · steward review passed: nineteen stable concepts whose text
  had been edited after their signatures, measured against each one's
  signing commit, re-verified (verified_by human:PaulMRamirez); each
  verified event is refreshed to the re-review, status stays stable.
  computations/ecco-geostrophic-balance.md, ecco-heat-budget.md,
  ecco-ocean-heat-content.md, ecco-regional-salt-budget.md,
  ecco-regional-volume-budget.md, ecco-section-transport.md and
  ecco-wind-stress-curl.md: the receipt `data` block and its
  provenance paragraph (the verified-tree stamp the attester requires).
  fields/ecco-v4r4/fresh-flux.md, geometry.md, heat-flux.md, obp.md,
  ocean-vel.md, salinity-flux-3d.md, ssh.md, temp-salinity.md,
  temperature-flux-3d.md and volume-flux-3d.md: the per-collection DOI
  on every ShortName row; ocean-vel.md also its Known issues section
  pointing at the vector-orientation gotcha. datasets/ecco-v4r4.md:
  the trend-without-effective-n gotcha added to its gotcha list.
  recipes/ecco-mht-26n.md: reader-facing wording of its provenance
  paragraph. Applied on the steward's explicit instruction, per the
  merge-then-sign rule; this clears the backlog, so from here a stable
  concept's last content commit precedes or is its signing commit.
- 2026-09-03 · steward review passed: the seven stable concepts edited
  in the bundle move re-verified (verified_by human:PaulMRamirez); each
  verified event is refreshed to the re-review, status stays stable.
  datasets/rapid-mocha.md, recipes/ecco-rapid-amoc-26n.md,
  computations/ecco-amoc-26n.md,
  computations/ecco-rapid-amoc-confrontation.md and
  recipes/ecco-regional-heat-budget.md carried path-only edits (shell
  examples and docs links). computations/ecco-flux-decomposition.md
  and computations/ecco-regional-heat-budget.md additionally carried
  the receipt `data` block (the verified-tree stamp) and, for the heat
  budget, the stated-units rule, both merged after their 2026-09-01
  signatures and covered by this review. Applied on the steward's
  explicit instruction after the merge, per the merge-then-sign rule.
- 2026-09-03 · bundle moved from podaac/ to knowledge/podaac/ (git mv)
  so each OSP repository keeps its bundle under knowledge/. Code and
  receipts under references/ are byte-identical (shas unchanged);
  the only concept edits are repository-relative paths in shell
  examples and links to docs/, which gain the extra level. Paths
  written as podaac/... in entries and commit-pinned links below
  resolve at their commits; the live path is knowledge/podaac/... ·
  steward
- 2026-09-03 · index.md findings section refined: each entry carries
  the finding's ladder position and confrontation kind so consumers can
  voice both; tools/run_checks.sh now runs check_okf_v02 with
  --findings for this bundle, so the finding checks are part of the
  gate from here on. Claude Code.
- 2026-09-02 · findings/us-northeast-sea-level-rise.md ADDED, status
  draft, the bundle's first finding: the regional sea level partition
  over the box 35 to 45N, 75 to 65W (total 5.25 mm/yr [4.06, 6.43],
  manometric 2.45 [2.17, 2.74], steric 2.80 [1.51, 4.09], 95 percent,
  from references/retrieval/exhibit-sea-level-record.json), verdict
  UNADJUDICATED (references/retrieval/fitness-sea-level-record.json,
  the governing domain is unsigned), confronted against NASA-SSH V1.1
  with independence stated as low (the estimate was fitted to these
  missions). Every number in it resolves to a receipt leaf under the
  findings checker. Signature is the steward's. Claude Code.
- 2026-09-02 · computations/ecco-ssh-vs-altimetry.md ADDED, status
  draft, the second confrontation pair: ECCO box-mean sea level
  against the NASA-SSH V1.1 simple grid over 1993-01 to 2017-12 (300
  months). Executor references/computations/ecco_ssh_vs_altimetry.py
  (reads the partition's region registry from source without importing
  it; records the empty grids in the box), attester
  references/attesters/altimetry_confrontation_check.py (re-hashes the
  tree, re-derives the model side from the partition receipt,
  recomputes every score; PASS on the reference receipt, FAIL on five
  doctored variants). Scores in
  references/retrieval/exhibit-ssh-vs-altimetry-record.json: r 0.91
  [0.84, 0.95], RMSD 29.3 mm, trend difference +1.99 mm/yr [1.39,
  2.59], ECCO 5.18 against altimetry 3.19. Eight globally empty grids
  thin four months to two or three grids, so the reference run binds
  min grids two. The index recipe line that said "queued and not
  built" now points at the computation. Claude Code.
- 2026-09-02 · datasets/nasa-ssh.md ADDED, status draft, the NASA-SSH
  V1.1 simple gridded SSHA record as an observational reference (DOI
  10.5067/NSREF-SG0V11, 1315 weekly grids 1992-10-26 to 2018-01-01,
  CC BY 4.0), with docs/nasa-ssh-record.md (tree, manifest, verification,
  the eight empty grids, terms), references/retrieval/nasa-ssh-manifest.json
  and nasa-ssh-verification.json. tools/obs_record_fetch.py ADDED
  (CMR-listed granule fetch with MD5 sidecar verification, netrc for
  retrieval only) and tools/obs_record_manifest.py generalized (version
  from product_version, DOI from id, scalar time; RAPID manifest
  regression identical). Claude Code.
- 2026-09-02 · steward review passed: recipes/ecco-rapid-amoc-26n.md,
  conventions/consistency-versus-confrontation.md,
  computations/ecco-amoc-26n.md and
  computations/ecco-rapid-amoc-confrontation.md verified (verified_by
  human:PaulMRamirez, applied on the steward's explicit instruction),
  status draft to stable; datasets/rapid-mocha.md re-verified after
  its post-signature edits (the release on record, two gotchas, the
  pointer to the recipe), the verified event refreshed to the
  re-review. The scores those concepts state were shown to the steward
  at the measurement before any concept stated them. (claude, for the
  steward)
- 2026-09-02 · THE FIRST CONFRONTATION, STATED. recipes/ecco-rapid-amoc-26n.md
  (new, draft, unsigned): the model's Atlantic overturning at 26.5N
  beside the RAPID array's delivered record over 2004-04 through
  2017-12 (165 months). Colocation: calendar-month means of the
  twelve-hourly ten-day-filtered series (a month enters at half its
  samples valid) against the model's monthly-mean streamfunction
  maximum under the array's own zero-net convention, Atlantic scope,
  face row 26.1N; the array's methodology papers cited (McCarthy et
  al. 2015, Cunningham et al. 2007, Kanzow et al. 2007, DOIs verified
  against Crossref). Representativeness in both directions, with the
  western boundary measured: the cable's 31.71 Sv passes through a
  strait the grid does not have, whose stand-in is four 861 m faces
  carrying 27.08 Sv (references/derivations/ecco_western_boundary_26n.py,
  output beside it). Metrics and sensitivities stated; the measured
  scores stated for the first time in prose after being shown at the
  measurement: bias -3.2322 Sv [-3.7484, -2.7160], RMSD 3.8394
  [3.3268, 4.2911] (2.07 Sv of it not the bias), correlation +0.7729
  [+0.6818, +0.8404], anomaly correlation +0.7850 [+0.7045, +0.8455],
  neither trend significant. Independence stated as a degree: no
  transport series is among the v4r4 constraints (synopsis Table 2,
  fetched and read), mooring hydrography is, and whether the array's
  own is among it the synopsis does not say. computations/ecco-amoc-26n.md
  and computations/ecco-rapid-amoc-confrontation.md (new, draft): the
  concept pages for the two sanctioned computations and the attester
  that landed with their receipts (PASS on the real run, FAIL on nine
  doctored variants). (claude)
- 2026-09-02 · THE DOCTRINE THE BUNDLE HAS NEEDED SINCE ITS FIRST
  ANCHOR. conventions/consistency-versus-confrontation.md (new,
  draft): internal consistency (closure, cross-computation anchors,
  agreement with an independent implementation of the same integral)
  shows a method agrees with itself; confrontation (an observation
  the estimate did not see, at a fixed version, with its own
  uncertainty) shows it agrees with the world; only the second
  supports a scientific claim; a quoted published spread is a third,
  weaker kind and must not call itself validation; the acceptable
  deviation is what the measured comparison and its uncertainty say,
  never a reviewer's call; independence is a degree and is stated.
  index.md: the recipe, the convention and the two computations
  listed; the second confrontation pair, sea level from altimetry
  against ECCO SSH, queued in the recipes section as not built. (claude)
- 2026-09-02 · THREE COLOCATION QUESTIONS ANSWERED BY MEASUREMENT.
  references/derivations/rapid_colocation_checks.py (new, output
  rapid-colocation-checks.json beside it): the record note had left
  open which observed quantity is the counterpart of a model
  streamfunction maximum and whether the ten-day product is the same
  series. Measured on the overlap: the delivered series is not the
  maximum of the delivered profile sample by sample (the profile is
  unfiltered, differences up to 14 Sv), but low-passing the profile
  (sixth-order zero-phase Butterworth, one cycle per ten days) and
  maximising reproduces it to sd 0.15 Sv; the maximum of the monthly
  mean profile sits 0.12 Sv below the mean of the twelve-hourly
  maxima (at most 0.53 in a month), the max-of-mean asymmetry of the
  colocation, small against the bias and favouring the model; the
  observed monthly-mean maximum sits at 1009 m on average against the
  model's 880 m; the ten-day product is a ten-day average, not a
  subsample (up to 4.85 Sv apart at coinciding times, monthly means
  up to 1.90 Sv apart), so a comparison built on it is a different
  comparison. docs/rapid-26n-record.md: the two open questions now
  point at the measurements. datasets/rapid-mocha.md: one sentence
  pointing at the recipe (a further post-signature edit; the concept
  needs a fresh signature at merge). (claude)
- 2026-09-02 · TWO SANCTIONED COMPUTATIONS AND ONE ATTESTER FOR THE
  OVERTURNING. references/computations/ecco_amoc_26n.py: the Atlantic
  overturning at 26.5N from the signed section machinery restricted
  by ECCO's own basin codes (references/derivations/llc90_basin_codes.py,
  masks under references/masks/), three conventions with the
  per-level transports in every receipt, the ecco_v4_py 1.8.1 anchor
  for 2010 enforced on both integration directions (11.7709 and
  12.8615 Sv, agreement to four decimals), two structural sabotages
  caught (sign flip 14.33 Sv, south faces 7.49 Sv) and two scope
  choices disclosed (Gulf of Mexico +0.15 Sv, one row north 0.21 Sv).
  references/computations/ecco_rapid_amoc_confrontation.py: the
  monthly colocation, four scores with 95 percent intervals from the
  attested uncertainty chain, series digests, and the observation's
  version, DOI, hash, licence, citation, acknowledgement and published
  RMS uncertainty in the receipt. references/attesters/rapid_confrontation_check.py:
  stdlib; refuses a receipt missing any provenance field, pins the
  release and the file hash, recomputes every score, interval, digest
  and descriptive block, and with the model receipt on disk
  recomputes its primary series from the per-level transports, its
  anchor and its sabotage flags. Receipts of the real runs under
  references/retrieval/ (exhibit-amoc-26n-record.json,
  exhibit-rapid-amoc-26n-confrontation.json). The scores stayed in
  the receipts until they had been shown. (claude)
- 2026-09-02 · THE OBSERVATION HAS A VERSION. docs/rapid-26n-record.md
  (new): the RAPID-MOCHA-WBTS 26N overturning release v2024.1a (DOI
  10.5285/48d0bf43-0598-ceb2-e063-7086abc062f1, OGL v3) retrieved to a
  tree outside the repository, hashed, manifested and stamped by the
  new tools/obs_record_manifest.py, which reads version and DOI from
  the netCDF attributes and refuses a build whose files disagree or a
  tree whose bytes do not match (refusals demonstrated: one flipped
  byte, one stray file, one wrong expected version). Every claim in
  the note was checked live against the delivered files: 14,599
  twelve-hourly samples 2004-04-02 to 2024-03-27, exactly 20 absent at
  the ends as the README says, overlap with the ECCO record 2004-04
  through 2017-12 (165 months, 164 complete). The BODC DOI package
  could not be taken (sixteen transfers closed early by the server);
  the rapid.ac.uk direct files carry the same version and DOI inside
  them and are refreshed in place, so identity is by hash and
  attribute, never by URL. datasets/rapid-mocha.md gains the AMOC
  series' own version and DOI in its version line, a paragraph
  pointing to the note, and two known issues (in-place refresh; the
  v2024-1a / 2025 inconsistency inside meridional_transports.nc):
  an edit after the 2026-07-04 signature, flagged here, obliging a
  fresh signature when merged. Nothing is computed against the
  observation yet; the confrontation executor and its attester come
  next, and no score is stated until the attester recomputes it.
  Manifest and report: references/retrieval/rapid-26n-*.json.
  (claude)
- 2026-09-02 · steward review passed: computations/ecco-steric-height.md and
  recipes/ecco-steric-height.md re-verified after the interval edits
  (verified_by human:PaulMRamirez); the verified event is refreshed to
  the re-review, status stays stable. The edits merged first and the
  merge raised the re-review: an edit after signature is fine to merge
  when the log flags it, and merging it obliges a fresh signature.
- 2026-09-02 · THE TREND NEVER TRAVELS BARE. computations/ecco-steric-height.md,
  recipes/ecco-steric-height.md (both edits after signature, for the
  steward's review at merge), computations/ecco-regional-sea-level.md,
  references/skills/run-sea-level.md, computations/ecco-trend-ci.md,
  recipes/ecco-trend-ci.md, gotchas/ecco-trend-without-effective-n.md,
  new gotchas/ecco-trend-deseasonalize-jointly.md, docs/science-record.md.
  The steric and sea-level executors no longer fit trends of their
  own: each calls the sanctioned trend method's interval_block and
  embeds trend plus interval (named by the method's hash) beside its
  trend field, and one shared stdlib recompute chain
  (references/attesters/trend_recompute.py) serves all three attesters.
  The partition receipt now carries its three anomaly series and the
  residual series, so the residual, its maximum, and every trend are
  recomputed rather than believed (new criterion A6; nineteen tampers
  across both receipts each fail naming their field). Run on the
  verified record, 1992-01 through 2017-12: steric +2.7999 mm/yr, 95
  percent [+1.5103, +4.0895] (r1 +0.893, 17.6 effective months of
  312), identical to every digit from both computations, and the
  anchor now holds over the record as well as over 2010; partition
  total +5.2452 [+4.0623, +6.4281], mass +2.4535 [+2.1701, +2.7370],
  residual max 8.282e-04 m inside the 1.0e-3 bar. The 2010 anchor
  +135.7772 is unchanged and now states [-701.5, +973.1] beside it
  everywhere it appears; every 2010 trend is undistinguishable from
  zero and the concepts say so. Two method defects found by the
  retrofit and fixed: the climatology was removed before the fit,
  which hands it 143/(144Y^2-1) of the trend (a quarter at two years;
  the concept's claim of orthogonality was false), so trend and
  climatology are now fitted jointly (Frisch-Waugh-Lovell), and the
  effective sample size is capped at n, since r1 estimated from a
  short residual series is biased negative and the uncapped formula
  gave the 2010 manometric trend 38 effective months from 12. A
  precision artifact explained: the partition's fixture residual
  reads 5.061e-04 m, not 5.085e-04, once the period mean is formed in
  double (the inputs are float32; the per-month arithmetic is
  untouched so the anchor holds). Calibration rerun on the final
  method: 91.8 to 95.1 percent in the asserted regime, naive 47 to 49
  at r1 0.8; charging the climatology's parameters to the degrees of
  freedom was measured and rejected (it refuses a third of the
  120-month, r1 0.8 trials); the cap lifts 12-month white-noise
  coverage from 86 to 95 percent. Five exhibits regenerated and pass
  from a fresh clone
- 2026-09-02 · computations/ecco-trend-ci.md, recipes/ecco-trend-ci.md,
  gotchas/ecco-trend-without-effective-n.md: a sanctioned trend with
  an honest interval (OLS, residual lag-1 r1, n_eff = n(1-r1)/(1+r1),
  Student's t on n_eff-2 degrees of freedom, exact fractional
  quantile, no scipy). The receipt carries the series and every
  intermediate; the attester recomputes the whole chain and refuses
  a series that did not arrive inside a sanctioned receipt from a
  verified tree; eleven tampers each fail. Calibration with teeth:
  2000-trial seeded Monte Carlo over AR(1) series, coverage asserted
  within 90 to 97.5 percent at 120 months or more (measured 92.0 to
  95.0), negative control asserted (naive interval collapses to 45
  to 49 percent at r1 0.8); removing the correction fails it four
  ways. Reference run on our own signed steric series: +135.7772 mm
  per year over 2010 has r1 +0.555, n_eff 3.43, interval [-701.5,
  +973.1]; the gotcha is named for that trap. All three draft
- 2026-09-02 · regional budget receipts: unit labels corrected. The
  shared executor named its residual and bar keys with a degC suffix
  for all three budgets, so salt (g per kg per s) and volume (per s)
  receipts carried a heat label on correct numbers. Keys are now
  budget-neutral (residual_per_volume_max, largest_term, abs_bar) and
  every receipt states its units explicitly; the attester makes the
  stated units part of the contract and refuses a receipt whose units
  are not the budget's own (shown: a salt receipt claiming degC per s
  fails on either field, a receipt with no units fails). Reference
  residuals unchanged to the digit (heat 1.352e-14, salt 3.056e-14,
  volume 1.068e-15); both record exhibits regenerated under the new
  code hash. Heat concept contract sentence added (the salt and
  volume variants inherit it); edit after signature, for review
- 2026-09-02 · science record extended with the two collections the
  salt budget reads (OCEAN_3D_SALINITY_FLUX and FRESH_FLUX, 624
  granules, 20.97 GB): manifest regenerated with every existing row
  unchanged, fetched, and the whole tree re-verified from scratch
  (4,056 of 4,056 present, every file hashed against the archive,
  zero undeclared, stamped). All three regional budgets are now
  closable 1992-02 through 2017-11. Second exhibit on the record:
  regional salt budget 2005 closes at 1.946e-14 g per kg per s
  against 1.5e-10, three of three applicable sabotages caught; the
  heat exhibit re-run on the extended record reproduces 5.931e-15
  exactly. Boundary doc updated
- 2026-09-01 · THE SCIENCE RECORD AND THE FIXTURE BOUNDARY. Two
  manifested, verified, stamped trees: the 2010 fixture cache (144
  files, 3.08 GB, exact) stays as it is for gates, anchors, and CI;
  the science record (3,432 files, 64.57 GB, 1992-01 through 2017-12
  monthly plus month-boundary snapshots) is where sanctioned
  computations run for real results. Every granule hashed against
  the archive checksum (SHA-512 from CMR; geometry and geothermal
  local), zero undeclared files, verifier proven to refuse a flipped
  byte, a missing granule, and a stray file. Every executor now
  records the tree that fed it (data root plus the RECORD.json stamp:
  record name, manifest and report hashes, verification time) and
  every attester refuses a receipt without that stamp; the eleven
  computation concepts declare the field and the rule (edit made
  after signature, additive, for the steward's review at merge).
  First result on the record: regional heat budget 2005 closes at
  5.931e-15 degC per s, all four sabotages caught, exhibit receipt
  committed beside the manifests. Coverage: heat and volume budgets
  closable 1992-02 through 2017-11; the salt budget waits on two
  collections the record does not hold (20.97 GB, measured). Tools:
  science_record_manifest, science_record_fetch (checksum check
  extended from MD5 and SHA-256 to any archive hash; it had verified
  the download by size only), science_record_verify. Boundary and
  coverage note: docs/science-record.md
- 2026-09-01 · steward review passed: the eight control-volume
  concepts verified (verified_by human:PaulMRamirez) and promoted
  draft to stable: the regional heat, salt, and volume budget
  computations, the section transport computation, the flux
  decomposition computation, and the three recipes beside them. The
  control-volume layer is complete and signed: budgets over registered
  regions and explicit boxes, seam-calibrated section transports, and
  grouping-disclosed flux decomposition, every receipt carrying its
  sabotage evidence
- 2026-09-01 · SALT AND VOLUME REGIONAL BUDGETS AND FLUX
  DECOMPOSITION complete the control-volume set. One sanctioned
  executor now serves all three budgets under per-budget contracts
  (bars, collections, sabotage sets), and the heat reference
  remeasured at 1.352e-14 degC per s with float64 rim accumulation.
  Salt closes at 3.056e-14 against its 1.5e-10 bar, with its two
  term-omission sabotages (surface salt flux, salt plume) recording
  applicable false in the reference volume, physics disclosed rather
  than a test weakened. Volume closes at 1.068e-15 against the
  tighter 1e-11 bar, and its sabotage set turns the documented
  freshwater double-count into a MANDATORY catch: every receipt
  proves that adding a separate surface forcing term breaks the
  closure. Flux decomposition lands as the twelfth attested
  computation with the grouping as a declared parameter rather than
  a settled question: two mathematical oracles (the four-term
  identity at 1.1e-16 and the vanishing cross-term means at 3.6e-17,
  the second being the one with teeth since the identity holds for
  any split point), all four stored terms in every receipt
  regardless of grouping, and an attester that fails any reported
  view disagreeing with the stored terms. Reference: mean-advective
  +9.04354 PW, eddy -0.06963 PW through the reference region's
  interior faces. Demos across the set: seven PASS, five distinct
  FAIL. (drafted by build assistant; steward review pending)
- 2026-09-01 · SEAM CALIBRATION AND SECTION TRANSPORTS. The llc90
  tile topology (lifted from ecco_v4_py 1.8.1, all 24 connected
  edges) was verified twice before any flux crossed a seam:
  geometrically (nearest-cell mapping within one local spacing;
  same-axis joins parallel, cross-axis joins reversed, no sign flip)
  and by physics, the sharper test: the pointwise heat budget
  evaluated on all 683,496 seam-adjacent cell months of 2010 with the
  stitched cross-tile faces closes at max 2.1e-11 degC per s, p99.9
  6.6e-12, median 5.4e-14, INSIDE the interior tolerances on every
  one of the 13 tiles, so no separate seam tolerance exists and none
  is needed. On that verified topology, section transports land as
  the eleventh attested computation: signed indicator-gradient face
  masks over stored faces with cross-tile ghost cells, five sabotages
  recorded in every receipt (the ghost-zeroing one is the error a
  topology-ignorant section tool commits silently), and the honesty
  rule that an unanchored transport's receipt must declare itself.
  Reference runs: the global 26.5 north circle (360 faces) measures
  heat transport +1.0963 PW against an independent implementation's
  1.098, cross-implementation agreement to 0.002 PW from disjoint
  code paths, volume net -0.43 Sv; an interior 15 south segment (90
  faces, one tile) measures -0.28 PW and -10.56 Sv as disclosure.
  Demos: PASS both, FAIL doctored-toward-the-anchor (the two-sided
  measured band catches what the anchor band admits), FAIL dropped
  unanchored caveat, FAIL a sabotage removed from evidence. (drafted
  by build assistant; steward review pending)
- 2026-09-01 · REGIONAL HEAT BUDGET lands as the tenth attested
  computation, promoting the design note's demonstration into a
  sanctioned executor and attester. The contract carries the design
  note's two findings as machinery: TWO BARS (the absolute per-volume
  bar alone certifies a budget missing geothermal, measured 1.24e-12
  inside 1e-10, so the relative bar is required beside it) and
  MUTATION EVIDENCE in every receipt (four sabotages rerun per
  execution; a structural sabotage that cannot fail aborts the run
  receiptless; the geothermal sabotage is applicability-aware after a
  300 m open-ocean box measured its omission below both bars, which
  is physics, not a broken test). Control volumes come in two tiers,
  a keyed registry (first entry southeast-atlantic-upper, the
  reference volume: 27,921 wet cells, 4.1351e15 m3, residual per
  volume 1.632e-14 degC per s) and an explicit lat-lon box resolved
  to one tile's index rectangle with the requested and resolved
  bounds, wet and bottom cell counts, mask digest, and geometry
  digest all disclosed in the receipt, because no oracle can check a
  mask is the water the user meant. Attester demos: PASS reference,
  PASS explicit box, FAIL on a doctored flattering residual
  (two-sided anchor), FAIL on dropped mutation evidence, FAIL on a
  dropped mask digest, FAIL on a caught flag contradicting its own
  numbers. Single-tile v1 limit stated; seam-crossing volumes wait
  for seam calibration. (drafted by build assistant; steward review
  pending)
- 2026-09-01 · THREE DEFECTS FIXED in artifacts that already carried a
  steward signature. (1) The region registries in the sea level partition
  and steric height computations stored boxes as bare tuples in OPPOSITE
  orders, so the same region names resolved to different water:
  gulf-of-mexico differed by 8.0 percent in area, north-sea by 18.5.
  us-northeast-coast happened to agree, which is why the steric
  cross-computation anchor never caught it. Both registries now key their
  bounds by name rather than position, so the ordering error cannot
  recur, and both unify on the sea level partition's boxes. Receipts
  regenerated; the cross-computation anchor still reads +135.7772 mm/yr
  from both sides over 102 cells, and gulf-of-mexico now resolves to 185
  cells from both. (2) The heat budget recipe asserted the residual sits
  at "median 0.15x the snapshot quantization floor, 99.6 percent of cells
  within 3x". That had no derivation on record and does not reproduce:
  measured over the 3,341,772 baseline cell-months the residual is median
  0.66x the floor with 96.4 percent within 3x and 99.7 percent within
  10x. The corrected statement now defines the floor explicitly and cites
  a derivation script kept beside it. The qualitative claim, that the
  residual is storage quantization rather than formulation error,
  survives. (3) See the ocean-science log for the volume budget golden.
  (fixed by build assistant; steward review)
- 2026-09-01 · steward review passed: the thirteen physics-calculations
  concepts verified (verified_by human:PaulMRamirez) and promoted draft
  to stable: the attested OHC, steric height, geostrophic balance with
  thermal wind, and wind-stress curl computations, their four recipes,
  and the five gotchas (curl second rotation, VELMASS hFac
  double-count, geostrophic density factor, daily-granule midnight
  overlap, PHIHYD surface pressure). The four reserved eval-case ids
  remain owed by the eval-commons seed
- 2026-09-01 · PHYSICS CALCULATIONS phase 2: steric height, geostrophic
  balance with thermal wind, and wind-stress curl with Ekman pumping
  land as attested computations seven through nine, each with a
  sanctioned executor, receipt, deterministic attester, and PASS plus
  tamper-FAIL demos on cached native granules. Steric carries a
  cross-computation anchor: its reference trend (+135.7772 mm per
  year, US northeast coast 2010) matches the attested sea-level
  partition's signed receipt to four decimals from independent code,
  and a global run cannot pass without the Boussinesq caveat.
  Geostrophy validates at r 0.9242 over the open-ocean interior with
  the weaker full-band (0.7921) and polar figures as REQUIRED
  disclosure fields (a receipt quoting only the flattering number
  fails); its first run measured r -0.04 and the cause, PHIHYD
  missing the g ETAN surface loading, is now
  gotchas/ecco-phihyd-surface-pressure.md, our first gotcha caught by
  our own receipts rather than by review. Curl is computed entirely
  in the tile-local frame, where rotation-invariance makes the
  second-rotation trap structurally impossible; Ekman pumping vs the
  model's WVEL at 70 m measures r 0.8225 (the independent PO.DAAC
  implementation records 0.74 for the same comparison). One stress
  granule (2009-12) was retrieved to the local cache for validation;
  retrieval stays outside the executors. (drafted by build assistant;
  steward review pending)
- 2026-09-01 · PHYSICS CALCULATIONS phase 1: ocean heat content lands
  as the bundle's sixth attested computation (sanctioned executor,
  receipt, deterministic attester; reference run on cached 2010
  granules PASS, one-character tamper and doctored-anchor runs FAIL),
  with a recipe concept carrying the measured anchors (surface area
  3.5801E+08 km2 matching the tutorial's published 3.58E+08, volume
  1.3350E+18 m3, volume-mean THETA 3.61 degC). Four gotcha drafts
  land alongside, each a trap PROVEN in the field: the PO.DAAC
  ecco-skills project (podaac/ecco-skills, an independent build with
  no contact with this bundle) hit the curl second-rotation, the
  VELMASS hFac double-count, and the geostrophic density factor, all
  caught by its adversarial evaluations and all previously absent
  here, plus the daily-granule midnight overlap. That convergence,
  two teams independently finding the same traps and the same
  countermeasures, is recorded in each concept's sources with
  attribution. All drafts await steward signature. Queued: attested
  executors for steric height, geostrophic balance, thermal wind, and
  curl. (drafted by claude-code/fable-5)
- 2026-08-30 · VALIDITY DOMAINS: the bundle's first
  three validity-domain concepts landed under validity-domains/ (all
  draft, queued for steward signature; unsigned domains never
  adjudicate, the attester lists them as advisory). The exclusion
  projects the signed native-vs-regridded gotcha into declaration
  space. Both supporting domains went through the librarian pattern
  first: the ECCO large-scale statistics basis verified against Forget
  et al. 2015 and the V4r4 synopsis with exact quotes; the MUR
  mean-state draft was CORRECTED by the pass before authoring (the
  planned independent-validation and fine-scale-artifact phrasings are
  not supported by Chin et al. 2017; the landed text claims ingested
  in situ residuals and ensemble agreement instead, and the summer
  Arctic is excluded structurally by a 66N region cap). Scale-axis
  limitation stated in the ECCO domain for the steward. (drafted by
  claude-code/fable-5; provenance by the standards-librarian agent)
- 2026-08-30 · EARTHDATA MCP: connectors/earthdata-mcp.md
  landed as the bundle's first connector concept (draft, queued for
  steward review): the official CMR MCP server's endpoint, transport,
  seven-tool surface, auth boundary (discovery public, credentials only
  at earthaccess download), and deprecation flux (near-term
  stale_after). The ocean-science registration (.mcp.json) predated
  this documentation: the wire existed with no concept recording its
  facts. Tool surface verified twice, local build 2026-08-29 and remote
  endpoint 2026-08-30 (marketplace issue 20 baseline). Gates stay
  direct REST; get_variables never signs a Schema row (drafted by
  claude-code/fable-5)
- 2026-08-30 · HEATWAVE WATCH: the Hobday-family MHW
  definition landed as conventions/mhw-definition-hobday.md (draft,
  unsigned, queued for steward review). Every number verified against
  open sources: the 2018 paper's verbatim restatement of the 2016
  operational definition (90th percentile, at least five days, gaps of
  two days or less joined), the exact category sentence (moderate
  1-2x I, strong 2-3x II, severe 3-4x III, extreme >4x IV), the fixed-
  baseline recommendation, and the reference implementation's defaults
  (pctile 90, minDuration 5, maxGap 2, windowHalfWidth 5,
  smoothPercentileWidth 31). Hobday 2016 itself is paywalled; the
  verification route is stated in the concept and page-level 2016
  citations are queued for review with the steward's PDF. Baseline
  window recorded as a parameter, never a constant. Signed
  human:PaulMRamirez.

- 2026-08-30 · RECEIPTED BRIEFINGS: the regional sea
  level partition authored as an Attested Computation
  (computations/ecco-regional-sea-level.md, status draft, unsigned;
  steward approved the concept, the A1-A5 attester criterion, and the
  two scope calls at the session gate: v1 attested scope is
  ECCO-internal with GRACE/altimetry as citable context only, and the
  v0.1-form sea-level convention trio is cited as-is with upstreaming
  proposed separately). Computation authored fresh (not extracted):
  SSH total vs OBP manometric plus model-density steric (RHOAnoma
  integral, native grid, registered-region masks), receipt with
  convention-bound bookkeeping fields. A4 tolerance MEASURED per the
  heat-budget precedent: fixture run us-northeast-coast 2010-01:2010-12
  (102 cells) gave max monthly area-mean residual 5.085e-04 m; recorded
  at 1.0e-3 m with ~2x headroom, written into concept and attester
  together. Demo: sanctioned receipt PASSes; a one-character tamper
  FAILs A1. Signed human:PaulMRamirez.

- 2026-08-30 · TUTORIAL COMPANION distilled, tiers 1 and 2
  (open-science-pillars/marketplace#16): 18 companion concepts
  under podaac/tutorial/, every claim footnoted to its tutorial page,
  all status draft, unsigned; the steward reviewed the two
  pattern-setters (access library, heat-budget checkpoints) at the
  session gate before the batch. Two eval fixtures extracted to the
  ocean-science plugin (heat and volume budget checkpoints). Findings,
  neither a signed-concept contradiction: the volume chapter closes
  the ETAN sea-level identity with oceFWflx while the bundle's
  interior volume budget closes on transport alone (both true, stated
  precisely in the companion); the MHT chapter's explicit conversion
  uses rho 1000 and cp 4000 against the closure chapter's 1029 and
  3994 (about 2.5 percent; recorded as an upstream-offer note).
  Load-bearing new facts captured: the ecco_access packaging split at
  ecco_v4_py 1.8, tiles 7-12 rotated 90 degrees CCW, the V4r5
  in-cloud section, the in-region S3 rule. Coverage 18/33.
  Signed human:PaulMRamirez.

- 2026-08-30 · INGEST SWEEP bootstrap
  (open-science-pillars/marketplace#15): miner run across four
  ECCO-GROUP trackers (82 issues: ECCOv4-py, ECCO-v4-Python-Tutorial,
  ECCO-v4-Configurations, ECCO-ACCESS), min-hits 3, five clusters
  staged, steward-triaged at the session gate. Decisions: ONE keeper,
  gotchas/ecco-vector-orientation.md drafted (grid-relative UVEL/VVEL
  vs east/north; severity high, eval case pending, status draft,
  unsigned; cross-linked from fields/ecco-v4r4/ocean-vel.md);
  interpolated-budgets (7) LINKED to ecco-native-vs-regridded;
  ecco-access-quirks (6) LINKED to the dataset concept's Access facts,
  remainder discarded as resolved library bugs; snapshots-and-bookends
  (3) DISCARDED as lexicon noise; units-signs (3) LINKED, SIaaflux now
  described in fields/heat-flux; llc-grid-orientation remainder
  discarded as library-usage issues. Below threshold: geothermal 2,
  hfac 2, bolus 1, all covered. Cadence: monthly with the
  product-watch, summaries append to the tracking issue. Signed
  human:PaulMRamirez.

- 2026-08-30 · CITATION PLUMBING (open-science-pillars/marketplace#13):
  per-ShortName DOIs
  harvested live from CMR, 90/90 with zero missing, into
  tools/ecco_v4r4_dois.yaml; every manifest family gains a dois
  mapping and all 43 claimed variants in the ten authored fields
  concepts carry their harvested DOI line (never hand-typed).
  tools/ecco_cite.py landed (harvest and cite subcommands; live-run
  fix disclosed: CMR's collections.json feed omits the DOI field,
  umm_json carries it as umm.DOI.DOI, observed and patched 2026-08-30
  before any merge). check_fields gains F12 (authored concept missing
  a harvested DOI; verified silent on the merged tree and firing in a
  negative control). Signed human:PaulMRamirez.

- 2026-08-30 · GRANULE SWEEP and steward promotion
  (open-science-pillars/marketplace#10): one granule per demo family
  verified against its Schema (cached 2010 fixtures plus one 2009-12
  monthly download each for ocean-vel, ssh, obp). 42/43 seeded rows
  confirmed. ONE ground-truth catch: OCEAN_VEL carries WVEL, not
  WVELMASS; fixed in manifest and concept together, ocean-science
  variable catalog correction queued for the snapshot refresh. Row
  fixes from
  granule attrs: SALT units 1e-3; salinity fluxes 1e-3 m3 s-1;
  temperature fluxes degree_C m3 s-1; VVELMASS attr recorded verbatim;
  masks carry no units attr; OBP and OBPGMAP in m; geometry edge
  placements and drC settled by dims. 20 granule-revealed variables
  added to manifest and Schemas (9 heat-flux and 9 fresh-flux EXF/SI
  components, WVEL, PHIBOT), granule-verified 2026-08-30. All ten
  demo concepts promoted: human:PaulMRamirez verified event appended
  after the process event, status stable; the steward reviewed the
  verification table at the session gate and directed the signing.
  Signed human:PaulMRamirez.

- 2026-08-30 · FIELDS LAYER scaffolding (tracking:
  open-science-pillars/marketplace#10): verify_cmr.py, check_fields.py,
  the 26-family manifest (ecco_v4r4_families.yaml, sweep_reference
  updated to today), and the contributor template landed in tools/;
  podaac/fields/ecco-v4r4/index.md scaffolded, no concept files yet.
  Live pin: all 90 manifest ShortNames FOUND in CMR; sweep reconciles
  90 in CMR, 90 claimed, exactly one family each, both correction
  lists empty. Signed human:PaulMRamirez.

- 2026-08-30 · steward review PASSED: computations/ecco-heat-budget.md
  promoted draft to stable with a verified event
  (by: human:PaulMRamirez, at: 2026-08-30T19:40:00Z). Review basis: the
  attested receipts (sanctioned run PASS at max 5.01e-11 degC/s over
  3,341,772 cell-months; geothermal sabotage FAIL on code_sha256 and
  residual_max), PR open-science-pillars/nasa-daac-knowledge#5. The
  event was written by the build session at the steward's explicit
  direction after their inspection. Salt/volume/MHT skeletons stay
  draft (no extracted code to sign yet).

- 2026-08-30 · index.md body aligned with v0.2: conformance
  line names okf_version and the vendored spec; listing labels verified ->
  stable; computations section added. No concept content changes.

- 2026-08-30 · OKF v0.2 MIGRATION (window: open-science-pillars/marketplace#6):
  all 17 concepts migrated from OKF v0.1 plus SPEC v0.6 trust extensions
  to OKF v0.2 frontmatter: timestamp -> generated {by, at}; status
  verified -> stable; verified/verified_by -> verified
  {by: human:PaulMRamirez, at} events preserving the original review
  dates; evidence -> sources entries with stable ids; stale_after
  2027-01-04 on every concept; root index gains okf_version "0.2".
  Footnote pass joined body claims to sources ids per spec 5.1 (25 refs,
  no claims added or reworded); sources enriched with titles, authors
  where grounded (team:ecco-consortium for ECCO tutorial resources,
  human:PaulMRamirez for OSP references). generated.at on ecco-v4r4 and
  grace-fo-mascons set to 2026-07-06 per the steward-addition entry
  below; generated.by is knowledge-seeder/claude throughout (log shows
  no hand-authored concept). Two sources ids deliberately left uncited
  and flagged rather than force-joined: github-variable-catalog on
  ecco-mht-basin-scope, github-swot-products on swot-crossover-unapplied.
  check_okf_v02: 0 errors, 2 warnings (the flagged pair).
  tools/sync_check.py is EXPECTED RED against plugin snapshots until the
  ocean-science snapshot refresh (declared in the tracking issue). Signed human:PaulMRamirez.

- 2026-07-06 · steward addition (knowledge-coupling migration follow-up): grace-fo-mascons gains the native-mascon-resolution / small-basin caveat (order 300 km); ecco-v4r4 gains the THETA/SALT tracer-flavor gloss and the double-hFac budget trap. Snapshots re-synced byte-identical.

- 2026-07-05 · steward review PASSED: five concepts
  (recipes/ecco-salt-budget.md, recipes/ecco-volume-budget.md, and gotchas/
  ecco-release-mixing.md, ecco-mht-basin-scope.md, swot-crossover-unapplied.md)
  promoted draft to status: verified (verified_by OSP steward review); datasets
  ecco-v4r4.md and swot-karin.md cross-linked to the new gotchas.

- 2026-07-05 · SPEC §10.5 completion: authored recipes/ecco-salt-budget.md
  and ecco-volume-budget.md with MEASURED round-off tolerances (salt max
  7.2e-11 g/kg/s, volume max 4.6e-12 1/s; 2010 tile-1 interior) and green
  goldens. Volume budget: discovered WVELMASS already carries the surface
  freshwater flux, so a separate oceFWflx forcing term double-counts
  (surface residual jumps to ~1e-8); recorded in the recipe and the
  budget-formulation reference. Drafted for steward review.

- 2026-07-05 · SPEC §10.5 completion: promoted three embedded facts to
  standalone high-severity gotchas with matching eval cases in the
  ocean-science plugin: ecco-release-mixing (V4R4 vs V4R4B), ecco-mht-basin-scope
  (no basin mask = full circle), swot-crossover-unapplied (height_cor_xover
  not pre-applied). Drafted for steward review.

- 2026-07-05 · CANONICAL HOME established: bundle imported from
  open-science-pillars/ocean-science (its full history stands in that
  repo's git log); ocean-science's knowledge/ becomes a pinned
  snapshot per §5.7; hydrology's snapshot-podaac re-points here ·
  a later session
- 2026-07-05 · close lint: zero 🔴, three 🟡 applied on steward
  decision: swot-karin verification stamp bumped to cover the ingested
  items; load-swot and swot skills updated to ACCOMMODATE the crossover
  fact (restate lists route through Known issues; loader summary applies
  height_cor_xover and says so; flags-not-sufficient rule; new Must
  NOT). Promotion to a high gotcha deferred
- 2026-07-05 · datasets/swot-karin.md Known issues extended via the
  operational ingest loop (Tutorial 2 fresh walkthrough): crossover
  calibration arrives unapplied in ssha_karin (spurious +/-2.9 m
  cross-track ramp until height_cor_xover is added, observed PGD0
  Expert cycle 011), and CMR spatial matches can be whole passes with
  zero in-box pixels. Steward review passed
- 2026-07-04 · close lint: zero 🔴, one 🟡 (two imperative
  phrases in rapid-mocha.md), reworded to the declarative pattern per
  standing steward precedent; cross-checks vs the MHT recipe and
  compare-obs confirmed complementary, no contradictions
- 2026-07-04 · datasets/rapid-mocha.md LIVE-INGESTED via the operational
  loop: the end-to-end discovered the MOCHA official page
  links a non-scriptable SharePoint share and the canonical scriptable
  path is the dataset DOI (10.17604/3nfq-va20, AMOCatlas-indexed);
  drafted immediately, steward review passed same session (verified_by
  OSP steward review). First ingest-loop concept of the build
- 2026-07-04 · close lint: zero 🔴, four 🟡. Applied (implementing
  already-approved decisions): the relative-1e-6 remnant in
  ecco-heat-budget expected_uncertainty replaced with the approved
  absolute criterion (T1); meridional-transport's carries-no-numbers
  claim reworded after the scope-trap addition (T3); budget-formulation's
  claim of nonexistent salt/volume recipes corrected, recipes parked
 . AMS DOI 403-to-fetchers stands as accepted context
- 2026-07-04 · recipes/ecco-mht-26n.md SCOPE-CORRECTED (steward-approved):
  the earlier anchor 1.098 PW was the GLOBAL latitude circle (bare
  calc_meridional_heat_trsp), not the RAPID-comparable Atlantic section.
  Discovered by a skill-following test agent during a spot
  test, independently verified by basin decomposition (atl 0.666 + pac
  0.430 + ind 0.002 = 1.098). Recipe now carries both anchors with
  scopes; the 0.8-1.4 band is Atlantic multi-year; transport golden
  asserts both anchors and the basin-sum identity;
  meridional-transport skill gained the scope trap
- 2026-07-04 · recipes/ecco-heat-budget.md tolerance RE-GROUNDED on
  measurement (steward-approved): the relative-1e-6 criterion replaced by
  absolute max 1e-10 degC/s pointwise (p99.9 1e-11). The ocean_budget
  golden's first run showed relative ratios up to 9e-2 on a CORRECT
  formulation because float32 storage quantization exceeds quiescent-cell
  term magnitudes; measured residuals: max 4.95e-11, median 5.7e-14
  degC/s over 3.34M cell-months. budget-formulation.md aligned
- 2026-07-04 · full-bundle lint: zero 🔴; the an earlier session
  standing check-8 pair CLOSED (all four high gotchas now match real
  eval cases); three check-11 rewordings applied on steward decision
  (ghrsst-mur house-rule phrasing, ecco-v4r4 never-mix imperative,
  swot-karin crid imperative). All 14 external URLs 200 this run
- 2026-07-04 · six arc concepts authored and steward-verified
  (verified_by OSP steward review): swot-karin (granule-verified structure,
  crid attribute, 39% valid-fraction normalization), swot-calval-orbit-phases
  (reproducible C-vs-D probes), grace-fo-mascons (RL06.3 v4), both GRACE
  gotchas (GIA severity medium per recorded rationale, steward-confirmed),
  ghrsst-mur (analysis-error framing)
- 2026-07-04 · close lint (incremental): zero 🔴, three new 🟡
  resolved on steward decision: heat-budget recipe reworded to the
  owned-by pattern (check 11), inputs expanded to exact ShortNames
  (check 12), and the residual-threshold contradiction reconciled
  (budget-formulation's unsupported 1e-9-relative claim corrected to
  round-off/epsilon framing; recipe's 1e-6 relabeled as conservative
  pass tolerance). Standing check-8 pair unchanged (then pending)
- 2026-07-04 · recipes/ecco-mht-26n.md, recipes/ecco-heat-budget.md
  authored with the live 2010 reproducing run (MHT 26.5N mean 1.098 PW,
  monthly series recorded) and tutorial provenance; steward review
  passed, both verified (verified_by OSP steward review)
- 2026-07-04 · steward review passed: all three ECCO concepts verified
  (verified_by OSP steward review). Linter run first: zero 🔴, four 🟡; the two
  check-11 findings resolved by applying the linter's rewordings (policy
  phrasing moved out of concept bodies; refusal owned by ocean-budget);
  the two check-8 findings (eval cases native-grid-refusal and
  geothermal-omission are placeholders) stand until a later session authors
  the cases
- 2026-07-04 · datasets/ecco-v4r4.md, gotchas/ecco-native-vs-regridded.md,
  gotchas/ecco-geothermal-flux.md drafted with evidence from the earlier
  ShortName audit (51 collections, CMR), live access tests (geometry +
  THETA 2010, 208.75 MB), and the tutorial-verified budget formulation;
  status draft pending steward review (drafted by build
  assistant; steward review)
