---
citekey: hartogFamilyWiseError2025
title: "Family-wise Error Rate Control with E-values"
authors: [Will Hartog, Lihua Lei]
year: 2025
status: preprint
public: true
note: "Closed testing with e-values: averaging e-values inside every intersection test beats Bonferroni on inverse e-values, gives post-hoc and always-valid FWER control that p-value closure cannot, and the e-Holm, e-Fallback and e-graphical (DAG) procedures all get polynomial-time algorithms despite losing consonance."
links:
  pdf: "https://arxiv.org/pdf/2501.09015v4"
  arxiv: "https://arxiv.org/abs/2501.09015"
  doi: "10.48550/arXiv.2501.09015"
  video: ""
tags: [multiple-testing, fwer, closed-testing, e-merging, post-hoc, anytime-valid, graphical-approach, algorithms]
ingested: 2026-10-08
version: "arxiv 2501.09015v4"
---

# Family-wise Error Rate Control with E-values

## Summary
Hartog and Lei formalise e-value-based closed testing: a family of e-values (e_I)_{I ⊆ [n]}, one per intersection hypothesis H_I, rejects H_i iff e_I ≥ 1/α for every I ∋ i, with adjusted e-value e*_i = min_{I ∋ i} e_I [hartogFamilyWiseError2025, Sec. 2.1]. Because max_{i ∈ H_0} e*_i ≤ e_{H_0} (Lemma 2.1), the procedure inherits every guarantee of the single e-value e_{H_0}: strong FWER, post-hoc FWER for data-dependent α̂, post-hoc anytime-valid FWER at stopping times, and always-valid FWER over all times when the local tests are e-processes [Thms 2.3–2.5]; p-Holm fails post-hoc FWER with infinite risk. The main local test is weighted e-Bonferroni e_I = Σ_{i ∈ I} w_i(I) e_i, which rejects whenever weighted p-Bonferroni on the inverse-e p-values does, so every e-graphical approach (weights from a Bretz et al. 2009 graph) is at least as powerful as its inverse-e p-counterpart [Sec. 3.1]. For running maxima of independent e-processes, which are not e-values, closure of weighted e-Bonferroni controls FWER at B_{n_0}(α) = α + ((n_0 − 1)/n_0) α² log(1/α) + O(α²) [Thm 3.1]. Averaging is not consonant, so the O(n²) sequential-rejection shortcut of p-graphical approaches is lost; the paper supplies an O(n) threshold rule for e-Holm [Thm 4.2], O(n) stack algorithms for e-Fallback [Algs 1–3, Thms 5.2–5.3], and an O(n|E|) dynamic-programming algorithm for any DAG [Alg. 4, Thm 6.4]. Simulations with SPRT test martingales and semi-synthetic New Yorker caption-contest bandit data show consistent gains over inverse-e p-procedures and mixed but often favourable results against always-valid p-values [Secs 7–8].

