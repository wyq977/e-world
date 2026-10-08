---
citekey: wassermanUniversalInference2020
title: "Universal inference"
authors: [Larry Wasserman, Aaditya Ramdas, Sivaraman Balakrishnan]
year: 2020
status: published
public: true
note: "The split likelihood-ratio test: an e-value built from any estimator on half the data and the null MLE on the other half, valid in finite samples for any model, with a running-MLE e-process version."
links:
  pdf: "https://www.pnas.org/doi/10.1073/pnas.1922664117"
  arxiv: "https://arxiv.org/abs/1912.11436"
  doi: "10.1073/pnas.1922664117"
  video: ""
tags: [e-variable, e-process, universal-inference, split-likelihood-ratio, confidence-sequence, composite-null, irregular-models, mixtures, shape-constraints]
ingested: 2026-10-08
version: "publisher-oa (PNAS 117(29):16880-16890; arXiv 1912.11436v4)"
---

# Universal inference

## Summary
The paper constructs hypothesis tests and confidence sets with finite-sample type I error and coverage guarantees that need no regularity conditions on the statistical model [wassermanUniversalInference2020]. The device is the *split likelihood-ratio statistic*: split the data into D0 and D1, fit any estimator θ̂1 on D1, and form the ratio of the D0-likelihood at θ̂1 to the D0-likelihood at the null MLE (or at a candidate parameter); the ratio has expectation at most 1 under the null, so Markov's inequality gives validity at threshold 1/α (Theorems 1 and 3). The construction works for any parametric model and for nonparametric classes in which the null MLE is computable, including Gaussian mixtures, log-concave densities, MTP2 Gaussian and Ising models, and nonnested independence hypotheses. Power is checked in regular models: the universal set has diameter O_p(√(log(1/α)/n)) under standard conditions (Theorem 5), and in the N_d(θ, I) model its squared radius is about 4 times that of the classical LRT set for large d. A running-MLE sequential version is dominated under the null by a nonnegative martingale, so Ville's inequality gives anytime-valid p-values and confidence sequences (Theorems 9–11). Extensions cover cross-fitting and derandomisation, profile likelihoods for nuisance parameters, upper bounds on the null maximum likelihood, powered and smoothed likelihoods, conditional likelihoods for non-i.i.d. data, misspecification in convex model classes, and an alternative "RIPR" split LRT.

## Main results
All claims below are from [wassermanUniversalInference2020]; section and theorem numbers follow the PNAS version.

