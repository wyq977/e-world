---
slug: e-merging
title: Merging e-values and p-values
sources: 1
updated: 2026-10-08
---

# Merging e-values and p-values

## Definition
An e-merging function F produces an [e-variable](e-variable.md) F(E_1, …, E_K) from any e-variables, whatever their dependence [ramdasHypothesisTestingEvalues2025, Definition 8.1]. The arithmetic mean essentially dominates every symmetric merger, and the admissible e-merging functions are exactly the weighted arithmetic means, a result of Wang 2025 proved via optimal transport [ramdasHypothesisTestingEvalues2025, Prop. 8.3, Thm 8.4, Lemma 11.1]. Independent or sequential e-values may instead be multiplied; sequential e-values need martingale merging [Thm 8.12].

## Key results
- ie-merging and products for independent e-values, mean–variance trade-off, FWER control by averaging [ramdasHypothesisTestingEvalues2025, Sec. 8.2, Prop. 8.16, Algorithm 8.18].
- p-merging under arbitrary dependence: twice the mean of p-values is a p-value, and every admissible p-merging function is dominated by a calibrate–average–threshold rule, so p-merging goes through e-values [ramdasHypothesisTestingEvalues2025, Props 12.1, 12.4, Thms 12.15, 12.17, 12.18, Table 12.29]; see [calibrator](calibrator.md).
- Exchangeable and randomised p-combinations [ramdasHypothesisTestingEvalues2025, Thms 12.27–12.28].
- Averages of split-LRT statistics are the simplest instance of e-merging under dependence [wassermanUniversalInference2020, Sec. 4]; see [universal-inference](universal-inference.md).

## Variants and related concepts
- [e-bh](e-bh.md), merging for multiple testing rather than a single decision.
- [optional-continuation](optional-continuation.md), merging by multiplication over time.

## Sources
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — Chapters 8, 11, 12.

## Disagreements / open issues
- Primary sources not yet in the bib: Vovk and Wang 2021 is in the bib; Wang 2025 "The only admissible way of merging arbitrary e-values", Vovk, Wang and Wang 2022 on p-merging, and Vovk and Wang 2024 on martingale merging are not.
