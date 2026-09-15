---
type: dataset
spheres: [cryosphere]
title: "ICESat-2 ATL10 along-track sea ice freeboard, Version 7: total freeboard per ATL07 height segment on six beams, from a per-beam reference sea surface found in leads over 10 km sections"
description: "Along-track total freeboard (the height of the air and snow interface above the local sea surface) for every good-quality ATL07 sea ice height segment on each of the six ATLAS ground tracks, where sea ice concentration exceeds 50 percent and the track is at least 25 km from the coast, in HDF5 granules of half an orbit per hemisphere, from 14 October 2018 onward. Each beam's freeboard is the segment height minus that beam's own reference sea surface, estimated from the specular leads within a 10 km section and, since Version 7, interpolated to the segment; segment lengths vary with the 150-photon aggregate, the strong and weak beams of each pair differ in energy by about four to one, and the product carries no ice thickness."
tags: [icesat2, atlas, atl10, atl07, sea-ice, freeboard, leads, reference-surface, strong-beam, weak-beam, arctic, antarctic, nsidc, cryosphere]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T13:30:00Z }
resource: https://nsidc.org/data/atl10/versions/7
version: "Version 7 (DOI 10.5067/ATLAS/ATL10.007; the user guide's version history dates release 7.0 to 23 September 2025), CMR concept C3565574246-NSIDC_CPRD, verified 2026-09-15: 65,074 granules named ATL10-<hemisphere>_<yyyymmddhhmmss>_<rgt cycle region>_007_<rr>.h5, the collection open-ended from 2018-10-14 with a 91-day temporal resolution, and the newest granules on that day dated 2026-05-18"
sources:
  - id: atl10-page
    resource: https://nsidc.org/data/atl10/versions/7
    title: "NSIDC product page: ATLAS/ICESat-2 L3A Sea Ice Freeboard, Version 7 (overview, the version summary, coverage, the documents it links and the citation), read 2026-09-15"
  - id: atl10-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/atl10-v007-userguide.pdf
    title: "ATL10 Version 7 user guide (NSIDC): file structure and groups, naming, browse files, coverage and the sea ice concentration inputs, resolution, geolocation, the freeboard definition and estimation, quality and the version history, read in full 2026-09-15"
  - id: sea-ice-atbd
    resource: https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl07_10_20_21_atbd_v007.pdf
    title: "Kwok and others, ICESat-2 Algorithm Theoretical Basis Document for Sea Ice Products (ATL07, ATL10, ATL20, ATL21), Release 007, 15 May 2025 (DOI 10.5067/KPMXUOH7TNIY): the background on freeboard and thickness, the beam configuration and expected signal levels, the first-photon bias, the ATL10 algorithm and its control parameters, the multibeam architecture and the constraints section, read 2026-09-15"
  - id: atl07-10-known-issues
    resource: https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl07_10_known_issues_v007_0.pdf
    title: "ATL07 and ATL10 notes to users and known issues, updated 7 January 2026 for Release 007: the disabled swath freeboards, the inter-beam sea surface differences, the ice-edge sea state, the anomalous data periods, the sea ice concentration input change of 15 January 2026, the beam 3 energy, the variable segment lengths and the release 3 freeboard changes, read in full 2026-09-15"
  - id: atl10-data-dict
    resource: https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl10_data_dict_v007.pdf
    title: "ATL10 data dictionary, Version 7: every group and variable with its type, units and description, read 2026-09-15 for the freeboard, reference surface, lead, segment and orbit variables named here"
  - id: cmr-atl10
    resource: https://cmr.earthdata.nasa.gov/search/collections.json?short_name=ATL10
    title: "CMR collection record for ATL10 (provider NSIDC_CPRD, version 007, concept C3565574246-NSIDC_CPRD) and its granule list, read 2026-09-15"
  - id: kwok-2019-jgr
    resource: https://doi.org/10.1029/2019JC015486
    title: "Kwok and others, 2019, Surface Height and Sea Ice Freeboard of the Arctic Ocean From ICESat-2: Characteristics and Early Results, Journal of Geophysical Research: Oceans 124, 6942 to 6959, record and abstract verified against the Crossref registry 2026-09-15"
  - id: kwok-2019-grl
    resource: https://doi.org/10.1029/2019GL084976
    title: "Kwok and others, 2019, ICESat-2 Surface Height and Sea Ice Freeboard Assessed With ATM Lidar Acquisitions From Operation IceBridge, Geophysical Research Letters 46, 11228 to 11236, record and abstract verified against the Crossref registry 2026-09-15"
