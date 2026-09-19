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
# The real-data anchor: the stamped three-term data root committed under
# references/retrieval is run for the reference period and attested, so
# the anchor the computation concept quotes is recomputed on every change.
sea_level_budget_record() {
  local x=knowledge/podaac/references/computations/sea_level_budget.py
  local a=knowledge/podaac/references/attesters/sea_level_budget_check.py
  local root=knowledge/podaac/references/retrieval/sea-level-budget-root
  local tmp; tmp=$(mktemp -d)
  uv run knowledge/podaac/references/loaders/slb_data_root.py --root "$root" --check || return 1
  uv run "$x" --data-root "$root" --period 2005-01:2016-12 --runtime run_checks --receipt "$tmp/record.json" || return 1
  uv run "$a" "$tmp/record.json" || return 1
  rm -rf "$tmp"
}
run uv run knowledge/podaac/references/attesters/sea_level_budget_check.py --selftest
run sea_level_budget_chain
run sea_level_budget_record
# The asdc energy budget closure: the fixture chain with its refusal, the
# loader selftests, the stamped data root check, and the real-data anchor
# run attested against the tree (nasa-daac-knowledge PR #174).
energy_budget_chain() {
  local x=knowledge/asdc/references/computations/energy_budget.py
  local a=knowledge/asdc/references/attesters/energy_budget_check.py
  local tmp; tmp=$(mktemp -d)
  uv run "$x" --fixture --seed 7 --window 2006-01:2020-12 --runtime run_checks --receipt "$tmp/receipt.json" || return 1
  uv run "$a" "$tmp/receipt.json" || return 1
  uv run "$x" --fixture --seed 7 --window 1998-01:2005-12 --runtime run_checks --receipt "$tmp/refusal.json"
  [ "$?" -eq 3 ] || { echo "energy_budget_chain: the window refusal did not exit 3"; return 1; }
  uv run "$a" "$tmp/refusal.json" | tee "$tmp/verdict.txt" || return 1
  grep -q "^PASS refusal" "$tmp/verdict.txt" || { echo "energy_budget_chain: the refusal did not attest as a refusal"; return 1; }
  rm -rf "$tmp"
}
energy_budget_record() {
  local x=knowledge/asdc/references/computations/energy_budget.py
  local a=knowledge/asdc/references/attesters/energy_budget_check.py
  local root=knowledge/asdc/references/retrieval/energy-budget-root
  local tmp; tmp=$(mktemp -d)
  uv run knowledge/asdc/references/loaders/eb_data_root.py --root "$root" --check || return 1
  uv run "$x" --data-root "$root" --ohc-receipt "$root/ohc-2000-receipt.json" --window 2006-01:2020-12 --runtime run_checks --receipt "$tmp/record.json" || return 1
  uv run "$a" "$tmp/record.json" --data-root "$root" || return 1
  rm -rf "$tmp"
}
run uv run knowledge/asdc/references/attesters/energy_budget_check.py --selftest
run uv run knowledge/asdc/references/loaders/eb_ceres_ebaf.py --selftest
run uv run knowledge/asdc/references/loaders/eb_data_root.py --selftest
run energy_budget_chain
run energy_budget_record

