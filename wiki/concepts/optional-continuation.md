---
slug: optional-continuation
title: Optional continuation
sources: 2
updated: 2026-10-08
---

# Optional continuation

## Definition
Optional continuation is deciding after each study whether to run another one, with the next e-variable's design (prior, sample size, stopping rule) chosen using everything seen so far, and multiplying the new e-value onto the running product [grunwaldSafeTesting2024, after Cor. 1]. The product is a [test martingale](test-martingale.md) at the study level, so [Ville's inequality](villes-inequality.md) controls type-I error under any continuation rule, including externally imposed or unknowable ones [grunwaldSafeTesting2024, Prop. 2, Cor. 1]. Formally, continuation is multiplication of an [e-process](e-process.md) by a new one at a stopping time [ramdasHypothesisTestingEvalues2025, Prop. 7.9].

## Key results
- Bayesian updating is a special case of optional continuation, the "local perspective" [grunwaldSafeTesting2024, Example 1].
- Continuation (study level, free choice of the next e-variable) and optional stopping (data level) are formally the same Ville–Robbins condition, but stopping inside a study needs extra structure [grunwaldSafeTesting2024, Sec. 5]; see [optional-stopping](optional-stopping.md).
- The authors' reply stresses that continuation across studies, not interim analysis, is the main point of e-values [grunwaldSafeTesting2024, reply Sec. 5].
- Contrast with p-value meta-analysis, which cannot combine results chosen in this way [ramdasHypothesisTestingEvalues2025, Sec. 1.2.1, Sec. 4.3].

## Variants and related concepts
- [e-merging](e-merging.md), for combining without a sequential structure.

## Sources
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — definition, Cor. 1, Example 1, Sec. 5, reply.
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — Sec. 4.3, Prop. 7.9.

## Disagreements / open issues
- Whether conditional e-variables are the right building blocks when e-variable types switch across studies is raised but not settled [grunwaldSafeTesting2024, Sec. 1.3].
