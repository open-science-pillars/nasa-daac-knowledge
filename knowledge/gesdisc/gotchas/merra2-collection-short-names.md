---
type: dataset-gotcha
spheres: [atmosphere, hydrosphere]
title: "A MERRA-2 short name encodes time treatment, frequency, vertical structure and variable group, and the same variable name lives in several collections: a search by variable alone lands on the wrong one"
description: "M2T1NXSLV, M2I1NXASM, M2TMNXSLV, M2IMNXASM, M2SDNXSLV and M2TUNXSLV all carry a 2 m air temperature, and M2T1NXFLX, M2T1NXINT, M2T1NXLND and M2T1NXLFO all carry a precipitation, but they are hourly averages, hourly snapshots, monthly means of each, daily statistics and monthly diurnal means, on grid-box or land-only terms. The nine-character short name says which (M2, then I or T or C or S for instantaneous, time-averaged, constant or statistics, a frequency character, N, a vertical letter and a three-letter group), and a catalog or keyword search that stops at the variable name returns several collections whose values differ in meaning while agreeing in name, units and shape."
tags: [merra-2, merra2, short-name, esdt, collections, cmr, search, gesdisc]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:30:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-14T12:12:43Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/144 }
severity: medium
# medium: the naming rule is documented in the file specification and
# every collection title spells the treatment out, and the trap bites
# through a search or a join that ignores the name rather than through
# a single collection's values; no eval case is required at this severity.
dataset: ../datasets/merra-2.md
status: stable
stale_after: 2027-03-14
sources:
  - id: filespec
    resource: https://gmao.gsfc.nasa.gov/media/publications/zbly36ziNFDFbmYmvhQeVqPhUo/Bosilovich785.pdf
    title: "Bosilovich, Lucchesi and Suarez, 2016, MERRA-2: File Specification, GMAO Office Note No. 9 (version 1.1), read 2026-09-14: section 5 on the collection name freq_dims_group_HV and the ESDT short name M2TFHVGGG with every letter's meaning, the note that fields may appear in more than one collection, and the variable tables of the single-level collections"
  - id: cmr-merra2
    resource: https://cmr.earthdata.nasa.gov/search/collections.json?short_name=M2T1NXSLV&provider=GES_DISC
    title: "CMR collection search by short name, read 2026-09-14 for eighteen MERRA-2 short names: each returns exactly one GES_DISC collection whose title spells the treatment out (for example MERRA-2 tavg1_2d_slv_Nx: 2d, 1-Hourly, Time-Averaged, Single-Level, Assimilation, Single-Level Diagnostics against MERRA-2 inst1_2d_asm_Nx: 2d, 1-Hourly, Instantaneous, ...)"
  - id: readme
    resource: https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T1NXSLV.5.12.4/doc/MERRA2.README.pdf
    title: "GES DISC README Document for MERRA-2 Data Products (revised 2021-03-01), read 2026-09-14: the collection tables, in which T2M appears in the instantaneous, the time-averaged, the daily-statistics and the monthly single-level collections, and precipitation in the flux, the vertically integrated, the land and the land forcing collections"
  - id: gmao-citing
    resource: https://gmao.gsfc.nasa.gov/gmao-products/merra-2/citing-merra-2-data_merra-2/
    title: "GMAO, Citing MERRA-2 Data, read 2026-09-14: the hourly, monthly and monthly-diurnal DOI tables, one DOI per collection, which show the pairs (M2T1NXSLV and M2TMNXSLV, M2I1NXASM and M2IMNXASM, M2SDNXSLV and M2SMNXSLV) side by side"
  - id: gmao-faq
    resource: https://gmao.gsfc.nasa.gov/gmao-products/merra-2/faq_merra-2/
    title: "GMAO MERRA-2 FAQ, read 2026-09-14: the difference between the FLX and LND collections (grid-box average against land-only), between the RAD and LFO downward shortwave (all surfaces against land only), and between the ANA and ASM collections"
  - id: dataset
    resource: ../datasets/merra-2.md
    title: "This bundle's MERRA-2 dataset concept, which states the naming rule in its structure and lists this trap among the known issues"
---

# MERRA-2 collection short names

