---
citekey: turnerGenericEvariablesExact2024
title: "Generic E-variables for exact sequential k-sample tests that allow for optional stopping"
authors: [Rosanne J. Turner, Alexander Ly, Peter D. Grünwald]
year: 2024
status: published
public: true
note: "Builds exact, anytime-valid k-sample tests from a generic block e-variable whose denominator is a product of per-outcome mixtures of the null, proves it is GRO whenever the single-outcome model is convex (so for 2x2 tables), and shows by simulation that with a Beta(0.18, 0.18) prior it matches Fisher's exact test in sample size while allowing optional stopping."
links:
  pdf: https://doi.org/10.1016/j.jspi.2023.106116
  arxiv: https://arxiv.org/abs/2106.02693
  doi: 10.1016/j.jspi.2023.106116
  video: ""
tags: [e-values, k-sample-tests, contingency-tables, two-proportions, gro, reverse-information-projection, test-martingale, optional-stopping, minimal-effect-size, bayesian-learning, simulations]
ingested: 2026-10-08
version: "publisher-oa (JSPI 230, 106116, 2024; arXiv 2106.02693)"
---

# Generic E-variables for exact sequential k-sample tests that allow for optional stopping

## Summary
The paper constructs e-variables for testing whether k ≥ 2 i.i.d. data streams come from the same distribution, against alternatives that may be unrestricted, restricted to a minimal effect size, or further restricted by knowledge of the control-group rate [turnerGenericEvariablesExact2024]. For a single block of n_a outcomes from stream a and n_b from stream b and a point alternative (θ*_a, θ*_b), the generic e-variable (eq. 3.1) is the likelihood of the alternative divided by a product, over each individual outcome, of the mixture (n_a/n) p_{θ*_a} + (n_b/n) p_{θ*_b}; Theorem 1 shows this is an e-variable for the composite null θ_a = θ_b for any parametric family, and that it is GRO whenever the single-outcome model {P_θ} is convex, even though the null for n outcomes is not. Composite alternatives are handled by Bayesian learning: the posterior after the previous blocks defines the e-variable for the next block (eq. 3.5), giving a test martingale that is safe under optional stopping between blocks. For Bernoulli streams (k × 2 contingency tables) the denominator collapses to a Bernoulli with the pooled mean θ_0 = (n_a/n)θ*_a + (n_b/n)θ*_b (eq. 4.2), independent beta priors give closed-form posterior means (Proposition 2), and the resulting e-variable is GRO for every point alternative. Simulations select the REGROW-optimal beta hyperparameter γ ≈ 0.18, show that the e-variable's expected sample size under optional stopping is about the planned sample size of Fisher's exact test and smaller under a well-specified effect-size restriction, and show that the k-sample version beats the chi-square test at small samples and large effects; a re-analysis of the SWEPIS stillbirth trial reaches e-values ≥ 20 before the sixth event [turnerGenericEvariablesExact2024].

