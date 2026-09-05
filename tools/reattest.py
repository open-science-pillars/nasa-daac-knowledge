#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml"]
# ///
"""Re-attest a sanctioned computation after a deliberate edit: the
whole ritual as one command, with the evidence a log entry needs.

Every receipt carries the sha256 of the computation file that produced
it, and the attester hashes the sanctioned file before it reads a
number, so any edit to a computation, a docstring's wording included,
invalidates every earlier receipt by construction. That is the
contract working, and it means an edit is never casual: the file is
re-run on the verified fixture cache with its reference parameters, the
fresh receipt is attested, the old receipt is shown to fail against
the new file, a tamper of the new file is shown to fail, and the bundle
log records it all with both hashes. This tool runs those steps in
order and refuses to call the result a pass unless each one lands as
the contract says it must:

  1. NEW PASS      a fresh run of the working-tree file, with the
                   reference arguments, attests PASS;
  2. OLD PASS      the previous version of the file (HEAD, or --old
                   REF) is run on the same data and attests PASS
                   against itself: the edit did not start from a
                   broken file;
  3. OLD vs NEW    the previous version's receipt attests FAIL against
                   the new file, on code_sha256;
  4. TAMPER FAIL   the fresh receipt attests FAIL against a one-byte
                   tamper of the new file.

Steps 2 and 3 are skipped, and said to be skipped, when the working
tree matches the reference version (a re-verification, not a
re-attestation). The reference arguments come from
tools/reference_runs.yaml by run name; the attester from the concept
whose frontmatter names the computation, unless --attester says
otherwise. The receipts, the old file and the tampered file are kept
under --keep (default: a fresh temporary directory, printed) so they
can be cited. The printed log entry is a draft for the steward's
change log; the tool writes nothing into the bundle.

  reattest.py --run NAME [--old REF] [--note TEXT] [--keep DIR]
  reattest.py COMPUTATION.py [--attester PATH] [--data-root DIR]
              [--old REF] [--note TEXT] [--keep DIR] -- ARGS ...
  reattest.py --list
  reattest.py --selftest

Exit 0 only when every step that ran landed as required.
"""

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
BUNDLE = REPO / "knowledge" / "podaac"
COMPUTATIONS = BUNDLE / "references" / "computations"
REGISTRY = HERE / "reference_runs.yaml"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def frontmatter(text: str) -> str:
    parts = text.split("---")
    return parts[1] if len(parts) > 2 and text.startswith("---") else ""


def attester_for(computation: Path, bundle: Path = BUNDLE):
    """The attester the concept names for this computation, resolved
    against the bundle; None when no concept names it."""
    target = computation.resolve()
    for concept in sorted((bundle / "computations").glob("*.md")):
        fm = frontmatter(concept.read_text(encoding="utf-8"))
        m = re.search(r"^computation:\s*(\S+)", fm, re.M)
        if not m or (bundle / m.group(1)).resolve() != target:
            continue
        a = re.search(r"^attester:\s*\n\s+resource:\s*(\S+)", fm, re.M)
        if a:
            return bundle / a.group(1)
    return None


def load_registry(path: Path = REGISTRY) -> dict:
    reg = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    reg.setdefault("data_roots", {})
    reg.setdefault("runs", {})
    return reg


def run_cmd(argv, cwd: Path):
    """Run argv, return (returncode, combined output)."""
    p = subprocess.run([str(a) for a in argv], cwd=str(cwd),
                       capture_output=True, text=True)
    return p.returncode, (p.stdout + p.stderr).strip()


def tamper(src: Path, dst: Path) -> None:
    """A one-byte edit that leaves the file runnable: one more newline
    at the end. The receipt's hash no longer matches, which is the
    whole point."""
    dst.write_bytes(src.read_bytes() + b"\n")


def old_version(path: Path, ref: str, repo: Path, dst: Path):
    """The file as of REF, written to dst; None when git has no such
    version."""
    rel = path.resolve().relative_to(repo.resolve()).as_posix()
    rc, out = run_cmd(["git", "show", f"{ref}:{rel}"], repo)
    if rc != 0:
        return None
    dst.write_text(out + "\n", encoding="utf-8")
    return dst


def receipt_summary(path: Path) -> dict:
    try:
        r = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    data = r.get("data") if isinstance(r.get("data"), dict) else {}
    record = data.get("record") if isinstance(data.get("record"), dict) else {}
    return {"run_id": r.get("run_id"), "code_sha256": r.get("code_sha256"),
            "record": record.get("record")}


