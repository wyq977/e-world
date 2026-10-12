---
slug: test-martingale
title: Test martingale
sources: 27
updated: 2026-10-12
---

# Test martingale

## Definition
A test martingale (or test supermartingale) is a nonnegative (super)martingale under every null distribution with initial value at most one; it is the wealth process of a gambler betting against the null [ramdasHypothesisTestingEvalues2025, Definition 7.3(i); grunwaldSafeTesting2024, Prop. 2]. The running product of conditional e-variables is a test supermartingale, and conversely for a simple null every [e-process](e-process.md) is dominated by a test martingale via the Snell envelope and Doob decomposition [ramdasHypothesisTestingEvalues2025, Sec. 7.5.1].

## Key results
- Optional stopping: E_P[M_τ] ≤ 1 at every stopping time [ramdasHypothesisTestingEvalues2025, Fact 7.5].
- The nonanticipating plug-in likelihood ratio L_t = ∏ p_{θ̂_{i−1}}(Y_i)/p_{θ*}(Y_i) is a test martingale under θ*, which is what makes the running-MLE statistic an e-process; the device goes back to Wald, Robbins and Siegmund, and Lorden and Pollak [wassermanUniversalInference2020, eq. 18, Sec. 7].
- Mixture and plug-in likelihood ratio processes are test martingales [ramdasHypothesisTestingEvalues2025, Sec. 7.5]; see [mixture-and-plug-in-methods](mixture-and-plug-in-methods.md).
- Flexible filtrations: conditional e-variables may condition on side information, and study-level versus data-level martingales differ [grunwaldSafeTesting2024, Def. 1, App. B.1, Sec. 5].
- Fork-convexity separates test supermartingales from e-processes: for some composite nulls no nonnegative supermartingale has power while an e-process does [ramdasHypothesisTestingEvalues2025, Chapter 7 note].
- Ville's original: Chapter V Definition 1 (nonnegative, s_0 = 1, E[s_n | past] = s_{n−1}) 'définit une martingale ou un jeu équitable'; Theorem IV.1 shows every null set is detected by some martingale and Theorem IV.2 that each is a.s. bounded; for Bernoulli data every martingale is a Beta-type mixture of likelihood ratios [villeEtudeCritiqueNotion1939, Ch. IV–V]; see [martingale-history](martingale-history.md).
- Every test martingale for a simple null is a likelihood ratio q(X^t)/p(X^t) of conditional unit bets; composite test martingales are 'simultaneous likelihood ratios' [ramdasGametheoreticStatisticsSafe2023, Secs 2.2–2.3, eqs 3–5].
- Sequential e-values (E[E_k | E_1..E_{k−1}] ≤ 1) have partial products that are test supermartingales, valid in any order [vovkEvaluesCalibrationCombination2021, Sec. 4]; Shafer's Protocol 2 shows any global bet is implementable round by round so the capital is a nonnegative martingale [shaferTestingBettingStrategy2021, Sec. 4].
- Nonparametric test supermartingales: the sub-ψ exponential supermartingales and the empirical-Bernstein self-normalised supermartingale [howardTimeuniformNonparametricNonasymptotic2021, Def. 1, App. A.8]; see [confidence-sequence-boundaries](confidence-sequence-boundaries.md).
- A simple e-variable multiplied over i.i.d. outcomes is a test martingale whose stopped value is log-optimal for any adapted stopping time [grunwaldOptimalEValuesExponential2024, Sec. 1.3; koolenLogoptimalAnytimevalidEvalues2022, Thm 12]; the Cox partial-likelihood ratio is a continuous-time test martingale [terschureAnytimevalidLogrankTest2024, Prop. 3.1].
- A composite nonnegative martingale is a likelihood ratio against an 'implied alternative' for every null element; nonnegative martingales with initial value one are precisely the admissible e-processes under a point null; complete characterisation under conditional symmetry as ∏ f_t(X_t) with f_t(x) + f_t(−x) = 2, and de la Peña's symmetric supermartingale is inadmissible, dominated by its mirrored version [ramdasAdmissibleAnytimevalidSequential2022, Prop. 4, Thm 18, Cor. 29, Prop. 39, Example 40].
- Useful supermartingales that are not nonnegative (improper mixtures with a receding floor), and the floor-hugger martingale as the extremal process for crossing a growing threshold from a sinking floor [koolenGeneralisationVilleInequality2025, eqs 3, 5–6, 8].
- Invariant likelihood ratios are martingales in the coarsened filtration [perezortizEstatisticsGroupInvariance2024, Prop. 6]; induced tests are bounded nonnegative martingales started at the size of the terminal test [koningAnytimeValidityFree2026, Remark 1]; restarted test martingales as change-detection primitives [sahaNonpartitionedEdetectorsNonparametric2026, Props 3.1, 4.1, A.1; shinEdetectorsNonparametricFramework2023, Defs 2.8–2.9].
- The NSM property is closed under fork-convex, not just convex, combinations; under all Bernoulli laws the only nonnegative martingale is constant and all supermartingales nonincreasing; composite Snell envelopes [ramdasTestingExchangeabilityForkconvexity2021, Lemma 12, Thms 13, 14, 17]. For families containing all i.i.d. Bernoulli laws no (super)martingale witnesses the composite strong law; singleton witnesses are martingales up to versions [rufCompositeGeneralizationVille2022, Sec. 4.3, Remark 3.2].
- Universal representation: for any class S, test (super)martingales are exactly ∏(1 + λ_i Z_i) with Z_i ≥ −1 conditionally mean-zero (≤ 0) under all of S; 'E(X_t | F_{t−1}) = μ' is equivalent to the betting capital K_t(μ) being a test martingale for every predictable λ; supermartingale-based sequences are conservative because Ville is tight only for martingales [waudbysmithEstimatingMeansBounded2020, Props 2–3, Secs 3.3, 4.1]; see [betting-confidence-sequences](betting-confidence-sequences.md). Extended nonintegrable supermartingales such as Lai's flat-mixture t-statistic process, needing the extended Ville inequality and a starting time; scale-invariant likelihood ratios are martingales on the scale-invariant filtration [wangAnytimevalidTtestsConfidence2023, Sec. 2.3, Lemma 4.5, Thm 4.7]. Power-one test martingales from the span condition [zhangExistencePowerfulPvalues2023, Cor. 7.1]. Predictable conic-combination supermartingales for constraint nulls [larssonTestingHypothesesGenerated2025, Sec. 10].
- Every test supermartingale is a product of sequential e-values E_t = M_t/M_{t−1} and conversely; from any anytime-valid test the martingale P(∃j : ψ_j = 1 | F_i)/P(∃j : ψ_j = 1) recovers or improves it [fischerAdmissibleOnlineClosed2024, eq. 10, Fact 1]. Running products of conditional e-values for invariance nulls reduce to invariance under the compact stabiliser of the past [koningMeasuringEvidenceExchangeability2023, Prop. 3, Lemma 4]. Sub-exponential supermartingale with predictable bounds for lower-bounded variables [choeComparingSequentialForecasters2021, Prop. 1]. Lag-1 products with adapted λ_t are nonnegative supermartingales under conditional forecast dominance; lag-h processes average h supermartingales in sub-filtrations [henziValidSequentialInference2021, Prop. 3.4].

