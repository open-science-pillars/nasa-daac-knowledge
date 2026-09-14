---
type: dataset-gotcha
spheres: [atmosphere, geosphere]
title: "The Daymet grid is Lambert conformal conic meters, not latitude and longitude: a cell is one square kilometer only on the standard parallels, and a lat/lon subset comes back as a projected box"
description: "Daymet x and y are meters in a Lambert conformal conic projection with standard parallels at 25 N and 60 N, and the 1 km cell is 1 km in those projected meters. A conformal projection keeps angles, not area: the scale is true on the two standard parallels and departs from it elsewhere, so the ground area of a cell is not one square kilometer across the domain, and a total computed as a cell count times one square kilometer is biased. The netCDF subset service returns the projected minimum bounding box of a lat/lon request, larger than the request and rectangular in the projection, not in degrees."
tags: [daymet, projection, lambert-conformal-conic, cell-area, coordinates, subsetting, ornldaac]
generated: { by: knowledge-seeder/claude, at: 2026-09-14T05:40:00Z }
severity: medium
# medium: the projection and its parameters are stated in the guide
# and on the project site, so the trap is documented; the error on an
# area-weighted total is under ten percent over most of the domain and
# about double at its northern edge, and a plotted field is visibly off when
# x and y are read as degrees; no eval case is required.
dataset: ../datasets/daymet-v4.md
status: draft
stale_after: 2027-03-14
sources:
  - id: ornl-v4-guide
    resource: https://daac.ornl.gov/DAYMET/guides/Daymet_Daily_V4.html
    title: "ORNL DAAC user guide, Daymet Daily V4 (documentation revision 2024-06-17): the coordinate reference system section with the projection parameters and the PROJ definition, and the 1 km by 1 km resolution"
  - id: daymet-overview
    resource: https://daymet.ornl.gov/overview
    title: "Daymet project site, description page: the projection definition section (Lambert conformal conic, WGS 84, standard parallels 25 N and 60 N, central meridian 100 W, latitude of origin 42.5 N, meters) and the 1 km resolution"
  - id: daymet-web-services
    resource: https://daymet.ornl.gov/web_services.html
    title: "Daymet project site, web services page: the note that the netCDF subset service finds the minimum bounding area of a lat/lon box in the projected system, so the output is rectangular in the projection"
  - id: thornton-2021
    resource: https://doi.org/10.1038/s41597-021-00973-0
    title: "Thornton and others, 2021, Scientific Data 8, 190: the elevation model projected to the Lambert conformal conic projection and resampled to a 1,000 m cell, and the data geolocated in that projection at 1 km by 1 km"
  - id: dataset
    resource: ../datasets/daymet-v4.md
    title: "This bundle's Daymet dataset concept, which lists this trap among the known issues"
---

# The Daymet grid is Lambert conformal conic meters

**Mechanism.** Daymet is delivered in a North America Lambert
conformal conic projection with projection units of meters, the WGS 84
spheroid, first and second standard parallels at 25 N and 60 N, a
central meridian at 100 W, a latitude of origin at 42.5 N and zero
false easting and northing; the guide gives the definition as a PROJ
string and the spatial resolution is 1 km in those
units.[^ornl-v4-guide][^daymet-overview] The elevation model behind
the grid was projected to the same system and resampled to a 1,000 m
output cell, and the data are geolocated in it at 1 km by 1
km.[^thornton-2021] A conformal conic projection with two standard
parallels has true scale on those parallels and a scale factor that
departs from one between and beyond them; that is the definition of
the projection the guide names, not a Daymet-specific statement, and
it means a 1,000 m by 1,000 m projected cell covers one square
kilometer of ground only where the scale factor is
one.[^ornl-v4-guide] Computed on 2026-09-14 with PROJ 9.5.1 from the
guide's PROJ string, along the central meridian, the areal scale factor is
1.00 at 25 N and 60 N, 0.91 at 42.5 N (a cell covers about 1.10
square kilometers of ground), 1.09 at 18 N (about 0.92), 1.20 at 70 N
(about 0.83) and 2.19 at 82.9 N, the domain's northern edge (about
0.46); these are properties of the stated projection, reproducible
from the guide's definition.[^ornl-v4-guide]

**Wrong-result mode.** A field read with x and y taken as degrees
puts every cell in the wrong place and fails to overlay with anything
in latitude and longitude. A basin, state or ecoregion total built as
the sum over cells times one square kilometer (a precipitation volume,
a snow water mass, a radiation load) equals the true total times the
areal scale factor, so it carries that factor as a bias: about 9
percent low at the latitude of origin, about 9 percent high at 18 N,
about 20 percent high at 70 N, and about 2.2 times the true total at
the northern edge, with the sign changing across the standard
parallels, so the bias differs between two regions being compared. A lat/lon
bounding box sent to the netCDF subset service returns the minimum
bounding area of that box in the projected system, square in the
projection and larger than the request, so a subset "for" a
lat/lon box contains cells outside it, and a mean over the returned
file is a mean over that larger area.[^daymet-web-services]

**Correct approach.** The projected coordinates are the geolocation,
and the guide's PROJ definition is the transform between them and
latitude and longitude.[^ornl-v4-guide][^daymet-overview] An area
total uses the true cell area from the projection's scale factor (or
a reprojection to an equal-area grid), and a regional statistic says
which cells were counted and how their areas were taken; a subset from
the netCDF subset service is clipped to the intended lat/lon extent
after retrieval when the intended extent is the analysis
unit.[^daymet-web-services]

**Verification.** The guide's coordinate reference system section and
the project site's projection definition carry the parameters and
the PROJ string.[^ornl-v4-guide][^daymet-overview] The web services
page states the minimum-bounding-area behavior of the subset
service.[^daymet-web-services] The paper records the elevation model's
projection and 1,000 m resampling.[^thornton-2021] The scale factors
above are reproducible from the PROJ string with any PROJ build. The
dataset concept lists this trap among the product's known
issues.[^dataset]

[^ornl-v4-guide]: ORNL DAAC user guide, Daymet Daily V4, revision 2024-06-17, read 2026-09-14
[^daymet-overview]: Daymet project site, description page, read 2026-09-14
[^daymet-web-services]: Daymet project site, web services page, read 2026-09-14
[^thornton-2021]: Thornton and others, 2021, Scientific Data 8, 190, doi:10.1038/s41597-021-00973-0, read at nature.com 2026-09-14
[^dataset]: This bundle's Daymet dataset concept
