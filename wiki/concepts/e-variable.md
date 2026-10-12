---
slug: e-variable
title: E-variable
sources: 33
updated: 2026-10-12
---

# E-variable

## Definition
An e-variable is a [0, ∞]-valued statistic E with E_P[E] ≤ 1 under every distribution P in the null hypothesis; its realised value is an e-value, and it is called exact if the expectation equals one [ramdasHypothesisTestingEvalues2025, Definition 1.2; grunwaldSafeTesting2024, eq. 1]. Rejecting when E ≥ 1/α is a level-α test by Markov's inequality [grunwaldSafeTesting2024, Prop. 1], and 1/E is a conservative p-value. For a simple null P the admissible e-variables are exactly likelihood ratios dS/dP with S a sub-probability measure [ramdasHypothesisTestingEvalues2025, Prop. 2.12; grunwaldSafeTesting2024, eq. 9]. Earlier names for the same object include S-value, betting score and Skeptic's capital [grunwaldSafeTesting2024, Sec. 7].

## Key results
- Closure: averages of e-variables are e-variables under arbitrary dependence; products of independent e-variables are e-variables; maxima are not [ramdasHypothesisTestingEvalues2025, Fact 1.3; wassermanUniversalInference2020, Sec. 4].
- Every e-variable is a calibrated exact p-variable, and the duality sup E = 1 / inf P links the two [ramdasHypothesisTestingEvalues2025, Prop. 2.7, Thm 14.2]; see [calibrator](calibrator.md).
- Representation: every e-variable is a conditional expectation of a likelihood ratio [ramdasHypothesisTestingEvalues2025, Thm 14.4].
- Admissibility: an e-variable is admissible if no other e-variable dominates it; characterised by a liminf condition [ramdasHypothesisTestingEvalues2025, Def. 2.11, Thm 2.14, Cor. 2.15].
- Randomised Markov: P(E ≥ U/α) ≤ α for an independent uniform U, so randomised tests reject strictly more; exchangeable Markov inequalities (EMI, EUMI) extend this to averages [ramdasHypothesisTestingEvalues2025, Thm 2.9, Thm 5.6, Thm 5.7].
- Three readings of an e-value: a gambling payoff, a conservative p-value, and a Bayes factor with a particular prior [grunwaldSafeTesting2024, Sec. 1.1]; see [testing-by-betting](testing-by-betting.md) and [bayes-factor-e-variable](bayes-factor-e-variable.md).
- Composite nulls are sets of distributions, often with no common reference measure; the book uses a generalised absolute continuity and the bipolar "effective null" P°° [ramdasHypothesisTestingEvalues2025, eq. 6.2, Sec. 6.3.1, Thm 6.10]; see [numeraire](numeraire.md).

