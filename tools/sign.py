#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# ///
"""Append the steward's verified event to a concept, the signing act
as one command.

A steward's signature is a `verified` event in the concept's
frontmatter, `{ by: human:<id>, at: <UTC time> }`. A concept edited
after its signing commit owes a new one (the merge-then-sign rule, as
signature_check.py measures it), and the steward pays the debt by
appending an event: the earlier events stay as history, the newest one
is the signature that binds the text from its commit on. This tool
writes exactly that edit, so re-signing a handful of concepts is one
command and one commit rather than a hand edit per file:

  - `verified: { ... }` (a single event) becomes a two-item list, the
    old event first;
  - a `verified:` list gains one item at its end;
  - a concept with no `verified` key gets a single event (a first
    signature; the status line is left alone and reported, since
    promotion to stable is the steward's separate decision).

Nothing else in the file changes, so the signing commit's diff is the
event alone. With --log the bundle's change log gains one entry, newest
first, naming the concepts and the reason given with --note.

  sign.py CONCEPT [CONCEPT ...] [--by human:ID] [--at ISO-Z]
          [--log knowledge/<bundle>/log.md --note TEXT] [--dry-run]
  sign.py --selftest

--by defaults to human:<git user.name with spaces removed>; --at to
now, UTC, whole seconds. The signature is PENDING until the edit is
committed, and only the steward or someone acting on the steward's
explicit word runs this: the tool moves the pen, it does not decide.
"""

import argparse
import datetime as dt
import re
import subprocess
import sys
import tempfile
import textwrap
from pathlib import Path

EVENT = "{ by: %s, at: %s }"


def now_utc() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def default_by() -> str:
    try:
        name = subprocess.run(["git", "config", "user.name"], check=True,
                              capture_output=True, text=True).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        name = ""
    return "human:" + re.sub(r"\s+", "", name) if name else ""


