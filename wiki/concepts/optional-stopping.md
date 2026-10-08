---
slug: optional-stopping
title: Optional stopping and sequential decomposability
sources: 2
updated: 2026-10-08
---

# Optional stopping and sequential decomposability

## Definition
Optional stopping means ending a single data stream at a data-dependent time. An e-value test is safe under optional stopping only if its e-specification is sequentially decomposable (seqdec), that is, s[n] factors as a product of conditional e-variables s_i, and the stopping time is adapted to the e-variable's possibly coarsened filtration [grunwaldSafeTesting2024, Sec. 5]. Otherwise one can construct fake conditional e-variables and lose the guarantee. Under these conditions the product is a [test martingale](test-martingale.md) and [Ville's inequality](villes-inequality.md) applies; the general object that is valid at every stopping time is the [e-process](e-process.md) [ramdasHypothesisTestingEvalues2025, Def. 7.3].

## Key results
- Seqdec has three properties: it permits stopping within studies, concatenated-data martingales, and coherence of local and global analysis; plug-in versus sequential application and the t-test coarsened-filtration caveat [grunwaldSafeTesting2024, Sec. 5, Fig. 3].
- REGROW for the 2×2 table is not seqdec, but a Beta(0.18, 0.18) sequential prior is almost REGROW [grunwaldSafeTesting2024, Example 9].
- Expected and worst-case sample sizes under optional stopping [grunwaldSafeTesting2024, Sec. 6]; see [e-power](e-power.md).
- The Safe Testing authors concede that "safe" was a poor name and that the "fewer samples" claim refers only to binary decisions [grunwaldSafeTesting2024, reply].
- SAVI (safe anytime-valid inference) versus Wald's sequential paradigm is contrasted on four points [ramdasHypothesisTestingEvalues2025, Sec. 7.2].

## Variants and related concepts
- [optional-continuation](optional-continuation.md), the study-level version.
- [confidence-sets-and-sequences](confidence-sets-and-sequences.md).

## Sources
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — Section 5 in full, Example 9, eq. 31.
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — e-process definition, Chapter 7.

## Disagreements / open issues
- When a GRO criterion admits a seqdec or ε-seqdec specification is open [grunwaldSafeTesting2024, eq. 31].
- Approximate optional stopping for non-e-process e-variables is conjectured [haoEValuesExponentialFamilies2025, Sec. 7].
