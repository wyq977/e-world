---
slug: e-bh
title: e-BH, compound e-values and multiple testing
sources: 17
updated: 2026-10-12
---

# e-BH, compound e-values and multiple testing

## Definition
The e-Benjamini–Hochberg procedure rejects the k* hypotheses with the largest e-values, where k* = max{k : k e_[k] / K ≥ 1/α} [ramdasHypothesisTestingEvalues2025, Definition 9.8]. It controls the false discovery rate under arbitrary dependence, with a post-hoc guarantee in α [Thm 9.11]. A compound e-value is a vector (E_1, …, E_K) with Σ_{k : P ∈ P_k} E_P[E_k] ≤ K for every P, tight if equality holds [Definition 9.1]; every FDR-controlling procedure is e-BH applied to some compound e-values [Thms 9.18–9.19].

## Key results
- Self-consistency, boosting, universality and minimally adaptive e-BH [ramdasHypothesisTestingEvalues2025, Def. 9.9, Thm 9.13, Thm 9.19, Sec. 9.4].
- Randomised e-BH via stochastic rounding (rounding an e-value onto a grid while preserving its expectation) rejects weakly more; closed e-BH strictly improves e-BH through an FDR closure principle [ramdasHypothesisTestingEvalues2025, Prop. 9.24, Thms 9.27, 9.29, Def. 9.31, Thms 9.32–9.36].
- Log-optimal simple separable compound e-values; approximate and asymptotic compound e- and p-values [ramdasHypothesisTestingEvalues2025, Thm 9.21, Defs 10.13, 10.17, 10.22, Thm 10.24].
- e-weighted BH and e-values as unnormalised weights [ramdasHypothesisTestingEvalues2025, Thm 11.10].
- e-BY controls the false coverage rate for e-confidence intervals [ramdasHypothesisTestingEvalues2025, Thm 13.7]; see [confidence-sets-and-sequences](confidence-sets-and-sequences.md).
- Post-hoc choice of α in e-BH extends to general e-closure procedures [ramdasHypothesisTestingEvalues2025, Thm 9.10 as cited by later work]; see [post-hoc-validity](post-hoc-validity.md).
- Precursor: Vovk and Wang's multiple testing is FWER-type via closure of e-merging functions, not e-BH; FDP control by non-singleton closure is flagged as the next step [vovkEvaluesCalibrationCombination2021, Sec. 5, App. A.3].
- Survey statement of e-BH: k* = max{k : e_[k] ≥ K/(kα)}, FDR under arbitrary dependence, also for stopped e-processes in bandit testing; e-values as unnormalised weights; e-BY for false coverage rate; 'e-hacking' as reporting the best of many strategies, exposed by the implied alternative at preregistration [ramdasGametheoreticStatisticsSafe2023, Secs 6.2–6.4].
- Primary source now ingested: e-BH rejects the k* largest with k* = max{k : k e_[k]/K ≥ 1/α}, equivalently e_k ≥ t_α with t_α R(t_α) = K/α; FDR ≤ K_0 α/K under arbitrary dependence in three lines from self-consistency, where self-consistent p-procedures only reach α(1 + log(1/α)); boosting by factors b_k with E[T(αb_kE_k)] ≤ α, typical gains 1.3–10; exact FDR identity and sharpness; PRDS version; e-BH dominates every FDR procedure applying a common increasing transform; structured, post-selection, focused and grouped variants valid under any selection; bandit and cryptocurrency applications [wangFalseDiscoveryRate2021, eq. 1, Props 1–4, Thms 2–5, Secs 4.2, 5.1, 7–8].
- Closed e-BH uniformly improves e-BH and equals e-BH on compound e-values; closed BY and closed Su; BH-type e-collections give no gain [xuBringingClosureFalse2025, Thms 17, 25, 28, 34, 37]; closed BH as the p-value counterpart, gaining only when BH already rejects at least √m [goemanUniformImprovementBenjaminiHochberg2026, Props 16, 18]; see [e-closure-principle](e-closure-principle.md).
- The confidence-bound alternative: discovery e-matrices compared with BH/BY rejection counts, and the generalized Bayes factor with learning rate η showing the likelihood ratio can be far from optimal as a base e-value in multiple testing [vovkConfidenceDiscoveriesEvalues2023, Tables 2, 4, 5, App. D].
- e-values as unnormalised weights: running a p-procedure on (p_k/E_k) ∧ 1 is weighted BH or Bonferroni with weights E_k that need not sum to K; FDR ≤ ℓ_K π_0 α under arbitrary dependence given only null independence of p and e, π_0 α under PRDS of the p-vector, with Storey adaptivity and Simes/Hochberg FWER variants; the first minimally adaptive e-BH; pe-BH valid but dominated; mouse striatum data 2387 vs 1973 discoveries [ignatiadisEvaluesUnnormalizedWeights2022, Def. 4.2, Thms 4.3, 4.7, 4.9, 4.10, Prop. S3.3, Thm S3.2, Table 1].
- e-BY, the parent of e-BH: reporting selected e-confidence intervals at level α|S|/K controls the false coverage rate under arbitrary dependence and arbitrary selection; sharp and admissible; weighted version; indicator e-CIs recover e-BH's FDR and a directional e-BH; the post-hoc level bound E[sup_α FCP(α)/α] ≤ 1 [xuPostselectionInferenceEvalue2022, Thms 2–5, Cors 1, 3, 4]. Compound e-values, universality and derandomisation [ignatiadisAsymptoticCompoundEvalues2024, Thms 4.3–4.4, App. C]; see [approximate-and-asymptotic-e-values](approximate-and-asymptotic-e-values.md). Post-hoc FWER and FDP as post-hoc validity of sup_i φ_i and of a p-function [koningPosthocAlphaHypothesis2023, Thms 7–8].
- The model-X knockoff filter is literally e-BH on e_j = p·1{W_j ≥ T}/(1 + Σ_k 1{W_k ≤ −T}), which are not e-values individually but satisfy Σ_{H_0} E[e_j] ≤ p, nearly saturating the e-BH proof inequality; derandomisation by averaging per-run e-values over M knockoff draws then e-BH, FDR ≤ α for any M and any inner level, converging to a deterministic selection as M → ∞; the inner level must be reduced (α_kn ≈ α/2); strictly more powerful than data-splitting inclusion rates; fixed-X, robust, multi-environment and side-information extensions [renDerandomizedKnockoffsLeveraging2022, Thms 1–3, Remark 1, Secs 3.1–3.3, App. A].
- Online: e-LOND, Ue-LOND, e-LOND-CI and online e-BH with SupFDR control [xuOnlineMultipleTesting2023, Thms 1–4; fischerOnlineGeneralizationEBH2024, Thm 2.2]; see [online-multiple-testing](online-multiple-testing.md). Closed e-BH and the inadmissibility of e-BH and BY [xuBringingClosureFDR2025, Props 2, 5]. Multi-stream change detection feeds e-detector values into e-BH with error-over-patience control [dandapanthulaMultipleTestingMultistream2025, Thm 4.2]. Example where 300 e-values of 0.9 and 700 of 1.1 give 306 discoveries by online closed testing while e-BH rejects nothing [fischerAdmissibleOnlineClosed2024, Example 2].

