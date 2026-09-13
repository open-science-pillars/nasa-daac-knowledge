#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# ///
"""Record a provider's reply on a "confirm this concept" issue as a
verified event on the concept, in the replier's name.

The issue is one solicit.py opened (title `Confirm: <path>`, the reply
a comment by the person asked) or one a person opened themselves from
the digest's confirm-or-correct link (the organization's confirm
concept form, whose body carries `### Concept` and `### Answer`
sections). The tool reads the issue and its comments through `gh api`,
finds the concept and the answer, says who gave it and when, and then:

  confirmed   appends `{ by: human:<login>, at, role: provider, source:
              <reply url> }` to the concept (sign.py's edit), removes
              `review:` if present, adds the bundle log entry, and
              prints the diff and the commit message to use,
              `Confirm <path> (closes #N)`, so the merge closes the
              issue
  correction  prints the correction and the concept path and edits
              nothing: the maintainer fixes the concept (its own pull
              request), asks again, and runs record.py once the person
              confirms the fixed text
  not         (not my product, not my call) prints it; on --apply
              comments on the issue with thanks and the question who
              would know, and removes `review:`
  no answer   says so and exits 1

The answer is the latest recognizable reply: a comment whose first
word, case folded and stripped of punctuation, is confirmed, correction,
corrected or not. On a solicited issue the reply comes from someone
other than the issue's author; on a form-opened issue the author is
the person answering, so their comments count, and the body's `###
Answer` section is the answer when no comment has overridden it. The
event's `at` is the reply's own time.

  record.py ISSUE_NUMBER [--repo owner/name] [--root DIR] [--apply]
  record.py --selftest

--repo defaults to the git remote of the current repository, --root to
its top-level directory (concept paths in issues are repository-
relative). Every edit and every GitHub write is printed in full and
dry-run unless --apply is given.
"""

import argparse
import difflib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True   # a sibling import leaves no __pycache__ in tools/
sys.path.insert(0, str(Path(__file__).resolve().parent))
import sign  # noqa: E402

TITLE_RE = re.compile(r"^\s*Confirm:\s*(\S+\.md)\s*$")
FORM_ANSWERS = {"confirmed as written": "confirmed", "needs a correction": "correction",
                "not my product or not my call": "not"}
WORDS = {"confirmed": "confirmed", "correction": "correction", "corrected": "correction", "not": "not"}
REMOTE_RE = re.compile(r"github\.com[:/]([^/\s]+)/([^/\s]+?)(?:\.git)?/?$")


def gh(args: list, dry_run: bool = False, payload: dict | None = None):
    """One `gh api` call; a write under dry_run is printed instead of
    made. Replaced by a fake in the selftest."""
    cmd = ["gh", "api", *args]
    if payload is not None:
        cmd += ["--input", "-"]
    if dry_run and (payload is not None or "-X" in args):
        print(f"  dry-run: {' '.join(cmd)}")
        return None
    r = subprocess.run(cmd, capture_output=True, text=True,
                       input=json.dumps(payload) if payload is not None else None)
    if r.returncode != 0:
        raise SystemExit(f"gh api failed: {' '.join(args)}: {(r.stderr or r.stdout).strip()[:400]}")
    return json.loads(r.stdout) if r.stdout.strip() else None


def git_top(start: Path):
    try:
        return Path(subprocess.run(["git", "-C", str(start), "rev-parse", "--show-toplevel"],
                                   capture_output=True, text=True, check=True).stdout.strip())
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def repo_from_remote(root: Path) -> str:
    try:
        url = subprocess.run(["git", "-C", str(root), "remote", "get-url", "origin"],
                             capture_output=True, text=True, check=True).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        raise SystemExit("--repo owner/name needed: no git remote named origin here")
    m = REMOTE_RE.search(url)
    if not m:
        raise SystemExit(f"--repo owner/name needed: remote {url} is not a GitHub repository")
    return f"{m.group(1)}/{m.group(2)}"


def form_sections(body: str) -> dict:
    """{heading: text} for an issue-form body (### headings)."""
    out = {}
    current = None
    for line in (body or "").split("\n"):
        m = re.match(r"^###\s+(.+?)\s*$", line)
        if m:
            current = m.group(1).strip().lower()
            out[current] = ""
        elif current is not None:
            out[current] += line + "\n"
    return {k: v.strip() for k, v in out.items()}


