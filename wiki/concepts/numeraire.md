---
slug: numeraire
title: Numeraire e-variable
sources: 7
updated: 2026-10-08
---

# Numeraire e-variable

## Definition
For a composite null and a point alternative Q, the numeraire is the Q-almost-surely positive [e-variable](e-variable.md) E* with E_Q[E/E*] ≤ 1 for every e-variable E [ramdasHypothesisTestingEvalues2025, Definition 6.1]. It exists and is unique with no assumptions at all, coincides with the log-optimal (GRO) e-variable, and equals dQ/dP* where P* is the [reverse-information-projection](reverse-information-projection.md), a sub-probability measure in the bipolar effective null [ramdasHypothesisTestingEvalues2025, Thm 6.4, Prop. 6.6]. The result comes from Larsson, Ramdas and Ruf, which the Safe Testing authors endorse in their reply as the default definition of the RIPr [grunwaldSafeTesting2024, reply Sec. 2].

## Key results
- Strong duality: sup_E E_Q[log E] = inf_{P ∈ P°°} KL(Q, P) [ramdasHypothesisTestingEvalues2025, Thm 6.13].
- The numeraire is the only e-variable that is a likelihood ratio against an element of the effective null [ramdasHypothesisTestingEvalues2025, Thm 6.15].
- It dominates universal inference, making the split LRT essentially inadmissible when the numeraire is computable [ramdasHypothesisTestingEvalues2025, Sec. 6.5; grunwaldSafeTesting2024, discussion by Larsson, Ramdas and Ruf]; see [universal-inference](universal-inference.md).
- Bayes-factor connection and explicit numeraires for standard problems, including the soft-rank e-value as the numeraire for exchangeability [ramdasHypothesisTestingEvalues2025, Sec. 6.6, Sec. 6.7].
- Removes the finite-KL condition of Safe Testing's Theorem 1, which fails for example for infinite-horizon exchangeability [grunwaldSafeTesting2024, discussion by Vovk, reply].
- The exponential-family paper notes that nonparametric mean tests built by betting are sequential RIPr e-variables in disguise, a view the numeraire makes precise [haoEValuesExponentialFamilies2025, Sec. 1].
- The survey's open problems anticipate the numeraire: when the per-τ RIPr is an e-process, how much universal inference loses to it, and fast RIPr algorithms [ramdasGametheoreticStatisticsSafe2023, Sec. 8.2.4].
- The Safe Testing authors' reply adopts the numeraire as the general form of their GRO e-variable and RIPr, with the caveat that for exchangeability nulls on infinite sequences the numeraire has infinite e-power and a coarsened filtration is needed [grunwaldAuthorsReplyDiscussion2024, Sec. 1].
- Primary source, with the paper's own numbering: Definition 2.1 (numeraire), Prop. 2.4 (numeraire iff log-optimal, first-order condition), Thm 2.6 (existence and uniqueness, plus four equivalent finiteness conditions: Q ≪ P in the Halmos–Savage sense, all e-variables Q-a.s. finite, the e-variable class bounded in Q-probability), proved by a Komlós-type lemma; the e-variable 'fundamental theorem of asset pricing' [larssonNumeraireEvariableReverse2025].
- The effective null P_eff = P°°, the bipolar of the null, is the largest family with the same e-variables; dP*/dQ = 1/X* defines the sub-probability measure P* in P_eff, the unique element that is a likelihood-ratio denominator for an e-variable; strong duality E_Q[log X*] = inf_{P ∈ P_eff} H(Q | P) possibly all infinite [larssonNumeraireEvariableReverse2025, Def. 3.1, Lemma 3.3, Def. 3.4, Thm 3.6, Thm 4.1].
- Verification tools: for generated nulls check E_Q[1/X*] = 1 and E_Q[X/X*] ≤ 1 on the generators; with a reference measure check E_Q[p/p*] ≤ 1 over P only; heuristic: parametric nulls, find the RIPr first; nonparametric nulls, find the numeraire first [larssonNumeraireEvariableReverse2025, Cor. 4.2, Thm 4.7, Remark 5.3].
- Explicit nonparametric numeraires: bounded mean 1 + λ*(Z − μ) with λ* solving (1 + λ*(1 − μ))/(1 − λ*μ) = e^{λ*}; sub-Gaussian nonpositive mean e^{μZ − μ²/2} with RIPr N(0,1); symmetry 2q(Z)/(q(Z) + q(−Z)), the e-variable class being exactly {X ≤ 1 + φ(Z), φ odd}; Gaussian pair vs Cauchy with RIPr (P1 + P2)/2 [larssonNumeraireEvariableReverse2025, Secs 5.1–5.4].
- Power utility x^{1−γ}/(1 − γ), γ > 1, gives U-optimal e-variables and reverse Rényi projections of order 1/γ, always existing; the Lardy et al. e-variable is strictly smaller [larssonNumeraireEvariableReverse2025, Thm 6.1]. Universal inference is dominated, hence inadmissible for nondegenerate composite nulls [larssonNumeraireEvariableReverse2025, Sec. 7, Lemma 7.1].
- The log-optimal e-value is the unique utility-optimal e-value preserved under conditioning [koningAnytimeValidityFree2026, Thm 7].

## Variants and related concepts
- [gro-criterion](gro-criterion.md).
- [reverse-information-projection](reverse-information-projection.md).

## Sources
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — Chapter 6 in full.
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — discussion and reply.
- [haoEValuesExponentialFamilies2025](../sources/haoEValuesExponentialFamilies2025.md) — passing use.
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md) — open problems.
- [grunwaldAuthorsReplyDiscussion2024](../sources/grunwaldAuthorsReplyDiscussion2024.md) — endorsement and caveat.
- [larssonNumeraireEvariableReverse2025](../sources/larssonNumeraireEvariableReverse2025.md) — primary source.
- [koningAnytimeValidityFree2026](../sources/koningAnytimeValidityFree2026.md) — conditioning invariance.

## Disagreements / open issues
- Book numbering (Def 6.1, Thm 6.4, Prop 6.6, Thm 6.13, Thm 6.15) maps to the paper's Def 2.1, Thm 2.6, Lemma 3.3/Def 3.4, Thm 3.6, Thm 4.1.
