#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml"]
# ///
"""Render a bundle's DIGEST.md: what the bundle claims about each
product, as the page a data provider's person reads first.

A provider person does not read a hundred concepts to find the ones
about their product. The digest lists, product by product, every
concept in the bundle that names that product, one row each: the
concept (linked), its type, severity where it has one, status, trust
tier, the date of its latest verified event, how many sources it
cites, and a "Confirm or correct" link that opens the organization's
confirm_concept issue form with the concept and product filled in.
Answering that issue is the first rung of the provenance ladder
(consulted); the steward then records the answer as a verified event
with `sign.py --role provider --by human:<them> --source <the reply>`.
The counts per tier at the top say how much of the bundle has been
confirmed by anyone, and by a provider.

The products are the bundle's `type: dataset` concepts. A concept is
listed under a product when it names it, by any join the bundle uses:

  - a path to the dataset concept anywhere in its frontmatter (a
    gotcha's `dataset`, a recipe's `inputs[].dataset`, a source's
    `resource`, a finding's `confrontation.observation`, `subject`,
    `bears_on`) or in a body link, resolved as OKF path fields are
    (bundle-absolute with a leading slash, else relative to the
    concept, else to the bundle root);
  - the fields directory convention: `fields/<name>/...` describes the
    collections of `datasets/<name>.md`;
  - a CMR ShortName the product declares, the last path segment of a
    `podaac.jpl.nasa.gov/dataset/` resource URL on the dataset concept
    or on one of its fields concepts, named in the concept's text
    either whole or as a family prefix at a separator boundary
    (ECCO_L4_HEAT_FLUX names ECCO_L4_HEAT_FLUX_LLC0090GRID_MONTHLY_V4R4);
  - a shared tag that names the product: the dataset concept's file
    stem (nasa-ssh) or the stem's first word (ecco, swot, grace, opera,
    rapid, ghrsst), present in the dataset's own `tags` and in the
    concept's; the bundle tags every ECCO computation and recipe
    `ecco`, and that tag is how they name the product.

A concept that names no product goes in the final section, with the
same link; a dataset concept is listed first under its own product.
The trust tiers follow check_okf_v02.py: unverified (no event),
machine-confirmed (process events only), human-reviewed (a `human:`
event), provider-confirmed (a `human:` event with `role: provider`).

  digest.py BUNDLE_DIR            write knowledge/<bundle>/DIGEST.md
  digest.py BUNDLE_DIR --check    exit 1 when the committed digest differs
  digest.py BUNDLE_DIR --stdout   print instead of writing
  digest.py --selftest

The digest is rendered, never edited: the check routine runs --check
on every bundle, so a concept change lands with its digest.
"""

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import urlencode

import yaml

ISSUES_URL = "https://github.com/open-science-pillars/nasa-daac-knowledge/issues/new"
ISSUE_TEMPLATE = "confirm_concept.yml"
TITLE = "What this bundle claims about your products"
NOT_CONCEPTS = {"index.md", "log.md", "DIGEST.md"}
DATASET_TYPE = "dataset"
SHORTNAME_URL = re.compile(r"https?://podaac\.jpl\.nasa\.gov/dataset/([A-Za-z0-9_.-]+)")
TOKEN_RE = re.compile(r"(?<![\w.-])[A-Z][A-Z0-9]*(?:[_-][A-Za-z0-9.]+)+(?![\w-])")
MD_PATH_LINK = re.compile(r"\]\(([^)\s#]+\.md)(?:#[^)]*)?\)")
MIN_PREFIX = 10   # a family prefix shorter than this is a word, not a ShortName
TIERS = ("unverified", "machine-confirmed", "human-reviewed", "provider-confirmed")


def split_frontmatter(text: str):
    if not text.startswith("---"):
        return None, text
    lines = text.split("\n")
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[1:i]), "\n".join(lines[i + 1:])
    return None, text


def events_of(fm: dict) -> list:
    ver = fm.get("verified")
    events = ver if isinstance(ver, list) else [ver] if ver else []
    return [e for e in events if isinstance(e, dict)]


def tier(fm: dict) -> str:
    events = events_of(fm)
    humans = [e for e in events if str(e.get("by", "")).startswith("human:")]
    if any(e.get("role") == "provider" for e in humans):
        return "provider-confirmed"
    if humans:
        return "human-reviewed"
    return "machine-confirmed" if events else "unverified"


