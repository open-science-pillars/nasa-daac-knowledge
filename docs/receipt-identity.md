# Receipts name the capability release

Every receipt an attested computation writes, and every attestation an
attester writes about one, carries two blocks beyond its code and data
digests:

```json
{
  "capability": {"name": "core", "version": "0.5.1", "release_lock": "sha256:..."},
  "runtime":    {"name": "claude-code", "version": "2.1.269 (Claude Code)"}
}
```

`capability` is the package the executor shipped in: its name and
version from `.osp/package.yaml`, and the sha256 of its
`.osp/release-lock.json` taken as a value (null where the tree carries
no lock). `runtime` is the runtime that ran the executor, declared by
the caller, with its version where known. An attester refuses a receipt
whose capability is not the package beside it.

This is what the multi-runtime packaging decision asks for (ADR B in the
marketplace repository): a result produced on Claude Code, Claude Cowork
or Codex is verified under one attester, and its receipt says which
governed release it is evidence for, so two runtimes can be shown to have
executed the same release and a qualification record can cite the
attestation. `tools/receipt_identity.py` checks a receipt or an
attestation for the two blocks, and with `--package DIR` for agreement
with a package tree; it runs in the check routine's selftests. The
foundation capability's reference computation
(core, `verification/trend_computation.py` and `trend_attester.py`) is
the first executor and attester written to this convention. The ECCO
computations in this bundle predate it; each gains the blocks at its
next re-attestation, which the ritual in `tools/reattest.py` records.
