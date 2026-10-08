---
citekey: goemanUniformImprovementBenjaminiHochberg2026
title: "A uniform improvement of the Benjamini–Hochberg procedure via e-closure"
authors: [Jelle Goeman]
year: 2026
status: preprint
public: true
note: "Closed BH never rejects fewer hypotheses than Benjamini–Hochberg, often rejects many more, stays valid under PRDS, and is built entirely from the e-Closure principle: a family of e-values indexed by subsets of hypotheses."
links:
  pdf: "https://arxiv.org/pdf/2606.01854"
  arxiv: "https://arxiv.org/abs/2606.01854"
  doi: "10.48550/arXiv.2606.01854"
  video: ""
tags: [e-closure, e-collection, fdr, benjamini-hochberg, prds, uniform-improvement, multiple-testing, closed-testing, adaptive-fdr, minimally-adaptive-bh, simultaneous-fdr, adjusted-p-values, software]
ingested: 2026-10-08
version: "arxiv 2606.01854v2 (10 June 2026, 27 pages), per meta.yaml"
---

# A uniform improvement of the Benjamini–Hochberg procedure via e-closure

arXiv 2606.01854v2, stat.ME, 10 June 2026. Single author (Leiden University Medical Center). Numbering below follows v2: Sections 1–9, Appendix A (proofs), Appendix B (adjusted p-value algorithm).

## Summary
The paper solves the open problem left by the e-Closure paper [xuBringingClosureFalse2025](xuBringingClosureFalse2025.md) of whether the Benjamini–Hochberg (BH) procedure itself can be uniformly improved through e-Closure. It defines a family of "BH-like" step-up procedures parameterised by an integer matrix of horizons r_{k,s} (0 ≤ k ≤ m, 1 ≤ s ≤ m), builds for each member an e-collection (e_S)_{S ⊆ [m]} in which e_S is the average over i ∈ S of the thresholded indicators 1{p_i ≤ a_{|S|}}/a_{|S|}, and shows via the e-Closure theorem that the procedure controls FDR at α whenever E[e_N] ≤ 1 for the set N of true nulls (Theorem 12). This "minimal sufficient condition" (Assumption 4) is implied by PRDS through the Blanchard–Roquain lemma (Theorem 8), and if it fails by a factor γ the FDR is still at most γα (Theorem 13). Minimally adaptive BH (MABH, Solari and Goeman 2017) is the most cautious member of the family (Lemma 14) and cannot be uniformly improved within it (Proposition 15), but a BH-like method uniformly improves BH iff r_{k,s} ≤ ks/(m − k) in the free region (Proposition 16); closed BH is the most ambitious such choice. Closed BH exploits p-values that are much smaller than the BH threshold to let later, larger p-values be rejected; the power gain over BH is large when the number of BH rejections is already substantial (Proposition 18; simulations in Section 8), while its simultaneity is essentially nil (Theorem 19). Algorithms with O(m) memory and roughly O(m log m + r²) time are implemented in the R package eClosure [goemanUniformImprovementBenjaminiHochberg2026].

## Main results

### BH-like methods (Section 2)
- **Horizon matrix**: r_{k,s} = k for k + s ≤ m + 1 except r_{1,m} = m (eq. 1); for k + s > m + 1 free subject to k ≤ r_{k,s} ≤ m (eq. 2) and r_{k−1,s} ≤ r_{k,s} ≤ b_{k,s} (eq. 3), where b_{k,s} = m ∧ (m − s)(k + s − m − 1) r_{k−1,s} / ((k + s − m)(m − s) − r_{k−1,s}) when the denominator is positive and m otherwise. Lemmas 1–2: the constraints are never contradictory (b_{k,s} ≥ r_{k−1,s} and b_{k,s} ≥ k) [goemanUniformImprovementBenjaminiHochberg2026].
- **Thresholds**: a_{k,s} = (k + s − m) r_{k,s} α / ((r_{k,s} + s − m) s) if r_{k,s} > k, else kα/s (eq. 4); a_{k,m} = kα/m always, the BH critical values. Thresholded horizons r̃_{k,s} = r_{k,s} 1{p_(k) ≤ a_{k,s}}, cumulative maxima v_{k,s} = max_{k' ≤ k} r̃_{k',s}, and the number of rejections r = max{k : v_{k,s} ≥ k for all s} (eq. 5); reject the r smallest p-values I_r. Worked example with m = 7 (Tables 2–4): closed BH rejects 6 where BH rejects 2 [goemanUniformImprovementBenjaminiHochberg2026].

