---
citekey: ignatiadisEvaluesUnnormalizedWeights2022
title: "E-values as unnormalized weights in multiple testing"
authors: [Nikolaos Ignatiadis, Ruodu Wang, Aaditya Ramdas]
year: 2022
status: preprint
public: true
note: "When every hypothesis comes with a p-value and an independent e-value, the e-values can be used as weights for Benjamini–Hochberg or Bonferroni without being normalised to sum to the number of hypotheses, which the paper turns into a meta-analysis combiner, a data-driven weighting scheme via compound e-values, and a gene-expression case study with more discoveries."
links:
  pdf: "https://arxiv.org/pdf/2204.12447v6"
  arxiv: "https://arxiv.org/abs/2204.12447"
  doi: "10.48550/arXiv.2204.12447"
  video: ""
tags: [e-bh, weighted-bh, compound-e-value, pe-combiner, q-combiner, calibrator, meta-analysis, false-discovery-rate, fwer, storey-adaptivity, minimally-adaptive-e-bh, prds, basu-theorem, differential-expression, simulations]
ingested: 2026-10-08
version: "arxiv 2204.12447v6 (18 July 2023; published Biometrika 111(2), 2024)"
---

# E-values as unnormalized weights in multiple testing

## Summary
The paper studies hypotheses that each carry a p-value P_k and an e-value E_k, and asks how to combine them for single and multiple testing [ignatiadisEvaluesUnnormalizedWeights2022]. For one hypothesis it identifies four admissible combiners, one per case (independent or dependent inputs, p- or e-value output), and singles out the quotient Q(P,E) = (P/E) ∧ 1, which is a valid p-value when P and E are independent (Theorem 3.1). Feeding Q(P_k, E_k) to any p-value procedure gives an "ep-D" procedure, which is exactly the weighted p-BH or weighted p-Bonferroni procedure with weights E_k; the central message is that, unlike classical weights, these e-value weights need not sum to K, so the "weight budget" Σ E_k can far exceed K when alternatives have large e-values (Theorems 4.3, 4.7, 4.9, 4.10). The validity needed is only Σ_{k∈N} E[E_k] ≤ K_0, a compound e-value condition, which the paper exploits to build data-driven unnormalised weights from the same dataset as the p-values in simultaneous t-tests, using Basu's theorem for independence (Theorem 5.1, Proposition 5.2). A meta-analysis of RNA-Seq p-values and microarray e-values on 24,906 mouse genes and simulations show ep-BH making substantially more discoveries than unweighted, normalised-weight and IHW BH, and a supplement adds the first (minimally) adaptive e-BH procedure (Proposition S3.3).

