---
slug: e-merging
title: Merging e-values and p-values
sources: 9
updated: 2026-10-08
---

# Merging e-values and p-values

## Definition
An e-merging function F produces an [e-variable](e-variable.md) F(E_1, …, E_K) from any e-variables, whatever their dependence [ramdasHypothesisTestingEvalues2025, Definition 8.1]. The arithmetic mean essentially dominates every symmetric merger, and the admissible e-merging functions are exactly the weighted arithmetic means, a result of Wang 2025 proved via optimal transport [ramdasHypothesisTestingEvalues2025, Prop. 8.3, Thm 8.4, Lemma 11.1]. Independent or sequential e-values may instead be multiplied; sequential e-values need martingale merging [Thm 8.12].

## Key results
- ie-merging and products for independent e-values, mean–variance trade-off, FWER control by averaging [ramdasHypothesisTestingEvalues2025, Sec. 8.2, Prop. 8.16, Algorithm 8.18].
- p-merging under arbitrary dependence: twice the mean of p-values is a p-value, and every admissible p-merging function is dominated by a calibrate–average–threshold rule, so p-merging goes through e-values [ramdasHypothesisTestingEvalues2025, Props 12.1, 12.4, Thms 12.15, 12.17, 12.18, Table 12.29]; see [calibrator](calibrator.md).
- Exchangeable and randomised p-combinations [ramdasHypothesisTestingEvalues2025, Thms 12.27–12.28].
- Averages of split-LRT statistics are the simplest instance of e-merging under dependence [wassermanUniversalInference2020, Sec. 4]; see [universal-inference](universal-inference.md).
- Primary source: e-, ie- and se-merging functions and domination; the arithmetic mean essentially dominates every symmetric e-merger and {λ + (1−λ)M_K} is the minimal complete class of symmetric mergers; the product is admissible and weakly dominates every ie-merger; U-statistics are admissible but not a complete class; Rüger and M-family p-mergers reappear as precise but inadmissible e-mergers; Bonferroni is admissible among p-mergers; e-to-p merging is average-then-invert, p-to-e is calibrate-then-average [vovkEvaluesCalibrationCombination2021, Props 3.1, 4.1–4.2, 6.1, Thm 3.2, Remark 4.3, Sec. 6, App. F–G].
- Family-wise validity: adjusted e-values E*_k are family-wise valid if E_Q[max_{k : Q ∈ H_k} E*_k] ≤ 1 for all Q, the e-analogue of FWER; closure of the mean gives an O(K²) procedure valid under any dependence and closure of the product an O(K) procedure for sequential e-values [vovkEvaluesCalibrationCombination2021, eq. 9, Thm 5.1, Algorithms 1–2]; non-singleton closure for FDP control is flagged as future work.
- Shafer's reply endorses weighted averaging of bets, equal to a Bayes factor for simple nulls with prior weights, over max-plus-adjustment [shaferTestingBettingStrategy2021, reply]; Koolen and Grünwald explain why the product's robustness to changing nulls costs power when the null is fixed [koolenLogoptimalAnytimevalidEvalues2022, Sec. 5].
- Survey: averaging arbitrarily dependent e-values with weights fixed in advance; multiplication of independent or conditionally valid e-values [ramdasGametheoreticStatisticsSafe2023, Secs 2.9–2.10].
- Closure of the arithmetic mean over all index sets with |R \ I| = j gives FDP-type bounds; Bonferroni and Simes e-mergers as lower bounds with tight ratios ln n + 1 and n; e-Bonferroni far worse than averaging for FDP control; U-statistic merger under independence [vovkConfidenceDiscoveriesEvalues2023, Sec. 6, App. B, Remark 6.5].
- The arithmetic mean as local e-value makes closed e-BH valid under arbitrary dependence; admissible procedures reduce to weighted affine mergers via Clerico's characterisation [xuBringingClosureFalse2025, eq. 6, Thm 17, App. B, Prop. 51]; e_S as the mean merger of indicator e-values certifies a whole range of nested rejection sets via the horizon lemma [goemanUniformImprovementBenjaminiHochberg2026, eq. 9, Lemma 10]; group-level averaging or products before post-selection e-BH [wangFalseDiscoveryRate2021, Sec. 5.1].

## Variants and related concepts
- [e-bh](e-bh.md), merging for multiple testing rather than a single decision.
- [optional-continuation](optional-continuation.md), merging by multiplication over time.

## Sources
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — Chapters 8, 11, 12.
- [vovkEvaluesCalibrationCombination2021](../sources/vovkEvaluesCalibrationCombination2021.md) — the primary source.
- [shaferTestingBettingStrategy2021](../sources/shaferTestingBettingStrategy2021.md), [koolenLogoptimalAnytimevalidEvalues2022](../sources/koolenLogoptimalAnytimevalidEvalues2022.md) — averaging vs product.
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md) — survey summary.
- [vovkConfidenceDiscoveriesEvalues2023](../sources/vovkConfidenceDiscoveriesEvalues2023.md), [xuBringingClosureFalse2025](../sources/xuBringingClosureFalse2025.md), [goemanUniformImprovementBenjaminiHochberg2026](../sources/goemanUniformImprovementBenjaminiHochberg2026.md), [wangFalseDiscoveryRate2021](../sources/wangFalseDiscoveryRate2021.md) — batch-3 contributions.

## Disagreements / open issues
- Primary sources not yet in the bib: Vovk and Wang 2021 is in the bib; Wang 2025 "The only admissible way of merging arbitrary e-values", Vovk, Wang and Wang 2022 on p-merging, and Vovk and Wang 2024 on martingale merging are not.
