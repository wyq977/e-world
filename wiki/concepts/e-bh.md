---
slug: e-bh
title: e-BH, compound e-values and multiple testing
sources: 1
updated: 2026-10-08
---

# e-BH, compound e-values and multiple testing

## Definition
The e-Benjamini–Hochberg procedure rejects the k* hypotheses with the largest e-values, where k* = max{k : k e_[k] / K ≥ 1/α} [ramdasHypothesisTestingEvalues2025, Definition 9.8]. It controls the false discovery rate under arbitrary dependence, with a post-hoc guarantee in α [Thm 9.11]. A compound e-value is a vector (E_1, …, E_K) with Σ_{k : P ∈ P_k} E_P[E_k] ≤ K for every P, tight if equality holds [Definition 9.1]; every FDR-controlling procedure is e-BH applied to some compound e-values [Thms 9.18–9.19].

## Key results
- Self-consistency, boosting, universality and minimally adaptive e-BH [ramdasHypothesisTestingEvalues2025, Def. 9.9, Thm 9.13, Thm 9.19, Sec. 9.4].
- Randomised e-BH via stochastic rounding (rounding an e-value onto a grid while preserving its expectation) rejects weakly more; closed e-BH strictly improves e-BH through an FDR closure principle [ramdasHypothesisTestingEvalues2025, Prop. 9.24, Thms 9.27, 9.29, Def. 9.31, Thms 9.32–9.36].
- Log-optimal simple separable compound e-values; approximate and asymptotic compound e- and p-values [ramdasHypothesisTestingEvalues2025, Thm 9.21, Defs 10.13, 10.17, 10.22, Thm 10.24].
- e-weighted BH and e-values as unnormalised weights [ramdasHypothesisTestingEvalues2025, Thm 11.10].
- e-BY controls the false coverage rate for e-confidence intervals [ramdasHypothesisTestingEvalues2025, Thm 13.7]; see [confidence-sets-and-sequences](confidence-sets-and-sequences.md).
- Post-hoc choice of α in e-BH extends to general e-closure procedures [ramdasHypothesisTestingEvalues2025, Thm 9.10 as cited by later work]; see [post-hoc-validity](post-hoc-validity.md).

## Variants and related concepts
- [e-merging](e-merging.md), [post-hoc-validity](post-hoc-validity.md).

## Sources
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — Chapters 9, 10, 11, 13.

## Disagreements / open issues
- The primary papers (Wang and Ramdas 2022 on e-BH; Ignatiadis, Wang and Ramdas 2024 on weights and compound e-values; Xu, Fischer and Ramdas 2025 on closed e-BH; Xu, Wang and Ramdas 2024 on e-BY) are candidates, not yet in the bib.
