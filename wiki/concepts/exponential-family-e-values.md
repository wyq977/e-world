---
slug: exponential-family-e-values
title: E-values for exponential family nulls
sources: 12
updated: 2026-10-12
---

# E-values for exponential family nulls

## Definition
The setting is a composite null that is a regular d-dimensional exponential family in mean-value parameterisation, against a simple alternative or a matching exponential family with the same sufficient statistic [haoEValuesExponentialFamilies2025, Def. 1]. Four e-statistics are compared by [e-power](e-power.md): the RIPr-optimal S_RIP (GRO), its sequentialised plug-in S_SEQ-RIP, universal inference S_UI = q/p_MLE, and the conditional S_COND = q(U^n | Z)/p(U^n | Z) with Z the sufficient statistic, whose denominator is prior-free by sufficiency [haoEValuesExponentialFamilies2025, eqs 1.2–1.3, 1.6–1.7, 1.13]. The "simple" case (Σ_q − Σ_p negative semidefinite) was treated by Grünwald, Lardy, Hao, Bar-Lev and de Jong [grunwaldOptimalEValuesExponential2024]; this paper adds the "anti-simple" case (Σ_q − Σ_p positive semidefinite), where the RIPr is a nondegenerate Bayes mixture.

## Key results
- Gaussian location, anti-simple: the RIPr prior is N(μ*, (Σ_q − Σ_p)/n) and S_RIP = S_COND exactly for all n; with a Gaussian prior W_1 on the alternative the RIPr prior is N(μ_1, Π_1 + (Σ_q − Σ_p)/n) and again S_{W_1,RIP} = S_COND [haoEValuesExponentialFamilies2025, Thms 1.4, 2.4]. S_COND equals the right-Haar Bayes factor of Pérez-Ortiz et al. [Remark 6].
- General families: E_Q[log S_RIP] = E_Q[log S_COND] + o(1) under a local-CLT regularity condition; the RIPr of a Bayes mixture is approximately the same mixture over the null [haoEValuesExponentialFamilies2025, Thms 3.4, 4.4].
- E-power ranking for composite alternatives: COND − UI = (d/2) log n + O(1); SEQ-RIP − UI = (d_qp/2) log n + O(1) with effective dimension d_qp = tr(Σ_q Σ_p^{-1}) < d in the strictly simple case; SEQ-RIP is trivial in the anti-simple case (≡ 1 for Gaussians, linear loss nε in general) [haoEValuesExponentialFamilies2025, Cor. 4, eqs 1.9–1.12, Thms 1.3, 3.3, 4.3].
- Simple alternative: UI loses d_rp/2 (a Wilks phenomenon), COND loses the O(1) amount D_{Σ_r}(Σ_q ‖ Σ_p) [haoEValuesExponentialFamilies2025, eqs 2.6–2.7, 3.3–3.4].
- Regularity: Conditions 1–3 (conditional, UI, plug-in), with Condition 3 verified for Bernoulli, Poisson, geometric, binomial, negative binomial, Gaussian location-scale and Gamma, failing for the Landau family [haoEValuesExponentialFamilies2025, Sec. 3].
- S_COND and S_RIP are generally not [e-processes](e-process.md), unlike S_UI and S_SEQ-RIP, except in the Gaussian and Poisson k-sample settings [haoEValuesExponentialFamilies2025, Prop. 7, Prop. 1].
- Contingency tables: for the 2×2 table with fixed design, the RIPr of a point alternative is the pooled rate, full-alternative REGROW is numerical with (1/2) log n regret, and a sequential Beta(0.18, 0.18) prior is almost REGROW [grunwaldSafeTesting2024, Examples 2, 6, 7, 9].
- The sequential plug-in analysis generalises prequential log-loss results of Grünwald and de Rooij 2005 and Kotłowski and Grünwald 2011 [haoEValuesExponentialFamilies2025, Prop. 4, Lemma 3].
- The simple case, origin: for a regular exponential family null P and a simple alternative Q, generate the family Q̄ = {q_β ∝ exp(βᵀt(U)) q(U)} sharing P's sufficient statistic; Theorem 1 gives eight equivalent conditions, chiefly Σ_p(μ) − Σ_q(μ) ⪰ 0 for all μ in the alternative's mean space, under which q_{μ*}/p_{μ*} is the GRO e-variable with the RIPr a point mass; locality for all μ implies globality [grunwaldOptimalEValuesExponential2024, eq. 1.3, Thm 1, Prop. 2]. Examples: Gaussian and Poisson k-sample (E_P[S] = 1 for all null elements), Bernoulli k-sample via concavity of log, Gaussian location with Σ_p ⪰ Σ_q, Gaussian scale, NEF pairs by variance functions, Tweedie pairs; Poisson regression violates the condition even at n = 2 [grunwaldOptimalEValuesExponential2024, Sec. 4, App. A].
- One-sided exponential-family interval nulls β ∈ [a, b] vs β1 < a: the RIPr is p_a and the log-optimal anytime-valid e-process is exp((β1 − a)Σx_i − m(φ(β1) − φ(a))) [koolenLogoptimalAnytimevalidEvalues2022, Sec. 4.4(iv)].
- Survey remarks: monotone-likelihood-ratio families with separated null and alternative have GRO equal to a simple likelihood ratio; conditional e-values via sufficient statistics are usually not (RE)GRO(W) [ramdasGametheoreticStatisticsSafe2023, Secs 4.1.1, 4.1.3].
- For 2 × 2 tables the conditional (sufficient-statistic) e-variable is Wald's two-sample SPRT, equal to one whenever the counts tie, and inferior to the GRO block e-variable [turnerGenericEvariablesExact2024, Sec. 8.2]; see [k-sample-and-contingency-table-e-values](k-sample-and-contingency-table-e-values.md).
- Canonical maximum entropy models are exponential families with uniform carrier; testing between families with different sufficient statistics complements the same-statistic setting, and the microcanonical GRO e-variable is the conditional e-variable with Z = c_0 [giuffridaTestingMaximumEntropy2025, Secs II–III]; see [mdl-and-maximum-entropy-e-values](mdl-and-maximum-entropy-e-values.md).
- One-dimensional exponential family with sufficient statistic and null with smallest element θ* > θ_1: RIPr p_{θ*}, numeraire p_{θ_1}/p_{θ*} via convexity of the log-partition function [larssonNumeraireEvariableReverse2025, Sec. 5.5]; Gaussian scale-location examples under invariance [perezortizEstatisticsGroupInvariance2024, Secs 2.2, 4.1, 4.2]; two-point e-process rates, MLE minimaxity and dampened Savage–Dickey bounds for regular one-dimensional families [grunwaldEposterior2023, SM Thm 1, Props 3–4].
- One-sided sub-ψ nulls: e-variables are exactly functions dominated by ∫e^{λx − ψ(λ)} π(dλ), a minimal complete class when ψ is a CGF, with e^{λ*x − ψ(λ*)} the numeraire against μ_{λ*} [larssonTestingHypothesesGenerated2025, Thm 4.3, Thm 6.5, Example 7.5]. Csiszár–Matúš exponential-family RIPr and the geometric-family moment-bound failure [lardyReverseInformationProjections2023, Sec. II-B, Example 3].

