#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml"]
# ///
"""OKF v0.2 conformance checker for OSP knowledge bundles.

Checks a bundle directory against OKF v0.2 (GoogleCloudPlatform/
knowledge-catalog, okf/SPEC.md) plus the OSP conventions layered on it.
Errors are conformance failures (spec 11); warnings are spec SHOULDs and
OSP house rules. Exit 1 on any error, or on warnings too with --strict.

ERRORS (spec 11 conformance)
  E1  concept has no parseable YAML frontmatter
  E2  frontmatter missing a non-empty `type`
  E3  `generated` present but malformed (needs mapping with `by`)
  E4  `verified` present but malformed (mapping or list of {by, at})
  E5  `status` outside draft | stable | deprecated
  E6  `stale_after` not YYYY-MM-DD
  E7  `sources` entry missing `resource`
  E8  actor value violates the convention (spec 7)
  E9  non-root index.md carries frontmatter (spec 8, 12)

WARNINGS (SHOULDs and OSP rules)
  W1  body footnote ref has no matching sources id (spec 5.1 join)
  W2  sources id never referenced by a body footnote
  W3  root index.md missing okf_version
  W4  concept unverified or machine-confirmed only (tier report)
  W5  stale: today >= stale_after (spec 5.5)
  W6  log.md date heading not ISO YYYY-MM-DD (spec 9)
  W7  legacy v0.1/v0.6 key present (timestamp, verified_by, evidence,
      or a v0.6 status value): migration incomplete

FINDINGS (OSP candidate section 5.10; only under --findings, which
touches `type: finding` concepts and nothing else)
  F1  required field missing or malformed (question, claim, computations,
      validity, confrontation, limitations, explicit status)
  F2  question is not one sentence ending in a question mark
  F3  claim not bound: from.receipt missing or not JSON, a field path that
      does not resolve, or a bound value/interval/confidence that
      disagrees with the receipt at the precision written
  F4  cited computation broken: concept missing or not an Attested
      Computation, receipt missing or not JSON, receipt code_sha256
      differs from the sanctioned computation file, or no verified data
      tree stamp in the receipt
  F5  the claim's receipt is not among the finding's cited receipts
  F6  validity verdict OUT, unknown, or disagreeing with the fitness receipt
  F7  stable finding without a human: verified event or without verdict IN
  F8  ladder inconsistency (retracted, superseded_by, deprecated forms)
  F9  a number in the finding's text resolves to no cited receipt field
      and no context entry
  F10 confrontation record incomplete (confronted without concept,
      receipt, observation concept, or an observational record named by
      version or identifier; not-confronted without a reason)
  FW1 no "What would overturn this" section
  FW2 stable finding not confronted
  FW3 no stale_after
  FW4 computation inline, so receipt identity cannot be checked
  FW5 links to a retracted finding

Usage: check_okf_v02.py BUNDLE_DIR [--strict] [--findings [--explain]]
"""

import argparse
import datetime
import hashlib
import json
import math
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("pyyaml required: python3 -m pip install pyyaml", file=sys.stderr)
    sys.exit(2)

ACTOR_RE = re.compile(r"^(human:|process:|team:)\S+$|^[\w.-]+/[\w.@-]+$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
STATUSES = {"draft", "stable", "deprecated"}
LEGACY_STATUSES = {"verified", "stale", "superseded", "disputed"}
FOOT_REF = re.compile(r"\[\^([\w-]+)\](?!:)")
FOOT_DEF = re.compile(r"^\[\^([\w-]+)\]:", re.M)


def split_frontmatter(text: str):
    if not text.startswith("---"):
        return None, text
    lines = text.split("\n")
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[1:i]), "\n".join(lines[i + 1:])
    return None, text


def check_actor(value, where, out, path):
    if not isinstance(value, str) or not ACTOR_RE.match(value):
        out.append(("E8", path, f"{where}: '{value}' violates the actor convention"))


