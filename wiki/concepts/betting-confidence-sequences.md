---
slug: betting-confidence-sequences
title: Betting confidence sequences for bounded means
sources: 4
updated: 2026-10-12
---

# Betting confidence sequences for bounded means

## Definition
A betting confidence sequence inverts, over candidate parameter values m, the wealth K_t(m) = ∏_{i ≤ t} (1 + λ_i(m)(X_i − m)) of a gambler betting predictable fractions λ_i against the hypothesis "conditional mean = m" for data in [0, 1]. K_t(m) is an exact nonnegative martingale under every law with conditional mean m, so {m : K_t(m) < 1/α} is a time-uniform confidence set by [Ville's inequality](villes-inequality.md); the choice of bets governs tightness but never validity [waudbysmithEstimatingMeansBounded2020, eq. 23, Thm 1, Prop. 2]. The construction is the nonparametric form of [testing by betting](testing-by-betting.md) and the survey's canonical example of an estimation e-process [ramdasGametheoreticStatisticsSafe2023, eq. 24].

## Key results
- Universal representation: for any set S of distributions, test (super)martingales are exactly ∏(1 + λ_i Z_i) with Z_i ≥ −1 conditionally mean-zero (or ≤ 0) under all of S; "mean = μ" is equivalent to K_t(μ) being a test martingale for every predictable λ [waudbysmithEstimatingMeansBounded2020, Props 2–3].
- Predictable plug-in boundaries: closed-form Hoeffding and empirical-Bernstein sequences with λ_t = √(2 log(2/α)/(σ̂²_{t−1} t log(1 + t))) ∧ c, matching Howard et al.'s conjugate-mixture sequence but over 500 times faster [waudbysmithEstimatingMeansBounded2020, Prop. 1, Thm 2, Table 1].
- Hedged capital max{θK⁺_t(m), (1 − θ)K⁻_t(m)} with truncated bets gives a sequence that is provably an interval at every time; fixed-n hedged intervals by intersection [waudbysmithEstimatingMeansBounded2020, Thm 3, Lemma 2, Remark 3].
- Betting strategies: GRAPA, the empirical maximiser of E[log(1 + λ(X − m)) | F_{t−1}], is a sequential version of the GROW criterion; aGRAPA, LBOW, ONS, diversified and hedged Kelly, ConBo, and a rebalanced portfolio, with timings [waudbysmithEstimatingMeansBounded2020, App. B, Table 2]; see [gro-criterion](gro-criterion.md).
- Sampling without replacement by replacing μ with the running conditional mean of the remaining population [waudbysmithEstimatingMeansBounded2020, Prop. 4, Thm 4]; anytime p-values sup_{m ∈ S} 1/K_t(m) and e-processes inf_{m ∈ S} K_t(m) for composite nulls [Sec. 5.4].
- Rates: capital dominates the Hoeffding process term by term for n ≥ 40 log(2/α); a zeta-weighted discrete-mixture betting process attains √(log log t / t); hedged intervals have O(1/√n) width; hindsight-optimal capital equals t^t times Owen's empirical likelihood ratio [waudbysmithEstimatingMeansBounded2020, App. E, Props 6–9, E.6].
- The numeraire for bounded means is 1 + λ*(Z − μ) with λ* solving (1 + λ*(1 − μ))/(1 − λ*μ) = e^{λ*}, and the betting e-variables are exactly the admissible e-variables for a bounded-mean constraint [larssonNumeraireEvariableReverse2025, Sec. 5.2; larssonTestingHypothesesGenerated2025, Example 3.8].
- Betting increments 1 + λ(X/m − 1) reappear as baseline increments of bounded-mean e-detectors and as point-null e-processes in non-partitioned change detection [shinEdetectorsNonparametricFramework2023, eq. 70; sahaNonpartitionedEdetectorsNonparametric2026, eq. 17].

## Variants and related concepts
- [confidence-sequence-boundaries](confidence-sequence-boundaries.md), [confidence-sets-and-sequences](confidence-sets-and-sequences.md), [e-process](e-process.md).

## Sources
- [waudbysmithEstimatingMeansBounded2020](../sources/waudbysmithEstimatingMeansBounded2020.md) — primary source.
- [larssonNumeraireEvariableReverse2025](../sources/larssonNumeraireEvariableReverse2025.md), [larssonTestingHypothesesGenerated2025](../sources/larssonTestingHypothesesGenerated2025.md) — optimality of betting e-variables.
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md) — survey placement.

## Disagreements / open issues
- The ingested text is arXiv v7 and contains none of the JRSSB discussion or rejoinder [waudbysmithEstimatingMeansBounded2020, Versions].
- The Safe Testing reply calls betting e-processes and the GRO construction "the same idea" once seen through the numeraire [grunwaldAuthorsReplyDiscussion2024, Sec. 1].
