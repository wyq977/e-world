---
citekey: xuBringingClosureFalse2025
title: "Bringing closure to false discovery rate control: a general principle for multiple testing"
authors: [Ziyu Xu, Aldo Solari, Lasse Fischer, Rianne de Heide, Aaditya Ramdas, Jelle Goeman]
year: 2025
status: preprint
public: true
note: "Every multiple testing method that controls an expected loss (FDR, FWER, PFER, FDX, ...) is a closed testing procedure driven by e-values for intersection hypotheses, and reverse-engineering the implicit e-values yields strictly more powerful versions of e-BH, Benjamini–Yekutieli and Su's procedure with free post-hoc choice of rejected set, error metric and even level."
links:
  pdf: "https://arxiv.org/pdf/2509.02517"
  arxiv: "https://arxiv.org/abs/2509.02517"
  doi: "10.48550/arXiv.2509.02517"
  video: ""
tags: [e-closure, closed-testing, fdr, fwer, e-bh, benjamini-yekutieli, su-procedure, compound-e-values, e-merging, calibrator, post-hoc-validity, simultaneous-inference, restricted-combinations, knockoffs, computation, eClosure]
ingested: 2026-10-08
version: "arxiv 2509.02517v3 (30 Jul 2026, 49 pages); merges and subsumes Xu, Fischer and Ramdas arXiv 2504.11759 and Goeman, de Heide and Solari arXiv 2504.15946"
---

# Bringing closure to false discovery rate control: a general principle for multiple testing

## Summary
The classical Closure Principle (Marcus, Peritz and Gabriel 1976; Sonnemann 1982, 2008) says that every FWER-controlling method is a closed testing procedure built from local tests of intersection hypotheses, and Goeman, Hemerik and Solari 2021 extended this to tail-probability (FDP) control, but expectation-based error rates, above all FDR, were outside its scope [xuBringingClosureFalse2025]. This paper closes the gap with the e-Closure Principle: for any error rate ER_f = E_P[f_{N_P}(R)] with nonnegative loss f, a (simultaneous) procedure controls ER_f at level α if and only if its rejected sets all satisfy e_S ≥ f_S(R)/α for every S ⊆ [m], where (e_S) is an e-collection, i.e. e_{N_P} is an [e-variable](../concepts/e-variable.md) under every P (Theorem 6). Thresholding the local e-values at 1/α recovers closed testing for FWER (Theorem 12, Corollary 13); plugging FDP in as the loss gives a novel necessary-and-sufficient principle for FDR (Theorem 14). Writing existing methods as e-Closure procedures and then replacing their implicit local e-values by stochastically larger ones yields uniform improvements in both power and simultaneity: closed e-BH from the arithmetic mean of e-values (Theorem 17), closed BY from a |S|-dependent calibrator (Theorem 28), closed Su from a calibrated Simes p-value under PRDN (Theorem 34); the e-collections tried for BH and its adaptive variants only reconstruct them (Theorem 37), while Goeman 2026 (in the bib, not yet a source page) improves BH by a different construction. Because all expected-loss error rates are governed by one principle, the researcher may choose the rejected set, the error metric (e.g. switch from FDR to FWER, Theorem 39, Theorem 41) and, when the e-collection does not depend on α, the nominal level after seeing the data (Definition 46, Theorem 48). Polynomial-time algorithms (O(m² log m) for closed e-BH, O(m³) for closed BY) are given in Section 10 and implemented in the eClosure (CRAN) and eclosure (PyPI) packages; on six p-value datasets and the Wang–Ramdas cryptocurrency e-values the closed procedures make up to a few dozen percent more discoveries (Tables 1, 5, 6) [xuBringingClosureFalse2025].

## Main results

### Framework (Section 3)
- Definition 1: R controls ER_f at α if E_P[f_{N_P}(R)] ≤ α for all P, with f_N(∅) = 0 and f_∅(R) = 0; Table 3 lists FDR (FDP), k-FWER, PFER (|N ∩ R|), FDX-γ, AER [xuBringingClosureFalse2025].
- Definition 2: a random collection 𝓡 ⊆ 2^[m] controls ER_f simultaneously if E_P[max_{R ∈ 𝓡} f_{N_P}(R)] ≤ α; Lemma 3 links single sets and collections; Lemma 4 shows simultaneous control equals post-hoc control over arbitrary measurable selectors R(X) ∈ 𝓡.
- Excluded: pFDR and local fdr are not expectations of a loss; Appendix E (Proposition 53) recovers ratio metrics such as mFDR_η and pFDR via an α-dependent loss f + α(G − g)/(G + η), dropping the empty-set convention.