# The cloud radiative effect (asdc): the fixture run and its attestation,
# the refusal of a clear-sky convention the product does not carry, and
# the anchored record run on the committed root.
cloud_radiative_effect_chain() {
  local x=knowledge/asdc/references/computations/cloud_radiative_effect.py
  local a=knowledge/asdc/references/attesters/cloud_radiative_effect_check.py
  local tmp; tmp=$(mktemp -d)
  uv run "$x" --fixture --seed 7 --region global --clear-sky total-region --window 2006-01:2020-12 --runtime run_checks --receipt "$tmp/receipt.json" || return 1
  uv run "$a" "$tmp/receipt.json" || return 1
  uv run "$x" --fixture --seed 7 --region global --clear-sky pristine --window 2006-01:2020-12 --runtime run_checks --receipt "$tmp/refusal.json"
  [ "$?" -eq 3 ] || { echo "cloud_radiative_effect_chain: the convention refusal did not exit 3"; return 1; }
  uv run "$a" "$tmp/refusal.json" | tee "$tmp/verdict.txt" || return 1
  grep -q "^PASS refusal" "$tmp/verdict.txt" || { echo "cloud_radiative_effect_chain: the refusal did not attest as a refusal"; return 1; }
  rm -rf "$tmp"
}
cloud_radiative_effect_record() {
  local x=knowledge/asdc/references/computations/cloud_radiative_effect.py
  local a=knowledge/asdc/references/attesters/cloud_radiative_effect_check.py
  local root=knowledge/asdc/references/retrieval/cloud-radiative-effect-root
  local tmp; tmp=$(mktemp -d)
  uv run knowledge/asdc/references/loaders/cre_data_root.py --root "$root" --check || return 1
  uv run "$x" --data-root "$root" --region global --clear-sky cloud-free-area --window 2005-07:2015-06 --runtime run_checks --receipt "$tmp/record.json" || return 1
  uv run "$a" "$tmp/record.json" --data-root "$root" || return 1
  rm -rf "$tmp"
}
run uv run knowledge/asdc/references/attesters/cloud_radiative_effect_check.py --selftest
run uv run knowledge/asdc/references/loaders/cre_ceres_fluxes.py --selftest
run uv run knowledge/asdc/references/loaders/cre_data_root.py --selftest
run cloud_radiative_effect_chain
run cloud_radiative_effect_record
# The ice sheet balance data root (nsidc): the firn and surface mass
# balance loaders' selftests and the committed root's manifest check.
run uv run knowledge/nsidc/references/loaders/isb_firn_gemb.py --selftest
run uv run knowledge/nsidc/references/loaders/isb_smb_gemb.py --selftest
# The nsidc ice sheet mass balance closure: the attester selftest, the
# fixture chain with its overlap refusal, the loader selftests, the
# stamped data root check, the Greenland real-data anchor attested
# against the tree and the Antarctic refusal (nasa-daac-knowledge PR #176).
run uv run knowledge/nsidc/references/attesters/ice_sheet_balance_check.py --selftest
ice_sheet_balance_chain() {
  local x=knowledge/nsidc/references/computations/ice_sheet_balance.py
  local a=knowledge/nsidc/references/attesters/ice_sheet_balance_check.py
  local tmp; tmp=$(mktemp -d)
  uv run "$x" --fixture --seed 7 --ice-sheet greenland --window 2019-01:2022-12 --altimetry atl15 --runtime run_checks --receipt "$tmp/receipt.json" || return 1
  uv run "$a" "$tmp/receipt.json" || return 1
  uv run "$x" --fixture --seed 7 --ice-sheet greenland --window 2019-01:2025-12 --altimetry atl15 --runtime run_checks --receipt "$tmp/refusal.json"
  [ "$?" -eq 3 ] || { echo "ice_sheet_balance_chain: the overlap refusal did not exit 3"; return 1; }
  uv run "$a" "$tmp/refusal.json" | tee "$tmp/verdict.txt" || return 1
  grep -q "^PASS refusal" "$tmp/verdict.txt" || { echo "ice_sheet_balance_chain: the refusal did not attest as a refusal"; return 1; }
  rm -rf "$tmp"
}
run ice_sheet_balance_chain
run uv run knowledge/nsidc/references/loaders/isb_mass_mascons.py --selftest
run uv run knowledge/nsidc/references/loaders/isb_volume_atl15.py --selftest
run uv run knowledge/nsidc/references/loaders/isb_volume_itslive.py --selftest
run uv run knowledge/nsidc/references/loaders/isb_data_root.py --root knowledge/nsidc/references/retrieval/ice-sheet-balance-root --check
ice_sheet_balance_record() {
  local x=knowledge/nsidc/references/computations/ice_sheet_balance.py
  local a=knowledge/nsidc/references/attesters/ice_sheet_balance_check.py
  local root=knowledge/nsidc/references/retrieval/ice-sheet-balance-root
  local tmp; tmp=$(mktemp -d)
  uv run "$x" --data-root "$root" --ice-sheet greenland --window 2003-01:2016-12 --altimetry itslive --runtime run_checks --receipt "$tmp/record.json" || return 1
  uv run "$a" "$tmp/record.json" --data-root "$root" || return 1
  uv run "$x" --data-root "$root" --ice-sheet antarctica --window 2003-01:2016-12 --runtime run_checks --receipt "$tmp/antarctica.json"
  [ "$?" -eq 3 ] || { echo "ice_sheet_balance_record: the Antarctic run did not refuse"; return 1; }
  uv run "$a" "$tmp/antarctica.json" --data-root "$root" | grep -q "^PASS refusal" || return 1
  rm -rf "$tmp"
}
run ice_sheet_balance_record

