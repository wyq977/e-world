---
slug: calibrator
title: Calibrators between p-values and e-values
sources: 2
updated: 2026-10-08
---

# Calibrators between p-values and e-values

## Definition
A p-to-e calibrator is a decreasing function f with ∫_0^1 f ≤ 1, so that f(P) is an [e-variable](e-variable.md) for any p-variable P; an e-to-p calibrator maps e-values to p-values, and e ↦ min(1, 1/e) is the only admissible one [ramdasHypothesisTestingEvalues2025, Definition 2.3, Props 2.4–2.5]. Every e-variable is a calibrated exact p-variable [Prop. 2.7]. Shafer's calibrator 1/√p − 1 maps p = 0.05 to 3.47 and needs p ≤ 0.0023 to reach an e-value of 20 [grunwaldSafeTesting2024, Sec. 7].

## Key results
- Explicit calibrator families and the log-optimal calibrator E_P[dQ/dP | P] [ramdasHypothesisTestingEvalues2025, eqs 2.1–2.5, Cor. 3.23].
- Randomised e-to-p calibrator U/E and conditional calibrators on subclasses [ramdasHypothesisTestingEvalues2025, Cor. 2.10, Thm 11.5, Chapter 15].
- Calibrators are the route for admissible p-merging under arbitrary dependence [ramdasHypothesisTestingEvalues2025, Thm 12.15]; see [e-merging](e-merging.md).
- Cost of calibrating: reaching 80% power through a calibrated p-value needs about 3.0 times the Neyman–Pearson sample size, against 2.2 for GROW e-variables [grunwaldSafeTesting2024, Sec. 7].
- Shafer's discussion frames p-values as dishonest bets and the authors reply with the lottery-ticket argument [grunwaldSafeTesting2024, discussion, reply Sec. 2].

## Variants and related concepts
- [e-variable](e-variable.md), [e-merging](e-merging.md).

## Sources
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — Chapter 2, Chapter 15, Thm 12.15.
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — Sec. 7 and discussion.

## Disagreements / open issues
- None recorded.
