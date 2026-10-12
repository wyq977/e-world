---
citekey: xuOnlineMultipleTesting2023
title: "Online multiple testing with e-values"
authors: [Ziyu Xu, Aaditya Ramdas]
year: 2023
status: preprint
public: true
note: "e-LOND: feed e-values instead of p-values into the LOND online FDR algorithm and the usual log-factor penalty for unknown dependence disappears, with randomised variants that reject strictly more and an online false-coverage-rate version for e-confidence intervals."
links:
  pdf: "https://arxiv.org/pdf/2311.06412v1"
  arxiv: "https://arxiv.org/abs/2311.06412"
  doi: "10.48550/arXiv.2311.06412"
  video: ""
tags: [online-multiple-testing, online-fdr, e-lond, lond, r-lond, lord, saffron, arbitrary-dependence, randomisation, stochastic-rounding, false-coverage-rate, e-confidence-interval, doubly-sequential, calibrator, reshaping-function, benjamini-yekutieli, conformal-selection, covariate-shift, sampling-without-replacement, local-dependence, simulations, sharpness]
ingested: 2026-10-08
version: "arxiv 2311.06412v1 (10 Nov 2023, 26 pages, Sections 1-9 and Appendices A-C); later published at AISTATS 2024"
---

# Online multiple testing with e-values

arXiv 2311.06412v1 (November 2023), 26 pages; a version appeared in AISTATS 2024 (not checked against this text). Numbering follows v1: Sections 1–9 (Section 8 holds the proofs), Appendices A (remarks on the problem), B (simulation details), C (sharpness).

## Summary
A stream of hypotheses H_1, H_2, … arrives and each must be rejected or not immediately; the target is FDR(R_t) ≤ α for every t, where R_t is the set of discoveries so far [xuOnlineMultipleTesting2023, eq. 1]. All previous online FDR algorithms take p-values, and the only one valid under arbitrary dependence, r-LOND, shrinks every test level by a reshaping function (the Benjamini–Yekutieli log factor ℓ_t = Σ_{i ≤ t} 1/i), exactly as BY pays relative to BH offline [Sec. 3.1]. The paper replaces the p-value P_t with an e-value E_t (E[E_t] ≤ 1 for t null, eq. 3), rejects when E_t ≥ 1/α_t, and shows that the undiscounted LOND levels α_t = αγ_t(|R_{t−1}| + 1), with (γ_t) a nonnegative sequence summing to at most one, control FDR under arbitrary dependence; this e-LOND algorithm strictly dominates r-LOND applied to 1/E_t for every reshaping sequence [Theorem 1]. The proof is the three-line e-BH argument transplanted to the online setting: 1{E ≥ 1/α} ≤ αE (eq. 6), then telescoping |R_t| ∨ 1 ≥ |R_{i−1}| + 1 for each discovery i. A calibrator f_t that maps p-values onto the r-LOND grid shows r-LOND is literally e-LOND on calibrated p-values, so p-values and e-values can be mixed in one stream [Corollary 1]. Randomising the threshold by one or several independent uniforms (Ue-LOND, Ur-LOND) gives procedures that never reject less and sometimes more, in expectation [Theorems 2–3], an online false-coverage-rate guarantee for e-confidence intervals holds under any dependence and any selection rule [Theorem 4], the FDR bound is attained in the limit [Theorem 6], and simulations with local and sampling-without-replacement dependence, plus an online weighted conformal selection task on HIV drug screening data, show the e-value procedures ahead of r-LOND, Ur-LOND and (for large lags) LORD* [Secs 5–6].