def concept_path(issue: dict):
    m = TITLE_RE.match(issue.get("title") or "")
    if m:
        return m.group(1)
    sections = form_sections(issue.get("body") or "")
    concept = sections.get("concept", "").split("\n")[0].strip().strip("`")
    return concept or None


def first_word(text: str):
    for tok in (text or "").split():
        word = re.sub(r"[^\w]", "", tok).lower()
        if word:
            return word
    return ""


def answer_of(comment_or_body: str):
    return WORDS.get(first_word(comment_or_body))


def find_answer(issue: dict, comments: list):
    """The answer to record: {kind, by, at, url, text} or None."""
    author = ((issue.get("user") or {}).get("login") or "").lower()
    form = "answer" in form_sections(issue.get("body") or "")
    for c in sorted(comments, key=lambda c: c.get("created_at") or "", reverse=True):
        login = ((c.get("user") or {}).get("login") or "")
        if (login.lower() == author) != form:
            continue
        kind = answer_of(c.get("body") or "")
        if kind:
            return {"kind": kind, "by": login, "at": c.get("created_at") or "",
                    "url": c.get("html_url") or "", "text": (c.get("body") or "").strip()}
    if form:
        sections = form_sections(issue.get("body") or "")
        kind = FORM_ANSWERS.get(sections.get("answer", "").split("\n")[0].strip().lower())
        if kind:
            text = sections.get("correction", "").strip()
            if text.lower() in ("", "_no response_"):
                text = ""
            return {"kind": kind, "by": (issue.get("user") or {}).get("login") or "",
                    "at": issue.get("created_at") or "", "url": issue.get("html_url") or "", "text": text}
    return None


def normalize_at(at: str) -> str:
    """GitHub's created_at (already UTC, whole seconds) as sign.py writes it."""
    m = re.match(r"^(\d{4}-\d{2}-\d{2})T(\d{2}:\d{2}:\d{2})", at or "")
    return f"{m.group(1)}T{m.group(2)}Z" if m else sign.now_utc()