class Ritual:
    """The four steps, each recorded as (name, required, got, detail)."""

    def __init__(self, computation: Path, attester: Path, args, keep: Path,
                 repo: Path = REPO, runner=None):
        self.computation, self.attester, self.args = computation, attester, list(args)
        self.keep, self.repo = keep, repo
        self.run = runner or run_cmd
        self.steps = []
        self.new_receipt = keep / "receipt_new.json"
        self.old_receipt = keep / "receipt_old.json"
        self.old_file = keep / ("old_" + computation.name)
        self.tampered = keep / ("tampered_" + computation.name)
        self.skipped = []

    def compute(self, script: Path, receipt: Path):
        return self.run(["uv", "run", script, *self.args, "--receipt", receipt], self.repo)

    def attest(self, receipt: Path, against: Path):
        return self.run(["uv", "run", self.attester, receipt, "--computation", against], self.repo)

    def record(self, name, required, rc, out):
        got = "PASS" if rc == 0 else "FAIL"
        self.steps.append((name, required, got, out.splitlines()[-1] if out else ""))
        return got == required

    def perform(self, old_ref: str) -> bool:
        ok = True
        rc, out = self.compute(self.computation, self.new_receipt)
        if rc != 0:
            self.steps.append(("NEW RUN", "PASS", "FAIL", out[-400:]))
            return False
        rc, out = self.attest(self.new_receipt, self.computation)
        ok &= self.record("NEW PASS", "PASS", rc, out)

        old = old_version(self.computation, old_ref, self.repo, self.old_file)
        if old is None:
            self.skipped.append(f"no version of the file at {old_ref}; OLD steps skipped")
        elif sha256(old) == sha256(self.computation):
            self.skipped.append(f"working tree matches {old_ref} (sha256 "
                                f"{sha256(old)[:12]}); a re-verification, OLD steps skipped")
        else:
            rc, out = self.compute(old, self.old_receipt)
            if rc != 0:
                self.steps.append(("OLD RUN", "PASS", "FAIL", out[-400:]))
                ok = False
            else:
                rc, out = self.attest(self.old_receipt, old)
                ok &= self.record("OLD PASS", "PASS", rc, out)
                rc, out = self.attest(self.old_receipt, self.computation)
                ok &= self.record("OLD vs NEW", "FAIL", rc, out)

        tamper(self.computation, self.tampered)
        rc, out = self.attest(self.new_receipt, self.tampered)
        ok &= self.record("TAMPER FAIL", "FAIL", rc, out)
        return ok

    def report(self, note: str, rel: str) -> str:
        lines = []
        for name, required, got, detail in self.steps:
            mark = "ok " if got == required else "BAD"
            lines.append(f"  {mark} {name:<12} required {required}, got {got}: {detail[:100]}")
        for s in self.skipped:
            lines.append(f"  --  {s}")
        new = receipt_summary(self.new_receipt)
        old = receipt_summary(self.old_receipt) if self.old_receipt.exists() else {}
        lines.append(f"  new sha256 {sha256(self.computation)}")
        if self.old_file.exists():
            lines.append(f"  old sha256 {sha256(self.old_file)}")
        lines.append(f"  receipts under {self.keep}")
        return "\n".join(lines) + "\n\n" + self.log_entry(note, rel, new, old)

    def log_entry(self, note: str, rel: str, new: dict, old: dict) -> str:
        day = dt.date.today().isoformat()
        new_sha = sha256(self.computation)[:12]
        old_sha = old.get("code_sha256", "")[:12] if old else None
        shas = f"(sha256 {old_sha} -> {new_sha})" if old_sha else f"(sha256 {new_sha}, unchanged)"
        head = "RE-ATTESTATION" if old_sha else "RE-VERIFICATION"
        args = " ".join(str(a) for a in self.args)
        where = f"on the verified tree {new['record']}" if new.get("record") else "on the data given"
        evidence = [f"a fresh run ({args}) attests PASS, run {new.get('run_id')}"]
        if old_sha:
            evidence.insert(0, "a receipt from the previous file FAILS against the new one on code_sha256, as the contract requires")
            evidence.insert(0, f"the previous file attests PASS against itself, run {old.get('run_id')}")
        evidence.append("a one-byte tamper of the new file FAILS")
        body = (f"{day} · {head} of {rel} {shas}: {note or '<why the file changed, and what did not>'} "
                f"Evidence, {where}: " + "; ".join(evidence) + ". (<who>)")
        return textwrap.fill(body, width=72, initial_indent="- ", subsequent_indent="  ")


