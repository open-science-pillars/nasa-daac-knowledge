# podaac-arc bundle: change log

Newest first. One line per change: date, concept path, what changed, who.

_Historical note: older entries use build-era shorthand (a "close lint" is a knowledge-linter pass; red/yellow marks are nonconformant/advisory findings; check numbers refer to the linter checks documented in core/agents/knowledge-linter). The decision chains, not the labels, are what teach the standards._

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