### The e-Closure Principle (Section 4)
- Definition 5: an e-collection E = (e_S)_{S ⊆ [m]} has E_P[e_{N_P}] ≤ 1 for all P; taking each e_S an e-value for H_S = ∩_{i∈S} H_i is sufficient, not necessary (Remark 50); e_∅ = 0.
- Eq. (2): 𝓡^{ER_f}_α(E) = {R : e_S ≥ f_S(R)/α ∀S}.
- Theorem 6: 𝓡 is a simultaneous ER_f-controlling procedure iff 𝓡 ⊆ 𝓡^{ER_f}_α(E) for some e-collection; the converse uses e_S = max_{R∈𝓡} f_S(R)/α (eq. 3). Corollary 7: same for single sets. Proposition 8: reapplying the construction is idempotent, so the canonical e-collection never adds power; improvements must come from better local e-values.
- Remark 9: validity hinges on the single e-value e_{N_P}, so asymptotic e-values (Ignatiadis, Wang, Ramdas 2025) give control converging at the rate E[e_{N_P}] → 1. Remark 11 / Appendix D: the problem is a composite generalised Neyman–Pearson problem and the e-Closure rule a maximally compatible decision rule in the sense of [grunwaldBeyondNeymanPearsonEvalues2024], though that paper's admissibility results need a richness condition violated by discrete losses.
- Theorem 12: for FWER one may restrict e_S ∈ {0, 1/α}; Corollary 13: e_S = φ_S/α maps closed testing from local tests Φ onto 𝓡^FWER_α(E) and back.
- Theorem 14: 𝓡 controls FDR simultaneously iff 𝓡 ⊆ 𝓡^FDR_α(E) = {R : e_S ≥ FDP_S(R)/α ∀S}. Remark 15: supports may be restricted to {k/(αr)}, used for boosting and randomisation in Appendix A.

### Closed e-BH (Section 5)
- Eq. (6): e_S = |S|^{-1} Σ_{i∈S} e_i, the admissible symmetric merger of [vovkEvaluesCalibrationCombination2021]; closed e-BH collection (7) ("mean-consistent" sets); ordered largest set by Lemma 52 (Appendix C).
- Theorem 17: for m > 1 closed e-BH is a uniform improvement in simultaneity and power over e-BH (every self-consistent set is mean-consistent, and e_1 = (m − ½)/α, e_2 = 1/(2α), rest 0 rejects {1} where e-BH rejects nothing). Example 20: if (2m − 2i + 1)/(mα) ≤ e_i < m/(iα) then e-BH rejects nothing and closed e-BH rejects all of [m] (Figure 1). Theorem 54 (Appendix F): same over minimally adaptive e-BH for m > 4.
- Examples 21–23: rejection of a set depends on e-values outside it; hypotheses with e_i < 1/α can be rejected (e_1 = 3/(2α), e_2 = 1/(2α) rejects both); the largest mean-consistent set need not be unique; the procedure behaves like an adaptive (π_0-estimating) method without an estimator.
- Section 5.3: compound e-values (Σ_{i∈N_P} E_P[ẽ_i] ≤ m) give an e-collection via e_S = m^{-1} Σ_{i∈S} ẽ_i (Proposition 24), and then closed e-BH equals e-BH (Theorem 25); conversely, from any R ∈ 𝓡^FDR_α(E) the universal compound e-values ẽ_i = m·1{i∈R}/(α|R| ∨ 1) satisfy Σ_{i∈S} ẽ_i ≤ m e_S (Proposition 26). The two universality results (Ignatiadis et al. 2025, Theorem 6.5, and Theorem 14) are complementary; e-Closure also covers richer action spaces and other losses.
- Remark 19 and Appendix B (Proposition 51): any admissible deterministic procedure on arbitrarily dependent input e-values is represented by weighted affine local e-values Σ w_{i,S} e_i + c_S, via Clerico 2026's characterisation of generalised e-merging functions; Sun and Wang 2026 then showed every constant-free weighted-mean closed e-BH is admissible.