status: draft
stale_after: 2027-03-15
---

# ICESat-2 ATL10 along-track sea ice freeboard

**Identity.** ATL10 is the along-track sea ice freeboard product of
the Advanced Topographic Laser Altimeter System (ATLAS) on ICESat-2,
derived from the ATL07 sea ice height product: a freeboard for every
good-quality ATL07 height segment, computed against a reference sea
surface found in leads over 10 km sections, from 14 October 2018
through the most current processing.[^atl10-page][^atl10-user-guide]
The product consists of up to 32 HDF5 granules per day, 16 for each
hemisphere, each holding half an orbit, with the six ground tracks
spanning a 6 km across-track swath; a file is named
ATL10-[HH]_[yyyymmdd][hhmmss]_[ttttccss]_[vvv_rr].h5, where HH is 01
for the north and 02 for the south, tttt is one of the 1,387
reference ground tracks, cc the 91-day cycle, ss the region number
and rr a revision that increments when a granule is reprocessed
(NSIDC deletes the superseded granule, and the highest revision is
the one to use).[^atl10-user-guide] Coverage is the ice-covered
oceans of both hemispheres where the sea ice concentration exceeds
50 percent and the track is at least 25 km from the coast; the guide
names the concentration inputs as AMSR2 (AU_SI12) by default, SSMI
(G02202) where AMSR2 is unavailable and near-real-time SSMI data
(G10016) after that; the known issues note records that on
15 January 2026 the SSMI sea ice concentration data set used as input
was retired and ATL07 and ATL10 switched to what the note calls the
AMSR2 Near-Real-Time NOAA/NSIDC Climate Data Record of Passive
Microwave Sea Ice Concentration, Version 4 of G10016, inter-calibrated
to match SSMI, with ice-edge differences of 0.4 percent or less and a
small discontinuity in the ATL07 and ATL10 records; so the G10016 the
guide names as near-real-time SSMI data and the G10016 Version 4 the
note names as the AMSR2 record are the same data set id under two
sensors, and the note is the later
document.[^atl10-user-guide][^atl07-10-known-issues] Version 7,
released 23 September 2025, interpolates the reference surface height
to the freeboard location where neighbouring reference surfaces exist
(earlier releases used one static value per 10 km section), adds an
option to include heights computed with a lognormal distribution and
fixes the oc_depth parameter, which previously held only
zeros.[^atl10-page][^atl10-user-guide] The CMR record listed 65,074
granules on 2026-09-15, the newest dated 18 May 2026, about four
months before the read; the guide states that temporal updates are
made available a few times per year and are not reflected in its
version history, and the known issues note updated 7 January 2026
records no pause, so the lag is stated here as
observed.[^cmr-atl10][^atl10-user-guide][^atl07-10-known-issues]

**Structure.** Each granule holds an ancillary_data group, six
ground track groups gt1l through gt3r, METADATA, orbit_info and
quality_assessment.[^atl10-user-guide] Each ground track group has
three subgroups: freeboard_segment, with the freeboard height for
the beam (beam_fb_height, the ATL07 ice surface height relative to
beam_refsurf_height, in metres), its time, latitude and longitude,
the along-track distance seg_dist_x and the quality indicators
beam_fb_confidence, beam_fb_quality_flag (1 best to 5 poor, minus 1
invalid) and beam_fb_unc, the combined uncertainty from the height
segment sigma and the reference surface sigma; leads, with the open
water leads and their heights; and reference_surface_section, with
beam_refsurf_height (the weighted combination of the leads in this
beam for this section, relative to the tide-free mean sea surface),
beam_refsurf_sigma, beam_lead_n (the number of leads used) and
beam_refsurf_interp_flag.[^atl10-user-guide][^atl10-data-dict] The
ATL07 height segments that fed the freeboard are kept in
freeboard_segment/heights with height_segment_length_seg (the
along-track length of the segment), height_segment_sigma,
height_segment_confidence and height_segment_type (0 cloud covered,
then the sea ice and sea surface
types).[^atl10-user-guide][^atl10-data-dict] The orbit_info group
carries the reference ground track, the cycle and sc_orient, which
records whether the observatory flies forward (the weak beams
leading the strong beams), backward (the strong beams leading) or in
transition, so which of a pair's l and r tracks is the strong beam
depends on it.[^atl10-user-guide][^atl10-data-dict] The guide's
geolocation section for Version 7 states that points are presented
in geodetic latitude, longitude and ellipsoidal height, World
Geodetic System 1984 (EPSG 4326) and ITRF2020 (EPSG 9988); as
history, the version table records that release 6.1 of 1 May 2024
reprocessed the data from 13 November 2022 to 26 October 2023 using
ITRF2014, replacing ITRF2020, for consistency across the entire data
set.[^atl10-user-guide] The along-track resolution is not fixed:
freeboard is estimated for ATL07 segments whose length is the ground
distance over which about 150 signal photons accumulate, so segments
lengthen where the surface returns fewer photons, and the length is
stored with each segment; the early-results paper gives the strong
beam sampling as 17 m by 27 m to 17 m by 200 m.[^atl10-user-guide][^atl07-10-known-issues][^kwok-2019-jgr]

