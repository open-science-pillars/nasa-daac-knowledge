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
# The finding rules (--findings) are not run here. They check a finding
# against the Attested Computation concepts and receipts it binds its
# numbers to, and after ADR E a provider bundle holds neither: the sea
# level finding's two computations and its three receipts are
# ocean-science's. The finding itself stays, as knowledge this bundle
# owns, and the coordinator decides where its rules run.
run uv run tools/check_okf_v02.py knowledge/podaac --provider nasa-daac-knowledge
run uv run tools/check_okf_v02.py knowledge/esdis --provider nasa-daac-knowledge
run uv run tools/check_okf_v02.py knowledge/nsidc --provider nasa-daac-knowledge
run uv run tools/check_okf_v02.py knowledge/gesdisc --provider nasa-daac-knowledge
run uv run tools/check_okf_v02.py knowledge/asdc --provider nasa-daac-knowledge
run uv run tools/check_okf_v02.py knowledge/obdaac --provider nasa-daac-knowledge
run uv run tools/check_okf_v02.py knowledge/lpdaac --provider nasa-daac-knowledge
run uv run tools/check_okf_v02.py knowledge/ornldaac --provider nasa-daac-knowledge
run uv run tools/check_negative.py knowledge/podaac
run uv run tools/check_negative.py knowledge/esdis
run uv run tools/check_negative.py knowledge/nsidc
run uv run tools/check_negative.py knowledge/gesdisc
run uv run tools/check_negative.py knowledge/asdc
run uv run tools/check_negative.py knowledge/obdaac
run uv run tools/check_negative.py knowledge/lpdaac
run uv run tools/check_negative.py knowledge/ornldaac
run uv run tools/signature_check.py knowledge/podaac $sig
run uv run tools/signature_check.py knowledge/esdis $sig
run uv run tools/signature_check.py knowledge/nsidc $sig
run uv run tools/signature_check.py knowledge/gesdisc $sig
run uv run tools/signature_check.py knowledge/asdc $sig
run uv run tools/signature_check.py knowledge/obdaac $sig
run uv run tools/signature_check.py knowledge/lpdaac $sig
run uv run tools/signature_check.py knowledge/ornldaac $sig
run uv run tools/digest.py knowledge/podaac --check
run uv run tools/digest.py knowledge/esdis --check
run uv run tools/digest.py knowledge/nsidc --check
run uv run tools/digest.py knowledge/gesdisc --check
run uv run tools/digest.py knowledge/asdc --check
run uv run tools/digest.py knowledge/obdaac --check
run uv run tools/digest.py knowledge/lpdaac --check
run uv run tools/digest.py knowledge/ornldaac --check
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
run uv run tools/check_negative.py --selftest
run uv run tools/solicit.py --selftest
run uv run tools/record.py --selftest
run uv run tools/check_prose.py .

# The computation chains are gone with the computations. Every executor,
# attester, loader and stamped data root this routine used to run now
# lives in the capability that owns the method (ADR E), and each of those
# packages proves its own scripts with a golden under verification/. What
# is left here is the knowledge routine: conformance, signatures, digests
# and the tool selftests of the tools this repository still holds.
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
