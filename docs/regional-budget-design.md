# Regional budgets and flux decomposition: a design

_Status: draft for review. Nothing here is sanctioned or signed._

The bundle closes tracer budgets pointwise (every wet cell) and globally.
Neither answers the question a researcher actually asks, which is whether
the heat budget closes over the Gulf of Mexico between the surface and
700 m. This document designs that calculation, and flux decomposition
alongside it, as attested computations: a sanctioned executor, a receipt,
and a deterministic attester anyone can run.

## 1. It closes, and the test can fail

A regional heat budget was assembled over a control volume and compared
across three independent collections: the tendency from temperature and
sea-surface-height SNAPSHOTS, the transport from the raw face fluxes of
the THREE-DIMENSIONAL FLUX collection read directly at the volume's six
boundary faces, and the forcing from the SURFACE FLUX collection plus
geothermal. Measured 2026-08-31, one tile interior, 40 by 40 cells over
the top 20 levels, 27,921 wet cells, 4.135e15 m3, all twelve months of
2010:

**Maximum residual 1.63e-14 degC per s**, against the signed pointwise
bar of 1e-10. Four orders of headroom.

The mutation controls matter more than the headline, because a test that
cannot fail is not evidence:

| implementation | residual per volume | relative to largest term | verdict |
|---|---|---|---|
| correct | 1.63e-14 | 1.85e-07 | passes |
| geothermal omitted | 1.24e-12 | 1.40e-05 | caught by the relative bar only |
| rim west face shifted one cell | 4.19e-09 | 4.75e-02 | caught by both |
| vertical face sign flipped | 3.37e-08 | 3.82e-01 | caught by both |
| vertical faces omitted | 1.68e-08 | 1.91e-01 | caught by both |

Read the second row carefully. Omitting geothermal flux, this bundle's
flagship trap, produces a residual of 1.24e-12, which is comfortably
INSIDE an absolute bar of 1e-10. An absolute criterion alone certifies a
budget missing a real physical term. It is caught only because the
relative criterion is also applied.

## 2. The oracle, corrected

An earlier draft of this document argued that the discrete divergence
theorem (summing pointwise convergence over a box equals the flux through
its rim) was the evidence that made regional budgets self-validating.
That argument was wrong and is retracted. The identity is algebra: each
interior face is added once and subtracted once from the same stored
number, so it holds bit for bit for ANY array, including random noise. It
was verified to return exactly zero on random data. It proves nothing
about physics, the grid, or an implementation.

What the identity actually licenses is narrower and still useful:
computing the regional convergence from rim faces is a legitimate
substitute for summing cell convergences. It is a permission, not a
proof.

The evidence has to cross an independence boundary, which gives three
requirements:

1. **Disjoint data paths.** The boundary term must be read from the raw
   face flux variables at the rim, never derived from the divergence
   field the pointwise pipeline already computes. An implementation that
   sums cell convergences and calls the result a boundary flux passes any
   consistency check while proving nothing, because both sides are then
   the same numbers.
2. **Two bars, not one.** An absolute bar in per-volume units, comparable
   to the signed pointwise tolerance, AND a relative bar against the
   largest regional term at about 1e-6. The absolute bar alone misses
   omitted physical terms, as measured above. Note that the bundle's
   argument for rejecting relative normalization is a POINTWISE argument
   (in quiescent cells both term and residual sit at the float32
   quantization floor, so the ratio measures storage precision). That
   argument does not transfer to regional sums, which sit far above the
   floor. Pointwise: absolute. Regional: both.
3. **Mutation controls as shipped evidence.** The receipt records that
   the sabotaged variants were run and failed. A pass with no
   demonstrated failure mode is not a result.

## 3. What this does NOT prove, and cannot

The oracle is blind to the error class that matters most to a researcher:
**whether the mask is the region they asked for.** If the box is off by
one cell, or confuses latitude with longitude, or mishandles the 0 to 360
against -180 to 180 convention, the same wrong mask feeds both the volume
integral and the rim extraction. The identity holds exactly, the budget
closes, the attester passes, and the user receives a beautifully attested
heat budget for the wrong body of water.

Nothing in the machinery can catch this. The mitigations are disclosure,
not verification: put the resolved bounds, the wet-cell count, the total
area, and a mask digest in the receipt so a reader can see which water
was actually integrated, and render the mask when a person is present.

## 4. What the authoritative material settles

The ECCO tutorial notebooks close budgets pointwise and globally. **No
tutorial closes a budget over a regional control volume** in any of the
heat, salt, or volume notebooks. There is no reproduction target to check
against and no prior art to defer to, which is why section 1 had to be
measured rather than cited.

The tutorial does supply the correct construction, in its meridional
transport example: build an indicator mask, take its discrete gradient to
get SIGNED boundary face masks, and integrate the already-face-integrated
fluxes against them. That generalizes from a latitude line to any closed
contour.

Three things it leaves genuinely unestablished, which this design must
therefore decide explicitly and disclose:

