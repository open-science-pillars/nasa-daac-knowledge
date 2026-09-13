#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml"]
# ///
"""Open a "confirm this concept" issue for each selected concept, in
the maintainer's name, mentioning the people who know the product.

The confirm-or-correct link on a bundle's DIGEST.md asks a provider
person to open the issue themselves. This tool is the other direction
of the same loop: the maintainer picks the concepts, opens one issue
per concept with the concept rendered inline, and mentions the person;
the person replies on GitHub with one word (confirmed, correction, or
not, as in not my product); record.py then records the reply on the
concept as a verified event in their name, and the pull request that
carries it closes the issue.

  solicit.py BUNDLE_DIR --concept PATH [--concept PATH ...] --to @handle [...]
  solicit.py BUNDLE_DIR --product "<dataset concept title or path>" --to @handle
  solicit.py BUNDLE_DIR --unconfirmed --to @handle
  solicit.py ... [--repo owner/name] [--mark] [--apply]
  solicit.py --selftest

Selection, always within BUNDLE_DIR: --concept names a concept by any
path (repository-relative, bundle-relative or on disk); --product
names a dataset concept by its title or path and selects every concept
the digest joins to that product (digest.py's join, imported), the
dataset concept first; --unconfirmed selects every stable concept with
no provider event, and given together with --concept or --product it
narrows those instead. A concept that already has an open issue with
the `confirm` label and the title `Confirm: <path>` is skipped and
said so.

Each issue carries the title `Confirm: <repository-relative path>`,
the labels `knowledge` and `confirm`, a one-paragraph ask that mentions
the handles, the concept inline (title, type, severity, status, tier,
the body text as written, the sources) and a footer naming the path
and what happens to the reply. --repo defaults to the git remote of
the bundle's repository. Every GitHub write is printed in full and
dry-run unless --apply is given; the tool calls GitHub through `gh
api`, so the issues are opened as the maintainer's own login.

--mark writes `review: <issue url>` into each solicited concept's
frontmatter on --apply (the key the specification uses for a concept
under review; the digest shows it as Asked, and signature_check.py
does not count it as an edit), re-renders the bundle digest, and lists
the files to commit.
"""

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

sys.dont_write_bytecode = True   # a sibling import leaves no __pycache__ in tools/
sys.path.insert(0, str(Path(__file__).resolve().parent))
import digest  # noqa: E402

LABELS = ("knowledge", "confirm")
LABEL_COLOR = "0E8A16"
ANSWERS = "confirmed, correction, or not"
REMOTE_RE = re.compile(r"github\.com[:/]([^/\s]+)/([^/\s]+?)(?:\.git)?/?$")


def gh(args: list, dry_run: bool = False, payload: dict | None = None):
    """One `gh api` call; a write (a payload, or -X) under dry_run is
    printed instead of made. Replaced by a fake in the selftest."""
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


def repo_from_remote(bundle: Path) -> str:
    try:
        url = subprocess.run(["git", "-C", str(bundle), "remote", "get-url", "origin"],
                             capture_output=True, text=True, check=True).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        raise SystemExit("--repo owner/name needed: no git remote named origin here")
    m = REMOTE_RE.search(url)
    if not m:
        raise SystemExit(f"--repo owner/name needed: remote {url} is not a GitHub repository")
    return f"{m.group(1)}/{m.group(2)}"


def find_concept(ref: str, bundle: Path, prefix: str, concepts: list):
    """The concept a --concept argument names: a repository-relative
    path (knowledge/<bundle>/...), a bundle-relative one, or a path on
    disk; None when it names nothing in the bundle."""
    by_rel = {c.rel: c for c in concepts}
    ref = ref.replace("\\", "/")
    if ref.startswith(prefix + "/") and ref[len(prefix) + 1:] in by_rel:
        return by_rel[ref[len(prefix) + 1:]]
    if ref in by_rel:
        return by_rel[ref]
    p = Path(ref)
    if p.exists():
        try:
            rel = p.resolve().relative_to(bundle.resolve()).as_posix()
        except ValueError:
            return None
        return by_rel.get(rel)
    return None


