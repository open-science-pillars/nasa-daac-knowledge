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
   freeze, so the tag is a commit the steward has signed, per the
   merge-then-sign rule; `uv run tools/sign.py <concept>... --log
   <bundle>/log.md --note '<why>'` writes the events and the log entry
   in one step, on the steward's word), and `claude plugin validate .` passes. The tag
   push runs the same routine in CI with the debt enforced; a red
   run there means the tag moved onto a commit that owes a signature.
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
6. **Catalog.** A one-line PR to open-science-pillars/marketplace
   moving this plugin's `ref` to the new tag. From that merge, users
   receive the release with
   `claude plugin update nasa-daac-knowledge@open-science-pillars` (or
   automatically where they enabled auto-update for the marketplace).
   Updating a domain plugin does not move this one: a domain plugin
   release that raises its floor past a user's installed version shows
   that plugin disabled until the user runs the update command above,
   so a domain plugin's release notes say so when its floor moves.
7. **Announce (optional, steward's clock).** Discussions post; the
   credit list travels with it.

Recording rule: steps 3 through 6 happen in one sitting so the tag,
the release and the catalog never drift apart. First release
candidate was staged on open-science-pillars/marketplace#25.

## At 1.0.0: the Zenodo deposit and the DOI

Zenodo archiving and the DOI are deferred until the first 1.0.0
release of a plugin that depends on this bundle, tracked on
open-science-pillars/marketplace#55 and on this repository's own
tracking issue; a citable plugin needs a citable bundle, and no
earlier release is one anyone should cite. Until then CITATION.cff
says so and steps 1 through 7 are the whole release. When that
release comes, two steps join step 5 in the same sitting:

- **Mint.** Zenodo deposit of the release archive; the contributor
  list is CREDITS.md verbatim (names and roles as derived); the
  automated-instruments section goes in the Zenodo description, not
  the author list.
- **Record.** The Zenodo DOI lands as a log.md entry at the top of
  each shipped bundle (one line: date, version, DOI, derived
  contributor count), in CITATION.cff as the concept DOI with the
  steward and provider organization added as authors (steward
  playbook, Credit), and in the README badge row as a DOI badge
  labeled with the version string, not the tag name.