### The e-collection and its validity (Section 3)
- **Theorem 3 (e-Closure, from Xu et al.)**: if an e-collection (e_S) with E[e_N] ≤ 1 satisfies e_S ≥ |R ∩ S| / ((|R| ∨ 1) α) for all S, then R controls FDR (eq. 6–7) [goemanUniformImprovementBenjaminiHochberg2026].
- **Construction (eq. 8–9)**: k_s = max{k ≤ r : p_(k) ≤ a_{k,s}}, a_s := a_{k_s, s} (random); e_∅ = 1, e_S = 0 if k_{|S|} = 0, otherwise e_S = Σ_{i ∈ S} 1{p_i ≤ a_{|S|}} / (|S| a_{|S|}), an arithmetic mean of per-hypothesis e-values with a subset-size-dependent threshold [goemanUniformImprovementBenjaminiHochberg2026].
- **Assumption 4 (minimal sufficient condition)**: E[(1/|N|) Σ_{i ∈ N} 1{p_i ≤ a_{|N|}} / a_{|N|}] ≤ 1, a single expectation of a single random variable [goemanUniformImprovementBenjaminiHochberg2026].
- **Theorem 5 (Blanchard and Roquain 2008)**: under valid p-values (eq. 10) and PRDS (eq. 11), E[1{p_i ≤ f(p)} / f(p)] ≤ 1 for every i ∈ N and every coordinatewise non-increasing f. **Lemma 6**: k_s is coordinatewise non-increasing in p. **Lemma 7**: a_{k,s} is non-decreasing in k (this is where constraint (3) and the form of b_{k,s} are needed). **Theorem 8**: hence under PRDS, (e_S) is an e-collection [goemanUniformImprovementBenjaminiHochberg2026].
- **Remark 9**: the same argument gives a minimal sufficient condition for BH itself, E[(1/|N|) Σ_{i ∈ N} 1{p_i ≤ bα/m} / (bα/m)] ≤ 1 with b the number of BH rejections (eq. 12), much weaker than PRDS, which Sarkar 2008a and Fithian and Lei 2022 showed to be restrictive [goemanUniformImprovementBenjaminiHochberg2026].

### FDR control (Section 4)
- **Lemma 10 (horizon lemma)**: if e_1, …, e_k ≥ 1/a_{k,s}, then (1/|S|) Σ_{i ∈ S} e_i ≥ |R ∩ S| / (|R| α) for every |S| = s and every R = [j] with k ≤ j ≤ r_{k,s}; a_{k,s} in (4) is the largest value making this hold. This is why r_{k,s} is a "horizon": p_(k) can look ahead to rejection sets up to size r_{k,s} [goemanUniformImprovementBenjaminiHochberg2026].
- **Lemma 11**: e_S ≥ |I_r ∩ S| / ((r ∨ 1) α) for all S. **Theorem 12**: under Assumption 4, rejecting I_r controls FDR at α. **Theorem 13**: if E[e_N] ≤ γ instead, FDR ≤ γα (proof: e_S/γ is an e-collection) [goemanUniformImprovementBenjaminiHochberg2026].

### Closed BH and its place in the family (Section 5)
- BH rejects b = max{k : p_(k) ≤ kα/m} (eq. 13); MABH rejects b' = 1{b > 0} · max{k : p_(k) ≤ kα/(m − 1)} (eq. 14), so b' ≤ b_{mα/(m−1)} (eq. 16) and the MABH gain vanishes as m grows [goemanUniformImprovementBenjaminiHochberg2026].
- **Lemma 14**: the minimal horizon choice ř_{k,s} = k (except s = m) reconstructs MABH exactly. **Proposition 15**: no BH-like method uniformly improves MABH (any method with r ≥ ř everywhere must have r_{k,m−1} = k for all k, which forces r = ř) [goemanUniformImprovementBenjaminiHochberg2026].
- **Proposition 16**: r ≥ b for all α and p iff r_{k,s} ≤ ks/(m − k) whenever k + s > m + 1, s < m, k < m; equivalently a_{k,s} ≥ kα/m. **Remark 17**: BH itself is not BH-like (it would need r_{1,m} = 1), and taking r_{k,m} = k is dominated since a_{k,m} does not depend on r_{k,m} [goemanUniformImprovementBenjaminiHochberg2026].
- **Closed BH** (definition): the maximally ambitious uniform improvement, r̄_{k,s} = min(b_{k,s}, ⌊ks/(m − k)⌋) for k + s > m + 1 and s < m, recursively from initialisation (1). Its critical values are at least those of BH, i.e. at least (m − 1)/m times those of MABH [goemanUniformImprovementBenjaminiHochberg2026].
- **Proposition 18**: if ř < √m then r̄ = ř, since ks/(m − k) < k + 1 for k < √m; closed BH and MABH coincide unless MABH already rejects at least √m hypotheses. Corollary: b = 0 implies r̄ = 0, so closed BH has the same implied global test as BH (true of every BH-like method) [goemanUniformImprovementBenjaminiHochberg2026].

