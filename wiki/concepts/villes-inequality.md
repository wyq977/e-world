---
slug: villes-inequality
title: Ville's inequality
sources: 26
updated: 2026-10-13
---

# Ville's inequality

## Definition
For a nonnegative supermartingale (M_t) with M_0 ≤ 1 under P, P(∃t : M_t ≥ 1/α) ≤ α; equivalently P(M_τ ≥ 1/α) ≤ α at every stopping time τ [ramdasHypothesisTestingEvalues2025, Fact 7.6]. It is the time-uniform Markov inequality and the single tool that upgrades a fixed-sample e-value test into an anytime-valid one [wassermanUniversalInference2020, Thm 9; grunwaldSafeTesting2024, Cor. 1]. Grünwald, de Heide and Koolen call the resulting continuation guarantee "Ville–Robbins" and trace it to Ville 1939, Robbins and Lai [grunwaldSafeTesting2024, Sec. 7].

## Key results
- Three equivalent forms, including a conditional version, and the SPRT thresholds γ_0 = β, γ_1 = 1/α as a corollary [ramdasHypothesisTestingEvalues2025, Sec. 7.2].
- Defines safety under optional continuation and optional stopping [grunwaldSafeTesting2024, Sec. 5]; see [optional-continuation](optional-continuation.md), [optional-stopping](optional-stopping.md).
- Gives anytime p-values and confidence sequences from an e-process [wassermanUniversalInference2020, Thms 10–11]; see [confidence-sets-and-sequences](confidence-sets-and-sequences.md).
- Tightness and the necessity of nonnegative martingales for admissible anytime-valid inference are cited to Ramdas, Ruf, Larsson and Koolen 2020 [ramdasHypothesisTestingEvalues2025, Chapter 7 note].
- The original: Chapter V Theorem 1, inequality (15), Pr{sup_n s_n ≥ λ} ≤ 1/λ for a nonnegative martingale with s_0 = 1, proved by freezing the martingale at first passage; an earlier instance of the stopped-process argument is in Chapter II; the continuous-time version can fail without path regularity [villeEtudeCritiqueNotion1939, Ch. V, p. 84, p. 98].
- Ville's theorem (P(A) < ε iff some test martingale exceeds 1/ε on A), its composite version requiring e-processes, equality for continuous paths, overshoot as the discrete-time looseness, and the extension to nonintegrable supermartingales [ramdasGametheoreticStatisticsSafe2023, Sec. 2.5, eqs 8–10].
- Applied to exponential supermartingales it yields only linear boundaries; curved boundaries need mixtures or a union bound over epochs [howardTimeuniformNonparametricNonasymptotic2021, Lemmas 1–2, Thm 1]; see [confidence-sequence-boundaries](confidence-sequence-boundaries.md).
- Used to sharpen the sequential-e-value-to-p merger to the running minimum [vovkEvaluesCalibrationCombination2021, App. G]; the single safety guarantee in the k-sample, contingency-table and logrank papers [turnerGenericEvariablesExact2024, eq. 2.4; turnerExactAnytimevalidConfidence2023, Sec. 3; terschureAnytimevalidLogrankTest2024, Prop. 3.1].
- Generalisation to monotone floors and thresholds: for a supermartingale with M_n ≥ −f(n) and non-decreasing f, g, P{∃n : M_n ≥ g(n)} ≤ 1 − ((g(0) − E M_0)/(g(0) + f(0))) ∏_{n ≥ 1} (g(n) + f(n − 1))/(g(n) + f(n)); tight, attained by the floor-hugger martingale; proved by applying classic Ville to a look-ahead supermartingale, so it is a corollary, not a strengthening; continuous relaxation via ∫ f′/(g + f); yields a finite-time law of the iterated logarithm with explicit constants [koolenGeneralisationVilleInequality2025, Thm 2.1, Lemma 2.2, Cor. 3.1, Lemma 4.1].
- Three equivalent forms plus a conditional version; anti-concentration converse sup_Q Q(sup M_t ≥ 1/α) = α under infinite aggregate variance; tightness does not imply admissibility [ramdasAdmissibleAnytimevalidSequential2022, Sec. 3.1, Lemma 33, Cor. 34, Example 50].
- Replaced by a direct expectation bound for bounded martingales in test induction [koningAnytimeValidityFree2026, Thm 5]; the ARL analogue E N* ≥ E M_{N*} ≥ (1/α) P(N* < ∞) for e-detectors [shinEdetectorsNonparametricFramework2023, Thm 2.4]; p-values from running maxima of e-processes [wangFalseDiscoveryRate2021, Sec. 7].
- Ville's theorem in composite form: ν(A) = 0 iff a P-e-process explodes on A; 1/ν(A) is the maximal attainable wealth on A and ν(A) the cheapest initial capital super-replicating 1_A; the theorem is false with sup_P P(A) in place of ν; a new L¹ Dubins–Savage line-crossing inequality needing only a first moment; the composite strong law as ν(A_div) = 0 [rufCompositeGeneralizationVille2022, Thms 3.1, 3.7, 4.1, 4.3, Cor. 3.10, Lemma 3.11, Remark 3.3, Prop. 2.6]. Ville used on the Jeffreys-mixture martingale gives the Bernoulli confidence sequence, and the exchangeability e-process is a constructive witness to a composite Ville theorem [ramdasTestingExchangeabilityForkconvexity2021, Secs 4.6, 5.4].
- Markov's equality sup_c 1{X ≥ 1/c}/c = X and Ville's equalities for martingales, supermartingales and exact e-processes once α may depend on the data [koningPosthocAlphaHypothesis2023, Lemma 2, Props 10–11]. Extended Ville inequality for nonintegrable supermartingales applied to Lai's process [wangAnytimevalidTtestsConfidence2023, Lemma 2.2, Thm 4.7]. 'Nearly an equality' for nonnegative martingales, the only tool in the betting construction [waudbysmithEstimatingMeansBounded2020, Thm 1, App. E.2]; the only tool in asymptotic sequences, almost an equality for continuous paths [waudbysmithTimeuniformCentralLimit2021, App. A.1, B.9].
- Regularized Ville inequality over a credal set of priors [martinRegularizedEprocessesAnytime2024, Thm 1]. An adapted nonnegative process bounded by c with E[W_τ] ≤ 1 at all stopping times has E[sup_t W_t] ≤ 1 + log c, converting StopFDR to SupFDR at cost 1 + log(1/α) [fischerOnlineGeneralizationEBH2024, Thm G.3]. Always-valid FWER by Ville applied to e_{H_0,t} and running maxima as pseudo e-values with Pareto(1) tail coupling [hartogFamilyWiseError2025, Thm 2.5, Thm 3.1]. PFA bounds for multi-stream detectors [dandapanthulaMultipleTestingMultistream2025, Thms 4.4, 5.5].
- The thesis that Robbins 1970 already combined Ville and likelihood ratios for anytime-valid confidence sequences, everything since being a choice of martingale [kirschnerConfidenceEstimationSequential2025, Lemma 1, App. A].

