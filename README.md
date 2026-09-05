# nasa-daac-knowledge

CANONICAL HOME for per-DAAC dataset knowledge bundles (SPEC v0.6
§5.7), one bundle per provider under `knowledge/`: `knowledge/podaac/`
holds the peculiarities that make naive analyses of PO.DAAC-archived
products silently wrong, as reviewable OKF concepts with sources,
statuses, and steward sign-off; `knowledge/esdis/` holds the
cross-archive requirements bundle. Every OSP repository that carries a
bundle keeps it under `knowledge/`, so tools and readers find it the
same way everywhere. Gate before any PR: `bash tools/run_checks.sh`.

## How this relates to the plugins

Plugins (ocean-science, hydrology) embed PINNED SNAPSHOTS of these
concepts so installs are self-contained (SPEC §0.5). Precedence: the
canonical concept here wins on any conflict; snapshots record source
commit, date, copy directory and scope in a `knowledge/snapshot.yaml`
manifest (and the pin in their index.md) and refresh at releases:
`tools/sync_check.py <plugin>/knowledge` verifies the copy against the
canonical bundle at the pinned commit (stale, missing, extra, dangling
links, pin drift, a pin that owes signatures) and `--refresh <commit>`
rewrites it at a commit the steward has signed.

## Tools

`tools/` carries the gate (`run_checks.sh`: OKF conformance, fields
conformance, and every tool selftest, all offline), the ECCO product
watch (`verify_cmr.py`, `release_delta.py`, `RELEASE-DAY.md`), the DOI
authority and citation formatter (`ecco_v4r4_dois.yaml`, `ecco_cite.py`;
the selftest cross-checks every DOI the concepts and the family manifest
quote against the authority), the community-issue miner that drafts
gotcha candidates (`mine_sources.py`, needs `GITHUB_TOKEN`), the
Earthdata MCP tool-surface smoke (`mcp_smoke.py`, network), the snapshot
check and refresh (`sync_check.py`), the owed-signature check
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
embed the snapshots (the plugins' evals/ directories); this repo owns
concept truth, not agent testing.

License: Apache-2.0. Cite via CITATION.cff.
