---
slug: villes-inequality
title: Ville's inequality
sources: 10
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
- The original: Chapter V Theorem 1, inequality (15), Pr{sup_n s_n ≥ λ} ≤ 1/λ for a nonnegative martingale with s_0 = 1, proved by freezing the martingale at first passage; an earlier instance of the stopped-process argument is in Chapter II; the continuous-time version can fail without path regularity [villeEtudeCritiqueNotion1939, Ch. V, p. 84, p. 98].
- Ville's theorem (P(A) < ε iff some test martingale exceeds 1/ε on A), its composite version requiring e-processes, equality for continuous paths, overshoot as the discrete-time looseness, and the extension to nonintegrable supermartingales [ramdasGametheoreticStatisticsSafe2023, Sec. 2.5, eqs 8–10].
- Applied to exponential supermartingales it yields only linear boundaries; curved boundaries need mixtures or a union bound over epochs [howardTimeuniformNonparametricNonasymptotic2021, Lemmas 1–2, Thm 1]; see [confidence-sequence-boundaries](confidence-sequence-boundaries.md).
- Used to sharpen the sequential-e-value-to-p merger to the running minimum [vovkEvaluesCalibrationCombination2021, App. G]; the single safety guarantee in the k-sample, contingency-table and logrank papers [turnerGenericEvariablesExact2024, eq. 2.4; turnerExactAnytimevalidConfidence2023, Sec. 3; terschureAnytimevalidLogrankTest2024, Prop. 3.1].

## Variants and related concepts
- [e-process](e-process.md), [test-martingale](test-martingale.md).

## Sources
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — statement, forms, SPRT corollary, p-processes.
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — Ville–Robbins, safety definitions, history.
- [wassermanUniversalInference2020](../sources/wassermanUniversalInference2020.md) — use for the sequential split LRT.
- [villeEtudeCritiqueNotion1939](../sources/villeEtudeCritiqueNotion1939.md) — original statement and proof.
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md) — Ville's theorem and composite forms.
- [howardTimeuniformNonparametricNonasymptotic2021](../sources/howardTimeuniformNonparametricNonasymptotic2021.md) — boundaries from Ville.
- [vovkEvaluesCalibrationCombination2021](../sources/vovkEvaluesCalibrationCombination2021.md), [turnerGenericEvariablesExact2024](../sources/turnerGenericEvariablesExact2024.md), [turnerExactAnytimevalidConfidence2023](../sources/turnerExactAnytimevalidConfidence2023.md), [terschureAnytimevalidLogrankTest2024](../sources/terschureAnytimevalidLogrankTest2024.md) — applications.

## Disagreements / open issues
- None recorded.
