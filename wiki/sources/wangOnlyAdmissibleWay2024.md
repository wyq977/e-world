---
citekey: wangOnlyAdmissibleWay2024
title: "The only admissible way of merging arbitrary e-values"
authors: [Ruodu Wang]
year: 2024
status: preprint
public: true
note: "A short proof, via multi-marginal optimal transport duality and Sion's minimax theorem, that every e-merging function valid under arbitrary dependence is dominated by a weighted average of the inputs and the constant 1, so weighted arithmetic means are the only admissible way to combine arbitrarily dependent e-values."
links:
  pdf: "https://arxiv.org/pdf/2409.19888"
  arxiv: "https://arxiv.org/abs/2409.19888"
  doi: "10.48550/arXiv.2409.19888"
  video: ""
tags: [e-merging, admissibility, complete-class, arithmetic-mean, weighted-average, optimal-transport, minimax, arbitrary-dependence, level-alpha-tests, exchangeable-e-values, closed-e-bh]
ingested: 2026-10-08
version: "arxiv 2409.19888v2 (14 Mar 2025, 11 pages); published as Biometrika 112(2), 2025"
---

# The only admissible way of merging arbitrary e-values

arXiv 2409.19888v2, dated 17 March 2025 in the text; published in Biometrika 112(2), 2025. Eleven pages: Sections 1–5, no appendix.

## Summary
An e-merging function is an increasing Borel map F: R_+^K → R_+ such that F(E_1, …, E_K) is an [e-variable](../concepts/e-variable.md) whenever E_1, …, E_K are e-variables for the same hypothesis, with no assumption on their joint law [wangOnlyAdmissibleWay2024, Sec. 2]. Vovk and Wang 2021 had shown that the admissible *symmetric* e-merging functions are exactly λ + (1 − λ)M_K with M_K the arithmetic mean, and conjectured the asymmetric analogue; this paper proves it: every e-merging function is dominated by some M_λ(e) = λ·(e, 1), a weighted average of the inputs and the constant 1 with λ in the simplex Δ_{K+1}, and F is admissible if and only if F = M_λ (Theorem 1) [wangOnlyAdmissibleWay2024]. The statement is "naturally anticipated", but the proof is not: because validity must hold under every dependence structure, sup over couplings of E[F(E_1, …, E_K)] is a multi-marginal optimal transport problem, and the argument combines its Kantorovich duality (Lemma 5) with a minimax interchange on compactly supported marginals (Lemma 6, via Sion 1958) and a one-dimensional lemma giving linear upper bounds on functions whose expectation is bounded over binary e-variables (Lemma 2) [wangOnlyAdmissibleWay2024, Secs 3–4]. The same proof shows that weighted averaging is the only admissible way to merge arbitrary level-α tests (Remark 3). Section 5 shows that for restricted classes of e-values (fixed marginals, bounded second moments, identical, exchangeable) weighted averages remain admissible but other mergers exist, so the characterisation is specific to arbitrary dependence [wangOnlyAdmissibleWay2024, Sec. 5].