- **Split likelihood-ratio statistic (Section 1, Eq. 3).** Data Y_1..Y_2n i.i.d. from P_θ*, split into D0, D1 of size n each (equal size not required). With θ̂1 any D1-based estimator and L0 the D0-likelihood, T_n(θ) = L0(θ̂1)/L0(θ). Key identity: E_θ*[T_n(θ*) | D1] ≤ 1 (Eq. 6), since conditionally on D1 the ratio integrates a density over the support of P_θ*.
- **Universal confidence set (Eq. 4, Theorem 1).** C_n = {θ : T_n(θ) ≤ 1/α} satisfies P_θ*(θ* ∈ C_n) ≥ 1 − α for every n and every model with densities. Nonparametric version (Remark 2): replace θ by densities p ∈ P and θ̂1 by any density estimate p̂1 ∈ P.
- **Cross-fit statistic (Eq. 5).** S_n(θ) = (T_n(θ) + T_n^swap(θ))/2, swapping the roles of D0 and D1; same guarantee.
- **Split LRT (Eq. 9, Theorem 3).** For H0 : θ* ∈ Θ0, let θ̂0 be the null MLE on D0; reject if U_n = L0(θ̂1)/L0(θ̂0) > 1/α. Then sup_{θ*∈Θ0} P_θ*(U_n > 1/α) ≤ α. Proof: L0(θ̂0) ≥ L0(θ*) plus Eq. 6. Cross-fit LRT (Eq. 10) W_n = (U_n + U_n^swap)/2 has the same guarantee. Remark 4: no parametric structure needed; H0 : p* ∈ P0 vs H1 : p* ∈ P1 with no relation between P0 and P1, θ̂1 fitted in P1, MLE p̂0 in P0.
- **Alternative universal set (Section 1).** {θ : ∫ L(ψ) dΠ(ψ)/L(θ) ≤ 1/α} for any prior Π and the full-data likelihood L also has coverage 1 − α but needs an integral that is intractable in irregular models.
- **"Poor man's Chernoff bound" (Section 1).** The proof is Markov applied to exp(log U_n) with E[e^{log U_n}] ≤ 1, i.e. a Chernoff bound with the exponent fixed at a = 1; the threshold log(1/α) scales like a χ²_1 quantile, but the numerator is an out-of-sample likelihood, so thresholds are not directly comparable with the classical LRT.
- **Theorem 5 (Section 2, regular parametric models).** Under identifiability, differentiability in quadratic mean, compact Θ ⊂ R^d, Lipschitz log-likelihood and nondegenerate Fisher information, if θ̂1 is √n-consistent then the split LRT confidence set has diameter O_p(√(log(1/α)/n)). Proof (SI Appendix) uses the Wong–Shen likelihood-ratio inequalities.
- **Theorem 6 (nonparametric rate).** If P has Hellinger bracketing entropy satisfying ∫_{ε_n²}^{ε_n} √log N(u, P) du ≤ c√n ε_n² (Eq. 11) and χ²(p*, p̂1) = O_p(η_n²) (Eq. 12), the split LRT set has Hellinger diameter O_p(η_n + ε_n + √(log(1/α)/n)).
- **Multivariate normal comparison (Section 2).** For Y_i ~ N_d(θ, I) with θ̂1 the D1 mean, C_n = {θ : ‖θ − Ȳ_0‖² ≤ (4/n) log(1/α) + ‖Ȳ_0 − Ȳ_1‖²}; squared radius R_n² equals in distribution (4 log(1/α) + 4χ²_d)/n, versus c_{α,d}/n for the LRT set, so for large d and fixed α the universal squared radius is about 4 times larger, with the same O_p(d/n) scaling.
- **Mixture example (Section 3, Fig. 1).** Testing one versus two Gaussian components, n = 200, α = 0.1, θ̂1 the EM-based MLE in M_2: type I error near 0, reasonable power for separation μ > 1, lower than the (unguaranteed) parametric bootstrap LRT; only one EM run is needed versus one per bootstrap replicate.
- **Sieve model selection (Section 3).** For nested P_1 ⊂ P_2 ⊂ ..., test H_j : p* ∈ P_j in turn via ∏_{D0} p̂_{j+1}/p̂_j > 1/α and stop at the first non-rejection ĵ; then P_{p*}(p* ∈ P_{ĵ−1}) ≤ α with no multiplicity correction, because a type I error can only occur at the first true H_j. Applications: number of mixture components, HMM states, latent factors, sparsity level.
- **Shape and dependence constraints (Section 3).** First finite-sample test of H0 : p log-concave (null MLE via the log-concave NPMLE, p̂1 e.g. a kernel density estimate); tests of Gaussian MTP2 vs Gaussian, Ising MTP2 vs Ising, and MTP2 log-concave vs log-concave, all previously open; marginal vs conditional independence in a trivariate Gaussian (nonnested hypotheses).
- **Uniform[0, θ] example (Section 3).** With θ̂1 the D1 maximum, the split set is [0, ∞) with probability 1/2; the cross-fit interval is [θ̂0, θ̂1 (2/α)^{1/n}] with expected length O(θ log(1/α)/n), rate optimal up to constants versus the exact pivotal interval [θ̂, θ̂ (1/α)^{1/(2n)}].
- **Derandomisation (Section 4).** Any average T̄_n = B^{-1} Σ_j T_{n,j} of statistics each with E[T_{n,j}] ≤ 1 still has expectation ≤ 1 regardless of dependence; this yields K-fold, repeated-subsampling and all-splits variants. Different estimators may be used on different folds; taking the maximum instead of the average breaks validity.
- **Profile likelihood (Section 5, Eqs. 13–14).** For ψ = g(θ), B_n = {ψ : L0(θ̂1)/L0†(ψ) ≤ 1/α} with L0†(ψ) = sup_{g(θ)=ψ} L0(θ) is a 1 − α confidence set for ψ; nuisance parameters are handled by profiling them out.
- **Upper bounding the null maximum likelihood (Section 5).** If F0 is a relaxation with max F0 ≥ max L0 (e.g. a convex relaxation or SDP), T'_n = L0(θ̂1)/F0(θ̂0^F) ≤ T_n, so the test remains valid. Relevant to best-subset sparsity testing and stochastic block models.
- **Powered likelihoods (Section 5).** For 0 < η < 1, E[(L0(θ̂1)/L0(θ))^η | D1] = ∏_{D0} ∫ p_{θ̂1}^η p_θ^{1−η} ≤ 1 by nonnegativity of the η-Rényi divergence, so the robustified statistic is also valid.
- **Smoothed split LRT (Section 5, Eq. 15).** With a kernel-smoothed likelihood L̃0 and θ̃0 the KL projection of the smoothed empirical density onto the smoothed null, Ũ_n = L̃0(θ̂1)/L̃0(θ̃0) controls type I error at α (proof via Jensen).
- **Non-i.i.d. data (Section 5).** Only the conditional likelihood of D0 given D1 is needed, e.g. sampling without replacement from an urn.
- **Misspecification, Proposition 7 (Section 6).** If the model P_Θ is convex, data come from q ∉ P_Θ, and the reversed information projection (RIPR) p* of q onto P_Θ lies in P_Θ, then P_q(p* ∈ C_n) ≥ 1 − α, using E_q[p_θ(Y)/p*(Y)] ≤ 1 for all θ (Eq. 16, from Li 1999).
- **RIPR split LRT, Proposition 8 (Section 6).** Let p*_0 be the RIPR of p_{θ̂1} onto the null class; reject if R_n = ∏_{D0} p_{θ̂1}(Y_i)/p*_0(Y_i) > 1/α. If {p_θ : θ ∈ Θ} is convex, sup_{θ0∈Θ0} P_{θ0}(R_n > 1/α) ≤ α. When the RIPR lies in the null set, R_n ≥ U_n, so the RIPR test is at least as powerful; the MLE version is more broadly computable.
- **Running MLE sequential LRT, Theorem 9 (Section 7).** With θ̂1,t−1 any nonanticipating estimator and θ̂0,t the null MLE on the first t observations, M_t = ∏_{i≤t} p_{θ̂1,i−1}(Y_i) / ∏_{i≤t} p_{θ̂0,t}(Y_i); rejecting when M_t > 1/α gives sup_{θ*∈Θ0} P_θ*(τ < ∞) ≤ α. Proof: under the null M_t ≤ L_t = ∏ p_{θ̂i−1}(Y_i)/p_θ*(Y_i) (Eq. 18), a nonnegative martingale with L_0 = 1, then Ville's inequality. Updates can start after t_0 burn-in steps or be done in batches.
- **Anytime-valid p-values, Theorem 10.** p_t = 1/M_t and p̄_t = min_{s≤t} 1/M_s satisfy sup_{θ*∈Θ0} P_θ*(p̄_T ≤ x) ≤ x for any random time T, not necessarily a stopping time.
- **Confidence sequences, Theorem 11.** With R_t(θ) = ∏ p_{θ̂1,i−1}(Y_i)/∏ p_θ(Y_i), C_t = {θ : R_t(θ) ≤ 1/α} and the running intersection C̄_t satisfy P_θ*(∃t : θ* ∉ C̄_t) ≤ α, equivalently coverage at any stopping time or arbitrary random time. Duality: p_t < α iff C_t ∩ Θ0 = ∅ (reverse direction needs Θ0 closed).
- **Sequential extensions (Section 7).** Profile likelihoods give sequential t-tests and confidence sequences for a Gaussian mean with unknown variance; with conditional or powered likelihoods L_t is a supermartingale rather than a martingale. The paper states that the sequential split LRT is simultaneously an anytime-valid p-value, an e-value and a safe test.

