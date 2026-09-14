---
type: dataset-gotcha
spheres: [atmosphere, hydrosphere]
title: "MERRA-2 is four production streams joined at 1992, 2001 and 2011, with reprocessed months carrying their own prefix, and an observing system whose entries leave documented steps: a long series is not one homogeneous record"
description: "MERRA-2 was run as four streams (MERRA2_100 from 1980, MERRA2_200 from 1992, MERRA2_300 from 2001, MERRA2_400 from 2011), each spun up for one unreleased year from MERRA, and the stream number is only in the file name; high-latitude land moisture and ice-sheet snow mass carry discontinuities at the joins that take years to recover. September 2020 and June to September 2021 were reprocessed and carry MERRA2_401. The assimilated instruments enter on documented dates (SSM/I 1987, ATOVS 1998, AIRS 2002, GPS radio occultation and MLS 2004, IASI 2008, ATMS 2011, CrIS 2012), and the evaluation records the imprints that the global budget constraints did not remove. A trend or a change-point fit across these dates reads the production history as climate."
tags: [merra-2, merra2, streams, discontinuity, observing-system, reprocessing, trend, homogeneity, gesdisc]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:30:00Z }
severity: medium
# medium: the streams, the reprocessed periods and the observing
# system dates are documented product history, and they bite through
# a long-series analysis that ignores them rather than through a
# single-file read; no eval case is required at this severity.
dataset: ../datasets/merra-2.md
status: draft
stale_after: 2027-03-14
sources:
  - id: filespec
    resource: https://gmao.gsfc.nasa.gov/media/publications/zbly36ziNFDFbmYmvhQeVqPhUo/Bosilovich785.pdf
    title: "Bosilovich, Lucchesi and Suarez, 2016, MERRA-2: File Specification, GMAO Office Note No. 9 (version 1.1), read 2026-09-14: the runid convention MERRA2_SVv, the four streams with their unreleased spin-up year, the version digits for reprocessing, and the first file of each stream"
  - id: cmr-merra2
    resource: https://cmr.earthdata.nasa.gov/search/granules.json?collection_concept_id=C1276812863-GES_DISC&temporal=1992-01-01T00:00:00Z,1992-01-01T23:59:59Z
    title: "CMR granule search on M2T1NXSLV (C1276812863-GES_DISC), read 2026-09-14 at the stream boundaries and the reprocessed periods: MERRA2_100 on 1991-12-31 and MERRA2_200 on 1992-01-01, MERRA2_200 on 2000-12-31 and MERRA2_300 on 2001-01-01, MERRA2_300 on 2010-12-31 and MERRA2_400 on 2011-01-01, MERRA2_401 on 2020-09-15 and 2021-07-15, MERRA2_400 on 2026-07-01"
  - id: reproc
    resource: https://docserver.gesdisc.eosdis.nasa.gov/public/project/MERRA/Records_MERRA-2_Data_Reprocessing_and_Service_Changes.pdf
    title: "GES DISC, Records of MERRA-2 Data Reprocessing and Service Changes, read 2026-09-14: all collections for September 2020 reprocessed for an AIRS data issue (archived 2021-11-05) and for June through September 2021 for a warm bias in near-surface temperatures (archived 2021-12-17), both with the MERRA2_401 prefix; the April 2019 monthly 3D collections; the observing-system alert of June 2025 among the service notices"
  - id: gelaro-2017
    resource: https://doi.org/10.1175/JCLI-D-16-0758.1
    title: "Gelaro and others, 2017, The Modern-Era Retrospective Analysis for Research and Applications, Version 2 (MERRA-2), Journal of Climate 30, 5419 to 5454 (record and abstract read on the Crossref registry 2026-09-14: production began in June 2014 in four processing streams and converged to a single near-real-time stream in mid 2015; reduction, not removal, of spurious trends and jumps related to observing-system changes; the journal page sits behind a bot check)"
  - id: bosilovich-2015
    resource: https://gmao.gsfc.nasa.gov/pubs/docs/Bosilovich803.pdf
    title: "Bosilovich and others, 2015, MERRA-2: Initial Evaluation of the Climate, NASA TM-2015-104606 volume 43, read 2026-09-14: the land surface spin-up section (discontinuities over high latitudes, with the flux and temperature bounds), the glaciated-surface section (snow mass discontinuities at stream transitions), the global constraints on the dry-mass and moisture increments, the AIRS-related step in land water vapour increments, the MLS temperature discontinuity, the Southern Ocean increment steps and the abrupt zonal wind changes"
  - id: mccarty-2016
    resource: https://gmao.gsfc.nasa.gov/pubs/docs/McCarty885.pdf
    title: "McCarty and others, 2016, MERRA-2 Input Observations: Summary and Assessment, NASA TM-2016-104606 volume 46, read 2026-09-14: Table 1, the observation types with the dates they are used"
  - id: dataset
    resource: ../datasets/merra-2.md
    title: "This bundle's MERRA-2 dataset concept, which names the streams and the observing-system epochs in its uncertainty section and lists this trap among the known issues"
