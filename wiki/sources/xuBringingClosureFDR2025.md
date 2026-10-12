---
citekey: xuBringingClosureFDR2025
title: "Bringing closure to FDR control: beating the e-Benjamini–Hochberg procedure"
authors: [Ziyu Xu, Lasse Fischer, Aaditya Ramdas]
year: 2025
status: preprint
public: true
note: "The short first paper on FDR closure: test every intersection hypothesis with the arithmetic mean of its e-values, accept the largest top-k set whose every intersection e-value beats its FDP over α, and e-BH, minimally adaptive e-BH and Benjamini–Yekutieli all turn out to be inadmissible; superseded by the merged e-Closure paper."
links:
  pdf: "https://arxiv.org/pdf/2504.11759v3"
  arxiv: "https://arxiv.org/abs/2504.11759"
  doi: "10.48550/arXiv.2504.11759"
  video: ""
tags: [e-closure, closed-testing, fdr, e-bh, closed-e-bh, benjamini-yekutieli, inadmissibility, compound-e-values, e-merging, calibrator, post-hoc-validity, error-metrics, e-holm, stochastic-rounding, boosting, dynamic-programming, simulations]
ingested: 2026-10-08
version: "arxiv 2504.11759v3 (3 Sep 2025, 18 pages); the authors' footnote states it is subsumed by the merged paper arXiv 2509.02517 (xuBringingClosureFalse2025)"
---

# Bringing closure to FDR control: beating the e-Benjamini–Hochberg procedure

## Summary
This is the 18-page predecessor of the general e-Closure paper [xuBringingClosureFalse2025]; it introduces the FDR closure idea in its simplest form and is now, by the authors' own footnote, subsumed by that work [xuBringingClosureFDR2025, p. 2]. Given K arbitrarily dependent e-values, test each intersection hypothesis H_A by the arithmetic mean E_A = |A|^{-1} Σ_{i∈A} E_i, call a rejection set R a candidate if E_A ≥ FDP_A(R)/α for every A ⊆ [K], and output the largest top-k set of e-values that is a candidate: this closed e-BH procedure controls FDR at α (Proposition 1) and always contains the e-BH rejection set (Proposition 2) and the minimally adaptive e-BH set of Ignatiadis, Wang and Ramdas (Proposition 3), with strict gains already at K = 3 (Example 1) [xuBringingClosureFDR2025]. Writing Benjamini–Yekutieli as e-BH on calibrated p-values gives a closed BY procedure that dominates BY, so BY is inadmissible even among deterministic procedures (Proposition 5) [xuBringingClosureFDR2025, Sec. 2.1]. The closure principle itself is stated in the direction "every FDR-controlling procedure is an e-closed procedure" via the implicit e-values E_A = FDP_A(R)/α (Theorem 1), with an α-free variant for post-hoc FDP-controlling families (Theorem 2), and is generalised to any expectation-based error metric F_A, which permits a post-hoc choice of the error metric, e.g. between e-Holm and closed e-BH (Theorem 3, Example 2) [xuBringingClosureFDR2025, Secs 3–4]. An O(K³) dynamic programme computes the closed set, stochastic rounding, boosting and product merging carry over, and Gaussian simulations show the closed procedures beating e-BH, minimally adaptive e-BH and BY at matched FDR [xuBringingClosureFDR2025, Algorithm 1, Secs 5–6].

## Main results

