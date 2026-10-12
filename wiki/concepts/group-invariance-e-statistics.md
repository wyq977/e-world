---
slug: group-invariance-e-statistics
title: Group invariance and the anytime-valid Hunt–Stein theorem
sources: 8
updated: 2026-10-12
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
- Scale-invariant filtration σ(X_i/|X_1|): the right-Haar mixture over σ is exactly the density of the maximal-invariant reduction, so the scale-invariant likelihood ratio is a martingale there; Lai's flat mixture over θ is a nonintegrable extended supermartingale, the Gaussian mixture an integrable one with a closed-form sequence; 'mixture of ratios' over θ is an e-process for the whole point null, against Pérez-Ortiz et al.'s 'ratio of mixtures' with Dirac minimisers [wangAnytimevalidTtestsConfidence2023, Def. 4.2, Lemmas 4.4–4.5, Thms 4.1, 4.9, Remark III]. Compact-group invariance as a constraint-generated null: e-variables are 1 + f − f_π with Haar orbit averages, exchangeability via one transposition and one cyclic shift; contrast between a null closed under the action and each law invariant [larssonTestingHypothesesGenerated2025, Thms 5.5–5.6, Example 5.7].
- The complementary problem, disjoint from the free-action setting: the null is that the law of Y is itself invariant under a compact group (exchangeability, sign symmetry, sphericity). Validity decomposes over orbits, so ε is an exact e-value iff E_G[ε(Gy)] = 1 for every y; every exact e-value is an orbit-normalised statistic T(y)/E_G[T(Gy)], with an exact Monte Carlo version for any number of Haar draws; the permutation test is the threshold special case; optimal on each orbit implies optimal under any monotone aggregation; utility-optimal e-values are (U′)^{−1}(λ_O dQ̄/dQ_a) with Q̄ = E_G[GQ] the group-averaged alternative, Neyman–Pearson utility recovering Lehmann–Stein and log utility giving dQ/dQ̄, so Q̄ is the RIPr onto invariant laws; for sign flips this is the symmetry numeraire 2q(Z)/(q(Z) + q(−Z)), for permutations against a Gaussian shift the softmax; e-processes are anytime valid iff dominated on every orbit by a uniform-orbit martingale, built by inducing Doob martingales orbit by orbit, with the orbit generally not measurable along the filtration; conditional e-values reduce to invariance under the stabiliser of the past, trivial for exchangeability with distinct values but full for within-batch exchangeability; inversion kernels (ranks, signs, y/‖y‖) impoverish the filtration to a single orbit; hot-hand data [koningMeasuringEvidenceExchangeability2023, Thms 1–8, Cors 1–5, Props 3–4, Secs 1.7, 6, 8.6–8.7, 9, Example 8].

## Variants and related concepts
- [bayes-factor-e-variable](bayes-factor-e-variable.md), [reverse-information-projection](reverse-information-projection.md), [k-sample-and-contingency-table-e-values](k-sample-and-contingency-table-e-values.md).

## Sources
- [perezortizEstatisticsGroupInvariance2024](../sources/perezortizEstatisticsGroupInvariance2024.md) — primary source.
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — Theorem 2 and the t-test.
- [haoEValuesExponentialFamilies2025](../sources/haoEValuesExponentialFamilies2025.md) — Haar equals conditional.
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md) — survey treatment.
- [koningAnytimeValidityFree2026](../sources/koningAnytimeValidityFree2026.md) — induced t-test.
- [wangAnytimevalidTtestsConfidence2023](../sources/wangAnytimevalidTtestsConfidence2023.md), [larssonTestingHypothesesGenerated2025](../sources/larssonTestingHypothesesGenerated2025.md) — scale invariance and constraint view.
- [koningMeasuringEvidenceExchangeability2023](../sources/koningMeasuringEvidenceExchangeability2023.md) — invariance of the law itself, orbit e-values.

## Disagreements / open issues
- Safe Testing cites this paper by arXiv numbering (Thm 4.2, Cor. 8.3, Prop. 4.4) which maps to Thm 2, Cor. 9, Thm 4 of the published version; the published text once says "Proposition 9" meaning Corollary 9 [perezortizEstatisticsGroupInvariance2024, Versions].
- The RIPr on the data level need not exist for non-compact groups; the infimum is approached, not attained, by truncated priors [perezortizEstatisticsGroupInvariance2024, Thm 2].