def selftest() -> int:
    """An offline ritual on stub scripts: the computation writes a
    receipt carrying its own sha256, the attester checks it."""
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        subprocess.run(["git", "init", "-q", str(root)], check=True)
        subprocess.run(["git", "-C", str(root), "config", "user.email", "t@example.org"], check=True)
        subprocess.run(["git", "-C", str(root), "config", "user.name", "T"], check=True)
        bundle = root / "knowledge" / "podaac"
        comps, atts = bundle / "references" / "computations", bundle / "references" / "attesters"
        (bundle / "computations").mkdir(parents=True); comps.mkdir(parents=True); atts.mkdir()
        comp = comps / "stub.py"
        comp.write_text(
            "import hashlib, json, sys\n"
            "args = sys.argv[1:]\nout = args[args.index('--receipt') + 1]\n"
            "json.dump({'run_id': 'r-' + hashlib.sha256(__file__.encode()).hexdigest()[:6],\n"
            "           'code_sha256': hashlib.sha256(open(__file__, 'rb').read()).hexdigest(),\n"
            "           'data': {'record': {'record': 'stub-tree'}}, 'value': 1.0}, open(out, 'w'))\n",
            encoding="utf-8")
        att = atts / "stub_check.py"
        att.write_text(
            "import hashlib, json, sys\n"
            "r = json.load(open(sys.argv[1]))\n"
            "want = hashlib.sha256(open(sys.argv[3], 'rb').read()).hexdigest()\n"
            "ok = r['code_sha256'] == want\nprint('PASS' if ok else 'FAIL: code_sha256')\n"
            "sys.exit(0 if ok else 1)\n", encoding="utf-8")
        (bundle / "computations" / "stub.md").write_text(
            "---\ntype: Attested Computation\ncomputation: references/computations/stub.py\n"
            "attester:\n  resource: references/attesters/stub_check.py\nstatus: draft\n---\nBody\n",
            encoding="utf-8")
        assert attester_for(comp, bundle) == att
        assert attester_for(comps / "other.py", bundle) is None
        subprocess.run(["git", "-C", str(root), "add", "-A"], check=True)
        subprocess.run(["git", "-C", str(root), "commit", "-q", "-m", "stub"], check=True)

        # Stubs run under plain python; the real ritual runs `uv run`.
        def runner(argv, cwd):
            argv = [str(a) for a in argv]
            if argv[:2] == ["uv", "run"]:
                argv = [sys.executable] + argv[2:]
            return run_cmd(argv, cwd)

        keep = root / "keep"; keep.mkdir()
        r = Ritual(comp, att, ["--x", "1"], keep, repo=root, runner=runner)
        assert r.perform("HEAD") is True, r.steps
        assert [s[0] for s in r.steps] == ["NEW PASS", "TAMPER FAIL"], r.steps
        assert r.skipped and "re-verification" in r.skipped[0]
        text = r.report("", "references/computations/stub.py")
        assert "RE-VERIFICATION" in text and "unchanged" in text and "stub-tree" in text

        comp.write_text(comp.read_text(encoding="utf-8") + "# edited\n", encoding="utf-8")
        keep2 = root / "keep2"; keep2.mkdir()
        r = Ritual(comp, att, [], keep2, repo=root, runner=runner)
        assert r.perform("HEAD") is True, r.steps
        assert [s[0] for s in r.steps] == ["NEW PASS", "OLD PASS", "OLD vs NEW", "TAMPER FAIL"], r.steps
        assert not r.skipped
        text = r.report("A test edit.", "references/computations/stub.py")
        assert "RE-ATTESTATION" in text and " -> " in text and "A test edit." in text
        assert "BAD" not in text

        # An attester that always passes must make the ritual fail: the
        # tamper and the old-vs-new steps are required to FAIL.
        att.write_text("import sys\nprint('PASS')\nsys.exit(0)\n", encoding="utf-8")
        keep3 = root / "keep3"; keep3.mkdir()
        r = Ritual(comp, att, [], keep3, repo=root, runner=runner)
        assert r.perform("HEAD") is False
        bad = [s for s in r.steps if s[1] != s[2]]
        assert {s[0] for s in bad} == {"OLD vs NEW", "TAMPER FAIL"}, r.steps

        reg = load_registry()
        for name, spec in reg["runs"].items():
            assert (COMPUTATIONS / spec["computation"]).is_file(), name
            assert isinstance(spec.get("args"), list), name
            if spec.get("needs"):
                assert spec["needs"] in reg["runs"], name
            assert spec.get("data_root", "fixtures") in ("none", *reg["data_roots"]), name
            assert attester_for(COMPUTATIONS / spec["computation"]) is not None, name
    print("reattest selftest: ok")
    return 0


