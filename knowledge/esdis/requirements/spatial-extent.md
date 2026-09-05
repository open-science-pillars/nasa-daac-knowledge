---
type: requirement
title: Spatial extent is a required collection field
description: "SpatialExtent is in the UMM-C schema's required array: a collection record without a declared spatial extent is invalid against the metadata model."
tags: [requirement, spatial, metadata, cross-archive]
status: draft
class: MUST
generated: { by: claude-code/fable-5, at: 2026-08-31T02:09:11Z }
stale_after: 2026-11-30
sources:
  - id: umm-c-schema
    resource: https://cdn.earthdata.nasa.gov/umm/collection/v1.18.4/umm-c-json-schema.json
    title: UMM-C JSON schema v1.18.4, top-level required array
---

# Spatial extent is a required collection field

Collection metadata declares its spatial extent. The UMM-C JSON
schema, version 1.18.4, lists SpatialExtent in its top-level required
array, so a record without one is invalid against the model
itself.[^umm-c-schema] The class is MUST on that verified schema
citation; a schema version bump re-verifies it at the next sweep.

**Check binding.** Structural: spatial-extent-present (cmr-structural,
the observatory sweeper). pyQuARC candidates, proposed and pending
confirmation by the Application Support and Science Enabling Team
(ASSET):
spatial_extent_requirement_fulfillment_check, with
granule_spatial_representation_check adjacent on the granule side.

[^umm-c-schema]: UMM-C v1.18.4 top-level required array, fetched 2026-08-30
