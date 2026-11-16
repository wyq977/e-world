---
citekey: csiszarIDivergenceGeometryProbability1975
title: "I-divergence geometry of probability distributions and minimization problems"
authors: [Imre Csiszár]
year: 1975
status: published
public: true
note: "Treats Kullback–Leibler divergence as a squared distance: the I-projection of a distribution onto a variation-closed convex set exists, is characterised by a Pythagorean inequality, and under linear constraints is an exponential-family member; the source of the projection geometry behind GROW e-variables for a simple null."
links:
  pdf: ""
  arxiv: ""
  doi: 10.1214/aop/1176996454
  video: ""
tags: [information-projection, i-projection, kl-divergence, pythagorean-theorem, exponential-families, minimum-discrimination-information, iterative-proportional-fitting, convex-sets, history]
ingested: 2026-11-16
version: "publisher-vor: Annals of Probability 3(1):146–158, February 1975 (JSTOR scan)"
---

# I-divergence geometry of probability distributions and minimization problems

## Summary
The paper develops a geometry of probability distributions (PDs) in which the I-divergence I(P ‖ Q) = ∫ log(dP/dQ) dP plays the role of squared Euclidean distance, and uses it to study the minimum discrimination information problem: given a PD R and a convex set ℰ of PDs, find Q ∈ ℰ minimising I(P ‖ R) over P ∈ ℰ [csiszarIDivergenceGeometryProbability1975]. Such a Q is called the I-projection of R on ℰ; the set S(R, ρ) = {P : I(P ‖ R) < ρ} is called an I-sphere with centre R and radius ρ. Section 2 proves, from an analogue of the parallelogram identity and Pinsker's inequality, that the I-projection exists whenever ℰ is closed in variation distance, and characterises it by a tangent-hyperplane condition equivalent to a Pythagorean inequality. Section 3 specialises to sets defined by linear constraints: the projection has an exponential-family density, with necessary and sufficient conditions in the two main cases (finitely many moment constraints; prescribed marginals), a counterexample showing that the Pythagorean identity can fail for infinitely many constraints, a convergence proof for a generalised iterative proportional fitting procedure on finite spaces, and an existence theorem for moment constraints with unbounded functions. The Lagrange multiplier technique is not used. The author notes that I-divergence is not a metric and that I-spheres do not even define a topology, so the geometric analogy must be used with caution.

