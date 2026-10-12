---
slug: asymptotic-confidence-sequences
title: Asymptotic confidence sequences and time-uniform central limit theory
sources: 4
updated: 2026-10-12
---

# Asymptotic confidence sequences and time-uniform central limit theory

## Definition
A (1 − α)-asymptotic confidence sequence for (θ_t) is a sequence of intervals θ̂_t ± (L_t, U_t) for which there exists, possibly on an enriched probability space, a nonasymptotic (1 − α)-confidence sequence θ̂_t ± (L*_t, U*_t) with L*_t/L_t → 1 and U*_t/U_t → 1 almost surely [waudbysmithTimeuniformCentralLimit2021, Def. 2.1]; the multivariate version asks that the normalised symmetric difference vanish [Def. B.6]. Convergence in probability is rejected because time-uniform convergence in probability equals almost-sure convergence, and the naive "lim sup of eventual miscoverage" definition is vacuous [Remark 1, Prop. B.4]. It is the time-uniform analogue of a central-limit interval: finite-sample validity is traded for universality.

## Key results
- The time-uniform CLT is Strassen's strong invariance principle: the centred average is coupled almost surely with a Gaussian walk at rate o(√(log log t / t)), dominated by Robbins' O(√(log t / t)) normal-mixture boundary, so the Gaussian boundary transfers to any finite-variance data with σ̂_t [waudbysmithTimeuniformCentralLimit2021, Lemma A.1, Thm 2.2].
- Abstract recipe: strong approximation, a boundary for the approximating process, rate domination, and almost-sure approximation of the boundary; any Gaussian boundary plugs in, including stitched LIL and delayed-start boundaries [waudbysmithTimeuniformCentralLimit2021, Thm 2.4, Props 2.3, 2.9]; see [confidence-sequence-boundaries](confidence-sequence-boundaries.md).
- Martingale dependence and time-varying means under a diverging-variance condition, a Lindeberg-type condition and a strongly consistent variance estimate, via Strassen 1967; a Lyapunov moment condition suffices for independent non-identical data [waudbysmithTimeuniformCentralLimit2021, Prop. 2.5, Cor. 2.6].
- Sharp asymptotic anytime-valid type-I control: lim inf over the first peeking time m of the time-uniform coverage from m is at least 1 − α, with equality for the tuned mixture; the delayed-start corollary coincides with the rmlSPRT of Bibaut, Kallus and Lindon [waudbysmithTimeuniformCentralLimit2021, Def. 2.7, Thm 2.8, Claims B.1–B.2].
- Causal inference: cross-fit AIPW with sequential sample splitting gives asymptotic sequences for the average treatment effect in randomised experiments with misspecified regressions and in observational studies under a product nuisance rate, plus a delta method; widths are sharp by admissibility of Robbins' mixture, unimprovable couplings and the semiparametric efficiency bound [waudbysmithTimeuniformCentralLimit2021, Thms 3.1–3.3, Cor. 3.4, App. B.9].
- The scale-invariant t-test sequence has an asymptotic version over L² [wangAnytimevalidTtestsConfidence2023, Thm 4.12]; the asymptotic sequence is the input to e-BY in the Twitter A/B application [xuPostselectionInferenceEvalue2022, Sec. 7].
- Elsewhere in the wiki this paper is named as the route to "approximate optional stopping" for e-variables that are not e-processes; it supplies confidence sequences and limiting type-I control, not e-processes, so that conjecture stays open [haoEValuesExponentialFamilies2025, Sec. 7; terschureAnytimevalidLogrankTest2024, Sec. 4].

## Variants and related concepts
- [confidence-sets-and-sequences](confidence-sets-and-sequences.md), [optional-stopping](optional-stopping.md).

## Sources
- [waudbysmithTimeuniformCentralLimit2021](../sources/waudbysmithTimeuniformCentralLimit2021.md) — primary source.
- [wangAnytimevalidTtestsConfidence2023](../sources/wangAnytimevalidTtestsConfidence2023.md), [xuPostselectionInferenceEvalue2022](../sources/xuPostselectionInferenceEvalue2022.md) — uses.
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md) — survey mention of asymptotic sequences.

## Disagreements / open issues
- The survey reports the symmetric-difference definition (Def. B.6) rather than the main ratio definition [ramdasGametheoreticStatisticsSafe2023, Sec. 5.8].