1. Volumes that do not touch the surface. Penetrating shortwave is
   nonzero to 200 m; geothermal enters only where the volume contains
   bottom cells.
2. Free-surface scaling for a regional integral rather than a point. The
   measurement in section 1 inherited the pointwise treatment unexamined.
3. Orientation for a closed-contour boundary mask. The tutorial's masks
   come out signed from the gradient and it never says what that sign
   means around a loop.

## 5. Where our shape differs

| Question | A skill-shaped answer | This design |
|---|---|---|
| How is the region fixed? | Elicited from the user at run time as free text | Bound parameters plus a mask digest in the receipt |
| What is the residual measured against? | A fraction of the largest term | Both an absolute per-volume bar and a relative bar, with measured baselines |
| Who refuses a non-closing budget? | The assistant is instructed to | The attester fails, mechanically, on the consumer's machine |
| Where does the knowledge live? | Inline in the skill's prose | Concepts with footnoted evidence, readable without running anything |
| What is the evidence? | A prose acceptance record | A receipt, a deterministic attester, mutation controls, and a signature path |

## 6. Attesting an arbitrary region

Attestation wants a fixed contract; users want an arbitrary box. Three
tiers resolve it.

1. **Registered name.** The registry lives inside the sanctioned file, so
   an unregistered name fails rather than improvising a mask.
2. **Explicit box.** Bounds and depth range travel as bound parameters,
   and the receipt carries a DIGEST OF THE RESOLVED MASK ARRAY, not
   merely a wet-cell count and area. Two scalars can be reproduced by an
   executor that then integrates over different cells; a digest cannot.
   The geometry granule's checksum is pinned alongside, and the edge
   predicate (cells whose centers fall inside, wet defined as partial
   cell fraction above zero) is specified exactly, so recomputation is
   deterministic and correct runs do not fail spuriously.
3. **Supplied mask.** The digest mechanism, applied directly.

Depth ranges snap to stored cell faces and the receipt reports the
resolved depths. A range cutting mid-cell has NO oracle: no stored
vertical flux exists at the cut plane, so the boundary term would have to
be interpolated and the residual would carry a first-order error rather
than round-off.

## 7. Terms a design must carry

- **Vertical boundary faces** at the top and bottom of the depth range.
  For a 0 to 700 m volume these carry the dominant vertical exchange, and
  omitting them was caught at 1.68e-08 above. Note the vertical
  convergence carries no leading minus sign where the horizontal does;
  applying the horizontal convention to the vertical faces flips them.
- **Geothermal flux**, heat budget only, at the bottom wet cell. It is a
  static model input distributed with the tutorial, NOT a PO.DAAC
  collection, so a budget assembled from archive holdings alone omits it
  silently, and as measured above the absolute bar will not catch that.
- **Shortwave penetration**, the two-exponential profile cut off below
  200 m, subtracted from the surface term so it is not double counted.
- **Salt plume tendency** as a three-dimensional term, with the surface
  salt flux at the top level only.
- **Free-surface scaling** from bracketing snapshots, not monthly means.
- **The weighting asymmetry.** Within one budget the tracer fluxes are
  already face-integrated transports and must NOT be multiplied by any
  area, while the mass velocities need face length and layer thickness
  and must NOT have the partial-cell factor reapplied.

## 8. Flux decomposition without settling the open question

Whether the decomposition carries three terms or four is a scope choice
about what the user means, not a correctness question. This design does
not need it answered: the grouping travels as a declared parameter, the
attester requires the parts to sum back to the total, and the receipt
discloses which convention produced the number. An outside reader
comparing two results can then see whether they used the same
decomposition.

## 9. Machinery to build

1. Indicator mask to signed boundary face masks, by discrete gradient.
2. Depth-range snapping to stored faces, with resolved bounds disclosed.
3. Seam-aware differencing. The connectivity is NOT new work: the
   thirteen-tile topology is a small static table, and lifting it into a
   sanctioned file keeps executors dependency-light rather than taking a
   heavy pinned stack. The open item is calibration, not topology: the
   pointwise tolerance was measured on a tile interior and has never been
   validated at a seam cell, so the tolerance must be re-measured there
   before a seam-crossing box can be judged against it.
4. Regional integration with per-collection weighting.
5. The mask-digest attestation path.

## 10. What still needs a person

Whether a chosen region and period answer the scientific question;
observational benchmarks; interpretation for publication; and the mask
sanity check that section 3 shows no machine can perform.

## 11. Trap encountered while measuring this

Reading a flux variable through a plain array conversion leaks the file's
fill values, near 1e36, into what looks like ordinary data; summed over a
large box in float32 the result overflows to infinity. The first run of
this work produced exactly that. Separately, land cells carry missing
values that survive multiplication by a zero volume weight, so an
unguarded volume integral returns not-a-number rather than a wrong
number. Both are the good failure mode, and both mean a regional
integration must mask before it sums and assert that the result is
finite and physically plausible.
