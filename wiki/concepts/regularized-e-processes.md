---
slug: regularized-e-processes
title: Regularized e-processes and possibilistic inferential models
sources: 2
updated: 2026-10-12
---

# Regularized e-processes and possibilistic inferential models

## Definition
A regularizer is a function ρ on the parameter space whose upper expectation under the investigator's imprecise prior (a credal set with upper probability Q̄) is at most one; the regularized e-process is the product ρ(θ) e_θ [martinRegularizedEprocessesAnytime2024, Def. 1, eq. 8]. Under a vacuous prior only ρ ≡ 1 qualifies, so nothing is gained without real knowledge. Validity is relaxed to an upper joint distribution P̄ built from all priors in the credal set and all pullbacks to the model index; the regularized Ville inequality states P̄(e^reg > 1/α) ≤ α at every stopping time, collapsing to ordinary [Ville](villes-inequality.md) when the prior is vacuous [Thm 1, Prop. 2, eq. 15]. A possibilistic inferential model is a data-dependent possibility measure on the parameter space with contour π_z(θ) ∈ [0, 1], valid when sup over true parameters of P(Π̄(H) ≤ α) ≤ α.

## Key results
- For possibilistic priors with contour q, ρ = 1/γ(q) with any admissible p-to-e [calibrator](calibrator.md) γ is a regularizer, because q(Θ) is a p-value relative to the prior and must be calibrated before its reciprocal is used [martinRegularizedEprocessesAnytime2024, Prop. 1].
- The product form is justified by updating coherence and by a no-domination result for "re-merging" functions, mirroring Vovk and Wang's ie-merging result [martinRegularizedEprocessesAnytime2024, Prop. 3].
- The contour 1 ∧ 1/e_θ is the capped [e-posterior](e-posterior.md) read as a possibilistic inferential model: strongly anytime valid, uniformly valid over data-chosen hypotheses, with a Choquet upper-expected-loss decision guarantee generalising the capped e-posterior risk bound and allowing data-dependent actions; no sure loss and no one-sided contraction [martinRegularizedEprocessesAnytime2024, Thms 2–5, Cors 1–3].
- Efficiency: Gaussian mean with a Savage–Dickey e-process and transformed-normal priors shrinks 95% sets and rejects a false value with fewer samples; weak moment or event priors give small gains [martinRegularizedEprocessesAnytime2024, Figs 2–3, App. E].
- ECMO re-analysis with the Turner–Grünwald 2 × 2 e-variable: neither the regularized nor the plain test rejects at 0.05, but the regularized lower and upper expectation of the survival difference is [0.086, 0.820] against [−0.042, 0.739] without the partial prior, so only with the prior is ECMO demonstrably preferred [martinRegularizedEprocessesAnytime2024, Sec. 5]; see [k-sample-and-contingency-table-e-values](k-sample-and-contingency-table-e-values.md).
- Companion: the predictive-recursion e-process, a running-MLE universal-inference e-process whose numerator is the product of predictive recursion's one-step-ahead densities (O(1) per update), is an e-process for any composite null under i.i.d. data and first-order optimal relative to its mixture model, with the gap to the oracle numerator of order n^{2/3} proved and n^{1/3} conjectured; applied to log-concavity, monotone densities, von Mises–Fisher mixtures and time homogeneity [dixitAnytimeValidAsymptotically2023, Thms 1–2, Sec. 3.3, Secs 4–5]; see [universal-inference](universal-inference.md).

## Variants and related concepts
- [e-posterior](e-posterior.md), [universal-inference](universal-inference.md), [mixture-and-plug-in-methods](mixture-and-plug-in-methods.md).

## Sources
- [martinRegularizedEprocessesAnytime2024](../sources/martinRegularizedEprocessesAnytime2024.md) — primary source.
- [dixitAnytimeValidAsymptotically2023](../sources/dixitAnytimeValidAsymptotically2023.md) — predictive-recursion e-processes.

## Disagreements / open issues
- The predictive-recursion paper leaves the null denominator as the MLE and asks whether replacing it by the RIPr still gives an e-process [dixitAnytimeValidAsymptotically2023, Sec. 3.1]; the Safe Testing reply calls the finite-n gap between universal inference and GRO "extreme" for multivariate Gaussians [grunwaldAuthorsReplyDiscussion2024, Sec. 2].
- The Bernoulli version of record of the regularized-e-process paper was not consulted; the text is arXiv v4.