## Main results
- Definition 1 (Sec. 2.2): a sequential e-variable process {S_(j)} has E_P[S_(j) | Y^(j−1)] ≤ 1 for all P in H_0; the running product S^(m) is the test martingale, and by Ville's inequality (eq. 2.4) P(∃j: S^(j) ≥ 1/α) ≤ α under every P in H_0.
- Proposition 1 (Sec. 2.2): for simple H_1 = {Q} and nondegenerate H_0, if some P in H_0 makes q/p an e-variable (Condition 2.6), then q/p is the Q-GRO e-variable; under i.i.d. blocks the m-block GRO e-variable is the product of the per-block ones.
- Theorem 1 (Sec. 3.1): S_[n_a,n_b,θ*_a,θ*_b] := s(Y; n_a, n_b, θ*_a, θ*_b) defined by eq. 3.1 satisfies sup_θ E_{P_θ}[S] ≤ 1 for arbitrary parametric {P_θ}; if {P_θ : θ ∈ Θ} (the single-outcome model, not H_0) is convex, it is the (θ*_a, θ*_b)-GRO e-variable among all functions of the block. The 2 × 2 null on n > 1 outcomes is not convex, yet the Bernoulli model on one outcome is, so GRO holds there.
- Eq. 3.3 (Sec. 3.1, proof in Appendix S1): k-stream extension with denominator ∏_g ∏_i Σ_{g'} (n_{g'}/n) p_{θ*_{g'}}(y_{i,g}); again GRO when {P_θ} is convex.
- Eq. 3.2 and the "ignore the remainder" rule (Sec. 3.1): with blocks fixed in advance (sizes may depend on the past but must be set before the block starts; Appendix S5 relaxes this), optional stopping is valid at any time t by evaluating the product at m_t = max{m : m n_a ≤ t_a, m n_b ≤ t_b} and discarding the incomplete block.
- Eq. 3.4 (Sec. 3.2): replacing θ*_a, θ*_b by the Bayes predictives p_{W_1,a}, p_{W_1,b} of any prior W_1 on Θ_1 gives an e-variable, by applying Theorem 1 to the "meta-model" of mixtures; eq. 3.5 uses the posterior W_1 | Y^(j−1) for block j, yielding a sequential e-variable process.
- Eq. 3.6 (Sec. 3.2): if {P_θ} is convex and the outcome space finite, Carathéodory gives a θ̆_0 | Y^(j−1) in Θ with p_{θ̆_0} = (n_a/n) p_{W_1,a|Y^(j−1)} + (n_b/n) p_{W_1,b|Y^(j−1)}, so each block is a ratio of per-stream predictive densities to a single null density.
- Eqs 3.7–3.8 (Sec. 3.2): with n_a = n_b = 1 and prior independence of θ_a, θ_b, the numerator telescopes to the Bayes marginal likelihood ∫p_{θ_a}(Y_a^m)dW_a ∫p_{θ_b}(Y_b^m)dW_b, but the denominator is a prequential product in which Y_{j,a}, Y_{j,b} are conditionally independent, so the e-variable is in general not a Bayes factor; Appendix S3 shows no applicable Gunel–Dickey Bayes factor is an e-variable.
- Eq. 4.2 (Sec. 4): for Bernoulli streams the generic e-variable equals p_{θ*_a}(y_a)p_{θ*_b}(y_b)/p_{θ_0}(y_a, y_b) with θ_0 = (n_a/n)θ*_a + (n_b/n)θ*_b, and is always (θ*_a, θ*_b)-GRO; eq. 4.3: the prior-W_1 version equals the point version at the posterior means.
- Proposition 2 (Sec. 4): with independent Beta(α_a, β_a), Beta(α_b, β_b) priors, θ̆_a | Y^(j−1) = (U_a + α_a)/((j−1)n_a + α_a + β_a), likewise for b, and θ̆_0 is their n_a:n_b weighted mean; if α_b = κα_a, β_b = κβ_a with κ = n_b/n_a, θ̆_0 = (U + (1+κ)α_a)/((j−1)n + (1+κ)(α_a + β_a)).
- Eq. 5.3 (Sec. 5.1): for minimal effect size δ' under d(θ) = θ_b − θ_a or the log odds ratio (eq. 5.2), a prior W*_1 supported on the boundary Θ(δ') guarantees that for every (θ_a, θ_b) with d > δ' the expected log e-value is at least the minimum over Θ(δ'); priors on all of Θ+(δ') grow faster when |d| ≫ |δ'| but slower near δ'. Posteriors on Θ(δ') are computed numerically (Appendix S2).
- Sec. 5.2: with both a minimal effect δ' and a known control rate θ*_a, Θ(δ') is a single point and the e-variable is the point-alternative one of eq. 4.2.
- Sec. 6, Fig. 2 (REGROW): among Beta(γ, γ) priors with n_a = n_b = 1, the hyperparameter minimising worst-case regret (eq. 2.7) over θ*_1 ∈ [0,1]² converges to γ ≈ 0.18 as the number of blocks grows; adopted as default.
- Sec. 6, Fig. 3: at α = 0.05 and 80% power, worst-case and expected sample sizes under optional stopping are essentially the same for γ = 0.18 and γ = 0.05 and worse for larger γ, except at very small δ (e.g. θ = (0.5, 0.58)) where larger γ wins, conjectured to be a composite-null version of the switching/stitching phenomenon.
- Sec. 6, Fig. 4: expected sample size of the unrestricted e-variable under optional stopping ≈ the fixed sample size to plan for with Fisher's exact test; a correctly specified restriction (δ = 0.04 difference, or the equivalent log odds ratio) gives considerably smaller expected sizes; a restriction far below the true effect costs samples. Fig. S4.1: Fisher's test loses type-I control under optional stopping, the e-variable does not.
- Sec. 6, Fig. 5: k = 4 Bernoulli streams, n⃗ = (1,1,1,1), γ = 1, θ on an equally spaced grid from 0.1 to 0.1 + δ_max: expected sample size is significantly below the chi-square test's planned size for δ_max ≥ 0.45.
- Sec. 7, Fig. 6 (SWEPIS): 1380 blocks with n_a = n_b = 1, 0 vs 6 stillbirths, Fisher p ≈ 0.015 under a (false) fixed design. With γ = 0.18 and restrictions δ = 0.00318, log odds ratio log 2, control rate 0.0001 from Muglu et al. 2019: the event-rate-plus-difference restriction stops before the sixth stillbirth in all 1000 permutations; unrestricted e-variables also typically stop earlier; the under-specified effect-size restrictions give lower e-values. Wagenmakers and Ly 2020 reported Bayes factors between 1 and 5.4 for the same data, whereas any rejection here means a product e-value ≥ 20.
- Sec. 8.1 and Proposition 3: for mean-parameterised families one may try the "mixture of means" ratio (eq. 4.2) instead of eq. 3.1; it fails to be an e-variable for exponential and negative binomial families (expectation diverges as θ → ∞) but is an e-variable, and then the GRO one, for the Gaussian location family, where it reduces to the paired Z-test on Y_a − Y_b; Proposition 3: whenever eq. 4.2 is an e-variable on a convex Θ ⊂ R^k, it is GRO.
- Sec. 8.2: Wald's 1947 2-sample SPRT corresponds to the conditional e-variable S_cond,δ = q_δ(Y_a, Y_b | Y_a + Y_b)/q_0(Y_a, Y_b | Y_a + Y_b), valid only for log-odds-ratio effect sizes; it equals 1 whenever y_a = y_b and is slightly worse than the GRO e-variable for small δ and substantially worse for large δ (experiments not reported).

