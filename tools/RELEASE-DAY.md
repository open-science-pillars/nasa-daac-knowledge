# RELEASE-DAY: the V4r5 day-one playbook

Run this cold the day PO.DAAC publishes ECCO V4r5 (or any successor
release; substitute the token). Prepared 2026-08-30. The tripwire is the
monthly product-watch, and the moment the probe below returns a nonzero
V4R5 count, the watch issue converts into the release tracking issue and
this playbook fires.

## The tripwire (also run monthly with the product-watch)

```bash
uv run tools/release_delta.py tools/ecco_v4r4_families.yaml --new-token V4R5 --live
```

Reading the output BEFORE the release: zero V4R5 collections makes
every v4r4 stem print as DISCONTINUED. That is the "trigger unfired"
shape, not a real deprecation; the summary line ("0 collections") is
the number that matters. Baseline recorded 2026-08-30: 0 collections,
80 stems listed discontinued for that reason.

## Release day, step by step

The procedure:

> Read first: tools/RELEASE-DAY.md, the PO.DAAC announcement, the delta
> tool output.
>
> Task: run release_delta.py --live --draft-dir, open the delta PR the
> same day: the v4r5 manifest skeleton, the migration-gotcha stub
> completed with the announcement's facts (period, changes,
> recommendation status), and a log.md entry. Then run the fields pattern against the
> ten demo-critical v4r5 families: draft, CMR-sign, granule-verify,
> steward-sign. Post the day-one
> summary to Discussions and send the steward the review link;
> if the handoff landed, this is their first release-moment review. If
> reproduction capsules exist, run the re-verification set as the
> final beat: the opted-in V4r4 findings re-execute against V4r5,
> receipts attach, and the pre-briefed authors get their results before
> anything is public, per the publication policy.

Expanded commands:

```bash
# 1. The delta and the three draft artifacts (report, skeleton, gotcha stub)
uv run tools/release_delta.py tools/ecco_v4r4_families.yaml \
  --new-token V4R5 --live --draft-dir /tmp/v4r5-delta
# 2. Complete the gotcha stub from the ANNOUNCEMENT's facts (period
#    extension, renames, baseline changes, mixing rule); never from memory.
# 3. Same-day delta PR: skeleton to tools/, completed gotcha to
#    podaac/gotchas/, log.md entry, run tools/run_checks.sh first.
# 4. Fields-kit pattern on the ten demo-critical v4r5 families:
#    draft from the skeleton and landing pages, verify_cmr --sign,
#    granule-verify, steward signs (their hands or their explicit
#    direction; the promotion ladder is unchanged).
```

## Lifecycle on the v4r4 side

Continued v4r4 collections stay `stable` until the steward declares the
recommendation flipped; then `status: deprecated` with `superseded_by`
forward links, the V4R4B precedent as the pattern, and `stale_after`
pulled forward on affected concepts per the steward playbook sweep.

## Standing rule

Reproduction capsules are built the moment a V4r5 DATE is announced,
not when the data lands, so that capsules exist before the release
does. That rule is active from today and does not wait for this
playbook to fire.

## Validity domains on release day

A nonzero new-release collection count also sweeps
podaac/validity-domains/: every domain whose releases qualifier names
the superseded token is flagged for steward re-verification (the
domain statement is falsifiable by exactly this event), and no flagged
domain adjudicates the new release's collections until re-verified and
re-signed. The fitness attester needs no change: new-release
ShortNames simply do not match un-updated product patterns, so the
honest default is UNADJUDICATED.