## Main results
- **Lemma 2.1 / Prop. 2.2**: max_{i ∈ H_0} e*_i ≤ e_{H_0}, hence FWER = P(max_{i∈H_0} e*_i ≥ 1/α) ≤ P(e_{H_0} ≥ 1/α) ≤ α under arbitrary dependence among the e_I.
- **Theorem 2.3 (post-hoc FWER)**: for any data-dependent α̂, E[1{max_{i∈H_0} e*_i ≥ 1/α̂}/α̂] ≤ 1. Counterexample for p-Holm: with independent uniform null p-values and α̂ = min_i p*_i the post-hoc risk is +∞ (Sec. 2.2).
- **Theorem 2.4 (post-hoc anytime-valid FWER)**: with e-processes e_{It} in the global filtration F_t, for any stopping time τ and F_τ-measurable α̂, E[1{max_{i∈H_0} e*_{iτ} ≥ 1/α̂}/α̂] ≤ 1.
- **Theorem 2.5 (always-valid FWER)**: for fixed α, P(max_{i∈H_0} sup_t e*_{it} ≥ 1/α) ≤ α via Ville's inequality, so rejections may use past peaks of the adjusted processes.
- **Weighted e-Bonferroni (eq. 3.2)**: e_I = Σ_{i∈I} w_i(I) e_i with Σ_{i∈I} w_i(I) ≤ 1 rejects whenever max_{i∈I} w_i(I) e_i ≥ 1/α, i.e. whenever weighted p-Bonferroni with p_i = 1/e_i rejects (eq. 3.1); the comparison says nothing about other p-values. Remark 4.1: compound e-values (expectations summing to at most |I| on each I) suffice.
- **Theorem 3.1 (pseudo e-values)**: for independent e-processes, closure of weighted e-Bonferroni applied to ẽ_i = max_t e_{it} has FWER ≤ B_{n_0}(α) := P(Σ_{k=1}^{n_0} Y_k ≥ n_0/α), Y_k i.i.d. Pareto(1), with B_{n_0}(α) = α + ((n_0−1)/n_0) α² log(1/α) + O_{n_0}(α²); B_K(0.05) stays close to 0.05 for a wide range of K (Fig. 1), with B_30(0.05) = 0.07 and the exact-level correction α′ = B_50^{-1}(0.05) = 0.038 (Sec. 8.4). Remark 3.2: any independent p-values give pseudo e-values 1/p_i with the same bound.
- **Theorem 4.2 (e-Holm threshold)**: with J* = {j : e_j < 1/α}, e-Holm rejects H_i iff e_i ≥ 1/α + Σ_{j∈J*}(1/α − e_j); O(n), no sorting; the threshold is at most (|H_0|+1)/α whereas inverse-e p-Holm needs e_(1) ≥ n/α, so e-Holm adapts to the number of nulls (Sec. 4.2, Fig. 2 with all-or-nothing e-values 1{X_i ≥ 1−c}/c).
- **Section 5 (e-Fallback, chain graph)**: Lemma 5.1 (minimiser has i as its largest element); Algorithm 1 O(n²) dynamic programme with Theorem 5.2 (m_i = α e*_i); Theorem 5.3 reverse search via j(i) = max{j < i : e_j ≤ e_i}, expected O(n) for exchangeable e-values (Thm F.1) but O(n²) worst case; Lemma 5.4 and Algorithm 3 stack search in O(n), the minimising set being the backward cumulative minima (eq. 5.2).
- **Section 6 (e-DAG)**: non-consonance example (e_1,e_2,e_3) = (25,25,10), α = 0.05: e_{123} = 20 ≥ 20 but e_{13} = e_{23} = 17.5; weights w_i(I) as hitting probabilities of a random walk on the expanded graph (eq. 6.1, 6.3); Definition 6.1 and Lemmas 6.2–6.3 rewrite e_I as (1/α) Σ_j α_j e_j^{(I)} with a children recursion; Algorithm 4 and Theorem 6.4 give e*_i = m_i/α in O(Σ_i N_i) ≤ O(n|E|) = O(n³) worst case, O(n log n) on a balanced binary tree. Appendix E extends to Index-Local DAGs (cyclic Fallback, two-endpoint gatekeeper) at O(n²|E|).
- **Theorem B.1 (post-hoc always-valid)**: Theorem 2.5 fails for data-driven α̂ (two-process counterexample after Tavyrikov et al. 2025, post-hoc risk ≥ 4/3 at t = 1), but applying an adjuster A with ∫_1^∞ A(x)/x² dx ≤ 1 to the closed-testing output on running maxima restores E[1{max_{i∈H_0} A(ẽ*_i) ≥ 1/α̂}/α̂] ≤ 1; by Jensen, adjusting after closure beats adjusting before for concave A.
- **Section 7 simulations**: Gaussian streams, SPRT martingale e_{it} = Π_s exp(μ̂ Y_{is} − μ̂²/2) (eq. 7.1); 20 hypotheses, 5 non-nulls, μ_alt ∈ {0.5,1,1.5,2}, 1000 runs: e-Holm beats always-valid p-Holm on time to first rejection with probability ≥ 0.05 above ties and ≈ 10% shorter stopping times when they differ (Fig. 4); at 25 steps e-Holm > ep-Holm and em-Holm > p-Holm in power, em(α′)-Holm ≈ p-Holm (Figs 5–6). Three-factor 2³ factorial DAG, β_1 = β_3 = 0.5, β_13 varying: e-DAG consistently beats ep-DAG, mixed against p-DAG, favourable only at β_13 = 2 (Figs 8–11).
- **Section 8 semi-synthetic**: New Yorker contest #895 (4958 captions, 777 820 votes), lilUCB sampling with ε = 0.4, betting e-processes with η = 0.25; e-Holm on 20 non-nulls and 30 nulls improves on p-Holm with probability 0.79 (ratio 0.988 of pulls); e-DAG on 6 contrasts, 48 captions, 1000 pulls, AIPW estimators: ratio 0.897, improvement probability 0.93; fixed-sample t-test p-values with em-Holm more powerful than p-Holm with empirical FWER controlled, em(α′)-Holm ≈ p-Holm (Fig. 12).
- **Section 9 discussion**: randomised thresholds U_I/α keep FWER under arbitrary dependence of the uniforms; decreasing densities allow level 2α (Blier-Wong and Wang 2024); logical constraints via J(I) preserve Section 2 guarantees; post-hoc FDP bounds ℓ_{1−α}(R) by brute force only for general graphs.

