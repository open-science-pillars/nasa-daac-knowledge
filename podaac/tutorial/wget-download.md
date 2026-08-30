---
type: convention
title: "Batch downloading ECCO granules with wget"
description: "Tutorial-companion facts for the wget path: Earthdata account, netrc plus urs_cookies files, granule list, GNU wget batch."
tags: [ecco, tutorial-companion, access]
generated: { by: claude-code/fable-5, at: 2026-08-30T21:40:00Z }
status: draft
stale_after: 2027-01-04
sources:
  - id: tut-wget
    resource: https://ecco-v4-python-tutorial.readthedocs.io/Tutorial_wget_Command_Line_HTTPS_Downloading_ECCO_Datasets_from_PODAAC.html
    title: "ECCO v4 Python Tutorial: Using wget to Download ECCO Datasets from PO.DAAC (v1.0, 2021-06-25, McNelis and Fenty)"
    author: team:ecco-consortium
---

# Batch downloading ECCO granules with wget

The command-line HTTPS download path, per the tutorial's four steps: an
Earthdata account, a netrc plus a `urs_cookies` file, a prepared list
of granules, and a GNU wget batch over that list.[^tut-wget] The
chapter is dated (v1.0, 2021-06-25) and predates the cloud migration
described in the AWS chapter; the Earthdata credential facts (netrc
structure, permissions, the password-character warning) are recorded
once on [the ecco_access companion](ecco-access-library.md) and apply
here unchanged.[^tut-wget]

[^tut-wget]: ECCO v4 Python Tutorial: Using wget to Download ECCO Datasets from PO.DAAC (v1.0, 2021-06-25, McNelis and Fenty)
