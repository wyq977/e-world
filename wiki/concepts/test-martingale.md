---
slug: test-martingale
title: Test martingale
sources: 11
updated: 2026-10-08
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

## Disagreements / open issues
- None recorded.