### Closed e-BH (Section 2)
- Eq. (1): E_A = |A|^{-1} Σ_{i∈A} E_i, the symmetric admissible e-merger of [vovkEvaluesCalibrationCombination2021]; sup_{P∈H_A} E_P[E_A] ≤ 1 [xuBringingClosureFDR2025].
- Eq. (2): candidate sets C = {R ⊆ [K] : E_A ≥ FDP_A(R)/α for all A ⊆ [K]}, with FDP_A(R) = |R ∩ A|/(|R| ∨ 1). Proposition 1: any R ∈ C has FDR ≤ α (deterministic inequality FDP_{A*}(R) ≤ α E_{A*}, then take expectations).
- Eq. (3): closed e-BH rejects R_[:k̂] with k̂ = max{i : R_[:i] ∈ C}, R_[:i] the i largest e-values; only top-k sets are searched, so R^closed is a largest element of C but not the whole candidate collection.
- Proposition 2: the self-consistent sets C^SC = {R : min_{i∈R} E_i ≥ K/(α|R|)} satisfy C^SC ⊆ C, hence R^eBH ⊆ R^closed; the proof chain (4)–(5) lower-bounds E_A by K^{-1}|A ∩ R| min_{i∈R} E_i and the slack in these inequalities is where the power comes from.
- Proposition 3: minimally adaptive e-BH (test the global null with E_[K] ≥ 1/α, then run e-BH at level αK/(K − 1); Ignatiadis, Wang and Ramdas 2024, Section S3.2) is also contained in closed e-BH, for every K. The two coincide at K = 2 and differ for K ≥ 3.
- Thresholds: closed e-BH imposes only E_j ≥ 1/(α k̂) on each rejected hypothesis plus joint constraints (the m smallest rejected e-values must average at least m/(α k̂)), whereas e-BH demands K/(α k) and minimally adaptive e-BH (K − 1)/(α k) per hypothesis [xuBringingClosureFDR2025, Sec. 2].
- Example 1: E = (60, 39, 11), α = 0.05: e-BH rejects one, minimally adaptive e-BH two, closed e-BH all three (each E_i > 20/3, pairwise means > 40/3, overall mean > 20).
- Algorithm 1: for k = K down to k^eBH + 1, r false discoveries among R_[:k] and m total nulls, the worst case takes the r smallest e-values inside R_[:k] and the m − r smallest outside; the estimated FDR of R_[:k] is max_{r,m} (r/k)/E_{A(k,r,m)}, an O(K²) table per k, hence O(K³) overall.
- Proposition 4: with C_β the candidate set at level β, E[sup_{β∈[0,1]} sup_{R∈C_β} FDP_{A*}(R)/β] ≤ 1 (0/0 = 1), i.e. both the level and the rejected set may be chosen after seeing the data, as for e-BH in Grünwald 2024, Xu, Wang and Ramdas 2024 and Koning 2024.

### Closed BY (Section 2.1)
- BY at level α equals e-BH applied to E_i = f^{BY(α,K)}(P_i) with the step calibrator of Xu, Wang and Ramdas 2024 (indicator P_i ≤ α/ℓ_K, ℓ_K the K-th harmonic number), as shown in [wangFalseDiscoveryRate2021]; Proposition 5: closed e-BH on these e-values contains R^BY. Hence BY is inadmissible among deterministic procedures; Xu and Ramdas 2023 had shown this only with external randomisation [xuBringingClosureFDR2025].
- Here the calibrator is the fixed K-dependent one; the |S|-dependent calibrator that defines closed BY in the merged paper [xuBringingClosureFalse2025, Lemma 27] is not yet present.

### Compound e-values (Section 2.2)
- Eq. (8)–(9): for compound e-values with Σ_{i∈A} E_A[Ẽ_i] ≤ K, E_A = K^{-1} Σ_{i∈A} Ẽ_i is an e-value for H_A; Proposition 6: compound e-BH ⊆ closed compound e-BH. Equality is conjectured on simulation evidence and left open; the merged paper proves it [xuBringingClosureFalse2025, Thm 25].
- The authors present their reduction (one e-value per intersection hypothesis) as complementary to the universality of e-BH with compound e-values of [ignatiadisAsymptoticCompoundEvalues2024].

### The FDR closure principle (Section 3)
- Theorem 1: for any FDR-controlling procedure R, E_A = FDP_A(R)/α is a valid e-collection, R ∈ C, and C = {R, ∅}, so the dominant e-closed procedure built from it is R itself: every FDR-controlling procedure is an e-closed procedure. Only the sufficiency-plus-representation direction for single procedures is given; the "if and only if" for simultaneous collections is [xuBringingClosureFalse2025, Thm 6].
- Theorem 2: for a post-hoc FDP-controlling family (R_β)_{β∈[0,1]} with E[sup_β FDP_{A*}(R_β)/β] ≤ 1, Ē_A = sup_β FDP_A(R_β)/β is an α-free e-collection whose closed procedure recovers or improves R_α; Ē_A ≥ E_A, and Ē_A can be positive for i ∉ R_α, so closure can genuinely add power there, whereas closing (12) is idempotent.