## Main results
- **Setting (Sec. 1)**: null set H_0 ⊆ N, discovery sets R_1 ⊆ R_2 ⊆ …, FDP(R) = |R ∩ H_0|/(|R| ∨ 1), FDR = E[FDP]; an online algorithm is a sequence of (possibly random) levels (α_t), R_t = {i ≤ t : P_i ≤ α_i} or {i ≤ t : E_i ≥ 1/α_i}; the e-value case is the p-value case with P_t = 1/E_t [xuOnlineMultipleTesting2023, eqs 1–3].
- **Doubly sequential framework (Sec. 2, Fig. 1)**: samples and hypotheses both arrive in streams; each experiment t stops at τ_t when its e-process crosses 1/α_t; overlapping experiments share time and data, so test statistics are dependent in unknown ways. The pointer to admissible sequential tests being e-process based is Ramdas et al. 2020 [ramdasAdmissibleAnytimevalidSequential2022].
- **Fact 1 / Fact 2 (Sec. 3.1)**: LOND, α_t = αγ_t(|R_{t−1}| + 1), controls FDR for independent or PRDS p-values; r-LOND, α_t = αγ_t β_t(|R_{t−1}| + 1) with reshaping functions β(r) = ∫_0^r x dν(x), controls FDR under arbitrary dependence; the BY reshaping is β^BY_t(r) = (⌊r⌋ ∧ t)/ℓ_t. Footnote 1 notes Zrnic et al. 2021 state r-LOND with |R_{t−1}| ∨ 1 instead of +1, which is weaker.
- **Theorem 1 (Sec. 3.2)**: e-LOND, α_t = αγ_t(|R_{t−1}| + 1) applied to e-values, has FDR(R_t) ≤ α for every t under arbitrary dependence, and strictly dominates r-LOND applied to (1/E_t) for any sequence of reshaping functions. Proof (Sec. 8.1): FDR ≤ Σ_{i ∈ H_0 ∩ [t]} αγ_i E[E_i] ≤ α; domination since β_t(r) ≤ r and a two-hypothesis example separates the two.
- **Corollary 1**: with the calibrator f_t(p) = (αγ_t ⌈(pℓ_t/(αγ_t)) ∨ 1⌉)^{−1}, e-LOND on E_t = f_t(P_t) is exactly r-LOND with BY reshaping; so only the p-values in a mixed stream need calibrating.
- **Fact 3 and Theorem 2 (Sec. 3.3)**: stochastic rounding S_α̂(E) = (E·1{E ≥ 1/α̂}) ∨ (1{U ≤ Eα̂}/α̂) is an e-value and 1{S_α̂(E) ≥ 1/α̂} = 1{E ≥ U/α̂} (Xu and Ramdas 2023); Ue-LOND uses α_t = α_t^{e-LOND}/U_t, controls FDR under arbitrary dependence and strictly dominates e-LOND in expectation. The uniforms may be a single shared U or independent per hypothesis.
- **Fact 4, Theorem 3, Corollary 2**: for p-values, Ur-LOND uses α_t = αγ_t β_t((|R_{t−1}| + 1)/U_t) and controls FDR under arbitrary dependence, strictly dominating r-LOND in expectation for β^BY; explicitly α_t = αγ_t(⌊(|R_{t−1}| + 1)/U_t⌋ ∧ t)/ℓ_t.
- **Algorithm 1 and Theorem 4 (Sec. 4)**: online selective CIs. A parameter θ_t is selected by an arbitrary data-dependent rule S_t; e-LOND-CI sets α_t = αγ_t(|S_{t−1}| + 1) (Ue-LOND-CI divides by U_t) and reports the e-CI C_t(X_t, α_t) = {θ : E_θ < 1/α_t}. FCR(S_t) ≤ α for all t, for any dependence among the (X_t) and any selection rules; the earlier online FCR method of Weinstein and Ramdas 2020 needed independence or conditional validity plus monotone selection rules. Remark 1: FCR control implies FDR control but not conversely.
- **Section 5 simulations** (γ_t = 1/(t(t + 1)), App. B): null μ ≤ 0 for data bounded in [−4, 4]. (i) Local dependence (Sec. 5.1, Fig. 2): T = 1000 hypotheses, N = 200 samples each, Gaussian-copula dependence with Σ_{ij} = 0.5^{|i−j|} within lag L, μ_1 ∈ {2.5, 3}, α = 0.3, 500 trials; e-values are the Hoeffding e-process of Waudby-Smith and Ramdas stopped at the first crossing of the current e-LOND level, p-values 1/max_i M^i_t. e-LOND beats r-LOND and Ur-LOND for every L and beats LORD* once L ≥ 250 (μ_1 = 3) or L ≥ 150 (stated as μ_1 = 2, presumably 2.5); LORD* needs L known and ignores conflicting hypotheses, so its power falls with L; Ue-LOND is omitted as barely above e-LOND. (ii) Sampling without replacement (Sec. 5.2, Fig. 3): finite population from a discretised Beta with mean 0 or μ_1 ∈ {1.5, 2}, non-null fraction π_1 ∈ [0.1, 0.9], α = 0.05, 500 trials, WoR e-process of Waudby-Smith and Ramdas 2020; e-LOND and Ue-LOND dominate across the board. All empirical FDRs sit well below α.
- **Section 6, Propositions 1–2, Theorem 5**: online model-free selective inference under covariate shift (Jin and Candès 2023). Nulls H_t : Y_{n+t} ≤ c_{n+t} are random, so the e-value condition becomes E[E_t 1{Y_{n+t} ≤ c_{n+t}}] ≤ 1 (eq. 11). The weighted conformal p-values (eq. 12) have intractable dependence, so r-LOND or Ur-LOND on them control FDR (Prop. 1). The e-value E^LOND_t = 1{P_t ≤ α̂^{LOND,+}_t}/α̂^{LOND,−}_t, built from leave-one-out conformal p-values and two LOND runs, is an e-value in the sense of eq. 11 (Prop. 2, proof via Hu and Lei 2023 weighted exchangeability), and e-LOND/Ue-LOND on it control FDR (Thm 5). On the DeepPurpose HIV binding data at α = 0.5 over 600 trials (Fig. 4), Ue-LOND has the largest power and e-LOND the smallest, because E^LOND is all-or-nothing at a conservative level and usually falls below the e-LOND threshold; randomisation repairs this.
- **Theorem 6 (App. C)**: if Σγ_t = 1, there is a joint law on e-values (all nulls, E_t = 1/(αγ_t) on a disjoint event of probability αγ_t, else 0) with FDR(R_t) = α Σ_{i ≤ t} γ_i → α, so the bound of Theorem 1 is sharp; likewise for Ue-LOND and the FCR versions.
- **Open directions (Sec. 9)**: extend to the LORD family, which spends α according to the time since each previous rejection and is more powerful; and to the adaptive SAFFRON and ADDIS procedures, which estimate the null proportion in the manner of Storey. The sharpness result does not rule out improvement in other instances.