def find_product(ref: str, bundle: Path, prefix: str, datasets: dict, concepts: list):
    """The dataset concept a --product argument names, by title
    (case-insensitive) or by any path form find_concept accepts."""
    c = find_concept(ref, bundle, prefix, concepts)
    if c is not None and c.rel in datasets:
        return c
    wanted = ref.strip().lower()
    for d in datasets.values():
        if d.title.lower() == wanted:
            return d
    return None


def is_stable(c) -> bool:
    return (c.status or "stable") == "stable"


def select(bundle: Path, prefix: str, concepts: list, datasets: dict,
           concept_refs: list, product_refs: list, unconfirmed: bool) -> list:
    """The concepts the arguments name, bundle order, each once."""
    chosen = []
    problems = []
    for ref in concept_refs:
        c = find_concept(ref, bundle, prefix, concepts)
        if c is None:
            problems.append(f"--concept {ref}: not a concept in {prefix}")
        elif c not in chosen:
            chosen.append(c)
    for ref in product_refs:
        d = find_product(ref, bundle, prefix, datasets, concepts)
        if d is None:
            names = ", ".join(sorted(x.title for x in datasets.values()))
            problems.append(f"--product {ref}: no dataset concept has that title or path (products: {names})")
            continue
        members = [d] + sorted((c for c in concepts if d.rel in c.products and c is not d),
                               key=lambda c: c.rel)
        chosen += [c for c in members if c not in chosen]
    if problems:
        raise SystemExit("\n".join(problems))
    if unconfirmed:
        pool = chosen if (concept_refs or product_refs) else sorted(concepts, key=lambda c: c.rel)
        chosen = [c for c in pool if is_stable(c) and c.tier != "provider-confirmed"]
    return chosen


def product_name(c, datasets: dict) -> str:
    names = [datasets[rel].title for rel in c.products if rel in datasets]
    if not names:
        return "the data this bundle describes"
    if len(names) == 1:
        return names[0]
    return ", ".join(names[:-1]) + " and " + names[-1]


def sources_of(c) -> list:
    out = []
    for s in c.fm.get("sources") or []:
        if not isinstance(s, dict):
            continue
        res = str(s.get("resource") or "").strip()
        title = str(s.get("title") or "").strip()
        out.append(f"- {title}: {res}" if res and title else f"- {res or title}")
    return out


def issue_title(path: str) -> str:
    return f"Confirm: {path}"


def issue_body(c, path: str, product: str, handles: list) -> str:
    mention = " ".join(h if h.startswith("@") else "@" + h for h in handles)
    ask = (f"{mention} We believe the following about {product}; you know it better than "
           f"we do. Would you reply here with one word: **confirmed** (the concept is right "
           f"as written), **correction** (something is wrong; say what, and where it is "
           f"documented), or **not** (not your product, or not your call)? A reply is all "
           f"that is asked: no tooling, no git, nothing to edit.")
    facts = [f"- Type: {c.type}"]
    if c.severity:
        facts.append(f"- Severity: {c.severity}")
    facts += [f"- Status: {c.status or 'stable'}", f"- Current tier: {c.tier}"]
    body = c.body.strip("\n")
    sources = sources_of(c)
    footer = (f"Concept: `{path}` in this repository. The maintainer records your reply on "
              f"the concept as a verified event in your name (`role: provider`) with a link "
              f"to the reply; the pull request that carries it closes this issue.")
    parts = [ask, "", "---", "", f"## {c.title}", "", *facts, "", body, ""]
    if sources:
        parts += ["### Sources", "", *sources, ""]
    parts += ["---", "", footer, ""]
    return "\n".join(parts)


def open_confirm_issues(repo: str) -> dict:
    """{title: html_url} of the repository's open issues labelled confirm."""
    out = {}
    page = 1
    while True:
        batch = gh([f"repos/{repo}/issues?state=open&labels=confirm&per_page=100&page={page}"]) or []
        for i in batch:
            if "pull_request" not in i:
                out[i.get("title", "")] = i.get("html_url", "")
        if len(batch) < 100:
            return out
        page += 1


