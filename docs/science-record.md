# The science record and the fixture cache

Two local trees hold ECCO V4r4 granules on a machine that runs the
sanctioned computations in this bundle. They are physically separate,
each is described by a manifest committed here, each has been verified
against its manifest file by file, and every receipt names the one that
fed it. This document is the rule, the machinery that enforces it, and
the coverage statement for the record as verified on 2026-09-01.

## The two trees

| | fixture cache | science record |
|---|---|---|
| root | `~/ECCO_V4r4` | `~/ECCO_V4r4_record` |
| record name | `ecco-v4r4-fixtures-2010` | `ecco-v4r4-science-record` |
| manifest | `podaac/references/retrieval/fixtures-2010-manifest.json` | `podaac/references/retrieval/science-record-manifest.json` |
| verification report | `fixtures-2010-verification.json` (same directory) | `science-record-verification.json` (same directory) |
| contents | 144 files, 3.08 GB: the 2010 months of the collections the computations read, the 2009-12 month a few of them need, the 2011-01 boundary snapshots, the geometry granule, the tutorial geothermal file | 4,056 files, 85.54 GB: eleven monthly collections 1992-01 through 2017-12, two snapshot collections at 311 month boundaries, geometry, geothermal |
| purpose | gates, CI, attester selftests, the reference anchors, demonstrations | real results over the full 1992-2017 span |
| rule | stays exactly as it is; verified with `--exact` so nothing undeclared may live there | grows only by manifest: extend the manifest, fetch, re-verify, re-stamp |

The fixture cache is the reference. The signed anchors in the attesters
(the reference region, the reference year 2010, the two-sided factor)
were measured on it and apply only to runs of the reference region and
year. A run on the science record for any other region or year is held
to the closure bars and the mutation evidence in its receipt, never to
the anchors.

The two trees share 142 granules (the 2010 fixtures are a subset of
the record) plus the geometry granule and the geothermal file. On this
machine those are hardlinks: identical bytes, one copy on disk, and both
manifests carry the same archive checksum for each. Nothing else is
shared. The computations glob a whole collection directory
(`<root>/<short_name>/*.nc`), which is exactly why the boundary has to
be physical: a fixture directory that also held the record would make
every gate run open 312 files where it expects 12 or 13, and would make
"the 2010 fixture" a fiction.

## The rule and what enforces it

No computation in this bundle is sanctioned against data absent from a
manifest. Four pieces make that a property of the code rather than a
sentence in a document.

1. **A manifest states what a tree holds.** Each row is a granule name,
   its byte size, and the checksum the archive publishes for it
   (SHA-512 from CMR for every PO.DAAC granule). Two files carry no
   archive checksum and say so in the row: the geometry granule, for
   which CMR publishes none, and `geothermalFlux.bin`, which is a
   tutorial distribution rather than a PO.DAAC product. Both are hashed
   locally (SHA-256, `"source": "local"`). A manifest is built either
   from a declared collection list and date span, or derived from an
   existing tree (`--from-tree`), in which case every file on disk must
   be matched to its CMR record or the tool refuses to write.

2. **The verify tool checks a tree against its manifest** and refuses
   on any miss: a row absent from disk, a size outside 1e-3 of the
   catalog size (catalog sizes are approximate; the largest deviation
   seen across 3,432 granules is 3.4e-5), a checksum mismatch, or, with
   `--exact`, any file present on disk that no row declares. It writes
   a report and, on success with `--stamp`, leaves `RECORD.json` in
   the tree: record name, manifest SHA-256, verification time, report
   SHA-256, granule count. The stamp is the tree's identity. It is
   machine-local and not committed; the manifest and the report it
   points at are.

3. **Every executor copies the stamp into its receipt** under `data`:

   ```json
   "data": {
     "data_root": "/Users/.../ECCO_V4r4_record",
     "record": {
       "record": "ecco-v4r4-science-record",
       "manifest_sha256": "d67caebf699864ea358c37813d75c503a302832bc0380ee69a89760d69f9f61f",
       "verified_utc": "2026-09-02T04:27:14.258145+00:00",
       "report_sha256": "fd7353151c4496e0b10073bfbdadf483d929918291768de24854c24ac91304d4",
       "granules": 4056
     }
   }
   ```

   A tree with no stamp is recorded as
   `"record": "unverified: no RECORD.json in this tree"`. The executor
   never invents a stamp.

