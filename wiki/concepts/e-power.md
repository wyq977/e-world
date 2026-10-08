---
slug: e-power
title: E-power and sample size
sources: 3
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

## Variants and related concepts
- [gro-criterion](gro-criterion.md), optimising e-power.
- [numeraire](numeraire.md).

## Sources
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — definition, axioms, existence of powered e-variables (Chapter 3).
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — justification of the log, sample sizes, critique in Sec. 8 and the discussion.
- [haoEValuesExponentialFamilies2025](../sources/haoEValuesExponentialFamilies2025.md) — quantitative e-power comparisons.

## Disagreements / open issues
- Whether log growth is the right objective is contested: the Safe Testing authors concede GRO rests on independence and bounded variance of log E and that it fails to explain stitching rates [grunwaldSafeTesting2024, Sec. 8]; Wang's Pareto counterexamples show rejection probability and e-power can point in opposite directions.
