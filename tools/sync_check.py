#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml"]
# ///
"""Snapshot sync check and refresh (SPEC 5.7).

A domain plugin ships a pinned copy of provider concepts under its own
knowledge/. The plugin declares that copy in knowledge/snapshot.yaml:

    source:
      repository: open-science-pillars/nasa-daac-knowledge
      bundle: knowledge/podaac     # the bundle's path in that repository at the pinned commit
      commit: 9224fe5a83e4           # normally the steward's signing commit
      date: 2026-09-03
    copy_dir: snapshot-podaac      # relative to knowledge/; "." = beside local concepts
    scope:                         # exactly one of include or exclude
      include:                     # explicit files or directories (trailing slash)
        - datasets/grace-fo-mascons.md
      # exclude:                   # everything in the bundle except these
      #   - tutorial/

The check compares the copy against the canonical bundle AT THE PINNED
COMMIT (git show), so it is deterministic whatever canonical's HEAD is.
The bundle's own index.md and log.md are never in scope.

Verdicts (any of the first five fails the check):
  STALE      copied file differs from canonical at the pin (hand edit)
  MISSING    in-scope canonical file absent from the copy
  EXTRA      file in copy_dir that is not in scope (subdirectory layout only)
  DANGLING   copied concept links to a canonical file outside the scope
  PIN-DRIFT  index.md's "Snapshot source commit" disagrees with the manifest
  BEHIND     informational: commits since the pin that touch in-scope files

Usage:
  sync_check.py <plugin-knowledge-dir>                 check at the pin
  sync_check.py <plugin-knowledge-dir> --against HEAD  check against another commit
  sync_check.py <plugin-knowledge-dir> --refresh [COMMIT]
        rewrite the copy from canonical at COMMIT (default HEAD), prune
        out-of-scope files in a subdirectory layout, update the manifest
        and the index.md pin lines, then re-run the check
  sync_check.py --selftest
  --canonical <repo>   canonical repository (default: the repo this tool lives in)

Without a manifest the legacy behaviour runs: every canonical *.md that
also exists in the plugin dir (flat or under snapshot-podaac/) is
compared against the working tree, and a note asks for a manifest.
Exit 0 when clean, 1 otherwise.
"""
import argparse
import os
import posixpath
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

LINK_RE = re.compile(r"\]\(([^)\s]+?)(?:#[^)]*)?\)")
SKIP_NAMES = ("index.md", "log.md")


def git(repo, *args, text=True):
    r = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=text)
    if r.returncode != 0:
        raise SystemExit(f"git {' '.join(args)}: {r.stderr.strip() if text else r.stderr}")
    return r.stdout


def in_scope(rel, scope):
    if "include" in scope:
        return any(rel == i or (i.endswith("/") and rel.startswith(i)) for i in scope["include"])
    return not any(rel == e or (e.endswith("/") and rel.startswith(e)) for e in scope.get("exclude", []))


def scoped_files(repo, bundle, ref, scope):
    tree = git(repo, "ls-tree", "-r", "--name-only", ref, "--", bundle).split()
    rels = [t[len(bundle) + 1:] for t in tree if t.startswith(bundle + "/")]
    if not rels:
        raise SystemExit(f"bundle {bundle} has no files at {ref}; source.bundle is the bundle's path "
                         f"AT THAT COMMIT (the bundle may have moved since), edit it and rerun")
    all_rels = set(rels)
    return sorted(r for r in rels if r not in SKIP_NAMES and in_scope(r, scope)), all_rels


def load_manifest(kdir):
    m = kdir / "snapshot.yaml"
    if not m.exists():
        return None
    data = yaml.safe_load(m.read_text()) or {}
    src = data.get("source") or {}
    for key in ("repository", "bundle", "commit"):
        if src.get(key) is None or src.get(key) == "":
            raise SystemExit(f"snapshot.yaml: source.{key} is required")
        src[key] = str(src[key])  # an all-digit commit would otherwise parse as an int
    scope = data.get("scope") or {}
    if ("include" in scope) == ("exclude" in scope):
        raise SystemExit("snapshot.yaml: scope needs exactly one of include or exclude")
    data["copy_dir"] = str(data.get("copy_dir") or ".")
    return data


def index_pin(kdir):
    idx = kdir / "index.md"
    if not idx.exists():
        return None
    m = re.search(r"Snapshot source commit:\s*([0-9a-f]{7,40})", idx.read_text())
    return m.group(1) if m else None


