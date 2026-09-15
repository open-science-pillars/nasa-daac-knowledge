---
type: dataset-gotcha
spheres: [biosphere]
title: "Every shot the L4A algorithm could run on carries a biomass prediction, flagged rather than removed: l2a_quality_flag_rel3 and l4a_quality_flag_rel3 gate which footprints are fit for a prediction, elev_highestreturn_outlier_flag gates which are fit for gridding, and degrade_include_flag names the degrade codes the L4B algorithm admits"
description: "The L4A file holds an AGBD value for every shot on which the algorithm ran (l2_algrunflag), including water, urban and leaf-off shots, waveforms too noisy to penetrate the canopy, shots with degraded pointing or positioning, and track segments where fog or cloud put the highest return in the wrong place. Version 3 gates them with named flags: l2a_quality_flag_rel3 for waveform fidelity, using beam sensitivity thresholds of 0.98 over tropical evergreen forest, 0.95 over other land and 0.5 over water; l4a_quality_flag_rel3 for shots that the applied models represent (land, urban proportion below 50, a prediction stratum, leaf-on unless the model uses RH98 alone, RH100 below 150 m); degrade_include_flag for the degrade codes accepted into the L4B sample; and elev_highestreturn_outlier_flag for outlier segments. A mean, a map or a fusion that takes every shot in the file is built on a sample that the product itself does not consider fit; the L4B cells are built only on high-quality waveforms, and the shipped L4B Version 2.1 grid predates the Version 3 flag names."
tags: [gedi, quality-flag, degrade-flag, sensitivity, filtering, l4a, gridding, ornldaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T14:02:24Z }
severity: medium
# medium: the flags are documented in the guide's own frequently asked
# questions with their definitions, the effect of skipping them is a
# biased sample rather than a wrong quantity, and the L4B product
# applies them upstream; no eval case is required.
dataset: ../datasets/gedi-l4a-footprint-biomass.md
status: draft
stale_after: 2027-03-15
sources:
  - id: ornl-l4a-v3-guide
    resource: https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V3.html
    title: "ORNL DAAC user guide, GEDI L4A Version 3 (documentation revision 2026-09-02): the variable table entries for l2_algrunflag, l2a_quality_flag_rel3, l4a_quality_flag_rel3, degrade_flag, degrade_include_flag, elev_highestreturn_outlier_flag, predictor_limit_flag, response_limit_flag, sensitivity and selected_algorithm; the frequently asked question on which quality metrics and flags to use, with the beam sensitivity thresholds; the definitions of l4a_quality_flag_rel3 and degrade_include_flag; and the revisions table naming the flags new in Version 3"
  - id: cmr-l4a-v3
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C4212593885-ORNL_CLOUD.umm_json
    title: "CMR collection record for GEDI L4A Version 3: the abstract's statement that quality flags are reported with the AGBD estimates for each beam"
  - id: ornl-l4b-v2-guide
    resource: https://daac.ornl.gov/GEDI/guides/GEDI_L4B_Gridded_Biomass.html
    title: "ORNL DAAC user guide, GEDI L4B Version 2 (documentation revision 2022-04-26): the L4B mean inferred from high-quality waveforms, the NC and NS layers counting high-quality waveforms, and the note that L4B coverage may differ from L4A owing to footprint quality checks"
  - id: dataset
    resource: ../datasets/gedi-l4a-footprint-biomass.md
    title: "This bundle's GEDI L4A dataset concept, which lists this trap among the known issues"
  - id: l4b-dataset
    resource: ../datasets/gedi-l4b-gridded-biomass.md
    title: "This bundle's GEDI L4B dataset concept: the Version 2.1 grid's publication date and the L4A version it rests on"
---

# The quality and degrade flags gate every footprint

