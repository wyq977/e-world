---
slug: information-projection
title: Information projection (I-projection) and its generalised form
sources: 4
updated: 2026-11-16
---

# Information projection (I-projection) and its generalised form

## Definition
The I-projection of a distribution R on a convex set ℰ of distributions is the element Q ∈ ℰ minimising the Kullback–Leibler divergence D(P ‖ R) over P ∈ ℰ; the reference R sits in the second argument and the minimisation is over the first [csiszarIDivergenceGeometryProbability1975, eq. 1.5]. It is unique when it exists, by strict convexity. When ℰ is not closed the minimum may not be attained, but every sequence in ℰ whose divergence tends to the infimum converges in variation to one distribution P*, which need not belong to ℰ: the generalized I-projection, called the relative center of attraction by Topsøe [csiszarSanovPropertyGeneralized1984, Sec. 1; topsoeInformationtheoreticalOptimizationTechniques1979, Thm 8]. This is the "forward" projection; the [reverse information projection](reverse-information-projection.md) minimises over the second argument instead.

## Key results
- Existence: if ℰ is convex and closed in variation distance and contains some P with D(P ‖ R) < ∞, the I-projection exists; the proof uses a parallelogram-type identity and Pinsker's inequality, and closedness only to put the limit in ℰ [csiszarIDivergenceGeometryProbability1975, Thm 2.1 and Remark].
- Pythagorean inequality: Q ∈ ℰ is the I-projection iff D(P ‖ R) ≥ D(P ‖ Q) + D(Q ‖ R) for every P ∈ ℰ, equivalently iff ∫ log(dQ/dR) dP ≥ D(Q ‖ R) (a tangent-hyperplane condition on the KL ball around R); equality holds throughout when Q is an algebraic inner point of ℰ [csiszarIDivergenceGeometryProbability1975, Lemma 2.1, Thm 2.2].
- The same inequality without closedness: for any convex ℰ with finite infimum, D(P ‖ R) ≥ inf_ℰ D(· ‖ R) + D(P ‖ P*) for every P ∈ ℰ, with P* the generalized I-projection, and this inequality characterises P* [topsoeInformationtheoreticalOptimizationTechniques1979, Thm 8, eq. 17; csiszarSanovPropertyGeneralized1984, eq. 1.5]. Hence minimising sequences converge to P* in information, D(P_n ‖ P*) → 0, which is stronger than convergence in variation [csiszarSanovPropertyGeneralized1984, Sec. 1].
- The generalized projection can undershoot: D(P* ‖ R) ≤ inf_ℰ D(· ‖ R) always, with strict inequality possible, and it cannot in general be obtained as an ordinary I-projection on some closure of ℰ [csiszarSanovPropertyGeneralized1984, eq. 1.6, Examples 3.1–3.2]. A discrete instance: with mean-energy constraints above a critical value the center of attraction is a fixed exponential-family member whose mean energy and entropy are both below the constraint values [topsoeInformationtheoreticalOptimizationTechniques1979, Thm 11(d)].
- Minimax reading: in the game where nature picks μ ∈ ℰ and the observer picks a code improvement relative to R, the value is inf_ℰ D(· ‖ R) and the observer's unique optimal strategy is the one adapted to P*; proved assuming D(μ ‖ R) < ∞ for every μ ∈ ℰ, with the weaker assumption of a finite infimum left as "probably" sufficient [topsoeInformationtheoreticalOptimizationTechniques1979, Thm 9].
- Linear constraints give exponential families: under finitely many moment constraints, or prescribed marginals, the I-projection has density c·exp(Σ t_i f_i) resp. a(x_1)b(x_2) relative to R, necessarily and sufficiently up to a null set; it exists at interior points of the attainable moment set when the natural parameter set is open, and the gradient of the minimal divergence in the constraint values is the canonical parameter [csiszarIDivergenceGeometryProbability1975, Cor. 3.1, Thm 3.3]. For inequality constraints and for "mean in a convex set C" the generalized I-projection is again an exponential-family member, with the dual formula D = max_ϑ [inf_{v ∈ C} ϑ(v) − log ∫ exp ϑ dQ] [csiszarSanovPropertyGeneralized1984, Thms 2–3].
- With infinitely many linear constraints the Pythagorean identity can fail (only the inequality holds), and neither the necessary nor the sufficient exponential-form condition is both [csiszarIDivergenceGeometryProbability1975, Thm 3.1 and Example].
- Large deviations and conditioning: for almost completely convex Π, (1/n) log Pr{P̂_n ∈ Π} ≤ −D(Π ‖ P_X) for every n, and given P̂_n ∈ Π the observations are asymptotically quasi-independent with limiting law the generalized I-projection [csiszarSanovPropertyGeneralized1984, Thm 1].
- Link to e-values: for a simple null P_0 and an alternative H_1, a P*_1 satisfying the Pythagorean property over H_1 makes p*_1/p_0 the GROW e-variable, with no convexity of H_1 or attainment of the infimum needed; for convex mean-defined alternatives P*_1 is the exponential-family member at the KL-closest mean [grunwaldGrowthOptimalEVariablesExtension2024a, Prop. 1, Prop. 2]. Wiki's reading: Topsøe's code improvement is the logarithm of an e-variable against P_0 and the value of his relative game is GROW.

## Variants and related concepts
- [reverse-information-projection](reverse-information-projection.md): projection in the other argument, onto the null; the two play the same role only for a simple null.
- [gro-criterion](gro-criterion.md), [exponential-family-e-values](exponential-family-e-values.md), [mdl-and-maximum-entropy-e-values](mdl-and-maximum-entropy-e-values.md).

## Sources
- [csiszarIDivergenceGeometryProbability1975](../sources/csiszarIDivergenceGeometryProbability1975.md) — definition, existence, Pythagorean characterisation, linear constraints.
- [topsoeInformationtheoreticalOptimizationTechniques1979](../sources/topsoeInformationtheoreticalOptimizationTechniques1979.md) — center of attraction without closedness, game-theoretic value.
- [csiszarSanovPropertyGeneralized1984](../sources/csiszarSanovPropertyGeneralized1984.md) — generalized I-projection, strictness examples, large deviations, conditional limit theorem.
- [grunwaldGrowthOptimalEVariablesExtension2024a](../sources/grunwaldGrowthOptimalEVariablesExtension2024a.md) — the projection as the numerator of the GROW e-variable for a simple null.

## Disagreements / open issues
- Every theorem in the three classical sources is for convex sets. For a non-convex alternative such as the complement of a KL ball, the wiki has only the CSC paper's Proposition 1 (which assumes the Pythagorean property rather than deriving it) and its one-dimensional Theorem 3 [grunwaldGrowthOptimalEVariablesExtension2024a].
- Whether Topsøe's Theorem 9 holds assuming only a finite infimum is left open in that paper [topsoeInformationtheoreticalOptimizationTechniques1979]; the CSC paper's Proposition 1 is described there as weakening it for the simple-null case [grunwaldGrowthOptimalEVariablesExtension2024a, Sec. 1.2].
- Attribution: the Pythagorean inequality for a projection outside the set is Topsøe's Theorem 8, not Csiszár 1975, which proves it only for a projection inside the set; Csiszár 1984 states this division explicitly.