def dangling_links(repo, bundle, ref, rel, scoped, all_rels):
    if not rel.endswith(".md"):
        return []
    text = git(repo, "show", f"{ref}:{bundle}/{rel}")
    out = []
    for target in LINK_RE.findall(text):
        if re.match(r"^[a-z]+:", target) or target.startswith("/"):
            continue
        resolved = posixpath.normpath(posixpath.join(posixpath.dirname(rel), target))
        if resolved in all_rels and resolved not in scoped and posixpath.basename(resolved) not in SKIP_NAMES:
            out.append(resolved)
    return out


def check(kdir, manifest, repo, ref=None):
    src = manifest["source"]
    bundle = src["bundle"].strip("/")
    ref = ref or src["commit"]
    scope = manifest["scope"]
    copy = (kdir / manifest["copy_dir"]).resolve()
    flat = copy == kdir.resolve()
    scoped, all_rels = scoped_files(repo, bundle, ref, scope)
    scoped_set = set(scoped)
    stale, missing, dangling = [], [], []
    for rel in scoped:
        want = git(repo, "show", f"{ref}:{bundle}/{rel}", text=False)
        have = copy / rel
        if not have.exists():
            missing.append(rel)
        elif have.read_bytes() != want:
            stale.append(rel)
        for t in dangling_links(repo, bundle, ref, rel, scoped_set, all_rels):
            dangling.append(f"{rel} -> {t}")
    extra = []
    if not flat:
        for p in sorted(copy.rglob("*")):
            if p.is_file() and str(p.relative_to(copy).as_posix()) not in scoped_set:
                extra.append(str(p.relative_to(copy).as_posix()))
    drift = []
    pin = index_pin(kdir)
    if pin and not (pin.startswith(src["commit"]) or src["commit"].startswith(pin)):
        drift.append(f"index.md says {pin}, snapshot.yaml says {src['commit']}")
    behind = None
    try:
        commits = git(repo, "rev-list", "--count", f"{src['commit']}..HEAD", "--", bundle).strip()
        changed = git(repo, "diff", "--name-only", src["commit"], "HEAD", "--", bundle).split()
        changed = [c[len(bundle) + 1:] for c in changed if c[len(bundle) + 1:] in scoped_set]
        behind = (int(commits), changed)
    except SystemExit:
        behind = None
    form = "include" if "include" in scope else "exclude"
    print(f"sync_check: {kdir} against {src['repository']} {bundle} at {ref} "
          f"(scope {form} {', '.join(scope[form]) or '(none)'}; {len(scoped)} files in scope; "
          f"layout {'flat, EXTRA not checked' if flat else manifest['copy_dir']})")
    fail = False
    for label, items in (("STALE", stale), ("MISSING", missing), ("EXTRA", extra),
                         ("DANGLING", dangling), ("PIN-DRIFT", drift)):
        if items:
            fail = True
            print(f"{label} ({len(items)}):", *items, sep="\n  ")
    if behind:
        n, changed = behind
        if n or changed:
            print(f"BEHIND: {n} commits since the pin touch the bundle; {len(changed)} in-scope files changed"
                  + (":" if changed else ""), *changed, sep="\n  ")
        else:
            print("BEHIND: none; the pin is canonical HEAD for this bundle")
    print("sync_check: " + ("FAIL" if fail else "OK"))
    return 1 if fail else 0


