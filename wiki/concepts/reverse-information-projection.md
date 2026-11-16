---
slug: reverse-information-projection
title: Reverse information projection (RIPr)
sources: 25
updated: 2026-10-19
---

# Reverse information projection (RIPr)

## Definition
The reverse information projection of an alternative Q onto a convex set of null distributions is the element P*_0 minimising D(Q ‖ P) over the convex hull (Bayes marginals) of the null; it may be a sub-probability measure and may lie outside the null [grunwaldSafeTesting2024, Thm 1, App. A.1]. The GRO e-variable is q/p*_0 [grunwaldSafeTesting2024, Cor. 2]. In the assumption-free version it is defined through the [numeraire](numeraire.md): dP*/dQ = 1/E*, living in the bipolar P°° of the null, and for finite nulls it is the KL-closest convex combination [ramdasHypothesisTestingEvalues2025, Definition 6.7, Props 6.6, 6.11]. The underlying lemmas come from Li's 1999 Yale thesis [grunwaldSafeTesting2024, App. A.1; wassermanUniversalInference2020, Sec. 6].

## Key results
- Strong duality and characterisations [ramdasHypothesisTestingEvalues2025, Thms 6.13, 6.14].
- The defining inequality E_Q[p_θ / p*] ≤ 1 for all θ, with the KKT heuristic [wassermanUniversalInference2020, eq. 16, Sec. 6].
- Under misspecification in convex model classes the universal confidence set covers the RIPr of the truth, and a RIPr split LRT dominates the plain split LRT when the RIPr lies in the null [wassermanUniversalInference2020, Props 7–8].
- Explicit nondegenerate RIPrs: for Gaussian location in the anti-simple case the RIPr prior is exactly N(μ*, (Σ_q − Σ_p)/n), and in general exponential families it is approximately Gaussian with O(1/n) variance; the RIPr of a Bayes mixture Q_{W_1} is approximately P_{W_1} with the same prior [haoEValuesExponentialFamilies2025, Thms 1.4, 2.4, 3.4, 4.4, Lemma 2].
- For the 2×2 contingency table with a point alternative the RIPr is a point mass at the pooled rate [grunwaldSafeTesting2024, Example 2, eq. 14]; finite support follows from Carathéodory [App. A.3].
- Local RIPr used by the sequential plug-in e-variable [haoEValuesExponentialFamilies2025, eq. 1.3]; see [exponential-family-e-values](exponential-family-e-values.md).
- Regularity-free extensions via description gain (Lardy, Grünwald, Harremoës) and the numeraire [grunwaldSafeTesting2024, reply Sec. 2].
- Sequential RIPr: the implied target under optional stopping equals inf KL(Q^σ ‖ mixture of stopped nulls), mixing jointly over null elements and stopping times; a flow parametrisation makes the dual a concave programme [koolenLogoptimalAnytimevalidEvalues2022, Thm 5, Prop. 6]. When the one-outcome RIPr of an i.i.d. alternative lies in the null, the log-optimal e-process is the likelihood ratio for every stopping rule, e.g. N(0, ρ²+μ²) for the Gaussian scale null, the pooled rate for 2 × 2 tables, the boundary point for exponential-family intervals [koolenLogoptimalAnytimevalidEvalues2022, Thm 12, Sec. 4.4].
- A checkable condition for the RIPr to be degenerate, equal to the KL projection onto the null family itself: the covariance ordering Σ_p − Σ_q ⪰ 0 on the alternative's mean space; exponential families are nonconvex except Bernoulli/multinomial, which is why RIPr computation is hard in general [grunwaldOptimalEValuesExponential2024, eqs 1.4–1.7, Thm 1, Sec. 1.3].
- For convex nulls Θ_0 ⊂ [0,1]² in the 2 × 2 table the RIPr of a point alternative is a point mass at the unique block-KL minimiser, on the boundary of Θ_0; closed-form stationarity for linear boundaries [turnerExactAnytimevalidConfidence2023, Thm 2, eq. 11]; in the generic k-sample construction the per-outcome mixture of the streams' alternatives plays the RIPr role, and for exponential or negative binomial families the mean-matched element is not the RIPr [turnerGenericEvariablesExact2024, eq. 3.6, Sec. 8.1].
- The survey treats the per-τ RIPr as a sub-probability measure, GRO among functions of X^τ, sometimes an e-process and sometimes not; the independence-test denominator ∫ q(Y | x) dR(x) is a RIPr [ramdasGametheoreticStatisticsSafe2023, Sec. 3.3.2, eq. 17, Sec. 4.2].
- Sequential RIPr for the Cox model with covariates is valid for any prior but not yet computable; a Li–Barron algorithm is proposed [terschureAnytimevalidLogrankTest2024, Thm B.1, App. B.2].
- The reply doubts Bon and Robert's conjecture that the RIPr prior on a bounded Gaussian location null is an endpoint point mass: experiments show the mass spreads over many points, a single point only when the alternative prior's mean lies outside the interval [grunwaldAuthorsReplyDiscussion2024, Sec. 3].
- A new exactly solvable family: for microcanonical maximum entropy nulls the RIPr prior is the push-forward of the alternative's universal distribution onto the null sufficient statistic; for canonical nulls the RIPr stays uncomputable and the microcanonical RIPr gives a valid lower bound [giuffridaTestingMaximumEntropy2025, eqs 29–31, 47].
- Assumption-free definition dP*/dQ = 1/X* on the effective null; P* coincides with Li's and with Lardy–Grünwald–Harremoës's RIPr whenever those exist, can be a proper sub-probability, and H(Q | P) can be infinite for every P in the null while H(Q | P*) is finite or zero [larssonNumeraireEvariableReverse2025, Lemma 3.3, Def. 3.4, Thm 4.7, Cors 4.10–4.11, Examples 4.4, 4.9, Table 1].
- Under group invariance the infimum KL over null-and-alternative mixtures equals the invariant KL and is approached, not attained, by truncated right-Haar priors when the group is non-compact [perezortizEstatisticsGroupInvariance2024, Thm 2].
- Betting-information identity I_bet(Q, θ) = inf_{R : E_R X = θ} D(Q ‖ R) with explicit minimiser dR*/dQ = 1/f_{λ*} [sahaNonpartitionedEdetectorsNonparametric2026, Lemma C.4]; RIPr block e-values multiply into supermartingales usable as e-detector baselines [shinEdetectorsNonparametricFramework2023, Sec. 2.6]; RIPr e-variables supply e-collections with nuisance parameters for the e-posterior [grunwaldEposterior2023, Sec. 5].
- Description-gain definition: the RIPr is the unique limit, in an averaged Bregman metric equivalent to L₁(P) convergence of logs, of sequences with vanishing maximum description gain; it subsumes Li's definition, with existence via finite convex hulls or finite minimax regret with NML in the null; a strict sub-probability RIPr can occur on a countable space with finite KL, ruled out by a constraint-domination condition; e-statistics of a null equal those of its convex, σ-convex and Choquet-convex hulls, RIPrs on different hulls agree when they exist, but an RIPr may exist on the σ-convex hull and not on the convex hull; description-gain closeness δ transfers to e-statisticity at rate δ^{β/(1+β)} under moment bounds; a gap in Li's convergence proof is repaired [lardyReverseInformationProjections2023, Thms 3–7, Props 2–5, Examples 2–4, Sec. III-C].
- Finite nulls: exact e-variables exist iff Span P ∩ Conv Q = ∅, with the finite-sample e-variable 1 + (orthogonal component of Q) [zhangExistencePowerfulPvalues2023, Thm 3.1, Remark 3.7]. The RIPr of μ_{λ*} onto a one-sided sub-ψ null is μ_0; a reference-measure version of the finite-constraint theory adds indicators of null sets as constraints [larssonTestingHypothesesGenerated2025, Example 7.5, Thm 3.10]. RIPr of N(μ, σ²) onto the scale family is N(0, σ² + μ²) [wangAnytimevalidTtestsConfidence2023, Prop. 6.5, C.3].
- The Haar average Q̄ = E_G[GQ] of the alternative is the RIPr onto the G-invariant laws; an invariant σ-finite reference measure may replace Q̄ in densities [koningMeasuringEvidenceExchangeability2023, Cor. 3, Lemma 3, Prop. 2]. Whether replacing the null MLE by the RIPr keeps the predictive-recursion statistic an e-process is open [dixitAnytimeValidAsymptotically2023, Sec. 3.1].
- For convex model classes sequential mixing covers the RIPr of the truth time-uniformly via E[p_θ/q*] ≤ 1, a sequential mixed analogue of Wasserman et al.'s Proposition 7 [kirschnerConfidenceEstimationSequential2025, Thm 12].
- The forward information projection of a simple null onto the alternative: for H_0 = {P_0} the GROW e-variable is p*_1/p_0 with P*_1 the Csiszár information projection of P_0 onto H_1, characterised by the Pythagorean property D(P ‖ P_0) ≥ D(P ‖ P*_1) + D(P*_1 ‖ P_0) for all P ∈ H_1, which needs neither convexity of H_1 nor attainment of the KL infimum; for mean-defined alternatives with convex M_1 the projection is the exponential-family element P̄_{μ*} at the KL-closest boundary mean, and for a one-dimensional two-sided alternative it is a two-point boundary mixture [grunwaldGrowthOptimalEVariablesExtension2024a, eqs 1.6–1.8, Prop. 1, Prop. 2, Thm 3]. The Pythagorean property is equivalent to the minimax statement (Grünwald–Dawid 2004, Sec. 8) and links to Topsøe 1979 [grunwaldGrowthOptimalEVariablesExtension2024a, Sec. 1.2].

