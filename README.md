# nasa-daac-knowledge

CANONICAL HOME for per-DAAC dataset knowledge bundles (SPEC v0.6
§5.7), one bundle per provider under `knowledge/`: `knowledge/podaac/`
holds the peculiarities that make naive analyses of PO.DAAC-archived
products silently wrong, as reviewable OKF concepts with sources,
statuses, and steward sign-off; `knowledge/esdis/` holds the
cross-archive requirements bundle. Every OSP repository that carries a
bundle keeps it under `knowledge/`, so tools and readers find it the
same way everywhere. Gate before any PR: `bash tools/run_checks.sh`.

## Install

The bundles ship as one plugin, `nasa-daac-knowledge`, in the Open
Science Pillars marketplace. The domain plugins that use these concepts
(ocean-science, hydrology) declare it as a dependency, so installing one
of them installs this plugin at a version that satisfies their floor,
with nothing else to do. To install it on its own:

```bash
claude plugin marketplace add open-science-pillars/marketplace
claude plugin install nasa-daac-knowledge@open-science-pillars
```

The plugin carries knowledge and tools only, no skills or agents;
installed skills find its bundles through core's consult-knowledge
convention. Releases carry calendar versions (2026.9.1): `claude plugin
list` shows which one is installed, and
`claude plugin update nasa-daac-knowledge@open-science-pillars` (or an
update of a domain plugin that already has it installed as a
dependency) fetches the newest, because this marketplace does not
update installs on its own unless you enable that. A domain plugin
installed before it declared this dependency does not gain it from an
update: `claude plugin list` shows that plugin disabled with an error
naming the install command above, and running it (or `/reload-plugins`
in a session) resolves it.

## How this relates to the plugins

The provider bundle is the canonical home: on any conflict the concept
here wins over a plugin-local one (SPEC 5.7). Domain plugins reach it as
an installed dependency, never by path and never by a copy: a plugin
cites a concept here by its bundle path (`knowledge/podaac/...`), and
core's consult-knowledge convention resolves that through the
installer's record of installed plugins. A plugin raises its version
floor when it needs a newer bundle and never pins an exact version, so
a correction here reaches every install that updates.

## Tools

`tools/` carries the gate (`run_checks.sh`: OKF conformance, fields
conformance, and every tool selftest, all offline), the ECCO product
watch (`verify_cmr.py`, `release_delta.py`, `RELEASE-DAY.md`), the DOI
authority and citation formatter (`ecco_v4r4_dois.yaml`, `ecco_cite.py`;
the selftest cross-checks every DOI the concepts and the family manifest
quote against the authority), the community-issue miner that drafts
gotcha candidates (`mine_sources.py`, needs `GITHUB_TOKEN`), the
Earthdata MCP tool-surface smoke (`mcp_smoke.py`, network), the owed-signature check
(`signature_check.py`: which stable concepts changed after their
steward signed them, measured by the signing commit; SPEC 5.4), and the
science and observation record tooling (`science_record_*.py`,
`obs_record_*.py`).

## Stewardship

CODEOWNERS maps each bundle to its steward; the PO.DAAC bundle is
held by an interim (pro tem) steward pending handoff to a provider
steward. The handoff trigger: a named provider accepts the CODEOWNERS
entry and co-reviews three PRs (see the playbook's onboarding section).
Review rules per SPEC §5.4 and the
[steward playbook](https://github.com/open-science-pillars/marketplace/blob/main/docs/steward-playbook.md).
Eval coverage for high-severity gotchas ships with the plugins that
depend on this bundle (their evals/ directories, or the eval
repository a plugin declares as the home of its cases); this repo
owns concept truth, not agent testing.

License: Apache-2.0. Cite via CITATION.cff.