## Variants and related concepts
- [e-process](e-process.md), [test-martingale](test-martingale.md).

## Sources
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — statement, forms, SPRT corollary, p-processes.
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — Ville–Robbins, safety definitions, history.
- [wassermanUniversalInference2020](../sources/wassermanUniversalInference2020.md) — use for the sequential split LRT.
- [villeEtudeCritiqueNotion1939](../sources/villeEtudeCritiqueNotion1939.md) — original statement and proof.
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md) — Ville's theorem and composite forms.
- [howardTimeuniformNonparametricNonasymptotic2021](../sources/howardTimeuniformNonparametricNonasymptotic2021.md) — boundaries from Ville.
- [vovkEvaluesCalibrationCombination2021](../sources/vovkEvaluesCalibrationCombination2021.md), [turnerGenericEvariablesExact2024](../sources/turnerGenericEvariablesExact2024.md), [turnerExactAnytimevalidConfidence2023](../sources/turnerExactAnytimevalidConfidence2023.md), [terschureAnytimevalidLogrankTest2024](../sources/terschureAnytimevalidLogrankTest2024.md) — applications.
- [koolenGeneralisationVilleInequality2025](../sources/koolenGeneralisationVilleInequality2025.md) — generalised Ville.
- [ramdasAdmissibleAnytimevalidSequential2022](../sources/ramdasAdmissibleAnytimevalidSequential2022.md), [koningAnytimeValidityFree2026](../sources/koningAnytimeValidityFree2026.md), [shinEdetectorsNonparametricFramework2023](../sources/shinEdetectorsNonparametricFramework2023.md), [wangFalseDiscoveryRate2021](../sources/wangFalseDiscoveryRate2021.md) — forms and analogues.
- [rufCompositeGeneralizationVille2022](../sources/rufCompositeGeneralizationVille2022.md) — composite Ville theorem.
- [ramdasTestingExchangeabilityForkconvexity2021](../sources/ramdasTestingExchangeabilityForkconvexity2021.md), [koningPosthocAlphaHypothesis2023](../sources/koningPosthocAlphaHypothesis2023.md), [wangAnytimevalidTtestsConfidence2023](../sources/wangAnytimevalidTtestsConfidence2023.md), [waudbysmithEstimatingMeansBounded2020](../sources/waudbysmithEstimatingMeansBounded2020.md), [waudbysmithTimeuniformCentralLimit2021](../sources/waudbysmithTimeuniformCentralLimit2021.md) — uses and equalities.
- [martinRegularizedEprocessesAnytime2024](../sources/martinRegularizedEprocessesAnytime2024.md), [fischerOnlineGeneralizationEBH2024](../sources/fischerOnlineGeneralizationEBH2024.md), [hartogFamilyWiseError2025](../sources/hartogFamilyWiseError2025.md), [dandapanthulaMultipleTestingMultistream2025](../sources/dandapanthulaMultipleTestingMultistream2025.md) — batch-4 wave-2 contributions.
- [kirschnerConfidenceEstimationSequential2025](../sources/kirschnerConfidenceEstimationSequential2025.md) — Robbins thesis.

## Disagreements / open issues
- None recorded.
