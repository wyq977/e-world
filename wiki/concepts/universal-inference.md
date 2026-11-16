---
slug: universal-inference
title: Universal inference and the split likelihood ratio
sources: 21
updated: 2026-11-09
---

# Universal inference and the split likelihood ratio

## Definition
A procedure is universal when its type-I error or coverage guarantee holds in finite samples for every member of an arbitrary model class, with no regularity, dimension or smoothness conditions [wassermanUniversalInference2020, Sec. 1]. The canonical construction splits the data into D_0 and D_1, fits any estimator θ̂_1 on D_1, and forms the split likelihood ratio U_n = L_0(θ̂_1)/L_0(θ̂_0) with L_0 the likelihood on D_0 and θ̂_0 the null MLE on D_0; U_n is an [e-variable](e-variable.md) because E[L_0(ψ)/L_0(θ*) | D_1] ≤ 1, so rejecting at U_n > 1/α is level α [wassermanUniversalInference2020, eqs 3, 6, 9, Thm 3; ramdasHypothesisTestingEvalues2025, Thm 5.1]. The same ratio with a generic θ inverts to a confidence set [wassermanUniversalInference2020, Thm 1].

## Key results
- Works wherever the null MLE, or merely an upper bound on the null maximum likelihood, is computable: Gaussian mixtures, log-concave densities, MTP2 models, nonnested independence hypotheses, sieve model selection without multiplicity correction [wassermanUniversalInference2020, Sec. 3, Sec. 5, Remark 4].
- Price of universality: rate-optimal shrinkage O_p(√(log(1/α)/n)) in regular models and Hellinger rates nonparametrically, but about four times the squared radius of the classical LRT set for Gaussian location in high dimension [wassermanUniversalInference2020, Thms 5–6, Sec. 2].
- Cross-fitting and averaging over K folds, subsamples or all splits stays valid under arbitrary dependence and improves e-power and power; the uniform-distribution example is rescued only by cross-fitting [wassermanUniversalInference2020, Sec. 4, eqs 5, 10; ramdasHypothesisTestingEvalues2025, Props 5.3–5.4, Thms 5.6–5.7].
- Extensions keeping E ≤ 1: profile likelihood for nuisance parameters, convex relaxations, powered likelihoods via Rényi divergence, smoothed and conditional likelihoods [wassermanUniversalInference2020, Sec. 5].
- Sequential version: the running-MLE statistic with nonanticipating numerator estimates is an [e-process](e-process.md), giving anytime p-values and confidence sequences [wassermanUniversalInference2020, Thms 9–11; ramdasHypothesisTestingEvalues2025, Prop. 7.18].
- Inadmissibility: the [numeraire](numeraire.md) dominates universal inference whenever it is available [ramdasHypothesisTestingEvalues2025, Sec. 6.5].
- E-power in exponential families: S_UI = q/p_MLE loses exactly d_rp/2 against a simple alternative and (d/2) log n against a composite one relative to the conditional e-variable [haoEValuesExponentialFamilies2025, Thms 1.1, 2.1, 3.1, 4.1, Cors 2, 4]; it is always an e-process, unlike the conditional e-variable.
- Safe Testing positions it as the density-free fallback when Theorem 1 cannot be applied [grunwaldSafeTesting2024, Sec. 8].
- The survey places UI between the generalised likelihood ratio and the composite Bayes factor: always an e-process, dominated by the RIPr when the latter is an e-process, the only route for exchangeability and log-concavity where no supermartingale exists, possibly inadmissible, power open [ramdasGametheoreticStatisticsSafe2023, Sec. 3.3.1, eq. 16, Sec. 5.5, Secs 8.2.3–8.2.4].
- The maximum-likelihood plug-in e-value (alternative over maximised null likelihood) is anytime-valid but strictly less log-optimal than the RIPr likelihood ratio: implied target 3.072 vs 3.466 at n = 10 for the Gaussian scale problem [koolenLogoptimalAnytimevalidEvalues2022, Sec. 4.3].
- Running-MLE denominator over nuisance regression coefficients is the recommended practical route to the full Cox model; power suffers when the covariate dimension is large relative to the number of events [terschureAnytimevalidLogrankTest2024, Sec. 8.1, eq. 8.2].
- Asymptotically equal e-power to GRO but extreme finite-n loss for multivariate Gaussians; UI is coherent across subsets of the null where GRO is not, a power–coherence trade-off; a GRO analogue of empirical-risk universal inference is called for [grunwaldAuthorsReplyDiscussion2024, Secs 2, 4, 5].
- Inadmissibility proved: p* ≤ p_max μ-a.s. so X* ≥ X_UI with strict inequality with positive probability for nondegenerate composite nulls; explicit example 2q/(p1 + p2) vs q/max(p1, p2) [larssonNumeraireEvariableReverse2025, Sec. 7, Lemma 7.1, Sec. 5.1].
- Universal-inference t e-process for Gaussian means with unknown variance, growth ½ log(1 + (m − θ)²/v) [sahaNonpartitionedEdetectorsNonparametric2026, Prop. 5.1]; universal-inference e-processes where no supermartingale exists (log-concavity) serve as e-detector inputs [shinEdetectorsNonparametricFramework2023, Remark 2.10]; per-P induction generalises UI beyond log utility [koningAnytimeValidityFree2026, Remark 6]; UI named as the generic computable design but not power-competitive in regression [grunwaldBeyondNeymanPearsonEvalues2024, Sec. 4.1].
- Sequential universal-inference t e-process in closed form with e-power ½ log(1 + μ²/σ²) under any finite-variance law, its one-sided version, the power-preserving translation rule for null μ_0, prior sensitivity and burn-in, and α-growth α^{−1/n} that beats the classical t-interval and works at n = 1 [wangAnytimevalidTtestsConfidence2023, Thms 3.2, 3.4, Props 3.3, 3.5, eq. 11, Secs 5.2, 6.2]. Sequential UI for exchangeability: null maximum likelihood with a mixture or predictable numerator, and smoothed non-anticipating MLEs for change points [ramdasTestingExchangeabilityForkconvexity2021, Secs 2.1, 2.7, 4.4]. Split-LR e-value families give e-confidence intervals for any fitting rule [xuPostselectionInferenceEvalue2022, Prop. 2]. Localised UI (minimise the null likelihood over a confidence set) and compound UI give (0, δ)-approximate e-values, well below the empirical-Bayes plug-in in simulations [ignatiadisAsymptoticCompoundEvalues2024, Props 5.5–5.6, Fig. 1].
- The predictive-recursion e-process is the running-MLE variant with a nonparametric-mixture numerator fitted recursively: valid for any composite null, first-order optimal relative to its mixture model, 50–50 splitting halves the growth slope, oracle gap O(n^{2/3}) proved and n^{1/3} conjectured; applied to log-concavity, monotone densities, von Mises–Fisher mixtures and time homogeneity; the authors decline to swap the MLE denominator for the RIPr [dixitAnytimeValidAsymptotically2023, Thms 1–2, Secs 3.1, 3.3, 5.1]; see [regularized-e-processes](regularized-e-processes.md). Generalised universal inference on risk minimisers used for the median example [martinRegularizedEprocessesAnytime2024, Sec. 4.5].
- The running-MLE sequential construction read as Robbins 1970, with the 'prior and an integral' set that Wasserman et al. set aside rehabilitated as the mixing construction [kirschnerConfidenceEstimationSequential2025, Thm 2, App. A].
- Recommended to the clinical-trial community as the e-value method for irregular models where no p-value is computable and no adaptive design exists; the null density in a likelihood-ratio e-value may be maximised over a composite null and the alternative over an independent training sample [brannathAnytimevalidTestingEvalues2026a, Example 1, Sec. 5.1].