### General error metrics (Section 4)
- For F = (F_A) with sup_A E_A[F_A(R)] ≤ α required (k-FWER, PFER, FDX-γ listed), C(F) = {R : E_A ≥ F_A(R)/α ∀A}; Theorem 3: every R ∈ C(F) controls F, and E_A = F_A(R)/α represents any controlling R.
- Post-hoc error metric: for a family 𝓕 and closed choices R_F ∈ C(F), sup_A E_A[sup_{F∈𝓕} F_A(R_F)] ≤ α. Example 2: with arithmetic-mean E_A, FDP gives closed e-BH and the FWER loss 1{|A ∩ R| > 0} gives e-Holm ([vovkEvaluesCalibrationCombination2021]; Hartog and Lei 2025), so one may decide between them after seeing the data.
- Remark 1: E_A = φ_A/α recovers Marcus–Peritz–Gabriel closed testing for FWER and the Goeman–Solari simultaneous true-discovery bound d(R) = min{|R ∖ A| : φ_A = 0}. Remark 2: multiple testing as a composite GNP problem whose maximally compatible rule is the closed procedure, with the richness condition of [grunwaldBeyondNeymanPearsonEvalues2024] failing because FDP is discrete.

### Extensions and simulations (Sections 5–6)
- Stochastic rounding (Xu and Ramdas 2023) per intersection e-value, with data-dependent levels α̂_{A,k} = α/FDP_A(R_[:k]); the rounded collection never rejects fewer and rejects k̂ + 1 with positive probability when min_A (E_A − α̂_{A,k̂}^{-1}) > 0.
- Boosting with a per-A truncation T_A onto the support {r/(αk) : k ∈ [K], r ≤ k ∧ |A|} ∪ {0}, new relative to e-BH boosting of [wangFalseDiscoveryRate2021]; product merging under independent nulls.
- Simulations (code github.com/neilzxu/closed-ebh): X_i ~ N(0,1) under nulls, N(µ,1) with µ = 3 otherwise, E_i = exp(λX_i − λ²/2) with λ = µ, α = 0.1, π_0 ∈ {0.5, 0.7, 0.9}, K ≤ 200, 1000 trials; closed e-BH has visibly higher TPR than e-BH and minimally adaptive e-BH with FDR below α (Figure 1). Closed BY vs BY and minimally adaptive BY on P_i = 1 − Φ(X_i) under a Toeplitz-like alternating-sign covariance |Cov(X_i, X_j)| = exp(−|i − j|/10)/5 shows substantial gains (Figure 2).

## Setting and assumptions
- K fixed hypotheses, true null set A*, data summarised into K e-values (or p-values) under arbitrary dependence; a procedure is a map from data to a single rejection set; FDR = E[FDP_{A*}(R)] [xuBringingClosureFDR2025, Sec. 1].
- No sequential element, no optional stopping; the e-values are taken as given.
- Closed e-BH and the closure principle need only that each E_A be an e-value for H_A; closed BY needs only p-values (arbitrary dependence); compound e-BH needs the compound condition (8); product merging needs independent null e-values.
- "Improvement" is set inclusion R^eBH ⊆ R^closed, with strictness shown by example and simulation; the pointwise "uniform improvement" definition and the simultaneity notion come later [xuBringingClosureFalse2025, Def. 16].

