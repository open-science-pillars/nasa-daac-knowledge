---
type: dataset-gotcha
spheres: [cryosphere]
title: "The strong and weak beams of each ATLAS pair differ four to one in energy, and so in photon rate, segment length and precision: which of gtXl and gtXr is strong depends on sc_orient, and a freeboard statistic names its beams"
description: "ATLAS transmits three beam pairs; within a pair the strong beam carries about four times the energy of the weak one, returns about 6 signal photons per pulse over snow-covered ice against about 1.5, and is read by 16 detector channels against 4. The weak beam's 150-photon segments are therefore longer, its coarse surface is taken from the adjacent strong beam, and the middle strong beam transmits about 80 percent of the outer two. Whether the strong beam of a pair is the l or the r ground track depends on the spacecraft orientation recorded in sc_orient. The gridded ATL20 product uses the strong beams only, and a statistic that pools all six beams as equals, or picks a track by name assuming it is strong, mixes two precisions and two samplings."
tags: [icesat2, atlas, atl10, atl07, atl20, strong-beam, weak-beam, sc_orient, beam-pair, photon-rate, segment-length, sea-ice, freeboard]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T13:30:00Z }
severity: medium
# medium: the beam configuration, the orientation flag and the strong
# beam choice of the gridded product are documented in the ATBD, the
# data dictionary and the known issues note, and the error is a
# mixed-precision statistic rather than a silently wrong number from
# the product alone; no eval case is required.
dataset: ../datasets/icesat2-atl10-freeboard.md
status: draft
stale_after: 2027-03-15
sources:
  - id: sea-ice-atbd
    resource: https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl07_10_20_21_atbd_v007.pdf
    title: "Kwok and others, ICESat-2 ATBD for Sea Ice Products, Release 007, 15 May 2025 (DOI 10.5067/KPMXUOH7TNIY): the beam configuration with its 1 to 4 energy ratio and separations, the expected signal levels table, the 16 and 4 detector channels and the first-photon bias, the weak beam slaved to the strong beam in coarse surface finding, the beam gains with beam 3 at 0.82, the multibeam implementation notes and the ATL20 beam list, read 2026-09-15"
  - id: atl10-data-dict
    resource: https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl10_data_dict_v007.pdf
    title: "ATL10 data dictionary, Version 7: sc_orient (0 backward, 1 forward, 2 transition) defined by whether the weak beams lead the strong beams, and height_segment_length_seg, read 2026-09-15"
  - id: atl07-10-known-issues
    resource: https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl07_10_known_issues_v007_0.pdf
    title: "ATL07 and ATL10 notes to users and known issues, release 007: note 2 on the lower transmitted energy of beam 3 (strong beam 2R or 2L depending on orientation), note 3 on variable segment lengths and length-weighted statistics, issue 2 on inter-beam sea surface differences especially on strong beam 1, and the coverage gaps once acute in the weak beams, read in full 2026-09-15"
  - id: atl10-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/atl10-v007-userguide.pdf
    title: "ATL10 Version 7 user guide: the six ground track groups gt1l to gt3r, the sc_orient parameter in orbit_info, and the version 4 history entry aligning weak beam meteorological data with the strong beam, read in full 2026-09-15"
  - id: kwok-2019-jgr
    resource: https://doi.org/10.1029/2019JC015486
    title: "Kwok and others, 2019, Surface Height and Sea Ice Freeboard of the Arctic Ocean From ICESat-2: Characteristics and Early Results, Journal of Geophysical Research: Oceans 124, 6942 to 6959: the abstract's three pairs with a strong and weak beam each, the strong beam sampling of 17 m by 27 m to 17 m by 200 m, and the 1 to 2 cm agreement of monthly freeboard distributions across the strong beams, record and abstract verified against the Crossref registry 2026-09-15"
  - id: dataset
    resource: ../datasets/icesat2-atl10-freeboard.md
    title: "This bundle's ATL10 dataset concept, which lists this trap among the known issues"
---

# ATL10 strong versus weak beams