**Mechanism.** MERRA-2 organises its output into file collections
of fields with common characteristics, and fields may appear in more
than one collection. The collection name reads freq_dims_group_HV
(tavg1_2d_slv_Nx), and the nine-character short name a catalog
indexes compresses it as M2TFHVGGG: T is the time description (I
instantaneous, T time-averaged, C time-independent, S statistics), F
the frequency (1 hourly, 3 three-hourly, 6 six-hourly, M monthly
mean, D daily statistics, U monthly-diurnal mean, 0 not applicable),
H is N for the native horizontal resolution, V the vertical location
(X two-dimensional, P pressure levels, V model layer centres, E model
edges) and GGG the group (SLV single-level diagnostics, ASM
assimilated state, FLX surface fluxes, INT vertical integrals, LND
land, LFO land forcing, RAD radiation, and so on).[^filespec] A
monthly (M) or diurnal (U) collection is a monthly mean of either
instantaneous or time-averaged parents, and which one is in the T
letter: M2TMNXSLV averages the hourly averages of M2T1NXSLV,
M2IMNXASM the hourly snapshots of M2I1NXASM.[^filespec] Every CMR
collection title spells the treatment out in words, and each
collection has its own DOI.[^cmr-merra2][^gmao-citing] The same
variable name recurs across the families: a 2 m air temperature sits
in the instantaneous, the time-averaged, the daily-statistics and the
monthly single-level collections; a precipitation sits in the flux
collection (grid-box average, as PRECTOT and PRECTOTCORR), the
vertically integrated collection, the land collection (per unit land
area, as PRECTOTLAND) and the land forcing collection; a downward
shortwave sits in RAD over all surfaces and in LFO over land
only.[^readme][^gmao-faq]

**Wrong-result mode.** A search that starts from the variable name
("T2M", "PRECTOT", "SWGDN") returns several collections whose arrays
share the name, the units and the 576 by 361 shape, and the first hit
is as likely to be the hourly snapshot as the hourly average, the
monthly mean of snapshots as the monthly mean of averages, or the
land-only field as the grid-box one. A series that steps from one to
another at a collection boundary mixes an instantaneous and an
averaged quantity; a comparison of M2IMNXASM and M2TMNXSLV
temperatures treats two differently formed monthly means as one
product; a daily maximum taken as the largest hourly average from
M2T1NXSLV is at most, and in general below, the daily maximum the
statistics collection M2SDNXSLV records from the model time step; a land flux from LND used
as a grid-box flux over-states it along coasts and is undefined over
the ocean; a variable read from the analysis collections (ANA) is not
the assimilated state (ASM) the documentation
describes.[^filespec][^readme][^gmao-faq] The join in the time-stamp
gotcha is the same mistake seen from the time axis.

**Correct approach.** A collection is chosen by decoding its short
name against the specification's letter table, with the CMR title as
the plain-language check, and every statement names the collection
(the short name or the collection name, with its DOI) beside the
variable, so that "T2M from M2I1NXASM" and "T2M from M2T1NXSLV" are
never the same series; a search goes to the catalog by short name,
which returns one collection, rather than by keyword, which returns
the family.[^filespec][^cmr-merra2][^gmao-citing] Grid-box budgets
take the FLX, RAD and INT collections and land budgets the LND and
LFO collections, per the FAQ's rule.[^gmao-faq]

**Verification.** The letter table and the note that fields recur
across collections are section 5 of the file specification; the
README's collection tables show the recurrence variable by variable;
the DOI tables show the paired collections; on 2026-09-14 a CMR
search by short name returned exactly one GES_DISC collection for
each of the eighteen short names tried, with the treatment spelled
out in its title.[^filespec][^readme][^gmao-citing][^cmr-merra2] The
dataset concept states the rule and lists this trap.[^dataset]

[^filespec]: Bosilovich, Lucchesi and Suarez, 2016, MERRA-2: File Specification, GMAO Office Note 9, version 1.1
[^cmr-merra2]: CMR collection search by short name, read 2026-09-14
[^readme]: GES DISC README Document for MERRA-2 Data Products, revised 2021-03-01
[^gmao-citing]: GMAO, Citing MERRA-2 Data: the per-collection DOI tables
[^gmao-faq]: GMAO MERRA-2 FAQ
[^dataset]: This bundle's MERRA-2 dataset concept