def refresh(kdir, manifest, repo, commit):
    src = manifest["source"]
    bundle = src["bundle"].strip("/")
    full = git(repo, "rev-parse", commit).strip()
    short = full[:12]
    date = git(repo, "show", "-s", "--format=%cs", full).strip()
    scoped, _ = scoped_files(repo, bundle, full, manifest["scope"])
    copy = (kdir / manifest["copy_dir"]).resolve()
    flat = copy == kdir.resolve()
    written = 0
    for rel in scoped:
        dest = copy / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        data = git(repo, "show", f"{full}:{bundle}/{rel}", text=False)
        if not dest.exists() or dest.read_bytes() != data:
            dest.write_bytes(data)
            written += 1
    removed = 0
    if not flat and copy.exists():
        keep = set(scoped)
        for p in sorted(copy.rglob("*"), reverse=True):
            if p.is_file() and str(p.relative_to(copy).as_posix()) not in keep:
                p.unlink()
                removed += 1
            elif p.is_dir() and not any(p.iterdir()):
                p.rmdir()
    mpath = kdir / "snapshot.yaml"
    text = mpath.read_text()
    text = re.sub(r"^(\s*commit:\s*)\S+", rf"\g<1>{short}", text, count=1, flags=re.M)
    if re.search(r"^\s*date:", text, flags=re.M):
        text = re.sub(r"^(\s*date:\s*)\S+", rf"\g<1>{date}", text, count=1, flags=re.M)
    else:
        text = re.sub(r"^(\s*commit:.*)$", rf"\1\n  date: {date}", text, count=1, flags=re.M)
    mpath.write_text(text)
    manifest["source"]["commit"] = short
    idx = kdir / "index.md"
    if idx.exists():
        t = idx.read_text()
        t = re.sub(r"(Snapshot source commit:\s*)[0-9a-f]{7,40}", rf"\g<1>{short}", t, count=1)
        t = re.sub(r"(Snapshot date:\s*)\d{4}-\d{2}-\d{2}", rf"\g<1>{date}", t, count=1)
        idx.write_text(t)
    print(f"refresh: {len(scoped)} files in scope at {short} ({date}); {written} written, {removed} removed"
          + ("" if flat else f" from {manifest['copy_dir']}/"))
    return check(kdir, manifest, repo)


def legacy(kdir, repo, bundle="knowledge/podaac"):
    canon = repo / bundle
    bad, checked = [], 0
    for f in canon.rglob("*.md"):
        rel = f.relative_to(canon)
        if rel.name in SKIP_NAMES:
            continue
        for cand in (kdir / rel, kdir / "snapshot-podaac" / rel):
            if cand.exists():
                checked += 1
                if cand.read_bytes() != f.read_bytes():
                    bad.append(str(rel))
                break
    print(f"sync_check (legacy, no snapshot.yaml): {checked} overlapping *.md files checked against the working tree")
    print("NOTE: write knowledge/snapshot.yaml to get MISSING, EXTRA, DANGLING and PIN-DRIFT, and --refresh")
    if bad:
        print("STALE:", *bad, sep="\n  ")
        return 1
    print("all byte-identical")
    return 0