## Variants and related concepts
- [e-merging](e-merging.md), [post-hoc-validity](post-hoc-validity.md).

## Sources
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — Chapters 9, 10, 11, 13.
- [vovkEvaluesCalibrationCombination2021](../sources/vovkEvaluesCalibrationCombination2021.md) — FWER precursor.
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md) — survey statement.
- [wangFalseDiscoveryRate2021](../sources/wangFalseDiscoveryRate2021.md) — primary source.
- [xuBringingClosureFalse2025](../sources/xuBringingClosureFalse2025.md), [goemanUniformImprovementBenjaminiHochberg2026](../sources/goemanUniformImprovementBenjaminiHochberg2026.md), [vovkConfidenceDiscoveriesEvalues2023](../sources/vovkConfidenceDiscoveriesEvalues2023.md) — closure and confidence-bound views.
- [ignatiadisEvaluesUnnormalizedWeights2022](../sources/ignatiadisEvaluesUnnormalizedWeights2022.md) — e-weighted BH.
- [xuPostselectionInferenceEvalue2022](../sources/xuPostselectionInferenceEvalue2022.md) — e-BY.
- [ignatiadisAsymptoticCompoundEvalues2024](../sources/ignatiadisAsymptoticCompoundEvalues2024.md), [koningPosthocAlphaHypothesis2023](../sources/koningPosthocAlphaHypothesis2023.md) — compound e-values, post-hoc multiple testing.
- [renDerandomizedKnockoffsLeveraging2022](../sources/renDerandomizedKnockoffsLeveraging2022.md) — knockoffs as e-BH, derandomisation.
- [xuOnlineMultipleTesting2023](../sources/xuOnlineMultipleTesting2023.md), [fischerOnlineGeneralizationEBH2024](../sources/fischerOnlineGeneralizationEBH2024.md), [xuBringingClosureFDR2025](../sources/xuBringingClosureFDR2025.md), [dandapanthulaMultipleTestingMultistream2025](../sources/dandapanthulaMultipleTestingMultistream2025.md), [fischerAdmissibleOnlineClosed2024](../sources/fischerAdmissibleOnlineClosed2024.md) — online, closed and multi-stream variants.

## Disagreements / open issues
- The 2026 online e-closure papers are in the reading queue, not ingested.