**Processing.** ATLAS transmits six beams in three pairs; the beams
of a pair differ in transmit energy, weak and strong with an energy
ratio of about 1 to 4, and are 90 m apart across track, the pairs
are about 3.3 km apart, and beams 1, 3 and 5 are the strong
beams.[^sea-ice-atbd] Total freeboard is defined as the height of
the air and snow interface above the local sea surface; for the
Arctic Ocean it is taken as a snow layer on top of the sea ice
freeboard, and for Antarctic sea ice the ATBD states that the
efficacy of that two-layer model remains to be demonstrated because
of wintertime layering and snow-ice formation from flooded
snow.[^sea-ice-atbd][^atl10-user-guide] The algorithm first finds the
leads, collections of height segments designated as sea surface in
ATL07, then uses them to estimate the reference surface height for
each 10 km section of each beam, and computes the freeboard of each
segment as its height minus that beam's reference surface, each beam
having its own; since release 3 only leads with specular returns
(surface types 2 to 5) enter the reference surface, because dark
leads under cloud gave a reference surface too high and freeboards
too low, a change that reduced coverage by about 10 to 20 percent
and raised composite means by 0 to 3 cm.[^atl10-user-guide][^sea-ice-atbd][^atl07-10-known-issues]
The multi-beam swath reference surface and its freeboards, present
in releases 1 and 2, have been switched off since release 3 because
the beams are not yet aligned relative to each other, so only
single-beam freeboards are available.[^atl07-10-known-issues][^sea-ice-atbd]
The weak beam of each pair is processed after its strong beam and
takes its coarse surface height and segment centres from it, so the
weak-beam segments are longer and oversampled; the middle strong
beam (beam 3) transmits about 80 percent of the energy of beams 1
and 5, and the gridded ATL20 product is built from the strong beams
only.[^sea-ice-atbd][^atl07-10-known-issues] The ICESat-2 mission
produces no routine sea ice thickness product; the ATBD gives the
hydrostatic conversion and states that the snow depth it needs is an
input from an external source (its own gotcha).[^sea-ice-atbd]

**Sea-ice use.** The early-results paper reports along-track height
precisions of about 2 cm and agreement of the monthly freeboard
distributions across the strong beams to 1 to 2 cm for the first
winter, and the IceBridge assessment reports total freeboard in 10 km
segments, calculated three ways, varying by 0.02 to
0.04 m against the airborne lidar.[^kwok-2019-jgr][^kwok-2019-grl]
The known issues note states that spatial means and standard
deviations of heights and freeboards are weighted by the segment
length, because the segment length varies with reflectance, and that
this weighting is applied in the gridded product.[^atl07-10-known-issues]

## Uncertainty

- **Per-segment uncertainty ships with the product**: beam_fb_unc,
  the combined uncertainty from the height segment sigma and the
  reference surface sigma, beside height_segment_sigma (the width of
  the trimmed histogram divided by the number of photons),
  beam_refsurf_sigma, beam_fb_unc_refsurf and the confidence and
  quality flags.[^atl10-data-dict] The guide states that the freeboard
  error is a function of the instrument precision, the number of
  leads used in the reference surface, the surface roughness and the
  number of signal photons, and refers to Magruder and others 2025
  for the description.[^atl10-user-guide]
- **Clouds and the first-photon bias are the instrument's
  constraints.** Coverage falls in summer after the spring
  transition; the first-photon bias of the photon-counting detectors
  is centimetre to sub-centimetre for most sea ice surfaces and large
  for intense pulses and flat surfaces, and the ATBD puts the
  correction at about 1 to 3 cm at nominal rates of about 6 photons
  per pulse on the strong beams and 1.5 on the
  weak.[^atl10-user-guide][^sea-ice-atbd]