4. **Every attester refuses a receipt whose `data.record` is not a
   stamp.** The same receipt passes with the stamp, fails with the
   stamp replaced by the unverified string, and fails with the `data`
   block removed. This was checked on the ocean heat content pair and
   the block is identical in all nine attesters.

So a result that reaches a signature carries, in its receipt, the
manifest hash of the tree it was computed on; the manifest is in this
repository; and the tree was checked against that manifest before the
run. Which tree fed a result is a fact in the receipt, not a memory.

## What was verified on 2026-09-01

**Science record.** First pass, nine monthly collections: 3,432 of
3,432 rows present, every size within the bar, every file hashed and
matched (3,430 SHA-512 against the CMR checksum, geometry and
geothermal SHA-256 against the local values in the manifest), zero
undeclared files. Extended the same day with the two collections the
salt budget reads (`OCEAN_3D_SALINITY_FLUX` and `FRESH_FLUX`, 624
granules, 20.97 GB): the manifest regenerated with the existing 3,432
rows unchanged, the fetch tool brought the 624 new rows in, and the
whole tree was re-verified from scratch: 4,056 of 4,056 present, all
hashed and matched, zero undeclared files. The committed report,
`science-record-verification.json`, is the extended one.

This was the first full integrity check of the record. The fetch tool
that ran the download verified each granule by size only, because its
checksum check recognized MD5 and SHA-256 and the archive publishes
SHA-512; that is fixed (the tool now checks any hash the manifest
names and logs which one), and the full hash pass above is the
integrity statement for the record as it stands. The verifier was also
shown to fail when it should: a flipped byte, a missing granule, and a
stray undeclared file each produced a refusal.

**Fixture cache.** 144 of 144 rows present, all sizes within the bar,
all 142 PO.DAAC granules SHA-512 against CMR, geometry and geothermal
SHA-256 local, zero undeclared files under `--exact`. Report:
`fixtures-2010-verification.json`.

The fixture manifest was derived from the tree rather than declared,
because the fixture cache predates manifests: the tool listed what was
on disk and CMR vouched for every file. The tree needed one repair
first. The record download had been pointed at the fixture root, so for
a few hours the fixture collections held 312 months instead of the
2010 set; the 3,314 fetched granules were moved to the record root and
the 116 shared 2010 granules hardlinked, after which the fixture tree
was manifested and verified exact. The fetch tool's default root is now
the record tree, and the fixture tree's `--exact` verification is what
keeps this from recurring unnoticed.

## Coverage

**Monthly collections, all 312 months 1992-01 through 2017-12:**
TEMP_SALINITY, DENS_STRAT_PRESS, SSH, OBP, OCEAN_VEL,
OCEAN_3D_VOLUME_FLUX, OCEAN_3D_TEMPERATURE_FLUX,
OCEAN_3D_SALINITY_FLUX, HEAT_FLUX, FRESH_FLUX, STRESS.

**Snapshot collections (TEMP_SALINITY and SSH):** the archive holds
daily snapshots (9,496 per collection). The record keeps the first day
of each month, which is what the budgets need for tendencies. The
archive has no 1992-01-01 and no 2018-01-01 snapshot, so there are 311
boundaries per collection, 1992-02-01 through 2017-12-01.

**Budget-closable windows.** A month is closable for a budget when
every monthly input of that budget is present for the month and both
snapshot inputs exist at its start and at the start of the next month
(the inputs are those the regional budget executor reads).

| budget | closable on the record | closable on the fixtures |
|---|---|---|
| heat | 1992-02 through 2017-11 (310 months) | 2010-01 through 2010-12 |
| volume | 1992-02 through 2017-11 (310 months) | 2010-01 through 2010-12 |
| salt | 1992-02 through 2017-11 (310 months) | 2010-01 through 2010-12 |