## Relation to other sources
- [xuBringingClosureFalse2025](xuBringingClosureFalse2025.md): the merged successor. It adds the necessary-and-sufficient principle for simultaneous collections (Thm 6, Thm 14), the full mean-consistent collection rather than top-k sets (Lemma 52), the uniform-improvement theorem with the "reject all where e-BH rejects none" example (Thm 17, Example 20), the proof of the compound conjecture (Thm 25), the |S|-dependent BY calibrator (Thm 28), closed Su and the negative result for BH-type e-collections (Thms 34, 37), knockoffs, post-hoc α for all e-Closure procedures (Thm 48), partitioning hypotheses, the O(m² log m) algorithm, real-data experiments and software. Everything in this paper is contained there, mostly with sharper statements.
- [wangFalseDiscoveryRate2021](wangFalseDiscoveryRate2021.md): defines e-BH, self-consistency, boosting, and the calibrated-p-value representation of BY that Proposition 5 exploits; this paper shows e-BH is inadmissible without any extra information or randomisation.
- [ignatiadisAsymptoticCompoundEvalues2024](ignatiadisAsymptoticCompoundEvalues2024.md): compound e-values and the universality of e-BH, to which Theorem 1 is the complementary intersection-hypothesis reduction; minimally adaptive e-BH (from Ignatiadis, Wang and Ramdas 2024, Section S3.2) is dominated by Proposition 3. See also [ignatiadisEvaluesUnnormalizedWeights2022](ignatiadisEvaluesUnnormalizedWeights2022.md).
- [vovkEvaluesCalibrationCombination2021](vovkEvaluesCalibrationCombination2021.md): the arithmetic mean as symmetric admissible e-merger (eq. 1) and e-Holm (Example 2). [vovkConfidenceDiscoveriesEvalues2023](vovkConfidenceDiscoveriesEvalues2023.md): FWER control and simultaneous FDP bounds by closure of the mean, the closest prior use of e-values in closed testing (Section 7). [hartogFamilyWiseError2025] (in the bib, no source page) extends it to graphical procedures.
- [ramdasHypothesisTestingEvalues2025](ramdasHypothesisTestingEvalues2025.md): Section 9.6 of the book presents closed e-BH in essentially this paper's form (Thms 9.32–9.36); cited here as the survey of e-BH developments.
- [grunwaldBeyondNeymanPearsonEvalues2024](grunwaldBeyondNeymanPearsonEvalues2024.md), [koningPosthocAlphaHypothesis2023](koningPosthocAlphaHypothesis2023.md), [xuPostselectionInferenceEvalue2022](xuPostselectionInferenceEvalue2022.md): sources of the post-hoc validity notion behind Proposition 4 and Theorem 2; the BY calibrator f^{BY(α,K)} is from Xu, Wang and Ramdas 2024.
- [goemanUniformImprovementBenjaminiHochberg2026](goemanUniformImprovementBenjaminiHochberg2026.md): not cited here; the question of improving BH by closure, which this paper does not pose explicitly, is answered there.
- In the bib without a source page: [renDerandomizedKnockoffsLeveraging2022] (knockoffs as e-BH, listed among the settings where closed e-BH applies).
- Not in the bib: Xu and Ramdas 2023 (stochastic rounding, randomised BY); Li and Zhang 2025 (BH as e-BH); Blier-Wong and Wang 2024; Lee and Ren 2024, Lee, Popov and Ren 2025 (conditional calibration); Marcus, Peritz and Gabriel 1976; Sonnemann and Finner 1988; Goeman and Solari 2011; Goeman, Hemerik and Solari 2021.

## Concepts touched
- [e-closure-principle](../concepts/e-closure-principle.md)
- [e-bh](../concepts/e-bh.md)
- [e-merging](../concepts/e-merging.md)
- [calibrator](../concepts/calibrator.md)
- [post-hoc-validity](../concepts/post-hoc-validity.md)

## Versions
v3 (3 Sep 2025) carries the footnote that the paper is subsumed by the merged work with Solari, de Heide and Goeman [xuBringingClosureFalse2025]. Earlier versions are not in the repository; the ingested text is v3.

## Open questions / gaps
- Whether closed compound e-BH equals compound e-BH (conjectured here; proved in [xuBringingClosureFalse2025, Thm 25]).
- Admissibility of closed e-BH itself is not addressed; the GNP admissibility theory of [grunwaldBeyondNeymanPearsonEvalues2024] does not apply because FDP is discrete (Remark 2). Later settled for weighted-mean closed e-BH by Sun and Wang 2026, per the merged paper.
- The search over top-k sets only; sets outside the e-value ordering that lie in C are not considered here.
- Boosting under joint-distribution knowledge, and combining closed e-BH with conditional-calibration boosting (Lee and Ren 2024), are left as directions (Sections 5, 7).