## Variants and related concepts
- [reverse-information-projection](reverse-information-projection.md), for the RIPr split LRT and misspecification.
- [confidence-sets-and-sequences](confidence-sets-and-sequences.md).
- [exponential-family-e-values](exponential-family-e-values.md).

## Sources
- [wassermanUniversalInference2020](../sources/wassermanUniversalInference2020.md) — the original construction and all its variants.
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — Chapter 5 treatment, inadmissibility.
- [haoEValuesExponentialFamilies2025](../sources/haoEValuesExponentialFamilies2025.md) — quantitative e-power loss.
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — positioning.
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md) — positioning and open problems.
- [koolenLogoptimalAnytimevalidEvalues2022](../sources/koolenLogoptimalAnytimevalidEvalues2022.md) — quantitative loss vs RIPr.
- [terschureAnytimevalidLogrankTest2024](../sources/terschureAnytimevalidLogrankTest2024.md) — Cox model with covariates.
- [grunwaldAuthorsReplyDiscussion2024](../sources/grunwaldAuthorsReplyDiscussion2024.md) — finite-n loss and coherence.
- [larssonNumeraireEvariableReverse2025](../sources/larssonNumeraireEvariableReverse2025.md) — inadmissibility.
- [sahaNonpartitionedEdetectorsNonparametric2026](../sources/sahaNonpartitionedEdetectorsNonparametric2026.md), [shinEdetectorsNonparametricFramework2023](../sources/shinEdetectorsNonparametricFramework2023.md), [koningAnytimeValidityFree2026](../sources/koningAnytimeValidityFree2026.md), [grunwaldBeyondNeymanPearsonEvalues2024](../sources/grunwaldBeyondNeymanPearsonEvalues2024.md) — uses and caveats.
- [wangAnytimevalidTtestsConfidence2023](../sources/wangAnytimevalidTtestsConfidence2023.md), [ramdasTestingExchangeabilityForkconvexity2021](../sources/ramdasTestingExchangeabilityForkconvexity2021.md), [xuPostselectionInferenceEvalue2022](../sources/xuPostselectionInferenceEvalue2022.md), [ignatiadisAsymptoticCompoundEvalues2024](../sources/ignatiadisAsymptoticCompoundEvalues2024.md) — batch-4 contributions.
- [dixitAnytimeValidAsymptotically2023](../sources/dixitAnytimeValidAsymptotically2023.md), [martinRegularizedEprocessesAnytime2024](../sources/martinRegularizedEprocessesAnytime2024.md) — predictive recursion, risk minimisers.
- [kirschnerConfidenceEstimationSequential2025](../sources/kirschnerConfidenceEstimationSequential2025.md) — Robbins reading of running-MLE UI.
- [brannathAnytimevalidTestingEvalues2026a](../sources/brannathAnytimevalidTestingEvalues2026a.md) — universal inference for clinical trials.

## Disagreements / open issues
- The original authors say they do not fully understand how close to optimal the split LRT is beyond uniform and Gaussian cases [wassermanUniversalInference2020, Sec. 2]; the later numeraire and exponential-family results quantify the loss.
- Choice of the D_1 estimator affects power with no general guidance; derandomisation gains are left open [wassermanUniversalInference2020, Sec. 4].
