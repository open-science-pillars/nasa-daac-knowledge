#!/usr/bin/env bash
# The repo check routine: conformance gates plus every tool selftest.
# All offline; run before any knowledge PR. Exit nonzero on any failure.
#
# Signature debt (SPEC 5.4, merge-then-sign) fails the routine by default,
# which is the release rule: a tag lands on a commit that owes nothing.
# SIGNATURE_DEBT=report tools/run_checks.sh lists the debt and passes,
# for a pull request or main, where a concept may owe a signature
# between a merge and its re-sign.
set -uo pipefail
cd "$(dirname "$0")/.."
fail=0
run() { echo; echo "== $*"; "$@" || fail=1; }
case "${SIGNATURE_DEBT:-fail}" in report) sig=--report ;; *) sig= ;; esac
run uv run tools/check_okf_v02.py knowledge/podaac --findings --provider nasa-daac-knowledge
run uv run tools/check_okf_v02.py knowledge/esdis --provider nasa-daac-knowledge
run uv run tools/signature_check.py knowledge/podaac $sig
run uv run tools/signature_check.py knowledge/esdis $sig
run uv run tools/check_fields.py knowledge/podaac/fields/ecco-v4r4 tools/ecco_v4r4_families.yaml
run uv run tools/verify_cmr.py tools/ecco_v4r4_families.yaml --selftest
run uv run tools/ecco_cite.py --selftest
run uv run tools/mine_sources.py --selftest
run uv run tools/release_delta.py tools/ecco_v4r4_families.yaml --selftest
run uv run tools/signature_check.py --selftest
# Sibling plugin clones, when present, have their local concepts checked
# for owed signatures; an absent sibling is not a failure here.
for plugin in ../ocean-science ../hydrology; do
  if [ -d "$plugin/knowledge" ]; then
    run uv run tools/signature_check.py "$plugin/knowledge" $sig
  fi
done
echo
if [ "$fail" -eq 0 ]; then echo "run_checks: ALL GREEN"; else echo "run_checks: FAILURES above"; fi
exit "$fail"