**Mechanism.** AGBD is predicted for every shot where it is possible
to run the L4A algorithm, as l2_algrunflag records, and the product
provides multiple quality flags and metrics for subsetting the
predictions to the observations useful for a given application; the
file itself removes nothing.[^ornl-l4a-v3-guide][^cmr-l4a-v3] Two
flags gate the prediction. l2a_quality_flag_rel3 encapsulates a
number of L2A quality metrics to identify land surface shots with
waveforms of high fidelity for AGBD estimation; l4a_quality_flag_rel3
identifies shots that may be considered samples of the population the
applied models represent, and its definition, in the guide's own spelling, is
l2a_quality_flag == 1 (with a pointer to the Level 2 Version 3 user
guide), urban_proportion below 50, is_land_rel3 == 1, a prediction
stratum assigned, leaf_off_flag not 1 unless the model's only
predictor is RH98, and RH100 below 150 m; the guide's example is that the
deciduous forest models were calibrated only on waveforms simulated
from leaf-on airborne lidar, so they apply only to leaf-on
acquisitions.[^ornl-l4a-v3-guide] Both flags use a beam sensitivity
threshold, the maximum canopy cover the waveform's signal-to-noise
ratio can penetrate, of 0.98 over tropical evergreen forests, 0.95
over all other land and 0.5 over water, the thresholds the Level 2,
4B and 4C products use, and the guide notes that a local study may
choose another threshold to trade quality against
quantity.[^ornl-l4a-v3-guide] Two more flags gate gridding and
fusion. degrade_flag, carried from L2A, marks a degraded state of
pointing or positioning; degrade_include_flag names the degrade codes
(attitude codes 0, 1, 2, 3, 4 and 6, trajectory codes 0, 3 and 8)
that a comparison with GEDI-to-airborne-lidar crossovers found free
of higher systematic geolocation error, the codes the Level 4B
algorithm admits into its sample, and it is meant to be used
together with elev_highestreturn_outlier_flag, which marks segments
of sub-orbit granules whose highest-return elevations are outliers
against the TanDEM-X elevation model, with low fog and cloud and
time-correlated noise below the ground among the
causes.[^ornl-l4a-v3-guide] predictor_limit_flag and
response_limit_flag mark shots whose RH metrics or whose prediction
lie outside the range of the training data, and selected_algorithm
equal to 10 marks shots where the lowest detected mode was likely
noise and a higher mode was used.[^ornl-l4a-v3-guide] The Version 3
revisions table names l4a_quality_flag_rel3, degrade_include_flag
and elev_highestreturn_outlier_flag as new in Version 3, with
l2_algrunflag, l2a_quality_flag_rel3 and selected_algorithm made
consistent across the Level 2 and Level 4 footprint products, so the
Version 2.1 files carry different flag names.[^ornl-l4a-v3-guide]
The L4B mean is inferred from high-quality waveforms only, its NC
and NS layers count high-quality waveforms, and the guide warns that
L4B coverage may differ from L4A owing to footprint quality
checks.[^ornl-l4b-v2-guide] The shipped L4B Version 2.1 grid
(published 2023-10-29) predates the Version 3 flag names, so the
names above describe what the L4B algorithm admits, not the flags the
Version 2.1 grid was built with.[^l4b-dataset]

**Wrong-result mode.** A mean, a histogram or a comparison against
field plots that takes every agbd value in a granule mixes in shots
over water and urban land, shots whose waveform never reached the
ground under dense canopy, leaf-off shots in deciduous forest for
which no model was calibrated, and shots with a prediction stratum of
none; nothing is missing, so nothing warns. A gridded or fused
product built with the two prediction flags but without
degrade_include_flag and elev_highestreturn_outlier_flag places
footprints with degraded geolocation, and whole track segments under
fog, into the wrong cells, which is why the guide says the shot-level
flags are insufficient for gridding.[^ornl-l4a-v3-guide] A filter
written for Version 2.1 flag names applied to Version 3 files, or the
reverse, fails on the missing dataset in most readers, and where the
reader defaults a missing flag it selects nothing or
everything.[^ornl-l4a-v3-guide] A beam sensitivity
threshold below the product's, chosen for quantity, admits waveforms
the product excludes over tropical evergreen forest, where the
threshold is highest.[^ornl-l4a-v3-guide]

**Correct approach.** The product's own gate for a prediction is
l2a_quality_flag_rel3 and l4a_quality_flag_rel3 both set; the gate
for a sample that feeds a grid or a fusion adds degrade_include_flag
and elev_highestreturn_outlier_flag, degrade_include_flag naming the
degrade codes the L4B algorithm admits; the L4B Version 2.1 grid that
ships was built before these Version 3 names
existed.[^ornl-l4a-v3-guide][^ornl-l4b-v2-guide][^l4b-dataset]
predictor_limit_flag and response_limit_flag identify the
out-of-range shots that the guide says deserve care, and a sensitivity
threshold other than the product's is an analysis choice stated with
its value.[^ornl-l4a-v3-guide] The flags are per version: the
Version 3 names above do not exist in the Version 2.1
files.[^ornl-l4a-v3-guide]

**Verification.** The flag definitions and thresholds are in the
Version 3 guide's variable table and frequently asked questions, and
the revisions table dates the new flags.[^ornl-l4a-v3-guide] On any
Version 3 granule the check is a count: the number of shots with
l2_algrunflag set exceeds the number with both quality flags set,
which exceeds the number that also pass the two gridding flags. No
GEDI file was opened for this concept; the statements rest on the
documentation read on 2026-09-15. The dataset concept lists this trap
among the known issues.[^dataset]

[^ornl-l4a-v3-guide]: ORNL DAAC user guide, GEDI L4A Version 3, revision 2026-09-02, read 2026-09-15
[^cmr-l4a-v3]: CMR collection C4212593885-ORNL_CLOUD, read 2026-09-15
[^ornl-l4b-v2-guide]: ORNL DAAC user guide, GEDI L4B Version 2, revision 2022-04-26, read 2026-09-15
[^dataset]: This bundle's GEDI L4A dataset concept
[^l4b-dataset]: This bundle's GEDI L4B dataset concept