## Main results
- **Definitions (Section 1).** I(P ‖ Q) by (1.1)–(1.3), with log 0 = −∞ and 0·(±∞) = 0; I-sphere S(R, ρ) (1.4); I-projection of R on a convex ℰ meeting S(R, ∞): a Q ∈ ℰ with I(Q ‖ R) = min_{P ∈ ℰ} I(P ‖ R) (1.5), unique by strict convexity of I(· ‖ R) [csiszarIDivergenceGeometryProbability1975].
- **Theorem 2.1 (existence).** If the convex set ℰ is variation-closed, every R with S(R, ∞) ∩ ℰ ≠ ∅ has an I-projection on ℰ. Proof: for a minimising sequence P_n the parallelogram-type identity (2.2), I(P_m ‖ R) + I(P_n ‖ R) = 2 I((P_m + P_n)/2 ‖ R) + I(P_m ‖ (P_m + P_n)/2) + I(P_n ‖ (P_m + P_n)/2), forces the last two terms to 0; Pinsker's inequality (2.3) makes P_n Cauchy in variation, with limit Q ≪ R (2.4); Fatou gives lower semicontinuity (2.5); closedness puts Q in ℰ [csiszarIDivergenceGeometryProbability1975].
- **Remark to Theorem 2.1.** Closedness is used only to ensure that the limit Q with properties (2.4)–(2.5) lies in ℰ. So for any convex ℰ meeting S(R, ∞), every minimising sequence converges in variation to one PD Q, which need not belong to ℰ. (The paper does not name this limit; Csiszár 1984 calls it the generalized I-projection, see [csiszarSanovPropertyGeneralized1984](csiszarSanovPropertyGeneralized1984.md).)
- **Identity (2.6).** For Q ≪ R and I(P ‖ Q) or I(P ‖ R) finite: I(P ‖ R) − I(P ‖ Q) = ∫ log q_R dP, where q_R = dQ/dR [csiszarIDivergenceGeometryProbability1975].
- **Lemma 2.1 (tangent hyperplane).** If I(P ‖ Q) and I(Q ‖ R) are finite, the segment P_α = αP + (1 − α)Q, 0 < α ≤ 1, stays outside the I-sphere S(R, ρ) with ρ = I(Q ‖ R), i.e. I(P_α ‖ R) ≥ I(Q ‖ R), iff ∫ log q_R dP ≥ I(Q ‖ R) (2.8). If Q = αP + (1 − α)P′ with 0 < α < 1 (2.9), the segment from P to P′ does not intersect S(R, ρ) iff ∫ log q_R dP = I(Q ‖ R) (2.10). Proof by the one-sided derivative (2.13): (d/dα) I(P_α ‖ R) at α = 0 equals ∫ log q_R dP − I(Q ‖ R) [csiszarIDivergenceGeometryProbability1975].
- **Pythagoras (1.7).** By (2.6), condition (2.10) is equivalent to I(P ‖ R) = I(P ‖ Q) + I(Q ‖ R): the PDs satisfying it form the "tangent hyperplane" of the I-sphere at Q. The interpretation is limited to P ∈ S(R, ∞) ∪ S(Q, ∞) [csiszarIDivergenceGeometryProbability1975].
- **Theorem 2.2 (characterisation).** A PD Q ∈ ℰ ∩ S(R, ∞) is the I-projection of R on the convex set ℰ iff every P ∈ ℰ ∩ S(R, ∞) satisfies (2.8), equivalently iff I(P ‖ R) ≥ I(P ‖ Q) + I(Q ‖ R) for every P ∈ ℰ (2.14). If Q is an algebraic inner point of ℰ (every P ∈ ℰ has α and P′ ∈ ℰ with Q = αP + (1 − α)P′), then ℰ ⊂ S(R, ∞) and (2.8), (2.14) hold with equality. Remark: if the I-projection Q exists then P ≪ Q for every P ∈ ℰ ∩ S(R, ∞) [csiszarIDivergenceGeometryProbability1975].
- **Theorem 2.3 (transitivity).** If ℰ_1 ⊂ ℰ are convex, R has I-projections Q on ℰ and Q_1 on ℰ_1, and the identity (1.7) holds for every P ∈ ℰ, then Q_1 is the I-projection of Q on ℰ_1. Warning given: the elements of the segment joining Q and R need not have the same I-projection on ℰ [csiszarIDivergenceGeometryProbability1975].
- **Minimum discrimination information theorem (Section 3, restated; Kullback 1959, Kullback–Khairat 1966).** For any set ℰ, if some Q ∈ ℰ has R-density c exp g(x) with ∫ g dP constant over ℰ, then (3.1) I(P ‖ R) = I(P ‖ Q) + I(Q ‖ R) for all P ∈ ℰ; immediate from (2.6). Case (A): ℰ = {P : ∫ f_i dP = a_i, i = 1, …, k}, Q with density c exp Σ t_i f_i (3.2). Case (B): prescribed marginals P_1, P_2 on a product space, Q with density a(x_1) b(x_2), log a ∈ L_1(P_1), log b ∈ L_1(P_2) (3.3) [csiszarIDivergenceGeometryProbability1975].
- **Theorem 3.1 (linear constraints, general).** ℰ defined by ∫ f_γ dP = a_γ for an arbitrary family {f_γ}. Necessary: if R has I-projection Q on ℰ then q_R(x) = c exp g(x) off a set N with P(N) = 0 for every P ∈ ℰ ∩ S(R, ∞), with g in the closed subspace of L_1(Q) spanned by the f_γ (3.4). Sufficient: if Q ∈ ℰ has density of form (3.4) with g in the linear span (no closure), Q is the I-projection and (3.1) holds. Proof of necessity via an algebraic-inner-point argument on {P ∈ ℰ : dP/dQ ≤ 2} and Hahn–Banach [csiszarIDivergenceGeometryProbability1975].
- **Corollary 3.1.** In cases (A) and (B) the condition is necessary and sufficient, and (3.1) holds; if some P ∈ ℰ with I(P ‖ R) < ∞ is equivalent to R, then (3.2) resp. (3.3) holds without an exceptional set [csiszarIDivergenceGeometryProbability1975].
- **Example (Section 3).** On the unit interval with countably many constraints (3.5), a Q that is the I-projection of R while the inequality in (3.7) is strict for some P ∈ ℰ: the Pythagorean identity (3.1) fails for a linear set, and neither the necessary nor the sufficient condition of Theorem 3.1 is both. Reversing the sign of g gives a Q of the necessary form that is not the I-projection [csiszarIDivergenceGeometryProbability1975].
- **Corollaries 3.2–3.3.** A PD with marginals P_1, P_2 and R-density a(x_1) b(x_2) exists iff some P equivalent to R with those marginals has I(P ‖ R) < ∞; for matrices, positive diagonal D_1, D_2 with D_1 A D_2 having given row and column sums exist iff some nonnegative B with those sums has the same zero pattern as A (generalising Sinkhorn 1967 and comparing with Hobby–Pyke 1965) [csiszarIDivergenceGeometryProbability1975].
- **Theorem 3.2 (iterative proportional fitting).** On a finite set, for linear sets ℰ_1, …, ℰ_k with nonempty intersection ℰ containing some P ≪ R, cyclic I-projections Q_n of Q_{n−1} on ℰ_n (3.13), Q_0 = R, converge to the I-projection of R on ℰ. No positivity of R is assumed. The author states that the convergence proofs in Ireland–Kullback 1968 and Kullback 1968 are incomplete [csiszarIDivergenceGeometryProbability1975].
- **Lemma 3.1.** If e^{tf} is Q-integrable for small |t|, then I(P_n ‖ Q) → 0 implies ∫ f dP_n → ∫ f dQ [csiszarIDivergenceGeometryProbability1975].
- **Theorem 3.3 (existence for moment constraints).** Let T_R = {t : exp Σ t_i f_i is R-integrable} (3.16) be open and A_R the set of (a_1, …, a_k) for which ℰ(a_1, …, a_k) contains a P with I(P ‖ R) < ∞. Then for every interior point of A_R the I-projection of R on ℰ(a_1, …, a_k) exists and has density of form (3.2). Remarks: the interior of A_R is the interior of the convex hull of the support of the image of R under x ↦ (f_1(x), …, f_k(x)); on the boundary of A_R the I-projection typically still exists but its density vanishes on a set of positive R-measure ("these problems will not be entered here"); F(a) = inf I(P ‖ R) over ℰ(a) (3.18) is differentiable in the interior with grad F(a) equal to the parameter vector t of the I-projection. The first version assumed T_R = E^k; the strengthening was inspired by Čencov 1972, Theorem 23.1 [csiszarIDivergenceGeometryProbability1975].