def ensure_labels(repo: str, apply: bool) -> None:
    existing = {l["name"] for l in (gh([f"repos/{repo}/labels?per_page=100"]) or [])}
    for name in LABELS:
        if name not in existing:
            payload = {"name": name, "color": LABEL_COLOR,
                       "description": "A knowledge concept awaiting a provider's word"}
            print(f"label {name} missing in {repo}; {'creating' if apply else 'would create'} it")
            print("  " + json.dumps(payload))
            gh(["-X", "POST", f"repos/{repo}/labels"], not apply, payload)


def mark_text(text: str, url: str) -> str:
    """The concept text with `review: <url>` in its frontmatter: a
    present review line replaced, else one inserted after status, else
    before the closing fence."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        raise ValueError("no frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError:
        raise ValueError("frontmatter never closes")
    idx = next((i for i in range(1, end) if re.match(r"review:(\s|$)", lines[i])), None)
    if idx is not None:
        lines[idx] = f"review: {url}"
        return "\n".join(lines)
    anchor = next((i for i in range(1, end) if lines[i].startswith("status:")), None)
    lines.insert(anchor + 1 if anchor is not None else end, f"review: {url}")
    return "\n".join(lines)


def solicit(bundle: Path, concepts: list, datasets: dict, prefix: str, repo: str,
            handles: list, mark: bool, apply: bool) -> list:
    """Open one issue per concept; returns [(concept, issue url or None)]."""
    if not concepts:
        print("nothing selected")
        return []
    existing = open_confirm_issues(repo)
    ensure_labels(repo, apply)
    results = []
    for c in concepts:
        path = f"{prefix}/{c.rel}"
        title = issue_title(path)
        if title in existing:
            print(f"SKIP {path}: open confirm issue already exists, {existing[title]}")
            results.append((c, None))
            continue
        payload = {"title": title, "body": issue_body(c, path, product_name(c, datasets), handles),
                   "labels": list(LABELS)}
        print(f"\n== {'opening' if apply else 'would open'} issue in {repo}")
        print(f"title: {payload['title']}")
        print(f"labels: {', '.join(payload['labels'])}")
        print("body:")
        print("\n".join("  " + ln for ln in payload["body"].split("\n")))
        created = gh(["-X", "POST", f"repos/{repo}/issues"], not apply, payload)
        url = (created or {}).get("html_url") if apply else None
        if apply:
            print(f"opened {url}")
        results.append((c, url))
    if mark:
        touched = []
        for c, url in results:
            if url is None:
                continue
            c.path.write_text(mark_text(c.path.read_text(encoding="utf-8"), url), encoding="utf-8")
            touched.append(c.path)
        if not apply:
            print("\n--mark: would write review: <issue url> into each solicited concept (needs --apply)")
        elif touched:
            (bundle / "DIGEST.md").write_text(digest.render(bundle), encoding="utf-8")
            print("\nmarked; files to commit:")
            for p in touched + [bundle / "DIGEST.md"]:
                print(f"  {p.as_posix()}")
    skipped = sum(1 for c in concepts if issue_title(f"{prefix}/{c.rel}") in existing)
    n = len(concepts) - skipped
    print(f"\nsolicit: {n} issue{'s' if n != 1 else ''} "
          f"{'opened' if apply else 'would be opened (dry run; add --apply)'}, {skipped} skipped")
    return results


class FakeGitHub:
    """Answers the reads solicit.py makes and records its writes."""

    def __init__(self, open_titles=()):
        self.labels = [{"name": "knowledge"}]
        self.issues = [{"number": i + 1, "title": t, "state": "open", "labels": [{"name": "confirm"}],
                        "html_url": f"https://github.com/o/r/issues/{i + 1}"} for i, t in enumerate(open_titles)]
        self.writes = []

    def __call__(self, args, dry_run=False, payload=None):
        path = args[-1]
        if payload is None and "-X" not in args:
            if path.startswith("repos/o/r/labels"):
                return self.labels
            if path.startswith("repos/o/r/issues?"):
                return [i for i in self.issues if i["state"] == "open"] if "page=1" in path else []
            raise AssertionError(path)
        if dry_run:
            return None
        self.writes.append((args[1], path, payload))
        if path == "repos/o/r/labels":
            self.labels.append({"name": payload["name"]})
            return None
        if path == "repos/o/r/issues":
            issue = {"number": len(self.issues) + 1, "title": payload["title"], "body": payload["body"],
                     "labels": [{"name": n} for n in payload["labels"]], "state": "open"}
            issue["html_url"] = f"https://github.com/o/r/issues/{issue['number']}"
            self.issues.append(issue)
            return issue
        raise AssertionError(path)


def selftest() -> int:
    global gh
    import contextlib
    import io
    files = {
        "index.md": '---\nokf_version: "0.2"\n---\n# b\n',
        "datasets/alpha.md": ("---\ntype: dataset\ntitle: Alpha product\nstatus: stable\ntags: [alpha]\n"
                              "resource: https://podaac.jpl.nasa.gov/dataset/ALPHA_L4_TEMP_V4\n"
                              "verified: { by: human:Steward, at: 2026-01-02T00:00:00Z }\n---\nAlpha.\n"),
        "datasets/beta.md": ("---\ntype: dataset\ntitle: Beta reference\nstatus: draft\ntags: [beta]\n---\nBeta.\n"),
        "gotchas/trap.md": ("---\ntype: dataset-gotcha\ntitle: A trap\nseverity: high\nstatus: stable\n"
                            "dataset: ../datasets/alpha.md\n"
                            "verified: { by: human:Steward, at: 2026-01-02T00:00:00Z }\n"
                            "sources:\n  - { id: a, resource: https://example.org/a, title: Source A }\n"
                            "  - { id: b, resource: https://example.org/b }\n"
                            "---\n\n# A trap\n\n**Mechanism.** The trap, as written.[^a]\n\n[^a]: Source A\n"),
        "gotchas/confirmed.md": ("---\ntype: dataset-gotcha\ntitle: Already confirmed\nseverity: low\nstatus: stable\n"
                                 "dataset: ../datasets/alpha.md\n"
                                 "verified:\n  - { by: human:Steward, at: 2026-01-02T00:00:00Z }\n"
                                 "  - { by: human:Prov, at: 2026-02-03T00:00:00Z, role: provider, "
                                 "source: https://github.com/o/r/issues/1#issuecomment-1 }\n---\nDone.\n"),
        "gotchas/draft.md": ("---\ntype: dataset-gotcha\ntitle: A draft\nstatus: draft\n"
                             "dataset: ../datasets/alpha.md\n---\nDraft.\n"),
        "conventions/doctrine.md": ("---\ntype: convention\ntitle: A doctrine\nstatus: stable\n"
                                    "---\nNames no product.\n"),
        "recipes/method.md": ("---\ntype: recipe\ntitle: A method\nstatus: stable\n"
                              "inputs:\n  - dataset: ../datasets/beta.md\n---\nUses beta.\n"),
        "log.md": "# log\n",
    }
    with tempfile.TemporaryDirectory() as d:
        bundle = Path(d) / "knowledge" / "b"
        for rel, text in files.items():
            (bundle / rel).parent.mkdir(parents=True, exist_ok=True)
            (bundle / rel).write_text(text, encoding="utf-8")
        (bundle / "DIGEST.md").write_text(digest.render(bundle), encoding="utf-8")
        concepts = digest.load(bundle)
        datasets = digest.join(bundle, concepts)
        prefix = "knowledge/b"
        rels = lambda cs: [c.rel for c in cs]  # noqa: E731
        # selection: by concept in three path forms, by product title and
        # path, by --unconfirmed alone and as a narrowing
        assert rels(select(bundle, prefix, concepts, datasets, ["knowledge/b/gotchas/trap.md"], [], False)) == ["gotchas/trap.md"]
        assert rels(select(bundle, prefix, concepts, datasets, ["gotchas/trap.md", str(bundle / "gotchas" / "trap.md")], [], False)) == ["gotchas/trap.md"]
        assert rels(select(bundle, prefix, concepts, datasets, [], ["alpha product"], False)) == \
            ["datasets/alpha.md", "gotchas/confirmed.md", "gotchas/draft.md", "gotchas/trap.md"]
        assert rels(select(bundle, prefix, concepts, datasets, [], ["datasets/beta.md"], False)) == ["datasets/beta.md", "recipes/method.md"]
        assert rels(select(bundle, prefix, concepts, datasets, [], [], True)) == \
            ["conventions/doctrine.md", "datasets/alpha.md", "gotchas/trap.md", "recipes/method.md"]
        assert rels(select(bundle, prefix, concepts, datasets, [], ["Alpha product"], True)) == ["datasets/alpha.md", "gotchas/trap.md"]
        for bad in (["nowhere.md"], ["../../index.md"]):
            try:
                select(bundle, prefix, concepts, datasets, bad, [], False)
            except SystemExit as e:
                assert "not a concept" in str(e), e
            else:
                raise AssertionError(bad)
        try:
            select(bundle, prefix, concepts, datasets, [], ["Gamma"], False)
        except SystemExit as e:
            assert "no dataset concept" in str(e) and "Alpha product" in str(e), e
        else:
            raise AssertionError("product")
        # the body: the ask mentions the handles and the product, the
        # concept follows inline with its facts, text and sources, the
        # footer names the path
        trap = next(c for c in concepts if c.rel == "gotchas/trap.md")
        body = issue_body(trap, "knowledge/b/gotchas/trap.md", product_name(trap, datasets), ["@ann", "bob"])
        assert body.startswith("@ann @bob We believe the following about Alpha product;"), body
        assert "**confirmed**" in body and "**correction**" in body and "**not**" in body, body
        assert "\n## A trap\n\n- Type: dataset-gotcha\n- Severity: high\n- Status: stable\n- Current tier: human-reviewed\n" in body, body
        assert "\n# A trap\n\n**Mechanism.** The trap, as written.[^a]\n\n[^a]: Source A\n" in body, body
        assert "### Sources\n\n- Source A: https://example.org/a\n- https://example.org/b\n" in body, body
        assert body.rstrip().endswith("closes this issue.") and "`knowledge/b/gotchas/trap.md`" in body, body
        doctrine = next(c for c in concepts if c.rel == "conventions/doctrine.md")
        dbody = issue_body(doctrine, "knowledge/b/conventions/doctrine.md", product_name(doctrine, datasets), ["x"])
        assert "about the data this bundle describes;" in dbody and "- Severity" not in dbody and "### Sources" not in dbody, dbody
        # a dry run reads, prints the issue in full and writes nothing
        fake = FakeGitHub(open_titles=["Confirm: knowledge/b/datasets/alpha.md"])
        gh = fake
        chosen = select(bundle, prefix, concepts, datasets, [], ["Alpha product"], True)
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            res = solicit(bundle, chosen, datasets, prefix, "o/r", ["@ann"], True, False)
        text = out.getvalue()
        assert fake.writes == [] and len(fake.issues) == 1, fake.writes
        assert "SKIP knowledge/b/datasets/alpha.md: open confirm issue already exists, https://github.com/o/r/issues/1" in text, text
        assert "would open issue in o/r\ntitle: Confirm: knowledge/b/gotchas/trap.md\nlabels: knowledge, confirm\nbody:\n  @ann We believe" in text, text
        assert "label confirm missing in o/r; would create it" in text and '"name": "confirm"' in text, text
        assert "would write review:" in text and "1 issue would be opened (dry run; add --apply), 1 skipped" in text, text
        assert [u for _, u in res] == [None, None] and "review:" not in (bundle / "gotchas" / "trap.md").read_text()
        # --apply opens the issue, creates the missing label, marks the
        # concept and re-renders the digest
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            res = solicit(bundle, chosen, datasets, prefix, "o/r", ["@ann"], True, True)
        text = out.getvalue()
        assert [w[:2] for w in fake.writes] == [("POST", "repos/o/r/labels"), ("POST", "repos/o/r/issues")], fake.writes
        assert fake.writes[0][2]["name"] == "confirm"
        issue = fake.issues[-1]
        assert issue["title"] == "Confirm: knowledge/b/gotchas/trap.md" and [l["name"] for l in issue["labels"]] == ["knowledge", "confirm"]
        assert res[1][1] == "https://github.com/o/r/issues/2" and "opened https://github.com/o/r/issues/2" in text, text
        marked = (bundle / "gotchas" / "trap.md").read_text(encoding="utf-8")
        assert "\nstatus: stable\nreview: https://github.com/o/r/issues/2\ndataset:" in marked, marked
        assert marked.endswith(files["gotchas/trap.md"].split("---\n", 2)[2]) and "1 issue opened, 1 skipped" in text, text
        assert f"  {(bundle / 'gotchas' / 'trap.md').as_posix()}\n  {(bundle / 'DIGEST.md').as_posix()}" in text, text
        assert "[Asked](https://github.com/o/r/issues/2)" in (bundle / "DIGEST.md").read_text(encoding="utf-8")
        # a second run skips the concept now that its issue is open
        fake.labels.append({"name": "confirm"})
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            solicit(bundle, chosen, datasets, prefix, "o/r", ["@ann"], False, True)
        assert "SKIP knowledge/b/gotchas/trap.md" in out.getvalue() and len(fake.issues) == 2
        # mark_text: a present review line is replaced; a concept with no
        # status line gets the key before the closing fence
        again = mark_text(marked, "https://github.com/o/r/issues/3")
        assert again.count("review:") == 1 and "review: https://github.com/o/r/issues/3" in again, again
        assert mark_text("---\ntype: x\n---\nBody\n", "u") == "---\ntype: x\nreview: u\n---\nBody\n"
        for bad in ("no frontmatter\n", "---\ntype: x\nnever closes\n"):
            try:
                mark_text(bad, "u")
            except ValueError:
                pass
            else:
                raise AssertionError(bad)
    assert REMOTE_RE.search("git@github.com:o/r.git").groups() == ("o", "r")
    assert REMOTE_RE.search("https://github.com/o/r").groups() == ("o", "r")
    assert REMOTE_RE.search("https://github.com/o/r.git/").groups() == ("o", "r")
    print("solicit selftest: ok (selection by concept, product and --unconfirmed; the issue body; "
          "dry run prints and writes nothing; --apply opens, labels, marks and re-renders; open issue skipped)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("bundle", nargs="?", type=Path, help="the bundle directory, knowledge/<bundle>")
    ap.add_argument("--concept", action="append", default=[], metavar="PATH",
                    help="a concept to ask about (repeatable; any path form)")
    ap.add_argument("--product", action="append", default=[], metavar="TITLE_OR_PATH",
                    help="a dataset concept, by title or path: every concept the digest joins to it")
    ap.add_argument("--unconfirmed", action="store_true",
                    help="every stable concept with no provider event (narrows --concept and --product when given with them)")
    ap.add_argument("--to", action="append", default=[], metavar="@handle",
                    help="a GitHub handle to mention (repeatable)")
    ap.add_argument("--repo", default=None, metavar="owner/name", help="default: the bundle's git remote")
    ap.add_argument("--mark", action="store_true",
                    help="on --apply, write review: <issue url> into each solicited concept and re-render the digest")
    ap.add_argument("--apply", action="store_true", help="open the issues (default: print them and write nothing)")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    if args.bundle is None or not args.bundle.is_dir():
        ap.error("BUNDLE_DIR required (or --selftest)")
    if not (args.concept or args.product or args.unconfirmed):
        ap.error("select concepts with --concept, --product or --unconfirmed")
    if not args.to:
        ap.error("--to @handle names who is asked (repeatable)")
    bundle = args.bundle
    concepts = digest.load(bundle)
    datasets = digest.join(bundle, concepts)
    prefix = digest.repo_relative(bundle)
    chosen = select(bundle, prefix, concepts, datasets, args.concept, args.product, args.unconfirmed)
    repo = args.repo or repo_from_remote(bundle)
    solicit(bundle, chosen, datasets, prefix, repo, args.to, args.mark, args.apply)
    return 0


if __name__ == "__main__":
    sys.exit(main())
