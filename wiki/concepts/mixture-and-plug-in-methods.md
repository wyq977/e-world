---
slug: mixture-and-plug-in-methods
title: Mixture and plug-in methods for composite alternatives
sources: 3
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

## Variants and related concepts
- [universal-inference](universal-inference.md), [exponential-family-e-values](exponential-family-e-values.md).

## Sources
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — Sections 3.7 and 7.5.
- [haoEValuesExponentialFamilies2025](../sources/haoEValuesExponentialFamilies2025.md) — quantitative comparison, prequential plug-in.
- [wassermanUniversalInference2020](../sources/wassermanUniversalInference2020.md) — running-MLE plug-in.

## Disagreements / open issues
- RIPr for plug-in alternatives and sequential RIPr for Bayesian alternatives are not analysed [haoEValuesExponentialFamilies2025, Remark 3].
