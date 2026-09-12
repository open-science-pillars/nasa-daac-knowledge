#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Does a receipt (or an attestation) identify the capability release and
the runtime that produced it? Stdlib only, no LLM.

The multi-runtime packaging decision (ADR B in the marketplace
repository) asks every receipt to name the governed release it is
evidence for, so that a result produced on Claude Code, Claude Cowork
or Codex can be shown to belong to one release and be verified under
one attester. The convention (docs/receipt-identity.md):

  capability: { name, version, release_lock }   release_lock is the
                                                 sha256 of the package's
                                                 .osp/release-lock.json as
                                                 a value, or null where the
                                                 tree carries none
  runtime:    { name, version }                  version may be null

Exit 0 when the blocks are present and well formed; with --package DIR
also when they match that package's .osp/package.yaml version and name
and its release lock. Exit 1 naming what is missing or differs.

  receipt_identity.py RECEIPT.json [--package DIR]
  receipt_identity.py --selftest
"""
import argparse
import hashlib
import json
import re
import sys
import tempfile
from pathlib import Path


def value_digest(value) -> str:
    return "sha256:" + hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()


def package_identity(root: Path) -> dict:
    """name, version and lock digest from a package tree, without pyyaml:
    the two scalar lines of package.yaml are all that is needed."""
    text = (root / ".osp" / "package.yaml").read_text(encoding="utf-8")
    block = text.split("package:", 1)[1]
    name = re.search(r"^\s+name:\s*['\"]?([A-Za-z0-9._-]+)", block, re.M)
    version = re.search(r"^\s+version:\s*['\"]?([0-9][0-9.]*)", block, re.M)
    lock_path = root / ".osp" / "release-lock.json"
    lock = json.loads(lock_path.read_text(encoding="utf-8")) if lock_path.is_file() else None
    return {"name": name.group(1) if name else None, "version": version.group(1) if version else None,
            "release_lock": value_digest(lock) if lock is not None else None}


def findings(doc: dict, package: dict | None = None) -> list[str]:
    out = []
    cap = doc.get("capability")
    if not isinstance(cap, dict):
        out.append("capability block missing")
    else:
        for k in ("name", "version"):
            if not isinstance(cap.get(k), str) or not cap.get(k):
                out.append(f"capability.{k} missing")
        if "release_lock" not in cap:
            out.append("capability.release_lock missing (null where the tree carries no lock)")
        elif cap["release_lock"] is not None and not re.match(r"^sha256:[0-9a-f]{64}$", str(cap["release_lock"])):
            out.append("capability.release_lock is not a sha256 digest")
    rt = doc.get("runtime")
    if not isinstance(rt, dict) or not isinstance(rt.get("name"), str) or not rt.get("name"):
        out.append("runtime.name missing")
    if package and isinstance(cap, dict):
        for k in ("name", "version", "release_lock"):
            if cap.get(k) != package.get(k):
                out.append(f"capability.{k} {cap.get(k)!r} is not the package's {package.get(k)!r}")
    return out


def selftest() -> int:
    good = {"capability": {"name": "core", "version": "0.5.1", "release_lock": "sha256:" + "0" * 64},
            "runtime": {"name": "openai-codex", "version": None}}
    assert findings(good) == []
    assert "capability block missing" in findings({"runtime": {"name": "x"}})
    assert any("release_lock missing" in f for f in findings({"capability": {"name": "a", "version": "1"}, "runtime": {"name": "x"}}))
    assert any("runtime.name" in f for f in findings({"capability": good["capability"]}))
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / ".osp").mkdir()
        (root / ".osp" / "package.yaml").write_text("schema_version: 1\npackage:\n  name: core\n  version: 0.5.1\n  type: foundation\n")
        pkg = package_identity(root)
        assert pkg == {"name": "core", "version": "0.5.1", "release_lock": None}, pkg
        assert any("release_lock" in f for f in findings(good, pkg))
        lock = {"package": "core", "version": "0.5.1"}
        (root / ".osp" / "release-lock.json").write_text(json.dumps(lock))
        pkg = package_identity(root)
        assert findings(dict(good, capability=dict(good["capability"], release_lock=value_digest(lock))), pkg) == []
    print("receipt_identity selftest: PASSED")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("receipt", nargs="?")
    ap.add_argument("--package", default=None, help="package tree whose identity the receipt must match")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    if not args.receipt:
        ap.error("a receipt path or --selftest")
    doc = json.loads(Path(args.receipt).read_text(encoding="utf-8"))
    package = package_identity(Path(args.package)) if args.package else None
    out = findings(doc, package)
    cap, rt = doc.get("capability") or {}, doc.get("runtime") or {}
    if out:
        for f in out:
            print(f"  {f}")
        print(f"FAIL: {args.receipt} does not identify a capability release")
        return 1
    print(f"PASS: {args.receipt} is {cap.get('name')} {cap.get('version')} (lock {cap.get('release_lock')}) on {rt.get('name')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