## Main results
- **Definitions (Section 2).** E-variable: [0, ∞]-valued with E_P[E] ≤ 1 for all P in H. E-merging function: increasing Borel F: R_+^K → R_+ with F(E_1, …, E_K) an e-variable for any e-variables and any hypothesis; infinite inputs excluded as in Vovk and Wang 2021, Appendix C. Admissible: G ≥ F pointwise for an e-merging G implies G = F. By Vovk and Wang 2021, Appendix D, it suffices to take H = {P} with P atomless [wangOnlyAdmissibleWay2024].
- **M_λ.** For λ ∈ Δ_{K+1}, M_λ(e) = λ·(e, 1) = Σ_{k≤K} λ_k e_k + λ_{K+1}; an e-merging function not dominated by any other weighted average [wangOnlyAdmissibleWay2024, Sec. 2].
- **Theorem 1.** (i) If F is an e-merging function then F ≤ M_λ for some λ ∈ Δ_{K+1}. (ii) F is an admissible e-merging function iff F = M_λ for some λ ∈ Δ_{K+1}. (ii) follows from (i) at once [wangOnlyAdmissibleWay2024].
- **Lemma 2 (K = 1, binary inputs).** For θ ∈ [1, ∞], r ≥ 0 and g: [0, θ] → R_+ with E[g(E)] ≤ r for every *binary* e-variable E in [0, θ], there is h ∈ [0, 1] with g(x) ≤ r(1 − h + hx) on [0, θ]. With r = 1 this is Theorem 1 for K = 1, "not found in the literature"; it refines Lemma EC.2 of Wang, Wang and Ziegel 2025 (E-backtesting), which used all e-variables rather than binary bounded ones. Proof (Section 4): if no line works, the sets Λ_0 (lines beaten at some y > 1) and Λ_1 (lines beaten at some x < 1) are intervals covering [0, 1] with sup Λ_0 > inf Λ_1, so a single λ_0 is beaten on both sides; the two-point e-variable with mean 1 on {x_0, y_0} then has E[g(X)] > 1 [wangOnlyAdmissibleWay2024].
- **Remark 3 (level-α tests).** A level-α test τ ∈ [0, 1] with E_P[τ] ≤ α gives the e-variable τ/α bounded by 1/α; running the proof on e-variables bounded in [0, 1/α] shows that weighted averaging is the only admissible way to merge arbitrary level-α tests, and tests at different levels merge the same way up to reweighting [wangOnlyAdmissibleWay2024].
- **Lemma 4.** Any e-merging function satisfies F(e) ≤ 1 ∨ max(e), hence F(e) ≤ 1 + Σ_k e_k (eq. 1), which makes the dual feasible [wangOnlyAdmissibleWay2024, Sec. 3].
- **Lemma 5 (optimal transport duality).** For marginals μ_1, …, μ_K with mean ≤ 1 and D_F the set of tuples (φ_1, …, φ_K) of univariate functions with ⊕_k φ_k ≥ F: 1 ≥ sup_{π ∈ Π(μ)} ∫F dπ = inf_{φ ∈ D_F} Σ_k ∫φ_k dμ_k (eq. 2), by Rachev and Rüschendorf 1998, Remark 2.1.2. The supremum over dependence structures equals the infimum over separable majorants, whose expectation depends only on the marginals [wangOnlyAdmissibleWay2024].
- **Lemma 6 (minimax).** If M ⊆ (M_0)^K is weakly compact and F bounded upper semicontinuous, then sup_{μ ∈ M} inf_{φ ∈ D_F} Σ∫φ_k dμ_k = inf_{φ ∈ D_F^+} sup_{μ ∈ M} Σ∫φ_k dμ_k (eq. 3), D_F^+ the nonnegative tuples. Proof: reduce to upper semicontinuous φ with values in [0, 1] (Kellerer 1984, Prop. 1.31), then apply Sion's minimax theorem to the bilinear J(μ, φ) = Σ∫φ_k dμ_k on the compact M (Fan 1953, Thm 2, would avoid the continuity check) [wangOnlyAdmissibleWay2024, Sec. 3].
- **Proof of Theorem 1 (Section 3).** Fix θ ≥ 1; the laws on [0, θ] with mean ≤ 1 are weakly compact by Prokhorov; replace F by an upper semicontinuous dominating e-merger (Vovk and Wang 2021, Prop. E.1). Lemmas 5–6 give inf_{φ ∈ D_F^+} Σ_k sup_{μ_k} ∫φ_k dμ_k ≤ 1 (eq. 4); for any ε > 0 pick φ with Σ_k T_{φ_k} ≤ 1 + ε, apply Lemma 2 to each φ_k to get φ_k(x) ≤ T_{φ_k}(1 − h_k + h_k x), so F ≤ (1 + ε)M_{λ_{ε,θ}} on [0, θ]^K; compactness of Δ_{K+1} gives a limit λ_0 with F ≤ M_{λ_0} on R_+^K as ε ↓ 0, θ → ∞ [wangOnlyAdmissibleWay2024].
- **Section 5, general observation.** If the subclass of input vectors contains one with mean-1 components and full support on R_+^K, then every M_λ is admissible within the subclass, because any continuous G ≥ M_λ, G ≠ M_λ, has E[G(E)] > 1 [wangOnlyAdmissibleWay2024].
- **Section 5(a), fixed marginals.** With continuous full-support marginals μ_k with survival functions g_k, the maps e ↦ M_λ(f_1∘g_1(e_1), …, f_K∘g_K(e_K)) for admissible [calibrators](../concepts/calibrator.md) f_k (decreasing, upper semicontinuous, f(0) = ∞, ∫_0^1 f = 1) are admissible mergers of the subclass, since g_k(E_k) is uniform [wangOnlyAdmissibleWay2024].
- **Section 5(b), bounded second moments.** If E[E_i E_j] ≤ σ_ij then e_i e_j/σ_ij and mixtures are valid mergers; under nonpositive pairwise correlation, e_i e_j (i ≠ j) is a merger [wangOnlyAdmissibleWay2024].
- **Section 5(c), identical e-variables.** The maximum V_K is a merger, and all admissible mergers of this subclass have the form λ + (1 − λ)V_K, by Lemma 2 applied to e ↦ F(e, …, e); on identical inputs this coincides with a weighted average [wangOnlyAdmissibleWay2024].
- **Section 5(d), exchangeable e-variables.** By the randomised Markov inequality of Ramdas and Wang 2024 (Theorem 4.5 of the arXiv version), F_β(e) = β 1{max_{k ≤ K} ē_k ≥ β} with ē_k the running mean is an e-merging function for exchangeable inputs, β > 1; F_β is neither above nor below any M_λ, and its admissibility is left open [wangOnlyAdmissibleWay2024].

## Setting and assumptions
- A hypothesis is any set of probability measures; results are proved for a single atomless P and transfer to composite hypotheses by Vovk and Wang 2021, Appendix D [wangOnlyAdmissibleWay2024, Sec. 2].
- No dependence assumption whatsoever on (E_1, …, E_K) for Theorem 1; the dependence structure is what the optimal transport supremum ranges over. Independence and sequential structure are explicitly deferred to Vovk and Wang 2021 and Vovk and Wang 2024 [wangOnlyAdmissibleWay2024, Secs 1, 5].
- Merging functions are increasing, Borel, finite-valued on R_+^K; domination and admissibility are pointwise. Upper semicontinuity is obtained for free from Vovk and Wang 2021, Prop. E.1 [wangOnlyAdmissibleWay2024].
- No sequential sampling or optional stopping appears; this is a one-shot combination result.

