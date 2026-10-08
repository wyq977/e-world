---
slug: calibrator
title: Calibrators between p-values and e-values
sources: 6
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
- Full characterisation: p-to-e calibrators are the decreasing f with ∫f ≤ 1, admissible iff upper semicontinuous with f(0) = ∞ and ∫f = 1; the single admissible e-to-p calibrator is min(1, 1/e); explicit families κp^{κ−1}, the mixture (1 − p + p ln p)/(p(−ln p)²), and the incomplete-gamma family; the Vovk–Sellke bound is not a valid e-value [vovkEvaluesCalibrationCombination2021, Props 2.1–2.2, eqs 1–2, App. B].
- Shafer's 1/√p − 1: 1/p has infinite null expectation and must be shrunk to a payoff with expectation one; the choice is 'fundamentally arbitrary' but maps 0.10/0.05/0.01/0.001 to 2.2/3.5/9.0/30.6 and agrees with Jeffreys; any shrinking rule implies a heavy-tailed alternative; −ln p is valid, −log₂ p is not [shaferTestingBettingStrategy2021, Sec. 3, eq. 6, Example 4, reply].
- Calibrators preserve family-wise validity in both directions; cross-merging: average e-values then invert, or calibrate p-values then average [vovkEvaluesCalibrationCombination2021, Remark A.1, App. G].
- Survey uses: turn any confidence interval into an e-confidence interval at level f^{−1}(1/α), lookback calibrators, calibrate per-study p-values before multiplying [ramdasGametheoreticStatisticsSafe2023, Secs 2.4, 6.1, 6.3].
- Lottery-ticket argument: reporting p is claiming the payout of a ticket one never bought; calibration makes the p-value an honest bet; the authors concede that once p-values are calibrated, e-values do not need more data [grunwaldAuthorsReplyDiscussion2024, Sec. 1].

## Variants and related concepts
- [e-variable](e-variable.md), [e-merging](e-merging.md).

## Sources
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — Chapter 2, Chapter 15, Thm 12.15.
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — Sec. 7 and discussion.
- [vovkEvaluesCalibrationCombination2021](../sources/vovkEvaluesCalibrationCombination2021.md) — primary source for calibrators.
- [shaferTestingBettingStrategy2021](../sources/shaferTestingBettingStrategy2021.md) — the 1/√p − 1 calibrator and its defence.
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md) — uses.
- [grunwaldAuthorsReplyDiscussion2024](../sources/grunwaldAuthorsReplyDiscussion2024.md) — lottery-ticket argument.

## Disagreements / open issues
- None recorded.
