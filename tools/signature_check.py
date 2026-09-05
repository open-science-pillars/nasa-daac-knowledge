#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml"]
# ///
"""Owed signatures: which stable concepts changed after their steward
signed them (SPEC 5.4, the merge-then-sign rule).

A steward's signature (`verified: {by: human:<id>, at}`) binds the
concept text as of the SIGNING COMMIT, the commit that introduced that
event. An edit to signed text may merge before the steward re-signs, so
that merges never wait on a signing calendar, but from that merge the
concept OWES a signature until a new human event follows. This tool
measures the debt by the signing commit, not by dates: for every stable
concept with a human event it finds the commit that introduced the
latest one, then compares that commit's text with the text under test,
ignoring only the `verified` events themselves.

  signature_check.py BUNDLE_DIR             the working tree owes what?
  signature_check.py BUNDLE_DIR --at COMMIT the bundle as of COMMIT (the
                                            pin rule: a snapshot refresh
                                            pins a commit that owes none)
  signature_check.py BUNDLE_DIR --diff      print each owed diff
  signature_check.py BUNDLE_DIR --report    list but exit 0
  signature_check.py --selftest

Lines: OWED path (signed AT in SHA; N later commits: ...), one per
concept in debt, then a summary. Exit 1 when anything is owed.
Drafts cannot owe (nothing is signed); a stable concept with no human
event is the checker's W4, not a debt. A signature written in the
working tree and not yet committed is PENDING; a concept whose signing
commit is not in the history (untracked, or a signature that arrived by
copy) is UNTRACED. Neither fails.
"""
import argparse
import difflib
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml


def git(repo, *args, check=True):
    r = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)
    if check and r.returncode != 0:
        raise SystemExit(f"git {' '.join(args)}: {r.stderr.strip()}")
    return r.stdout


def split_frontmatter(text):
    if not text.startswith("---"):
        return None, text
    lines = text.split("\n")
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[1:i]), "\n".join(lines[i + 1:])
    return None, text


def parse(text):
    """(frontmatter dict or None, body)."""
    raw, body = split_frontmatter(text)
    if raw is None:
        return None, body
    try:
        fm = yaml.safe_load(raw) or {}
    except yaml.YAMLError:
        return None, body
    return (fm if isinstance(fm, dict) else None), body


def human_events(fm):
    ver = fm.get("verified")
    events = ver if isinstance(ver, list) else [ver] if ver else []
    out = []
    for e in events:
        if isinstance(e, dict) and str(e.get("by", "")).startswith("human:"):
            at = e.get("at")
            if hasattr(at, "strftime"):   # YAML parsed the timestamp; keep the written form
                at = at.strftime("%Y-%m-%dT%H:%M:%SZ") if at.utcoffset() is not None or hasattr(at, "hour") else at.isoformat()
            out.append((str(e.get("by")), str(at)))
    return out


def signed_text(text):
    """The text a signature binds: frontmatter minus `verified`, then the body."""
    fm, body = parse(text)
    if fm is None:
        return text
    fm = dict(fm)
    fm.pop("verified", None)
    return yaml.safe_dump(fm, sort_keys=True, default_flow_style=False, allow_unicode=True) \
        + "\n---\n" + body.rstrip() + "\n"


def history(repo, ref, rel):
    """[(sha, path-at-that-commit)] newest first, following renames."""
    out = git(repo, "log", "--follow", "--format=%x00%H", "--name-only",
              *([ref] if ref else []), "--", rel, check=False)
    entries = []
    for block in out.split("\x00"):
        lines = [ln for ln in block.strip().split("\n") if ln.strip()]
        if len(lines) >= 2:
            entries.append((lines[0], lines[-1]))
    return entries