## Main results
- Theorem 3.1: for any admissible p-to-e calibrator h and λ ∈ (0,1), Π_h(p,e) = h(p)e is an admissible i-pe/e combiner, Q(p,e) = (p/e) ∧ 1 an admissible i-pe/p combiner, M_h^λ = λh(p) + (1−λ)e an admissible pe/e combiner, and B(p,e) = {2(p ∧ e^{-1})} ∧ 1 an admissible pe/p combiner ("i" = independent inputs) [ignatiadisEvaluesUnnormalizedWeights2022, Sec. 3.1, proof S1.1].
- Remark 3.2: Q(U,E) with an independent uniform U is a randomised e-to-p calibrator that dominates the unique admissible deterministic one e ↦ (1/e) ∧ 1 [ignatiadisEvaluesUnnormalizedWeights2022].
- Section 3.2–3.3 and Proposition S4.1: rule of thumb for two-study meta-analysis: Fisher's combination for exchangeable studies, the Q-combiner (p-value from the better-powered primary study, e-value from the secondary) for imbalanced ones; Pitman ARE of Q versus the full likelihood ratio z-test tends to 1 as α ↓ 0 or as the secondary share θ ↓ 0, and equals 0.956 at θ = 0.5, α = 0.05, power 0.9 (Table S1) [ignatiadisEvaluesUnnormalizedWeights2022].
- Definition 4.2: ep-D = p-D applied to P*_k = Q(P_k, E_k); ep-BH and ep-Bonferroni equal weighted p-BH and weighted p-Bonferroni with weights E_k [ignatiadisEvaluesUnnormalizedWeights2022].
- Theorem 4.3: under Assumption 4.1 (P_k independent of E_k for null k), any generalised type-I error bound of p-D valid under arbitrary dependence transfers to ep-D; in particular ep-BH has FDR ≤ ℓ_K π_0 α and ep-Bonferroni has PFER and FWER ≤ α [ignatiadisEvaluesUnnormalizedWeights2022].
- Theorem 4.5: under Assumptions 4.1 and 4.4 (null (P_k, E_k) pairs mutually independent and independent of the non-null pairs), ep-BH has FDR ≤ π_0 α and ep-Hochberg FWER ≤ α [ignatiadisEvaluesUnnormalizedWeights2022].
- Theorem 4.7: if (P_k) is PRDS and the whole p-vector is independent of the whole e-vector (Assumption 4.6), ep-BH has FDR ≤ π_0 α with no assumption on dependence among the e-values; the proof conditions on the e-values and applies the weighted-BH bound FDR ≤ (α/K) Σ_{k∈N} E_k [ignatiadisEvaluesUnnormalizedWeights2022].
- Theorem 4.9: if null p-values are independent of null e-values (Assumption 4.8) and (P_k) is PRD within nulls, ep-Simes has type-I error ≤ α under the global null, ep-BH has FDR ≤ π_0 α log{e/(π_0 α)} via Su's FDR-linking theorem, and ep-Hochberg (and ep-Hommel, S2.2) has FWER ≤ α [ignatiadisEvaluesUnnormalizedWeights2022].
- Theorem 4.10: ep-Storey, weighted p-BH with weights 1(P_k ≤ τ) E_k / π̂_0 and Storey's π̂_0 = {1 + Σ 1(P_k > τ)}/{K(1−τ)}, has FDR ≤ α under Assumption 4.6 and p-independence [ignatiadisEvaluesUnnormalizedWeights2022, proof S1.2].
- Remark 4.11: normalised weighted BH has FDR controlled at α Σ_{k∈N} w_k / Σ_k w_k, so informative weights make it conservative; ep-BH pays no such penalty while E[E_k] = 1 for nulls [ignatiadisEvaluesUnnormalizedWeights2022].
- Section 4.5 (robustness): inflated inputs with E[E_k] ≤ 1 + η or P(P_k ≤ t) ≤ (1+η)t inflate all bounds by the factor (1+η); compound e-values with (1/K_0) Σ_{k∈N} E[E_k] ≤ 1 (eq. 4) still give ep-Bonferroni FWER ≤ α and ep-BH FDR ≤ α in the settings of Theorems 4.3 and 4.7 [ignatiadisEvaluesUnnormalizedWeights2022].
- Section 5.1, eq. 7–9: for simultaneous one-sample t-tests Y_kj ~ N(μ_k, σ_k²), the mean of squares S_k² is independent of the t-statistic for null k (Basu); E*_k = K_0 S_k² / Σ_{ℓ∈N} σ_ℓ² are compound e-values, estimated by E_k = K S_k² / Σ_ℓ σ̂_ℓ²; the expected budget grows by the factor Σ(μ_k² + σ_k²)/Σσ_k² relative to the normalised Westfall–Kropf–Finos weights [ignatiadisEvaluesUnnormalizedWeights2022].
- Theorem 5.1 and Proposition 5.2: with P(Σ σ̂_ℓ² < (1−δ) Σ_{ℓ∈N} σ_ℓ²) ≤ η, ep-Bonferroni controls FWER and ep-BH controls FDR at α/(1−δ) + η; δ(η) = O{√(log(1/η)/(nK_0))} by a Gamma left-tail Chernoff bound, e.g. α = 0.1, n = 10, K = 20,000, π_0 = 0.95 gives η = 0.001, δ < 0.0128 and FDR ≤ 0.1023 [ignatiadisEvaluesUnnormalizedWeights2022, proofs S1.3–S1.4].
- Eq. 10 and Supplement S6: a more powerful weighting ψ(S_k²) from a truncated (D = 6, λ = n) power series of the noncentral-χ² likelihood ratio, rescaled by the matching function of σ̂_ℓ² so that null expectations agree [ignatiadisEvaluesUnnormalizedWeights2022].
- Section 5.3: a hierarchy of side-information assumptions: (i) side-information independent of null p-values (IHW-type), (ii) a second independent p-value (Du–Zhang, needs known σ² = 1), (iii) the intermediate compound-e-value condition (4) [ignatiadisEvaluesUnnormalizedWeights2022].
- Section 6, Table 1: Bottomly et al. 2011 mouse striatum data, RNA-Seq DESeq2 p-values for 24,906 genes, microarray e-values for 15,875 (rest set to 1), α = 0.01: BH 1973, ep-BH 2387, normalised-weight BH 1310, IHW 2016, Fisher 2354, SIM 2282 discoveries; adaptive: Storey 2147, ep-Storey 2540, Fisher-Storey 2556; ep-BH's average weight 18.11 versus 1.00 for normalised weights [ignatiadisEvaluesUnnormalizedWeights2022].
- Section 7, Figs 3–5: t-test simulations (n = 10, K = 20,000, π_0 = 0.95, 4,000 replicates): all weighted methods control FDR, ep-BH is most powerful after SIM, which violates FDR at small effect sizes; under heteroscedasticity σ_k² ~ U(1−τ, 1+τ), τ ∈ {0.3, 0.5}, Fisher and SIM lose FDR control and ep-BH has the most power; RNA-Seq/microarray simulation (K = 10,000, π_0 = 0.8): ep-BH more than doubles unweighted BH power at small fold changes when microarray data are informative and loses little when they are uninformative [ignatiadisEvaluesUnnormalizedWeights2022].
- Theorem S3.2: pe-BH, e-BH on E*_k = h(P_k) E_k, has FDR ≤ α K_0/K under Assumption 4.1 with no dependence assumption, but is dominated by ep-BH whenever both are valid since h(p) ≤ 1/p for every calibrator; the two are incomparable when ep-BH needs the BY correction [ignatiadisEvaluesUnnormalizedWeights2022, Supp. S3.1].
- Proposition S3.3 (minimally adaptive e-BH): test the global null by an e-merging function F(e_1..e_K) ≥ 1/α, then run e-BH at α' = Kα/(K−1); FDR ≤ α for any F, and with the arithmetic mean M the procedure dominates e-BH; a boosted version uses S(e) = max_k k e_[k]/K; the gain is negligible unless K ≤ 10 [ignatiadisEvaluesUnnormalizedWeights2022, Supp. S3.2].
- Proposition S7.1: for replicated microarray data under the Lönnstedt–Speed/Smyth hierarchical model, E_k = (γ_k+1)^{-1/2} {1 − γ_k T̃_k² / ((1+γ_k)(ν_0+ν_k+T̃_k²))}^{−(ν_0+ν_k+1)/2} is an e-value with E[E_k | β_k = 0] = 1, equal to the Lönnstedt–Speed posterior odds when the working null proportion is 1/2 [ignatiadisEvaluesUnnormalizedWeights2022, Supp. S7].

