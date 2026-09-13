#!/usr/bin/env bash
# The repo check routine: conformance gates plus every tool selftest.
# All offline; run before any knowledge PR. Exit nonzero on any failure.
#
# Signature debt (merge-then-sign: a merged edit to a signed concept owes
# a new signature) fails the routine by default, which is the release
# rule: a tag lands on a commit that owes nothing.
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
run uv run tools/check_okf_v02.py knowledge/nsidc --provider nasa-daac-knowledge
run uv run tools/check_negative.py knowledge/podaac
run uv run tools/check_negative.py knowledge/esdis
run uv run tools/check_negative.py knowledge/nsidc
run uv run tools/signature_check.py knowledge/podaac $sig
run uv run tools/signature_check.py knowledge/esdis $sig
run uv run tools/signature_check.py knowledge/nsidc $sig
run uv run tools/digest.py knowledge/podaac --check
run uv run tools/digest.py knowledge/esdis --check
run uv run tools/digest.py knowledge/nsidc --check
run uv run tools/check_fields.py knowledge/podaac/fields/ecco-v4r4 tools/ecco_v4r4_families.yaml
run uv run tools/verify_cmr.py tools/ecco_v4r4_families.yaml --selftest
run uv run tools/ecco_cite.py --selftest
run uv run tools/mine_sources.py --selftest
run uv run tools/release_delta.py tools/ecco_v4r4_families.yaml --selftest
run uv run tools/signature_check.py --selftest
run uv run tools/check_script_deps.py --selftest
run uv run tools/check_script_deps.py knowledge tools
run uv run tools/check_prose.py --selftest
run uv run tools/sign.py --selftest
run uv run tools/check_okf_v02.py --selftest
run uv run tools/digest.py --selftest
run uv run tools/reattest.py --selftest
run uv run tools/check_negative.py --selftest
run uv run tools/receipt_identity.py --selftest
run uv run tools/solicit.py --selftest
run uv run tools/record.py --selftest
run uv run tools/check_prose.py .
# The sea level budget chain, end to end on every change: the executor
# writes a receipt on the fixture, the attester passes it; the refusal
# path (a period across the inter-mission gap, no bridge) exits 3 and
# attests as a refusal. Receipts live in a temporary directory only.
sea_level_budget_chain() {
  local x=knowledge/podaac/references/computations/sea_level_budget.py
  local a=knowledge/podaac/references/attesters/sea_level_budget_check.py
  local tmp; tmp=$(mktemp -d)
  uv run "$x" --fixture --seed 7 --period 2005-01:2016-12 --runtime run_checks --receipt "$tmp/receipt.json" || return 1
  uv run "$a" "$tmp/receipt.json" || return 1
  uv run "$x" --fixture --seed 7 --period 2016-01:2019-12 --runtime run_checks --receipt "$tmp/refusal.json"
  [ "$?" -eq 3 ] || { echo "sea_level_budget_chain: the gap refusal did not exit 3"; return 1; }
  uv run "$a" "$tmp/refusal.json" | tee "$tmp/verdict.txt" || return 1
  grep -q "^PASS refusal" "$tmp/verdict.txt" || { echo "sea_level_budget_chain: the refusal did not attest as a refusal"; return 1; }
  rm -rf "$tmp"
}
run uv run knowledge/podaac/references/attesters/sea_level_budget_check.py --selftest
run sea_level_budget_chain
# Sibling plugin clones, when present, have their local concepts checked
# for owed signatures, their scripts for undeclared dependencies and their
# prose for the wording rules; an absent sibling is not a failure here.
for plugin in ../ocean-science ../hydrology; do
  if [ -d "$plugin/knowledge" ]; then
    run uv run tools/signature_check.py "$plugin/knowledge" $sig
    run uv run tools/check_script_deps.py "$plugin"
    run uv run tools/check_prose.py "$plugin"
  fi
done
echo
if [ "$fail" -eq 0 ]; then echo "run_checks: ALL GREEN"; else echo "run_checks: FAILURES above"; fi
exit "$fail"
