# The RAPID 26N observational record

The bundle's first confrontation pair puts the attested ECCO overturning
at 26.5N against the RAPID array's observed overturning over their
overlap. Everything attested before this shows ECCO agreeing with
itself; this is the independent observation, with its own DOI, version,
and terms. This document records exactly which release is on the
machine, where it came from, how it was verified, what it holds over
the overlap, and the terms under which it is used. Nothing here is a
comparison; no score is computed until the confrontation executor
exists and its attester recomputes it.

## Identity

| | |
|---|---|
| dataset | Atlantic meridional overturning circulation observed by the RAPID-MOCHA-WBTS (RAPID-Meridional Overturning Circulation and Heatflux Array-Western Boundary Time Series) array at 26N from 2004 to 2024 |
| release | v2024.1a (read from the global attribute `version` of every netCDF file in the tree, not from a web page) |
| DOI | 10.5285/48d0bf43-0598-ceb2-e063-7086abc062f1 (read from the files' `DOI` attribute; the same string on the BODC record and in DataCite) |
| publisher | NERC EDS British Oceanographic Data Centre NOC; record published 2026-01-27 |
| collected | 2004-04-01 to 2024-03-27 (DataCite `Collected` date; the delivered series runs 2004-04-02 00:00 to 2024-03-27 00:00) |
| licence | UK Open Government Licence v3, https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/ (the BODC record's `licence` field; DataCite rights identifier "uk open government licence") |
| citation | Moat B.I.; Smeed D.; Rayner D.; Johns W.E.; Smith R.H.; Volkov D.L.; Elipot S.; Petit T.; Kajtar J.B.; Baringer M.O.; Collins J. (2026). Atlantic meridional overturning circulation observed by the RAPID-MOCHA-WBTS (RAPID-Meridional Overturning Circulation and Heatflux Array-Western Boundary Time Series) array at 26N from 2004 to 2024 (v2024.1a). NERC EDS British Oceanographic Data Centre NOC. doi:10.5285/48d0bf43-0598-ceb2-e063-7086abc062f1 |
| acknowledgement the programme asks for | "Data from the RAPID AMOC observing project is funded by the Natural Environment Research Council, U.S. National Science Foundation (NSF) with support from NOAA. They are freely available from https://rapid.ac.uk/" (the `Acknowledgement` attribute of moc_transports.nc; the README's wording differs slightly and names www.rapid.ac.uk) |
| method papers the README cites | McCarthy et al. 2015, Prog. Oceanogr. 130, 91-111, doi:10.1016/j.pocean.2014.10.006; Cunningham et al. 2007, Science 317, 935-938; Kanzow et al. 2007, Science 317, 938-941 |
| supersedes | v2024.1, v2023.1a, v2023.1, v2022.1, v2020.2, v2020.1, v2018.2, v2018.1, v2017.1, v2015.1, v2014.1 (the BODC record's `replaces` list, each with its own DOI) |

One internal inconsistency in the delivered files, recorded rather than
resolved: `meridional_transports.nc` writes the version as `v2024-1a`
and its embedded citation carries the year 2025, while the two
transport files, the README (dated 29 January 2026), and the BODC
record say `v2024.1a` and 2026. The manifest tool normalises the hyphen
and refuses if the files disagree on the release; they do not.

## Two distributions, and which one is on the machine

The DOI landing page at BODC offers the release as one package (a zip
of 1,075,185,645 bytes, prepared on request). On 2026-09-02 it was
requested sixteen times; every transfer was closed by the server
somewhere between 1 MB and 678 MB in, and the server ignores byte
ranges, so no complete copy could be taken. A 1 GB control download
from another host completed in 58 seconds, so the fault is at the
source. The truncated fragments were deleted.

The RAPID programme's own site serves the same files directly and
anonymously (https://rapid.ac.uk/sites/default/files/rapid_data/),
with byte ranges honoured and no registration. That is where this
tree came from. Two facts about that distribution decide how the
tree is handled:

- **The files are refreshed in place.** The server's Last-Modified for
  `moc_transports.nc` and `moc_vertical.nc` was the retrieval day
  (02 Sep 2026 08:22 GMT), while their `Creation_date` attribute says
  22-Jan-2026. Whether any byte changed between January and September
  cannot be known from here. So the tree is hashed at retrieval, the
  manifest vouches for those bytes, and a later retrieval that hashes
  differently is a new record beside this one, never an overwrite.
- **The release identifies itself inside the files.** Version and DOI
  are global attributes, so the manifest reads the identity from the
  data rather than from the page that served it, and refuses to build
  if the files disagree or if the identity it was told to expect is
  not what the files say.

Retrieval was by curl (User-Agent `osp-obs-capture/0.1.0`) with no
credentials and no form. The BODC package, if it ever completes, would
be verified against the same file hashes: identical bytes are identical
evidence whichever server delivered them.

## The tree and its manifest

| | |
|---|---|
| root | `~/RAPID_26N/rapid.ac.uk-2026-09-02` |
| record name | `rapid-26n-v2024.1a` |
| fetch record | `SOURCE.json` in the tree: every URL, the server's Last-Modified and Content-Length per file, the retrieval time, and the note on the DOI package |
| manifest | `podaac/references/retrieval/rapid-26n-manifest.json` (SHA-256 per file, identity read from the netCDF attributes, the fetch record carried in) |
| verification report | `podaac/references/retrieval/rapid-26n-verification.json` |
| tool | `tools/obs_record_manifest.py` (`build`, `verify --stamp`) |
| stamp | `RECORD.json` in the tree: record name, manifest SHA-256, verification time, report SHA-256; machine-local, not committed |

| file | bytes | SHA-256 (first 16) | server Last-Modified |
|---|---|---|---|
| `moc_transports.nc` | 1,182,284 | `ba135d9447a87c2b` | 02 Sep 2026 08:22:08 GMT |
| `moc_vertical.nc` | 35,983,608 | `1e77f263bcf2523e` | 02 Sep 2026 08:22:11 GMT |
| `meridional_transports.nc` | 9,666,320 | `e2df75b5c443bcdd` | 22 Jul 2026 08:41:19 GMT |
| `moc_transports.mat` | 1,012,687 | `abe91ceda0375902` | 29 Jan 2026 11:02:16 GMT |
| `README.pdf` | 369,816 | `f7edfc8ce056d750` | 22 Jul 2026 08:40:51 GMT |
| `README_ERROR.pdf` | 129,212 | `706c160849abb01a` | 22 Jul 2026 08:40:51 GMT |

Not taken: `ts_gridded.nc` (485 MB, the merged temperature and salinity
profiles) and `2d_gridded.nc` (1.7 GB, sections at 10-day resolution).
The overturning confrontation reads none of them. Either can be added
later by extending the tree and rebuilding the manifest; the record
then gets a new name and stamp.

The verifier was shown to refuse what it must: one byte changed in
`moc_transports.nc` fails the checksum check; an undeclared file in
the tree fails the exact check; asking `build` to expect v2023.1a
against these files is refused with what the files actually say. On
the clean tree: 6 of 6 present, 6 of 6 hashed and matched, zero
undeclared, stamped 2026-09-02T15:13:27Z.

The stamp works exactly as the science record's does. A sanctioned
computation that reads this tree copies `RECORD.json` into its receipt
beside the ECCO stamp, so a confrontation receipt names both trees by
manifest hash, and an attester refuses a receipt that names neither.

## What the delivered files say, checked live

Every statement below was read from the files on disk, not from
documentation, and the documentation was then checked against it.

**`moc_transports.nc`**, the overturning time series. One dimension,
`time`, 14,599 samples, `days since 2004-4-1 00:00:00`, every step
exactly 0.5 day (twelve-hourly), first sample 2004-04-02 00:00, last
2024-03-27 00:00. Nine variables in Sv, all with fill value -99999:
`moc_mar_hc10` (overturning transport), `t_gs10` (Florida Straits),
`t_ek10` (Ekman), `t_umo10` (upper mid-ocean), and the layer transports
`t_therm10` (0 to 800 m), `t_aiw10` (800 to 1100 m), `t_ud10` (1100 to
3000 m), `t_ld10` (3000 to 5000 m), `t_bw10` (below 5000 m). The `10`
names the 10-day low-pass filter the README describes. Exactly 20
samples of `moc_mar_hc10` are absent: the first ten (2004-04-02 00:00
through 2004-04-06 12:00) and the last ten (2024-03-22 12:00 through
2024-03-27 00:00), which is the README's statement that the first and
last five days are set to absent because the filter is spurious there,
confirmed to the sample. Over the delivered record the overturning has
mean 16.98 Sv, standard deviation 4.40 Sv, range -4.35 to 32.34 Sv; the
mean is quoted only as a sanity check against the published order of
17 Sv, and the negative values are the December 2009 and January 2010
episode the README documents.

**`meridional_transports.nc`**, the 10-day product added in 2025: 730
samples, `days since 1950-01-01`, every step 10 days, 2004-04-06 to
2024-03-22; `amoc_depth` (maximum of the streamfunction in depth
coordinates), `amoc_sigma0`, `amoc_sigma2`, `heat_trans` (PW),
`frwa_trans` (Sv), and the streamfunctions in depth, sigma0 and sigma2
coordinates. The README says the depth-space overturning here is the
same series as in the other files at 10-day resolution; that claim is
checkable and will be checked when the confrontation is built, because
which RAPID quantity is the counterpart of a model streamfunction
maximum is a colocation decision the recipe has to state.

**`moc_vertical.nc`**: the streamfunction profile in depth space,
`stream_function_mar` (depth 307 levels, time 14,599), same time axis
as the transports.

## The overlap with the ECCO record

The ECCO V4r4 science record on this machine spans 1992-01 through
2017-12 as monthly means. RAPID begins 2004-04-02. The usable overlap
is therefore **2004-04 through 2017-12, 165 calendar months**, of
which 164 carry every twelve-hourly sample valid; April 2004 carries
48 of its 58 samples because the first five days are absent. In
twelve-hourly samples the overlap holds 10,034 valid values. Whether
April 2004 enters the monthly series as a partial month or is dropped
is a colocation choice for the recipe to state, not a fact of the data.

## Uncertainty as the programme states it

`README_ERROR.pdf` reproduces the measurement uncertainty table of
McCarthy et al. 2015: RMS error 1.5 Sv on 10-day values and 0.9 Sv on
annual values for the AMOC; within that, geostrophic transports 0.9
and 0.7, temperature and salinity accuracy 0.8 and 0.6, gridding 0.4
and 0.4, the western boundary wedge 0.5 and 0.5, and the Florida
Straits 1.1 and 0.3. The README states, and the recipe must not forget,
that these errors do not reduce substantially in annual averages;
the annual (April to April) accuracies listed for 2004 through 2014
are 0.9 Sv in every year but 2005 (1.0) and 2007 (1.3). A time-varying
error bar is distributed as a Matlab file the programme offers
separately; it is not in this tree.

## Processing facts inside the overlap that a comparison must know

From the README's change log and data-gaps section, the events that
fall inside 2004-04 through 2017-12:

- the Ekman component is computed from ERA5 wind stress at 26.5N (from
  the July 2020 release on); the model's own wind forcing is a
  different product, so the Ekman parts of the two overturnings are not
  built from the same winds;
- the Florida Straits transport comes from the submarine cable, with
  the gap of 4 September to 28 October 2004 (hurricane Frances) filled
  by linear interpolation, and a correction for the secular change of
  the geomagnetic field applied from the 2024 releases on;
- mooring losses filled by substitution or climatology: WB2 absent
  7 November 2005 to 26 March 2006 (WB3 used and the wedge extended);
  eastern boundary February to June 2006 interpolated; the eastern
  mid-Atlantic-ridge mooring lost 1 November 2009 to 22 December 2010
  (climatology); the top 800 m of the western ridge mooring lost
  25 October to 22 December 2010 and again 10 October 2016 to 28
  February 2017 (climatology); EBH4 lost 1 March 2017 to 23 October
  2018 with EBH3, 21 km west, substituted (the README's own estimate:
  a seasonal-cycle effect of about 0.5 Sv, no significant effect on the
  mean);
- the upper mid-ocean transport is defined adaptively (the depth above
  which intermediate water flows north, or 800 m when none does), which
  is the Cunningham et al. 2007 maximum-overturning convention rather
  than a fixed-depth integral; and on 20 to 24 December 2009 and
  6 January 2010 there was no northward transport and the overturning
  is defined by the special rule the README gives;
- each release changes the series mean and standard deviation used in
  interpolation and quality control, so values inside the overlap can
  differ slightly between releases: comparisons cite the release, and
  a result stated against v2024.1a is a result against v2024.1a.

## Terms of use, and the bundle's own rule on top of them

The Open Government Licence v3 permits copying, adapting and
redistributing the data with attribution. The programme asks for the
DOI citation and the acknowledgement above in anything that uses the
data. The bundle adds its own rule, the same one it keeps for captured
observations: the data tree stays outside the repository; the
repository holds the manifest (hashes) and the verification report,
not the data; a confrontation receipt carries the file digests, the
tree's stamp, the release version and the DOI; and where a receipt
must carry derived values (the monthly overlap series, so an attester
can recompute a score) it carries the citation and the acknowledgement
beside them. Nothing from the array is quoted anywhere without the
release it came from.

## What the dataset concept said before this

`podaac/datasets/rapid-mocha.md` was verified on 2026-07-04 with the
MOCHA heat-transport DOI (10.17604/3nfq-va20) as its resource and the
note that the AMOC series downloads from rapid.ac.uk. It carried no
DOI, version, or licence for the AMOC series itself. That concept now
points here for the overturning release; its resource and the heat
transport product are unchanged.
