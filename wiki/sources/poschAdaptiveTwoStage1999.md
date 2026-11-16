---
citekey: poschAdaptiveTwoStage1999
title: "Adaptive two stage designs and the conditional error function"
authors: [Martin Posch, Peter Bauer]
year: 1999
status: published
public: true
note: "Four adaptive two-stage designs (Proschan–Hunsberger, Lehmacher–Wassmer, Bauer–Köhne, Shen–Fisher) are each written as a conditional error function A(z₁) integrating to α under the null, which shows that combination tests and conditional error functions describe the same rejection regions and gives a conditional power function for comparing designs and reassessing the sample size."
links:
  pdf: ""
  arxiv: ""
  doi: "10.1002/(SICI)1521-4036(199910)41:6<689::AID-BIMJ689>3.0.CO;2-P"
  video: ""
tags: [adaptive-designs, conditional-error-function, combination-test, fisher-product-test, inverse-normal-method, conditional-power, sample-size-reassessment, two-stage-design, clinical-trials, history]
ingested: 2026-11-11
version: "Version of record, Biometrical Journal 41(6):689–696, 1999 (received February 1999, accepted June 1999), Wiley PDF from Zotero with Zotero text layer; the font encoding has mangled every formula, which are reconstructed below from context and checked numerically where the paper gives numbers."
---

# Adaptive two stage designs and the conditional error function

Department of Medical Statistics, University of Vienna. An eight-page note that takes Proschan and Hunsberger's 1995 device and uses it as a common language for the adaptive two-stage designs then on the table [poschAdaptiveTwoStage1999].

## Summary
The setting is the one-sided test of H_0: μ = 0 against μ > 0 for a normal mean with known variance, with standardised stage-wise means z_1 (from n_1 units) and z_2 (from n_2 units, n_2 chosen after seeing the first stage). A conditional error function for the level α is a non-decreasing A: R → [0, 1] with ∫ A(z)φ(z) dz = α; it gives the conditional probability under H_0 of rejecting given z_1. The note computes A for four designs: Proschan and Hunsberger's circular function, Lehmacher and Wassmer's unweighted inverse-normal design with group-sequential boundaries, Bauer and Köhne's Fisher product test, and Shen and Fisher's self-designing trial restricted to two stages. Early rejection is A = 1 and early acceptance is A = 0, so stopping boundaries are part of the same function. Written this way the designs can be compared directly (Figure 1), and one sees that each of them can end with a final test of the pooled sample at a local level above α when the second stage is large. The conditional power function, the same conditional rejection probability computed under an alternative, compares designs with the same first-stage stopping rule (Figure 2) and is the natural tool for choosing n_2. The concluding remarks say that little is known about the optimal choice of the conditional error function.

