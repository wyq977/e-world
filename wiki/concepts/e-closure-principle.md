---
slug: e-closure-principle
title: The e-Closure principle and true-discovery guarantees
sources: 5
updated: 2026-10-08
---

# The e-Closure principle and true-discovery guarantees

## Definition
An e-collection is a family (e_S)_{S ⊆ [m]} of nonnegative statistics with E_P[e_{N_P}] ≤ 1 for every P in the model, where N_P is the set of true nulls; for example e_S an e-value for the intersection hypothesis H_S, or only for the partitioning hypothesis {N_P = S} [xuBringingClosureFalse2025, Def. 5, Sec. 9]. The e-Closure procedure for an expected-loss error rate E[f_{N_P}(R)] at level α rejects any set R with e_S ≥ f_S(R)/α for all S. The e-Closure principle states that a procedure controls such an error rate, simultaneously over a collection of rejected sets, if and only if it is contained in an e-Closure procedure [xuBringingClosureFalse2025, Thm 6]. Thresholding at 1/α recovers the classical closure principle for FWER exactly, and with FDP as loss it yields the first necessary-and-sufficient principle for FDR [xuBringingClosureFalse2025, Thms 12, 14]. The e-value translation of closed testing goes back to Vovk and Wang's discovery e-vector and e-matrix, which give simultaneous lower bounds on true discoveries for every rejection set under arbitrary dependence [vovkConfidenceDiscoveriesEvalues2023, Sec. 6, App. C].

## Key results
- The canonical e-collection e_S = max_R f_S(R)/α proves necessity and is idempotent, so power gains require better local e-values [xuBringingClosureFalse2025, Prop. 8].
- Closed e-BH uses the arithmetic mean of the e_i in S as local e-value and uniformly improves e-BH in power and simultaneity under arbitrary dependence; it can reject all m hypotheses where e-BH rejects none and rejects hypotheses with e_i < 1/α; with compound e-values closed e-BH equals e-BH [xuBringingClosureFalse2025, Thm 17, Example 20, Thm 25]; see [e-bh](e-bh.md).
- Closed BY uses an |S|-dependent p-to-e calibrator; closed Su uses a Simes p-value with l_α = −W_{−1}(−α/e); e-collections built from Li–Zhang compound e-values only reconstruct BH and adaptive BH [xuBringingClosureFalse2025, Thms 28, 34, 37].
- Closed BH: the first uniform improvement of ordinary BH by e-closure, valid under PRDS and a weaker minimal sufficient condition E[e_N] ≤ 1, built from a family of BH-like step-up procedures with a horizon matrix; equals minimally adaptive BH whenever that rejects fewer than √m, gains when BH already rejects many; simultaneity is essentially nil for it [goemanUniformImprovementBenjaminiHochberg2026, Thms 8, 12, 13, 19, Props 15, 16, 18].
- Post-hoc flexibility: simultaneity equals post-hoc choice of the rejected set; the error metric may be chosen post hoc among losses controlled by the same collection; if the collection is α-free, α may be chosen post hoc, extending the e-BH result of the book [xuBringingClosureFalse2025, Lemma 4, Thms 39, 41, 44, 48; ramdasHypothesisTestingEvalues2025, Thm 9.10]; see [post-hoc-validity](post-hoc-validity.md).
- Discovery e-matrix for nested rejection sets is monotone along rows, columns and diagonals and computable in O(K²) by a convex-hull slope argument; it is the exact e-translation of the Genovese–Wasserman / Goeman–Solari procedure, and the authors assert admissibility of the arithmetic-mean version as an e-procedure without proof [vovkConfidenceDiscoveriesEvalues2023, Sec. 9, Algorithm 4, App. C].
- Computation: O(m²) subsets suffice for monotone local e-values; closed e-BH in O(m² log m), closed BY in O(m³); R package eClosure and Python eclosure [xuBringingClosureFalse2025, Sec. 10].
- Admissible procedures on arbitrary e-values have weighted affine local e-values; Sun and Wang 2026 prove a complete-class theorem for weighted-mean closed e-BH [xuBringingClosureFalse2025, App. B].
- FWER closure of e-merging functions, the precursor [vovkEvaluesCalibrationCombination2021, Thm 5.1].

## Variants and related concepts
- [e-bh](e-bh.md), [e-merging](e-merging.md), [calibrator](calibrator.md).

## Sources
- [xuBringingClosureFalse2025](../sources/xuBringingClosureFalse2025.md) — the principle, closed e-BH, BY, Su, post-hoc results, computation.
- [goemanUniformImprovementBenjaminiHochberg2026](../sources/goemanUniformImprovementBenjaminiHochberg2026.md) — closed BH.
- [vovkConfidenceDiscoveriesEvalues2023](../sources/vovkConfidenceDiscoveriesEvalues2023.md) — discovery e-vectors and e-matrices.
- [vovkEvaluesCalibrationCombination2021](../sources/vovkEvaluesCalibrationCombination2021.md) — FWER closure precursor.
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — closed e-BH in Section 9.6.

## Disagreements / open issues
- Closed BH is a uniform improvement classically but not in the simultaneity sense of the e-Closure paper [goemanUniformImprovementBenjaminiHochberg2026, Thm 19].
- Online e-closure (Fischer, Ramdas; Xu, Fischer, Ramdas 2026) and the Sun–Wang complete-class paper are in the reading queue, not ingested.