---

# MERRA-2 stream boundaries and discontinuities

**Mechanism.** MERRA-2 was produced in four streams, each of the
first three covering about a third of the period and the fourth
running on toward real time; production began in June 2014 and the
streams converged to a single near-real-time stream in mid
2015.[^filespec][^gelaro-2017] Each stream was initialised from
MERRA and run through one year of spin-up that is not released, so
the files of stream 1 (runid MERRA2_100) begin on 1980-01-01, stream
2 (MERRA2_200) on 1992-01-01, stream 3 (MERRA2_300) on 2001-01-01 and
stream 4 (MERRA2_400) on 2011-01-01; the stream digit lives in the
file name and in the granule id, and nowhere in the data
arrays.[^filespec][^cmr-merra2] The version digits of the runid mark
reprocessing: all collections for September 2020 (an issue with AIRS
data that month) and for June through September 2021 (a warm bias in
the near-surface temperatures and related quantities) were rerun and
archived as MERRA2_401, replacing the original granules, as were the
monthly three-dimensional collections for April
2019.[^filespec][^reproc][^cmr-merra2] The land restarts for each
stream came from an offline land spin-up forced with the corrected
precipitation without the high-latitude tapering the coupled system
applies, so over high-latitude land the land moisture starts each
stream lower than the stream before it ended, and the ice-sheet
surface, whose 15 to 23 metre column the interannual temperature
wave does not reach within the spin-up, carries discontinuities in
integrated quantities such as snow mass at the stream
transitions.[^bosilovich-2015] The observing system changes on
documented dates: SSM/I radiances from 9 July 1987 to 4 November 2009,
the ATOVS microwave sounders from 1 November 1998, AIRS and the EOS
AMSU-A from 1 September 2002, GPS radio occultation from 15 July 2004,
MLS temperature from 13 August 2004, IASI from 17 September 2008, ATMS
from 16 November 2011 and CrIS from 7 April 2012, among
others.[^mccarty-2016] MERRA-2 applies global constraints on the
dry-mass and moisture analysis increments to damp the abrupt jumps
such changes produced in MERRA, and the evaluation finds the total
column water far more stable than MERRA's; it also records what
remains: the land water vapour increment and land precipitation step
up in 2003 with the arrival of AIRS, the high-altitude temperatures
change character when MLS assimilation begins in August 2004, the
Southern Ocean moisture increment steps from minus 19 to 39 mm per
year between 1989 and 1992 and from about 40 to 56 mm per year between
the mid 1990s and 2000 to 2002, and the zonal wind changes abruptly at
72 S and 400 hPa in 1997 and at the equator and 150 hPa in
2000.[^bosilovich-2015][^gelaro-2017]

