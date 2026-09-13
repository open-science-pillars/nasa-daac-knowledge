#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# ///
"""Append a verified event to a concept: the steward's signature, or
a data provider's confirmation recorded on their behalf, as one command.

A signature is a `verified` event in the concept's frontmatter,
`{ by: human:<id>, at: <UTC time>, role: <role> }`, with `source: <URL>`
when the confirmation was given somewhere citable. `by` and `at` are
the OKF shape (consumers key on the `human:` prefix); `role` and
`source` are the OSP extension keys, allowed by OKF's extensions rule.
The role says whose word the event carries:

  maintainer  the steward who holds the bundle signs (the default; an
              event with no `role` key means this)
  provider    a person from the organization that produces the data
              confirmed the concept, either by signing themselves or
              by answering a "confirm this concept" issue, in which
              case the steward records the event on their behalf with
              `--by human:<their id>` and `--source <the reply URL>`
  community   a user of the data confirmed it the same way

The trust tier a consumer reads follows from the events: unverified
(none), machine-confirmed (process events only), human-reviewed (a
human event), provider-confirmed (a human event with role provider).
A provider's confirmation is invited at any point and never required.

A concept edited after its signing commit owes a new event (the
merge-then-sign rule, as signature_check.py measures it), and the
steward pays the debt by appending one: the earlier events stay as
history, the newest one is the signature that binds the text from its
commit on. This tool writes exactly that edit, so re-signing a handful
of concepts is one command and one commit rather than a hand edit per
file:

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
          [--role maintainer|provider|community] [--source URL]
          [--log knowledge/<bundle>/log.md --note TEXT] [--dry-run]
  sign.py --selftest

--by defaults to human:<git user.name with spaces removed>; --at to
now, UTC, whole seconds. --source is required when --role provider is
recorded for someone other than the git user (the on-behalf case: the
URL is where they gave the confirmation, an issue reply or a review
comment, and it is what makes the recorded event checkable). The
signature is PENDING until the edit is committed, and only the steward
or someone acting on the steward's explicit word runs this: the tool
moves the pen, it does not decide.
"""

import argparse
import datetime as dt
import re
import subprocess
import sys
import tempfile
import textwrap
from pathlib import Path

ROLES = ("maintainer", "provider", "community")


def event_text(by: str, at: str, role: str = "maintainer", source: str | None = None) -> str:
    """The event in the flow style the bundles write, one line."""
    text = f"{{ by: {by}, at: {at}, role: {role}"
    if source:
        text += f", source: {source}"
    return text + " }"


def now_utc() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def default_by() -> str:
    try:
        name = subprocess.run(["git", "config", "user.name"], check=True,
                              capture_output=True, text=True).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        name = ""
    return "human:" + re.sub(r"\s+", "", name) if name else ""