## Setting and assumptions
- n elementary nulls H_1,…,H_n, true-null set H_0, logically independent unless Sec. 9.2; strong FWER throughout.
- Static setting: arbitrary dependence among the e_i and the e_I; no distributional assumption beyond E_{H_I}[e_I] ≤ 1 (or compound validity, Remark 4.1).
- Sequential setting: e-processes with respect to the global filtration F_t of all arms ("global e-processes" in Wang, Dandapanthula and Ramdas 2025); stopping times must be F_t-adapted; sub-filtration e-processes need adjusters (Choe and Ramdas 2024).
- Theorem 3.1 and Remark 3.2 need independence across the elementary e-processes or p-values; the bound is asymptotic in α → 0 for fixed n_0.
- The p-value comparisons are against inverse-e p-values (exact dominance) or always-valid p-values 1/max_t e_{it} (empirical); with fixed samples and parametric nulls the authors concede optimal p-values can beat the best e-values by more than closure recovers (Sec. 1.4, Sec. 8.4).
- Optional stopping and continuation allowed in the sequential results; post-hoc α̂ allowed in Theorems 2.3, 2.4, B.1 but not 2.5.

## Relation to other sources
- [vovkEvaluesCalibrationCombination2021](vovkEvaluesCalibrationCombination2021.md): e-Holm is the closure of the arithmetic mean there (Thm 5.1, Algorithm 1, O(n log n) adjusted e-values); this paper adds the O(n) rejection threshold (Thm 4.2), weights, general graphs, and the post-hoc and sequential guarantees. Inverse e-values as the only admissible e-to-p calibrator (Prop. 2.2 there) underpin the dominance claim.
- [vovkConfidenceDiscoveriesEvalues2023](vovkConfidenceDiscoveriesEvalues2023.md): Vovk and Wang 2023/2024 give the efficient FDP bounds for e-Holm by symmetry; Hartog and Lei leave FDP bounds for asymmetric e-graphical approaches open (Sec. 9.3).
- [wangOnlyAdmissibleWay2024](wangOnlyAdmissibleWay2024.md): cited for the inverse e-value being the only admissible p-value without distributional assumptions, which makes the e-Bonferroni versus p-Bonferroni comparison exact.
- [xuBringingClosureFalse2025](xuBringingClosureFalse2025.md): the e-Closure principle covers FDR and can choose FWER post hoc (Thm 12 there), but is tied to simultaneous FDR control and said to be less powerful than the FWER-focused closure here (Sec. 2.1). Both use the arithmetic mean as local e-value.
- [koningPosthocAlphaHypothesis2023](koningPosthocAlphaHypothesis2023.md) and [grunwaldBeyondNeymanPearsonEvalues2024](grunwaldBeyondNeymanPearsonEvalues2024.md): single-hypothesis post-hoc validity generalised to strong post-hoc FWER (Thm 2.3); Koning's Appendix C.2 had only weak post-hoc FWER.
- [koningAnytimeValidityFree2026](koningAnytimeValidityFree2026.md), [howardTimeuniformNonparametricNonasymptotic2021](howardTimeuniformNonparametricNonasymptotic2021.md), [turnerExactAnytimevalidConfidence2023](turnerExactAnytimevalidConfidence2023.md): anytime and always validity for one hypothesis, lifted to FWER by Theorems 2.4–2.5.
- [ramdasAdmissibleAnytimevalidSequential2022](ramdasAdmissibleAnytimevalidSequential2022.md), [ramdasGametheoreticStatisticsSafe2023](ramdasGametheoreticStatisticsSafe2023.md): e-process definitions and the anytime- versus always-valid distinction used in Section 2.3.
- [villeEtudeCritiqueNotion1939](villeEtudeCritiqueNotion1939.md): Ville's inequality drives Theorem 2.5, the pseudo e-values and the always-valid p-values of the comparison.
- [ignatiadisAsymptoticCompoundEvalues2024](ignatiadisAsymptoticCompoundEvalues2024.md) and [wangFalseDiscoveryRate2021](wangFalseDiscoveryRate2021.md): compound e-values suffice for e-Holm (Remark 4.1).
- [wassermanUniversalInference2020](wassermanUniversalInference2020.md): universal inference as a motivating source of e-values for irregular models.
- [koolenLogoptimalAnytimevalidEvalues2022](koolenLogoptimalAnytimevalidEvalues2022.md): not cited; Koolen and Vovk 2014 "Buy low, sell high" supplies the adjuster condition of Theorem B.1.
- Without pages: Fischer and Ramdas 2024 (online closed testing with e-values, product merging under independence), Tavyrikov, Goeman and de Heide 2025 (adjusters for carefree e-process multiple testing), Choe and Ramdas 2024 (adjusters across filtrations), Wang, Dandapanthula and Ramdas 2025 (stopped e-BH, global versus local e-processes), Johari et al. 2022 (always-valid p-values), Bretz et al. 2009 (graphical approach), Blier-Wong and Wang 2024 (improved thresholds), Ramdas and Manole 2026 (randomised Markov), Koning 2024 "Continuous testing".

