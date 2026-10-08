---
slug: e-power
title: E-power and sample size
sources: 9
updated: 2026-10-08
---

# E-power and sample size

## Definition
The e-power of an [e-variable](e-variable.md) E against an alternative Q is E_Q[log E], the expected log growth of wealth; it plays the role that power plays for Neyman–Pearson tests and is the quantity that the GRO criterion maximises [ramdasHypothesisTestingEvalues2025, Definition 3.11; grunwaldSafeTesting2024, Sec. 2.1]. The term was coined in the e-backtesting literature and popularised by Vovk and Wang [haoEValuesExponentialFamilies2025, Sec. 1; grunwaldSafeTesting2024, discussion]. For misspecified data R ≠ Q the relevant divergence is the generalised KL D_R(Q‖P) [haoEValuesExponentialFamilies2025, eq. 1.14].

## Key results
- Positive e-power implies "powered" (E_Q[E] > 1) but not conversely; E_Q[X] > 1 iff some shrinkage 1 − λ + λX has positive e-power [ramdasHypothesisTestingEvalues2025, Thm 3.14, Prop. 3.12].
- Axiomatic characterisation: e-power is the only quality criterion consistent with multiplication and asymptotic consistency [ramdasHypothesisTestingEvalues2025, Thm 3.28].
- Powered tests, powered e-variables and powered p-variables exist under exactly the same conditions [ramdasHypothesisTestingEvalues2025, Thm 3.9].
- For simple P vs Q the maximal e-power is KL(Q, P), attained by the likelihood ratio [ramdasHypothesisTestingEvalues2025, Thm 3.20].
- E-power expansions for exponential families: conditional e-variable loses only O(1) or o(1) relative to the optimum, universal inference loses (d/2) log n with a composite alternative and d_rp/2 with a simple one [haoEValuesExponentialFamilies2025, Thms 1–4, Cors 1–4]; see [exponential-family-e-values](exponential-family-e-values.md).
- Sample size planning: a target growth L needs n ≈ L / D(P_δ ‖ P_0); fixed-n GRO tests need about c_α times the Neyman–Pearson sample size with c_0.05 ≈ 2.2 and c_0.01 ≈ 1.7; under optional stopping the expected n for 80% power is 4.97/δ² against 6.18/δ² for NP, but the worst case is 8.59/δ² [grunwaldSafeTesting2024, Sec. 6, eq. 32, App. B.4].
- E-power can be infinite or minus infinity in ways that mislead [ramdasHypothesisTestingEvalues2025, Examples 3.16, 7.25, 7.26; grunwaldSafeTesting2024, discussion by Wang].
- Shafer's implied target S* = exp(E_Q[ln S]) = exp(E_P[S ln S]) is e-power exponentiated; it replaces power, is fixed by P and S alone, and always coheres with the realised score where level, p-value and power do not; worked examples with P = N(0,100) [shaferTestingBettingStrategy2021, Secs 2.3–2.4, Table 1]. The reply proposes it for pre-accepting studies.
- Koolen and Grünwald adopt the implied target as the objective under optional stopping; explicit values (n/2) ln((μ²+ρ²)/ρ²) for the Gaussian scale case and 3.466 vs 3.072 for the RIPr likelihood ratio vs the maximum-likelihood plug-in at n = 10 [koolenLogoptimalAnytimevalidEvalues2022, Secs 2.2, 4.3].
- The survey justifies the log via Kelly compounding, Breiman's exponent and hitting-time optimality by Wald's identity, and frames type-II error as low e-power; at fixed n GRO loses power to UMP tests and sequences are 1.5–2× wider, but expected stopping times under optional stopping are about the same or smaller [ramdasGametheoreticStatisticsSafe2023, Sec. 3.1, App. B].
- GROW approximately minimises the worst-case expected number of events to rejection, E[N_τ] ≈ ln(1/α)/E[ln R]; survival data need a larger design maximum but equal or fewer mean events than the fixed-sample logrank test [terschureAnytimevalidLogrankTest2024, App. A.1, Sec. 7, Fig. 4].
- Expected log growth and worst-case regret used to tune the Beta(γ, γ) prior to γ ≈ 0.18 and to compare with Fisher's exact and chi-square tests at 80% power [turnerGenericEvariablesExact2024, eqs 2.5, 2.7, Figs 2–5]; growth rate of a simple e-variable equals inf over the convex hull of KL [grunwaldOptimalEValuesExponential2024, eq. 1.5].

## Variants and related concepts
- [gro-criterion](gro-criterion.md), optimising e-power.
- [numeraire](numeraire.md).

## Sources
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — definition, axioms, existence of powered e-variables (Chapter 3).
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — justification of the log, sample sizes, critique in Sec. 8 and the discussion.
- [haoEValuesExponentialFamilies2025](../sources/haoEValuesExponentialFamilies2025.md) — quantitative e-power comparisons.
- [shaferTestingBettingStrategy2021](../sources/shaferTestingBettingStrategy2021.md) — implied target.
- [koolenLogoptimalAnytimevalidEvalues2022](../sources/koolenLogoptimalAnytimevalidEvalues2022.md) — implied target under optional stopping.
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md) — justification of the log, costs at fixed n.
- [terschureAnytimevalidLogrankTest2024](../sources/terschureAnytimevalidLogrankTest2024.md), [turnerGenericEvariablesExact2024](../sources/turnerGenericEvariablesExact2024.md), [grunwaldOptimalEValuesExponential2024](../sources/grunwaldOptimalEValuesExponential2024.md) — applied comparisons.

## Disagreements / open issues
- Whether log growth is the right objective is contested: the Safe Testing authors concede GRO rests on independence and bounded variance of log E and that it fails to explain stitching rates [grunwaldSafeTesting2024, Sec. 8]; Wang's Pareto counterexamples show rejection probability and e-power can point in opposite directions.