def sign_text(text: str, by: str, at: str, role: str = "maintainer",
              source: str | None = None):
    """The concept text with the event appended; (new text, note)."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        raise ValueError("no frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError:
        raise ValueError("frontmatter never closes")
    event = event_text(by, at, role, source)
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


def log_entry(paths, note: str, day: str, first: bool = False,
              role: str = "maintainer", by: str = "", source: str | None = None) -> str:
    """The bundle's log line for this signing act.

    A concept signed for the first time has no earlier events to keep,
    so the entry says so; a concept signed again does, and the sentence
    about history is what the merge-then-sign rule asks the log to
    record. A provider or community event names its role, whose word it
    carries and where that word was given, so the log reads the same as
    the event."""
    names = ", ".join(paths)
    if role == "maintainer":
        act = "STEWARD SIGNING" if first else "STEWARD RE-SIGNING"
        tail = ("The verified event is written on the steward's word."
                if first else
                "The new verified event is appended on the steward's word, "
                "the earlier events kept as history.")
    else:
        act = f"{role.upper()} CONFIRMATION"
        tail = (f"The verified event carries role {role} by {by}"
                + (f", given at {source}" if source else "")
                + ("." if first else ", the earlier events kept as history."))
    body = f"{day} · {act} of {names}: {note} {tail} (steward)"
    # break_on_hyphens=False keeps a concept path in one piece: a path
    # broken across lines at one of its hyphens is no longer a path.
    return textwrap.fill(body, width=72, initial_indent="- ",
                         subsequent_indent="  ", break_on_hyphens=False,
                         break_long_words=False)


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
            f"  - {event_text(by, at)}\nstatus: stable") in out, out
    assert event_text(by, at) == "{ by: human:Tester, at: 2026-09-05T12:00:00Z, role: maintainer }"
    assert out.endswith("---\n\nBody.\n") and "single" in note
    out2, note2 = sign_text(out, by, "2026-09-06T00:00:00Z")
    assert out2.count("  - {") == 3 and "event 3" in note2, (out2, note2)
    assert out2.index("2026-09-06") > out2.index("2026-09-05")
    # A provider's confirmation recorded on their behalf: role and the
    # reply URL inside the same one-line event, after by and at.
    url = "https://github.com/open-science-pillars/nasa-daac-knowledge/issues/9#issuecomment-1"
    out4, note4 = sign_text(out2, "human:ProviderPerson", "2026-09-07T00:00:00Z", "provider", url)
    assert ("  - { by: human:ProviderPerson, at: 2026-09-07T00:00:00Z, role: provider, "
            f"source: {url} }}\nstatus: stable") in out4, out4
    assert "event 4" in note4
    assert event_text("human:U", at, "community") == f"{{ by: human:U, at: {at}, role: community }}"
    unsigned = "---\ntype: Gotcha\ngenerated: { by: x, at: 2026-01-01T00:00:00Z }\nstatus: draft\n---\nBody\n"
    out3, note3 = sign_text(unsigned, by, at)
    assert f"generated: {{ by: x, at: 2026-01-01T00:00:00Z }}\nverified: {event_text(by, at)}\nstatus: draft" in out3, out3
    assert "first signature" in note3 and "status: draft" in note3
    out5, _ = sign_text(unsigned, "human:ProviderPerson", at, "provider", url)
    assert f"verified: {{ by: human:ProviderPerson, at: {at}, role: provider, source: {url} }}" in out5, out5
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
        assert "earlier events kept as history" in text
        firstlog = Path(d) / "first.md"
        firstlog.write_text("# log\n\nNewest first.\n", encoding="utf-8")
        add_log(firstlog, log_entry(["a.md"], "the first signature.", "2026-09-05", first=True))
        ftext = firstlog.read_text(encoding="utf-8")
        assert "STEWARD SIGNING of a.md" in ftext and "RE-SIGNING" not in ftext
        assert "kept as history" not in ftext
        # A hyphenated concept path survives the wrapping in one piece.
        wrapped = Path(d) / "wrap.md"
        wrapped.write_text("# log\n\nNewest first.\n", encoding="utf-8")
        add_log(wrapped, log_entry(["knowledge/gotchas/mod16-fill-over-water-barren-urban.md"],
                                   "a path long enough to need wrapping in the entry.", "2026-09-06"))
        assert "knowledge/gotchas/mod16-fill-over-water-barren-urban.md" in wrapped.read_text(encoding="utf-8")
        assert "\n\n- 2026-01-01" in text and text.startswith("# log\n\nNewest first.\n\n- 2026-09-05")
        empty = Path(d) / "empty.md"
        empty.write_text("# log\n\nNewest first.\n", encoding="utf-8")
        add_log(empty, log_entry(["a.md"], "note.", "2026-09-05"))
        assert "STEWARD RE-SIGNING of a.md" in empty.read_text(encoding="utf-8")
        # The on-behalf entry names the role, the person and the source.
        onbehalf = Path(d) / "onbehalf.md"
        onbehalf.write_text("# log\n\nNewest first.\n", encoding="utf-8")
        add_log(onbehalf, log_entry(["a.md"], "confirmed in the issue.", "2026-09-07",
                                    role="provider", by="human:ProviderPerson", source=url))
        otext = onbehalf.read_text(encoding="utf-8")
        assert "PROVIDER CONFIRMATION of a.md" in otext and "SIGNING" not in otext, otext
        assert "role provider by human:ProviderPerson" in otext and url in otext, otext
        assert "kept as history" in otext
    print("sign selftest: ok")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("concepts", nargs="*", type=Path)
    ap.add_argument("--by", default=None, help="signer id, default human:<git user.name>")
    ap.add_argument("--at", default=None, help="UTC time, default now")
    ap.add_argument("--role", choices=ROLES, default="maintainer",
                    help="whose word the event carries: maintainer (the steward, default), "
                         "provider (a person from the data's producing organization), "
                         "community (a user of the data)")
    ap.add_argument("--source", default=None, metavar="URL",
                    help="where the person gave the confirmation (an issue reply, a review "
                         "comment); required with --role provider when --by is not the git "
                         "user, that is when the steward records the event on someone's behalf")
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
    if args.source and not re.match(r"https?://\S+$", args.source):
        ap.error("--source must be a URL (where the confirmation was given)")
    if args.role == "provider" and not args.source and by != default_by():
        ap.error("--role provider recorded for someone other than the git user needs "
                 "--source URL, the issue reply or review comment where they confirmed")
    rc = 0
    notes = []
    for path in args.concepts:
        try:
            new, note = sign_text(path.read_text(encoding="utf-8"), by, at,
                                  args.role, args.source)
        except (OSError, ValueError) as e:
            print(f"SKIP {path}: {e}")
            rc = 1
            continue
        if not args.dry_run:
            path.write_text(new, encoding="utf-8")
        notes.append(note)
        print(f"{'would sign' if args.dry_run else 'signed'} {path}: {note}")
    if args.log and rc == 0:
        entry = log_entry([p.as_posix() for p in args.concepts], args.note.strip(),
                          at[:10], first=all(n.startswith("first signature") for n in notes),
                          role=args.role, by=by, source=args.source)
        if not args.dry_run:
            add_log(args.log, entry)
        print(("would add to " if args.dry_run else "logged in ") + args.log.as_posix())
    if rc == 0:
        print(f"event {event_text(by, at, args.role, args.source)}; pending until committed "
              "(signature_check.py shows PENDING, then nothing owed)")
    return rc


if __name__ == "__main__":
    sys.exit(main())