# The two altimetry records over the window they share, each run and attested.
# The pair is the claim the concept's reference run makes, so the routine runs
# both: the parameter changes only the altimetric term, and a change in either
# rate belongs to that record rather than to the mascons.
ice_sheet_balance_altimetry_pair() {
  local x=knowledge/nsidc/references/computations/ice_sheet_balance.py
  local a=knowledge/nsidc/references/attesters/ice_sheet_balance_check.py
  local root=knowledge/nsidc/references/retrieval/ice-sheet-balance-root
  local tmp; tmp=$(mktemp -d)
  local alt
  for alt in itslive atl15; do
    uv run "$x" --data-root "$root" --ice-sheet greenland --window 2019-01:2023-10 \
      --altimetry "$alt" --runtime run_checks --receipt "$tmp/$alt.json" || return 1
    uv run "$a" "$tmp/$alt.json" --data-root "$root" || return 1
  done
  rm -rf "$tmp"
}
run ice_sheet_balance_altimetry_pair

# The nsidc input-output balance: the attester selftest, the fixture chain
# with its window refusal, the loader selftests, the stamped data root
# check, and the record run, which refuses because the root carries no
# thickness term (the archive host this environment's egress policy
# refuses) and no surface mass balance term (no NASA archive distributes
# one over grounded ice), and attests as a refusal.
ice_sheet_input_output_chain() {
  local x=knowledge/nsidc/references/computations/ice_sheet_input_output.py
  local a=knowledge/nsidc/references/attesters/ice_sheet_input_output_check.py
  local tmp; tmp=$(mktemp -d)
  uv run "$x" --fixture --seed 7 --ice-sheet greenland --window 2005-01:2014-12 --gates synthetic-outlets --runtime run_checks --receipt "$tmp/receipt.json" || return 1
  uv run "$a" "$tmp/receipt.json" || return 1
  uv run "$x" --fixture --seed 7 --ice-sheet greenland --window 2021-01:2023-12 --gates synthetic-outlets --runtime run_checks --receipt "$tmp/refusal.json"
  [ "$?" -eq 3 ] || { echo "ice_sheet_input_output_chain: the window refusal did not exit 3"; return 1; }
  uv run "$a" "$tmp/refusal.json" | tee "$tmp/verdict.txt" || return 1
  grep -q "^PASS refusal" "$tmp/verdict.txt" || { echo "ice_sheet_input_output_chain: the refusal did not attest as a refusal"; return 1; }
  rm -rf "$tmp"
}
ice_sheet_input_output_record() {
  local x=knowledge/nsidc/references/computations/ice_sheet_input_output.py
  local a=knowledge/nsidc/references/attesters/ice_sheet_input_output_check.py
  local root=knowledge/nsidc/references/retrieval/ice-sheet-input-output-root
  local tmp; tmp=$(mktemp -d)
  uv run knowledge/nsidc/references/loaders/iio_data_root.py --root "$root" --check || return 1
  uv run "$x" --data-root "$root" --ice-sheet greenland --window 2014-01:2023-12 --gates greenland-outlets-v1 --runtime run_checks --receipt "$tmp/record.json"
  [ "$?" -eq 3 ] || { echo "ice_sheet_input_output_record: the record run did not refuse"; return 1; }
  uv run "$a" "$tmp/record.json" --data-root "$root" | tee "$tmp/verdict.txt" || return 1
  grep -q "^PASS refusal" "$tmp/verdict.txt" || { echo "ice_sheet_input_output_record: the record run did not attest as a refusal"; return 1; }
  rm -rf "$tmp"
}
run uv run knowledge/nsidc/references/attesters/ice_sheet_input_output_check.py --selftest
run uv run knowledge/nsidc/references/loaders/iio_velocity_itslive.py --selftest
run uv run knowledge/nsidc/references/loaders/iio_thickness_bedmachine.py --selftest
run uv run knowledge/nsidc/references/loaders/iio_smb_gemb.py --selftest
run uv run knowledge/nsidc/references/loaders/iio_data_root.py --selftest
run ice_sheet_input_output_chain
run ice_sheet_input_output_record

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
