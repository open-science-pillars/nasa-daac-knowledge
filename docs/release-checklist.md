# Bundle release checklist

Every step below is a steward action; the build stages, the steward
releases. Credit is derived, never edited: if the credit list looks
wrong, fix the frontmatter events or CODEOWNERS and re-derive; never
the output.

The bundles ship as one plugin (`.claude-plugin/plugin.json`) that the
domain plugins depend on at a version floor, so a release is three
things: the version bump that lets installs see it, the tag the
installer resolves, and the catalog line that names it. Versions are
calendar semver, `YYYY.M.N` with no zero padding (2026.9.1, then
2026.9.2 for a second release in the same month), because the installer
compares versions as semver and semver forbids a leading zero.

1. **Freeze and gate.** Main is green: `bash tools/run_checks.sh`
   (check_okf_v02 zero errors on every bundle root shipping in the
   release; no concept owes a signature, as
   `uv run tools/signature_check.py <bundle>` measures it, listing every
   stable concept edited since its signing commit with `--diff` showing
   the edit; a merged edit to a stable concept is re-signed before the
   freeze, so the tag is a commit the steward has signed, SPEC 5.4,
   merge then sign), and `claude plugin validate .` passes.
2. **Bump.** `version` in `.claude-plugin/plugin.json` and in
   CITATION.cff, in the same PR as the last content change of the
   release; merge it. The bump is what reaches installs: an install
   keeps its cached copy until the version string changes.
3. **Tag.** From the repository root, on the merge commit:
   `claude plugin tag --push -m "nasa-daac-knowledge %s"` (add a short
   body after the subject). It derives `nasa-daac-knowledge--v<version>`
   from plugin.json, checks the catalog entry agrees, and refuses a dirty
   tree or an existing tag. The tag is what a dependent plugin's version
   floor resolves against, so it exists before any plugin declares a
   floor at this version.
4. **Derive.** From the marketplace clone:
   uv run tools/derive_credit.py <this repo>/knowledge/podaac <this repo>/knowledge/esdis
   --since <previous release date> --out-dir release-staging/
   producing CREDITS.md and RELEASE-NOTES.md. Read both; the sanity
   rule applies: every human name must be explicable
   from an event or CODEOWNERS line, and any surprise is a bug in the
   inputs, never a candidate for hand-editing the output.
5. **Release.** A GitHub release on the tag with RELEASE-NOTES.md as
   the body and CREDITS.md attached as an asset.
6. **Mint.** Zenodo deposit of the release archive; the contributor
   list is CREDITS.md verbatim (names and roles as derived); the
   automated-instruments section goes in the Zenodo description, not
   the author list.
7. **Record.** The Zenodo DOI lands as a log.md entry at the top of
   each shipped bundle (one line: date, version, DOI, derived
   contributor count), and the README badge row gains or updates the
   DOI badge, labeled with the version string, not the tag name.
8. **Catalog.** A one-line PR to open-science-pillars/marketplace
   moving this plugin's `ref` to the new tag. From that merge, users
   receive the release with `claude plugin update` (or automatically
   where they enabled auto-update for the marketplace), and a domain
   plugin whose floor sits below this version receives it on its next
   update with no change of its own.
9. **Announce (optional, steward's clock).** Discussions post; the
   credit list travels with it.

Recording rule: steps 3 through 8 happen in one sitting so the tag,
the release, the DOI and the catalog never drift apart. While a domain
plugin still carries a pinned copy of a shipped bundle
(`knowledge/snapshot.yaml`), `uv run tools/sync_check.py
<plugin>/knowledge --refresh <tag>` moves the copy to the tagged commit
in that plugin's next release; the copies are being retired in favor of
the dependency and this sentence goes with them. First release
candidate is staged on open-science-pillars/marketplace#25.
