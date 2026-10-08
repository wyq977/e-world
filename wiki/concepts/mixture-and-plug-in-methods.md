---
slug: mixture-and-plug-in-methods
title: Mixture and plug-in methods for composite alternatives
sources: 12
updated: 2026-10-08
---

# Mixture and plug-in methods for composite alternatives

## Definition
When the alternative is composite, two standard devices produce a single likelihood-ratio-type statistic: the method of mixtures integrates the alternative density over a prior ν, and the plug-in (prequential) method predicts each observation with an estimate built from the past [ramdasHypothesisTestingEvalues2025, eqs 3.7–3.8]. Both yield [test martingales](test-martingale.md) under a simple null and are asymptotically log-optimal under an L² condition [ramdasHypothesisTestingEvalues2025, Sec. 3.7, Prop. 7.14, Cor. 7.15]. The nonanticipating running-MLE numerator of universal inference is the plug-in method applied to an arbitrary model [wassermanUniversalInference2020, eq. 18].

## Key results
- The target growth rate for asymptotic log-optimality and the changepoint mixture example [ramdasHypothesisTestingEvalues2025, eq. 3.6, Example 3.25].
- In exponential families the mixture and plug-in universal-inference variants differ by O(1), and learning the alternative by a Bayes marginal costs (d/2) log n relative to a known alternative [haoEValuesExponentialFamilies2025, Thms 2.1, 4.1, Cor. 2].
- The sequential RIPr plug-in uses the prequential estimate μ̆ = (x_0 n_0 + Σ x_i)/(n + n_0) and achieves nD_R + ((d_rp − d_rq)/2) log n + O(1) in the simple case [haoEValuesExponentialFamilies2025, eqs 2.12–2.13, Thms 2.3, 4.3].
- REGROW with a simple null is a redundancy–capacity problem whose optimal prior tends to Jeffreys' [grunwaldSafeTesting2024, Example 5]; see [gro-criterion](gro-criterion.md).
- Empirically adaptive e-processes (betting on the past) are asymptotically log-optimal and consistent [ramdasHypothesisTestingEvalues2025, Def. 7.21, Thm 7.22]; see [testing-by-betting](testing-by-betting.md).
- History and mechanics: plug-in goes back to Wald's 1947 eq. 10.10; never plug in the raw MLE on discrete data; mixtures are not a special case of plug-in unless the class is fork-convex; Bayes factors are mixture martingales; mixing e-processes directly over a parameter; GRAPA [ramdasGametheoreticStatisticsSafe2023, Secs 3.2.1–3.2.5, 3.3.3].
- Mixtures as boundary devices with explicit conjugate forms, the √(v log v) rate of any continuous mixture, discrete approximations, and equivalence to Robbins' mixture SPRT for exponential families [howardTimeuniformNonparametricNonasymptotic2021, Lemma 2, Props 2, 5–10, Thm 2, Cor. 6]; see [confidence-sequence-boundaries](confidence-sequence-boundaries.md).
- The Gaussian mixture 'universal' test martingale (K+1)^{−1/2} exp((Σx)²/(2(K+1))) survives misspecification where a fixed-δ product collapses [vovkEvaluesCalibrationCombination2021, eq. 23, Fig. 1]; for Bernoulli data every martingale is a mixture, by de Finetti's representation [villeEtudeCritiqueNotion1939, Ch. V §3].
- If a simple e-variable exists for every point of a composite alternative, an e-variable for the whole alternative follows by mixtures or prequential plug-in [grunwaldOptimalEValuesExponential2024, Sec. 1.2].
- Applied prequential plug-ins: Bayes posterior mean per block with REGROW-tuned Beta priors [turnerGenericEvariablesExact2024, eq. 3.5, Prop. 2]; two-virtual-point smoothed MLE for the hazard ratio, tracking the oracle and beating a misspecified GROW test [terschureAnytimevalidLogrankTest2024, eq. 3.7, Fig. 1].
- 'Empirical E': renormalise a data-optimised e-variable by its supremum null expectation, turning redundancy into regret; predictive recursion praised as an alternative to Robbins mixtures and plug-in; learning the robustification weight by mixtures [grunwaldAuthorsReplyDiscussion2024, Secs 2–4].
- Composite alternatives handled only by Bayes mixtures and NML, whose redundancy bounds the e-variable's regret [giuffridaTestingMaximumEntropy2025, eq. 22, Thm 1].

## Variants and related concepts
- [universal-inference](universal-inference.md), [exponential-family-e-values](exponential-family-e-values.md).

## Sources
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — Sections 3.7 and 7.5.
- [haoEValuesExponentialFamilies2025](../sources/haoEValuesExponentialFamilies2025.md) — quantitative comparison, prequential plug-in.
- [wassermanUniversalInference2020](../sources/wassermanUniversalInference2020.md) — running-MLE plug-in.
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md) — history and mechanics.
- [howardTimeuniformNonparametricNonasymptotic2021](../sources/howardTimeuniformNonparametricNonasymptotic2021.md) — mixtures as boundaries.
- [vovkEvaluesCalibrationCombination2021](../sources/vovkEvaluesCalibrationCombination2021.md), [villeEtudeCritiqueNotion1939](../sources/villeEtudeCritiqueNotion1939.md) — mixture martingales.
- [grunwaldOptimalEValuesExponential2024](../sources/grunwaldOptimalEValuesExponential2024.md), [turnerGenericEvariablesExact2024](../sources/turnerGenericEvariablesExact2024.md), [terschureAnytimevalidLogrankTest2024](../sources/terschureAnytimevalidLogrankTest2024.md) — applied plug-ins.
- [grunwaldAuthorsReplyDiscussion2024](../sources/grunwaldAuthorsReplyDiscussion2024.md) — empirical E, predictive recursion.
- [giuffridaTestingMaximumEntropy2025](../sources/giuffridaTestingMaximumEntropy2025.md) — universal numerators.

## Disagreements / open issues
- RIPr for plug-in alternatives and sequential RIPr for Bayesian alternatives are not analysed [haoEValuesExponentialFamilies2025, Remark 3].
