# Bundle release checklist

Every step below is a steward action; the build stages, the steward
releases. Credit is derived, never edited: if the credit list looks
wrong, fix the frontmatter events or CODEOWNERS and re-derive; never
the output.

1. **Freeze and gate.** Main is green: check_okf_v02 zero errors on
   every bundle root shipping in the release, and no concept owes a
   signature: `uv run tools/signature_check.py <bundle>` lists every
   stable concept edited since its signing commit (`--diff` shows the
   edit), and a merged edit to a stable concept is re-signed before the
   freeze, so the tag is a commit the steward has signed (SPEC 5.4,
   merge then sign).
2. **Tag.** An annotated tag on main (vYYYY.MM.N), DCO-signed like any
   commit.
3. **Derive.** From the marketplace clone:
   uv run tools/derive_credit.py <this repo>/podaac <this repo>/esdis
   --since <previous release date> --out-dir release-staging/
   producing CREDITS.md and RELEASE-NOTES.md. Read both; the sanity
   rule applies: every human name must be explicable
   from an event or CODEOWNERS line, and any surprise is a bug in the
   inputs, never a candidate for hand-editing the output.
4. **Release.** A GitHub release on the tag with RELEASE-NOTES.md as
   the body and CREDITS.md attached as an asset.
5. **Mint.** Zenodo deposit of the release archive; the contributor
   list is CREDITS.md verbatim (names and roles as derived); the
   automated-instruments section goes in the Zenodo description, not
   the author list.
6. **Record.** The Zenodo DOI lands as a log.md entry at the top of
   each shipped bundle (one line: date, release tag, DOI, derived
   contributor count), and the README badge row gains or updates the
   DOI badge.
7. **Refresh the snapshots.** Every plugin that pins a copy of a
   shipped bundle (knowledge/snapshot.yaml names the source bundle,
   commit, copy directory, and scope) is refreshed to the tagged
   commit from this clone:
   uv run tools/sync_check.py <plugin>/knowledge --refresh <tag>
   which refuses a commit that owes signatures (the pin rule, SPEC
   5.7), then rewrites the in-scope files, prunes out-of-scope copies
   in a subdirectory layout, and moves the manifest and index.md pin
   lines;
   the plugin's own check_okf_v02 run stays green and the plugin's PR
   carries the tag in its title. Between releases, run_checks.sh keeps
   verifying each sibling clone at its pin and reports how far behind
   the pin sits; BEHIND is information, not a failure.
8. **Announce (optional, steward's clock).** Discussions post; the
   credit list travels with it.

Recording rule: steps 2 through 6 happen in one sitting so the tag,
the release, and the DOI never drift apart; step 7 follows in the same
sitting or the next, and the plugin release that ships the refreshed
copy pins nothing older than this tag. First release candidate
is staged on open-science-pillars/marketplace#25.
