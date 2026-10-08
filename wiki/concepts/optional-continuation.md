---
slug: optional-continuation
title: Optional continuation
sources: 13
updated: 2026-10-08
---

# Optional continuation

## Definition
Optional continuation is deciding after each study whether to run another one, with the next e-variable's design (prior, sample size, stopping rule) chosen using everything seen so far, and multiplying the new e-value onto the running product [grunwaldSafeTesting2024, after Cor. 1]. The product is a [test martingale](test-martingale.md) at the study level, so [Ville's inequality](villes-inequality.md) controls type-I error under any continuation rule, including externally imposed or unknowable ones [grunwaldSafeTesting2024, Prop. 2, Cor. 1]. Formally, continuation is multiplication of an [e-process](e-process.md) by a new one at a stopping time [ramdasHypothesisTestingEvalues2025, Prop. 7.9].

## Key results
- Bayesian updating is a special case of optional continuation, the "local perspective" [grunwaldSafeTesting2024, Example 1].
- Continuation (study level, free choice of the next e-variable) and optional stopping (data level) are formally the same Ville–Robbins condition, but stopping inside a study needs extra structure [grunwaldSafeTesting2024, Sec. 5]; see [optional-stopping](optional-stopping.md).
- The authors' reply stresses that continuation across studies, not interim analysis, is the main point of e-values [grunwaldSafeTesting2024, reply Sec. 5].
- Contrast with p-value meta-analysis, which cannot combine results chosen in this way [ramdasHypothesisTestingEvalues2025, Sec. 1.2.1, Sec. 4.3].
- Opportunistic testing: successive bets multiply without a pre-declared strategy; Bonferroni is twenty all-or-nothing bets of one each; 'we cannot pretend to have stopped before we actually did' [shaferTestingBettingStrategy2021, Secs 2.1.2, 4.2].
- Products of two log-optimal anytime-valid e-values from consecutive stopped experiments are safe even against adaptively changing null elements; a sharper infimum-of-products version is valid only for a fixed null [koolenLogoptimalAnytimevalidEvalues2022, Sec. 5].
- Products of conditionally valid unit bets and ALL-IN meta-analysis as a study-level test martingale, safe under continuation even when the RIPr gives no outcome-level e-process [ramdasGametheoreticStatisticsSafe2023, Sec. 2.10, Sec. 6.1].
- Survival trials: the product of per-trial logrank martingales stays a test martingale when trial start times depend on other trials' data, by a left-truncation argument; basis of living meta-analysis of interim results [terschureAnytimevalidLogrankTest2024, Prop. 5.1]. The stopped SWEPIS e-value can be multiplied with other trials' e-values [turnerGenericEvariablesExact2024, Sec. 7].
- The reply insists continuation across studies is the target, distinct from restricted optional stopping and interim analysis; continuation arises automatically in meta-analysis; the sceptical p-value is not designed for repeated continuation [grunwaldAuthorsReplyDiscussion2024, Secs 2, 4]. Per-batch e-variables for maximum entropy models multiply across independent studies [giuffridaTestingMaximumEntropy2025, Sec. II].
- Test-scale formulation: a [0,1]-valued outcome serves as a conditional significance level for the next test, equivalent on the e-scale to multiplying sequential e-values; data-dependent level switching via E[φ_2/α′] ≤ 1; reporting the whole family (φ^P) dominates continuing from the infimum [koningAnytimeValidityFree2026, Thms 4–6, Remark 13, Sec. 5.1]; see [test-induction](test-induction.md).
- Product property with a data-dependently chosen next e-statistic, including 'do not continue' [perezortizEstatisticsGroupInvariance2024, Sec. 2.3]; a single factor 2 on the capped e-posterior risk is continuation-friendly without modifying each study's e-value [grunwaldEposterior2023, Prop. 2]; e-BH accepts stopped e-processes from continued studies [wangFalseDiscoveryRate2021, Sec. 7].

## Variants and related concepts
- [e-merging](e-merging.md), for combining without a sequential structure.

## Sources
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — definition, Cor. 1, Example 1, Sec. 5, reply.
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — Sec. 4.3, Prop. 7.9.
- [shaferTestingBettingStrategy2021](../sources/shaferTestingBettingStrategy2021.md) — opportunistic testing.
- [koolenLogoptimalAnytimevalidEvalues2022](../sources/koolenLogoptimalAnytimevalidEvalues2022.md) — products under changing nulls.
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md), [terschureAnytimevalidLogrankTest2024](../sources/terschureAnytimevalidLogrankTest2024.md), [turnerGenericEvariablesExact2024](../sources/turnerGenericEvariablesExact2024.md) — meta-analysis.
- [grunwaldAuthorsReplyDiscussion2024](../sources/grunwaldAuthorsReplyDiscussion2024.md), [giuffridaTestingMaximumEntropy2025](../sources/giuffridaTestingMaximumEntropy2025.md) — continuation as the target.
- [koningAnytimeValidityFree2026](../sources/koningAnytimeValidityFree2026.md), [perezortizEstatisticsGroupInvariance2024](../sources/perezortizEstatisticsGroupInvariance2024.md), [grunwaldEposterior2023](../sources/grunwaldEposterior2023.md), [wangFalseDiscoveryRate2021](../sources/wangFalseDiscoveryRate2021.md) — batch-3 contributions.

## Disagreements / open issues
- Whether conditional e-variables are the right building blocks when e-variable types switch across studies is raised but not settled [grunwaldSafeTesting2024, Sec. 1.3].
