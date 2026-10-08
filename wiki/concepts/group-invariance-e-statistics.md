---
slug: group-invariance-e-statistics
title: Group invariance and the anytime-valid Hunt–Stein theorem
sources: 5
updated: 2026-10-08
---

# Group invariance and the anytime-valid Hunt–Stein theorem

## Definition
For a testing problem invariant under a group G acting freely on data and parameters, with the parameter of interest δ a maximal invariant of θ, the canonical e-statistic is the likelihood ratio of a maximally invariant statistic M_n; by Wijsman's representation it equals the ratio of right-Haar-mixed likelihoods, the right-Haar Bayes factor, independent of the choice of maximal invariant and the same on the data or on a sufficient statistic [perezortizEstatisticsGroupInvariance2024, Sec. 2.2, eq. 5]. The prototype is the one-sample t-test with G = (R⁺, ·) and δ = μ/σ, the safe t-test of Safe Testing [grunwaldSafeTesting2024, Sec. 4.3].

## Key results
- Anytime-valid Hunt–Stein theorem: if G is amenable and a (1 + ε) log-likelihood-ratio moment condition holds, the infimum over all prior pairs on G of KL(Q_{Π1} ‖ P_{Π0}) equals KL(Q^{M_n} ‖ P^{M_n}), so the invariant likelihood ratio is GROW among all e-statistics, invariant or not; the proof uses truncated right-Haar priors on Følner-type compact sets [perezortizEstatisticsGroupInvariance2024, Thm 2, Cor. 3, Lemma 2].
- Under invariance the oracle growth rate is constant over the group, so GROW and REGROW coincide, unlike contingency tables [perezortizEstatisticsGroupInvariance2024, Thm 4, Cor. 5]; see [gro-criterion](gro-criterion.md).
- The sequence of maximal-invariant likelihood ratios is a nonnegative martingale under every null element in the filtration σ(M_1, …, M_n), so optional stopping and continuation are valid for stopping times of that coarser filtration; a data-filtration stopping time exists for which the stopped t-test statistic is not an e-statistic [perezortizEstatisticsGroupInvariance2024, Prop. 6, supplement S3.1]; see [optional-stopping](optional-stopping.md).
- Composite δ: the GROW/REGROW e-statistic is a ratio of δ-Bayes marginals under the optimal priors, point priors for the one-sided t-test by monotone likelihood ratio; any proper-prior Bayes factor on δ satisfying the moment condition is GROW and REGROW, so the Jeffreys/Rouder t-test with a Gaussian prior is REGROW while the Cauchy case is open [perezortizEstatisticsGroupInvariance2024, Prop. 7, Cors 8–9].
- Examples: a lower-triangular group alternative to Hotelling's T² with explicit Wishart-integral likelihood ratio, and a single regression coefficient with group R⁺ × R^d [perezortizEstatisticsGroupInvariance2024, Secs 4.1–4.2].
- Amenability is sufficient, not necessary: Hotelling's T² under the non-amenable GL(d) is GROW for d = 2 via Giri–Kiefer–Stein mixtures; the Sun–Berger right-Haar non-uniqueness does not arise because the e-statistic is a ratio of marginals of two models at the same n [perezortizEstatisticsGroupInvariance2024, Sec. 5].
- The conditional e-variable of the exponential-family paper equals this Haar Bayes factor for Gaussian location [haoEValuesExponentialFamilies2025, Remark 6]; the survey records that the t-test e-process is GROW and REGROW for every γ and τ because its expected log is constant in σ [ramdasGametheoreticStatisticsSafe2023, Sec. 4.1.2].
- Test induction covers the log-optimal t-test as the induced test of a terminal test non-decreasing in the sufficient statistic [koningAnytimeValidityFree2026, Thm 3, Prop. 5].

## Variants and related concepts
- [bayes-factor-e-variable](bayes-factor-e-variable.md), [reverse-information-projection](reverse-information-projection.md), [k-sample-and-contingency-table-e-values](k-sample-and-contingency-table-e-values.md).

## Sources
- [perezortizEstatisticsGroupInvariance2024](../sources/perezortizEstatisticsGroupInvariance2024.md) — primary source.
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — Theorem 2 and the t-test.
- [haoEValuesExponentialFamilies2025](../sources/haoEValuesExponentialFamilies2025.md) — Haar equals conditional.
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md) — survey treatment.
- [koningAnytimeValidityFree2026](../sources/koningAnytimeValidityFree2026.md) — induced t-test.

## Disagreements / open issues
- Safe Testing cites this paper by arXiv numbering (Thm 4.2, Cor. 8.3, Prop. 4.4) which maps to Thm 2, Cor. 9, Thm 4 of the published version; the published text once says "Proposition 9" meaning Corollary 9 [perezortizEstatisticsGroupInvariance2024, Versions].
- The RIPr on the data level need not exist for non-compact groups; the infimum is approached, not attained, by truncated priors [perezortizEstatisticsGroupInvariance2024, Thm 2].
