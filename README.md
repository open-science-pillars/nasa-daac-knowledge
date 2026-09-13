# nasa-daac-knowledge

The provider knowledge bundles of Open Science Pillars (PO.DAAC,
ESDIS, NSIDC), one per NASA archive under `knowledge/`: `knowledge/podaac/` holds the peculiarities
that make naive analyses of PO.DAAC-archived products (ECCO, SWOT,
GRACE-FO, MUR, NASA-SSH, RAPID) silently wrong, as reviewable OKF
concepts with sources, statuses and steward sign-off; `knowledge/esdis/`
holds the cross-archive metadata requirements; `knowledge/nsidc/`
holds the NSIDC DAAC land ice products (ICESat-2 ATL15, the MEaSUREs
ITS_LIVE and InSAR velocity mosaics), the cryosphere's first concepts.
It carries no skills and no agents: you use it through
[ocean-science](https://github.com/open-science-pillars/ocean-science)
and [hydrology](https://github.com/open-science-pillars/hydrology),
which declare it as a dependency and cite its concepts by bundle path,
and any installed skill reads it through core's consult-knowledge
convention. It is a provider repository (`kind: provider` in
`.osp/repository.yaml`); the words used on this page (provider bundle,
concept, steward, capability, plugin) are defined in the
[glossary](https://github.com/open-science-pillars/marketplace/blob/main/GLOSSARY.md).
Gate before any pull request: `bash tools/run_checks.sh`; the same
routine runs on every pull request, on main, and on each release tag
(`.github/workflows/gate.yml`), where a signature owed is a failure.

## Provider authority

A provider repository's bundles are keyed by the organization that
signs their facts, and a steward's approval is the authority,
runtime-independent. Every scientific concept names the Earth science
spheres its claim spans in `spheres` (hydrosphere throughout here,
geosphere added on GRACE); the tag states the scope of the claim and
moves no authority, and it sits outside the text a signature binds. One
signed concept feeds every runtime's projection; nothing is re-approved
per runtime, and a packaging-only change needs no scientific
re-approval. A provider person who takes the steward rung (below)
joins the bundle's steward team (`podaac-stewards`, `esdis-stewards`, `nsidc-stewards`),
which CODEOWNERS already names.

## Install

The bundles ship as one plugin, `nasa-daac-knowledge`, in the Open
Science Pillars marketplace. The domain plugins that use these concepts
(ocean-science, hydrology) declare it as a dependency, so installing one
of them installs this plugin at a version that satisfies their floor,
with nothing else to do. To install it on its own, on Claude Code:

```bash
claude plugin marketplace add open-science-pillars/marketplace
claude plugin install nasa-daac-knowledge@open-science-pillars
```

On Claude Cowork, add the marketplace by repository
(`open-science-pillars/marketplace`) under Customize > Plugins > Add
marketplace and install the same plugin from it; the shell commands on
this page are for Claude Code.

The plugin carries knowledge and tools only, no skills or agents;
installed skills find its bundles through core's consult-knowledge
convention. Releases carry calendar versions (2026.9.1): `claude plugin
list` shows which one is installed, and
`claude plugin update nasa-daac-knowledge@open-science-pillars` fetches
the newest, because this marketplace does not update installs on its
own unless you enable that. Updating a domain plugin does not update
this one: when the new release of a domain plugin raises its floor
past the version you have, `claude plugin list` shows that plugin
disabled with an error naming the floor and the installed version
(observed 2026-09-05: "Requires nasa-daac-knowledge >=2026.9.2,
installed 2026.9.1"), and the update command above resolves it. The
same holds for a domain plugin installed before it declared this
dependency: its update does not install this plugin, the error names
the install command above, and running it (or `/reload-plugins` in a
session) resolves it.

## How this relates to the plugins

The provider bundle is the canonical home: on any conflict the concept
here wins over a plugin-local one. Domain plugins reach it as an
installed dependency, never by path and never by a copy: a plugin
cites a concept here by its bundle path (`knowledge/podaac/...`), and
core's consult-knowledge convention resolves that through the
installer's record of installed plugins. A plugin raises its version
floor when it needs a newer bundle and never pins an exact version, so
a correction here reaches every install that updates.

## Stewardship

CODEOWNERS maps each bundle to its steward team, and the maintainer
who holds a bundle is its steward. The steward's signature (a
`verified` event written by `sign.py`) is the honesty marker on a
concept: a named person read the claim and stands behind it. It is
not a gate. A concept ships at whatever trust tier its events have
earned, and a consumer reads the tier from them: unverified (no
event), machine-confirmed (process events only), human-reviewed (a
`human:` event), provider-confirmed (a `human:` event carrying
`role: provider`). A verified event keeps the OKF shape,
`{ by: human:<id>, at: <time> }`, and may carry two OSP keys inside
it: `role` (maintainer, provider or community; absent means
maintainer) and `source`, the URL where the person gave the
confirmation.

A person from the organization that produces the data is invited at
every rung of that ladder and required at none:

- **Consulted.** They read the bundle's `DIGEST.md` ("What this
  bundle claims about your products", one row per concept about their
  product, rendered by `digest.py`) and answer a "confirm this
  concept" issue, one they open from its Confirm or correct link or
  one the steward opens for them with `solicit.py`. The steward
  records the answer on their behalf with `record.py <issue>` (which
  runs `sign.py`'s edit: `--role provider --by human:<their id>
  --source <the reply URL>`, plus the log entry). The event lands as
  `{ by, at, role: provider, source }` and the concept becomes
  provider-confirmed; the checker's W10 asks for the source on any
  provider event recorded without one.
- **Reviewer.** They review the knowledge pull requests that touch
  their product.
- **Steward.** They join the bundle's CODEOWNERS team and sign with
  `sign.py --role provider` themselves.

The confirmation loop, from the steward's side, is five steps:

1. Pick the concepts from the digest: a product's rows, or every stable concept with no provider event.
2. `uv run tools/solicit.py knowledge/<bundle> --product "<title>" --to @<them> --mark`, then the same with `--apply`: one issue per concept, the concept inline, the digest marks the row Asked.
3. They reply on the issue with one word: confirmed, correction, or not (my product).
4. `uv run tools/record.py <issue number>`, then with `--apply`: confirmed writes the event and the log entry; a correction is the steward's to fix, followed by a fresh ask.
5. Open the pull request with the printed commit message, `Confirm <path> (closes #N)`; its merge closes the issue.

Review rules per the specification's stewardship section
(docs/SPECIFICATION.md in open-science-pillars/marketplace) and the
[steward playbook](https://github.com/open-science-pillars/marketplace/blob/main/docs/steward-playbook.md);
how to write a concept is
[docs/contributing-knowledge.md](https://github.com/open-science-pillars/marketplace/blob/main/docs/contributing-knowledge.md)
and what the checker demands is
[docs/okf-conformance.md](https://github.com/open-science-pillars/marketplace/blob/main/docs/okf-conformance.md),
both in the marketplace repository. A release follows
[docs/release-checklist.md](docs/release-checklist.md) here; the
bundle owes no provider signature for it, only that no stable concept
owes its own steward a re-sign (the merge-then-sign rule).
Eval coverage for high-severity gotchas ships with the plugins that
depend on this bundle (their evals/ directories, or the eval
repository a plugin declares as the home of its cases); this repo
owns concept truth, not agent testing.

## Running the tools

Everything runnable here, and in the plugins that depend on this one,
is a Python script that declares its own dependencies in a PEP 723
header, and `uv` builds the environment from that header on first run.
The one requirement is uv itself:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

The one rule is to run a script through uv, `uv run <script>`, never
`python script.py` and never `uv run python script.py`: both skip the
header, and the run fails with `No module named netCDF4` (or numpy, or
matplotlib) at first import. Nothing needs installing by hand; nothing
needs a virtualenv. `uv run tools/doctor.py` confirms uv is present and
lists every script and the packages it will resolve;
`uv run tools/doctor.py --warm` builds every environment now, so a
first run on a new machine or an offline one starts at once (give it
the other plugins' paths too, `claude plugin list` shows them). The
gate (`check_script_deps.py`, in `run_checks.sh` and in each plugin's
CI) fails any script whose imports are not covered by its header, so
what is on main resolves.

## Tools

| Tool | Purpose | Who runs it |
|---|---|---|
| `run_checks.sh` | The gate: OKF conformance, fields conformance, the negative-knowledge check, the script-dependency check, the wording check, the signature-debt measure, each bundle's digest up to date, and every tool selftest, all offline | A contributor before any pull request; CI on every pull request, on main and on each release tag |
| `doctor.py` | Readiness: confirms uv, lists every script and the packages it resolves; `--warm` builds every environment ahead of a first or offline run | Anyone on a new machine |
| `check_okf_v02.py` | OKF v0.2 conformance of one bundle root | `run_checks.sh`; each plugin's gate on its local bundle; a bundle copied from knowledge-template |
| `check_fields.py` | The fields concepts agree with the ECCO family manifest (`ecco_v4r4_families.yaml`) | `run_checks.sh` |
| `check_negative.py` | A dead-end records who tried what, when and why it failed; a field-state records the positions a field holds as of a date; neither adjudicates, both carry a load-bearing key, both are reopened or superseded rather than deleted; `--candidates` scans text for dead-end phrasings | `run_checks.sh`; a steward drafting negative knowledge |
| `check_script_deps.py` | Every script's PEP 723 header covers what it imports | `run_checks.sh`; each plugin's CI |
| `check_prose.py` | The wording rules: specification rules cited by name rather than section number, no program bookkeeping in what a reader meets, no em or en dashes | `run_checks.sh`; each plugin's CI |
| `signature_check.py` | Which stable concepts changed after their steward signed them, measured by the signing commit (the merge-then-sign rule) | `run_checks.sh`, reported on pull requests and main, enforced on a release tag |
| `sign.py` | Appends a verified event to each named concept and one entry to the bundle log, so paying a signature debt is one command and one commit; `--role provider --by human:<id> --source <reply URL>` records a provider person's confirmation on their behalf (`--role community` a user's), the source being where they gave it | The steward |
| `digest.py` | Renders a bundle's `DIGEST.md`, what the bundle claims about each product: one row per concept with its tier, latest verified date, an Asked mark when a confirm issue is open for it (`review:` in its frontmatter) and a Confirm or correct link that opens the confirm-concept issue prefilled; `--check` fails when the committed digest is stale | `run_checks.sh` for `--check`; the steward after a concept change, and the page a provider person reads first |
| `solicit.py` | Opens one confirm-concept issue per selected concept (`--concept`, `--product`, `--unconfirmed`), the concept rendered inline and the people asked mentioned (`--to @handle`); skips a concept whose issue is open; `--mark` writes `review: <issue url>` on the concept; every write is a printed dry run until `--apply` | The steward, asking a provider person to confirm |
| `record.py` | Reads a confirm-concept issue and its comments, finds the reply (confirmed, correction, not mine), and on confirmed writes the provider event in the replier's name with the reply as source, removes `review:`, adds the log entry and prints the commit message whose merge closes the issue; a correction is printed for the steward to fix; dry run until `--apply` | The steward, when the person has replied |
| `verify_cmr.py`, `release_delta.py`, `RELEASE-DAY.md` | The ECCO product watch: the family manifest against CMR, the delta a new release introduces, and the day-one playbook | The steward, monthly and on release day |
| `ecco_v4r4_dois.yaml`, `ecco_cite.py` | The DOI authority and the citation formatter; the selftest cross-checks every DOI the concepts and the family manifest quote against the authority | The cite-ecco skill in ocean-science; `run_checks.sh` for the selftest |
| `mine_sources.py` | The community-issue miner: drafts gotcha candidates and routes can-I-use-X-for-Y questions and phrasings of a failed attempt to the validity-domain and dead-end registers; needs `GITHUB_TOKEN` | The steward, at a sweep |
| `mcp_smoke.py` | The Earthdata MCP tool-surface smoke, over the network | The steward, at a connector sweep |
| `receipt_identity.py` | A receipt or attestation names the capability release and the runtime (the convention in `docs/receipt-identity.md`); with `--package DIR` it must match that package | Attesters and each capability's CI; `run_checks.sh` for the selftest |
| `ecco_budget_badge.py`, `templates/ecco-budget-badge-workflow.yml` | Runs the heat budget attester on a receipt and writes the verdict as a shields.io badge; the template is an adopter's workflow, pinned by release tag | A repository that adopts the workflow |
| `reattest.py`, `reference_runs.yaml` | After a deliberate edit to a sanctioned computation: one command runs the file on the fixture cache with its reference arguments, attests the fresh receipt, shows the previous version's receipt failing against the new file and a tamper of the new file failing, and drafts the log entry with both hashes | The steward, after an edit to a sanctioned computation |
| `science_record_*.py`, `obs_record_*.py` | The science and observation record tooling: fetch, manifest and verify the frozen records a finding or an observation cites | An analyst freezing a record; the steward verifying one |
| `migrate_okf_v02.py` | Migrates a bundle's frontmatter from OKF v0.1 to v0.2, touching only the keys being migrated | A bundle owner with a bundle that predates OKF v0.2 |

License: Apache-2.0. Cite via CITATION.cff.