def selftest():
    def commit(repo, msg):
        git(repo, "add", "-A")
        git(repo, "-c", "user.name=selftest", "-c", "user.email=selftest@example.invalid",
            "commit", "-q", "-m", msg)
        return git(repo, "rev-parse", "HEAD").strip()

    with tempfile.TemporaryDirectory() as td:
        repo = Path(td) / "canon"
        b = repo / "knowledge" / "podaac"
        (b / "datasets").mkdir(parents=True)
        (b / "gotchas").mkdir()
        (b / "tutorial").mkdir()
        (b / "references" / "retrieval").mkdir(parents=True)
        (b / "index.md").write_text("---\nokf_version: \"0.2\"\n---\n# index\n")
        (b / "log.md").write_text("# log\n")
        (b / "datasets" / "a.md").write_text("# a\nsee [b](../gotchas/b.md) and [t](../tutorial/t.md) and [idx](../index.md)\n")
        (b / "gotchas" / "b.md").write_text("# b\n")
        (b / "tutorial" / "t.md").write_text("# t\n")
        (b / "references" / "retrieval" / "x.json").write_text("{}\n")
        git(repo.parent, "init", "-q", str(repo))
        c1 = commit(repo, "c1")

        kdir = Path(td) / "plugin" / "knowledge"
        kdir.mkdir(parents=True)
        (kdir / "index.md").write_text("# plugin\n- Snapshot source commit: 000000000000\n- Snapshot date: 2000-01-01\n")
        (kdir / "gotchas").mkdir()
        (kdir / "gotchas" / "local.md").write_text("# local\n")
        (kdir / "snapshot.yaml").write_text(
            "source:\n  repository: example/canon\n  bundle: knowledge/podaac\n  commit: 0000000\n"
            "copy_dir: snapshot-podaac\nscope:\n  exclude: [tutorial/]\n")
        m = load_manifest(kdir)

        def run(fn, *a):
            import io, contextlib
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                rc = fn(*a)
            return rc, buf.getvalue()

        rc, out = run(refresh, kdir, m, repo, c1)
        assert "DANGLING (1)" in out and "datasets/a.md -> tutorial/t.md" in out, out
        assert "MISSING" not in out and "STALE" not in out and "PIN-DRIFT" not in out, out
        assert (kdir / "snapshot-podaac" / "references" / "retrieval" / "x.json").exists()
        assert not (kdir / "snapshot-podaac" / "tutorial").exists()
        assert c1[:12] in (kdir / "index.md").read_text() and c1[:12] in (kdir / "snapshot.yaml").read_text()
        assert "date:" in (kdir / "snapshot.yaml").read_text()
        assert (kdir / "gotchas" / "local.md").exists()

        # widen the scope: the dangling link resolves
        (kdir / "snapshot.yaml").write_text((kdir / "snapshot.yaml").read_text().replace("exclude: [tutorial/]", "exclude: []"))
        m = load_manifest(kdir)
        rc, out = run(refresh, kdir, m, repo, c1)
        assert rc == 0 and "sync_check: OK" in out, out

        # each failure verdict
        (kdir / "snapshot-podaac" / "gotchas" / "b.md").write_text("# b edited\n")
        (kdir / "snapshot-podaac" / "datasets" / "a.md").unlink()
        (kdir / "snapshot-podaac" / "gotchas" / "z.md").write_text("# z\n")
        (kdir / "index.md").write_text("# plugin\n- Snapshot source commit: 1111111111\n- Snapshot date: 2000-01-01\n")
        rc, out = run(check, kdir, m, repo)
        for want in ("STALE (1)", "gotchas/b.md", "MISSING (1)", "datasets/a.md", "EXTRA (1)", "gotchas/z.md", "PIN-DRIFT (1)"):
            assert want in out, (want, out)
        assert rc == 1

        # refresh repairs all four, and BEHIND reports canonical movement
        (b / "datasets" / "a.md").write_text("# a v2\nsee [b](../gotchas/b.md)\n")
        c2 = commit(repo, "c2")
        rc, out = run(refresh, kdir, m, repo, c1)
        assert rc == 0 and "BEHIND: 1 commits" in out and "datasets/a.md" in out, out
        rc, out = run(refresh, kdir, m, repo, c2)
        assert rc == 0 and "BEHIND: none" in out, out
        assert (kdir / "snapshot-podaac" / "datasets" / "a.md").read_text().startswith("# a v2")

        # include form, flat layout: only listed files, EXTRA not checked, locals untouched
        (kdir / "snapshot.yaml").write_text(
            f"source:\n  repository: example/canon\n  bundle: knowledge/podaac\n  commit: {c2[:12]}\n"
            "copy_dir: .\nscope:\n  include:\n    - gotchas/b.md\n")
        m = load_manifest(kdir)
        rc, out = run(refresh, kdir, m, repo, c2)
        assert rc == 0 and "1 files in scope" in out and "EXTRA not checked" in out, out
        assert (kdir / "gotchas" / "b.md").exists() and (kdir / "gotchas" / "local.md").exists()
        assert not (kdir / "datasets").exists()

        # manifest validation
        (kdir / "snapshot.yaml").write_text("source:\n  repository: x\n  bundle: knowledge/podaac\n  commit: abc\nscope: {}\n")
        try:
            load_manifest(kdir)
            raise AssertionError("scope validation did not fire")
        except SystemExit as e:
            assert "exactly one" in str(e)
    print("sync_check selftest: OK (refresh, STALE, MISSING, EXTRA, DANGLING, PIN-DRIFT, BEHIND, include, flat, validation)")
    return 0


def main():
    ap = argparse.ArgumentParser(description="snapshot sync check and refresh (SPEC 5.7)")
    ap.add_argument("plugin_knowledge_dir", nargs="?")
    ap.add_argument("--against", metavar="COMMIT", help="compare against this commit instead of the pin")
    ap.add_argument("--refresh", nargs="?", const="HEAD", metavar="COMMIT", help="rewrite the copy from canonical at COMMIT (default HEAD)")
    ap.add_argument("--canonical", metavar="REPO", help="canonical repository (default: this tool's repo)")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(selftest())
    if not a.plugin_knowledge_dir:
        ap.error("plugin knowledge dir required (or --selftest)")
    kdir = Path(a.plugin_knowledge_dir).resolve()
    repo = Path(a.canonical).resolve() if a.canonical else Path(__file__).resolve().parent.parent
    manifest = load_manifest(kdir)
    if manifest is None:
        sys.exit(legacy(kdir, repo))
    if a.refresh:
        sys.exit(refresh(kdir, manifest, repo, a.refresh))
    sys.exit(check(kdir, manifest, repo, a.against))


if __name__ == "__main__":
    main()
