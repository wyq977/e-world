---
slug: numeraire
title: Numeraire e-variable
sources: 4
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

## Variants and related concepts
- [gro-criterion](gro-criterion.md).
- [reverse-information-projection](reverse-information-projection.md).

## Sources
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — Chapter 6 in full.
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — discussion and reply.
- [haoEValuesExponentialFamilies2025](../sources/haoEValuesExponentialFamilies2025.md) — passing use.
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md) — open problems.

## Disagreements / open issues
- Larsson, Ramdas and Ruf 2025, "The numeraire e-variable and reverse information projection", is the primary source and is not yet in the bib; see gaps.
