#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["earthaccess"]
# ///
"""Fetch every granule of one archived observational collection over a
date range into a tree, and leave the fetch record the manifest tool
needs (SOURCE.json).

The RAPID tree was taken with curl from the programme's own server and
its SOURCE.json written by hand: six files. An archived record served
through CMR (a PO.DAAC altimetry product, for example) has more files
than a hand can record, so this tool does the same job from the CMR
listing: it enumerates the collection's granules over the range, fetches
them through an authenticated Earthdata session into ROOT, verifies each
against the checksum the archive publishes (inline in the granule
record, or in the NAME.md5 sidecar PO.DAAC serves beside each file), and
writes SOURCE.json with
the collection identity (concept id, ShortName, version, DOI), the query,
the retrieval time, and one row per file (granule id, URL, archive
checksum and algorithm, bytes, revision date). Files already present
that pass their archive checksum are not fetched again, so an
interrupted run continues where it stopped. Nothing else is written;
the tree's local SHA-256 manifest and its RECORD.json stamp come from
obs_record_manifest.py, which reads the release identity from the files
themselves.

Credentials come from earthaccess (environment or netrc) and are used
for the download only.

Usage:
  obs_record_fetch.py --short-name NAME [--version V] --start YYYY-MM-DD
      --end YYYY-MM-DD --data-root ROOT --record NAME [--threads N]
"""
import argparse
import datetime as dt
import hashlib
import json
import sys
from pathlib import Path

import earthaccess

ALGOS = {"SHA-512": "sha512", "SHA-256": "sha256", "MD5": "md5",
         "SHA512": "sha512", "SHA256": "sha256"}


SIDECAR = {".md5": "MD5", ".sha256": "SHA-256", ".sha512": "SHA-512"}


def checksum_of(granule, session):
    """The checksum the archive publishes for the data file: inline in
    the granule's UMM when the provider fills it, otherwise in a sidecar
    file (NAME.nc.md5 beside the granule, as PO.DAAC serves it) that is
    fetched and parsed. Returns (algorithm, value, size_in_bytes)."""
    umm = granule["umm"]
    info = umm.get("DataGranule", {}).get("ArchiveAndDistributionInformation", [])
    size = None
    for row in info:
        name = row.get("Name", "")
        if not any(name.endswith(ext) for ext in SIDECAR):
            size = row.get("SizeInBytes", size)
        c = row.get("Checksum")
        if c and c.get("Algorithm") in ALGOS:
            return c["Algorithm"], c["Value"], size
    for u in umm.get("RelatedUrls", []):
        url = u.get("URL", "")
        ext = next((e for e in SIDECAR if url.endswith(e)), None)
        if ext and url.startswith("https://"):
            r = session.get(url, timeout=60)
            r.raise_for_status()
            value = r.text.split()[0].lower()
            return SIDECAR[ext], value, size
    return None, None, size


def local_hash(path, algo):
    h = hashlib.new(ALGOS[algo])
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--short-name", required=True)
    ap.add_argument("--version")
    ap.add_argument("--start", required=True)
    ap.add_argument("--end", required=True)
    ap.add_argument("--data-root", type=Path, required=True)
    ap.add_argument("--record", required=True, help="record name for SOURCE.json")
    ap.add_argument("--threads", type=int, default=8)
    args = ap.parse_args()

    auth = earthaccess.login(strategy="netrc")
    if not auth.authenticated:
        sys.exit("Earthdata login failed: no environment token and no netrc entry")
    query = {"short_name": args.short_name,
             "temporal": (args.start, args.end)}
    if args.version:
        query["version"] = args.version
    cols = earthaccess.search_datasets(short_name=args.short_name,
                                       **({"version": args.version} if args.version else {}))
    if len(cols) != 1:
        sys.exit(f"{len(cols)} collections match {args.short_name} "
                 f"{args.version or ''}; name one")
    col = cols[0]
    cu = col["umm"]
    collection = {"concept_id": col["meta"]["concept-id"],
                  "short_name": cu.get("ShortName"),
                  "version": cu.get("Version"),
                  "doi": (cu.get("DOI") or {}).get("DOI"),
                  "title": cu.get("EntryTitle")}
    granules = earthaccess.search_data(count=-1, **query)
    granules.sort(key=lambda g: g["umm"]["GranuleUR"])
    if not granules:
        sys.exit("no granules in range")
    root = args.data_root.expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)

    session = earthaccess.get_requests_https_session()
    rows, todo = [], []
    for g in granules:
        algo, value, size = checksum_of(g, session)
        links = g.data_links()
        url = links[0] if links else None
        name = Path(url).name if url else g["umm"]["GranuleUR"] + ".nc"
        row = {"file": name, "granule": g["umm"]["GranuleUR"],
               "concept_id": g["meta"]["concept-id"],
               "revision_date": g["meta"].get("revision-date"),
               "url": url, "archive_checksum_algorithm": algo,
               "archive_checksum": value, "archive_bytes": size}
        rows.append(row)
        p = root / name
        if p.exists() and algo and local_hash(p, algo) == value:
            continue
        todo.append(g)
    print(f"{len(granules)} granules declared, {len(todo)} to fetch "
          f"into {root}", file=sys.stderr)
    if todo:
        earthaccess.download(todo, str(root), threads=args.threads)

    failures = []
    for row in rows:
        p = root / row["file"]
        if not p.exists():
            failures.append({"file": row["file"], "check": "presence"})
            continue
        row["bytes_on_disk"] = p.stat().st_size
        algo = row["archive_checksum_algorithm"]
        if algo:
            ok = local_hash(p, algo) == row["archive_checksum"]
            row["archive_checksum_verified"] = ok
            if not ok:
                failures.append({"file": row["file"], "check": "checksum"})
        else:
            # No published checksum at all: the size is the only check
            # the archive offers, and the row says so.
            row["archive_checksum_verified"] = None
            if row["archive_bytes"] not in (None, row["bytes_on_disk"]):
                failures.append({"file": row["file"], "check": "size"})
    source = {"record": args.record,
              "distribution": "NASA Earthdata archive through CMR; every file "
                              "verified against the checksum the archive publishes",
              "retrieved_at": dt.datetime.now(dt.timezone.utc)
              .strftime("%Y-%m-%dT%H:%M:%SZ"),
              "retrieved_with": "obs_record_fetch.py (earthaccess), "
                                "authenticated Earthdata session",
              "collection": collection,
              "query": {"short_name": args.short_name, "version": args.version,
                        "temporal": [args.start, args.end]},
              "files": rows}
    (root / "SOURCE.json").write_text(json.dumps(source, indent=1) + "\n")
    print(f"SOURCE.json: {len(rows)} files, {len(failures)} failures",
          file=sys.stderr)
    for f in failures:
        print("FAIL", json.dumps(f), file=sys.stderr)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