Extending the record is one manifest edit: add the short names to the
monthly list in the manifest tool, regenerate the manifest (existing
rows do not change), run the fetch tool (resumable; it skips every row
already present and matching), then verify with `--exact --stamp` and
commit the new manifest and report. That is how the two salt-budget
collections were added.

**By computation.** Every attested computation in this bundle can be
fed from the record over its full span: ocean heat content, steric
height, geostrophic balance and thermal wind, wind-stress curl, the
sea-level partition, the pointwise heat budget, the regional heat,
salt and volume budgets, section transports and the flux
decomposition. The trend-with-interval computation reads no tree
directly: it takes a monthly series out of another computation's
receipt and copies that receipt's stamp forward, so its attester
enforces the same rule one step removed.

## First result on the record

The regional heat budget over the reference region
(`southeast-atlantic-upper`) for 2005, a year no anchor was measured
on: residual per unit volume 5.931e-15 degC/s against the 1e-10 bar,
relative residual 7.03e-8 against 1e-6, all four mutations caught
(geothermal omitted 1.45e-5 relative; rim face shifted 0.050; vertical
sign flipped 0.410; vertical faces omitted 0.205), attester PASS. The
receipt is at `podaac/references/retrieval/exhibit-regional-heat-2005.json`
and its `data.record` is the science record stamp above. This is an
exhibit that the boundary works end to end, not a signed finding.

The regional salt budget over the same region and year, run after the
record was extended: residual per unit volume
1.946e-14 g per kg per s against the 1.5e-10 bar,
relative
3.86e-07 against 1e-6, 3 of 3 applicable
sabotages caught, attester PASS. Receipt:
`podaac/references/retrieval/exhibit-regional-salt-2005.json`.

The first trends on the record, each with the interval the
sanctioned trend method states for it: over the US northeast coast,
1992-01 through 2017-12, steric height rises +2.7999 mm per year,
95 percent interval [+1.5103, +4.0895] (r1 +0.893, 17.6 effective
months of 312), identical to every digit from the steric computation
and from the sea-level partition, whose total and manometric trends
over the same months are +5.2452 [+4.0623, +6.4281] and +2.4535
[+2.1701, +2.7370], with a maximum partition residual of 8.282e-04 m
against the 1.0e-3 bar. Receipts:
`podaac/references/retrieval/exhibit-steric-record.json` and
`exhibit-sea-level-record.json`; the 2010 fixture runs of both ship
beside them and carry the intervals a single year deserves.

A run on the record takes roughly ninety seconds where the same run on
the fixtures takes a few, because the loaders open every granule in a
collection directory before selecting the months they need. The result
is unaffected; selecting files by name before opening is the obvious
follow-on if record runs become routine.

## Operating the trees

All tools run with `uv run`; only the fetch tool authenticates (through
earthaccess, from the environment or `~/.netrc`, never embedded), and
the manifest and verify tools hold no credentials at all.

```
# build the record manifest from the declared collections and span
uv run tools/science_record_manifest.py \
    --out podaac/references/retrieval/science-record-manifest.json

# derive a manifest from a tree that already exists (CMR must vouch for every file)
uv run tools/science_record_manifest.py --from-tree ~/ECCO_V4r4 \
    --record ecco-v4r4-fixtures-2010 \
    --out podaac/references/retrieval/fixtures-2010-manifest.json

# fetch what the manifest declares and the tree lacks (resumable; default root is the record)
uv run tools/science_record_fetch.py \
    --manifest podaac/references/retrieval/science-record-manifest.json

# verify a tree against its manifest, hash everything, refuse undeclared files, stamp it
uv run tools/science_record_verify.py \
    --manifest podaac/references/retrieval/science-record-manifest.json \
    --data-root ~/ECCO_V4r4_record --checksum all --exact --stamp \
    --report podaac/references/retrieval/science-record-verification.json
```

Re-verify after any change to a tree, and commit the new report beside
the manifest. A receipt whose `data.record.manifest_sha256` does not
match a manifest in this repository names a tree this bundle has never
described, and should be read that way.