## Relation to other sources
- [vovkEvaluesCalibrationCombination2021](vovkEvaluesCalibrationCombination2021.md): extends Theorem 3.2 there (symmetric case, complete class {λ + (1 − λ)M_K}) by dropping symmetry; reuses Appendices C, D and E (infinite values, single rich space, upper semicontinuous dominating merger) as proof ingredients; the proof technique is entirely different [wangOnlyAdmissibleWay2024, Secs 1–3].
- [ramdasHypothesisTestingEvalues2025](ramdasHypothesisTestingEvalues2025.md): this paper is the source of the book's Theorem 8.4 (admissible e-mergers are the weighted means) and of the multi-marginal optimal transport duality the book states as Lemma 11.1 to prove it; the book's Section 8 presentation and the e-merging concept page cite "Wang 2025" for exactly this result. The exchangeable merger in Section 5(d) rests on the book's randomised Markov / exchangeable Markov inequalities (Theorems 2.9, 5.6–5.7 in the book's numbering) [wangOnlyAdmissibleWay2024, Sec. 5].
- [xuBringingClosureFalse2025](xuBringingClosureFalse2025.md): closed e-BH takes the arithmetic mean of the e-values in S as its local e-value; Theorem 1 here is the reason no other dependence-free local merger can do better, and the paper's Appendix B (admissible procedures on arbitrary e-values have weighted affine local e-values, via Clerico 2026 and Sun and Wang 2026) is the multiple-testing continuation of this result. Wang's paper itself cites Lee and Ren 2024 for boosting e-BH by averaging [wangOnlyAdmissibleWay2024, Sec. 1].
- [vovkConfidenceDiscoveriesEvalues2023](vovkConfidenceDiscoveriesEvalues2023.md): cited as an application of weighted averaging (discovery matrices); Theorem 1 supports that paper's unproved claim that the arithmetic-mean discovery matrix is admissible among dependence-free procedures [wangOnlyAdmissibleWay2024, Sec. 1].
- [wangFalseDiscoveryRate2021](wangFalseDiscoveryRate2021.md): the e-BH procedure whose boosting by averaging motivates the question [wangOnlyAdmissibleWay2024, Sec. 1].
- [ramdasGametheoreticStatisticsSafe2023](ramdasGametheoreticStatisticsSafe2023.md), [grunwaldSafeTesting2024](grunwaldSafeTesting2024.md), [shaferTestingBettingStrategy2021](shaferTestingBettingStrategy2021.md), [wassermanUniversalInference2020](wassermanUniversalInference2020.md), [grunwaldBeyondNeymanPearsonEvalues2024](grunwaldBeyondNeymanPearsonEvalues2024.md): cited only as background on e-values and their features [wangOnlyAdmissibleWay2024, Sec. 1].
- Mentioned without link: Vovk, Wang and Wang 2022 (admissible p-merging via e-values and optimal transport duality, the closest methodological relative); Vovk and Wang 2024 (martingale merging of sequential e-values); Wang, Wang and Ziegel 2025 (E-backtesting, Lemma EC.2); Koning 2024 (continuous testing, tests as e-values); Ren and Barber 2024 (derandomised knockoffs by averaging e-values); Lee and Ren 2024 (boosting e-BH by conditional calibration).

## Concepts touched
- [e-merging](../concepts/e-merging.md): the complete characterisation of admissible e-merging functions under arbitrary dependence.
- [e-variable](../concepts/e-variable.md): definition used; tests as bounded e-variables (Remark 3).
- [e-bh](../concepts/e-bh.md) and [e-closure-principle](../concepts/e-closure-principle.md): justification for the arithmetic-mean local e-values in closed e-BH and discovery matrices.
- [calibrator](../concepts/calibrator.md): admissible calibrators composed with survival functions give extra admissible mergers under fixed marginals (Section 5(a)).

## Versions
The arXiv v2 text is dated March 2025 and thanks the editors and two referees; the Biometrika 112(2) version is the version of record. No material differences are known; theorem numbering above follows v2.

## Open questions / gaps
- Admissibility of the exchangeable merger F_β = β 1{max_k ē_k ≥ β} is stated as unclear [wangOnlyAdmissibleWay2024, Sec. 5(d)].
- Complete classes of mergers for the subclasses in Section 5 (fixed marginals, bounded second moments, exchangeable) are not characterised; only the identical case gets a full answer [wangOnlyAdmissibleWay2024, Sec. 5].
- Not in the bib: Vovk, Wang and Wang 2022 (admissible p-merging); Vovk and Wang 2024 (merging sequential e-values via martingales); Wang, Wang and Ziegel 2025 (E-backtesting); Koning 2024 (continuous testing); Lee and Ren 2024; Ren and Barber 2024.