### FDR from p-values (Section 6)
- Lemma 27 / eq. (13): closed BY uses e_S = Σ_{i∈S} 1{h_{|S|} p_i ≤ α} / (α ⌈|S| h_{|S|} p_i / α⌉ ∨ 1), the Xu–Wang–Ramdas 2024 calibrator with k = |S| rather than k = m; Theorem 28: FDR under arbitrary dependence and a uniform improvement over BY for m > 1; Example 29 (Figure 2): BY rejects nothing while closed BY rejects everything. Closed BY never rejects p_i > α. Remark 31 / Appendix G: e-BH on calibrated p-values also improves BY, neither dominates the other, but closed BY wins on all datasets in Table 5.
- Lemma 32: e(x) = (l_α x ∨ α)^{-1} with l_α = −W_{−1}(−α/e) is a [calibrator](../concepts/calibrator.md); Corollary 33: e_S = (l_α p_S ∨ α)^{-1} for the Simes p-value p_S is an e-value under PRDN; Theorem 34: closed Su controls FDR under PRDN and uniformly improves Su 2018's BH-at-level-α/l_α (1/l_α = 0.174 at α = 0.05); Example 35 (Figure 3).
- Theorem 37 (Section 7): the e-collections (16), (17), (19) built from the compound e-values of Li and Zhang 2025 for BH, minimally adaptive BH and Storey-type adaptive BH reconstruct exactly {∅, R_BH} etc.; the only exception is BH rejecting all of [m], where every singleton becomes available and the union controls FWER.