## Setting and assumptions
- Each hypothesis t comes with one e-value E_t (E[E_t] ≤ 1 under H_t) or one p-value; no assumption whatever on the joint law of (E_t) across t [xuOnlineMultipleTesting2023, eq. 3]. For p-value procedures the dependence assumptions are: LOND needs independence or PRDS, r-LOND and Ur-LOND nothing, LORD* needs known conflict sets.
- Decisions are immediate; the discount sequence (γ_t) is fixed in advance with Σγ_t ≤ 1; the levels α_t depend on the past only through |R_{t−1}|.
- Within each hypothesis, optional stopping is allowed in the sense of the doubly sequential framework: E_t may be an e-process stopped at a data-dependent time, including one that depends on the current level α_t (App. B.2 uses τ_t = min{i : M^i_t ≥ 1/α̂_t(i)}).
- Randomised variants need uniforms U_t independent of the e-values (or p-values).
- The FCR version needs e-CIs (inverted e-value families) but places no restriction on selection rules or dependence.
- In the conformal application the nulls are random and the e-value condition is the joint one of eq. 11; the covariate-shift likelihood ratio w(x) is assumed known.

## Relation to other sources
- [wangFalseDiscoveryRate2021](wangFalseDiscoveryRate2021.md): the offline template. e-LOND is to LOND what e-BH is to BH (Sec. 3.2); the proof reuses the e-BH inequality 1{E ≥ 1/α} ≤ αE and the calibrator argument that BY is e-BH on calibrated p-values reappears as Corollary 1 for r-LOND.
- [xuPostselectionInferenceEvalue2022](xuPostselectionInferenceEvalue2022.md): supplies the e-CI definition and the offline e-BY procedure; Theorem 4 is the online analogue, with |S_{t−1}| + 1 playing the role of |S|/K.
- [ramdasHypothesisTestingEvalues2025](ramdasHypothesisTestingEvalues2025.md): the stochastic-rounding e-value of Fact 3 is the book's randomised e-BH ingredient (Prop. 9.24) and Ue-LOND is the randomised Markov inequality P(E ≥ U/α) ≤ α (Thm 2.9) applied online; e-BY for FCR is Thm 13.7.
- [ramdasAdmissibleAnytimevalidSequential2022](ramdasAdmissibleAnytimevalidSequential2022.md): cited (as Ramdas et al. 2020) for the claim that every admissible sequential test is built on an e-process, the motivation for taking e-values as the online input.
- [waudbysmithEstimatingMeansBounded2020](waudbysmithEstimatingMeansBounded2020.md): source of the predictable-plug-in Hoeffding e-process (App. B.2, λ = √(8 log(1/(αγ_t))/((u − ℓ)²N))) and of the WoR e-process with the μ^{WoR} adjustment (App. B.3) used in the simulations.
- [vovkEvaluesCalibrationCombination2021](vovkEvaluesCalibrationCombination2021.md): the calibrator definition used for Corollary 1 (nonincreasing, upper semicontinuous, ∫f ≤ 1).
- [wassermanUniversalInference2020](wassermanUniversalInference2020.md): named as the paradigmatic e-value for composite nulls without regularity (log-concavity tests of Dunn et al. 2022, Gangrade et al. 2023).
- [ignatiadisEvaluesUnnormalizedWeights2022](ignatiadisEvaluesUnnormalizedWeights2022.md), [vovkConfidenceDiscoveriesEvalues2023](vovkConfidenceDiscoveriesEvalues2023.md): offline e-value multiple testing cited in Sec. 7 as the body of results being carried online.
- [xuBringingClosureFalse2025](xuBringingClosureFalse2025.md): lists online/infinite-m extensions as future work; this paper is the earlier online route that does not go through closure.
- [ramdasGametheoreticStatisticsSafe2023](ramdasGametheoreticStatisticsSafe2023.md): cited as the catalogue of e-value constructions.
- Without link: Foster and Stine 2008 (alpha-investing, mFDR); Javanmard and Montanari 2015, 2018 (LOND, r-LOND); Ramdas, Yang, Wainwright and Jordan 2017 (LORD++); Ramdas, Zrnic, Wainwright and Jordan 2018 (SAFFRON); Tian and Ramdas 2019 (ADDIS); Zrnic, Ramdas and Jordan 2021 (asynchronous testing, LORD*, local dependence); Zrnic et al. 2020 (batching); Fisher 2022a,b; Robertson, Wason and Ramdas 2023 (survey); Weinstein and Ramdas 2020 (online FCR); Xu and Ramdas 2023 (randomised multiple testing); Jin and Candès 2023 (weighted conformal selection); Hu and Lei 2023; Blanchard and Roquain 2008 (reshaping functions); Benjamini and Yekutieli 2001; Xu, Wang and Ramdas 2021 (bandit multiple testing); Ren and Barber 2023; Ahn, Lin and Mei 2022.