def tier(verified) -> str:
    events = verified if isinstance(verified, list) else [verified] if verified else []
    bys = [e.get("by", "") for e in events if isinstance(e, dict)]
    if any(isinstance(b, str) and b.startswith("human:") for b in bys):
        return "human-reviewed"
    return "machine-confirmed" if bys else "unverified"


def check_concept(path: Path, out: list, tiers: dict):
    text = path.read_text(encoding="utf-8")
    raw_fm, body = split_frontmatter(text)
    if raw_fm is None:
        out.append(("E1", path, "no frontmatter block"))
        return None, body
    try:
        fm = yaml.safe_load(raw_fm) or {}
    except yaml.YAMLError as e:
        out.append(("E1", path, f"frontmatter does not parse: {e}"))
        return None, body
    if not isinstance(fm, dict):
        out.append(("E1", path, "frontmatter is not a mapping"))
        return None, body

    if not str(fm.get("type") or "").strip():
        out.append(("E2", path, "missing non-empty `type` (the one required key)"))

    for legacy in ("timestamp", "verified_by", "evidence"):
        if legacy in fm:
            out.append(("W7", path, f"legacy key `{legacy}` present: migration incomplete"))

    gen = fm.get("generated")
    if gen is not None:
        if not isinstance(gen, dict) or "by" not in gen:
            out.append(("E3", path, "`generated` must be a mapping with `by`"))
        else:
            check_actor(gen["by"], "generated.by", out, path)

    ver = fm.get("verified")
    if ver is not None:
        events = ver if isinstance(ver, list) else [ver]
        for e in events:
            if not isinstance(e, dict) or "by" not in e or "at" not in e:
                out.append(("E4", path, "`verified` events need `by` and `at`"))
            else:
                check_actor(e["by"], "verified.by", out, path)
    t = tier(ver)
    tiers[t] = tiers.get(t, 0) + 1
    if t != "human-reviewed":
        out.append(("W4", path, f"trust tier: {t}"))

    status = fm.get("status")
    if status is not None and status not in STATUSES:
        code = "W7" if status in LEGACY_STATUSES else "E5"
        out.append((code, path, f"status '{status}' outside draft|stable|deprecated"))

    sa = fm.get("stale_after")
    if sa is not None:
        s = sa.isoformat() if isinstance(sa, datetime.date) else str(sa)
        if not DATE_RE.match(s):
            out.append(("E6", path, f"stale_after '{sa}' is not YYYY-MM-DD"))
        elif datetime.date.today().isoformat() >= s:
            out.append(("W5", path, f"stale since {s}"))

    src_ids = set()
    sources = fm.get("sources")
    if sources is not None:
        for entry in sources if isinstance(sources, list) else []:
            if not isinstance(entry, dict) or "resource" not in entry:
                out.append(("E7", path, "sources entry missing `resource`"))
            elif "id" in entry:
                src_ids.add(str(entry["id"]))
            if isinstance(entry, dict) and "author" in entry:
                check_actor(entry["author"], "sources[].author", out, path)

    refs = set(FOOT_REF.findall(body)) | set(FOOT_DEF.findall(body))
    for r in sorted(refs - src_ids):
        if sources is not None:
            out.append(("W1", path, f"footnote [^{r}] has no matching sources id"))
    for s in sorted(src_ids - refs):
        out.append(("W2", path, f"sources id '{s}' never cited by a footnote"))
    return fm, body


# ---------------------------------------------------------------------
# Findings (candidate section 5.10). Every rule below runs only under
# --findings and only on `type: finding` concepts, so no existing bundle
# changes behavior until the section is normative.
# ---------------------------------------------------------------------

VERDICTS = {"IN", "OUT", "UNADJUDICATED"}
FINDING_TYPE = "finding"
COMPUTATION_TYPE = "Attested Computation"
OVERTURN_HEADING = re.compile(r"^#+\s+what would overturn this", re.I | re.M)
NUM_TOKEN = re.compile(
    r"(?<![\w.])([+-]?)(\d{1,3}(?:,\d{3})+|\d+)(\.\d+)?([eE][+-]?\d+)?(?![\w.]|\.\d)")
