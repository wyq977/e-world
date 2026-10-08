---
slug: e-process
title: E-process
sources: 16
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
- The survey fixes both definitions (domination by a P-dependent test-martingale family, eq. 6; E_P[E_τ] ≤ 1 at all τ), their equivalence, the admissible form E_t = inf_P M^P_t and the parallel-games interpretation; tests and anytime p-values are declared 'secondary and derivative' of e-processes [ramdasGametheoreticStatisticsSafe2023, Sec. 2.4, eq. 7].
- Existence hierarchy: nulls with test martingales without a reference measure, with supermartingales only, with e-processes only (exchangeability, log-concavity via universal inference), and with reverse submartingales; the composite Ville theorem needs e-processes [ramdasGametheoreticStatisticsSafe2023, Sec. 5, Sec. 8.2.1].
- Koolen and Grünwald's 'anytime-valid e-value' (E_{P^τ}[E] ≤ 1 for every randomised stopping time) is the same notion; every such process is an infimum of test martingales, one per null element, and the numerical example exhibits a log-optimal one that drops below one deterministically and recovers, hence is not a supermartingale [koolenLogoptimalAnytimevalidEvalues2022, Def. 1, Lemma 4, Sec. 4.5].
- Always-valid p-values satisfy equivalent uniform, stopping-time and random-time formulations [howardTimeuniformNonparametricNonasymptotic2021, Lemma 3].
- Block-structured e-processes with past-dependent but pre-fixed block sizes, evaluated only at complete blocks [turnerGenericEvariablesExact2024, Sec. 3.1]; continuous-time e-processes indexed by events for survival data [terschureAnytimevalidLogrankTest2024, Prop. 3.1, Cor. A.2].
- Six equivalent definitions (stopping times with lim sup or lim inf, finite or bounded stopping times, domination by a nonnegative martingale or supermartingale for each null) proved via Snell envelopes and Doob decomposition; e-processes are not closed under running maxima, unlike p-processes [ramdasAdmissibleAnytimevalidSequential2022, Lemma 6, Lemma 3].
- Admissibility: every e-process is dominated by an essential infimum of pointwise nonnegative martingales, itself an e-process; admissible composite e-processes are such infima with initial value one; under a point null admissible e-processes are exactly nonnegative martingales with E[e_0] = 1; the gap between composite martingales and e-processes is real [ramdasAdmissibleAnytimevalidSequential2022, Prop. 23, Cors 24, 26, 29, Thm 18, Examples 31–32].
- p-processes (always-valid p-values): [0,1]-valued with Q(p_τ ≤ α) ≤ α at every stopping time; admissible ones are closed max-martingales with uniform limit, not ordinary martingales, and initial randomisation is needed for admissibility but ruins e-process tests via overshoot [ramdasAdmissibleAnytimevalidSequential2022, Sec. 4.1, Thm 18, Cor. 21, Example 20, Sec. 8.3].
- Bounded e-processes: every admissible bounded anytime-valid test is the Doob martingale of a terminal test [koningAnytimeValidityFree2026, Prop. 2]; s-delay (restartable, conditionally valid) e-processes and the fact that a weighted sum then infimum is again an e-process [sahaNonpartitionedEdetectorsNonparametric2026, Def. 2.1, Thm 2.3]; e_j-processes started at time j as e-detector building blocks [shinEdetectorsNonparametricFramework2023, Def. 2.5]; e-specifications vs e-processes for e-collections [grunwaldEposterior2023, Sec. 3]; stopped e-processes as e-BH inputs under adaptive stopping [wangFalseDiscoveryRate2021, Secs 7–8]; (T^{M_n}) is an e-process for the invariant filtration but not for the data filtration [perezortizEstatisticsGroupInvariance2024, Prop. 6].

## Variants and related concepts
- [test-martingale](test-martingale.md), the special case most constructions use.
- [confidence-sets-and-sequences](confidence-sets-and-sequences.md), the dual estimation object.
- [optional-stopping](optional-stopping.md), when stopping inside a study is safe.

## Sources
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — definition and equivalence, sequential tests, continuation, log-optimality, sequential e-values (Chapter 7).
- [wassermanUniversalInference2020](../sources/wassermanUniversalInference2020.md) — running-MLE e-process, anytime p-values, confidence sequences (Thms 9–11).
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — products of conditional e-variables, limitation of the product construction.
- [haoEValuesExponentialFamilies2025](../sources/haoEValuesExponentialFamilies2025.md) — which exponential family e-variables are e-processes.
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md) — definitions, equivalence, hierarchy, open problems.
- [koolenLogoptimalAnytimevalidEvalues2022](../sources/koolenLogoptimalAnytimevalidEvalues2022.md) — anytime-valid e-values, infimum representation, non-supermartingale example.
- [howardTimeuniformNonparametricNonasymptotic2021](../sources/howardTimeuniformNonparametricNonasymptotic2021.md) — always-valid p-values, Lemma 3.
- [turnerGenericEvariablesExact2024](../sources/turnerGenericEvariablesExact2024.md), [terschureAnytimevalidLogrankTest2024](../sources/terschureAnytimevalidLogrankTest2024.md) — block and continuous-time instances.
- [ramdasAdmissibleAnytimevalidSequential2022](../sources/ramdasAdmissibleAnytimevalidSequential2022.md) — equivalent definitions, admissibility, p-processes.
- [koningAnytimeValidityFree2026](../sources/koningAnytimeValidityFree2026.md), [sahaNonpartitionedEdetectorsNonparametric2026](../sources/sahaNonpartitionedEdetectorsNonparametric2026.md), [shinEdetectorsNonparametricFramework2023](../sources/shinEdetectorsNonparametricFramework2023.md), [grunwaldEposterior2023](../sources/grunwaldEposterior2023.md), [wangFalseDiscoveryRate2021](../sources/wangFalseDiscoveryRate2021.md), [perezortizEstatisticsGroupInvariance2024](../sources/perezortizEstatisticsGroupInvariance2024.md) — instances.

## Disagreements / open issues
- "Approximate optional stopping" for e-variables that are not e-processes is conjectured, possibly via time-uniform central limit theory or coarser filtrations [haoEValuesExponentialFamilies2025, Sec. 7].
