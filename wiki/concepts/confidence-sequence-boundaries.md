---
slug: confidence-sequence-boundaries
title: Confidence sequence boundaries and sub-ψ supermartingales
sources: 13
updated: 2026-10-12
---

# Confidence sequence boundaries and sub-ψ supermartingales

## Definition
A sub-ψ process is a pair (S_t, V_t) such that exp{λS_t − ψ(λ)V_t} is dominated by a nonnegative supermartingale for each λ in a range, with ψ the log-MGF of a reference law (Gaussian λ²/2, Bernoulli, Poisson, exponential, sub-gamma) [howardTimeuniformNonparametricNonasymptotic2021, Def. 1, Prop. 11]. A sub-ψ uniform boundary is a function u with P(∃t : S_t ≥ u(V_t)) ≤ α for every such pair; a confidence sequence for a mean is then X̄_t ± u(V_t)/t, so the boundary's shape governs how fast the sequence shrinks [Def. 2]. The exponential supermartingales exp(λ·sum − ψ(λ)·variance) are the nonparametric counterpart of likelihood ratios and the building block of most nonparametric [test martingales](test-martingale.md) [ramdasGametheoreticStatisticsSafe2023, Sec. 5.1, 5.9.1].

## Key results
- One application of [Ville's inequality](villes-inequality.md) gives only linear boundaries whose confidence radius never shrinks [howardTimeuniformNonparametricNonasymptotic2021, Lemma 1].
- Four curved-boundary recipes: stitching over geometric epochs with explicit LIL-rate constants (Thm 1), conjugate mixtures with one- and two-sided normal, beta-binomial, gamma-Poisson and gamma-exponential forms (Lemma 2, Props 5–10), discrete mixtures (Thm 2), and inverted stitching for finite horizons (Thm 3) [howardTimeuniformNonparametricNonasymptotic2021].
- Rates: continuous mixtures grow as √(v log v) (Prop. 2), stitching and discrete mixtures reach √(v log log v); in practice the log v rate is tighter over several orders of magnitude, tuned via Lambert W (Prop. 3); sub-Gaussian mixture boundaries are unimprovable (Prop. 4) [howardTimeuniformNonparametricNonasymptotic2021, Sec. 3.5].
- Empirical-Bernstein confidence sequence for bounded observations with predictable centring, proved by a self-normalised supermartingale; application to sequential average-treatment-effect estimation under adaptive randomisation [howardTimeuniformNonparametricNonasymptotic2021, Thm 4, Cor. 2].
- Matrix, Banach-space and continuous-time extensions, including a matrix finite LIL and operator-norm covariance sequences [howardTimeuniformNonparametricNonasymptotic2021, Cors 3–8].
- For one-parameter exponential families, mixture boundaries are exactly Robbins' mixture SPRT, and stitching is an approximate discrete mixture [howardTimeuniformNonparametricNonasymptotic2021, Cor. 6, App. A.6].
- Catalogue in the survey: sub-Gaussian mixture sequence (eq. 22), Catoni heavy-tailed, empirical-Bernstein (eq. 23), betting martingale for bounded means (eq. 24), symmetry via self-normalisation (eq. 25), reverse-submartingale and asymptotic sequences [ramdasGametheoreticStatisticsSafe2023, Sec. 5].
- Ville's own exponential mixture ∫ e^{λx − λ²t/2} dF(λ) reproves Petrowsky's upper-class test for Brownian motion, the first sub-Gaussian mixture boundary; for Bernoulli data every martingale is a Beta-type mixture [villeEtudeCritiqueNotion1939, Ch. V §3, §7].
- Third route to iterated-logarithm boundaries: an improper mixture e^{−η²/2}dη/|η| over the sub-Gaussian exponential supermartingale, bounded below by −ln(1 + n)/√(2π), combined with the generalised Ville inequality gives a finite-time LIL at rate √(2 ln(ln n/δ)) with explicit lower-order terms for δ ≤ 3/5; thresholds must grow super-linearly in the floor [koolenGeneralisationVilleInequality2025, Lemma 4.1, Example 3.3].
- Sub-Gaussian trichotomy for nulls μ_t = 0, μ_t ≤ 0, Σμ_i ≤ 0 and admissibility of exp(ΣX_i − t/2) for all conditionally 1-sub-Gaussian laws, yet inadmissibility for an intermediate class [ramdasAdmissibleAnytimevalidSequential2022, Sec. 5, Thm 35, Example 37].
- Boundary technology transferred to change detection: geometric grids, zeta weights and stitching-style boundary functions for mixture e-detectors [shinEdetectorsNonparametricFramework2023, Def. 4.1, eqs 53, 59–61]; restarted Gaussian-mixture supermartingale [sahaNonpartitionedEdetectorsNonparametric2026, eq. 6].
- Predictable plug-ins as a device alongside mixtures and stitching, with closed-form Hoeffding and empirical-Bernstein boundaries and rate table; a zeta-weighted discrete-mixture betting process attains the LIL rate by dominating a stitched boundary [waudbysmithEstimatingMeansBounded2020, Prop. 1, Thm 2, Table 1, Prop. 7]. Robbins' normal mixture in closed form, delayed-start and folded-Gaussian one-sided boundaries, Lambert-W tuning, and the fact that any Gaussian boundary becomes an asymptotic-sequence boundary through strong approximation [waudbysmithTimeuniformCentralLimit2021, App. A.1, B.1, B.2, Sec. 2.6, Thm 2.4]; see [asymptotic-confidence-sequences](asymptotic-confidence-sequences.md). Normal-mixture and one-sided closed-form supermartingales as explosion witnesses for the composite Ville theorem [rufCompositeGeneralizationVille2022, Sec. 3.2]. Stitched variance and median sequences restated with their large constants [wangAnytimevalidTtestsConfidence2023, App. A].
- Converting any c√((log log t + log(1/α))/t) boundary into a detection-delay sample size O(c²(log log(c/Δ) + log(1/α))/Δ²), and the empirical-Bernstein width in terms of the true post-change variance [shekharSequentialChangeDetection2023, Props 29–30]. Sub-exponential supermartingale with predictable bounds, closed-form gamma-exponential mixture with the bound ≤ 1 when the data support the null, explicit stitched sequence [choeComparingSequentialForecasters2021, Prop. 1, Prop. 3, eq. 53].

## Variants and related concepts
- [confidence-sets-and-sequences](confidence-sets-and-sequences.md), the object these boundaries produce.
- [mixture-and-plug-in-methods](mixture-and-plug-in-methods.md), [e-process](e-process.md).

## Sources
- [howardTimeuniformNonparametricNonasymptotic2021](../sources/howardTimeuniformNonparametricNonasymptotic2021.md) — the taxonomy, rates, tuning, applications.
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md) — compendium of exponential supermartingales and nonparametric sequences.
- [villeEtudeCritiqueNotion1939](../sources/villeEtudeCritiqueNotion1939.md) — the earliest mixture boundaries.
- [koolenGeneralisationVilleInequality2025](../sources/koolenGeneralisationVilleInequality2025.md) — improper mixtures and finite-time LIL.
- [ramdasAdmissibleAnytimevalidSequential2022](../sources/ramdasAdmissibleAnytimevalidSequential2022.md), [shinEdetectorsNonparametricFramework2023](../sources/shinEdetectorsNonparametricFramework2023.md), [sahaNonpartitionedEdetectorsNonparametric2026](../sources/sahaNonpartitionedEdetectorsNonparametric2026.md) — admissibility, change detection.
- [waudbysmithEstimatingMeansBounded2020](../sources/waudbysmithEstimatingMeansBounded2020.md), [waudbysmithTimeuniformCentralLimit2021](../sources/waudbysmithTimeuniformCentralLimit2021.md), [rufCompositeGeneralizationVille2022](../sources/rufCompositeGeneralizationVille2022.md), [wangAnytimevalidTtestsConfidence2023](../sources/wangAnytimevalidTtestsConfidence2023.md) — batch-4 contributions.
- [shekharSequentialChangeDetection2023](../sources/shekharSequentialChangeDetection2023.md), [choeComparingSequentialForecasters2021](../sources/choeComparingSequentialForecasters2021.md) — batch-4 wave-2 contributions.

## Disagreements / open issues
- Howard et al. 2020, "Time-uniform Chernoff bounds via nonnegative supermartingales", defines the sub-ψ condition and is not in the bib; see gaps.
