---
type: convention
title: "ECCO in the NASA Earthdata Cloud on AWS"
description: "Tutorial-companion facts: the 2021-2022 PO.DAAC migration to AWS, in-cloud advantages, and the S3 open methods the chapter demonstrates."
tags: [ecco, tutorial-companion, access, cloud]
generated: { by: claude-code/fable-5, at: 2026-08-30T21:40:00Z }
status: draft
stale_after: 2027-01-04
sources:
  - id: tut-aws
    resource: https://ecco-v4-python-tutorial.readthedocs.io/AWS_Cloud_getting_started.html
    title: "ECCO v4 Python Tutorial: AWS Cloud getting started and retrieving ECCO datasets (updated 2025-07-24)"
    author: team:ecco-consortium
---

# ECCO in the NASA Earthdata Cloud on AWS

During 2021-2022 PO.DAAC datasets, ECCO included, migrated to the NASA
Earthdata Cloud hosted on Amazon Web Services; downloads from the cloud
behave like any web download, and working inside the cloud adds the
options the chapter demonstrates: opening datasets directly from an S3
bucket without downloading, or fast downloads to a cloud
instance.[^tut-aws] The chapter walks EC2 setup end to end and opens
ECCO datasets from S3 with and without parallelization.[^tut-aws]
In-region S3 access requirements are recorded on
[the thermal-forcing companion](ocean-thermal-forcing-s3.md); the
credential facts live on
[the ecco_access companion](ecco-access-library.md).

[^tut-aws]: ECCO v4 Python Tutorial: AWS Cloud getting started and retrieving ECCO datasets (updated 2025-07-24)