def sign_text(text: str, by: str, at: str):
    """The concept text with the event appended; (new text, note)."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        raise ValueError("no frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError:
        raise ValueError("frontmatter never closes")
    event = EVENT % (by, at)
    idx = next((i for i in range(1, end)
                if re.match(r"verified:(\s|$)", lines[i])), None)
    if idx is None:
        status = next((l for l in lines[1:end] if l.startswith("status:")), "")
        anchor = next((i for i in range(1, end)
                       if lines[i].startswith(("generated:", "status:"))), end)
        insert = anchor + 1 if lines[anchor].startswith("generated:") else anchor
        lines.insert(insert, f"verified: {event}")
        note = "first signature" + (f"; {status.strip()} left as is" if status else "")
        return "\n".join(lines), note
    head = lines[idx]
    rest = head[len("verified:"):].strip()
    if rest:
        if not (rest.startswith("{") and rest.endswith("}")):
            raise ValueError(f"unrecognized verified value: {rest}")
        lines[idx:idx + 1] = ["verified:", f"  - {rest}", f"  - {event}"]
        return "\n".join(lines), "single event became a list of two"
    last = idx
    while last + 1 < end and lines[last + 1].startswith("  - "):
        last += 1
    if last == idx:
        raise ValueError("verified: is empty")
    lines.insert(last + 1, f"  - {event}")
    return "\n".join(lines), f"appended as event {last - idx + 1}"


def log_entry(paths, note: str, day: str) -> str:
    names = ", ".join(paths)
    body = (f"{day} · STEWARD RE-SIGNING of {names}: {note} The new verified "
            "event is appended on the steward's word, the earlier events "
            "kept as history. (steward)")
    return textwrap.fill(body, width=72, initial_indent="- ",
                         subsequent_indent="  ")


def add_log(log: Path, entry: str) -> None:
    lines = log.read_text(encoding="utf-8").split("\n")
    first = next((i for i, l in enumerate(lines) if re.match(r"- \d{4}-\d{2}-\d{2}", l)),
                 len(lines))
    lines[first:first] = entry.split("\n") + ([""] if first < len(lines)
                                              and lines[first].startswith("- 2") else [])
    log.write_text("\n".join(lines), encoding="utf-8")


def selftest() -> int:
    by, at = "human:Tester", "2026-09-05T12:00:00Z"
    single = ("---\ntype: Gotcha\ngenerated: { by: x, at: 2026-01-01T00:00:00Z }\n"
              "verified: { by: human:Tester, at: 2026-02-01T00:00:00Z }\n"
              "status: stable\n---\n\nBody.\n")
    out, note = sign_text(single, by, at)
    assert ("verified:\n  - { by: human:Tester, at: 2026-02-01T00:00:00Z }\n"
            f"  - {EVENT % (by, at)}\nstatus: stable") in out, out
    assert out.endswith("---\n\nBody.\n") and "single" in note
    out2, note2 = sign_text(out, by, "2026-09-06T00:00:00Z")
    assert out2.count("  - {") == 3 and "event 3" in note2, (out2, note2)
    assert out2.index("2026-09-06") > out2.index("2026-09-05")
    unsigned = "---\ntype: Gotcha\ngenerated: { by: x, at: 2026-01-01T00:00:00Z }\nstatus: draft\n---\nBody\n"
    out3, note3 = sign_text(unsigned, by, at)
    assert f"generated: {{ by: x, at: 2026-01-01T00:00:00Z }}\nverified: {EVENT % (by, at)}\nstatus: draft" in out3, out3
    assert "first signature" in note3 and "status: draft" in note3
    for bad in ("no frontmatter\n", "---\ntype: X\nverified: yes\n---\n"):
        try:
            sign_text(bad, by, at)
        except ValueError:
            pass
        else:
            raise AssertionError(bad)
    with tempfile.TemporaryDirectory() as d:
        log = Path(d) / "log.md"
        log.write_text("# log\n\nNewest first.\n\n- 2026-01-01 · older entry\n", encoding="utf-8")
        add_log(log, log_entry(["a.md", "b.md"], "the wording sweep changed them.", "2026-09-05"))
        text = log.read_text(encoding="utf-8")
        assert text.index("2026-09-05 · STEWARD RE-SIGNING of a.md, b.md") < text.index("older entry")
        assert "\n\n- 2026-01-01" in text and text.startswith("# log\n\nNewest first.\n\n- 2026-09-05")
        empty = Path(d) / "empty.md"
        empty.write_text("# log\n\nNewest first.\n", encoding="utf-8")
        add_log(empty, log_entry(["a.md"], "note.", "2026-09-05"))
        assert "STEWARD RE-SIGNING of a.md" in empty.read_text(encoding="utf-8")
    print("sign selftest: ok")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("concepts", nargs="*", type=Path)
    ap.add_argument("--by", default=None, help="signer id, default human:<git user.name>")
    ap.add_argument("--at", default=None, help="UTC time, default now")
    ap.add_argument("--log", type=Path, help="the bundle change log to add an entry to")
    ap.add_argument("--note", default="", help="the reason, one sentence, for the log entry")
    ap.add_argument("--dry-run", action="store_true", help="report, write nothing")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    if not args.concepts:
        ap.error("give at least one CONCEPT or --selftest")
    by = args.by or default_by()
    if not by.startswith("human:") or len(by) < 7:
        ap.error("--by must be human:<id> (git user.name is unset)")
    at = args.at or now_utc()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", at):
        ap.error("--at must be YYYY-MM-DDTHH:MM:SSZ")
    if args.log and not args.note:
        ap.error("--log needs --note, the reason the log records")
    rc = 0
    for path in args.concepts:
        try:
            new, note = sign_text(path.read_text(encoding="utf-8"), by, at)
        except (OSError, ValueError) as e:
            print(f"SKIP {path}: {e}")
            rc = 1
            continue
        if not args.dry_run:
            path.write_text(new, encoding="utf-8")
        print(f"{'would sign' if args.dry_run else 'signed'} {path}: {note}")
    if args.log and rc == 0:
        entry = log_entry([p.as_posix() for p in args.concepts], args.note.strip(), at[:10])
        if not args.dry_run:
            add_log(args.log, entry)
        print(("would add to " if args.dry_run else "logged in ") + args.log.as_posix())
    if rc == 0:
        print(f"event {EVENT % (by, at)}; pending until committed "
              "(signature_check.py shows PENDING, then nothing owed)")
    return rc


if __name__ == "__main__":
    sys.exit(main())
