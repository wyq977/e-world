---
slug: k-sample-and-contingency-table-e-values
title: k-sample and contingency-table e-values
sources: 9
updated: 2026-10-12
---

# k-sample and contingency-table e-values

## Definition
The problem is to test that k ≥ 2 independent i.i.d. streams share one distribution (a k × 2 contingency table for Bernoulli streams), where the nuisance parameter is the common distribution and there is no group invariance to exploit. The generic block e-variable divides the alternative likelihood of a block by a product, over each single outcome, of the mixture (n_a/n) p_{θ*_a} + (n_b/n) p_{θ*_b}; it is an [e-variable](e-variable.md) in any parametric family and GRO whenever the single-outcome model is convex [turnerGenericEvariablesExact2024, eq. 3.1, Thm 1]. For 2 × 2 tables the denominator collapses to Bernoulli(θ_0) with θ_0 the allocation-weighted mean, so the [reverse information projection](reverse-information-projection.md) of a point alternative is a point mass at the pooled rate [turnerGenericEvariablesExact2024, eq. 4.2; grunwaldSafeTesting2024, Example 2; koolenLogoptimalAnytimevalidEvalues2022, Sec. 4.4].

## Key results
- Composite alternatives are learned Bayesianly block by block (posterior mean under independent Beta priors); the product is a test martingale and optional stopping is valid between complete blocks, with block sizes fixed before each block [turnerGenericEvariablesExact2024, eqs 3.5, 4.3–4.4, Prop. 2, Sec. 3.1].
- Not a Bayes factor: numerator is a Bayes marginal but the denominator is a prequential product; no Gunel–Dickey Bayes factor is an e-variable [turnerGenericEvariablesExact2024, eqs 3.7–3.8, App. S3]; see [bayes-factor-e-variable](bayes-factor-e-variable.md).
- Minimal effect size: put the prior on the boundary Θ(δ′) to guarantee growth for all larger effects; a known control rate reduces to a point alternative [turnerGenericEvariablesExact2024, Sec. 5, eq. 5.3].
- REGROW-optimal Beta(γ, γ) prior has γ ≈ 0.18; expected sample size under optional stopping is about Fisher's exact test planned size; k = 4 streams beat the chi-square test for larger effects; Fisher's test loses type-I control under optional stopping [turnerGenericEvariablesExact2024, Figs 2, 4, 5, S4.1]. Safe Testing records the same prior as almost REGROW and its (1/2) log n regret [grunwaldSafeTesting2024, Examples 6, 7, 9].
- Wald's two-sample SPRT is the conditional e-variable given Y_a + Y_b, equals one whenever y_a = y_b, and is worse than the GRO one [turnerGenericEvariablesExact2024, Sec. 8.2]; the "mixture of means" ratio is an e-variable for Bernoulli and Gaussian location but not for exponential or negative binomial families [Sec. 8.1].
- General nulls and confidence sequences: lift to a modified single-outcome problem with a random group label, take the RIPr there, re-expand to a block likelihood ratio; for closed convex Θ_0 ⊂ [0,1]² the block-KL minimiser is unique, on the boundary, and the GRO e-variable is a plain likelihood ratio; inverting over effect sizes gives exact anytime-valid confidence sequences for risk difference, relative risk and, via a one-sided union, odds ratio [turnerExactAnytimevalidConfidence2023, Thms 1–2, eqs 7, 9, 11, 12].
- Gaussian and Poisson k-sample tests are "simple" cases where the GRO e-variable is a likelihood ratio with E_P[S] = 1 for every null element; the Bernoulli case follows from concavity of the log [grunwaldOptimalEValuesExponential2024, Secs 4.1, 4.3.1]; in the Gaussian and Poisson k-sample settings the conditional and RIPr e-variables are also e-processes [haoEValuesExponentialFamilies2025, Prop. 1].
- Log-optimality under optional stopping holds for the 2 × 2 table because the one-outcome RIPr lies in the null [koolenLogoptimalAnytimevalidEvalues2022, Thm 12].
- SWEPIS stillbirth re-analysis: the effect-restricted e-variable stops before the sixth event in all permutations, any rejection means e ≥ 20 [turnerGenericEvariablesExact2024, Sec. 7].
- GRO e-variables for 2 × 2 and 2 × k binary tables from the maximum-entropy viewpoint: exact microcanonical forms and canonical approximations with NML and Beta priors, a regime where k grows with m, and a regret-slope dichotomy at γ = 1 that differs from the γ ≈ 0.18 REGROW prior of the block construction because the e-variable and the criterion differ [giuffridaTestingMaximumEntropy2025, eqs 62–68, 75–85, 90–107]; see [mdl-and-maximum-entropy-e-values](mdl-and-maximum-entropy-e-values.md).
- Contrast case where GROW ≠ REGROW, unlike group-invariant problems [perezortizEstatisticsGroupInvariance2024, below Cor. 3].
- ECMO 2 × 2 analysis with the Turner–Grünwald e-variable at β = 0.18, with and without a knowledge-based regularizer [martinRegularizedEprocessesAnytime2024, Sec. 5].

## Variants and related concepts
- [exponential-family-e-values](exponential-family-e-values.md), [survival-e-values](survival-e-values.md).
- [confidence-sets-and-sequences](confidence-sets-and-sequences.md), [optional-stopping](optional-stopping.md).

## Sources
- [turnerGenericEvariablesExact2024](../sources/turnerGenericEvariablesExact2024.md) — generic construction, simulations, SWEPIS.
- [turnerExactAnytimevalidConfidence2023](../sources/turnerExactAnytimevalidConfidence2023.md) — general nulls and confidence sequences.
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — 2 × 2 examples, REGROW.
- [koolenLogoptimalAnytimevalidEvalues2022](../sources/koolenLogoptimalAnytimevalidEvalues2022.md) — stopping-time log-optimality.
- [grunwaldOptimalEValuesExponential2024](../sources/grunwaldOptimalEValuesExponential2024.md) — simple-case k-sample results.
- [haoEValuesExponentialFamilies2025](../sources/haoEValuesExponentialFamilies2025.md) — e-process property in Gaussian/Poisson cases.
- [giuffridaTestingMaximumEntropy2025](../sources/giuffridaTestingMaximumEntropy2025.md) — maximum-entropy 2 × k tests.
- [perezortizEstatisticsGroupInvariance2024](../sources/perezortizEstatisticsGroupInvariance2024.md) — GROW vs REGROW contrast.
- [martinRegularizedEprocessesAnytime2024](../sources/martinRegularizedEprocessesAnytime2024.md) — ECMO application.

## Disagreements / open issues
- Theorem 2 of the confidence-sequence paper is proved only for the 2 × 2 table [turnerExactAnytimevalidConfidence2023].
- Hao, Grünwald, Lardy, Long and Adams 2024 on k-sample tests with exponential families is the source of several examples and is not in the bib.