## Variants and related concepts
- [villes-inequality](villes-inequality.md), the inequality that makes them tests.
- [testing-by-betting](testing-by-betting.md), the interpretation.
- [optional-continuation](optional-continuation.md).

## Sources
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — definition, domination result, mixture and plug-in martingales.
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — products of conditional e-variables, filtrations.
- [wassermanUniversalInference2020](../sources/wassermanUniversalInference2020.md) — nonanticipating likelihood-ratio martingale.
- [villeEtudeCritiqueNotion1939](../sources/villeEtudeCritiqueNotion1939.md) — the original definition and theorems.
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md) — simple and composite test martingales.
- [vovkEvaluesCalibrationCombination2021](../sources/vovkEvaluesCalibrationCombination2021.md), [shaferTestingBettingStrategy2021](../sources/shaferTestingBettingStrategy2021.md) — sequential e-values, round-by-round bets.
- [howardTimeuniformNonparametricNonasymptotic2021](../sources/howardTimeuniformNonparametricNonasymptotic2021.md) — nonparametric supermartingales.
- [grunwaldOptimalEValuesExponential2024](../sources/grunwaldOptimalEValuesExponential2024.md), [koolenLogoptimalAnytimevalidEvalues2022](../sources/koolenLogoptimalAnytimevalidEvalues2022.md), [terschureAnytimevalidLogrankTest2024](../sources/terschureAnytimevalidLogrankTest2024.md) — products of simple e-variables, survival martingale.
- [ramdasAdmissibleAnytimevalidSequential2022](../sources/ramdasAdmissibleAnytimevalidSequential2022.md) — admissibility and symmetry.
- [koolenGeneralisationVilleInequality2025](../sources/koolenGeneralisationVilleInequality2025.md), [perezortizEstatisticsGroupInvariance2024](../sources/perezortizEstatisticsGroupInvariance2024.md), [koningAnytimeValidityFree2026](../sources/koningAnytimeValidityFree2026.md), [sahaNonpartitionedEdetectorsNonparametric2026](../sources/sahaNonpartitionedEdetectorsNonparametric2026.md), [shinEdetectorsNonparametricFramework2023](../sources/shinEdetectorsNonparametricFramework2023.md) — instances.
- [ramdasTestingExchangeabilityForkconvexity2021](../sources/ramdasTestingExchangeabilityForkconvexity2021.md), [rufCompositeGeneralizationVille2022](../sources/rufCompositeGeneralizationVille2022.md), [waudbysmithEstimatingMeansBounded2020](../sources/waudbysmithEstimatingMeansBounded2020.md), [wangAnytimevalidTtestsConfidence2023](../sources/wangAnytimevalidTtestsConfidence2023.md), [zhangExistencePowerfulPvalues2023](../sources/zhangExistencePowerfulPvalues2023.md), [larssonTestingHypothesesGenerated2025](../sources/larssonTestingHypothesesGenerated2025.md) — batch-4 contributions.
- [fischerAdmissibleOnlineClosed2024](../sources/fischerAdmissibleOnlineClosed2024.md), [koningMeasuringEvidenceExchangeability2023](../sources/koningMeasuringEvidenceExchangeability2023.md), [choeComparingSequentialForecasters2021](../sources/choeComparingSequentialForecasters2021.md), [henziValidSequentialInference2021](../sources/henziValidSequentialInference2021.md) — batch-4 wave-2 contributions.

## Disagreements / open issues
- None recorded.