def show(repo, sha, path):
    r = subprocess.run(["git", "-C", str(repo), "show", f"{sha}:{path}"],
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def signing_commit(repo, ref, rel, event):
    """The oldest commit in the file's history that carries `event`,
    scanning newest first and stopping at the first that lacks it."""
    found = None
    for sha, path in history(repo, ref, rel):
        text = show(repo, sha, path)
        fm, _ = parse(text) if text is not None else (None, "")
        if fm is None or event not in human_events(fm):
            if found is not None:
                break
            continue
        found = (sha, path)
    return found


def later_commits(repo, ref, rel, since):
    out = git(repo, "log", "--follow", "--format=%h %s", f"{since}..{ref or 'HEAD'}", "--", rel, check=False)
    return [ln for ln in out.strip().split("\n") if ln.strip()]


def concept_files(repo, ref, bundle_rel):
    if ref:
        names = git(repo, "ls-tree", "-r", "--name-only", ref, "--", bundle_rel).split("\n")
        return sorted(n for n in names if n.endswith(".md") and Path(n).name not in ("index.md", "log.md"))
    root = Path(repo) / bundle_rel
    return sorted(p.relative_to(repo).as_posix() for p in root.rglob("*.md")
                  if p.name not in ("index.md", "log.md"))


def audit(repo: Path, bundle_rel: str, ref=None):
    """The debt of one bundle: a dict with owed [(rel, at, sha7, later,
    then, now)], pending and untraced [(rel, at)], and the counts
    signed, unsigned, drafts. `ref` None means the working tree."""
    repo = Path(repo)
    owed, untraced, pending, signed, drafts, unsigned = [], [], [], 0, 0, 0
    for rel in concept_files(repo, ref, bundle_rel):
        text = show(repo, ref, rel) if ref else (repo / rel).read_text(encoding="utf-8")
        fm, _ = parse(text)
        if fm is None:
            continue
        if fm.get("status", "stable") != "stable":
            drafts += 1
            continue
        events = human_events(fm)
        if not events:
            unsigned += 1
            continue
        signed += 1
        latest = max(events, key=lambda e: e[1])
        sc = signing_commit(repo, ref, rel, latest)
        if sc is None:
            if not ref and (repo / rel).exists() and show(repo, "HEAD", rel) is not None:
                pending.append((rel, latest[1]))   # signed in the working tree, not yet committed
            else:
                untraced.append((rel, latest[1]))
            continue
        sha, path_then = sc
        then = signed_text(show(repo, sha, path_then))
        now = signed_text(text)
        if then != now:
            later = later_commits(repo, ref, rel, sha)
            owed.append((rel, latest[1], sha[:7], later, then, now))
    return {"owed": owed, "pending": pending, "untraced": untraced,
            "signed": signed, "unsigned": unsigned, "drafts": drafts}


def check(bundle: Path, ref=None, diff=False):
    repo = Path(git(bundle if bundle.is_dir() else bundle.parent, "rev-parse", "--show-toplevel").strip())
    bundle_rel = bundle.resolve().relative_to(repo).as_posix()
    if ref:
        ref = git(repo, "rev-parse", "--verify", f"{ref}^{{commit}}").strip()
    a = audit(repo, bundle_rel, ref)
    for rel, at, sha, later, then, now in a["owed"]:
        tail = f"; {len(later)} later commit{'s' if len(later) != 1 else ''}: " + " | ".join(later[:3]) if later else "; edited in the working tree"
        print(f"OWED  {rel} (signed {at} in {sha}{tail})")
        if diff:
            sys.stdout.writelines(difflib.unified_diff(
                then.splitlines(True), now.splitlines(True),
                f"{rel}@{sha}", f"{rel}@{ref[:7] if ref else 'worktree'}"))
            print()
    for rel, at in a["pending"]:
        print(f"PENDING  {rel} (signed {at} in the working tree; commit it)")
    for rel, at in a["untraced"]:
        print(f"UNTRACED  {rel} (signed {at}; no commit in this history introduces that event)")
    where = f"at {ref[:12]}" if ref else "in the working tree"
    print(f"signature_check {bundle_rel} {where}: stable signed {a['signed']}, owed {len(a['owed'])}, "
          f"pending {len(a['pending'])}, untraced {len(a['untraced'])}, stable unsigned {a['unsigned']}, "
          f"not stable {a['drafts']}")
    return a["owed"]


def selftest():
    tmp = Path(tempfile.mkdtemp(prefix="sigcheck-"))
    repo = tmp / "repo"
    (repo / "knowledge" / "b" / "gotchas").mkdir(parents=True)
    git(tmp, "init", "-q", "-b", "main", str(repo))
    git(repo, "config", "user.email", "t@example.com")
    git(repo, "config", "user.name", "t")

    def write(rel, body, verified=None, status="stable"):
        ver = "" if verified is None else "verified:\n" + "".join(
            f"  - {{ by: {b}, at: {a} }}\n" for b, a in verified)
        (repo / rel).write_text(f"---\ntype: dataset-gotcha\nstatus: {status}\n{ver}---\n{body}\n")

    def commit(msg):
        git(repo, "add", "-A")
        git(repo, "commit", "-q", "-m", msg)
        return git(repo, "rev-parse", "HEAD").strip()

    a, b = "knowledge/b/gotchas/a.md", "knowledge/b/gotchas/b.md"
    write(a, "one fact", status="draft")
    write(b, "another fact")
    c1 = commit("drafts")
    write(a, "one fact", [("human:t", "2026-01-01T00:00:00Z")])
    write(b, "another fact", [("process:sweep", "2026-01-01T00:00:00Z"), ("human:t", "2026-01-02T00:00:00Z")])
    c2 = commit("sign both")

    def run(*args):
        r = subprocess.run([sys.executable, __file__, str(repo / "knowledge" / "b"), *args],
                           capture_output=True, text=True)
        return r.returncode, r.stdout + r.stderr

    rc, out = run()
    assert rc == 0 and "owed 0" in out and "stable signed 2" in out, out
    # an edit to signed text in the working tree owes; a new machine event does not
    write(a, "one fact, sharpened", [("human:t", "2026-01-01T00:00:00Z")])
    write(b, "another fact", [("process:sweep", "2026-01-01T00:00:00Z"), ("human:t", "2026-01-02T00:00:00Z"),
                              ("process:sweep", "2026-02-01T00:00:00Z")])
    rc, out = run("--diff")
    assert rc == 1 and "OWED  knowledge/b/gotchas/a.md" in out and "OWED  knowledge/b/gotchas/b.md" not in out, out
    assert "+one fact, sharpened" in out and "edited in the working tree" in out, out
    # a re-sign in the working tree is pending until committed, and clears the debt
    write(a, "one fact, sharpened", [("human:t", "2026-01-01T00:00:00Z"), ("human:t", "2026-01-03T00:00:00Z")])
    rc, out = run()
    assert rc == 0 and "PENDING  knowledge/b/gotchas/a.md" in out and "owed 0" in out and "pending 1" in out, out
    write(a, "one fact, sharpened", [("human:t", "2026-01-01T00:00:00Z")])
    c3 = commit("sharpen a, sweep b")
    rc, out = run()
    assert rc == 1 and "1 later commit: " in out and "sharpen a" in out and "owed 1" in out, out
    # --at a commit: c2 owes nothing, c3 owes one, and --report exits 0
    rc, out = run("--at", c2)
    assert rc == 0 and "owed 0" in out, out
    rc, out = run("--at", c3, "--report")
    assert rc == 0 and "owed 1" in out, out
    # a re-sign clears the debt; a rename after signing does not create one
    write(a, "one fact, sharpened", [("human:t", "2026-01-01T00:00:00Z"), ("human:t", "2026-03-01T00:00:00Z")])
    commit("re-sign a")
    git(repo, "mv", a, "knowledge/b/gotchas/a-moved.md")
    commit("move a")
    rc, out = run()
    assert rc == 0 and "owed 0" in out and "stable signed 2" in out and "untraced 0" in out, out
    # a draft never owes, whatever its history
    write("knowledge/b/gotchas/c.md", "draft", [("human:t", "2026-01-01T00:00:00Z")], status="draft")
    commit("odd draft")
    rc, out = run()
    assert rc == 0 and "not stable 1" in out, out
    print("signature_check selftest: OK (owed, pending, cleared by re-sign, --at, --diff, --report, rename, draft)")


def main():
    ap = argparse.ArgumentParser(description="owed signatures (SPEC 5.4)")
    ap.add_argument("bundle", nargs="?", type=Path)
    ap.add_argument("--at", metavar="COMMIT", help="check the bundle as of COMMIT instead of the working tree")
    ap.add_argument("--diff", action="store_true", help="print each owed diff (verified events excluded)")
    ap.add_argument("--report", action="store_true", help="list owed signatures but exit 0")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        selftest()
        return 0
    if args.bundle is None:
        ap.error("bundle directory required")
    owed = check(args.bundle, args.at, args.diff)
    return 0 if (args.report or not owed) else 1


if __name__ == "__main__":
    sys.exit(main())
