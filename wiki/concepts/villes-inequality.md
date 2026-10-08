---
slug: villes-inequality
title: Ville's inequality
sources: 3
updated: 2026-10-08
---

# Ville's inequality

## Definition
For a nonnegative supermartingale (M_t) with M_0 ≤ 1 under P, P(∃t : M_t ≥ 1/α) ≤ α; equivalently P(M_τ ≥ 1/α) ≤ α at every stopping time τ [ramdasHypothesisTestingEvalues2025, Fact 7.6]. It is the time-uniform Markov inequality and the single tool that upgrades a fixed-sample e-value test into an anytime-valid one [wassermanUniversalInference2020, Thm 9; grunwaldSafeTesting2024, Cor. 1]. Grünwald, de Heide and Koolen call the resulting continuation guarantee "Ville–Robbins" and trace it to Ville 1939, Robbins and Lai [grunwaldSafeTesting2024, Sec. 7].

## Key results
- Three equivalent forms, including a conditional version, and the SPRT thresholds γ_0 = β, γ_1 = 1/α as a corollary [ramdasHypothesisTestingEvalues2025, Sec. 7.2].
- Defines safety under optional continuation and optional stopping [grunwaldSafeTesting2024, Sec. 5]; see [optional-continuation](optional-continuation.md), [optional-stopping](optional-stopping.md).
- Gives anytime p-values and confidence sequences from an e-process [wassermanUniversalInference2020, Thms 10–11]; see [confidence-sets-and-sequences](confidence-sets-and-sequences.md).
- Tightness and the necessity of nonnegative martingales for admissible anytime-valid inference are cited to Ramdas, Ruf, Larsson and Koolen 2020 [ramdasHypothesisTestingEvalues2025, Chapter 7 note].

## Variants and related concepts
- [e-process](e-process.md), [test-martingale](test-martingale.md).

## Sources
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — statement, forms, SPRT corollary, p-processes.
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — Ville–Robbins, safety definitions, history.
- [wassermanUniversalInference2020](../sources/wassermanUniversalInference2020.md) — use for the sequential split LRT.

## Disagreements / open issues
- None recorded.
