---
slug: e-process
title: E-process
sources: 4
updated: 2026-10-08
---

# E-process

## Definition
An e-process is an adapted nonnegative process (E_t) with E_P[E_τ] ≤ 1 for every stopping time τ and every null P; equivalently, for each null P it is dominated by a test supermartingale that may depend on P [ramdasHypothesisTestingEvalues2025, Definition 7.3]. Its value at any stopping time is an [e-variable](e-variable.md). Every test supermartingale is an e-process, but useful e-processes exist that are not supermartingales in the natural filtration, for instance for exchangeability [grunwaldSafeTesting2024, remark after Prop. 2; ramdasHypothesisTestingEvalues2025, Chapter 7 note]. The running-MLE universal inference statistic is the paradigmatic example: it is dominated by a likelihood-ratio martingale but re-maximises its denominator at every time [wassermanUniversalInference2020, Sec. 7, eq. 18].

## Key results
- Ville's inequality turns an e-process into a sequential test, and every level-α sequential test is a thresholded e-process [ramdasHypothesisTestingEvalues2025, Fact 7.6, Prop. 7.8]; see [villes-inequality](villes-inequality.md).
- Running products of conditional e-variables (sequential e-values, E_P[E_t | F_{t−1}] ≤ 1) are test supermartingales, hence e-processes [grunwaldSafeTesting2024, Prop. 2, Def. 1; ramdasHypothesisTestingEvalues2025, Def. 7.19, Prop. 7.20].
- Optional continuation is multiplication by a new e-process at a stopping time [ramdasHypothesisTestingEvalues2025, Prop. 7.9]; see [optional-continuation](optional-continuation.md).
- The likelihood-ratio process is log-optimal at every stopping time [ramdasHypothesisTestingEvalues2025, Thm 7.11]; empirically adaptive e-processes are asymptotically log-optimal [Thm 7.22].
- Anytime-valid p-values: p_t = 1/E_t or the running minimum satisfies P(p_T ≤ x) ≤ x at arbitrary random times T, and the first crossing times coincide with the e-process test [wassermanUniversalInference2020, Thm 10; ramdasHypothesisTestingEvalues2025, Def. 7.10].
- Time-mixture e-processes can be built from a single e-variable [ramdasHypothesisTestingEvalues2025, Prop. 7.23].
- Not every good e-variable extends to an e-process: the conditional and RIPr e-variables for exponential families are generally not e-processes because the optimal prior depends on n, although they are in Gaussian and Poisson k-sample settings [haoEValuesExponentialFamilies2025, Prop. 7, Prop. 1, Appendix E].
- Sequential e-values must be merged by martingale merging, not plain averaging [ramdasHypothesisTestingEvalues2025, Thm 8.12]; see [e-merging](e-merging.md).

## Variants and related concepts
- [test-martingale](test-martingale.md), the special case most constructions use.
- [confidence-sets-and-sequences](confidence-sets-and-sequences.md), the dual estimation object.
- [optional-stopping](optional-stopping.md), when stopping inside a study is safe.

## Sources
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — definition and equivalence, sequential tests, continuation, log-optimality, sequential e-values (Chapter 7).
- [wassermanUniversalInference2020](../sources/wassermanUniversalInference2020.md) — running-MLE e-process, anytime p-values, confidence sequences (Thms 9–11).
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — products of conditional e-variables, limitation of the product construction.
- [haoEValuesExponentialFamilies2025](../sources/haoEValuesExponentialFamilies2025.md) — which exponential family e-variables are e-processes.

## Disagreements / open issues
- "Approximate optional stopping" for e-variables that are not e-processes is conjectured, possibly via time-uniform central limit theory or coarser filtrations [haoEValuesExponentialFamilies2025, Sec. 7].