## Catalogue of constructions
- Likelihood ratio for simple vs simple, log-optimal with e-power equal to KL [ramdasHypothesisTestingEvalues2025, Thm 3.20].
- Split likelihood ratio for arbitrary composite nulls with computable MLE [wassermanUniversalInference2020]; see [universal-inference](universal-inference.md).
- GRO e-variable q/p*_0 with the reverse information projection in the denominator [grunwaldSafeTesting2024, Thm 1]; see [gro-criterion](gro-criterion.md).
- Conditional, universal-inference and sequential plug-in e-variables for exponential families [haoEValuesExponentialFamilies2025]; see [exponential-family-e-values](exponential-family-e-values.md).
- Soft-rank e-value for Monte Carlo and permutation settings: E = (B+1)R_0 / Σ R_b, with 1/E at least the permutation p-value; it is the numeraire for exchangeability [ramdasHypothesisTestingEvalues2025, Sec. 1.7, Sec. 2.6.7, Sec. 6.7.7].
- E-variables for monotone likelihood ratio, symmetry, mean and variance, sub-Gaussian, constrained and exchangeable nulls [ramdasHypothesisTestingEvalues2025, Sec. 2.6].
- Backtest e-statistics e(x, r): e-variables for the null ρ(F) ≤ r with mean above one when ρ(F) > r, including an expected-shortfall and value-at-risk pair [ramdasHypothesisTestingEvalues2025, Defs 16.5–16.6, Thm 16.11].
- Canonical modern definition and the betting reading: E ≥ 0 with E_Q[E] ≤ 1, infinity meaning outright rejection; e-values are defined through expectations where p-values use probabilities, so 1/e is exactly a p-value but not conversely [vovkEvaluesCalibrationCombination2021, Sec. 2, Remark 2.3]; the universal quantifier over probability spaces can be replaced by one rich model [vovkEvaluesCalibrationCombination2021, App. D].
- Shafer's betting score S with E_P[S] = 1 is the same object; every bet implies an alternative Q = SP, so betting scores are likelihood ratios; the level-α test is the all-or-nothing bet (1/α)1_E [shaferTestingBettingStrategy2021, Sec. 2]. Grünwald's discussion proves equivalence with the ≤ 1 definition.
- The survey's 'unit bet' terminology and the remark that statisticians always used e-values via likelihood ratios, interesting only for composite nulls [ramdasGametheoreticStatisticsSafe2023, Sec. 2.1].
- Local e-variables (null restricted to a canonical neighbourhood) need not be global, but locality for all alternatives in the generated family implies globality [grunwaldOptimalEValuesExponential2024, Sec. 2, Thm 1, Fig. 3].
- Constructive e-variables for composite nulls without invariance: the k-sample block e-variable [turnerGenericEvariablesExact2024, Thm 1], the lifted single-outcome e-variable for general two-sample nulls [turnerExactAnytimevalidConfidence2023, Thm 1], the one-event partial-likelihood ratio for survival data [terschureAnytimevalidLogrankTest2024, eq. 3.3]; see [k-sample-and-contingency-table-e-values](k-sample-and-contingency-table-e-values.md), [survival-e-values](survival-e-values.md).
- Two constructions from the reply: the robustified (1 − γ)E + γ with γ learnable by mixtures, and the renormalised empirical e-variable [grunwaldAuthorsReplyDiscussion2024, Secs 3–4].
- Infinite-valued e-variables are essential; Example 4.4 gives a null where every [0,1]-valued function is an e-variable; exact description of the e-variable class under symmetry [larssonNumeraireEvariableReverse2025, Thm 2.6, Remark 3.14, Sec. 5.4].
- E-variables are exactly the Type-I risk safe statistics; S_np(α) = (1/α)1{P ≤ α} reproduces every level-α test; sharpness E_{P0}[S] = 1 [grunwaldBeyondNeymanPearsonEvalues2024, Prop. 1, Example 2, Thm 1].
- Six statistical reasons to prefer e-values with concrete constructions: (ΣX_i)/(nμ) for nonnegative data, exp(λX − λ²X²/2) for symmetric data, products under conditional-mean nulls; approximate (1 + ε) and asymptotic e-values [wangFalseDiscoveryRate2021, Sec. 2, Example 1, Sec. 5.2].
- The basic e-variable 1/α on A cannot be improved while the basic p-variable can; permutation e-values valid conditionally on the multiset of scores [vovkConfidenceDiscoveriesEvalues2023, Sec. 2, eq. 38]. E-collections (e_S)_S and the calibrated indicator 1{p ≤ a}/a with a random non-increasing threshold as an e-variable under PRDS [xuBringingClosureFalse2025, Def. 5; goemanUniformImprovementBenjaminiHochberg2026, Thm 5].
- E-values as tests rescaled to [0, 1/α], and utility-optimal e-values characterised by λ dP/dQ ∈ ∂U(ε*) [koningAnytimeValidityFree2026, Sec. 6.1, eq. 8]; dampened e-variables (1 − γ) + γS and max{S, 1}/E[max{S, 1}] [grunwaldEposterior2023, eq. 35].
- E-variables as the polar of the null, the effective null as bipolar, and tests and bounded e-variables interconvertible via φ/sup_P E[φ] and Z/B [larssonCompleteCharacterizationTestable2026, Sec. 3, Cor. 3.7]. Exact, pivotal and nontrivial as separate properties; existence of exact and non-exact nontrivial e-variables by the span and convex hull of the null; translation families of infinitely divisible laws admit no exact nontrivial e-variable [zhangExistencePowerfulPvalues2023, Sec. 1, Thms 3.1, 3.4, 6.1–6.2, Prop. 6.9].
- Full description of the e-variable class for constraint-generated nulls, with explicit forms for finitely many constraints, one-sided sub-ψ laws and compact-group invariance [larssonTestingHypothesesGenerated2025, Thms 2.2, 3.1, 4.3, 5.5]; e-statistics of a null equal those of its convex hulls [lardyReverseInformationProjections2023, Sec. IV-A]. Decision-theoretic foundation as 1/post-hoc-p, with h-valid, harmonic and geometric generalisations [koningPosthocAlphaHypothesis2023, Thm 2, Def. 4]. Infinite values matter [larssonTestingHypothesesGenerated2025, Example 8.2]. Indicator e-values and two-sided e-values (e⁺ ∨ e⁻)/2 [xuPostselectionInferenceEvalue2022, App. B]; an exact e-variable for the Lönnstedt–Speed microarray model [ignatiadisEvaluesUnnormalizedWeights2022, Prop. S7.1]; approximate and asymptotic relaxations [ignatiadisAsymptoticCompoundEvalues2024, Def. 3.1].
- Orbit characterisation of exact e-values for invariance nulls and the fact that any non-exact e-value plugged into T/E_G[T] becomes exact [koningMeasuringEvidenceExchangeability2023, Thms 1, 3, Remark 16]. Knockoff statistics as relaxed e-values with Σ_{H_0} E[e_j] ≤ p [renDerandomizedKnockoffsLeveraging2022, Sec. 2.2]. Complete characterisation of one-observation e-values for an interval null on a Bernoulli parameter [henziValidSequentialInference2021, Thm 3.1]. Backtest e-statistics and their domination results for mean, variance, VaR and ES–VaR [wangEbacktesting2022, Lemmas EC.2–EC.5]. The inequality 1{E ≥ 1/α} ≤ αE as the single engine of online FDR proofs [xuOnlineMultipleTesting2023, eq. 6].