def resolve_args(spec: dict, reg: dict, receipts: dict, data_root_override):
    """A registry run's argv, with {receipt:NAME} filled in and the
    data root appended unless the run reads none."""
    args = []
    for a in spec.get("args", []):
        m = re.fullmatch(r"\{receipt:([^}]+)\}", str(a))
        args.append(receipts[m.group(1)] if m else a)
    root_key = spec.get("data_root", "fixtures")
    if root_key != "none":
        root = data_root_override or Path(os.path.expanduser(reg["data_roots"][root_key]))
        args += ["--data-root", root]
    return args


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("computation", nargs="?", type=Path)
    ap.add_argument("args", nargs="*", help="the computation's arguments, after --")
    ap.add_argument("--run", help="a run name from tools/reference_runs.yaml")
    ap.add_argument("--attester", type=Path)
    ap.add_argument("--data-root", type=Path, help="override the registry's data root")
    ap.add_argument("--old", default="HEAD", help="the reference version, a git ref (default HEAD)")
    ap.add_argument("--note", default="", help="why the file changed, for the log entry draft")
    ap.add_argument("--keep", type=Path, help="directory for the receipts and files (default: a new temp dir)")
    ap.add_argument("--list", action="store_true", help="list the registry runs")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    reg = load_registry()
    if a.list:
        for name, spec in reg["runs"].items():
            print(f"{name:<20} {spec['computation']:<40} {' '.join(map(str, spec.get('args', [])))}")
        return 0

    keep = a.keep or Path(tempfile.mkdtemp(prefix="reattest-"))
    keep.mkdir(parents=True, exist_ok=True)
    receipts = {}
    if a.run:
        if a.run not in reg["runs"]:
            ap.error(f"unknown run {a.run}; --list shows them")
        order = []
        name = a.run
        while name:
            order.insert(0, name)
            name = reg["runs"][name].get("needs")
        # Runs this one needs are produced first, from the working tree,
        # and their receipts substituted; only the named run is attested.
        for dep in order[:-1]:
            spec = reg["runs"][dep]
            comp = COMPUTATIONS / spec["computation"]
            out = keep / f"receipt_{dep}.json"
            rc, text = run_cmd(["uv", "run", comp, *resolve_args(spec, reg, receipts, a.data_root),
                                "--receipt", out], REPO)
            if rc != 0:
                print(f"needed run {dep} failed:\n{text[-600:]}")
                return 1
            receipts[dep] = out
            print(f"needed run {dep}: receipt {out}")
        spec = reg["runs"][a.run]
        computation = COMPUTATIONS / spec["computation"]
        args = resolve_args(spec, reg, receipts, a.data_root)
        attester = a.attester or (BUNDLE / spec["attester"] if spec.get("attester") else None)
    else:
        if not a.computation:
            ap.error("give --run NAME or a COMPUTATION.py")
        computation = a.computation
        args = list(a.args)
        if a.data_root:
            args += ["--data-root", a.data_root]
        attester = a.attester
    if not computation.is_file():
        ap.error(f"no such computation: {computation}")
    attester = attester or attester_for(computation)
    if attester is None or not attester.is_file():
        ap.error("no attester: no concept names this computation; give --attester")
    rel = computation.resolve().relative_to(BUNDLE.resolve()).as_posix() \
        if computation.resolve().is_relative_to(BUNDLE.resolve()) else computation.as_posix()

    print(f"re-attesting {rel} with {attester.relative_to(BUNDLE) if attester.is_relative_to(BUNDLE) else attester}")
    print(f"  args: {' '.join(str(x) for x in args)}")
    ritual = Ritual(computation, attester, args, keep)
    ok = ritual.perform(a.old)
    print(ritual.report(a.note, rel))
    print()
    print("reattest: " + ("every step landed as the contract requires"
                          if ok else "FAILED, see the BAD lines above"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
