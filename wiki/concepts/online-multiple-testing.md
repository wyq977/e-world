---
slug: online-multiple-testing
title: Online multiple testing with e-values
sources: 5
updated: 2026-10-12
---

# Online multiple testing with e-values

## Definition
Hypotheses arrive one at a time, a filtration fixes what each decision may use, and a procedure is online if its output on a set S is measurable at time max S; offline testing is the case of a constant filtration [fischerAdmissibleOnlineClosed2024, Sec. 2]. Classical procedures (LOND, LORD, SAFFRON, alpha-investing) fix each decision at arrival and control OnlineFDR = sup_t FDR_t; the stronger SupFDR = E[sup_t FDP_t] gives validity at arbitrary stopping times [fischerOnlineGeneralizationEBH2024, Sec. 1.2]. With e-values the dependence penalties of the p-value world disappear: e-LOND keeps the LOND levels α γ_t (|R_{t−1}| + 1) on e-values with no reshaping, controls FDR at every t under arbitrary dependence, and strictly dominates r-LOND applied to 1/E_t [xuOnlineMultipleTesting2023, Thm 1].

## Key results
- e-LOND proof is the [e-BH](e-bh.md) argument moved online: 1{E ≥ 1/α} ≤ αE plus telescoping; r-LOND is e-LOND on calibrated p-values; Ue-LOND divides the level by an independent uniform (stochastic rounding) and strictly dominates e-LOND; e-LOND-CI controls the online false coverage rate for e-confidence intervals under any dependence and selection; the FDR bound is sharp [xuOnlineMultipleTesting2023, Cor. 1, Thms 2–4, 6].
- Online e-BH: nested rejection sets ("ARC" procedures, rejections never undone), reject i ≤ t iff E_i ≥ 1/(k*_t α γ_i) with a nondecreasing k*_t; it is exactly e-BH at a known horizon, controls SupFDR ≤ α under arbitrary dependence by weighted self-consistency and Fatou, uniformly dominates e-LOND, and upgrades e-LOND, r-LOND, online BR, TOAD and e-TOAD to SupFDR control; boosting with per-hypothesis truncation and a new local-dependence boosting (factors 1.27–2.64 vs 1.17) [fischerOnlineGeneralizationEBH2024, Def. 1, Prop. 2.1, Thm 2.2, Props 2.3–2.4, A.1].
- Online BH on p-values: OnlineFDR ≤ α under PRDS; SupFDR ≤ α(1 + log(1/α)) under PRDN via a weighted FDR-linking theorem, sharp even for independent p-values; nothing below 1 for infinite streams under arbitrary dependence; StopFDR ≤ α implies SupFDR ≤ α(1 + log(1/α)) by Ville [fischerOnlineGeneralizationEBH2024, Prop. 3.1, Thms 3.2–3.9, G.3].
- Online closed testing: every coherent online true-discovery procedure is dominated by an online closed procedure built from increasing online intersection tests; such families are exactly what anytime-valid tests per intersection hypothesis produce, and by the admissibility paper every anytime-valid test is a thresholded test martingale, so admissible online closed testing must multiply sequential e-values; SeqE-Guard computes the full closed procedure in linear time per query set; 300 e-values of 0.9 and 700 of 1.1 give at least 306 discoveries where e-BH rejects nothing; hedged GRO e-values 1 − λ_i + λ_i E_i with an estimated null fraction are growth-optimal under a two-groups mixture [fischerAdmissibleOnlineClosed2024, Thms 2.1–2.3, 3.1, Example 2, Prop. 3.4]; see [e-closure-principle](e-closure-principle.md).
- Admissible-but-incoherent online procedures exist, unlike offline [fischerAdmissibleOnlineClosed2024, Example 1].
- Multi-stream change detection is the same problem over time: the e-detector values at each time are fed into e-BH, Bonferroni or Holm with "error over patience" guarantees [dandapanthulaMultipleTestingMultistream2025, Algs 1–4]; see [e-detector](e-detector.md).
- FWER procedures with e-values in the sequential setting (post-hoc anytime-valid and always-valid FWER) [hartogFamilyWiseError2025, Thms 2.4–2.5].

## Variants and related concepts
- [e-bh](e-bh.md), [e-closure-principle](e-closure-principle.md), [calibrator](calibrator.md), [optional-stopping](optional-stopping.md).

## Sources
- [xuOnlineMultipleTesting2023](../sources/xuOnlineMultipleTesting2023.md) — e-LOND family.
- [fischerOnlineGeneralizationEBH2024](../sources/fischerOnlineGeneralizationEBH2024.md) — online e-BH and BH, SupFDR.
- [fischerAdmissibleOnlineClosed2024](../sources/fischerAdmissibleOnlineClosed2024.md) — online closed testing.
- [dandapanthulaMultipleTestingMultistream2025](../sources/dandapanthulaMultipleTestingMultistream2025.md) — multi-stream detection.
- [hartogFamilyWiseError2025](../sources/hartogFamilyWiseError2025.md) — sequential FWER.

## Disagreements / open issues
- e-value versions of LORD and SAFFRON are open [xuOnlineMultipleTesting2023, Sec. 9]; stochastic rounding does not combine with online e-BH [fischerOnlineGeneralizationEBH2024, Remark 1].
- The online e-closure papers of 2026 (online analogs of e-closure, dynamic e-closure) are in the reading queue, not ingested.