### Post-hoc flexibility (Section 8)
- Section 8.1: simultaneity = post-hoc choice of the discovery set (volcano plots, brain clusters, pathways). Theorem 38: closed knockoffs with e_S from the sign-flip property (eq. 20) equal all subsets of the knockoff set R_Kn with |R| ≥ (1 + #negatives)/α, a simultaneity but not power improvement.
- Theorem 39: from any simultaneous-FDR collection, the union of available singletons controls FWER at α.
- Definition 40, Theorem 41: simultaneous control over a family F of losses, E[sup_f max_R f_{N_P}(R)] ≤ α, holds for every e-collection and conversely every such family is dominated by one. Example 42: post-hoc γ in FDX; Example 43: decide between e-Holm (FWER) and closed e-BH (FDR) by the data-dependent size of the discovery set. Theorem 44: the e-Closure true-discovery bound d_E(R) = max{d : e_S ≥ 1{|R∖S| < d}/α ∀S} reproduces Genovese–Wasserman / Goeman–Solari closed testing when e_S = φ_S/α.
- Definition 46, Corollary 47, Theorem 48: if E does not depend on α, then E_P[sup_α sup_f max_R f_{N_P}(R)/α] ≤ 1, so α may be chosen post hoc (extends [ramdasHypothesisTestingEvalues2025, Thm 9.10] from e-BH to all e-Closure procedures); calibrators such as BY's must keep a fixed calibration level α_0 (Remark 49).

### Restricted combinations and computation (Sections 9–10)
- Section 9: e_S may be an e-value for the partitioning hypothesis {P : N_P = S} (Finner and Strassburger 2002); impossible null patterns impose no constraint (six pairwise comparisons of four means: 49 of 63 subsets impossible), so closed e-BH can reject {1, 2, 3} where it would reject {1}.
- Section 10: with local e-values monotone in the p-values, checking R needs only O(m²) sets S (a largest p-values inside R, b largest outside); closed BY in O(m³) and closed e-BH in O(m² log m) via convexity of g(a, r, b) in b (Dobriban 2020-style shortcuts).
- Appendix A: stochastic rounding of each e_S (Xu and Ramdas 2023) and boosting with the truncation T_A onto {r/(αk)} apply to every e-Closure procedure; product merging for independent e-values.

## Setting and assumptions
- m fixed hypotheses H_i ⊆ M, true set N_P; a method is a random set or random collection of subsets of [m]; auxiliary randomisation allowed [xuBringingClosureFalse2025].
- No optional stopping or sequential element; the discussion lists online/infinite-m extensions as future work.
- Closed e-BH: arbitrary dependence of input e-values. Closed BY: arbitrary dependence of p-values. Closed Su: PRDN (positive regression dependence on the nulls only). BH-type e-collections: PRDS, or independence plus a monotone null-proportion estimator with E[1/π̂_0^i] ≤ m/|N_P| (eq. 18). Closed knockoffs: the usual null sign-flip property.
- "Uniform improvement" (Definition 16) is pointwise in the data; whether the improvement region has positive probability depends on the distribution.
- Measurability of suprema over uncountable loss families is assumed (Remark 45, cf. Chugg, Lardy, Ramdas and Grünwald 2025).

## Relation to other sources
- [ramdasHypothesisTestingEvalues2025](ramdasHypothesisTestingEvalues2025.md): the book's closed e-BH section (Thms 9.32–9.36) presents the Xu–Fischer–Ramdas precursor; this paper generalises Theorem 9.10's post-hoc α to all e-Closure procedures (Theorem 48) and cites the book for e-values generally and for the admissible-merger result.
- [vovkEvaluesCalibrationCombination2021](vovkEvaluesCalibrationCombination2021.md): supplies the arithmetic mean as the only admissible symmetric e-merger (basis of closed e-BH) and the e-Holm procedure that reappears as 𝓡^FWER_α(E) with mean local e-values (Example 43); its flagged non-singleton closure for FDP is realised here.
- [grunwaldBeyondNeymanPearsonEvalues2024](grunwaldBeyondNeymanPearsonEvalues2024.md): multiple testing is a composite GNP problem and e-Closure a maximally compatible decision rule (Remark 11, Appendix D); Definition 46 builds on its post-hoc validity notion and on Koning 2023.
- [grunwaldSafeTesting2024](grunwaldSafeTesting2024.md), [shaferTestingBettingStrategy2021](shaferTestingBettingStrategy2021.md): cited as e-value background only.
- [wassermanUniversalInference2020](wassermanUniversalInference2020.md): not cited; the arithmetic-mean closure here is the same device as averaging split-LRTs.
- [goemanUniformImprovementBenjaminiHochberg2026](goemanUniformImprovementBenjaminiHochberg2026.md): the closed BH procedure that uniformly improves BH under PRDS and a weaker condition, answering the open problem posed in earlier versions of this paper (Sections 1, 7); this paper's Theorem 37 shows why the Li–Zhang-type e-collections cannot do it.
- In the bib but without a source page yet: Wang and Ramdas 2022 (e-BH, boosting, the cryptocurrency data; in the bib as wangFalseDiscoveryRate2021); Vovk and Wang 2023 (closure of the mean for FWER and FDP bounds); Grünwald 2023 (e-posterior, cited for e-collections); Koning 2023 is not in the bib.
- Not in the bib: Ignatiadis, Wang and Ramdas 2024 and 2025 (compound and asymptotic e-values, minimally adaptive e-BH); Xu, Wang and Ramdas 2024 (the BY calibrator); Li and Zhang 2025 (BH as compound e-BH); Ren and Barber 2024 (knockoff e-values); Su 2018; Goeman, Hemerik and Solari 2021; Blanchard and Roquain 2008; Sun and Wang 2026; Clerico 2026; Hartog and Lei 2025; Fischer and Ramdas 2024.

## Concepts touched
- e-closure-principle (new)
- [e-bh](../concepts/e-bh.md)
- [e-merging](../concepts/e-merging.md)
- [calibrator](../concepts/calibrator.md)
- [post-hoc-validity](../concepts/post-hoc-validity.md)
- [e-variable](../concepts/e-variable.md)

## Versions
v3 (30 Jul 2026) merges the two parallel preprints Xu, Fischer and Ramdas 2025 (arXiv 2504.11759, "Beating the e-Benjamini–Hochberg procedure") and Goeman, de Heide and Solari 2025 (arXiv 2504.15946, "The e-partitioning principle of FDR control"). It also records that the earlier open problem of improving BH is now solved by Goeman 2026, corrects (per the acknowledgments) an error in the theorem on BH variants (now Theorem 37), and cites Sun and Wang 2026 for the admissibility characterisation that an earlier draft posed as open [xuBringingClosureFalse2025].

## Open questions / gaps
- Which further FDR methods (beyond e-BH, BY, Su, knockoffs) can be improved or made simultaneous by e-Closure, and with polynomial-time shortcuts (branch and bound as in Vesely, Finos and Goeman 2023)?
- Extension to infinitely many hypotheses / online multiple testing (Discussion).
- Hybrid γ-FDX and FWER procedures via e-Closure, in the spirit of Hemerik 2025's multi-resolution method (Section 8.2).
- Admissibility of maximally compatible rules from [grunwaldBeyondNeymanPearsonEvalues2024] does not transfer because the loss is discrete (Appendix D); a general admissibility theory for e-Closure procedures beyond the FDR/e-value case of Sun and Wang 2026 is open.
- Ratio metrics with unbounded stopping times (error-over-patience) are outside the bounded reduction of Appendix E.
- Measure-theoretic treatment of uncountable loss families (Remark 45).