## Setting and assumptions
- K hypotheses with null set N, K_0 = |N|, π_0 = K_0/K; for null k, P(P_k ≤ t) ≤ t and E[E_k] ≤ 1; no restriction on non-null inputs [ignatiadisEvaluesUnnormalizedWeights2022, Sec. 2.1].
- Error metrics: generalised type-I errors E{G(F_D, R_D)} covering FDR, PFER and FWER; p-value dependence notions: p-independence (Def. 2.1), PRDS in the Finner–Barber–Ramdas form (Def. 2.2), PRD within nulls of Su (Def. 2.3) [ignatiadisEvaluesUnnormalizedWeights2022].
- Cross-dependence hierarchy: Assumption 4.1 (P_k ⫫ E_k, null k) is the weakest; 4.8 (null p-vector ⫫ null e-vector) is intermediate; 4.6 (full p-vector ⫫ full e-vector) is strongest; 4.4 adds independence across null pairs [ignatiadisEvaluesUnnormalizedWeights2022, Sec. 4].
- Fixed-sample p-values and e-values; no optional stopping is analysed, though the e-value source dataset may have been collected with optional stopping [ignatiadisEvaluesUnnormalizedWeights2022, Sec. 3.2].
- Section 5 model: Y_kj ~ N(μ_k, σ_k²), j = 1..n, n ≥ 2, all observations mutually independent; two-sample and nonparametric (Wilcoxon with a permutation-invariant statistic) analogues sketched in S5 [ignatiadisEvaluesUnnormalizedWeights2022].
- Code: https://github.com/nignatiadis/evalues-as-weights-paper [ignatiadisEvaluesUnnormalizedWeights2022].