## Concepts touched
- [e-merging](../concepts/e-merging.md): weighted arithmetic means as local tests, exact dominance over Bonferroni on inverse e-values, loss of consonance.
- [e-closure-principle](../concepts/e-closure-principle.md): e-closed testing for FWER, Lemma 2.1, post-hoc and sequential FWER, e-graphical algorithms.
- [post-hoc-validity](../concepts/post-hoc-validity.md): post-hoc strong FWER (Thm 2.3), post-hoc anytime-valid FWER (Thm 2.4), post-hoc always-valid via adjusters (Thm B.1), p-Holm counterexample.
- [e-process](../concepts/e-process.md) and [villes-inequality](../concepts/villes-inequality.md): always-valid FWER (Thm 2.5), running maxima as pseudo e-values, Pareto coupling (Thm 3.1).
- [calibrator](../concepts/calibrator.md): inverse e-values as the only admissible p-values; adjusters A with ∫ A(x)/x² ≤ 1 as e-to-e calibrators of running maxima.
- [optional-stopping](../concepts/optional-stopping.md): global versus sub-filtration e-processes in multi-arm stopping (Sec. 7.1).
- fwer-graphical-procedures (new): graphical and sequentially rejective FWER procedures (Holm, Fallback, Bretz-type DAGs, gatekeeping) and their e-value versions with algorithms.

## Versions
Text layer is arXiv v4 (17 May 2026). Earlier versions are not in the repository; the v4 abstract already includes the DAG dynamic programme and e-Fallback algorithms, so no material renaming is known.

## Open questions / gaps
- Whether randomised thresholds U_I/α retain post-hoc or always-valid FWER (Sec. 9.1).
- Threshold constants c_I for e-values with known covariance structure, after Bretz et al. 2011 (Sec. 9.1).
- Dynamic programming under logical constraints J(I) (Sec. 9.2); O(n) algorithms for trees via depth-first stacks (Sec. 6.2); FDP lower bounds ℓ_{1−α}(R) for asymmetric e-graphical approaches at large n (Sec. 9.3).
- Exact rather than asymptotic FWER for pseudo e-values; dependence between elementary e-processes is not covered by Theorem 3.1.
- Fischer and Ramdas 2024 (online e-closed testing), Tavyrikov, Goeman and de Heide 2025, Choe and Ramdas 2024, Wang, Dandapanthula and Ramdas 2025 and Blier-Wong and Wang 2024 are cited but not in the bib.