def latest_verified(fm: dict) -> str:
    dates = []
    for e in events_of(fm):
        at = e.get("at")
        if at is None:
            continue
        s = at.strftime("%Y-%m-%d") if hasattr(at, "strftime") else str(at)[:10]
        dates.append(s)
    return max(dates) if dates else ""


def strings_in(obj):
    """Every string value in a frontmatter tree."""
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from strings_in(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from strings_in(v)


def resolve(ref: str, concept: Path, bundle: Path):
    """An OKF path field: bundle-absolute with a leading slash, else
    relative to the concept, else to the bundle root; None when the
    reference is not a path into the bundle."""
    if "://" in ref:
        return None
    ref = ref.split("#", 1)[0]
    if ref.startswith("/"):
        cand = bundle / ref.lstrip("/")
    else:
        cand = concept.parent / ref
        if not cand.exists():
            cand = bundle / ref
    try:
        return cand.resolve().relative_to(bundle.resolve()).as_posix()
    except ValueError:
        return None


class Concept:
    def __init__(self, bundle: Path, path: Path, fm: dict, raw_fm: str, body: str):
        self.path = path
        self.rel = path.relative_to(bundle).as_posix()
        self.fm = fm
        self.text = raw_fm + "\n" + body
        self.body = body
        self.type = str(fm.get("type") or "").strip()
        self.title = str(fm.get("title") or path.stem).strip()
        self.status = str(fm.get("status") or "").strip()
        self.severity = str(fm.get("severity") or "").strip()
        self.tier = tier(fm)
        self.verified = latest_verified(fm)
        sources = fm.get("sources")
        self.sources = len(sources) if isinstance(sources, list) else 0
        self.products: list = []


def load(bundle: Path) -> list:
    out = []
    for path in sorted(bundle.rglob("*.md")):
        if path.name in NOT_CONCEPTS:
            continue
        raw, body = split_frontmatter(path.read_text(encoding="utf-8"))
        if raw is None:
            continue
        try:
            fm = yaml.safe_load(raw) or {}
        except yaml.YAMLError:
            continue
        if isinstance(fm, dict) and fm.get("type"):
            out.append(Concept(bundle, path, fm, raw, body))
    return out


def shortnames(dataset: Concept, concepts: list) -> set:
    """The CMR ShortNames a product declares: its own resource URL and
    those of its fields concepts."""
    names = set()
    stem = Path(dataset.rel).stem
    for c in [dataset] + [c for c in concepts if c.rel.startswith(f"fields/{stem}/")]:
        res = c.fm.get("resource")
        if isinstance(res, str):
            m = SHORTNAME_URL.match(res)
            if m:
                names.add(m.group(1))
    return names


def product_tags(dataset: Concept) -> set:
    """The tags by which a product is named: its file stem and the
    stem's first word, when the dataset concept itself carries them."""
    tags = dataset.fm.get("tags")
    tags = {str(t) for t in tags} if isinstance(tags, list) else set()
    stem = Path(dataset.rel).stem
    return {t for t in (stem, stem.split("-")[0]) if t in tags}


def names_shortname(token: str, name: str) -> bool:
    if token == name:
        return True
    if len(token) < MIN_PREFIX:
        return False
    return name.startswith(token) and name[len(token)] in "_-"


def join(bundle: Path, concepts: list) -> dict:
    """Attach each concept to the products it names; returns {dataset
    rel: Concept} for the products."""
    datasets = {c.rel: c for c in concepts if c.type == DATASET_TYPE}
    declared = {rel: shortnames(d, concepts) for rel, d in datasets.items()}
    by_tag = {rel: product_tags(d) for rel, d in datasets.items()}
    for c in concepts:
        if c.type == DATASET_TYPE:
            c.products = [c.rel]
            continue
        ctags = c.fm.get("tags")
        ctags = {str(t) for t in ctags} if isinstance(ctags, list) else set()
        found = {rel for rel, tags in by_tag.items() if tags & ctags}
        refs = [s for s in strings_in(c.fm) if s.endswith(".md") or ".md#" in s]
        refs += MD_PATH_LINK.findall(c.body)
        for ref in refs:
            target = resolve(ref, c.path, bundle)
            if target in datasets:
                found.add(target)
        parts = c.rel.split("/")
        if parts[0] == "fields" and len(parts) >= 3 and f"datasets/{parts[1]}.md" in datasets:
            found.add(f"datasets/{parts[1]}.md")
        tokens = set(TOKEN_RE.findall(c.text))
        for rel, names in declared.items():
            if rel in found:
                continue
            if any(names_shortname(t, n) for t in tokens for n in names):
                found.add(rel)
        c.products = sorted(found)
    return datasets


def repo_relative(bundle: Path) -> str:
    """The bundle path as the organization cites it (knowledge/<bundle>),
    from the enclosing git repository; the bundle name alone outside one."""
    try:
        top = subprocess.run(["git", "-C", str(bundle), "rev-parse", "--show-toplevel"],
                             capture_output=True, text=True, check=True).stdout.strip()
        return bundle.resolve().relative_to(Path(top).resolve()).as_posix()
    except (subprocess.CalledProcessError, FileNotFoundError, ValueError):
        return bundle.name


def confirm_link(concept_path: str, product: str) -> str:
    params = {"template": ISSUE_TEMPLATE, "title": f"Confirm: {concept_path}", "concept": concept_path}
    if product:
        params["product"] = product
    return f"{ISSUES_URL}?{urlencode(params)}"


def cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def row(c: Concept, prefix: str, product: str) -> str:
    link = confirm_link(f"{prefix}/{c.rel}", product)
    return (f"| [{cell(c.title)}]({c.rel}) | {cell(c.type)} | {cell(c.severity)} | {cell(c.status)} "
            f"| {c.tier} | {c.verified} | {c.sources} | [Confirm or correct]({link}) |")


HEADER = ("| Concept | Type | Severity | Status | Tier | Latest verified | Sources | |\n"
          "|---|---|---|---|---|---|---|---|")


def render(bundle: Path) -> str:
    concepts = load(bundle)
    datasets = join(bundle, concepts)
    prefix = repo_relative(bundle)
    counts = {t: 0 for t in TIERS}
    for c in concepts:
        counts[c.tier] += 1
    lines = [f"# {TITLE}", "",
             f"The `{bundle.name}` bundle, concept by concept, grouped by the product each "
             "one names. Rendered by `tools/digest.py` from the concepts' frontmatter; "
             "never edited by hand (the check routine fails when this page is stale).", "",
             "If you know one of these products, each row's last link opens an issue "
             "with the concept and product filled in: say whether the claim is right, "
             "and correct it if not. Your answer is recorded on the concept as a "
             "verified event in your name, with a link to your reply.", "",
             "## Summary", "",
             f"{len(concepts)} concepts, {len(datasets)} products.", ""]
    for t in TIERS:
        lines.append(f"- {t}: {counts[t]}")
    lines += ["",
              "A tier reads the concept's verified events: unverified (none), "
              "machine-confirmed (process events only), human-reviewed (a person signed), "
              "provider-confirmed (a person from the organization that produces the data "
              "confirmed it).", ""]
    for rel in sorted(datasets, key=lambda r: datasets[r].title.lower()):
        d = datasets[rel]
        members = [c for c in concepts if rel in c.products and c is not d]
        lines += [f"## {d.title}", "",
                  f"[{cell(d.rel)}]({d.rel}): {len(members) + 1} concept" + ("s" if members else "") + ".", "",
                  HEADER, row(d, prefix, d.title)]
        lines += [row(c, prefix, d.title) for c in sorted(members, key=lambda c: c.rel)]
        lines.append("")
    rest = [c for c in concepts if not c.products]
    lines += ["## Concepts that name no product", "",
              "Conventions, requirements, method concepts and anything whose claim is not "
              "about one product. The same link applies: confirm or correct.", ""]
    if rest:
        lines += [HEADER] + [row(c, prefix, "") for c in sorted(rest, key=lambda c: c.rel)]
    else:
        lines.append("None.")
    return "\n".join(lines) + "\n"


def selftest() -> int:
    url = "https://github.com/open-science-pillars/nasa-daac-knowledge/issues/9#issuecomment-1"
    files = {
        "index.md": '---\nokf_version: "0.2"\n---\n# b\n',
        "datasets/alpha.md": ("---\ntype: dataset\ntitle: Alpha product\nstatus: stable\ntags: [alpha, state-estimate]\n"
                              "resource: https://podaac.jpl.nasa.gov/dataset/ALPHA_L4_TEMP_SALINITY_LLC0090GRID_MONTHLY_V4R4\n"
                              "verified: { by: human:Steward, at: 2026-01-02T00:00:00Z }\n---\nAlpha.\n"),
        "datasets/beta.md": ("---\ntype: dataset\ntitle: Beta reference\nstatus: draft\ntags: [altimetry, beta-ref]\n"
                             "resource: https://doi.org/10.5067/EXAMPLE\n---\nBeta.\n"),
        "computations/attested.md": ("---\ntype: Attested Computation\ntitle: An attested run\nstatus: stable\n"
                                     "tags: [alpha, budget, attested]\n"
                                     "verified: { by: human:Steward, at: 2026-01-06T00:00:00Z }\n---\nRun.\n"),
        "conventions/altimetry.md": ("---\ntype: convention\ntitle: Altimetry doctrine\nstatus: draft\n"
                                     "tags: [altimetry, state-estimate]\n---\nNames no product: a shared "
                                     "tag joins only when it is the product's stem or first word.\n"),
        "fields/alpha/heat.md": ("---\ntype: Data Collection\ntitle: Alpha heat flux\nstatus: stable\n"
                                 "resource: https://podaac.jpl.nasa.gov/dataset/ALPHA_L4_HEAT_FLUX_LLC0090GRID_MONTHLY_V4R4\n"
                                 "verified: { by: process:sweep, at: 2026-01-01T00:00:00Z }\n---\nHeat.\n"),
        "gotchas/trap.md": ("---\ntype: dataset-gotcha\ntitle: \"A trap | with a pipe\"\nseverity: high\nstatus: stable\n"
                            "dataset: ../datasets/alpha.md\n"
                            "verified:\n  - { by: human:Steward, at: 2026-01-02T00:00:00Z }\n"
                            f"  - {{ by: human:Provider, at: 2026-02-03T00:00:00Z, role: provider, source: {url} }}\n"
                            "sources:\n  - { id: a, resource: https://example.org/a }\n  - { id: b, resource: https://example.org/b }\n"
                            "---\nTrap.\n"),
        "recipes/method.md": ("---\ntype: recipe\ntitle: A method\nstatus: stable\n"
                              "inputs:\n  - dataset: ../datasets/beta.md\n"
                              "verified: { by: human:Steward, at: 2026-01-05T00:00:00Z, role: maintainer }\n"
                              "---\nUses ALPHA_L4_HEAT_FLUX for the flux and ALPHA_L4_TEMP_SALINITY_LLC0090GRID_SNAPSHOT_V4R4.\n"),
        "findings/claim.md": ("---\ntype: finding\ntitle: A claim\nstatus: draft\n"
                              "confrontation: { status: confronted, observation: /datasets/beta.md }\n---\nClaim.\n"),
        "conventions/doctrine.md": ("---\ntype: convention\ntitle: A doctrine\nstatus: stable\n"
                                    "verified: { by: human:Steward, at: 2026-01-02T00:00:00Z }\n"
                                    "---\nSee [the trap](../gotchas/trap.md); nothing about a product.\n"),
        "log.md": "# log\n",
    }
    with tempfile.TemporaryDirectory() as d:
        bundle = Path(d) / "knowledge" / "b"
        for rel, text in files.items():
            (bundle / rel).parent.mkdir(parents=True, exist_ok=True)
            (bundle / rel).write_text(text, encoding="utf-8")
        text = render(bundle)
        assert text.startswith(f"# {TITLE}\n"), text
        assert "9 concepts, 2 products." in text, text
        # beta, the finding and the altimetry doctrine carry no event; the
        # fields concept a process event; alpha, the recipe, the computation
        # and the doctrine a human event; the gotcha a provider event
        assert "- unverified: 3\n- machine-confirmed: 1\n- human-reviewed: 4\n- provider-confirmed: 1\n" in text, text
        alpha = text[text.index("## Alpha product"):text.index("## Beta reference")]
        beta = text[text.index("## Beta reference"):text.index("## Concepts that name no product")]
        rest = text[text.index("## Concepts that name no product"):]
        # the dataset concept leads its own section; the gotcha joins by `dataset`,
        # the fields concept by directory, the recipe by a ShortName family
        # prefix, the computation by the product's tag
        assert alpha.count("\n| [") == 5 and alpha.index("[datasets/alpha.md]") < alpha.index("gotchas/trap.md"), alpha
        for rel in ("fields/alpha/heat.md", "gotchas/trap.md", "recipes/method.md", "computations/attested.md"):
            assert f"]({rel})" in alpha, (rel, alpha)
        # the recipe joins beta by inputs[].dataset, the finding by
        # confrontation.observation; a tag that is not the product's name
        # (altimetry, state-estimate) joins nothing
        assert beta.count("\n| [") == 3 and "recipes/method.md" in beta and "findings/claim.md" in beta, beta
        assert "gotchas/trap.md" not in beta and "conventions/altimetry.md" not in beta
        # a body link to a gotcha is not a product; the doctrines name none
        assert rest.count("\n| [") == 2 and "conventions/doctrine.md" in rest and "conventions/altimetry.md" in rest, rest
        # the row: escaped title, severity, status, tier, date, source count, the link
        assert ("| [A trap \\| with a pipe](gotchas/trap.md) | dataset-gotcha | high | stable "
                "| provider-confirmed | 2026-02-03 | 2 | [Confirm or correct](") in alpha, alpha
        assert "| machine-confirmed | 2026-01-01 | 0 |" in alpha and "| unverified |  | 0 |" in beta, text
        link = re.search(r"\[Confirm or correct\]\((\S+)\)", alpha.split("gotchas/trap.md")[1]).group(1)
        assert link.startswith(f"{ISSUES_URL}?template={ISSUE_TEMPLATE}&"), link
        assert "title=Confirm%3A+b%2Fgotchas%2Ftrap.md" in link and "concept=b%2Fgotchas%2Ftrap.md" in link, link
        assert "product=Alpha+product" in link, link
        doctrine_link = re.search(r"\[Confirm or correct\]\((\S+)\)", rest).group(1)
        assert "product=" not in doctrine_link, doctrine_link
        # the digest, once present, is not a concept and does not change the render
        (bundle / "DIGEST.md").write_text(text, encoding="utf-8")
        assert render(bundle) == text
        # --check passes on the written digest and fails on a stale one
        cmd = [sys.executable, __file__, str(bundle)]
        r = subprocess.run(cmd + ["--check"], capture_output=True, text=True)
        assert r.returncode == 0 and "up to date" in r.stdout, r.stdout + r.stderr
        (bundle / "gotchas" / "trap.md").write_text(files["gotchas/trap.md"].replace("severity: high", "severity: medium"),
                                                    encoding="utf-8")
        r = subprocess.run(cmd + ["--check"], capture_output=True, text=True)
        assert r.returncode == 1 and "stale" in r.stdout, r.stdout + r.stderr
        r = subprocess.run(cmd + ["--stdout"], capture_output=True, text=True)
        assert r.returncode == 0 and "| medium |" in r.stdout and not (bundle / "DIGEST.md").read_text().count("| medium |")
        r = subprocess.run(cmd, capture_output=True, text=True)
        assert r.returncode == 0 and "| medium |" in (bundle / "DIGEST.md").read_text(encoding="utf-8"), r.stdout
        r = subprocess.run(cmd + ["--check"], capture_output=True, text=True)
        assert r.returncode == 0, r.stdout + r.stderr
        (bundle / "DIGEST.md").unlink()
        r = subprocess.run(cmd + ["--check"], capture_output=True, text=True)
        assert r.returncode == 1 and "missing" in r.stdout, r.stdout + r.stderr
    assert names_shortname("ALPHA_L4_HEAT", "ALPHA_L4_HEAT_FLUX_X") and not names_shortname("ALPHA_L4_HE", "ALPHA_L4_HEAT_FLUX_X")
    assert not names_shortname("ALPHA_L4_HEAT_FLUX_X", "ALPHA_L4_HEAT") and not names_shortname("SHORT_A", "SHORT_A_B")
    print("digest selftest: ok (joins by path, directory and ShortName; tiers; links; --check; --stdout)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("bundle", nargs="?", type=Path)
    ap.add_argument("--check", action="store_true", help="exit 1 when the committed DIGEST.md differs")
    ap.add_argument("--stdout", action="store_true", help="print the digest instead of writing it")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    if args.bundle is None or not args.bundle.is_dir():
        ap.error("BUNDLE_DIR required (or --selftest)")
    text = render(args.bundle)
    target = args.bundle / "DIGEST.md"
    if args.stdout:
        sys.stdout.write(text)
        return 0
    if args.check:
        if not target.is_file():
            print(f"digest: {target.as_posix()} missing; run digest.py {args.bundle.as_posix()}")
            return 1
        if target.read_text(encoding="utf-8") != text:
            print(f"digest: {target.as_posix()} is stale; run digest.py {args.bundle.as_posix()} and commit it")
            return 1
        print(f"digest: {target.as_posix()} up to date")
        return 0
    target.write_text(text, encoding="utf-8")
    print(f"digest: wrote {target.as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