## Main results
- **Definition (Sec. 1).** A non-decreasing A: R → [0, 1] with ∫ A(z)φ(z) dz = α, φ the standard normal density, is a conditional error function for the level α. Any second-stage test whose conditional null rejection probability given z_1 equals A(z_1) for all z_1 has level α, whatever the rule for n_2.
- **Proschan and Hunsberger (Sec. 2).** Pooled statistic Z = w_1z_1 + w_2z_2 with w_1 = √(n_1/(n_1 + n_2)), w_2 = √(n_2/(n_1 + n_2)); the conditional rejection probability is CP_μ(n_2, c | z_1) = 1 − Φ((c√(n_1 + n_2) − z_1√n_1 − n_2μ)/√n_2), and CP_0 = A(z_1) holds iff the critical value is c(n_2, z_1) = (√n_1 z_1 + √n_2 z_{1−A(z_1)})/√(n_1 + n_2), after which n_2 is free. Circular function: A_cir(z_1) = 0 for z_1 < z_{1−α_0}, 1 − Φ(√(z²_{1−α_1} − z_1²)) for z_{1−α_0} ≤ z_1 ≤ z_{1−α_1}, and 1 above, with 0 ≤ α_1 < α and α_0 < 0.5 solving the level condition. As n_2 → ∞, c → z_{1−A(z_1)}, which is below z_{1−α} whenever max(z_{1−α_0}, √(z²_{1−α_1} − z²_{1−α})) ≤ z_1 ≤ z_{1−α_1}; with α = 0.025 and Pocock's α_1 = 0.0147 (so α_0 = 0.174, z_{1−α_0} = 0.940) this is z_1 > 0.950, almost the whole continuation region.
- **Lehmacher and Wassmer (Sec. 3).** Z = (z_1 + z_2)/√2 with critical values z_{1−α_1} for z_1 and z_{1−α_2} for Z, so A(z_1) = P(Z > z_{1−α_2} | z_1) = 1 − Φ(√2 z_{1−α_2} − z_1) for z_1 ≤ z_{1−α_1} and 1 above; no early acceptance, so A > 0 everywhere. For n_1 = n_2 it is the classical group-sequential design; for n_1 ≠ n_2 the stages are not weighted by sample size. In general it is a combination test of stage-wise p-values with Z = (1/√2) Σ Φ^{−1}(1 − p_i). The pooled statistic falls below z_{1−α} at rejection when √2 z_{1−α_2} − z_1 < z_{1−α}, i.e. z_1 > 1.120 for α = 0.025, α_1 = α_2 = 0.0147.
- **Bauer and Köhne (Sec. 4).** Fisher's product criterion with early acceptance if p_1 > α_0 and early rejection if p_1 < α_1; reject at stage 2 if p_1p_2 < c_{α_2} = exp(−χ²_{4,1−α_2}/2); level condition α_1 + c_{α_2}(log α_0 − log α_1) = α. With p_1 = 1 − Φ(z_1): A(z_1) = 0 for z_1 < z_{1−α_0}, c_{α_2}/(1 − Φ(z_1)) = c_{α_2}/p_1 for z_{1−α_0} ≤ z_1 ≤ z_{1−α_1}, and 1 above. The second stage is tested at the adjusted level c_α/p_1, which exceeds α iff p_1 < c_α/α = 0.152 for α = 0.025, "very frequently" for large n_2.
- **Shen and Fisher (Sec. 5).** Prespecified weights 0 ≤ w_1 ≤ 1, w_2 = √(1 − w_1²), Z = w_1z_1 + w_2z_2 tested at z_{1−α}, early acceptance if z_1 < z_{1−α_0} without adjusting for it (conservative): A(z_1) = 0 below z_{1−α_0} and 1 − Φ((z_{1−α} − w_1z_1)/w_2) above. A special case of Proschan and Hunsberger's linear conditional error function, already in Lan and Wittes 1988; the Lehmacher–Wassmer continuation region is the equal-weight case.
- **Comparison (Sec. 6, Figure 1).** With α = 0.025, α_1 = 0.0147: the PH and BK functions vanish for small z_1 (α_0 = 0.174 and 0.221 respectively), the LW function does not; the limiting level for n_2 → ∞, A(z_{1−α_1}), is largest for PH and smallest for LW.
- **Conditional power function (Sec. 7, Figure 2).** LW: 1 − Φ(√2 z_{1−α_2} − z_1 − μ√n_2); BK with α_0 = 1: 1 − Φ(z_{1−α*} − μ√n_2) with α* = c_α/(1 − Φ(z_1)). The product test has the higher conditional power for small z_1 and LW for large z_1, with a switching point that does not depend on μ√n_2. Overall power with n_1 = n_2 at μ√n_1 = 1, 2, 3, 4: 0.248, 0.748, 0.980, 0.9997 (BK) against 0.258, 0.764, 0.983, 0.9998 (LW); with n_2 = 2n_1 at 1, 2, 3: 0.338, 0.8951, 0.9985 against 0.340, 0.8953, 0.9984. Proceeding to stage 2 one may choose n_2 to reach a target conditional power, plugging in the first-stage variance estimate when σ² is unknown.
- **Unknown variance (Sec. 8).** PH is valid only asymptotically; BK is exact with one-sided t-test p-values from the disjoint stage samples; LW and SF are exact if Z = w_1Φ^{−1}(1 − p_1) + w_2Φ^{−1}(1 − p_2) is used.

