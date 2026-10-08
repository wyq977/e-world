---
slug: confidence-sets-and-sequences
title: E-confidence sets and confidence sequences
sources: 9
updated: 2026-10-08
---

# E-confidence sets and confidence sequences

## Definition
An e-confidence set inverts a family of [e-variables](e-variable.md) indexed by the parameter: C = {θ : E(θ) < 1/α} [ramdasHypothesisTestingEvalues2025, Definition 13.1; wassermanUniversalInference2020, eq. 4, Thm 1]. A confidence sequence is a sequence of sets (C_t) with P(∃t : θ* ∉ C_t) ≤ α, hence valid at any stopping or random time; it is dual to an [e-process](e-process.md) and to anytime p-values [wassermanUniversalInference2020, Thm 11; ramdasHypothesisTestingEvalues2025, Sec. 13.1.1]. Robbins introduced confidence sequences [ramdasHypothesisTestingEvalues2025, Sec. 1.8.2].

## Key results
- Universal confidence sets shrink at the optimal rate O_p(√(log(1/α)/n)) in regular models and at Hellinger rates nonparametrically, with an explicit Gaussian radius [wassermanUniversalInference2020, Thms 5–6; ramdasHypothesisTestingEvalues2025, Thm 5.9].
- Profile versions for functionals ψ = g(θ) and coverage of the RIPr under misspecification in convex classes [wassermanUniversalInference2020, eq. 14, Prop. 7].
- Running intersection and duality: p_t < α iff C_t ∩ Θ_0 = ∅, with a converse for closed nulls; sequential t-test example [wassermanUniversalInference2020, Sec. 7].
- Stopped confidence sequences give e-CIs; level-free e-CIs when E does not depend on α; one-observation t-CI [ramdasHypothesisTestingEvalues2025, Prop. 13.4, Thm 13.5, Example 13.2].
- e-BY controls the false coverage rate for e-CIs under arbitrary dependence, and majority-vote merging combines e-CIs [ramdasHypothesisTestingEvalues2025, Def. 13.6, Thms 13.7–13.8]; see [e-bh](e-bh.md).
- REGROW confidence intervals shrink at O(log n / n), slower than the O(log log n / n) of stitching, which GRO does not explain [grunwaldSafeTesting2024, Sec. 8].
- Definition with a drifting estimand and the equivalence of uniform, stopping-time and random-time coverage; duality with always-valid p-values and tests of power one; running intersection [howardTimeuniformNonparametricNonasymptotic2021, eq. 1, Lemma 3, Sec. 6]. The boundary constructions have their own page: [confidence-sequence-boundaries](confidence-sequence-boundaries.md).
- Shafer's (1/α)-warranty sets {θ : S(θ) < 1/α}: every confidence set is a warranty set from all-or-nothing bets, warranty sets nest in α, are valid under optional continuation, and warranty equals confidence in Protocol 5; a Hoeffding strategy gives capital ≥ 20 whenever |mean| > 2.72/√n for all n [shaferTestingBettingStrategy2021, Secs 4.2–4.3, reply].
- Survey: inversion C_t = {θ : M^θ_t < 1/α}, explicit sub-Gaussian, empirical-Bernstein and betting sequences, asymptotic and reverse-submartingale sequences, e-confidence intervals versus credible and support intervals [ramdasGametheoreticStatisticsSafe2023, Sec. 2.8, eq. 12, Secs 5, 6.3, App. A].
- Exact anytime-valid confidence sequences for risk difference, relative risk and odds ratio in 2 × 2 tables by inverting GRO e-variables over effect sizes; one-sided union for the non-convex odds-ratio level set [turnerExactAnytimevalidConfidence2023, eq. 12, Sec. 3.1]; hazard-ratio sequences from the prequential logrank statistic [terschureAnytimevalidLogrankTest2024, Sec. 6].
- Ly's incompatibility: under GROW point priors a test and an anytime-valid confidence interval cannot both shrink and be consistent; the authors 'did not realize this' and point to REGROW and nonlocal priors; Cattaneo's minimum-e-value estimator under optional continuation is open [grunwaldAuthorsReplyDiscussion2024, Secs 3, 5].

## Variants and related concepts
- [universal-inference](universal-inference.md), [villes-inequality](villes-inequality.md), [post-hoc-validity](post-hoc-validity.md).

## Sources
- [wassermanUniversalInference2020](../sources/wassermanUniversalInference2020.md) — universal sets, confidence sequences, duality.
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — Chapter 13, Thm 5.9.
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — rate comparison.
- [howardTimeuniformNonparametricNonasymptotic2021](../sources/howardTimeuniformNonparametricNonasymptotic2021.md) — definition, equivalences, duality.
- [shaferTestingBettingStrategy2021](../sources/shaferTestingBettingStrategy2021.md) — warranty sets.
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md) — catalogue.
- [turnerExactAnytimevalidConfidence2023](../sources/turnerExactAnytimevalidConfidence2023.md), [terschureAnytimevalidLogrankTest2024](../sources/terschureAnytimevalidLogrankTest2024.md) — exact applied sequences.
- [grunwaldAuthorsReplyDiscussion2024](../sources/grunwaldAuthorsReplyDiscussion2024.md) — test/interval consistency.

## Disagreements / open issues
- Estimation is declared out of scope by the book, so confidence sequences are only sketched there [ramdasHypothesisTestingEvalues2025, Sec. 13.1.1].