## Setting and assumptions
- Arbitrary measurable space; all objects are probability distributions. The paper notes that in physics R may be an infinite measure, which changes little except that (1.1) may be negative or undefined.
- The set projected onto is convex throughout Section 2. Existence (Theorem 2.1) needs closedness in variation distance; the characterisation (Theorem 2.2) presupposes that the candidate Q lies in ℰ.
- The reference R is in the second argument: the paper minimises I(P ‖ R) over P. The author remarks that Čencov's geometry uses the reversed order and has no overlap with these results except for Theorem 3.3.
- No sampling model, no testing, no e-values. This is background to the wiki's topic, not a paper on it.

## Relation to other sources
- [csiszarSanovPropertyGeneralized1984](csiszarSanovPropertyGeneralized1984.md): names the variation limit of Theorem 2.1's Remark the generalized I-projection, cites Theorem 2.2 for the Pythagorean inequality when the projection is in the set, generalises Theorem 3.1 (its Lemma 3.4) and uses Lemma 3.1.
- [topsoeInformationtheoreticalOptimizationTechniques1979](topsoeInformationtheoreticalOptimizationTechniques1979.md): its Theorems 1–2 are described there as analogous to this paper's results, and its Theorem 8 proves the inequality (2.14) for the variation limit without requiring it to lie in the set, "a slight improvement over" this paper.
- [grunwaldGrowthOptimalEVariablesExtension2024a](grunwaldGrowthOptimalEVariablesExtension2024a.md): its Proposition 1 turns the Pythagorean property (2.14), with R the simple null P_0, into the statement that p*_1/p_0 is the GROW e-variable; the KL ball whose complement is that paper's alternative is an I-sphere in this paper's terms.
- [grunwaldSafeTesting2024](grunwaldSafeTesting2024.md) and [larssonNumeraireEvariableReverse2025](larssonNumeraireEvariableReverse2025.md) work with the reverse information projection, which minimises over the second argument; this paper's projection is the forward one. Wiki's reading: the two coincide in role only for a simple null against a convex alternative.
- [haoEValuesExponentialFamilies2025](haoEValuesExponentialFamilies2025.md) and [grunwaldOptimalEValuesExponential2024](grunwaldOptimalEValuesExponential2024.md): exponential-family form of projections under moment constraints (Corollary 3.1, Theorem 3.3) is the classical fact behind their constructions. Wiki's reading; neither page was checked for a direct citation.

## Concepts touched
- [information-projection](../concepts/information-projection.md)
- [reverse-information-projection](../concepts/reverse-information-projection.md)
- [gro-criterion](../concepts/gro-criterion.md)
- [exponential-family-e-values](../concepts/exponential-family-e-values.md)
- [mdl-and-maximum-entropy-e-values](../concepts/mdl-and-maximum-entropy-e-values.md)

## Versions
Only the Annals of Probability version exists. The file is a JSTOR page scan with no text layer; `paper.txt` is a tesseract OCR in which inequality signs and most displayed formulas are unreliable. The statements above were reconstructed from context and from how Csiszár 1984 quotes them (its eq. 1.5 for Theorem 2.2); quote formulas only from the PDF.

## Open questions / gaps
- What happens at boundary points of A_R in Theorem 3.3 is explicitly left out.
- The paper has no statement of the Pythagorean inequality for the variation limit when it is outside ℰ; that is in Topsøe 1979 (Theorem 8).
- Cited works not in the bib: Čencov 1972, Statistical decision rules and optimal decisions; Kullback 1959, Information theory and statistics; Kullback and Khairat 1966; Ireland and Kullback 1968; Ku and Kullback 1968; Csiszár 1967 (information-type measures, Pinsker's inequality); Kemperman 1967; Pinsker 1964; Sanov 1957; Jaynes 1957; Sinkhorn 1967; Hobby and Pyke 1965; Deming and Stephan 1940; Fienberg 1970.