## Setting and assumptions
- Null: simple, μ = 0 for a normal mean with known variance (one-sided alternative); unknown variance only in Sec. 8.
- Two stages; the second-stage sample size may depend on the first stage in any way; the stages use disjoint samples.
- No optional stopping beyond the single interim look, no multiple testing, no optimality criterion.
- No measure-theoretic treatment of the adaptation rule; that is [liuUnifiedTheoryTwoStage2002](liuUnifiedTheoryTwoStage2002.md) and [brannathProbabilisticFoundationConfirmatory2012](brannathProbabilisticFoundationConfirmatory2012.md).

## Relation to other sources
- [brannathAnytimevalidTestingEvalues2026a](brannathAnytimevalidTestingEvalues2026a.md): cites this note for the equivalence of combination tests and conditional error functions; its Example 2 is the Bauer–Köhne function with α_0 = 1, A = min(1, c/P_1). Wiki's reading, not the note's wording: on the e-scale each A(z_1)/α here is a first-stage e-variable with null expectation one, capped at 1/α, and for a function of p_1 it is a (capped, possibly zero-truncated) p-to-e calibrator, so the note is a catalogue of four calibrators in use in clinical trials before the word existed.
- [brannathMultiplicityFlexibilityClinical2007](brannathMultiplicityFlexibilityClinical2007.md): cites this note (with Wassmer 1999) for "both methods are equivalent" and extends A to functions of several first-stage statistics.
- [liuUnifiedTheoryTwoStage2002](liuUnifiedTheoryTwoStage2002.md): supplies the conditions under which "n_2 can be chosen in an arbitrary way" is a theorem.
- [koningAnytimeValidityFree2026](koningAnytimeValidityFree2026.md): the Lehmacher–Wassmer function A(z_1) = P(Z > z_{1−α_2} | z_1) is the induced test of a fixed-sample z-test at the interim.
- brannathOptimalMonotoneConditional2026 (in the bib and raw/, not ingested) takes up the open question of the optimal choice of A.
- Not sources: Proschan and Hunsberger 1995; Bauer and Köhne 1994; Bauer and Röhmel 1995; Lehmacher and Wassmer 1999; Shen and Fisher 1999; Fisher 1998; Lan and Wittes 1988; Wassmer 1998; Pocock 1977; O'Brien and Fleming 1979; DeMets and Ware 1980; Posch and Bauer 1999, Interim analysis and sample size reassessment (mimeo, University of Vienna).

## Concepts touched
- [conditional-error-functions](../concepts/conditional-error-functions.md): the catalogue and the equivalence with combination tests.
- [calibrator](../concepts/calibrator.md): A(p_1)/α as a capped calibrator.
- [martingale-history](../concepts/martingale-history.md): the adaptive-design lineage.

## Versions
Only the Biometrical Journal version of record exists.

## Open questions / gaps
- "Little is known on the 'optimal' choice of the conditional error function. It has to be expected that optimal proposals will depend on the underlying assumptions in the design phase" (Sec. 9).
- Sec. 4 quotes α_0 = 0.174 alongside the Bauer–Köhne example while Sec. 6 gives α_0 = 0.221 for that design; the level condition gives 0.221 for α = 0.025, α_1 = 0.0147, α_2 = α, and the threshold p_1 < 0.152 does not depend on α_0. Either a slip in the paper or in the text layer; not checked against the PDF.
- Figures 1 and 2 are described from the captions and text only.
- The text layer is unusable for quoting formulas; consult the PDF before quoting any equation.
