---
slug: test-martingale
title: Test martingale
sources: 3
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

## Variants and related concepts
- [villes-inequality](villes-inequality.md), the inequality that makes them tests.
- [testing-by-betting](testing-by-betting.md), the interpretation.
- [optional-continuation](optional-continuation.md).

## Sources
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — definition, domination result, mixture and plug-in martingales.
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — products of conditional e-variables, filtrations.
- [wassermanUniversalInference2020](../sources/wassermanUniversalInference2020.md) — nonanticipating likelihood-ratio martingale.

## Disagreements / open issues
- None recorded.
