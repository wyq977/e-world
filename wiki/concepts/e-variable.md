---
slug: e-variable
title: E-variable
sources: 11
updated: 2026-10-08
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

## Disagreements / open issues
- Wang's discussion of Safe Testing shows that e-variables with high rejection probability can have e-power minus infinity, so "good e-variable" is not a single ordering [grunwaldSafeTesting2024, discussion].