**Mechanism.** ATLAS transmits six beams as three pairs about 3.3 km
apart across track; within each pair the two beams have different
transmit energies, weak and strong with an energy ratio of about
1 to 4, are 90 m apart across track and about 2.5 km apart along
track, and beams 1, 3 and 5 are the strong beams.[^sea-ice-atbd] The
ATBD's expected signal levels for snow-covered winter ice are on the
order of 6 signal photons per pulse from a strong beam and 1.5 from a
weak one, six times lower over dark leads, and the receiver has 16
detector channels for the strong beams against 4 for the weak, so
that the first-photon bias correction, about 1 to 3 cm at those
nominal rates, is a beam-dependent correction.[^sea-ice-atbd] A
height segment is the ground distance over which about 150 signal
photons accumulate, so the weak beam's segments are longer than the
strong beam's; the multibeam architecture processes the strong beams
first and takes the centre location and initial coarse surface height
of each weak-beam segment from the adjacent strong beam, the weak
beam being slaved to the strong beam's fine-tracker output, with the
consequence that the weak-beam segments are oversampled.[^sea-ice-atbd][^atl07-10-known-issues]
The strong beams are not identical either: beam 3, the middle strong
beam, transmits about 80 percent of the energy of beams 1 and 5 (the
ATBD's relative beam gains are 1.0, 1.0, 0.82, 1.0, 1.0 and 1.0), so
its segment lengths and photon statistics differ from the other two,
while its smaller incidence angle raises its photon rate for the
same surface; and the known issues note records centimetre-scale
inter-beam differences in the reference sea surface heights,
especially on strong beam 1.[^atl07-10-known-issues][^sea-ice-atbd]
The file names the tracks gt1l to gt3r, not strong and weak: the
data dictionary defines sc_orient as forward (1) when the weak beams
lead the strong beams, backward (0) when the strong beams lead, and
transition (2), and the known issues note names beam 3 as strong beam
2R or 2L depending on the orientation of the observatory, so the
mapping from track name to beam strength changes with the
orientation.[^atl10-data-dict][^atl07-10-known-issues][^atl10-user-guide]
The gridded ATL20 product is derived from beams 1, 3 and 5, the
strong beams, and ATL21 from beam 3 alone.[^sea-ice-atbd] The
early-results paper reports the sampling of the strong beams as 17 m
by 27 m to 17 m by 200 m and the agreement of monthly freeboard
distributions across the strong beams as 1 to 2 cm; it states
neither figure for the weak beams.[^kwok-2019-jgr]

**Wrong-result mode.** A statistic that pools the six ground tracks
as six equal samples mixes segments of two lengths, two photon
counts and two first-photon corrections, and gives the longer,
noisier weak-beam segments equal weight with the strong ones, while
a statistic that weights by segment count rather than segment length
is biased by the same variable sampling the note describes.[^sea-ice-atbd][^atl07-10-known-issues]
A track selected by name, gt1l or gt2r, on the assumption that it is
the strong beam is the weak beam whenever the observatory flies in
the other orientation, and a time series built from one named track changes beam
strength at each yaw flip.[^atl10-data-dict][^atl07-10-known-issues]
A comparison of a weak beam's freeboard distribution with a strong
beam's, or of beam 3 with beams 1 and 5, reads the energy and
detector differences as a difference in the ice; and a comparison of
along-track ATL10 freeboards with the gridded ATL20, which used the
strong beams only, is a comparison of different beam
sets.[^sea-ice-atbd][^atl07-10-known-issues] A coverage analysis
near the coast in the early releases would have read the weak beams'
saturation gaps in the land and sea ice mask overlap, acute in the
weak beams at high sun, as an absence of ice.[^atl07-10-known-issues]

**Correct approach.** A freeboard statistic names the beams it used,
resolved from sc_orient in orbit_info rather than from the track
letter, weights segments by height_segment_length_seg, and treats
the strong and weak beams as two populations, with the strong beams
as the population the gridded product and the early-results
agreement figures describe; a comparison with ATL20 uses the strong
beams.[^atl10-data-dict][^atl07-10-known-issues][^sea-ice-atbd][^kwok-2019-jgr]
A statement about beam 3 or about strong beam 1 carries the note's
caveats on energy and on the reference surface
differences.[^atl07-10-known-issues]

**Verification.** The ATBD's photon counting section gives the
energy ratio and the separations, its instrument table gives the
expected photon rates, its first-photon bias section gives the
channel counts and the 1 to 3 cm correction, its coarse surface
finding notes and multibeam implementation notes give the slaving of
the weak beam and the oversampling, its surface classification table
gives the beam gains and its ATL20 control table gives the strong
beam list; the data dictionary gives sc_orient; the known issues note
gives notes 2 and 3 and issue 2; the guide gives the group names; all
read on 2026-09-15.[^sea-ice-atbd][^atl10-data-dict][^atl07-10-known-issues][^atl10-user-guide]
Kwok and others 2019 is cited on its Crossref record and abstract
(verified 2026-09-15); the journal page returned a bot check from the
drafting session.[^kwok-2019-jgr] No granule was opened. The dataset
concept lists this trap among the product's known
issues.[^dataset]

[^sea-ice-atbd]: ICESat-2 sea ice products ATBD, release 007, doi:10.5067/KPMXUOH7TNIY
[^atl10-data-dict]: ATL10 data dictionary, Version 7
[^atl07-10-known-issues]: ATL07 and ATL10 notes to users and known issues, release 007
[^atl10-user-guide]: ATL10 Version 7 user guide, NSIDC
[^kwok-2019-jgr]: Kwok and others, 2019, Journal of Geophysical Research: Oceans, doi:10.1029/2019JC015486
[^dataset]: This bundle's ATL10 dataset concept