PERCENT_AFTER = re.compile(r"^\s*(%|percent)")
MAX_LIST_LEAVES = 4      # longer numeric lists are series, not fields


def resolve_path(ref, concept: Path, bundle: Path):
    """Path-valued fields (OKF 6.2): bundle-absolute with a leading slash,
    else relative to the concept, else relative to the bundle root."""
    if not isinstance(ref, str) or not ref or "://" in ref:
        return None
    if ref.startswith("/"):
        return bundle / ref.lstrip("/")
    for base in (concept.parent, bundle):
        cand = (base / ref)
        if cand.exists():
            return cand
    return concept.parent / ref


def load_frontmatter(path: Path):
    try:
        raw, body = split_frontmatter(path.read_text(encoding="utf-8"))
        fm = yaml.safe_load(raw) if raw is not None else None
        return (fm if isinstance(fm, dict) else None), body
    except (OSError, yaml.YAMLError):
        return None, ""


def load_json(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def field_path(obj, dotted: str):
    """Resolve `a.b.0.c` in a JSON object; None when any step fails."""
    cur = obj
    for step in str(dotted).split("."):
        if isinstance(cur, dict) and step in cur:
            cur = cur[step]
        elif isinstance(cur, list) and step.isdigit() and int(step) < len(cur):
            cur = cur[int(step)]
        else:
            return None
    return cur


def numeric_leaves(obj, prefix=""):
    """Every numeric field of a receipt with its dotted path. Lists longer
    than MAX_LIST_LEAVES are series carried for recomputation, not fields
    a finding quotes, and are skipped."""
    out = []
    if isinstance(obj, bool):
        return out
    if isinstance(obj, (int, float)) and math.isfinite(obj):
        out.append((prefix, float(obj)))
    elif isinstance(obj, dict):
        for k, v in obj.items():
            out.extend(numeric_leaves(v, f"{prefix}.{k}" if prefix else str(k)))
    elif isinstance(obj, list):
        nums = [x for x in obj if isinstance(x, (int, float)) and not isinstance(x, bool)]
        if len(nums) > MAX_LIST_LEAVES:
            return out
        for i, v in enumerate(obj):
            out.extend(numeric_leaves(v, f"{prefix}.{i}" if prefix else str(i)))
    return out


def token_value_ulp(sign, intpart, frac, exp):
    """A number as written, and the unit in its last written place."""
    text = f"{sign}{intpart.replace(',', '')}{frac or ''}{exp or ''}"
    value = float(text)
    decimals = len(frac) - 1 if frac else 0
    e = int(exp[1:]) if exp else 0
    return value, 10.0 ** (e - decimals)


def matches(value, ulp, leaf):
    tol = 0.5 * ulp * (1 + 1e-9) + 1e-12
    return abs(leaf - value) <= tol


def has_record_stamp(obj) -> bool:
    if isinstance(obj, dict):
        if "manifest_sha256" in obj:
            return True
        return any(has_record_stamp(v) for v in obj.values())
    if isinstance(obj, list):
        return any(has_record_stamp(v) for v in obj)
    return False


def strip_exempt(text: str) -> str:
    """Remove what the number rule exempts by pattern: code, URLs, DOIs,
    hashes, timestamps and dates, years, footnote refs and definition
    lines, list markers, and identifiers that mix letters and digits."""
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`[^`\n]*`", " ", text)
    text = re.sub(r"^\[\^[\w-]+\]:.*$", " ", text, flags=re.M)
    text = re.sub(r"\[\^[\w-]+\]", " ", text)
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"\b10\.\d{4,}/\S+", " ", text)
    text = re.sub(r"\b[0-9a-f]{12,}\b", " ", text)
    text = re.sub(r"\d{4}-\d{2}-\d{2}T[\d:.]+(?:Z|[+-]\d{2}:\d{2})?", " ", text)
    text = re.sub(r"\b\d{4}-\d{2}(?:-\d{2})?\b", " ", text)
    text = re.sub(r"(?<![\d.])(?:19|20)\d{2}(?![\d.])", " ", text)
    text = re.sub(r"^\s*\d+\.\s", " ", text, flags=re.M)
    text = re.sub(r"\b[A-Za-z][\w-]*\d[\w.-]*\b", " ", text)
    return text


def scan_numbers(text: str):
    """Yield (value, ulp, percent, snippet) for every number in the text."""
    clean = strip_exempt(text)
    for m in NUM_TOKEN.finditer(clean):
        value, ulp = token_value_ulp(*m.groups())
        percent = bool(PERCENT_AFTER.match(clean[m.end():m.end() + 9]))
        snippet = clean[max(0, m.start() - 24):m.end() + 12].replace("\n", " ")
        yield value, ulp, percent, m.group(0), snippet


def resolve_number(value, ulp, percent, leaves):
    """The receipt field a written number resolves to, or None."""
    for path, leaf in leaves:
        if matches(value, ulp, leaf):
            return path, leaf, ""
    if percent:
        for path, leaf in leaves:
            if matches(value, ulp, leaf * 100.0):
                return path, leaf, " (as a percentage)"
    for path, leaf in leaves:
        if matches(abs(value), ulp, abs(leaf)):
            return path, leaf, " (magnitude)"
    return None


def normalize_declaration(d):
    """The fitness attester's normalized declaration form, from either the
    command-line strings or the already-normalized mappings."""
    if not isinstance(d, dict):
        return None
    out = {"product": d.get("product"), "claim": d.get("claim")}
    region = d.get("region")
    if isinstance(region, str) and region != "global":
        try:
            out["region"] = {"bbox": [float(x) for x in region.split(",")]}
        except ValueError:
            out["region"] = region
    else:
        out["region"] = region
    period = d.get("period")
    if isinstance(period, str) and period != "any" and ":" in period:
        a, b = period.split(":", 1)
        out["period"] = {"start": a, "end": b}
    else:
        out["period"] = period
    return out


def ladder(fm: dict):
    """The derived position on the finding ladder (5.10.3)."""
    if isinstance(fm.get("retracted"), dict):
        return "retracted"
    if fm.get("superseded_by"):
        return "superseded"
    status = fm.get("status")
    if status == "stable":
        return "stable (disputed)" if fm.get("disputed") else "stable"
    if status == "draft":
        return "under-review" if fm.get("review") else "draft"
    return "unplaced"


def check_finding(path: Path, fm: dict, body: str, bundle: Path, out: list,
                  positions: dict, explain: bool):
    def err(code, msg):
        out.append((code, path, msg))

    # F1 required fields and shapes
    missing = [k for k in ("question", "claim", "computations", "validity",
                           "confrontation", "limitations", "status") if k not in fm]
    if missing:
        err("F1", f"required finding field(s) missing: {', '.join(missing)}")
    claim = fm.get("claim") if isinstance(fm.get("claim"), dict) else {}
    for k in ("statement", "value", "interval", "confidence", "units", "from"):
        if "claim" in fm and k not in claim:
            err("F1", f"claim.{k} missing")
    if "claim" in fm and not isinstance(claim.get("interval"), list) or \
            ("claim" in fm and isinstance(claim.get("interval"), list)
             and len(claim["interval"]) != 2):
        err("F1", "claim.interval must be a two-element list [low, high]")
    comps = fm.get("computations")
    if "computations" in fm and (not isinstance(comps, list) or not comps):
        err("F1", "computations must be a non-empty list of {concept, receipt}")
        comps = []
    comps = comps if isinstance(comps, list) else []
    lims = fm.get("limitations")
    if "limitations" in fm and (not isinstance(lims, list) or not lims
                                or not all(isinstance(s, str) and s.strip() for s in lims)):
        err("F1", "limitations must be a non-empty list of sentences")

    # F2 the question
    q = fm.get("question")
    if isinstance(q, str):
        qs = q.strip()
        if not qs.endswith("?") or qs.count("?") != 1 or re.search(r"[.!]\s+\S", qs):
            err("F2", "question must be one sentence ending in a question mark")
    elif "question" in fm:
        err("F1", "question must be a string")

    # F4 computations and their receipts; collect leaves and cited receipts
    leaves, cited = [], set()
    for i, c in enumerate(comps):
        if not isinstance(c, dict) or "concept" not in c or "receipt" not in c:
            err("F1", f"computations[{i}] needs concept and receipt")
            continue
        cpath = resolve_path(c["concept"], path, bundle)
        rpath = resolve_path(c["receipt"], path, bundle)
        cfm, _ = load_frontmatter(cpath) if cpath and cpath.exists() else (None, "")
        if cfm is None:
            err("F4", f"computations[{i}].concept {c['concept']} missing or unreadable")
        elif cfm.get("type") != COMPUTATION_TYPE:
            err("F4", f"computations[{i}].concept is type '{cfm.get('type')}', not {COMPUTATION_TYPE}")
        receipt = load_json(rpath) if rpath else None
        if not isinstance(receipt, dict):
            err("F4", f"computations[{i}].receipt {c['receipt']} missing or not a JSON object")
            continue
        cited.add(rpath.resolve())
        leaves.extend(numeric_leaves(receipt, f"{rpath.name}:"))
        if not has_record_stamp(receipt):
            err("F4", f"receipt {rpath.name} names no verified data tree (no manifest stamp)")
        if cfm is not None:
            comp_ref = cfm.get("computation")
            if not comp_ref:
                out.append(("FW4", path, f"{cpath.name}: computation is inline, receipt identity not checkable"))
            else:
                comp_file = resolve_path(comp_ref, cpath, bundle)
                if comp_file is None or not comp_file.exists():
                    err("F4", f"{cpath.name} names computation {comp_ref}, which does not exist")
                elif "code_sha256" not in receipt:
                    err("F4", f"receipt {rpath.name} carries no code_sha256")
                elif receipt["code_sha256"] != hashlib.sha256(comp_file.read_bytes()).hexdigest():
                    err("F4", f"receipt {rpath.name} code_sha256 differs from {comp_file.name}: "
                               "the number was produced by code that no longer stands")

    # F10 confrontation
    conf = fm.get("confrontation")
    if "confrontation" in fm:
        if not isinstance(conf, dict) or conf.get("status") not in ("confronted", "not-confronted"):
            err("F10", "confrontation.status must be confronted or not-confronted")
        elif conf["status"] == "not-confronted":
            if not isinstance(conf.get("reason"), str) or not conf["reason"].strip():
                err("F10", "not-confronted needs a reason")
        else:
            for k in ("concept", "receipt", "observation"):
                if k not in conf:
                    err("F10", f"confronted needs confrontation.{k}")
            cpath = resolve_path(conf.get("concept"), path, bundle)
            cfm, _ = load_frontmatter(cpath) if cpath and cpath.exists() else (None, "")
            if cfm is None or cfm.get("type") != COMPUTATION_TYPE:
                err("F10", "confrontation.concept is not an Attested Computation in the bundle")
            opath = resolve_path(conf.get("observation"), path, bundle)
            ofm, _ = load_frontmatter(opath) if opath and opath.exists() else (None, "")
            if ofm is None:
                err("F10", "confrontation.observation is not a concept in the bundle")
            rpath = resolve_path(conf.get("receipt"), path, bundle)
            receipt = load_json(rpath) if rpath else None
            if not isinstance(receipt, dict):
                err("F10", "confrontation.receipt missing or not a JSON object")
            else:
                cited.add(rpath.resolve())
                leaves.extend(numeric_leaves(receipt, f"{rpath.name}:"))
                obs = receipt.get("observation")
                if not isinstance(obs, dict) or not (obs.get("doi") or obs.get("version")):
                    err("F10", "confrontation receipt names no observational record by version or identifier")
                if not has_record_stamp(receipt):
                    err("F10", f"confrontation receipt {rpath.name} names no verified data tree")

    # F6 validity
    val = fm.get("validity")
    verdict = None
    if "validity" in fm:
        if not isinstance(val, dict):
            err("F1", "validity must be a mapping")
            val = {}
        verdict = val.get("verdict")
        if verdict not in VERDICTS:
            err("F6", f"validity.verdict '{verdict}' is not IN, OUT or UNADJUDICATED")
        elif verdict == "OUT":
            err("F6", "validity verdict is OUT: the claim lies outside a signed exclusion; a finding cannot state it")
        if "declaration" not in val:
            err("F1", "validity.declaration missing")
        if val.get("receipt"):
            rpath = resolve_path(val["receipt"], path, bundle)
            fr = load_json(rpath) if rpath else None
            if not isinstance(fr, dict):
                err("F6", "validity.receipt missing or not a JSON object")
            else:
                leaves.extend(numeric_leaves(fr, f"{rpath.name}:"))
                if fr.get("verdict") != verdict:
                    err("F6", f"validity.verdict {verdict} disagrees with the fitness receipt ({fr.get('verdict')})")
                if normalize_declaration(val.get("declaration")) != normalize_declaration(fr.get("declaration")):
                    err("F6", "validity.declaration disagrees with the fitness receipt's declaration")
                gov_names = {Path(str(g.get("concept", ""))).name for g in fr.get("governing_concepts", [])
                             if isinstance(g, dict)}
                for g in val.get("governing") or []:
                    gpath = resolve_path(g, path, bundle)
                    gfm, _ = load_frontmatter(gpath) if gpath and gpath.exists() else (None, "")
                    if gfm is None or gfm.get("type") != "validity-domain":
                        err("F6", f"validity.governing entry {g} is not a validity-domain concept")
                    elif gpath.name not in gov_names:
                        err("F6", f"validity.governing entry {g} is not among the fitness receipt's governing concepts")
                if verdict in ("IN", "OUT") and not val.get("governing"):
                    err("F6", f"verdict {verdict} with no governing domain named")
        elif verdict in ("IN", "OUT"):
            err("F6", f"verdict {verdict} stated without a fitness receipt")

    # F3 and F5 the claim binding
    frm = claim.get("from") if isinstance(claim.get("from"), dict) else None
    raw_fm, _ = split_frontmatter(path.read_text(encoding="utf-8"))
    if "claim" in fm and frm is None:
        err("F1", "claim.from must be a mapping of receipt and field paths")
    elif frm is not None:
        rpath = resolve_path(frm.get("receipt"), path, bundle)
        receipt = load_json(rpath) if rpath else None
        if not isinstance(receipt, dict):
            err("F3", f"claim.from.receipt {frm.get('receipt')} missing or not a JSON object")
        else:
            if rpath.resolve() not in cited:
                err("F5", f"claim.from.receipt {rpath.name} is not among the finding's cited receipts")
            bindings = [("value", claim.get("value"), frm.get("value"))]
            iv = claim.get("interval") if isinstance(claim.get("interval"), list) else [None, None]
            fiv = frm.get("interval") if isinstance(frm.get("interval"), list) else [None, None]
            bindings += [("interval[0]", iv[0] if len(iv) > 0 else None, fiv[0] if len(fiv) > 0 else None),
                         ("interval[1]", iv[1] if len(iv) > 1 else None, fiv[1] if len(fiv) > 1 else None),
                         ("confidence", claim.get("confidence"), frm.get("confidence"))]
            for name, stated, fpath in bindings:
                if fpath is None:
                    err("F3", f"claim.from.{name.split('[')[0]} names no receipt field")
                    continue
                got = field_path(receipt, fpath)
                if not isinstance(got, (int, float)) or isinstance(got, bool):
                    err("F3", f"claim.from {name}: field '{fpath}' does not resolve to a number in {rpath.name}")
                    continue
                if not isinstance(stated, (int, float)) or isinstance(stated, bool):
                    err("F3", f"claim.{name} is not a number")
                    continue
                ulp = written_ulp(raw_fm or "", stated)
                if not matches(float(stated), ulp, float(got)):
                    err("F3", f"claim.{name} {stated} disagrees with {rpath.name}:{fpath} = {got} at the precision written")
                elif explain:
                    print(f"    claim.{name} {stated} = {rpath.name}:{fpath} ({got})")

    # context entries: numbers that are not results, each with a source id
    src_ids = {str(s.get("id")) for s in fm.get("sources") or [] if isinstance(s, dict) and "id" in s}
    for i, c in enumerate(fm.get("context") or []):
        if not isinstance(c, dict) or not isinstance(c.get("value"), (int, float)) \
                or not c.get("meaning") or str(c.get("source")) not in src_ids:
            err("F9", f"context[{i}] needs value, meaning, and a source id from sources")
        else:
            leaves.append((f"context:{c['meaning']}", float(c["value"])))

    # F9 every number in the finding's text
    texts = [("title", fm.get("title")), ("description", fm.get("description")),
             ("question", fm.get("question")), ("claim.statement", claim.get("statement"))]
    texts += [(f"limitations[{i}]", s) for i, s in enumerate(lims or []) if isinstance(s, str)]
    texts.append(("body", body))
    if explain:
        print(f"    receipt fields available: {len(leaves)}")
    for where, text in texts:
        if not isinstance(text, str):
            continue
        for value, ulp, percent, token, snippet in scan_numbers(text):
            hit = resolve_number(value, ulp, percent, leaves)
            if hit is None:
                err("F9", f"{where}: '{token}' resolves to no cited receipt field or context entry (...{snippet}...)")
            elif explain:
                print(f"    {where}: {token} -> {hit[0]} ({hit[1]}){hit[2]}")

    # F7, F8 and the ladder
    status = fm.get("status")
    pos = ladder(fm)
    positions[pos] = positions.get(pos, 0) + 1
    if status == "stable":
        if tier(fm.get("verified")) != "human-reviewed":
            err("F7", "stable finding without a human: verified event (a finding becomes stable by signature only)")
        if verdict != "IN":
            err("F7", f"stable finding with validity verdict {verdict}; stable requires IN")
        if isinstance(conf, dict) and conf.get("status") == "not-confronted":
            out.append(("FW2", path, "stable finding not confronted against an independent observation"))
    ret = fm.get("retracted")
    if ret is not None:
        if not isinstance(ret, dict) or any(k not in ret for k in ("at", "by", "reason", "issue")):
            err("F8", "retracted must carry at, by, reason, issue")
        elif not str(ret.get("by", "")).startswith("human:"):
            err("F8", "retracted.by must be a human: actor")
        if status != "deprecated":
            err("F8", f"retracted finding must be status: deprecated (is {status})")
        if not re.search(r"^#+\s+retraction", body, re.I | re.M):
            err("F8", "retracted finding needs a Retraction section in the body")
    sup = fm.get("superseded_by")
    if sup:
        spath = resolve_path(sup, path, bundle)
        sfm, _ = load_frontmatter(spath) if spath and spath.exists() else (None, "")
        if sfm is None or sfm.get("type") != FINDING_TYPE:
            err("F8", f"superseded_by {sup} is not a finding concept")
        if status != "deprecated":
            err("F8", f"superseded finding must be status: deprecated (is {status})")
    if status == "deprecated" and not sup and ret is None:
        err("F8", "deprecated finding must say which: superseded_by or retracted")

    # FW1, FW3, FW5
    if not OVERTURN_HEADING.search(body):
        out.append(("FW1", path, "no 'What would overturn this' section"))
    if "stale_after" not in fm:
        out.append(("FW3", path, "no stale_after: a finding rests on a product release"))
    for link in re.findall(r"\]\(([^)\s]+\.md)\)", body):
        lpath = resolve_path(link, path, bundle)
        lfm, _ = load_frontmatter(lpath) if lpath and lpath.exists() else (None, "")
        if lfm and lfm.get("type") == FINDING_TYPE and isinstance(lfm.get("retracted"), dict):
            out.append(("FW5", path, f"links to the retracted finding {link}"))
    if explain:
        print(f"    position: {pos}")


def written_ulp(raw_fm: str, stated) -> float:
    """The unit in the last place of a frontmatter number as written; the
    parsed float loses its precision, the source text keeps it."""
    best = None
    for m in NUM_TOKEN.finditer(raw_fm):
        value, ulp = token_value_ulp(*m.groups())
        if value == float(stated) and (best is None or ulp < best):
            best = ulp
    return best if best is not None else 1e-9


def check_index(path: Path, is_root: bool, out: list):
    text = path.read_text(encoding="utf-8")
    raw_fm, _ = split_frontmatter(text)
    if is_root:
        if raw_fm is None:
            out.append(("W3", path, 'root index missing okf_version: "0.2"'))
        else:
            fm = yaml.safe_load(raw_fm) or {}
            if "okf_version" not in fm:
                out.append(("W3", path, "root index frontmatter lacks okf_version"))
    elif raw_fm is not None:
        out.append(("E9", path, "non-root index.md must not carry frontmatter"))


def check_log(path: Path, out: list):
    for line in path.read_text(encoding="utf-8").split("\n"):
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m and not DATE_RE.match(m.group(1)):
            out.append(("W6", path, f"log heading '{m.group(1)}' not ISO YYYY-MM-DD"))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("bundle", type=Path)
    ap.add_argument("--strict", action="store_true", help="warnings fail too")
    ap.add_argument("--findings", action="store_true",
                    help="apply the finding rules (candidate section 5.10) to "
                         "type: finding concepts; nothing else changes")
    ap.add_argument("--explain", action="store_true",
                    help="with --findings: print how each number resolved")
    args = ap.parse_args()

    out: list = []
    tiers: dict = {}
    positions: dict = {}
    for path in sorted(args.bundle.rglob("*.md")):
        if path.name == "index.md":
            check_index(path, path.parent == args.bundle, out)
        elif path.name == "log.md":
            check_log(path, out)
        else:
            fm, body = check_concept(path, out, tiers)
            if args.findings and fm is not None and fm.get("type") == FINDING_TYPE:
                if args.explain:
                    print(f"finding {path}")
                check_finding(path, fm, body, args.bundle, out, positions, args.explain)

    errors = [x for x in out if x[0].startswith(("E", "F")) and not x[0].startswith("FW")]
    warns = [x for x in out if x[0].startswith(("W", "FW"))]
    for code, path, msg in errors + warns:
        print(f"{code}  {path}: {msg}")
    total = sum(tiers.values())
    print(f"\nconcepts: {total}  tiers: " +
          ", ".join(f"{k} {v}" for k, v in sorted(tiers.items())))
    if args.findings:
        print(f"findings: {sum(positions.values())}" +
              ("  positions: " + ", ".join(f"{k} {v}" for k, v in sorted(positions.items()))
               if positions else ""))
    print(f"errors: {len(errors)}  warnings: {len(warns)}")
    if errors or (args.strict and warns):
        return 1
    print("conformant with OKF v0.2 (spec 11)" +
          ("" if not warns else "; warnings above are SHOULDs, not failures"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
