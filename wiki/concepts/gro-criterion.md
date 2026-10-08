---
slug: gro-criterion
title: GRO, GROW, REGROW and log-optimality
sources: 3
updated: 2026-10-08
---

# GRO, GROW, REGROW and log-optimality

## Definition
Growth-rate optimality (GRO) chooses, for a given alternative Q, the [e-variable](e-variable.md) maximising [e-power](e-power.md) E_Q[log E], the analogue of Neyman–Pearson power for e-values [grunwaldSafeTesting2024, Sec. 2, eq. 11]. The book calls the same object log-optimal: E is log-optimal against Q if E_Q[log(E′/E)] ≤ 0 for every e-variable E′ [ramdasHypothesisTestingEvalues2025, Definition 3.18]. GROW is the maximin version over a composite alternative, sup_E inf_θ E_θ[log E] [grunwaldSafeTesting2024, Sec. 3], and REGROW maximises worst-case growth relative to the oracle GRO rate, which is needed when GROW trivialises (nested models) or nuisance parameters are present [grunwaldSafeTesting2024, Sec. 4].

## Key results
- Theorem 1 of Safe Testing: if Q has finite KL to the convex hull of the null, the GRO e-variable exists, is essentially unique, equals q/p*_0 with P*_0 the [reverse-information-projection](reverse-information-projection.md), and its growth rate is D(Q ‖ P*_0); it is the only e-variable of likelihood-ratio form with q on top, so GRO e-variables are Bayes factors with a forced null prior [grunwaldSafeTesting2024, Thm 1, Cor. 2].
- Without regularity conditions the log-optimal e-variable always exists and is unique; it is the [numeraire](numeraire.md) [ramdasHypothesisTestingEvalues2025, Prop. 3.19, Thm 6.4].
- Simple vs simple: the likelihood ratio is log-optimal with e-power KL(Q, P) [ramdasHypothesisTestingEvalues2025, Thm 3.20]; conditional and process-level log-optimality [Prop. 3.22, Thm 7.11].
- GROW under monotone likelihood ratio with a minimum effect size is the point-vs-point ratio p_{δ+}/p_{δ−} [grunwaldSafeTesting2024, Prop. 3, Example 4]; for a simple null REGROW is the redundancy–capacity problem, the prior tends to Jeffreys' and regret is (d/2) log n + O(1) [Example 5].
- Nuisance recipe: REGROW away the nuisance for each effect size, then GROW over effect sizes; in group-invariant settings GROW = REGROW, for the 2×2 table they differ [grunwaldSafeTesting2024, Sec. 4.2–4.3, Examples 6–7]; see [bayes-factor-e-variable](bayes-factor-e-variable.md).
- Uniqueness corollary: at most one prior W_0 on the null makes q/p_{W_0} an e-variable, and then it is GRO [haoEValuesExponentialFamilies2025, Lemma 1].
- Asymptotic log-optimality of mixture and plug-in methods [ramdasHypothesisTestingEvalues2025, Sec. 3.7, Def. 7.13, Prop. 7.14]; see [mixture-and-plug-in-methods](mixture-and-plug-in-methods.md).
- Quantitative e-power gaps between GRO and its competitors for exponential families [haoEValuesExponentialFamilies2025, Cors 1–4]; see [exponential-family-e-values](exponential-family-e-values.md).

## Variants and related concepts
- [numeraire](numeraire.md), the assumption-free form.
- [e-power](e-power.md).

## Sources
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — GRO, GROW, REGROW, Theorem 1 in four versions, nuisance recipe, sample sizes.
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — log-optimality, existence without assumptions, asymptotic log-optimality.
- [haoEValuesExponentialFamilies2025](../sources/haoEValuesExponentialFamilies2025.md) — GRO as yardstick, e-power gaps, uniqueness lemma.

## Disagreements / open issues
- Ly's discussion: GROW point priors leave δ+ inside anytime-valid confidence intervals forever; the authors answer with REGROW or nonlocal priors [grunwaldSafeTesting2024, discussion and reply].
- Whether the right-Haar t-test Bayes factor is GROW under Jeffreys' Cauchy prior (no second moment) is open [grunwaldSafeTesting2024, Sec. 4.3].
- Which GRO criteria admit sequentially decomposable specifications is open [grunwaldSafeTesting2024, eq. 31]; see [optional-stopping](optional-stopping.md).
