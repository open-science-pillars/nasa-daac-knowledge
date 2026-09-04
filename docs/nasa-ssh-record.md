# The NASA-SSH observational record

The bundle's second confrontation pair puts the attested ECCO regional
sea level against JPL's NASA-SSH gridded altimetry over the same box.
It differs from the first pair in one way that matters: the RAPID
array's transports were never among the estimate's constraints, while
the along-track sea surface height NASA-SSH is built from was. This
document records exactly which release is on the machine, where it
came from, how it was verified, what the files say when read live,
and the terms under which it is used. Nothing here is a comparison;
the comparison, its scores and the statement of how independent the
record is live in the computation concept and the finding that cites
it.

## Identity

| | |
|---|---|
| dataset | NASA-SSH Simple Gridded Sea Surface Height from Standardized Reference Missions Only Version 1.1 (the `title` attribute of every file) |
| release | V1.1 (read from the global attribute `product_version` of every file in the tree, not from a web page; the manifest normalises the case) |
| DOI | 10.5067/NSREF-SG0V11 (read from the files' `id` attribute; the same string on the PO.DAAC collection record) |
| collection | NASA_SSH_REF_SIMPLE_GRID_V11, CMR concept C4155232533-POCLOUD, PO.DAAC |
| along-track source | DOI 10.5067/NSREF-AT0V1 (the files' `references` attribute), the reference-mission along-track anomalies each grid is built from |
| created | the files carry `date_created` 2026-03-25; the archive's granule revision dates are 2026-04-27 |
| licence | Creative Commons Attribution 4.0, https://creativecommons.org/licenses/by/4.0/ (the files' `license` attribute) |
| citation | Willis, J. K., S. Fournier, K. Marlis, E. Killett and J. Sanchez (2026), NASA-SSH: JPL Sea Surface Height Anomalies, Version 1.1, PO.DAAC, doi:10.5067/NSREF-SG0V11 |
| acknowledgement in the files | "This data is provided by NASAs PO.DAAC." |
| documentation | NASA-SSH V1.1 User Guide, https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/nasa-ssh/NASA-SSH_V1_1_UserGuide.pdf |
| mean sea surface | DTU21 (the `mean_sea_surface` attribute) |
| gridding | "pyresample resample_gauss with roi=600000.0, sigma=175000.0, neighbours=500, respecting basin boundaries" (the `gridding_method` attribute): a Gaussian-weighted average with a 175 km scale over passes up to 600 km away, kept inside the basin of the cell |

## Distribution, and how the tree was taken

The collection is served by the NASA Earthdata archive behind
Earthdata Login. The tree was taken with `tools/obs_record_fetch.py`:
it enumerates the collection's granules through CMR for the requested
range, fetches each through an authenticated earthaccess session
(credentials from the machine's netrc, used for retrieval only),
and verifies every file against the checksum the archive publishes
for it. For this collection CMR carries no inline checksum; the
archive publishes an MD5 sidecar (`<granule>.nc.md5`) beside every
file, which the tool fetches and checks. Every one of the 1315 files
matched. The tool writes `SOURCE.json` into the tree: the collection
identity, the query, and for every file its granule concept id,
archive revision date, URL, archive checksum and algorithm, archive
size, size on disk, and whether the checksum verified. A rerun skips
files already present that still verify, so a partial fetch resumes
rather than restarting.

Retrieval completed 2026-09-03 05:35 UTC (the evening of 2026-09-02
local, which the tree's directory name carries). The archive's files
are identified by their checksums; if the archive ever replaces a
granule, a later retrieval hashes differently and becomes a new
record beside this one, never an overwrite.

## The tree and its manifest

| | |
|---|---|
| root | `~/NASA_SSH/podaac-2026-09-02` |
| record name | `nasa-ssh-ref-simple-grid-v1.1` |
| contents | 1315 grids, `NASA-SSH_alt_ref_simple_grid_v1_1_19921026.nc` through `..._20180101.nc`, one every seven days, 1,483,856,623 bytes |
| fetch record | `SOURCE.json` in the tree (above) |
| manifest | `knowledge/podaac/references/retrieval/nasa-ssh-manifest.json` (SHA-256 per file, identity read from the netCDF attributes of every file, the fetch record carried in); SHA-256 of the manifest `578b8f29b8cd7aff69be3eea74fa330f32e0bad4635e38b6e37d0b97f3e3e449` |
| verification report | `knowledge/podaac/references/retrieval/nasa-ssh-verification.json`: declared 1315, present 1315, checksum ok 1315, undeclared 0, stamped 2026-09-03T05:37:50Z |
| tools | `tools/obs_record_fetch.py` (fetch and archive-checksum verification), `tools/obs_record_manifest.py` (`build --version V1.1 --doi 10.5067/NSREF-SG0V11`, `verify --stamp`) |
| stamp | `RECORD.json` in the tree: record name, manifest SHA-256, verification time, report SHA-256, file count; machine-local, not committed |

`build` was told to expect V1.1 and the DOI and would have refused if
any file said otherwise; all 1315 agree. The manifest tool reads the
identity from `product_version` and `id` for this producer (RAPID
writes `version` and `DOI`), and the change was checked against the
RAPID tree: its manifest rebuilds to the same record, identity, file
list and byte count, and its stamped tree still verifies.

A computation that reads this tree copies `RECORD.json` into its
receipt beside the ECCO stamp, so the comparison receipt names both
trees by manifest hash. The comparison also digests the tree itself
(the SHA-256 of the lines `NAME SHA256` for every grid, sorted, newline
terminated), and its attester re-hashes every grid against that digest
when the tree is on disk.

## What the delivered files say, checked live

Every statement below was read from the files on disk, not from
documentation, and the documentation was then checked against it.

**Grid.** `latitude` 360 values from -89.75 to 89.75 and `longitude`
720 values from 0.25 to 359.75 (degrees east, 0 to 360, which the
comparison converts before selecting a box), half-degree cell centres.
`ssha` is float64 in metres on (latitude, longitude), standard name
`sea_surface_height_above_sea_level`, comment "Sea level determined
from satellite altitude - range - all altimetric corrections", fill
value the largest double; `counts` is the number of along-track values
weighted into each cell; `basin_flag` and `basin_names_table` carry
the basin mask the gridding respects. CF-1.9.

**Time.** `time` is a scalar, `seconds since 1990-01-01`, proleptic
Gregorian, the centre of the grid's window; the global attributes
`time_coverage_start` and `time_coverage_end` give the ten-day window
(for the grid dated 1992-11-02, 1992-10-28 through 1992-11-07). The
filename date is the centre date. Grids are seven days apart with no
break in cadence from 1992-10-26 to 2018-01-01.

**Coverage.** A typical grid holds values in about 146,000 of the
259,200 cells (the ocean between the reference missions' turning
latitudes of about 66 degrees, less the cells no pass reached in the
window). Eight grids hold no values anywhere: those dated 1995-12-04,
2001-12-10, 2003-11-24, 2005-09-26, 2006-11-06, 2006-11-13,
2013-04-01 and 2013-09-09. They are complete, well-formed files whose
windows fell in reference-mission outages; the archive delivers them
and the manifest keeps them, and a computation that averages grids
by month must decide how to treat the months they thin. In the box
the comparison uses (35 to 45 degrees north, 75 to 65 degrees west)
every other grid holds 323 or 324 of its 324 cells, except one that holds 311.

**Convention.** The User Guide states, and the attributes agree, that
the anomaly is relative to the DTU21 mean sea surface and that the
dynamic atmospheric correction has been applied, which removes the
inverse-barometer response to atmospheric pressure. ECCO's `SSH`
variable is the inverse-barometer corrected one, so the two share a
convention; the estimate's `SSHIBC` and `SSHNOIBC` variants do not,
and the comparison refuses a partition receipt that is not in the
`SSH` variant.

## The overlap with the ECCO record

The ECCO v4r4 monthly record runs 1992-01 through 2017-12. The first
grid, dated 1992-10-26, is alone in its month; from 1992-11 on every
month through 2017-12 has four or five grids except the four months
thinned by the empty grids (1995-12, 2003-11 and 2005-09 with three,
2006-11 with two). The largest consecutive overlap is therefore
1992-11 through 2017-12, 302 months, provided a month is allowed to
enter on two grids. The reference comparison binds the overlap to
1993-01 through 2017-12 (300 months, complete calendar years so the
trend method's climatology is taken over whole cycles) and the
minimum grids per month to two.

## Uncertainty the record publishes

The User Guide publishes no uncertainty for the gridded fields. For
the along-track source it states that the orbit error reduction
lowers the RMS variability at crossovers by a variance of about 2.3
cm, and that a pass is removed when its crossover mean exceeds 0.1 m
or its crossover RMS exceeds 0.27 m. The comparison's receipt carries
those statements verbatim under `observation.published_uncertainty`,
together with the published order of a regional altimetry trend
uncertainty (Prandi et al. 2021, Scientific Data 8, 1,
doi:10.1038/s41597-020-00786-7: an average local trend uncertainty
of 0.83 mm/yr, range 0.78 to 1.22, at the 90 percent level over
1993-2019, for a different gridded multi-mission product), cited as
the order such a trend is held to and never as this product's own
figure.

## Independence

The estimate was fitted to along-track sea surface height from the
same reference missions this product regrids. The record is therefore
not independent of the estimate in the way the RAPID array is, and
the comparison says so in its receipt in the words the attester
requires. What it can and cannot show is stated there and in the
dataset concept; the un-fitted sea level record for the box is the
coastal tide gauge network, a different quantity (relative sea level,
inverse-barometer uncorrected, with vertical land motion) and a
different computation.

## Terms

Creative Commons Attribution 4.0: use with attribution. The citation
above is the attribution the product asks for; the bundle carries it
in the dataset concept, the comparison receipt and here. The data
tree stays outside the repository; the manifest and verification
report are committed so that anyone with Earthdata credentials can
retrieve the same 1315 files and verify them to the same hashes.