## Setting and assumptions
- Data: k ≥ 2 mutually independent i.i.d. streams from a parametric family {P_θ : θ ∈ Θ} with densities; main text treats k = 2, the k-stream Theorem 1 is in Appendix S1.
- Null: H_0 = {P_{θ,θ,...} : θ ∈ Θ}, all streams identical; composite with a nuisance parameter θ_0 that admits no group invariance (contrast with t-tests handled by maximal invariants in grunwaldSafeTesting2024).
- Alternative: d(θ_a, θ_b) > δ for a user-chosen divergence d and δ ≥ 0; unrestricted (δ = 0, two-sided), effect-size restricted (Θ(δ) boundary or Θ+(δ)), or point (effect plus known control rate).
- Blocks: n_a and n_b outcomes per block, fixed before the block starts (may depend on past data; Appendix S5 learns them); the test is evaluated only at complete blocks, so optional stopping is between, not within, blocks. The paired one-sample test is n_a = n_b = 1 with alternating arrivals.
- Validity: exact and nonasymptotic for any finite sample; type-I error ≤ α under any stopping rule, including unknown or externally determined ones; optional continuation across studies by multiplication.
- Optimality: GRO for point alternatives when {P_θ} is convex (Bernoulli, finite outcome spaces with convex models); the Bayesian-learned version is not claimed GRO in general; prior choice affects power, never validity.
- Software: Ly, Turner, ter Schure 2022 (R package safestats) used for all simulations.

## Relation to other sources
- [grunwaldSafeTesting2024](grunwaldSafeTesting2024.md): source of the GRO and REGROW criteria, of Proposition 1 (point alternative, composite null, RIPr in the null), of the claim that simple-null e-variables coincide with Bayes factors, and of the maximal-invariant route for group-invariant nuisance parameters that this paper's proportion nuisance lacks; the 2 × 2 example there (RIPr at the pooled rate) is the special case n_a = n_b = 1 of eq. 4.2 here.
- [koolenLogoptimalAnytimevalidEvalues2022](koolenLogoptimalAnytimevalidEvalues2022.md): cited in Theorem 1's discussion for the fact that convexity of H_0 would already imply the GRO property; this paper obtains GRO without convex H_0 by requiring convexity of the single-outcome model instead.
- [howardTimeuniformNonparametricNonasymptotic2021](howardTimeuniformNonparametricNonasymptotic2021.md): anytime-valid confidence sequences and the stitching construction invoked to explain why larger γ wins at tiny effect sizes (log log n / n versus log n / n rejection boundaries).
- [turnerExactAnytimevalidConfidence2023](turnerExactAnytimevalidConfidence2023.md): the follow-up that extends these e-variables to nulls θ_a ≠ θ_b (δ ≤ δ_0 vs δ ≥ δ_1) and inverts them into anytime-valid confidence sequences for the effect size.
- [terschureAnytimevalidLogrankTest2024](terschureAnytimevalidLogrankTest2024.md): cited (ter Schure et al. 2020) for the comparison of e-value tests with α-spending and group-sequential designs; ter Schure and Grünwald 2022 for anytime-valid meta-analysis by combining e-values across studies.
- [ramdasGametheoreticStatisticsSafe2023](ramdasGametheoreticStatisticsSafe2023.md), [shaferTestingBettingStrategy2021](shaferTestingBettingStrategy2021.md): cited as the general introductions to safe anytime-valid inference and to the betting interpretation; Definition 1 adapts the terminology of Ramdas et al. 2022 and Shafer et al. 2011.
- [vovkEvaluesCalibrationCombination2021](vovkEvaluesCalibrationCombination2021.md): cited as part of the recent surge of interest in e-variables.
- [villeEtudeCritiqueNotion1939](villeEtudeCritiqueNotion1939.md): Ville's inequality (eq. 2.4) is the safety guarantee, cited via Shafer et al. 2021.
- [haoEValuesExponentialFamilies2025](haoEValuesExponentialFamilies2025.md): classifies this paper's Bernoulli k-sample setting as "simple but not super-simple" and quantifies the e-power loss of the sequential plug-in; its conditional e-variable S_COND is the general form of Wald's conditional e-variable of Sec. 8.2 here.
- [grunwaldOptimalEValuesExponential2024](grunwaldOptimalEValuesExponential2024.md): the Sec. 8.1 question (when is the "mixture of means" ratio an e-variable for general exponential families?) is the question that paper answers through the simple case.
- Wald 1947 (sequential 2 × 2 SPRT), Darling and Robbins 1967, Robbins 1970, Lai 1976 (confidence sequences and invariance), Dawid 1984 (prequential likelihood): historical anchors without links.