## Setting and assumptions
- Model: any collection {P_θ : θ ∈ Θ} with densities p_θ with respect to a common dominating measure μ; Θ is an arbitrary set, no dimension, smoothness, identifiability or regularity needed for validity (Theorems 1, 3, 9–11). Nonparametric classes allowed whenever likelihoods can be evaluated.
- Null: composite H0 : θ* ∈ Θ0 (or p* ∈ P0); alternative arbitrary, possibly nonnested. The only computational requirement is the null MLE on D0, or any upper bound on the null maximum likelihood.
- Data: i.i.d. for exposition; only the conditional likelihood of D0 given D1 is needed. Fixed-n split for Theorems 1–8; i.i.d. stream with nonanticipating estimators for Theorems 9–11.
- Optional stopping and continuation: not addressed in the fixed-n version; fully allowed in the running-MLE version (Section 7), which is valid at stopping times and arbitrary random times.
- Power results (Theorems 5, 6) require the usual regularity conditions (DQM, compactness, Lipschitz log-likelihood, nondegenerate Fisher information, bracketing-entropy bound) and a √n-consistent or χ²-close first-stage estimator. Conservativeness is acknowledged: a factor of about 4 in squared radius for the Gaussian location model, and near-zero type I error in the mixture simulation.
- Misspecification results (Propositions 7, 8) require a convex model class.