def unmark_text(text: str) -> str:
    """The concept text without its `review:` frontmatter line."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return text
    try:
        end = lines.index("---", 1)
    except ValueError:
        return text
    keep = [ln for i, ln in enumerate(lines) if not (0 < i < end and re.match(r"review:(\s|$)", ln))]
    return "\n".join(keep)


def log_of(concept: Path, root: Path):
    """The bundle log beside the concept, knowledge/<bundle>/log.md."""
    rel = concept.resolve().relative_to(root.resolve()).parts
    if len(rel) >= 3 and rel[0] == "knowledge":
        log = root / rel[0] / rel[1] / "log.md"
        return log if log.is_file() else None
    return None


def show_diff(path: str, old: str, new: str) -> None:
    sys.stdout.writelines(difflib.unified_diff(old.splitlines(True), new.splitlines(True),
                                               f"a/{path}", f"b/{path}"))
    if not new.endswith("\n"):
        print()


def record(number: int, repo: str, root: Path, apply: bool) -> int:
    issue = gh([f"repos/{repo}/issues/{number}"]) or {}
    comments = gh([f"repos/{repo}/issues/{number}/comments?per_page=100"]) or []
    path = concept_path(issue)
    if not path:
        print(f"#{number} {issue.get('title', '')!r}: no concept path in the title (Confirm: <path>) or the form's Concept section")
        return 1
    concept = root / path
    print(f"#{number}: {issue.get('title', '')}")
    print(f"concept: {path}" + ("" if concept.is_file() else "  (NOT FOUND under " + root.as_posix() + ")"))
    ans = find_answer(issue, comments)
    if ans is None:
        print("no recognizable answer yet: waiting for a reply whose first word is confirmed, correction or not")
        return 1
    print(f"answer: {ans['kind']} by @{ans['by']} at {ans['at']}, {ans['url']}")
    if not concept.is_file():
        return 1
    text = concept.read_text(encoding="utf-8")
    if ans["kind"] == "confirmed":
        by = f"human:{ans['by']}"
        at = normalize_at(ans["at"])
        new, note = sign.sign_text(text, by, at, "provider", ans["url"])
        new = unmark_text(new)
        print(f"\n{'signing' if apply else 'would sign'} {path}: {note}" + ("; review: removed" if "review:" in text else ""))
        show_diff(path, text, new)
        files = [concept]
        log = log_of(concept, root)
        if log is not None:
            entry = sign.log_entry([path], f"confirmed as written on #{number}.", at[:10],
                                   first=note.startswith("first signature"), role="provider", by=by, source=ans["url"])
            print(f"\n{'adding to' if apply else 'would add to'} {log.relative_to(root).as_posix()}:\n{entry}")
            files.append(log)
            if apply:
                sign.add_log(log, entry)
        if apply:
            concept.write_text(new, encoding="utf-8")
        print(f"\n{'files to commit' if apply else 'files that would change'}: " + ", ".join(f.relative_to(root).as_posix() for f in files))
        print("re-render the digest (tools/digest.py knowledge/<bundle>) and commit it too")
        print(f"commit message: Confirm {path} (closes #{number})")
        if not apply:
            print("dry run; nothing written (add --apply)")
        return 0
    if ans["kind"] == "correction":
        print(f"\ncorrection for {path} from @{ans['by']}:")
        print("\n".join("  " + ln for ln in (ans["text"] or "(no text given)").split("\n")))
        print("\nnothing edited: fix the concept in its own pull request, ask again on the issue, "
              "and run record.py once they confirm the corrected text")
        return 0
    # not my product, not my call
    print(f"\n@{ans['by']} says it is not their product or not their call:")
    print("\n".join("  " + ln for ln in ans["text"].split("\n")))
    thanks = {"body": (f"Thank you, @{ans['by']}. We will ask elsewhere; if you know who would know "
                       f"this product, a name or a team here would help.")}
    print(f"\n{'commenting' if apply else 'would comment'} on #{number}: {thanks['body']}")
    gh(["-X", "POST", f"repos/{repo}/issues/{number}/comments"], not apply, thanks)
    if "review:" in text:
        new = unmark_text(text)
        print(f"{'removing' if apply else 'would remove'} review: from {path}")
        show_diff(path, text, new)
        if apply:
            concept.write_text(new, encoding="utf-8")
            print(f"files to commit: {path}")
    if not apply:
        print("dry run; nothing written (add --apply)")
    return 0


class FakeGitHub:
    """One issue with comments; records the writes record.py makes."""

    def __init__(self, issue: dict, comments: list):
        self.issue, self.comments, self.writes = issue, comments, []

    def __call__(self, args, dry_run=False, payload=None):
        path = args[-1]
        if payload is None and "-X" not in args:
            if path == f"repos/o/r/issues/{self.issue['number']}":
                return self.issue
            if path.startswith(f"repos/o/r/issues/{self.issue['number']}/comments"):
                return self.comments
            raise AssertionError(path)
        if dry_run:
            return None
        self.writes.append((args[1], path, payload))
        return {"id": 99}


def selftest() -> int:
    global gh
    import contextlib
    import io

    def user(login):
        return {"login": login}

    def comment(login, body, n, when="2026-09-10T12:00:00Z"):
        return {"user": user(login), "body": body, "created_at": when,
                "html_url": f"https://github.com/o/r/issues/7#issuecomment-{n}"}

    concept_text = ("---\ntype: dataset-gotcha\ntitle: A trap\nstatus: stable\n"
                    "review: https://github.com/o/r/issues/7\n"
                    "verified: { by: human:Steward, at: 2026-01-02T00:00:00Z }\n---\n\nBody.\n")
    solicited = {"number": 7, "title": "Confirm: knowledge/b/gotchas/trap.md", "user": user("maintainer"),
                 "body": "@ann We believe the following...", "created_at": "2026-09-09T00:00:00Z",
                 "html_url": "https://github.com/o/r/issues/7"}

    def run(issue, comments, apply=False, root=None):
        global gh
        fake = FakeGitHub(issue, comments)
        gh = fake
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rc = record(issue["number"], "o/r", root, apply)
        return rc, out.getvalue(), fake

    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        concept = root / "knowledge" / "b" / "gotchas" / "trap.md"
        concept.parent.mkdir(parents=True)
        log = root / "knowledge" / "b" / "log.md"
        log.write_text("# log\n\nNewest first.\n\n- 2026-01-01 · older entry\n", encoding="utf-8")

        def reset():
            concept.write_text(concept_text, encoding="utf-8")

        # no answer yet: the maintainer's own comment and an unrelated
        # reply do not count
        reset()
        rc, out, _ = run(solicited, [comment("maintainer", "Confirmed? Please have a look.", 1),
                                     comment("ann", "Looking at it this week.", 2)], root=root)
        assert rc == 1 and "no recognizable answer yet" in out, out
        # confirmed: the latest recognizable reply wins over an earlier
        # correction; the event is in the replier's name at the reply's
        # time with the reply as source; review: goes; the log entry, the
        # diff and the commit message are printed; dry run writes nothing
        replies = [comment("ann", "Correction: the fill value is wrong.", 2, "2026-09-10T10:00:00Z"),
                   comment("ann", "**Confirmed.** Right as written now.", 3, "2026-09-11T15:30:00Z")]
        rc, out, _ = run(solicited, replies, root=root)
        assert rc == 0 and "answer: confirmed by @ann at 2026-09-11T15:30:00Z, https://github.com/o/r/issues/7#issuecomment-3" in out, out
        assert "would sign knowledge/b/gotchas/trap.md: single event became a list of two; review: removed" in out, out
        assert ("-review: https://github.com/o/r/issues/7\n-verified: { by: human:Steward, at: 2026-01-02T00:00:00Z }\n"
                "+verified:\n+  - { by: human:Steward, at: 2026-01-02T00:00:00Z }\n"
                "+  - { by: human:ann, at: 2026-09-11T15:30:00Z, role: provider, "
                "source: https://github.com/o/r/issues/7#issuecomment-3 }\n") in out, out
        assert "would add to knowledge/b/log.md:\n- 2026-09-11 · PROVIDER CONFIRMATION of" in out, out
        assert "confirmed as written on #7." in out and "role provider\n  by human:ann" in out, out
        assert "commit message: Confirm knowledge/b/gotchas/trap.md (closes #7)" in out and "dry run" in out, out
        assert concept.read_text(encoding="utf-8") == concept_text and "older entry" in log.read_text() and "PROVIDER" not in log.read_text()
        rc, out, fake = run(solicited, replies, apply=True, root=root)
        assert rc == 0 and fake.writes == [] and "signing knowledge/b/gotchas/trap.md" in out, out
        new = concept.read_text(encoding="utf-8")
        assert "review:" not in new and new.endswith("---\n\nBody.\n"), new
        assert ("verified:\n  - { by: human:Steward, at: 2026-01-02T00:00:00Z }\n  - { by: human:ann, at: 2026-09-11T15:30:00Z, "
                "role: provider, source: https://github.com/o/r/issues/7#issuecomment-3 }\n---") in new, new
        assert log.read_text().index("PROVIDER CONFIRMATION") < log.read_text().index("older entry")
        assert "files to commit: knowledge/b/gotchas/trap.md, knowledge/b/log.md" in out, out
        # correction: printed with the path, nothing edited, even with --apply
        reset()
        rc, out, fake = run(solicited, [comment("ann", "correction, the fill value is -9999 not NaN; see the user guide section 4.", 2)],
                            apply=True, root=root)
        assert rc == 0 and "answer: correction by @ann" in out and "correction for knowledge/b/gotchas/trap.md from @ann:" in out, out
        assert "  correction, the fill value is -9999 not NaN; see the user guide section 4." in out and "nothing edited" in out, out
        assert concept.read_text(encoding="utf-8") == concept_text and fake.writes == []
        # not mine: printed; on --apply a thank-you comment and review: removed
        rc, out, fake = run(solicited, [comment("ann", "Not my product, try the SWOT team.", 2)], root=root)
        assert rc == 0 and "not their product" in out and "would comment on #7: Thank you, @ann." in out, out
        assert "would remove review:" in out and fake.writes == [] and concept.read_text(encoding="utf-8") == concept_text, out
        rc, out, fake = run(solicited, [comment("ann", "Not my product, try the SWOT team.", 2)], apply=True, root=root)
        assert rc == 0 and fake.writes == [("POST", "repos/o/r/issues/7/comments", {"body": "Thank you, @ann. We will ask elsewhere; "
                                                                                    "if you know who would know this product, a name or a team here would help."})], fake.writes
        assert "review:" not in concept.read_text(encoding="utf-8") and "files to commit: knowledge/b/gotchas/trap.md" in out, out
        # a form-opened issue: the concept comes from the form's Concept
        # section when the title carries none, the answer from the Answer
        # section, the person is the issue's author, and the correction
        # text is the Correction section
        reset()
        form_body = ("### Concept\n\nknowledge/b/gotchas/trap.md\n\n### Product\n\nAlpha\n\n"
                     "### Answer\n\nConfirmed as written\n\n### Correction\n\n_No response_\n\n### Affiliation\n\nThe data center\n")
        form = {"number": 7, "title": "A trap: looks right", "user": user("bea"), "body": form_body,
                "created_at": "2026-09-08T08:00:00Z", "html_url": "https://github.com/o/r/issues/7"}
        rc, out, _ = run(form, [], root=root)
        assert rc == 0 and "concept: knowledge/b/gotchas/trap.md" in out, out
        assert "answer: confirmed by @bea at 2026-09-08T08:00:00Z, https://github.com/o/r/issues/7" in out, out
        assert "+  - { by: human:bea, at: 2026-09-08T08:00:00Z, role: provider, source: https://github.com/o/r/issues/7 }" in out, out
        form_corr = dict(form, body=form_body.replace("Confirmed as written", "Needs a correction").replace("_No response_", "Units are cm, not m."))
        rc, out, _ = run(form_corr, [comment("maintainer", "Confirmed you mean the units attribute?", 1)], root=root)
        assert rc == 0 and "answer: correction by @bea" in out and "  Units are cm, not m." in out, out
        # the author's later comment overrides the form's answer; a
        # maintainer's comment never does
        rc, out, _ = run(form_corr, [comment("maintainer", "Confirmed you mean the units attribute?", 1),
                                     comment("bea", "Confirmed as written, now that the units are fixed.", 2, "2026-09-12T00:00:00Z")], root=root)
        assert rc == 0 and "answer: confirmed by @bea at 2026-09-12T00:00:00Z" in out, out
        form_not = dict(form, body=form_body.replace("Confirmed as written", "Not my product or not my call"))
        rc, out, _ = run(form_not, [], root=root)
        assert rc == 0 and "answer: not by @bea" in out and "would comment on #7: Thank you, @bea." in out, out
        # a form-opened issue with no answer, and a title with no path
        rc, out, _ = run(dict(form, body="### Concept\n\nknowledge/b/gotchas/trap.md\n\n### Answer\n\n\n"), [], root=root)
        assert rc == 1 and "no recognizable answer yet" in out, out
        rc, out, _ = run(dict(form, body="just a note"), [], root=root)
        assert rc == 1 and "no concept path" in out, out
        # a concept the issue names but the tree lacks
        rc, out, _ = run(dict(solicited, title="Confirm: knowledge/b/gotchas/gone.md"), replies, root=root)
        assert rc == 1 and "NOT FOUND" in out and "answer: confirmed by @ann" in out, out
    assert [answer_of(s) for s in ("CONFIRMED!", "**Corrected** now", "not mine", "Not my call", "Notably wrong", "I confirm", "")] == \
        ["confirmed", "correction", "not", "not", None, None, None]
    assert normalize_at("2026-09-11T15:30:00Z") == "2026-09-11T15:30:00Z" and normalize_at("2026-09-11T15:30:00+00:00") == "2026-09-11T15:30:00Z"
    assert unmark_text("---\na: 1\nreview: u\nb: 2\n---\nreview: kept in body\n") == "---\na: 1\nb: 2\n---\nreview: kept in body\n"
    print("record selftest: ok (no answer, confirmed, correction, not mine, the form-opened shape, "
          "dry run and --apply, the log entry, the commit message)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("issue", nargs="?", type=int, metavar="ISSUE_NUMBER")
    ap.add_argument("--repo", default=None, metavar="owner/name", help="default: the git remote of the current repository")
    ap.add_argument("--root", type=Path, default=None, metavar="DIR",
                    help="the repository top level the concept path is relative to (default: git's)")
    ap.add_argument("--apply", action="store_true", help="write the edit and the comment (default: print them)")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    if args.issue is None:
        ap.error("ISSUE_NUMBER required (or --selftest)")
    root = args.root or git_top(Path.cwd()) or Path.cwd()
    repo = args.repo or repo_from_remote(root)
    return record(args.issue, repo, root, args.apply)


if __name__ == "__main__":
    sys.exit(main())