## Concepts touched
- [e-variable](../concepts/e-variable.md)
- [test-martingale](../concepts/test-martingale.md)
- [e-process](../concepts/e-process.md)
- [optional-stopping](../concepts/optional-stopping.md)
- [optional-continuation](../concepts/optional-continuation.md)
- [villes-inequality](../concepts/villes-inequality.md)
- [gro-criterion](../concepts/gro-criterion.md)
- [reverse-information-projection](../concepts/reverse-information-projection.md)
- [mixture-and-plug-in-methods](../concepts/mixture-and-plug-in-methods.md)
- [bayes-factor-e-variable](../concepts/bayes-factor-e-variable.md)
- [exponential-family-e-values](../concepts/exponential-family-e-values.md)
- [confidence-sets-and-sequences](../concepts/confidence-sets-and-sequences.md)
- [e-power](../concepts/e-power.md)
- k-sample-and-contingency-table-e-values (new)

## Versions
The ingested text is the JSPI version of record (received 22 June 2022, accepted 24 October 2023). The arXiv preprint 2106.02693 first appeared in June 2021 under the title "Two-sample tests that are safe under optional stopping, with an application to contingency tables"; the published version adds the k-sample framing to the title and the k-sample simulation (Fig. 5). All proofs and Appendices S1–S5 are in the supplementary material, not in paper.txt [turnerGenericEvariablesExact2024].

## Open questions / gaps
- For which mean-parameterised exponential and location families is the "mixture of means" ratio (eq. 4.2) an e-variable, and hence GRO by Proposition 3? Only Bernoulli and Gaussian location are settled positively, exponential and negative binomial negatively (Sec. 8.1).
- Is the Bayesian-learned e-variable (eq. 3.5) W_1-GRO outside the Bernoulli case? Not claimed; only simulation evidence of good power (Sec. 3.2).
- The REGROW search is restricted to one-dimensional Beta(γ, γ) priors and to n_a = n_b = 1; the full minimax-regret prior over [0,1]² is not computed (Sec. 6).
- Whether the switching/stitching-type gain from larger γ at very small effect sizes is real for the composite null is a conjecture (Sec. 6).
- Extension to logistic regression is stated as the main open practical problem (Sec. 9).
- Cited works not in the bib: Manole and Ramdas 2023 and Shekhar and Ramdas 2021 (nonparametric sequential two-sample tests by betting); Lindon and Malek 2022 (sequential A/B tests with simple null); Johari, Koomen, Pekelis, Walsh 2022 (always-valid inference for A/B tests); Henzi and Ziegel 2022 (sequential forecast comparison); Ly, Turner, ter Schure 2022 (safestats R package); ter Schure and Grünwald 2022 (ALL-IN meta-analysis); Turner and Grünwald 2023 (this paper's confidence-sequence sequel is in the bib); van der Pas and Grünwald 2018 (switch prior); Hendriksen, de Heide, Grünwald 2021 (optional stopping with Bayes factors); Wagenmakers and Ly 2020 (SWEPIS Bayes factors); Gunel and Dickey 1974, Jamil et al. 2017, Kass and Vaidyanathan 1992 (Bayes factors for contingency tables); Pace and Salvan 2020 (likelihood ratios and the reproducibility crisis).