## Relation to other sources
- [grunwaldSafeTesting2024](grunwaldSafeTesting2024.md): cited as ref. 35 (the 2019 arXiv version). The split LRT is an e-variable in the safe-testing sense; the paper notes that the sequential version is "an e value, and a safe test". The RIPR split LRT (Proposition 8) uses the same reversed-information-projection object that underlies GRO e-variables for composite nulls, but with the alternative fixed by the D1 estimate and the RIPR computed for that single alternative, without sample splitting in the fixed-alternative case studied there [wassermanUniversalInference2020].
- [ramdasHypothesisTestingEvalues2025](ramdasHypothesisTestingEvalues2025.md): universal inference is the generic e-value construction for arbitrary composite nulls where only the null MLE is available; the running-MLE process is the canonical example of an e-process dominated by a test martingale rather than being one.
- [haoEValuesExponentialFamilies2025](haoEValuesExponentialFamilies2025.md): for exponential families the running MLE update is constant-time in the sufficient statistics (Section 7), but the split LRT does not optimise growth rate; the paper leaves optimality open beyond the uniform and Gaussian cases.
- howardTimeuniformNonparametricNonasymptotic2021 (ref. 40): supplies the equivalence between time-uniform coverage, coverage at stopping times and coverage at arbitrary random times used in Theorem 11.
- villeEtudeCritiqueNotion1939 (ref. 38): Ville's inequality is the only probabilistic tool beyond Markov in the sequential proofs.
- waldSequentialAnalysis1947 (ref. 48): the running-MLE martingale for point nulls is attributed to Wald's Eq. 10:10; the sequential LRT (ref. 36) is the template the running MLE LRT extends.
- shaferTestingBettingStrategy2021 and vovkEvaluesCalibrationCombination2021 are not cited; the paper predates the term "e-value" becoming standard and uses it only once, in Section 7.

## Concepts touched
- [universal-inference](../concepts/universal-inference.md)
- [split-likelihood-ratio](../concepts/universal-inference.md)
- [e-variable](../concepts/e-variable.md)
- [e-process](../concepts/e-process.md)
- [test-martingale](../concepts/test-martingale.md)
- [e-confidence-set](../concepts/confidence-sets-and-sequences.md)
- [confidence-sequence](../concepts/confidence-sets-and-sequences.md)
- [anytime-valid-p-value](../concepts/e-process.md)
- [villes-inequality](../concepts/villes-inequality.md)
- [reverse-information-projection](../concepts/reverse-information-projection.md)
- [cross-fitting-and-derandomisation](../concepts/universal-inference.md)
- [composite-null](../concepts/e-variable.md)

## Versions
The arXiv version (1912.11436, v4) and the PNAS version of record are not known to differ materially; theorem numbering above follows PNAS. Proofs of Theorems 5 and 6 are in the SI Appendix, which is not part of `paper.txt`.

## Open questions / gaps
- Optimality: the authors state they "do not yet fully understand how close to optimal" the split LRT is beyond the uniform and Gaussian cases, and do not expect rate optimality in general; the Gaussian location example shows a constant-factor loss of about 4 in squared radius [wassermanUniversalInference2020].
- Choice of θ̂1: validity holds for any D1 estimator, but power depends on it; no guidance beyond MLE, Bayes or robust estimators is given.
- Derandomisation: the statistical gains of K-fold, subsampling and all-splits averaging are left to future work (Section 4).
- Power comparison of the universal test against the envelope test for marginal vs conditional independence is left open (Section 3).
- Semiparametric extension (finite-dimensional parameter of interest with infinite-dimensional nuisance) is proposed but not developed (Section 8).
- Cited but not in the bib: Wong and Shen 1995 (likelihood-ratio inequalities behind Theorem 5), Li 1999 (RIPR), Darling and Robbins 1967 and Lai 1976 (confidence sequences), Robbins and Siegmund 1972/1974 and Lorden and Pollak 2005 (nonanticipating-estimator martingales), Shafer, Shen, Vereshchagin and Vovk 2011 (test martingales), Howard et al. 2020 (time-uniform Chernoff bounds).
