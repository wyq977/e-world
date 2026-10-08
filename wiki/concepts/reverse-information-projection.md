---
slug: reverse-information-projection
title: Reverse information projection (RIPr)
sources: 4
updated: 2026-10-08
---

# Reverse information projection (RIPr)

## Definition
The reverse information projection of an alternative Q onto a convex set of null distributions is the element P*_0 minimising D(Q ‖ P) over the convex hull (Bayes marginals) of the null; it may be a sub-probability measure and may lie outside the null [grunwaldSafeTesting2024, Thm 1, App. A.1]. The GRO e-variable is q/p*_0 [grunwaldSafeTesting2024, Cor. 2]. In the assumption-free version it is defined through the [numeraire](numeraire.md): dP*/dQ = 1/E*, living in the bipolar P°° of the null, and for finite nulls it is the KL-closest convex combination [ramdasHypothesisTestingEvalues2025, Definition 6.7, Props 6.6, 6.11]. The underlying lemmas come from Li's 1999 Yale thesis [grunwaldSafeTesting2024, App. A.1; wassermanUniversalInference2020, Sec. 6].

## Key results
- Strong duality and characterisations [ramdasHypothesisTestingEvalues2025, Thms 6.13, 6.14].
- The defining inequality E_Q[p_θ / p*] ≤ 1 for all θ, with the KKT heuristic [wassermanUniversalInference2020, eq. 16, Sec. 6].
- Under misspecification in convex model classes the universal confidence set covers the RIPr of the truth, and a RIPr split LRT dominates the plain split LRT when the RIPr lies in the null [wassermanUniversalInference2020, Props 7–8].
- Explicit nondegenerate RIPrs: for Gaussian location in the anti-simple case the RIPr prior is exactly N(μ*, (Σ_q − Σ_p)/n), and in general exponential families it is approximately Gaussian with O(1/n) variance; the RIPr of a Bayes mixture Q_{W_1} is approximately P_{W_1} with the same prior [haoEValuesExponentialFamilies2025, Thms 1.4, 2.4, 3.4, 4.4, Lemma 2].
- For the 2×2 contingency table with a point alternative the RIPr is a point mass at the pooled rate [grunwaldSafeTesting2024, Example 2, eq. 14]; finite support follows from Carathéodory [App. A.3].
- Local RIPr used by the sequential plug-in e-variable [haoEValuesExponentialFamilies2025, eq. 1.3]; see [exponential-family-e-values](exponential-family-e-values.md).
- Regularity-free extensions via description gain (Lardy, Grünwald, Harremoës) and the numeraire [grunwaldSafeTesting2024, reply Sec. 2].

## Variants and related concepts
- [gro-criterion](gro-criterion.md), [numeraire](numeraire.md).
- [bayes-factor-e-variable](bayes-factor-e-variable.md), the RIPr as a forced null prior.

## Sources
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — definition, Theorem 1, existence proofs, examples.
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — bipolar definition, duality, history.
- [haoEValuesExponentialFamilies2025](../sources/haoEValuesExponentialFamilies2025.md) — explicit and approximate RIPrs in exponential families.
- [wassermanUniversalInference2020](../sources/wassermanUniversalInference2020.md) — RIPr under misspecification, RIPr split LRT.

## Disagreements / open issues
- No general fast algorithm for computing the RIPr prior is given; numerical accuracy for infinite sample spaces is unclear [grunwaldSafeTesting2024, Sec. 2]; direct computation is infeasible for large effect sizes in the simulations [haoEValuesExponentialFamilies2025, Sec. 4].
- Whether q/p_{W_0,(n)} with the Gaussian O(1/n)-variance prior is exactly an e-variable in general exponential families, or only o(1)-close in e-power, is unresolved [haoEValuesExponentialFamilies2025, below Thm 3].
