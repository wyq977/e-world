---
slug: bayes-factor-e-variable
title: Bayes factors as e-variables, and the safe t-test
sources: 3
updated: 2026-10-08
---

# Bayes factors as e-variables, and the safe t-test

## Definition
A Bayes factor with the null in the denominator is an [e-variable](e-variable.md) whenever the null is simple, for any prior on the alternative [grunwaldSafeTesting2024, eq. 6]. For composite nulls it is an e-variable only for one particular prior on the null, the one induced by the [reverse-information-projection](reverse-information-projection.md); then it is the GRO e-variable [grunwaldSafeTesting2024, Cor. 2]. In group-invariant nuisance settings the right-Haar (improper) prior produces an exact e-variable, which is the basis of the safe t-test [grunwaldSafeTesting2024, Sec. 4.3]. The book treats the same connection through the [numeraire](numeraire.md) [ramdasHypothesisTestingEvalues2025, Sec. 6.6].

## Key results
- Safe t-test: the scale-free statistic V = Y/|Y_1| makes the right-Haar (1/σ) Bayes factor, equivalently a noncentral-t density ratio, an exact e-variable; Theorem 2 (from Pérez-Ortiz et al.) shows it is GROW for any effect-size prior with a (2+ε)-th moment [grunwaldSafeTesting2024, eqs 28–30, Thm 2, App. B.3].
- The one-observation t-test e-variable is nontrivial, and the t-test illustrates mixture methods [ramdasHypothesisTestingEvalues2025, Example 3.24, Example 13.2].
- The conditional e-variable for Gaussian location coincides with the right-Haar Bayes factor [haoEValuesExponentialFamilies2025, Remark 6, eq. 2.24]; see [exponential-family-e-values](exponential-family-e-values.md).
- Bayesian updating is a special case of optional continuation, and a Bayesian posterior corresponds to sequential application of a conditional e-variable [grunwaldSafeTesting2024, Example 1, Example 8].
- The filtration of the t-test e-variable is coarsened, so stopping rules must be adapted to it for optional stopping to be safe [grunwaldSafeTesting2024, Sec. 5]; see [optional-stopping](optional-stopping.md).
- Safe Testing claims e-values reconcile Neyman–Pearson error control, Fisherian evidence and Jeffreys' Bayes factors with matched priors [grunwaldSafeTesting2024, Sec. 9].

## Variants and related concepts
- [gro-criterion](gro-criterion.md), [mixture-and-plug-in-methods](mixture-and-plug-in-methods.md).

## Sources
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — Bayes-factor interpretation, Theorem 2, t-test, discussion by Mulder, Bon and Robert, Dickhaus.
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — numeraire and Bayes factors, t-test examples.
- [haoEValuesExponentialFamilies2025](../sources/haoEValuesExponentialFamilies2025.md) — Haar Bayes factor equals the conditional e-variable.

## Disagreements / open issues
- Cauchy (Jeffreys) prior case for the t-test is open [grunwaldSafeTesting2024, Sec. 4.3].
- Hendriksen, de Heide and Grünwald 2021 on optional stopping with Bayes factors underpins the coarser-filtration e-process property and is not in the bib.
