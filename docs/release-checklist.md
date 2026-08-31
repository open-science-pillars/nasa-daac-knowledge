# Bundle release checklist

Every step below is a steward action; the build stages, the steward
releases. Credit is derived, never edited: if the credit list looks
wrong, fix the frontmatter events or CODEOWNERS and re-derive; never
the output.

1. **Freeze and gate.** Main is green: check_okf_v02 zero errors on
   every bundle root shipping in the release.
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
7. **Announce (optional, steward's clock).** Discussions post; the
   credit list travels with it.

Recording rule: steps 2 through 6 happen in one sitting so the tag,
the release, and the DOI never drift apart. First release candidate
is staged on open-science-pillars/marketplace#25.