- **Subsurface scattering is not quantified.** Multiple scattering
  within the snow or ice volume may affect the heights; it is
  mitigated by windowing the photon distributions, and a correction
  would need external knowledge of the snow.[^atl10-user-guide][^sea-ice-atbd]
- **Near the ice edge the reference surface can sit low.** Sea state
  propagating into the ice cover can put reference surfaces tens of
  centimetres below the local mean sea level, giving erroneously high
  freeboards in sporadic 10 km sections; most are removed by the
  50 percent concentration filter.[^atl07-10-known-issues]
- **Inter-beam sea surface differences are centimetre scale**,
  especially on strong beam 1, and the note asks for care in absolute
  sea surface height analyses.[^atl07-10-known-issues]
- **Anomalous periods.** The 9 to 26 July 2019 data carry a timing
  bias and are absent from ATL10 since release 5, when the pointing
  angle filter failed every such file; 23 to 31 March 2022 had a beam
  steering anomaly that cut signal strength by up to 15 percent;
  4 to 11 April 2022 and 10 May to 21 June 2024 were safe holds with
  no science data.[^atl07-10-known-issues]
- **What the product's uncertainty does not contain**: the snow depth
  and the densities that turn a freeboard into a thickness (its own
  gotcha), and the difference in precision between strong and weak
  beams (its own gotcha).

## Known issues

- [atl10-freeboard-is-not-thickness](../gotchas/atl10-freeboard-is-not-thickness.md):
  total freeboard is the air and snow interface above the sea
  surface; thickness needs a snow depth and densities from outside
  the product.
- [atl10-strong-versus-weak-beams](../gotchas/atl10-strong-versus-weak-beams.md):
  the beams of a pair differ in energy, photon rate, segment length
  and precision, and which track is strong depends on sc_orient.
- [sea-ice-nrt-versus-final](../gotchas/sea-ice-nrt-versus-final.md):
  the coverage mask rests on a near-real-time sea ice concentration
  input (G10016) that changed on 15 January 2026; that gotcha covers
  NSIDC-0081, NSIDC-0051 and NSIDC-0803 and does not name G10016, and
  the same caution about a near-real-time record joined to a final
  one applies here.
- The swath (multi-beam) freeboards are disabled, so a freeboard is
  always relative to its own beam's reference
  surface.[^atl07-10-known-issues]

**Verification.** The product page, the Version 7 user guide, the
known issues note and the data dictionary were read on 2026-09-15,
the ATBD release 007 was read the same day for its background,
instrument, ATL10 algorithm, multibeam and constraints sections, and
the CMR collection and granule records were read the same day; no
granule was opened from the drafting session, so the group and
variable names above come from the guide and the data
dictionary.[^atl10-page][^atl10-user-guide][^sea-ice-atbd][^atl07-10-known-issues][^atl10-data-dict][^cmr-atl10]
The guide's coverage section and the known issues note do not say
the same thing about the sea ice concentration input: the guide
lists AMSR2 AU_SI12 as the default, while the note dated
7 January 2026 records a switch to the AMSR2 near-real-time record
G10016 Version 4 on 15 January 2026; this concept reports
both.[^atl10-user-guide][^atl07-10-known-issues] The two Kwok and
others 2019 papers were verified against the Crossref registry
(title, authors, journal, year, volume and pages) on 2026-09-15 and
are cited on their registry abstracts; the Wiley journal pages
returned a bot check from the drafting
session.[^kwok-2019-jgr][^kwok-2019-grl]

[^atl10-page]: NSIDC product page, ATL10 Version 7
[^atl10-user-guide]: ATL10 Version 7 user guide, NSIDC
[^sea-ice-atbd]: ICESat-2 sea ice products ATBD, release 007, doi:10.5067/KPMXUOH7TNIY
[^atl07-10-known-issues]: ATL07 and ATL10 notes to users and known issues, release 007
[^atl10-data-dict]: ATL10 data dictionary, Version 7
[^cmr-atl10]: CMR collection record for ATL10
[^kwok-2019-jgr]: Kwok and others, 2019, Journal of Geophysical Research: Oceans, doi:10.1029/2019JC015486
[^kwok-2019-grl]: Kwok and others, 2019, Geophysical Research Letters, doi:10.1029/2019GL084976
