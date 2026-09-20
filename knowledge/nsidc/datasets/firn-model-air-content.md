---
type: dataset
spheres: [cryosphere]
title: "The firn model air content term the ice sheet closure subtracts: GEMB and GSFC-FDM firn air content as the ITS_LIVE elevation change products distribute it"
description: "Firn air content is the depth-integrated porosity of the firn column, in metres of air, and its change is the part of a surface height change that carries no mass. The term this bundle's closure subtracts is distributed inside two ITS_LIVE elevation change files: a Greenland monthly anomaly from GEMB version 1.3.0 with a second series from GSFC-FDM version 1.2.1 beside it, over the grounded ice sheet and the peripheral glaciers from 1992 to 2023, and an Antarctic quarterly field from a GEMB run forced with 3-hourly ERA5, over the floating ice shelves only from 1992 to 2017. Neither file carries a firn error a mass budget can use: the Greenland product ships none and its paper takes the difference between the two models as the error, and the Antarctic error field is not a firn air content error in the units a budget needs."
tags: [firn, firn-air-content, fac, gemb, gsfc-fdm, its-live, nsidc-0792, height-change, mass-balance, density, greenland, antarctica, cryosphere]
generated: { by: knowledge-seeder/claude, at: 2026-09-19T05:30:00Z }
verified: { by: human:PaulMRamirez, at: 2026-09-19T06:21:43Z, role: maintainer, source: https://github.com/open-science-pillars/nasa-daac-knowledge/pull/192 }
resource: https://doi.org/10.5067/ICFVI7DKHZJV
version: "two products, each verified 2026-09-19. Greenland: ITS_LIVE Greenland Grounded Ice Sheet and Peripheral Glacier Ice Elevation Change version 1.1, doi 10.5067/ICFVI7DKHZJV, whose DOI resolves to the netCDF file on the ITS_LIVE bucket rather than to a product landing page, described by Nilsson and Gardner 2026 (doi 10.5194/essd-18-1729-2026); its firn variables are dfac_gemb from GEMB version 1.3.0 and dfac_gsfc from GSFC-FDM version 1.2.1. Antarctica: MEaSUREs ITS_LIVE Antarctic Quarterly 1920 m Ice Shelf Height Change and Basal Melt Rates, 1992 to 2017, Version 1 (NSIDC-0792), doi 10.5067/SE3XH9RXQWAM, user guide version 1.0 the initial release, described by Paolo and others 2023"
status: stable
stale_after: 2027-03-19
sources:
  - id: greenland-product
    resource: https://doi.org/10.5067/ICFVI7DKHZJV
    title: "ITS_LIVE Greenland Grounded Ice Sheet and Peripheral Glacier Ice Elevation Change, version 1.1: the file that carries dfac_gemb and dfac_gsfc; the DOI resolved on 2026-09-19 with a 302 straight to the netCDF on the ITS_LIVE bucket"
  - id: nilsson-2026
    resource: https://doi.org/10.5194/essd-18-1729-2026
    title: "Nilsson and Gardner, 2026, Elevation change of the Greenland Ice Sheet and its peripheral glaciers 1992 to 2023, Earth System Science Data 18, 1729 to 1745: the Greenland product's paper, which names the two firn models, the interpolation and the error treatment"
  - id: nilsson-2026-pdf
    resource: https://essd.copernicus.org/articles/18/1729/2026/essd-18-1729-2026.pdf
    title: "The Greenland product's paper as published by Copernicus (CC BY 4.0), read in full on 2026-09-19: the data section on the two firn densification models, the error section on the firn term, Table 3 and the discussion of the model spread"
  - id: crossref-nilsson
    resource: https://api.crossref.org/works/10.5194/essd-18-1729-2026
    title: "Crossref registry record for doi 10.5194/essd-18-1729-2026, read 2026-09-19: Nilsson and Gardner, Earth System Science Data 18, 1729 to 1745, issued 2026-03-05"
  - id: nsidc-0792-page
    resource: https://nsidc.org/data/nsidc-0792/versions/1
    title: "NSIDC product page for NSIDC-0792, MEaSUREs ITS_LIVE Antarctic Quarterly 1920 m Ice Shelf Height Change and Basal Melt Rates, 1992 to 2017, Version 1, reachable 2026-09-19"
  - id: nsidc-0792-user-guide
    resource: https://nsidc.org/sites/default/files/documents/user-guide/nsidc-0792-v001-userguide.pdf
    title: "NSIDC-0792 Version 1 user guide, read 2026-09-19: the variable table with fac, fac_err and fac_mean in metres, the 1920 m EPSG 3031 grid, the 104 quarters from 17 March 1992 to 16 December 2017, and section 2.3.1.3 on the GEMB calibration and its ERA5 forcing"
  - id: paolo-2023
    resource: https://doi.org/10.5194/tc-17-3409-2023
    title: "Paolo, Gardner, Greene, Nilsson, Schodlok, Schlegel and Fricker, 2023, Widespread slowdown in thinning rates of West Antarctic ice shelves, The Cryosphere 17, 3409 to 3433: the Antarctic product's paper, which the user guide names for the uncertainty quantification; cited on its Crossref registry record"
  - id: gsfc-fdm
    resource: https://doi.org/10.5194/tc-16-3971-2022
    title: "Medley, Neumann, Zwally, Smith and Stevens, 2022, Simulations of firn processes over the Greenland and Antarctic ice sheets 1980 to 2021, The Cryosphere 16, 3971 to 4011: the GSFC-FDM version 1.2.1 description, the definition of firn air content, the MERRA-2 forcing and the model's own uncertainty"
  - id: gemb
    resource: https://doi.org/10.5194/gmd-16-2277-2023
    title: "Gardner, Schlegel and Larour, 2023, Glacier Energy and Mass Balance (GEMB) a model of firn processes for cryosphere research, Geoscientific Model Development 16, 2277 to 2302: the model description both products cite, read in full on 2026-09-19 after the journal's site became reachable from this environment; it describes the model as of version 1.0, which is not the version either product ran"
  - id: itslive-site
    resource: https://its-live.jpl.nasa.gov/
    title: "The ITS_LIVE project site and its documentation index, read 2026-09-19: the elevation change datasets and their NSIDC links; the project distributes no standalone firn product page"
  - id: data-root
    resource: land-ice/knowledge/references/retrieval/ice-sheet-balance-root/RECORD.json
    title: "The stamped data root committed in this bundle: the firn stamp with the two granules, their hashes, the variables read, the domains, the cell sets and the uncertainty basis, and SOURCES.json with the reads and their dates"
  - id: gotcha-spread
    resource: ../gotchas/firn-air-content-spread-dominates-the-altimetric-mass-rate.md
    title: "Bundle gotcha: the spread between firn models is the dominant uncertainty of the altimetric mass rate and the term changes sign inside the record"
  - id: gotcha-height
    resource: ../gotchas/atl15-height-change-is-not-mass-change.md
    title: "Bundle gotcha: a height change becomes a mass change only after the firn air content change is removed and a density applied"
  - id: gotcha-epoch
    resource: ../gotchas/atl15-delta-h-reference-epoch.md
    title: "Bundle gotcha: a height change series is relative to a reference epoch, and each lagged rate has its own window"
  - id: atl15
    resource: ../datasets/icesat2-atl15.md
    title: "Bundle dataset concept: ICESat-2 ATL15, the height change product the closure is intended to read"
  - id: its-live
    resource: ../datasets/its-live-ice-velocity.md
    title: "Bundle dataset concept: the MEaSUREs ITS_LIVE products, the project that distributes the two elevation change files this term lives inside"
  - id: computation
    resource: land-ice/knowledge/computations/ice-sheet-balance.md
    title: "Bundle attested computation: the ice sheet mass balance closure that subtracts this term before applying a density"
---

# The firn model air content term the ice sheet closure subtracts

**Identity.** Firn air content is the depth-integrated porosity of the
firn column: the integral, from the surface to the depth at which the
density of ice is reached, of the shortfall of the local density below
the density of ice, divided by the density of ice, expressed in metres
of air.[^gsfc-fdm] A change in it is a change in the height of the
surface that carries no change in mass, which is why a mass balance
from altimetry subtracts the change in firn air content from the
measured volume change before multiplying by a
density.[^gsfc-fdm][^gotcha-height] The firn air content this bundle's
closure subtracts is not distributed as a product of its own. It
travels inside two ITS_LIVE elevation change files, one per hemisphere,
each carrying the output of a firn densification model on the same grid
as the heights it corrects.[^data-root][^itslive-site]

**The Greenland term.** The ITS_LIVE Greenland Grounded Ice Sheet and
Peripheral Glacier Ice Elevation Change product, version 1.1, doi
10.5067/ICFVI7DKHZJV, carries the firn air content anomaly as
dfac_gemb, from GEMB version 1.3.0, against the product's own reference
date of 1 January 2014, monthly on the 1920 m EPSG 3413 polar
stereographic grid, and a second anomaly dfac_gsfc from GSFC-FDM
version 1.2.1 beside it; the file's mask separates the grounded ice
sheet from the peripheral glaciers.[^greenland-product][^data-root] The
product's paper states that both firn models cover the continental ice
sheet and the peripheral glaciers, that their modelled firn air content
was interpolated in space and time from the models' native output onto
the 1920 m grid at monthly sampling through the end of 2023, that the
firn air content volume change is subtracted from the glacier volume
change to give an ice equivalent volume change, that this is multiplied
by an ice density of 917 kilograms per cubic metre, and that the
published mass change is the mean of the two models'
results.[^nilsson-2026-pdf][^nilsson-2026] The DOI resolves to the
netCDF file itself rather than to a landing page, and NSIDC carries no
product page for it, so the paper is its documentation; the record was
verified on the Crossref registry the same
day.[^greenland-product][^crossref-nilsson] The forcing of the GEMB
1.3.0 run behind dfac_gemb is stated neither in the file's attributes
nor in the paper, and this concept does not supply
one.[^data-root][^nilsson-2026-pdf]

**The Antarctic term.** NSIDC-0792, MEaSUREs ITS_LIVE Antarctic
Quarterly 1920 m Ice Shelf Height Change and Basal Melt Rates, 1992 to
2017, Version 1, doi 10.5067/SE3XH9RXQWAM, carries fac, fac_err and
fac_mean, all in metres, on the 1920 m EPSG 3031 grid, for the 104
quarters from 17 March 1992 to 16 December 2017, with fac_mean the mean
over the record.[^nsidc-0792-user-guide][^nsidc-0792-page] Its user
guide states that the GEMB snow densification parameters were
calibrated against observed density profiles, that the model was then
forced following a relaxation simulation with 3-hourly ERA5 reanalysis
data for 1979 to 2017, and that the resulting daily firn air content
and surface mass balance were converted to monthly values and linearly
interpolated onto a constant 5 km grid before use; the detailed
uncertainty treatment is deferred to the product's
paper.[^nsidc-0792-user-guide][^paolo-2023] The domain is the floating
ice shelves: the product is an ice shelf height change and basal melt
product, and its identifiers name the shelves.[^nsidc-0792-user-guide]
No GEMB field over the grounded Antarctic ice sheet is in the ITS_LIVE
distribution, which is why the closure refuses an Antarctic
run.[^data-root][^computation]

**The two firn models.** GEMB, the Glacier Energy and Mass Balance
model, is described by Gardner, Schlegel and Larour, 2023,
Geoscientific Model Development 16, 2277 to 2302; both ITS_LIVE
products cite it for the model and for the relaxation simulation their
runs follow.[^gemb][^nsidc-0792-user-guide][^nilsson-2026-pdf] It is a
column model of the surface and atmosphere energy and mass exchange and
of the firn state, with no horizontal communication between columns,
embedded in the Ice-sheet and Sea-level System Model framework and
one-way coupled with the atmosphere, so it runs offline against
whichever climate forcing a run chooses and feeds nothing back; it
offers several parameterization choices for albedo, subsurface
shortwave absorption and compaction, and it requires a spin-up of
thousands of years to initialise a deep firn column, which is why
computational efficiency is one of its stated design
goals.[^gemb] That description covers the model as of version 1.0, and
neither product ran that version: the Greenland file names GEMB 1.3.0
and the ice shelf product a later revision, so what the description
establishes here is the model's structure and the choices a run makes,
not the configuration of either run.[^gemb][^data-root][^nsidc-0792-user-guide]
The description names ERA5 as the forcing of choice when the model is
not being compared against another firn model, which is consistent with
the ice shelf product's stated 3-hourly ERA5 forcing, and it does not
establish the forcing of the Greenland run, which remains unstated in
that product's own documents.[^gemb][^nsidc-0792-user-guide][^nilsson-2026-pdf]
GSFC-FDM
version 1.2.1 is the Goddard Space Flight Center firn densification
model: simulations of the Greenland and Antarctic firn columns with the
Community Firn Model framework, forced by MERRA-2 snowfall,
precipitation and related fields, with the dry snow densification scheme
calibrated against more than 250 measured depth density
profiles.[^gsfc-fdm] Its authors report that seasonal volume changes
associated with firn air content are on average about 2.5 times larger
over Antarctica and 1.5 times larger over Greenland than those
associated with surface mass fluxes, and that over multiple years the
ice and air volume fluctuations inside the column are of comparable
magnitude; between 1 September 1996 and 1 September 2021 the mean loss
of firn air content over the Greenland ice sheet was 4.8
percent.[^gsfc-fdm]

## Uncertainty

Neither file carries a firn air content error a mass budget can use as
published, and the two products answer that differently.

The Greenland product ships no firn error field at all. Its paper
states that estimating firn air content errors is an active area of
research and outside its scope, and takes instead the difference in
firn air content change between GEMB and GSFC-FDM as the measure of
error: the firn rate error over an interval is the root mean square
error, including bias and variance, of the volume difference between
the two models divided by the time span, with the variance scaled by
the number of uncorrelated bins at a 200 km correlation length, and the
mass error is the volume change error and the firn error added in
quadrature and multiplied by the density of
ice.[^nilsson-2026-pdf][^nilsson-2026] That is a spread between two
models, not a formal error, and the paper says so while recommending
further analysis of how surface melt enters the two models, whose
forcing and physics differ, and noting large spatial differences in the
estimated firn air content rates and a temporal divergence around 2005
as melt becomes more prevalent.[^nilsson-2026-pdf] This bundle's loader
takes the same basis, the absolute difference between the two
aggregates the file carries, and records it as a model spread in the
firn stamp.[^data-root]

The Antarctic product does ship fac_err, described in the user guide as
a firn air content error in metres and referred to the product's paper
for its derivation.[^nsidc-0792-user-guide][^paolo-2023] This bundle's
loader does not use it: the stamp records that the field does not read
as a firn air content error in the units a budget needs, carrying
values of tens of metres at the median, a fill of 9999 where it has
none, and a units attribute of metres of ice per year, and the loader
substitutes the same noise floor the altimetry loaders use and puts the
field's statistics in the stamp.[^data-root]

The firn models carry uncertainties of their own, which are not the
same quantity as the spread between them. For GSFC-FDM version 1.2.1
the authors ran a hundred-member perturbation ensemble and report a
mean two-sigma uncertainty on the mean firn air content of 3.0 metres
over the Greenland ice sheet, where the mean firn air content is 15.7
metres, ranging spatially from 0.2 to 3.9 metres, and 4.7 metres over
the Antarctic ice sheet against a mean firn air content of 24.0 metres;
for the rate they found no usable relationship with the climate forcing
and adopt a single relative error of 0.134 times the absolute firn
thickness change rate.[^gsfc-fdm] GEMB's description carries no single
error figure of that kind. It names instead where the uncertainty
lives: the parameterizations of albedo, snow grain growth, surface
roughness, densification and its calibration, and thermal
conductivity, all worsened once liquid water enters the column, and
three setup decisions, the spin-up climatology, the spin-up length and
the vertical resolution of the column.[^gemb] Its own evaluation puts a
size on what those choices do to a trend. Compared against another firn
model forced with the same regional climate data, GEMB's seasonal and
interannual firn air content variations agree closely over both ice
sheets while the long-term trends do not: over Greenland GEMB shows
virtually no trend from 1979 to 2005 where the other model trends
positive, a difference the description attributes to the spin-up
climatology and calls a known major source of uncertainty in firn air
content trends, and with that trend removed from both the two series
run nearly together until 2004, after which GEMB loses about 0.5 metres
of firn air content and the other model about 1.0 metres to 2015; over
Antarctica the two are nearly identical until 2008, after which GEMB
trends slightly positive and the other slightly negative.[^gemb] The
description states that there is no objective way yet to say which
model is closer to the truth, and that the most definitive test would
be to compare firn-corrected altimetry against satellite gravimetry,
which is the comparison this bundle's closure
makes.[^gemb][^computation]

The consequence for a mass rate computed from these files is that the
firn term's uncertainty is a two-model spread rather than a measurement
error, that it is the term that sets the formal error of the altimetric
mass rate in this bundle's own receipted Greenland run, and that the
term itself changes sign inside the record; this bundle carries that as
a separate gotcha.[^gotcha-spread][^computation]

## Known issues

The ITS_LIVE distribution carries no firn air content field over the
grounded Antarctic ice sheet, so an Antarctic grounded mass balance has
no firn term from this source; the RACMO2 and MAR alternates the firn
stamp names were not read here.[^data-root] The two hemispheres differ
in every property a comparison would want held fixed: different firn
models behind the distributed field, different domains (grounded ice
and peripheral glaciers against floating ice shelves), different
sampling (monthly against quarterly), different record ends (2023
against 2017) and different reference conventions (an anomaly against
1 January 2014 against a value with a record mean beside
it).[^data-root][^nsidc-0792-user-guide][^greenland-product] A firn air
content series is an anomaly or a value against a stated reference, and
a difference taken across two reference conventions is not a firn
change; the bundle's reference epoch gotcha states the same trap for
the height side.[^gotcha-epoch][^data-root] The height change and
velocity products this term is read beside are the subject of their own
concepts and their numbers are not restated
here.[^atl15][^its-live]

[^greenland-product]: ITS_LIVE Greenland elevation change product, doi:10.5067/ICFVI7DKHZJV
[^nilsson-2026]: Nilsson and Gardner, 2026, Earth System Science Data, doi:10.5194/essd-18-1729-2026
[^nilsson-2026-pdf]: The Greenland product's paper, read in full 2026-09-19
[^crossref-nilsson]: Crossref registry record for the Greenland product's paper, read 2026-09-19
[^nsidc-0792-page]: NSIDC product page for NSIDC-0792
[^nsidc-0792-user-guide]: NSIDC-0792 Version 1 user guide, read 2026-09-19
[^paolo-2023]: Paolo and others, 2023, The Cryosphere, doi:10.5194/tc-17-3409-2023
[^gsfc-fdm]: Medley and others, 2022, The Cryosphere, doi:10.5194/tc-16-3971-2022
[^gemb]: Gardner, Schlegel and Larour, 2023, Geoscientific Model Development, doi:10.5194/gmd-16-2277-2023
[^itslive-site]: The ITS_LIVE project site, read 2026-09-19
[^data-root]: The stamped ice sheet balance data root committed in this bundle
[^gotcha-spread]: This bundle's gotcha on the firn model spread
[^gotcha-height]: This bundle's gotcha that height change is not mass change
[^gotcha-epoch]: This bundle's gotcha on the reference epoch
[^atl15]: This bundle's ATL15 dataset concept
[^its-live]: This bundle's ITS_LIVE dataset concept
[^computation]: This bundle's attested ice sheet mass balance closure