## Variants and related concepts
- [e-process](e-process.md), the sequential object.
- [e-power](e-power.md), how e-variables are compared.
- [e-merging](e-merging.md) and [e-bh](e-bh.md), how several e-values are combined.

## Sources
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — definition, Markov test, likelihood-ratio characterisation for simple nulls, interpretations, history.
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — canonical definition, closure, admissibility, representation theorems, randomised Markov, catalogue.
- [wassermanUniversalInference2020](../sources/wassermanUniversalInference2020.md) — split LRT as an e-variable; averages stay valid.
- [haoEValuesExponentialFamilies2025](../sources/haoEValuesExponentialFamilies2025.md) — four e-variables for exponential family nulls.
- [vovkEvaluesCalibrationCombination2021](../sources/vovkEvaluesCalibrationCombination2021.md) — definition, naming, composite nulls, Appendix D.
- [shaferTestingBettingStrategy2021](../sources/shaferTestingBettingStrategy2021.md) — betting scores, implied alternative.
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md) — unit bets, taxonomy.
- [grunwaldOptimalEValuesExponential2024](../sources/grunwaldOptimalEValuesExponential2024.md) — local vs global e-variables.
- [turnerGenericEvariablesExact2024](../sources/turnerGenericEvariablesExact2024.md), [turnerExactAnytimevalidConfidence2023](../sources/turnerExactAnytimevalidConfidence2023.md), [terschureAnytimevalidLogrankTest2024](../sources/terschureAnytimevalidLogrankTest2024.md) — constructive composite-null e-variables.
- [grunwaldAuthorsReplyDiscussion2024](../sources/grunwaldAuthorsReplyDiscussion2024.md) — robustified and empirical e-variables.
- [larssonNumeraireEvariableReverse2025](../sources/larssonNumeraireEvariableReverse2025.md), [grunwaldBeyondNeymanPearsonEvalues2024](../sources/grunwaldBeyondNeymanPearsonEvalues2024.md), [wangFalseDiscoveryRate2021](../sources/wangFalseDiscoveryRate2021.md), [vovkConfidenceDiscoveriesEvalues2023](../sources/vovkConfidenceDiscoveriesEvalues2023.md), [xuBringingClosureFalse2025](../sources/xuBringingClosureFalse2025.md), [goemanUniformImprovementBenjaminiHochberg2026](../sources/goemanUniformImprovementBenjaminiHochberg2026.md), [koningAnytimeValidityFree2026](../sources/koningAnytimeValidityFree2026.md), [grunwaldEposterior2023](../sources/grunwaldEposterior2023.md) — batch-3 contributions.
- [larssonCompleteCharacterizationTestable2026](../sources/larssonCompleteCharacterizationTestable2026.md), [zhangExistencePowerfulPvalues2023](../sources/zhangExistencePowerfulPvalues2023.md), [larssonTestingHypothesesGenerated2025](../sources/larssonTestingHypothesesGenerated2025.md), [lardyReverseInformationProjections2023](../sources/lardyReverseInformationProjections2023.md), [koningPosthocAlphaHypothesis2023](../sources/koningPosthocAlphaHypothesis2023.md), [xuPostselectionInferenceEvalue2022](../sources/xuPostselectionInferenceEvalue2022.md), [ignatiadisEvaluesUnnormalizedWeights2022](../sources/ignatiadisEvaluesUnnormalizedWeights2022.md), [ignatiadisAsymptoticCompoundEvalues2024](../sources/ignatiadisAsymptoticCompoundEvalues2024.md) — batch-4 contributions.
- [koningMeasuringEvidenceExchangeability2023](../sources/koningMeasuringEvidenceExchangeability2023.md), [renDerandomizedKnockoffsLeveraging2022](../sources/renDerandomizedKnockoffsLeveraging2022.md), [henziValidSequentialInference2021](../sources/henziValidSequentialInference2021.md), [wangEbacktesting2022](../sources/wangEbacktesting2022.md), [xuOnlineMultipleTesting2023](../sources/xuOnlineMultipleTesting2023.md) — batch-4 wave-2 contributions.

## Disagreements / open issues
- Wang's discussion of Safe Testing shows that e-variables with high rejection probability can have e-power minus infinity, so "good e-variable" is not a single ordering [grunwaldSafeTesting2024, discussion].
