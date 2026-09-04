---
type: convention
title: "The ecco_access library: packaging, contract, and Earthdata setup"
description: "Tutorial-companion facts about ECCO access tooling: the ecco_access packaging split at ecco_v4_py 1.8, the two top-level functions, how earthaccess finds an Earthdata Login, and V4r5 in-cloud reachability."
tags: [ecco, tutorial-companion, access]
generated: { by: claude-code/fable-5, at: 2026-08-30T21:25:00Z }
status: draft
stale_after: 2027-01-04
sources:
  - id: tut-access-intro
    resource: https://ecco-v4-python-tutorial.readthedocs.io/ECCO_access_intro.html
    title: "ECCO v4 Python Tutorial: The ecco_access library (page updated 2025-11-13)"
    author: team:ecco-consortium
  - id: earthaccess-login
    resource: https://github.com/nsidc/earthaccess
    title: "earthaccess 0.18.0, login() docstring read from the installed package 2026-08-31: default strategy all, trying environment then netrc then interactive"
---

# The ecco_access library: packaging, contract, and Earthdata setup

Companion concept for the tutorial's access chapter: the dated facts an
agent needs, each footnoted to the page; the OSP-observed access
peculiarities stay in the concepts that own them (linked below).

**Packaging split (load-bearing, dated).** The ecco_access modules are
now their own Python package, installable with conda or pip, and are no
longer included in ecco_v4_py as of version 1.8; the tutorial page
covers users of ecco_v4_py at least 1.7.4 and below 1.8, and states it
will be removed at a later date.[^tut-access-intro] Version therefore
matters when reproducing any recorded ecco_access behavior: the quirk
pinned in this bundle was observed on ecco_access 0.3.1 (see
[grid geometry](../fields/ecco-v4r4/geometry.md)).

**The two top-level functions.** `ecco_podaac_to_xrdataset` takes a
text query or ECCO dataset identifier and returns an xarray Dataset;
`ecco_podaac_access` takes the same input and returns the URLs, paths,
or local files where the data is located.[^tut-access-intro] The
exact-ShortName discipline and the static-collection route around
ecco_access are recorded on
[the dataset concept](../datasets/ecco-v4r4.md).

**Earthdata setup.** An Earthdata account is required for ECCO output
hosted by PO.DAAC, and only for retrieving data: searching CMR needs
no account.[^tut-access-intro] earthaccess finds the credential in
three places, and at version 0.18.0 its default `login()` strategy
tries them in this order: the environment (an `EARTHDATA_TOKEN`, or
username and password variables), then `~/.netrc`, then an interactive
prompt.[^earthaccess-login] The environment path is the practical one
in CI and in cloud notebooks, where creating a file is the awkward
step.

Using `~/.netrc` (`_netrc` on Windows) means a
`machine urs.earthdata.nasa.gov` entry in a file readable only by the
current user (mode 0600), otherwise the error "netrc access too
permissive" is raised, and some password characters cause problems
depending on the system: backslash, space, hash, quotes, and the
greater-than sign.[^tut-access-intro]

The tutorial chapter documents the netrc path only. That is narrower
than the library rather than wrong, and the difference is a candidate
for the upstream offer.[^tut-access-intro][^earthaccess-login]

**V4r5 reachability.** The chapter carries a section on accessing
ECCOv4 release 5 output in the AWS Cloud through
ecco_access,[^tut-access-intro] which is the in-cloud reachability the
release-trigger kit's playbook assumes ahead of the PO.DAAC
publication.

[^tut-access-intro]: ECCO v4 Python Tutorial: The ecco_access library (page updated 2025-11-13)
[^earthaccess-login]: earthaccess 0.18.0 login() docstring, read from the installed package 2026-08-31
