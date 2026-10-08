---
slug: testing-by-betting
title: Testing by betting
sources: 8
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
- Primary source: a test of P is a bet, buy a nonnegative payoff S with E_P[S] = 1; the betting score is the multiplier on the stake; every bet implies an alternative Q = SP; the implied target replaces power; testing protocols with Sceptic, Reality and Forecaster; the reply argues betting scores are strictly more general than e-values because products across unplanned experiments are no single bet's value, and reframes the enterprise as prediction testing [shaferTestingBettingStrategy2021, Secs 2, 4, reply]; see [e-power](e-power.md).
- The survey's central principle: no strategy makes money under the null, some strategy does under the alternative; Forecaster/Skeptic/Reality game; betting score as realised over expected value; two generalised games with an Intermediary or parallel games for composite nulls [ramdasGametheoreticStatisticsSafe2023, Secs 1, 1.2].
- Betting readings of products (successive full-stake bets), U-statistics (fractions of capital in sub-bets) and family-wise validity ('made at least E*_k risking at most one against any Q in H_k') [vovkEvaluesCalibrationCombination2021, Secs 4–5].
- The game tree with an opponent controlling stop/continue nodes and the null choosing chance moves [koolenLogoptimalAnytimevalidEvalues2022, Sec. 2.3]; the test martingale as capital in a sequential game with no expected earnings under the null [terschureAnytimevalidLogrankTest2024, Sec. 3.1].
- Ville's gambler with betting fractions λ_n, μ_n and the reading of von Mises's impossibility of a gambling system, with the complaint that von Mises ignored the distribution of stakes [villeEtudeCritiqueNotion1939, Ch. IV §§2–3].

## Variants and related concepts
- [e-power](e-power.md), [gro-criterion](gro-criterion.md), [e-process](e-process.md).

## Sources
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — Sec. 1.5, Chapter 7.
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — interpretation and reply.
- [shaferTestingBettingStrategy2021](../sources/shaferTestingBettingStrategy2021.md) — the primary source.
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md) — the game and the central principle.
- [vovkEvaluesCalibrationCombination2021](../sources/vovkEvaluesCalibrationCombination2021.md), [koolenLogoptimalAnytimevalidEvalues2022](../sources/koolenLogoptimalAnytimevalidEvalues2022.md), [terschureAnytimevalidLogrankTest2024](../sources/terschureAnytimevalidLogrankTest2024.md) — betting readings.
- [villeEtudeCritiqueNotion1939](../sources/villeEtudeCritiqueNotion1939.md) — the original gambler.

## Disagreements / open issues
- Shafer 2021 (in the bib) and Shafer and Vovk 2019 (not in the bib) are the primary sources and are not yet ingested.
