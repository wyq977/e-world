---
slug: test-induction
title: Test induction: anytime validity without e-values
sources: 6
updated: 2026-11-11
---

# Test induction: anytime validity without e-values

## Definition
Given a terminal [0,1]-valued test φ valid at level α for a simple null P and a planned sample size N, its induced sequential test is the Doob martingale φ_n = E_P[φ | F_n]; it is anytime valid and φ_N = φ, so anytime validity costs no power at time N. For a composite null one induces from a family (φ^P) and takes the essential infimum over P [koningAnytimeValidityFree2026, Thm 1, Prop. 3, Thm 2]. It is a backward construction, fixing the target test and conditioning down, as opposed to the forward accumulation of martingale increments in [testing by betting](testing-by-betting.md).

## Key results
- Strong converse: if φ is invalid, φ_τ is invalid for every stopping time [koningAnytimeValidityFree2026, Thm 1].
- Completeness: every admissible anytime-valid bounded sequential test is induced from a single terminal test φ_∞ = lim sup φ_n, so a bounded e-process is a Doob martingale of a terminal test; this needs the uniform integrability that boundedness supplies and does not transfer to [0, ∞]-valued e-values [koningAnytimeValidityFree2026, Prop. 2, Remark 5].
- Closed forms: induced z-test φ′_n = Φ((N^{−1/2} Σ x_i/σ − z_{1−α})/√r_n) with r_n = (N − n)/N, valid for μ ≤ 0; induced t-test via Beta distributions, anytime valid for the full one-sided null, generalising the Grünwald–Koolen sufficient-MLR theorem to any test non-decreasing in the sufficient statistic [koningAnytimeValidityFree2026, Sec. 3, eq. 6, Thm 3, Props 4–5].
- Conditional significance levels: if E_P[φ_2 | φ_1] ≤ φ_1 then φ_2 is valid at α; an anytime-valid test can be aborted at any stopping time σ and continued at conditional level φ_σ; on the e-scale this is multiplying sequential e-values, and pointwise continuation over a family (φ^P) dominates continuing from the infimum [koningAnytimeValidityFree2026, Thms 4–6, Remark 13]; see [optional-continuation](optional-continuation.md).
- Log utility singled out: the likelihood-ratio process is the unique utility-optimal e-value preserved under conditioning, a motivation for the log not relying on independence over time [koningAnytimeValidityFree2026, Thm 7, Prop. 6]; see [gro-criterion](gro-criterion.md).
- SPRT as a limit of Neyman–Pearson: with α_N = exp{−N·D(Q ‖ P)}, induced NP tests on the e-scale converge almost surely to the likelihood ratio at every n, strengthening Breiman 1961 [koningAnytimeValidityFree2026, Thm 8].
- Motivating numbers for N(μ, 1), μ = 0 vs 0.3, N = 100: z-test power 91%, oracle SPRT 79% (84% randomised), running-MLE SPRT 47% [koningAnytimeValidityFree2026, Sec. 1].
- Precursors: stochastic curtailment and conditional power (Lan, Simon, Halperin 1982; Müller and Schäfer 2004) [koningAnytimeValidityFree2026, Sec. 1.4]; see [martingale-history](martingale-history.md).
- Per-orbit Doob-martingale induction from a terminal orbit-wise optimal e-value, converging to the terminal e-value once the orbit is measurable; on a single orbit after an inversion kernel this is exactly Koning–van Meer induction [koningMeasuringEvidenceExchangeability2023, Sec. 5.3, Sec. 9.1].
- The conditional rejection probability principle of Müller and Schäfer, A^P = E_P[φ | D] for a prespecified fixed-sample or group-sequential test φ at a data-chosen interim time, is the same construction, and conditional error functions in general are conditional significance levels; the identification with Koning and van Meer is made explicitly [brannathAnytimevalidTestingEvalues2026a, Example 3, Sec. 5.2]. The conditional expectation is defined only up to null sets, and when the second-stage design is chosen after seeing the data a version chosen then can be gamed; a regression model for the second-stage data given interim data and design supplies the canonical version [brannathProbabilisticFoundationConfirmatory2012, Secs 3, 5–6]; see [conditional-error-functions](conditional-error-functions.md).
- In the adaptive-design literature the principle is a way of adding flexibility to any conventional or prespecified-adaptive design: compute A = E_H(φ | interim data), replace φ by any φ* with E_H(φ* | interim data) ≤ A, and complete the design as planned if no change is needed; lowering the conditional level never inflates the overall level. Applied to a hierarchical or step-down Dunnett test for two treatments it tells at which interim results one may drop an arm, change the sample size and still use the conventional z-test [brannathMultiplicityFlexibilityClinical2007, Secs 2.2.3, 3]. The Lehmacher–Wassmer conditional error function 1 − Φ(√2 z_{1−α_2} − z_1) is the induced test of a two-stage group-sequential z-test [poschAdaptiveTwoStage1999, Sec. 3].

## Variants and related concepts
- [e-process](e-process.md), [test-martingale](test-martingale.md), [group-invariance-e-statistics](group-invariance-e-statistics.md).

## Sources
- [koningAnytimeValidityFree2026](../sources/koningAnytimeValidityFree2026.md) — primary source.
- [koningMeasuringEvidenceExchangeability2023](../sources/koningMeasuringEvidenceExchangeability2023.md) — orbit-wise induction.
- [brannathAnytimevalidTestingEvalues2026a](../sources/brannathAnytimevalidTestingEvalues2026a.md) — conditional rejection probability principle.
- [brannathProbabilisticFoundationConfirmatory2012](../sources/brannathProbabilisticFoundationConfirmatory2012.md) — canonical versions of the conditional expectation.
- [brannathMultiplicityFlexibilityClinical2007](../sources/brannathMultiplicityFlexibilityClinical2007.md), [poschAdaptiveTwoStage1999](../sources/poschAdaptiveTwoStage1999.md) — conditional rejection probabilities of z-, Dunnett and group-sequential tests.

## Disagreements / open issues
- The authors call it a "myth" that anytime validity and optional continuation belong to the e-value paradigm, treating e-values as tests rescaled to [0, 1/α]; the rest of the wiki, following the survey and the book, treats e-processes as primary and tests as derivative. Both views agree on the mathematics: the induced test is a bounded e-process scaled by α. The authors do not advocate NP-induced tests in practice, since they stop at N and may hit zero, and say they personally prefer the e-scale [koningAnytimeValidityFree2026, Sec. 7].