### Simultaneity (Section 6)
- With R = {R : e_S ≥ |R ∩ S| / ((|R| ∨ 1) α) for all S} (eq. 17), e-Closure gives simultaneous FDR control E[max_{R ∈ R} FDP(R)] ≤ α. **Theorem 19** (via Lemmas 22–24): R ∈ R iff R = ∅ or |R| = r and |{i ∈ R : p_i ≤ a_s}| ≥ k_s for every s. Non-trivial simultaneity only swaps rejected hypotheses for others of the same size with equivalent threshold-passing pattern (example: {1,…,6} and {1,2,3,4,5,7}); for MABH, R = {∅, I_r}. Unlike the closed BY, Su and Wang–Ramdas procedures of Xu et al., the BH rejection set I_b is generally not in R, so closed BH is a uniform improvement in the classical sense (r̄ ≥ b) but not in the simultaneity-based sense of Xu et al. [goemanUniformImprovementBenjaminiHochberg2026].

### Algorithms and software (Section 7, Appendix B)
- **Algorithm 1**: number of rejections with a doubly linked candidate set, breadth-first order over s, late start at k = m − s + 1 (only the region k + s ≥ m + 1 needs checking), O(m) memory and about O(m log m + r²) time after sorting, versus O(m²) naive [goemanUniformImprovementBenjaminiHochberg2026].
- **Algorithm 2**: FDR-adjusted p-values q_i = min{α' : {i} ∈ R_{α'}} via a sliding-window minimum of p_(k')/ã_{k',s} maintained by a monotone deque; O(m²) worst case, O(m) memory; adjusted p-values can be smaller than raw ones (as for all π₀-adaptive methods), so the software caps them at the raw p-value by default. Both are in the CRAN package eClosure [goemanUniformImprovementBenjaminiHochberg2026].

### Applications and simulations (Section 8, Table 1, Figures 1–4)
- Six datasets from Xu et al.: at α = 0.05, closed BH vs BH rejects 12 vs 11 (NAEP, m = 34), 801 vs 767 (fdrtool p-values, m = 4,289), 1412 vs 1340 (Van de Vijver, m = 4,919), 1275 vs 1249 (Golub, m = 7,128); at α = 0.1 the gaps widen (e.g. 1856 vs 1728, 1688 vs 1605). MABH equals BH everywhere except PADJUST at α = 0.05 (21 vs 20) [goemanUniformImprovementBenjaminiHochberg2026, Table 1].
- Simulation: m = 200 equicorrelated normals, ρ ∈ {0, 0.3, 0.6, 0.9}, target power t ∈ {0.2, …, 0.8}, π₀ ∈ {0.1, …, 0.9}, α = 0.05, 10⁵ runs. E[e_N] ≤ 1 holds everywhere for one-sided tests (PRDS holds) and is mildly violated (γ ≤ 1.1) in two-sided cases with small ρ, high t and low π₀; closed BH keeps E[e_N] lower than BH. Realised FDR stays below 0.05 in all scenarios, including the violating ones. MABH is indistinguishable from BH; closed BH gains most when π₀, ρ are small and t is large, and never shows a noticeable loss against MABH [goemanUniformImprovementBenjaminiHochberg2026, Figures 1–3].

## Setting and assumptions
- m null hypotheses with p-values p_1, …, p_m; N ⊆ [m] the unknown true nulls; FDR = E[|R ∩ N| / (|R| ∨ 1)]. Fixed α and fixed m; no sequential component, no optional stopping [goemanUniformImprovementBenjaminiHochberg2026].
- Validity (P(p_i ≤ t) ≤ t for i ∈ N) plus either PRDS on N (eq. 11) or just Assumption 4; Theorem 13 quantifies the FDR excess under violations. The horizon matrix r_{k,s} must be chosen independently of the data [goemanUniformImprovementBenjaminiHochberg2026].
- The e-collection is not a compound e-value in the sense of the monograph but an e-collection of 2^m subset-indexed e-values, validity required only at S = N; e-values here are of the thresholded-indicator type 1{p ≤ a}/a, not likelihood ratios [goemanUniformImprovementBenjaminiHochberg2026].

