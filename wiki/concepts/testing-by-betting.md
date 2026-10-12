---
slug: testing-by-betting
title: Testing by betting
sources: 21
updated: 2026-10-12
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
- The payout is E, not log E; agreement with Shafer that free continuation is best treated game-theoretically [grunwaldAuthorsReplyDiscussion2024, Secs 1, 4].
- The numeraire property is the numeraire-portfolio property (any wealth divided by the numeraire is a supermartingale), its existence theorem the e-variable fundamental theorem of asset pricing, and the numeraire is the optimal Kelly bet against P when reality follows Q [larssonNumeraireEvariableReverse2025, Def. 2.1, Thm 2.6].
- One-dollar-per-day skeptic reading of e-detectors: Shiryaev–Roberts is total wealth, CUSUM max-minus-min wealth [shinEdetectorsNonparametricFramework2023, Sec. 6.1]; receding floors in the generalised Ville inequality are deterministic subsidies funding repeated attempts, i.e. multiple testing [koolenGeneralisationVilleInequality2025, Sec. 5]; bounded conditional-mean nulls tested by wealth Π(1 + λ(X − θ)) with betting information governing delay [sahaNonpartitionedEdetectorsNonparametric2026, eq. 17, Thm 4.2]; the De Finetti-style bookie game behind the e-posterior risk bound [grunwaldEposterior2023, Sec. 2].
- Parallel games for every candidate mean, bets as signed capital fractions, the constrained adversary who sees disclosed bets, and the four-thread history (probability, statistics, information theory, online learning) that 'rarely cited each other' [waudbysmithEstimatingMeansBounded2020, Secs 4.1, 4.3, 6, App. F]. Parallel-games protocol for a null that is a convex hull of sub-nulls, with skeptic wealth the worst game [ramdasTestingExchangeabilityForkconvexity2021, Sec. 5.4]. Inverse capital measure as minimal super-replicating capital, 1/ν(A) as maximal wealth [rufCompositeGeneralizationVille2022, Cor. 3.10, Lemma 3.11]. Betting e-variables as all admissible e-variables for a bounded mean [larssonTestingHypothesesGenerated2025, Example 3.8].
- Game-theoretic forecast comparison with adversarial Reality choosing outcomes after seeing both forecasts [choeComparingSequentialForecasters2021, Game 1]; cumulative capital reaching level 10 with 9–27% of the data in the precipitation study [henziValidSequentialInference2021, Fig. 3]; the regulator bets a fraction λ_t of capital on each day's exceedance, may announce λ after seeing the forecast, and the bank's ignorance of λ deters gaming [wangEbacktesting2022, Sec. 4.1, App. E].

## Variants and related concepts
- [e-power](e-power.md), [gro-criterion](gro-criterion.md), [e-process](e-process.md).

## Sources
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — Sec. 1.5, Chapter 7.
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — interpretation and reply.
- [shaferTestingBettingStrategy2021](../sources/shaferTestingBettingStrategy2021.md) — the primary source.
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md) — the game and the central principle.
- [vovkEvaluesCalibrationCombination2021](../sources/vovkEvaluesCalibrationCombination2021.md), [koolenLogoptimalAnytimevalidEvalues2022](../sources/koolenLogoptimalAnytimevalidEvalues2022.md), [terschureAnytimevalidLogrankTest2024](../sources/terschureAnytimevalidLogrankTest2024.md) — betting readings.
- [villeEtudeCritiqueNotion1939](../sources/villeEtudeCritiqueNotion1939.md) — the original gambler.
- [grunwaldAuthorsReplyDiscussion2024](../sources/grunwaldAuthorsReplyDiscussion2024.md) — payout and game-theoretic framing.
- [larssonNumeraireEvariableReverse2025](../sources/larssonNumeraireEvariableReverse2025.md), [shinEdetectorsNonparametricFramework2023](../sources/shinEdetectorsNonparametricFramework2023.md), [koolenGeneralisationVilleInequality2025](../sources/koolenGeneralisationVilleInequality2025.md), [sahaNonpartitionedEdetectorsNonparametric2026](../sources/sahaNonpartitionedEdetectorsNonparametric2026.md), [grunwaldEposterior2023](../sources/grunwaldEposterior2023.md) — betting readings.
- [waudbysmithEstimatingMeansBounded2020](../sources/waudbysmithEstimatingMeansBounded2020.md), [ramdasTestingExchangeabilityForkconvexity2021](../sources/ramdasTestingExchangeabilityForkconvexity2021.md), [rufCompositeGeneralizationVille2022](../sources/rufCompositeGeneralizationVille2022.md), [larssonTestingHypothesesGenerated2025](../sources/larssonTestingHypothesesGenerated2025.md) — batch-4 contributions.
- [choeComparingSequentialForecasters2021](../sources/choeComparingSequentialForecasters2021.md), [henziValidSequentialInference2021](../sources/henziValidSequentialInference2021.md), [wangEbacktesting2022](../sources/wangEbacktesting2022.md) — forecasting and backtesting games.

## Disagreements / open issues
- Shafer 2021 (in the bib) and Shafer and Vovk 2019 (not in the bib) are the primary sources and are not yet ingested.
