---
slug: approximate-and-asymptotic-e-values
title: Approximate, asymptotic and compound e-values
sources: 5
updated: 2026-10-12
---

# Approximate, asymptotic and compound e-values

## Definition
A compound e-value is a vector (E_1, …, E_K) with Σ_{k ∈ N(P)} E_P[E_k] ≤ K for every P, where N(P) is the set of true nulls; the condition appeared unnamed in the e-BH paper, was named in the weights paper, and is formalised with its lineage ("generalized" or "relaxed" e-values elsewhere) by Ignatiadis, Wang and Ramdas [wangFalseDiscoveryRate2021, proof of Prop. 2; ignatiadisEvaluesUnnormalizedWeights2022, Sec. 4.5; ignatiadisAsymptoticCompoundEvalues2024, Def. 2.1, App. A]. An (ε, δ)-approximate e-variable satisfies E_P[E ∧ t] ≤ 1 + ε + δt for all t, equivalently for atomless P E[E 1_A] ≤ 1 + ε on an event of probability at least 1 − δ; an asymptotic e-variable is a sequence that is (ε_n, δ_n)-approximate with both tending to zero, strongly so if δ_n = 0 eventually, uniformly so if the limits hold in supremum over P; approximate and asymptotic compound versions replace 1 by K and run along a triangular array in (n, K) [ignatiadisAsymptoticCompoundEvalues2024, Defs 3.1, 3.5, 3.13, 3.18, Props 3.2, 3.6].

## Key results
- Calibration commutes with every relaxation [ignatiadisAsymptoticCompoundEvalues2024, Thms 2.3, 3.3, Props 3.12, 3.16]; convergence in distribution to an e-variable suffices, giving CLT-type asymptotic e-values such as exp(λ√n X̄/S − λ²/2) for the mean-zero finite-variance null, where no nonasymptotic e-value is known [Prop. 3.8, Example 3.11, Thm 6.5].
- e-BH on compound, (ε, δ)-approximate or asymptotic compound e-values gives exact, α(1 + ε) + δ, or asymptotic FDR control under arbitrary dependence; every FDR procedure is e-BH on compound e-values, tightly if admissible [ignatiadisAsymptoticCompoundEvalues2024, Thms 4.3–4.4]; see [e-bh](e-bh.md). The compound condition alone gives FWER for ep-Bonferroni and FDR for ep-BH [ignatiadisEvaluesUnnormalizedWeights2022, Sec. 4.5].
- Closure under averaging lets any FDR procedures be combined or derandomised, recovering derandomised knockoffs and derandomising randomised e-BH; compound e-values are exactly the random weights under which weighted BH controls FDR; BY on compound p-values controls FDR [ignatiadisAsymptoticCompoundEvalues2024, App. C].
- Log-optimal simple separable compound e-value for point nulls against point alternatives is Storey's optimal discovery procedure statistic, the ratio of mixtures, via Robbins' compound-decision reduction to Kelly's problem; it pays only when nulls must be learned [ignatiadisAsymptoticCompoundEvalues2024, Thm 5.2, Prop. 5.4]; see [gro-criterion](gro-criterion.md).
- Localised and compound universal inference give (0, δ)-approximate e-values; plugging the NPMLE of the variance distribution into the ODP Bayes factor gives strongly asymptotic compound e-values for multiple t-tests as K → ∞ with n fixed, the first type-I guarantee for data-driven ODP [ignatiadisAsymptoticCompoundEvalues2024, Props 5.5–5.6, 6.1, Thm 6.3].
- Data-driven unnormalised weights from means of squares in simultaneous t-tests are approximate compound e-values by Basu's theorem [ignatiadisEvaluesUnnormalizedWeights2022, Thm 5.1, Prop. 5.2].
- Complementary universality: Thm 4.4 (single rejected set, FDR, compound e-values) versus the e-Closure principle (simultaneous sets, any expected loss, e-collections), with the dictionary e_S = K^{-1} Σ_{i ∈ S} ẽ_i [xuBringingClosureFalse2025, Thm 25]; see [e-closure-principle](e-closure-principle.md).
- First FDR-level instance of relaxed (compound) e-values and of derandomisation by averaging: knockoff e-values satisfy only Σ_{H_0} E[e_j] ≤ p, which the e-BH proof needs; averaging over independent knockoff draws keeps the condition and converges to the conditional expectation given the data, with a Hoeffding bound on the number of draws [renDerandomizedKnockoffsLeveraging2022, eq. 9, Thm 3, Sec. 3.3].

## Variants and related concepts
- [e-variable](e-variable.md), [e-bh](e-bh.md), [calibrator](calibrator.md).

## Sources
- [ignatiadisAsymptoticCompoundEvalues2024](../sources/ignatiadisAsymptoticCompoundEvalues2024.md) — primary source.
- [ignatiadisEvaluesUnnormalizedWeights2022](../sources/ignatiadisEvaluesUnnormalizedWeights2022.md) — compound condition and data-driven weights.
- [wangFalseDiscoveryRate2021](../sources/wangFalseDiscoveryRate2021.md) — origin, approximate e-values in Sec. 5.2.
- [xuBringingClosureFalse2025](../sources/xuBringingClosureFalse2025.md) — relation to e-collections.
- [renDerandomizedKnockoffsLeveraging2022](../sources/renDerandomizedKnockoffsLeveraging2022.md) — knockoff e-values and derandomisation.

## Disagreements / open issues
- A weaker *approximate compound notion gives FDR control only when e-BH makes order-K rejections [ignatiadisAsymptoticCompoundEvalues2024, Def. 3.17, Prop. B.3].