## Relation to other sources
- [wangFalseDiscoveryRate2021](wangFalseDiscoveryRate2021.md): supplies e-BH (Definition 2.5) and its FDR ≤ α K_0/K under arbitrary dependence (used in Theorem S3.2 and Proposition S3.3); the compound condition (4) is attributed to that paper and to Ren and Barber 2022; the pe-BH versus ep-BH trade-off mirrors e-BH versus BY-corrected p-BH there (Section 6.5) [ignatiadisEvaluesUnnormalizedWeights2022, Secs 2.2, 4.5, S3].
- [ramdasHypothesisTestingEvalues2025](ramdasHypothesisTestingEvalues2025.md): Chapter 11 presents the pe/e and pe/p combiners (Definition 11.4, Theorem 11.5) and e-weighted BH (Definition 11.9, Theorem 11.10) from this paper; Chapter 9 names compound e-values (Definition 9.1) and minimally adaptive e-BH (Section 9.4), both of which appear here in Section 4.5 and Supplement S3.2; the randomised calibrator of Remark 3.2 is the book's Corollary 2.10.
- [vovkEvaluesCalibrationCombination2021](vovkEvaluesCalibrationCombination2021.md): source of the admissible calibrator classes (Props 2.1–2.2), the arithmetic-mean domination used for the minimally adaptive procedure (Prop. 3.1), and the combiner terminology adapted here [ignatiadisEvaluesUnnormalizedWeights2022, Secs 3.1, S3.2].
- [xuBringingClosureFalse2025](xuBringingClosureFalse2025.md) and [goemanUniformImprovementBenjaminiHochberg2026](goemanUniformImprovementBenjaminiHochberg2026.md): the minimally adaptive e-BH of Proposition S3.3 is a global-null-then-BH shortcut of Solari–Goeman type; closed e-BH later subsumes such uniform improvements.
- [wassermanUniversalInference2020](wassermanUniversalInference2020.md): universal inference is the motivating example of a small secondary dataset summarised by an e-value [ignatiadisEvaluesUnnormalizedWeights2022, Secs 1, 3.2].
- [ramdasGametheoreticStatisticsSafe2023](ramdasGametheoreticStatisticsSafe2023.md): cited as the survey of settings where e-values arise naturally (optional stopping and continuation) [ignatiadisEvaluesUnnormalizedWeights2022, Sec. 3.2].
- [shaferTestingBettingStrategy2021](shaferTestingBettingStrategy2021.md), [howardTimeuniformNonparametricNonasymptotic2021](howardTimeuniformNonparametricNonasymptotic2021.md), [grunwaldSafeTesting2024](grunwaldSafeTesting2024.md): cited for e-values as betting scores, stopped supermartingales and safe tests [ignatiadisEvaluesUnnormalizedWeights2022, Sec. 1].
- Other work by author-year, no link: Vovk and Wang 2020 and Vovk, Wang and Wang 2022 (p-merging); Shafer, Shen, Vereshchagin and Vovk 2011 and Shafer and Vovk 2019 (calibration); Ren and Barber 2022 (derandomised knockoffs, compound e-values); Xu, Wang and Ramdas 2021 (bandit multiple testing); Solari and Goeman 2017 (minimally adaptive BH); Su 2018 (FDR-linking); Ramdas, Barber, Wainwright and Jordan 2019 (p-filter, weighted BH lemma); Genovese, Roeder and Wasserman 2006 and Blanchard and Roquain 2008 (weighted BH); Westfall, Kropf and Finos 2004 (S_k² weights); Ignatiadis et al. 2016 and Ignatiadis and Huber 2021 (IHW); Du and Zhang 2014 (SIM); Storey, Taylor and Siegmund 2004; Armstrong 2022 (compound p-values); Lönnstedt and Speed 2002 and Smyth 2004 (limma model).

## Concepts touched
- [e-bh](../concepts/e-bh.md)
- [e-merging](../concepts/e-merging.md)
- [calibrator](../concepts/calibrator.md)
- [e-variable](../concepts/e-variable.md)
- [universal-inference](../concepts/universal-inference.md)

## Versions
Six arXiv versions (v1 April 2022 to v6 July 2023); v6 is read here and is dated after the paper was accepted. The Biometrika 111(2) 2024 version of record is expected to match v6 in numbering (Theorems 3.1, 4.3–4.10, 5.1, Proposition 5.2, Supplements S1–S8); not verified. Footnote 4 records that an earlier working version used the noncentral-χ² likelihood ratio itself as the e-value in the simulations, replaced in later versions by the rescaled truncated series (10).

## Open questions / gaps
- The optimal, possibly data-driven, choice of the weighting function ψ in E_k ∝ ψ(S_k²) is left open [ignatiadisEvaluesUnnormalizedWeights2022, Sec. 5.2].
- No Storey-type null-proportion-adaptive version of e-BH is known; Proposition S3.3 gives only a minimal improvement useful for K ≤ 10 [ignatiadisEvaluesUnnormalizedWeights2022, Supp. S3.2].
- ep-Storey discards hypotheses with P_k > τ even when E_k alone would be rejected by e-BH; larger τ is suggested but not analysed [ignatiadisEvaluesUnnormalizedWeights2022, Sec. 4.4].
- FDR control for ep-BH under arbitrary dependence of the combined p-values still requires the ℓ_K ≈ log K Benjamini–Yekutieli factor (Theorem 4.3), unlike e-BH; whether an e-weighted procedure can avoid it under weaker assumptions is not addressed.
- Approximate validity of DESeq2 p-values causes slight FDR exceedance for all methods in the adaptive RNA-Seq simulation (Fig. S1); the e-value construction of S7 relies on the Lönnstedt–Speed variance prior fitted by empirical Bayes, with estimation uncertainty ignored [ignatiadisEvaluesUnnormalizedWeights2022, Supp. S7–S8].
- Not in the bib: Ren and Barber 2022 (derandomised knockoffs via e-values), Solari and Goeman 2017 (minimally adaptive BH), Su 2018 (FDR-linking theorem), Vovk, Wang and Wang 2022 (admissible p-merging), Xu, Wang and Ramdas 2021 (bandit multiple testing).
