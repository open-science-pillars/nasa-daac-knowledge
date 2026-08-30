---
type: convention
title: "Thermal forcing direct from PO.DAAC S3: the in-region rule"
description: "Tutorial-companion facts: reading ECCO straight from the PO.DAAC S3 bucket requires running in AWS us-west-2, avoids local copies and egress charges, and authenticates via Earthdata netrc."
tags: [ecco, tutorial-companion, cloud, access]
generated: { by: claude-code/fable-5, at: 2026-08-30T21:45:00Z }
status: draft
stale_after: 2027-01-04
sources:
  - id: tut-thermal
    resource: https://ecco-v4-python-tutorial.readthedocs.io/ECCO_v4_Calculating_the_ECCOv4_ocean_thermal_forcing.html
    title: "ECCO v4 Python Tutorial: Calculate ocean thermal forcing from ECCOv4r4 data, direct from PO.DAAC S3 storage"
    author: team:ecco-consortium
---

# Thermal forcing direct from PO.DAAC S3: the in-region rule

The chapter computes ocean thermal forcing (as forcing for
marine-terminating glaciers) by reading ECCO v4r4 directly from the
PO.DAAC S3 bucket in the AWS us-west-2 region, and states the
load-bearing access facts: the notebook must run from an environment
also in us-west-2, direct S3 reads avoid maintaining a local copy and
avoid data egress charges, and authentication rides the same Earthdata
netrc setup.[^tut-thermal] The credential facts are owned by
[the ecco_access companion](ecco-access-library.md); the cloud context
by [the AWS companion](aws-cloud-access.md); the heat-flux inputs by
[the heat-flux family](../fields/ecco-v4r4/heat-flux.md).

[^tut-thermal]: ECCO v4 Python Tutorial: Calculate ocean thermal forcing from ECCOv4r4 data, direct from PO.DAAC S3 storage