## Relation to other sources
- [xuBringingClosureFalse2025](xuBringingClosureFalse2025.md): the source of the e-Closure principle (Theorem 3 here), of the e-collection concept, of simultaneous FDR control (Section 6), of the datasets in Table 1, and of the open problem this paper solves; Xu et al. improved BY, Su 2018 and Wang–Ramdas 2022 but got no further than MABH for BH. The two papers disagree on what "uniform improvement" should mean: Xu et al.'s simultaneity-based definition (the old set stays available post hoc) is not met by closed BH [goemanUniformImprovementBenjaminiHochberg2026, Section 6].
- [ramdasHypothesisTestingEvalues2025](ramdasHypothesisTestingEvalues2025.md): the monograph's closed e-BH (Theorems 9.27–9.36) and the universality theorem (every FDR procedure is e-BH on compound e-values) are the e-value-input counterparts; this paper applies closure to p-value inputs via calibrated indicators 1{p ≤ a}/a. The monograph treats PRDS only when comparing with BH (Section 9.1.4).
- [vovkEvaluesCalibrationCombination2021](vovkEvaluesCalibrationCombination2021.md): cited for the definition of e-values; e_S is the arithmetic-mean e-merger of Proposition 3.1 applied to indicator e-values on S, and the subset-indexed construction realises the "non-singleton closure for FDP control" flagged in its Appendix A.3.
- [grunwaldSafeTesting2024](grunwaldSafeTesting2024.md): cited as a reference for e-values; no further connection.
- Other works by author–year (not in the bib): Benjamini and Hochberg 1995; Benjamini and Yekutieli 2001 (PRDS); Blanchard and Roquain 2008 (Theorem 5); Solari and Goeman 2017 (MABH); Marcus, Peritz and Gabriel 1976 (closed testing); Wang and Ramdas 2022 (e-BH); Fithian and Lei 2022; Sarkar 2008a; Storey 2002 and Storey, Taylor and Siegmund 2004 (plug-in π₀); Ignatiadis, Wang and Ramdas 2026 (compound-e-value improvements of adaptive BH); Li and Goeman 2026 (e-Closure for invariant causal prediction); Goeman and Solari 2014 (adjusted p-values are joint properties, Section 5.4).

## Concepts touched
- [e-bh](../concepts/e-bh.md): closed BH as a p-value-input relative of closed e-BH; the "every FDR procedure is e-closed" universality, now used constructively.
- [e-merging](../concepts/e-merging.md): e_S is an arithmetic mean of dependent e-values, exactly the merger that is admissible under arbitrary dependence.
- [e-variable](../concepts/e-variable.md): the calibrated indicator 1{p ≤ a}/a with a data-dependent but coordinatewise non-increasing threshold a, valid under PRDS by Blanchard–Roquain.
- [post-hoc-validity](../concepts/post-hoc-validity.md): simultaneous FDR control over the e-closed collection R allows post-hoc choice of the rejected set; here that freedom is shown to be negligible (Theorem 19).
- [calibrator](../concepts/calibrator.md): 1{p ≤ a}/a is the extreme calibrator f = 1_[0,a]/a from Vovk and Wang, here with random a.
- e-closure (new): the e-Closure principle, e-collections, FDR via e_S ≥ |R ∩ S| / (|R| α), simultaneous FDR control, and the minimal sufficient condition E[e_N] ≤ 1 (Sections 3–4, 6).

## Versions
Only arXiv versions exist (v2, 10 June 2026); no journal version known. The v1 → v2 differences are not described in the text.

## Open questions / gaps
- Robustness beyond PRDS: Theorem 13 bounds FDR by γα when E[e_N] ≤ γ, and simulations show FDR control even where γ > 1, but whether closed BH shares BH's known robustness to PRDS violations is explicitly left open (Section 9).
- The minimal sufficient condition is sufficient, not necessary; the paper notes that low e_S for S ≠ N under imperfect power is part of why FDR is still controlled, without a theory.
- Admissibility of BH-like methods and of the class as a whole; whether BH-like methods that do not uniformly improve BH (violating Proposition 16) could trade uniformity for substantial power; capping r_{k,s} at a user-chosen n to gain power when at most n rejections are wanted (Section 9).
- Whether a "more elegant" uniform improvement of BH exists outside the BH-like class; the author states the class covers all known uniform improvements of BH under PRDS and under independence.
- Uniform improvements of BH that emphasise simultaneity rather than power are suggested as potentially more relevant for some applications, since closed BH inherits the non-simultaneity problems of BH (no post-hoc shrinking of the rejected set).
- The companion e-Closure paper [xuBringingClosureFalse2025](xuBringingClosureFalse2025.md) is in this batch; Wang and Ramdas 2022, Solari and Goeman 2017, Blanchard and Roquain 2008, Benjamini and Yekutieli 2001, Ignatiadis, Wang and Ramdas 2026 and Li and Goeman 2026 are cited but not in the bib (record in wiki/gaps.md).