## Variants and related concepts
- [gro-criterion](gro-criterion.md), [numeraire](numeraire.md).
- [bayes-factor-e-variable](bayes-factor-e-variable.md), the RIPr as a forced null prior.

## Sources
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — definition, Theorem 1, existence proofs, examples.
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — bipolar definition, duality, history.
- [haoEValuesExponentialFamilies2025](../sources/haoEValuesExponentialFamilies2025.md) — explicit and approximate RIPrs in exponential families.
- [wassermanUniversalInference2020](../sources/wassermanUniversalInference2020.md) — RIPr under misspecification, RIPr split LRT.
- [koolenLogoptimalAnytimevalidEvalues2022](../sources/koolenLogoptimalAnytimevalidEvalues2022.md) — sequential RIPr, point-RIPr cases.
- [grunwaldOptimalEValuesExponential2024](../sources/grunwaldOptimalEValuesExponential2024.md) — degeneracy criterion.
- [turnerExactAnytimevalidConfidence2023](../sources/turnerExactAnytimevalidConfidence2023.md), [turnerGenericEvariablesExact2024](../sources/turnerGenericEvariablesExact2024.md) — contingency-table RIPrs.
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md), [terschureAnytimevalidLogrankTest2024](../sources/terschureAnytimevalidLogrankTest2024.md) — survey view, survival with covariates.
- [grunwaldAuthorsReplyDiscussion2024](../sources/grunwaldAuthorsReplyDiscussion2024.md) — spread of RIPr priors.
- [giuffridaTestingMaximumEntropy2025](../sources/giuffridaTestingMaximumEntropy2025.md) — microcanonical RIPr.
- [larssonNumeraireEvariableReverse2025](../sources/larssonNumeraireEvariableReverse2025.md) — assumption-free RIPr.
- [perezortizEstatisticsGroupInvariance2024](../sources/perezortizEstatisticsGroupInvariance2024.md) — invariant case.
- [sahaNonpartitionedEdetectorsNonparametric2026](../sources/sahaNonpartitionedEdetectorsNonparametric2026.md), [shinEdetectorsNonparametricFramework2023](../sources/shinEdetectorsNonparametricFramework2023.md), [grunwaldEposterior2023](../sources/grunwaldEposterior2023.md) — applied uses.
- [lardyReverseInformationProjections2023](../sources/lardyReverseInformationProjections2023.md) — description-gain RIPr.
- [zhangExistencePowerfulPvalues2023](../sources/zhangExistencePowerfulPvalues2023.md), [larssonTestingHypothesesGenerated2025](../sources/larssonTestingHypothesesGenerated2025.md), [wangAnytimevalidTtestsConfidence2023](../sources/wangAnytimevalidTtestsConfidence2023.md) — finite-null and worked RIPrs.
- [koningMeasuringEvidenceExchangeability2023](../sources/koningMeasuringEvidenceExchangeability2023.md), [dixitAnytimeValidAsymptotically2023](../sources/dixitAnytimeValidAsymptotically2023.md) — invariance RIPr, open question.
- [kirschnerConfidenceEstimationSequential2025](../sources/kirschnerConfidenceEstimationSequential2025.md) — RIPr coverage under misspecification.
- [grunwaldGrowthOptimalEVariablesExtension2024a](../sources/grunwaldGrowthOptimalEVariablesExtension2024a.md) — forward projection for simple nulls, Pythagorean property.

## Disagreements / open issues
- No general fast algorithm for computing the RIPr prior is given; numerical accuracy for infinite sample spaces is unclear [grunwaldSafeTesting2024, Sec. 2]; direct computation is infeasible for large effect sizes in the simulations [haoEValuesExponentialFamilies2025, Sec. 4].
- Whether q/p_{W_0,(n)} with the Gaussian O(1/n)-variance prior is exactly an e-variable in general exponential families, or only o(1)-close in e-power, is unresolved [haoEValuesExponentialFamilies2025, below Thm 3].