## Variants and related concepts
- [reverse-information-projection](reverse-information-projection.md), [gro-criterion](gro-criterion.md).
- [universal-inference](universal-inference.md), [mixture-and-plug-in-methods](mixture-and-plug-in-methods.md).
- [bayes-factor-e-variable](bayes-factor-e-variable.md), for the Haar connection and the t-test.

## Sources
- [haoEValuesExponentialFamilies2025](../sources/haoEValuesExponentialFamilies2025.md) — the general case, all theorems above.
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — 2×2 table and Gaussian examples.
- [grunwaldOptimalEValuesExponential2024](../sources/grunwaldOptimalEValuesExponential2024.md) — the simple case in full.
- [koolenLogoptimalAnytimevalidEvalues2022](../sources/koolenLogoptimalAnytimevalidEvalues2022.md) — interval nulls under optional stopping.
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md), [turnerGenericEvariablesExact2024](../sources/turnerGenericEvariablesExact2024.md) — MLR remark, conditional e-variable for 2 × 2.
- [giuffridaTestingMaximumEntropy2025](../sources/giuffridaTestingMaximumEntropy2025.md) — different-statistic tests.
- [larssonNumeraireEvariableReverse2025](../sources/larssonNumeraireEvariableReverse2025.md), [perezortizEstatisticsGroupInvariance2024](../sources/perezortizEstatisticsGroupInvariance2024.md), [grunwaldEposterior2023](../sources/grunwaldEposterior2023.md) — batch-3 contributions.
- [larssonTestingHypothesesGenerated2025](../sources/larssonTestingHypothesesGenerated2025.md), [lardyReverseInformationProjections2023](../sources/lardyReverseInformationProjections2023.md) — constraint and projection views.

## Disagreements / open issues
- No general n-free sufficient condition for the UI regularity condition in multivariate families [haoEValuesExponentialFamilies2025, App. C.1].
- The anti-simple case under misspecification R ≠ Q is stated only for R = Q [haoEValuesExponentialFamilies2025, below Thm 3].
- grunwaldOptimalEValuesExponential2024 (the simple case) is in the bib but not yet ingested.
