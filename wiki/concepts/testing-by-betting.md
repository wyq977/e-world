---
slug: testing-by-betting
title: Testing by betting
sources: 2
updated: 2026-10-08
---

# Testing by betting

## Definition
Testing by betting represents a hypothesis test as a sequential game: a bettor stakes wealth on outcomes at prices the null considers fair, the wealth process is a [test martingale](test-martingale.md), and large wealth is evidence against the null [ramdasHypothesisTestingEvalues2025, Sec. 1.5]. An e-value is the payoff of a single bet; the Kelly-optimal bet is the conditional likelihood ratio, and against a composite null the overall wealth is the infimum across the games for each null member [ramdasHypothesisTestingEvalues2025, Algorithms 7.16–7.17]. Safe Testing gives the gambling interpretation as the first of three readings of an e-value and names Kelly's doubling rate as the reason to maximise expected log growth [grunwaldSafeTesting2024, Sec. 1.1, Sec. 2.1].

## Key results
- p-values as hindsight-optimal bets, and the contract interpretation of an e-value [ramdasHypothesisTestingEvalues2025, Sec. 1.5].
- Empirically adaptive betting strategies are asymptotically log-optimal [ramdasHypothesisTestingEvalues2025, Thm 7.22]; see [mixture-and-plug-in-methods](mixture-and-plug-in-methods.md).
- Four contrasts between safe anytime-valid inference and Wald's sequential paradigm [ramdasHypothesisTestingEvalues2025, Sec. 7.2].
- The betting e-processes of Waudby-Smith and Ramdas for bounded means are "the same idea" as the GRO construction once seen through the numeraire [grunwaldSafeTesting2024, reply].

## Variants and related concepts
- [e-power](e-power.md), [gro-criterion](gro-criterion.md), [e-process](e-process.md).

## Sources
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — Sec. 1.5, Chapter 7.
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — interpretation and reply.

## Disagreements / open issues
- Shafer 2021 (in the bib) and Shafer and Vovk 2019 (not in the bib) are the primary sources and are not yet ingested.
