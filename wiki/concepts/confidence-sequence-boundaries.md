---
slug: confidence-sequence-boundaries
title: Confidence sequence boundaries and sub-ψ supermartingales
sources: 3
updated: 2026-10-08
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

## Variants and related concepts
- [confidence-sets-and-sequences](confidence-sets-and-sequences.md), the object these boundaries produce.
- [mixture-and-plug-in-methods](mixture-and-plug-in-methods.md), [e-process](e-process.md).

## Sources
- [howardTimeuniformNonparametricNonasymptotic2021](../sources/howardTimeuniformNonparametricNonasymptotic2021.md) — the taxonomy, rates, tuning, applications.
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md) — compendium of exponential supermartingales and nonparametric sequences.
- [villeEtudeCritiqueNotion1939](../sources/villeEtudeCritiqueNotion1939.md) — the earliest mixture boundaries.

## Disagreements / open issues
- Howard et al. 2020, "Time-uniform Chernoff bounds via nonnegative supermartingales", defines the sub-ψ condition and is not in the bib; see gaps.
