---
slug: testability-and-existence
title: Testability, existence of powerful e-values, and complete classes
sources: 6
updated: 2026-10-12
---

# Testability, existence of powerful e-values, and complete classes

## Definition
When does a nontrivial test, or a powered [e-variable](e-variable.md), exist between two sets of distributions at all? Kraft and Le Cam answered under a common dominating measure: the minimax risk is 1 − d_TV(co(P), co(Q)). Without any assumption, the risk is 1 − d_TV(co*(P), co*(Q)) where co* is the weak-∗ closure of the convex hull in the space ba of bounded finitely additive measures; the infimum is attained in the closures and finitely additive measures are unavoidable [larssonCompleteCharacterizationTestable2026, Thms 1.1, 1.5, Example 3.5]. A bounded e-variable uniformly powered against a composite alternative exists iff d_TV(co*(P), co*(Q)) > 0 [Cor. 3.7]. For finite nulls and convex-polytope alternatives, exact powered e-variables exist iff Span P ∩ Conv Q = ∅ and merely valid ones iff Conv P ∩ Conv Q = ∅ [zhangExistencePowerfulPvalues2023, Thms 3.1, 3.4, 6.1–6.2].

## Key results
- The effective null of the numeraire theory equals co*(P) on probability measures, and is the solid hull of the countably additive parts of co*(P); the TV-quantitative theorem cannot use the effective null even for a point alternative [larssonCompleteCharacterizationTestable2026, Thms 3.3–3.4, Example 3.5]; see [numeraire](numeraire.md).
- Le Cam's generalised tests keep the TV closure but may depend on the generating law rather than the sample; his remark sketched the right approach without a theorem [larssonCompleteCharacterizationTestable2026, Thm 1.12, App. B]. Published misuses of minimax theorems are flagged [App. A].
- Simultaneous optimal transport: a map collapsing every null law to one measure is exactly a filtration coarsening; existence of exact e-variables reduces to convex-order dominance of the Radon–Nikodym vector; log-optimality under exactness and pivotality is still a likelihood ratio, computable by the SHINE separating-hyperplane iteration with exponential convergence for two null points; batching always suffices for finite nulls on Euclidean spaces [zhangExistencePowerfulPvalues2023, Props 2.3, 3.3, Thms 4.2, 4.4, 4.9, 5.3, 5.5].
- Nontrivial e-power and nontrivial mean coincide for finite alternatives by shrinking but differ for infinite ones; maximal pivotal exact e-power is superadditive over batches with a positive limit at most the minimal KL [zhangExistencePowerfulPvalues2023, Prop. A.2, Example A.4, Prop. 4.11].
- Constraint-generated nulls {μ : ∫f dμ ≤ 0, f ∈ Φ}: every e-variable is 1 + f with f in the weak closure of cone(Φ) minus nonnegative functions; with finitely many constraints the admissible e-variables are exactly 1 + Σπ_i g_i (mean with bounded sd, quantile, bounded mean, where the betting e-variables are all the admissible ones); one-sided sub-ψ nulls have exactly the mixtures ∫e^{λx − ψ(λ)} π(dλ); compact-group invariance gives 1 + f − f_π with Haar orbit averages; unions handle CVaR [larssonTestingHypothesesGenerated2025, Thms 2.2, 3.1, 4.3, 5.5, Cor. 3.3, Lemma 8.1].
- Complete classes: minimal complete classes of e-variables need not exist but do with a reference measure and for the three families above; optimal e-variables exist for any objective inf_Q ∫U(h)dQ − χ(Q) with U nondecreasing, usc and linearly bounded, which covers GRO, GROW, REGROW and power utilities [larssonTestingHypothesesGenerated2025, Thms 6.3, 6.5, 7.3, 7.4, 7.6, Example 7.1].
- Admissibility of anytime-valid instruments: admissible e-processes are essential infima of pointwise nonnegative martingales; admissible p-processes are closed max-martingales; a confidence sequence is admissible iff its inverted tests are; admissibility is neither subset- nor superset-proof [ramdasAdmissibleAnytimevalidSequential2022, Thm 18, Cors 24, 26, Thm 30, Example 37]; see [e-process](e-process.md).
- Admissible e-merging functions are exactly weighted arithmetic means [wangOnlyAdmissibleWay2024, Thm 1]; see [e-merging](e-merging.md).

## Variants and related concepts
- [numeraire](numeraire.md), [e-power](e-power.md), [gro-criterion](gro-criterion.md), [optional-stopping](optional-stopping.md) (filtration coarsening).

## Sources
- [larssonCompleteCharacterizationTestable2026](../sources/larssonCompleteCharacterizationTestable2026.md) — testability without assumptions.
- [zhangExistencePowerfulPvalues2023](../sources/zhangExistencePowerfulPvalues2023.md) — existence for finite nulls, simultaneous transport.
- [larssonTestingHypothesesGenerated2025](../sources/larssonTestingHypothesesGenerated2025.md) — constraint-generated nulls, complete classes, optimality.
- [ramdasAdmissibleAnytimevalidSequential2022](../sources/ramdasAdmissibleAnytimevalidSequential2022.md) — admissibility of sequential instruments.
- [wangOnlyAdmissibleWay2024](../sources/wangOnlyAdmissibleWay2024.md) — admissible merging.
- [larssonNumeraireEvariableReverse2025](../sources/larssonNumeraireEvariableReverse2025.md) — effective null.

## Disagreements / open issues
- Whether the batch e-power limit equals the minimal KL in general is open [zhangExistencePowerfulPvalues2023, Prop. 4.11].
- Sequential characterisation of admissible e-processes for constraint-generated nulls is open; Clerico 2025 settles the bounded-conditional-mean case [larssonTestingHypothesesGenerated2025, Sec. 10].
- Klein and Köstenberger 2026 propose pre-Hahn localizable hypotheses as a way to avoid finitely additive measures [larssonCompleteCharacterizationTestable2026, Sec. 1].