**Wrong-result mode.** A series read across 1992, 2001 or 2011 looks
continuous because the daily files run without a gap and the stream
digit is only in the name. A trend or a change-point fit on
high-latitude soil moisture, runoff or ice-sheet snow mass then
finds steps at the stream joins that are the restart, not the
climate; the evaluation bounds the near-surface consequences during
the overlap years at about 0.5 K in 2 m air temperature, 10 W per
square metre (about a tenth) in daily maximum latent heat flux, 5 W
per square metre (about a quarter) in daily maximum sensible heat
flux and 1 to 2 mm per day (more than half) in peak summer runoff
over high-latitude land, as upper limits, with two to three years for
the soil wetness to recover.[^bosilovich-2015] A trend in land
precipitation or in the land moisture increment across 2002 to 2003,
in stratopause temperatures across 2004, or in Southern Ocean
evaporation and precipitation across the early 1990s and 2000
inherits an observing-system step that the constraints reduced but
did not remove.[^bosilovich-2015][^gelaro-2017] A near-surface
temperature series for the summer of 2021 or for September 2020 read
from files fetched before the reprocessing carries the corrected
bias; a mixed set of MERRA2_400 and MERRA2_401 files for the same
month is two products.[^reproc]

**Correct approach.** The runid is read from each file name, and any
series that spans 1992, 2001 or 2011 states that it crosses a stream
boundary; a trend on high-latitude land states, ice-sheet snow mass
or any quantity with a long memory is fit within a stream or with the
join tested as a step, and a change-point found at a stream boundary
is attributed to the production history first.[^filespec][^bosilovich-2015]
A long-series statement on water vapour, precipitation, the
increments or the middle atmosphere names the observing-system epochs
it spans, with the entry dates from the input-observations
memorandum, and the evaluation's documented imprints are the prior
for any step found near them.[^mccarty-2016][^bosilovich-2015]
For September 2020 and June through September 2021 the granules used
are the MERRA2_401 ones the catalog now serves.[^reproc][^cmr-merra2]

**Verification.** The runid convention and the first file of each
stream are in the file specification; on 2026-09-14 the CMR granule
search on M2T1NXSLV returned MERRA2_100 for 1991-12-31 and MERRA2_200
for 1992-01-01, MERRA2_200 for 2000-12-31 and MERRA2_300 for
2001-01-01, MERRA2_300 for 2010-12-31 and MERRA2_400 for 2011-01-01,
MERRA2_401 for 2020-09-15 and 2021-07-15, and MERRA2_400 for
2026-07-01.[^filespec][^cmr-merra2] The initial-evaluation memorandum
gives the spin-up years as 1979, 1991, 2000 and 2010 (one figure
caption in it names the product start years as 1980, 1991, 2000 and
2010, which the file specification and the catalog contradict; the
file names are the authority).[^bosilovich-2015][^filespec] The
reprocessed periods and their prefix are the GES DISC record;
the observing-system dates are Table 1 of the input-observations
memorandum; the overview paper's registry record was verified on
Crossref on 2026-09-14 and its abstract read there, the journal page
sitting behind a bot check.[^reproc][^mccarty-2016][^gelaro-2017]
The dataset concept lists this trap.[^dataset]

[^filespec]: Bosilovich, Lucchesi and Suarez, 2016, MERRA-2: File Specification, GMAO Office Note 9, version 1.1
[^cmr-merra2]: CMR granule search on M2T1NXSLV at the stream boundaries, read 2026-09-14
[^reproc]: GES DISC, Records of MERRA-2 Data Reprocessing and Service Changes
[^gelaro-2017]: Gelaro and others, 2017, Journal of Climate, doi:10.1175/JCLI-D-16-0758.1
[^bosilovich-2015]: Bosilovich and others, 2015, MERRA-2: Initial Evaluation of the Climate, NASA TM-2015-104606 volume 43
[^mccarty-2016]: McCarty and others, 2016, MERRA-2 Input Observations, NASA TM-2016-104606 volume 46
[^dataset]: This bundle's MERRA-2 dataset concept
