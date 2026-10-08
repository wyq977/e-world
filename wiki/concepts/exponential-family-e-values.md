---
slug: exponential-family-e-values
title: E-values for exponential family nulls
sources: 2
updated: 2026-10-08
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

## Variants and related concepts
- [reverse-information-projection](reverse-information-projection.md), [gro-criterion](gro-criterion.md).
- [universal-inference](universal-inference.md), [mixture-and-plug-in-methods](mixture-and-plug-in-methods.md).
- [bayes-factor-e-variable](bayes-factor-e-variable.md), for the Haar connection and the t-test.

## Sources
- [haoEValuesExponentialFamilies2025](../sources/haoEValuesExponentialFamilies2025.md) — the general case, all theorems above.
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — 2×2 table and Gaussian examples.

## Disagreements / open issues
- No general n-free sufficient condition for the UI regularity condition in multivariate families [haoEValuesExponentialFamilies2025, App. C.1].
- The anti-simple case under misspecification R ≠ Q is stated only for R = Q [haoEValuesExponentialFamilies2025, below Thm 3].
- grunwaldOptimalEValuesExponential2024 (the simple case) is in the bib but not yet ingested.
