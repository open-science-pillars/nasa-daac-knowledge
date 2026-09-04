#!/usr/bin/env bash
# The repo check routine: conformance gates plus every tool selftest.
# All offline; run before any knowledge PR. Exit nonzero on any failure.
set -uo pipefail
cd "$(dirname "$0")/.."
fail=0
run() { echo; echo "== $*"; "$@" || fail=1; }
run uv run tools/check_okf_v02.py knowledge/podaac --findings --provider nasa-daac-knowledge
run uv run tools/check_okf_v02.py knowledge/esdis --provider nasa-daac-knowledge
run uv run tools/check_fields.py knowledge/podaac/fields/ecco-v4r4 tools/ecco_v4r4_families.yaml
run uv run tools/verify_cmr.py tools/ecco_v4r4_families.yaml --selftest
run uv run tools/ecco_cite.py --selftest
run uv run tools/mine_sources.py --selftest
run uv run tools/release_delta.py tools/ecco_v4r4_families.yaml --selftest
run uv run tools/sync_check.py --selftest
# Sibling plugin clones that declare a snapshot manifest are checked at
# their pin; a plugin without a manifest is not a failure here.
for plugin in ../ocean-science ../hydrology; do
  if [ -f "$plugin/knowledge/snapshot.yaml" ]; then
    run uv run tools/sync_check.py "$plugin/knowledge"
  fi
done
echo
if [ "$fail" -eq 0 ]; then echo "run_checks: ALL GREEN"; else echo "run_checks: FAILURES above"; fi
exit "$fail"
