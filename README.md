# nasa-daac-knowledge

CANONICAL HOME for per-DAAC dataset knowledge bundles (SPEC v0.6
§5.7), starting with `podaac/`: the peculiarities that make naive
analyses of PO.DAAC-archived products silently wrong, as reviewable
OKF concepts with evidence links, statuses, and steward sign-off.

## How this relates to the plugins

Plugins (ocean-science, hydrology) embed PINNED SNAPSHOTS of these
concepts so installs are self-contained (SPEC §0.5). Precedence: the
canonical concept here wins on any conflict; snapshots record source
commit and date in their index.md and refresh at plugin releases
(`tools/sync_check.py` verifies byte-identity).

## Stewardship

CODEOWNERS maps each bundle to its steward; the PO.DAAC bundle is
held pro tem pending the provider handoff (the Phase-2 exit
criterion). Review rules per SPEC §5.4 and the
[steward playbook](https://github.com/open-science-pillars/marketplace/blob/main/docs/steward-playbook.md).
Eval coverage for high-severity gotchas ships with the plugins that
embed the snapshots (the plugins' evals/ directories); this repo owns
concept truth, not agent testing.

License: Apache-2.0. Cite via CITATION.cff.
