---
type: dataset-gotcha
spheres: [biosphere]
title: "A GEDI footprint is a sample, not a pixel: the L4A footprints are 25 m spots 60 m apart along eight tracks 600 m apart, and a mean of the footprints in an area is a sample mean of a model output, not the area's biomass density"
description: "GEDI is a sampling mission. Each L4A value stands for one laser footprint about 25 m across, the footprints sit about 60 m apart along track on eight beam transects about 600 m apart, the swath is about 4.2 km wide, and the tracks fall where the station's orbit, the instrument's pointing, cloud and the mission's outages put them, so the sampled fraction of any area is small and uneven. The L4B product exists because an area mean has to be inferred from that sample: it treats each ground track as a cluster, needs at least two tracks in a cell before it estimates anything, and carries a standard error built from the model covariance and the sampling design. A rasterized or gap-filled surface of footprint values, an area mean taken as the plain average of the footprints in it, or a stock taken as that average times the area, is presented as a map or an estimate of the area when it is a sample statistic of a modeled quantity with no design behind it, and nothing in the files raises an error."
tags: [gedi, footprint, sampling, pixel, area-mean, hybrid-inference, biomass, ornldaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-15T14:02:24Z }
severity: high
# high: the wrong result is silent (a footprint average or a rasterized
# surface computes without complaint and looks like a map), it
# misstates the quantity itself (a stock or an area density) rather
# than its uncertainty, and the correct route (L4B, or a hybrid
# estimate with the tracks as clusters) is a different product or a
# different computation; the eval case exercises the trap.
dataset: ../datasets/gedi-l4a-footprint-biomass.md
eval_case: gedi-footprint-is-not-a-pixel
status: draft
stale_after: 2027-03-15
sources:
  - id: ornl-l4a-v3-guide
    resource: https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V3.html
    title: "ORNL DAAC user guide, GEDI L4A Version 3 (documentation revision 2026-09-02): the instrument geometry (three lasers, eight beam transects, footprints of about 25 m every 60 m along track, transects 600 m apart, a swath of about 4.2 km), the statement that GEDI is a sampling mission whose data will not intersect most field plot locations during the mission, the model_data group carrying the parameter covariance that the L4B algorithm needs, and the flags recommended for gridding"
  - id: ornl-l4b-v2-guide
    resource: https://daac.ornl.gov/GEDI/guides/GEDI_L4B_Gridded_Biomass.html
    title: "ORNL DAAC user guide, GEDI L4B Version 2 (documentation revision 2022-04-26): the L4B mean inferred from the sample present within each 1 km cell; uncertainty due to GEDI's sampling of the cell as opposed to wall-to-wall observation; the cluster sample with a ground track as a cluster; the two-cluster requirement for a variance; the zero cells and the non-response pattern; the NC and NS layers; the whole-cell meaning of the mean; and the mission's variance estimator using sample theory as national forest inventories do"
  - id: cmr-l4b-v21
    resource: https://cmr.earthdata.nasa.gov/search/concepts/C2792577683-ORNL_CLOUD.umm_json
    title: "CMR collection record for GEDI L4B Version 2.1: the abstract's statement that L4B uses the sample present within the borders of each 1 km cell to statistically infer mean AGBD and that uncertainty is due to sampling and to the modeled L4A values"
  - id: crossref-patterson-2019
    resource: https://api.crossref.org/works/10.1088/1748-9326/ab18df
    title: "Crossref registry record for Patterson and others 2019, Environmental Research Letters 14, 065007: the abstract on hybrid inference incorporating both the sampling design and the model parameter covariance, the cluster (footprint track) sample, and sampling error as the larger variance component in the study areas"
  - id: dataset
    resource: ../datasets/gedi-l4a-footprint-biomass.md
    title: "This bundle's GEDI L4A dataset concept, which lists this trap among the known issues"
  - id: l4b-dataset
    resource: ../datasets/gedi-l4b-gridded-biomass.md
    title: "This bundle's GEDI L4B dataset concept, the product that performs the area inference"
---

# A GEDI footprint is a sample, not a pixel

