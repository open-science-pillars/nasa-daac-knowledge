# ECCO V4r4 fields layer

The layer that makes "all the ECCO model fields" a machine-checked
claim: one Data Collection concept per collection family, 26 families
covering the 90 ECCO_L4_*V4R4* collections at PO.DAAC. Concepts are
drafted only from the family manifest (tools/ecco_v4r4_families.yaml,
the single source of truth for family membership), machine-confirmed by
the live CMR verifier (tools/verify_cmr.py, whose --sign is the only
writer of process events), and steward-signed after granule
verification; tools/check_fields.py reconciles this directory against
the manifest and its coverage meter is the completeness claim.

## families

Filled as family concepts land; the coverage meter in
tools/check_fields.py tracks progress toward 26/26 families and 90/90
ShortNames.