## Concepts touched
- [e-BH, compound e-values and multiple testing](../concepts/e-bh.md): the online counterpart of e-BH and e-BY; the same Markov-plus-telescoping proof.
- [e-variable](../concepts/e-variable.md): 1{E ≥ 1/α} ≤ αE as the whole engine; randomised Markov via stochastic rounding; the joint e-value condition for random nulls (eq. 11).
- [calibrator](../concepts/calibrator.md): the grid calibrator f_t of Corollary 1 that makes r-LOND a special case of e-LOND.
- [e-process](../concepts/e-process.md) and [optional-stopping](../concepts/optional-stopping.md): e-values as stopped e-processes in the doubly sequential framework, stopped at the current online level.
- [confidence-sets-and-sequences](../concepts/confidence-sets-and-sequences.md): e-CIs and online FCR control (Theorem 4).
- online-fdr-control (new): the LOND / r-LOND / LORD / SAFFRON family, discount sequences, conflict sets, and the e-value versions e-LOND, Ue-LOND, Ur-LOND, e-LOND-CI.

## Versions
Only arXiv v1 was read. The AISTATS 2024 proceedings version (PMLR 238) may differ in numbering; not checked.

## Open questions / gaps
- e-LOND is a LOND-type rule (levels grow with the number of rejections, not their recency); an e-value LORD, SAFFRON or ADDIS is left open (Sec. 9).
- The FDR bound is sharp only in the specific adversarial instance of Theorem 6; whether larger levels are possible once discoveries have been made is open.
- In the conformal application e-LOND loses to the p-value procedures because E^LOND is all-or-nothing at a conservative level (Fig. 4); a non-binary e-value for weighted conformal selection would be the natural fix.
- Simulation reporting is thin: Fig. 2 lists a μ_1 value (2) that does not match the stated grid {2.5, 3}; Monte Carlo error is stated as below line width without numbers.
- Candidates for the bib: Javanmard and Montanari 2018 (LOND/r-LOND), Ramdas et al. 2017 (LORD++), Ramdas et al. 2018 (SAFFRON), Zrnic, Ramdas and Jordan 2021 (asynchronous online testing), Robertson, Wason and Ramdas 2023 (survey), Xu and Ramdas 2023 (randomised multiple testing), Weinstein and Ramdas 2020 (online FCR), Jin and Candès 2023 (weighted conformal selection).