**Mechanism.** The GEDI instrument's three lasers produce eight beam
ground transects that sample footprints about 25 m in diameter spaced
about 60 m along track, with the transects about 600 m apart across
track for a swath about 4.2 km wide, and GEDI is a sampling mission:
because most field plots are small, the guide notes, GEDI data will
not intersect most of them during the mission
life.[^ornl-l4a-v3-guide] Every L4A value is therefore one footprint,
a modeled biomass density for one 25 m spot, and the spot centres
along a transect are 60 m apart, more than twice the 25 m diameter,
while the transects are 600 m apart, many times the spot size;
between and beside them the surface is unobserved.[^ornl-l4a-v3-guide] Where the
tracks fall is not the analyst's choice: the L4B guide records that
cells go without an estimate more often early in the mission, closer
to the equator where the station's overpass pattern is sparser, under
cloud, and along the reference tracks the second-year orbital
resonance left unsampled.[^ornl-l4b-v2-guide] The Level 4B product is
the mission's answer to the question of area: it uses the sample
present within the borders of each 1 km cell to statistically infer
the cell's mean, by hybrid inference in which the ground tracks are
the clusters of a cluster sample and the variance carries both the
L4A model parameter covariance and the sampling design; at least two
clusters are required before a variance exists, so a cell crossed by
one track holds no estimate, and the uncertainty is stated as due
both to GEDI's sampling of the cell, as opposed to wall-to-wall
observation, and to the modeled L4A
values.[^ornl-l4b-v2-guide][^cmr-l4b-v21][^crossref-patterson-2019]
The L4A files carry the model parameters and their covariance in the
model_data group for exactly that computation.[^ornl-l4a-v3-guide]

**Wrong-result mode.** The footprint file reads like a point dataset,
and every step below runs without error. Footprints rasterized to a
25 m or 30 m grid, with the gaps interpolated or filled by nearest
neighbour, become a continuous biomass map whose values between the
tracks were never observed and whose apparent resolution is the grid
cell, not the footprint spacing. A polygon's biomass density taken as
the plain mean of the footprints inside it is a sample mean of a
clustered, unevenly placed sample: a polygon crossed by one track has
no variance under the mission's estimator at all, a polygon with only
two tracks has a variance of the kind the estimator's simulations,
at six United States sites, under-stated by about 20 percent, and a
polygon whose tracks are concentrated on one side is represented by
that side.[^ornl-l4b-v2-guide][^crossref-patterson-2019]
A stock taken as that mean times the polygon area inherits the same
sampling error plus the model error and carries no standard error
unless one is built, while the L4B product would report a standard
error for every cell it estimates and zero for the cells it
cannot.[^ornl-l4b-v2-guide] A footprint value compared with a pixel
of a wall-to-wall map, or a footprint count used as a weight, treats
the footprint as an areal unit when it is a 25 m sample of one; and a
1 km cell mean recomputed from the L4A footprints without the cluster
structure differs from the L4B value for the same cell, without the
L4B standard error, for cells where L4B holds a value, and produces a
number where L4B holds zero because a single track cannot support an
estimate.[^ornl-l4b-v2-guide]

**Correct approach.** An area mean of GEDI biomass is an inference
from a sample with a design, and the product family assigns the
roles: L4A is the footprint sample, with its per-footprint model
standard error, and L4B is the 1 km inference, with the cell mean, its
standard error, the number of tracks (NC) and footprints (NS) behind
it, and the mode of inference that says whether an estimate exists at
all.[^ornl-l4b-v2-guide][^l4b-dataset] For an area that is not a 1 km
cell, the same hybrid estimator applies with the tracks as clusters
and the L4A model_data covariance as the model component, and the
result is stated with the sample it rests on; a footprint mean is a
sample mean, reported as such with the number of tracks and
footprints, and a surface between the tracks is a model of its own
(the mission's end-of-mission plan is a second-level model to
wall-to-wall imagery, recorded in the mode of inference layer as a
different mode).[^ornl-l4b-v2-guide][^crossref-patterson-2019][^ornl-l4a-v3-guide]
The gridding flags in L4A (degrade_include_flag and
elev_highestreturn_outlier_flag) exist because the quality gate for a
sample feeding an area estimate is stricter than for a single
footprint.[^ornl-l4a-v3-guide]

**Verification.** The instrument geometry is in the L4A guide's
summary and methods, and the sampling statements are in the L4B
guide's overview, application and methods sections and in the L4B CMR
abstract.[^ornl-l4a-v3-guide][^ornl-l4b-v2-guide][^cmr-l4b-v21] The
L4B NC and NS layers show, for any cell, how many tracks and
footprints its mean rests on, and the MI layer shows where no
estimate exists; on any L4A granule the along-track spacing of
consecutive shots in a beam and the across-track separation of the
beams are readable from lat_lowestmode and lon_lowestmode. No GEDI
file was opened for this concept; the statements rest on the
documentation and registry records read on 2026-09-15. The dataset
concepts list this trap among the known issues.[^dataset][^l4b-dataset]

[^ornl-l4a-v3-guide]: ORNL DAAC user guide, GEDI L4A Version 3, revision 2026-09-02, read 2026-09-15
[^ornl-l4b-v2-guide]: ORNL DAAC user guide, GEDI L4B Version 2, revision 2022-04-26, read 2026-09-15
[^cmr-l4b-v21]: CMR collection C2792577683-ORNL_CLOUD, read 2026-09-15
[^crossref-patterson-2019]: Crossref record for doi:10.1088/1748-9326/ab18df, read 2026-09-15
[^dataset]: This bundle's GEDI L4A dataset concept
[^l4b-dataset]: This bundle's GEDI L4B dataset concept
