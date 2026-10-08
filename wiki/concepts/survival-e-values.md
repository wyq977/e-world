---
slug: survival-e-values
title: E-values for survival data (anytime-valid logrank)
sources: 3
updated: 2026-10-08
---

# E-values for survival data (anytime-valid logrank)

## Definition
For time-to-event data under proportional hazards, the ratio of sequentially computed Cox partial likelihoods S_t = PL_{θ1,t}/PL_{θ0,t} is a [test martingale](test-martingale.md): each one-event factor, the risk-set multinomial probability under the alternative divided by that under the null, has conditional null expectation exactly one [terschureAnytimevalidLogrankTest2024, eqs 3.1–3.4, Prop. 3.1]. [Ville's inequality](villes-inequality.md) then gives an exact, nonasymptotic level-α test at any random time with any allocation ratio, the anytime-valid logrank test. The survey treats the logrank statistic as the canonical monotone-likelihood-ratio GRO example [ramdasGametheoreticStatisticsSafe2023, Sec. 4.1.1].

## Key results
- Validity under general independent incomplete observation (censoring, left truncation, filtering), proved in continuous time with counting processes because these preserve the compensator structure [terschureAnytimevalidLogrankTest2024, Lemma A.1, Cor. A.2].
- Any predictable numerator on the risk set gives a valid generalised test; the point-alternative numerator is conditionally GROW for θ ≤ θ1, and GROW approximately minimises the worst-case expected number of events to rejection via Wald's identity [terschureAnytimevalidLogrankTest2024, eq. 3.5, Sec. 3.1, App. A.1]; see [gro-criterion](gro-criterion.md).
- No minimal effect size: prequential smoothed-MLE plug-in or Bayes-mixture numerator, valid for any prior; with θ0 = 1 the test stays valid under arbitrary violation of proportional hazards [terschureAnytimevalidLogrankTest2024, eq. 3.7, App. A.4, Example 3.2]; see [mixture-and-plug-in-methods](mixture-and-plug-in-methods.md).
- Ties via hypergeometric null and Fisher-noncentral-hypergeometric numerator, only for θ0 = 1 [terschureAnytimevalidLogrankTest2024, Lemma 3.3, Cor. A.4].
- Gaussian Z-score approximation for summary-statistic meta-analysis, an e-variable only for balanced allocation and 0.5 ≤ θ1 ≤ 2, otherwise conservative; its rejection region matches continuous-monitoring O'Brien–Fleming but has no maximum sample size [terschureAnytimevalidLogrankTest2024, eq. 4.3, App. C.1, Figs 2, 6, 7].
- Price of anytime validity: larger design maximum than the fixed-sample logrank test (195 events vs O'Brien–Fleming 205, Pocock 245 at θ1 = 0.7, α = 0.05, 80% power) but equal or smaller mean number of events when stopping at S ≥ 20 [terschureAnytimevalidLogrankTest2024, Fig. 4, Sec. 7].
- Meta-analysis: the product of per-trial martingales is a test martingale even when trial start times depend on other trials' data, enabling ALL-IN living meta-analysis [terschureAnytimevalidLogrankTest2024, Prop. 5.1]; see [optional-continuation](optional-continuation.md).
- Covariates: running-MLE universal-inference denominator is practical; a RIPr version is valid for any prior but not yet computable [terschureAnytimevalidLogrankTest2024, eq. 8.2, Thm B.1].
- Inverting the prequential statistic gives anytime-valid confidence sequences for the hazard ratio; inverting the point-alternative one can leave intervals wide forever [terschureAnytimevalidLogrankTest2024, Sec. 6, Sec. 8.4].
- Cox partial-likelihood ratios are e-processes, so the e-posterior results apply to proportional-hazards estimation [grunwaldEposterior2023, Sec. 5].

## Variants and related concepts
- [k-sample-and-contingency-table-e-values](k-sample-and-contingency-table-e-values.md), the discrete two-group analogue.
- [confidence-sets-and-sequences](confidence-sets-and-sequences.md).

## Sources
- [terschureAnytimevalidLogrankTest2024](../sources/terschureAnytimevalidLogrankTest2024.md) — founding source.
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md) — positioning as the MLR example.
- [grunwaldEposterior2023](../sources/grunwaldEposterior2023.md) — e-posterior for survival.

## Disagreements / open issues
- Rigorous justification of the sequential Gaussian approximation is left to time-uniform central limit theory [terschureAnytimevalidLogrankTest2024, Sec. 4].
