---
slug: martingale-history
title: History: from collectives to safe anytime-valid inference
sources: 12
updated: 2026-10-12
---

# History: from collectives to safe anytime-valid inference

## Definition
The lineage of test martingales and e-values as recorded by the sources: von Mises's collectives (1919) and Wald's countable selection systems (1937); Ville's 1939 thesis, which coined "martingale" for a gambling system, gave the first general definition via conditional expectations, proved the maximal inequality now bearing his name, and showed selection-rule randomness cannot capture the law of the iterated logarithm [villeEtudeCritiqueNotion1939, Ch. II, IV, V]; Doob's adoption of the word for the stochastic process; Wald's SPRT with plug-in and mixture extensions (1945, 1947); Kelly 1956 and Breiman 1961 on log-optimal gambling; Robbins, Darling, Siegmund and Lai on confidence sequences, mixture SPRTs and tests of power one (1967–1976); Shafer and Vovk's game-theoretic probability; and the post-2017 composite-null literature [ramdasGametheoreticStatisticsSafe2023, Secs 1, 2.5–2.6, 8.1; shaferTestingBettingStrategy2021, Appendix; grunwaldSafeTesting2024, Sec. 7].

## Key results
- What Ville did and did not do: Chapter IV Theorem 1 (every null set is detected by a martingale) and Theorem 2 (every martingale is a.s. bounded); Chapter V Definition 1 and Theorem 1 (P(sup s_n ≥ λ) ≤ 1/λ); Bernoulli martingales are Beta-type mixtures by de Finetti's representation; no testing, no alternative, no α [villeEtudeCritiqueNotion1939].
- Shafer's reading: Ville strengthened von Mises's impossibility of a gambling system; Fisher's likelihood ratio of 1/15, Edwards and Royall on likelihood; after Doob nobody read a nonnegative martingale's running value as cumulative evidence; Wald knew Ville [shaferTestingBettingStrategy2021, Appendix, reply].
- The survey's taxonomy of ancestors: Ville's inequality and theorem, Wald's plug-in from eq. 10.10 of his 1947 book, Rushton and Cox on the sequential t-test, Darling–Robbins power-one tests, Lai's anytime-valid t-test; Barnard 1947's "embedded statistician" as an early betting framing [ramdasGametheoreticStatisticsSafe2023, Secs 1.2, 2.6, 3.2, 4.1, 8.1.2].
- Terminology: Vovk and V'yugin 1993 "impossibility measure", Shafer 2019 "betting score", Shafer and Vovk 2019 "Skeptic's capital", Grünwald et al. 2019 "S-value", Vovk and Wang 2019 "e-value" [shaferTestingBettingStrategy2021, reply; grunwaldSafeTesting2024, Sec. 7; vovkEvaluesCalibrationCombination2021, Sec. 2].
- Calibrator lineage: Vovk 1993, Sellke, Bayarri and Berger 2001, Shafer, Shen, Vereshchagin and Vovk 2011 [vovkEvaluesCalibrationCombination2021, Sec. 2]; see [calibrator](calibrator.md).
- Independent discovery in physics: Zhang, Glancy and Knill 2011 proved a special case of the GRO theorem for rejecting local realism [grunwaldSafeTesting2024, Sec. 7].
- Wald's likelihood-ratio martingale and his awareness of Ville; Darling and Robbins's 1967 union-bound definition of a confidence sequence; Robbins's tests of power one versus Wald's SPRT; Johari et al. as modern proponents of always-valid p-values [ramdasAdmissibleAnytimevalidSequential2022, Secs 2.1, 3.2]. Stochastic curtailment and conditional power (Lan, Simon, Halperin 1982; Müller, Schäfer 2004) as an unnoticed precursor of test induction, and Breiman 1961 as the precursor of the SPRT-as-limit theorem [koningAnytimeValidityFree2026, Sec. 1.4, Remark 14]. Lai 1976 made the first anytime-valid use of the right-Haar t-test ratio [perezortizEstatisticsGroupInvariance2024, Sec. 2].
- Four-thread timeline (probability, statistics, information theory, online learning), Doob 'stripped martingales of their betting roots', Wald's eq. 10:10 as the first predictable plug-in [waudbysmithEstimatingMeansBounded2020, Sec. 6, App. F, Fig. 9]. Ville's theorem on coin flips and the LIL, Doob 1940 crediting the inequality to Ville, the strategy-vs-wealth terminology switch, Ville's 1984–85 recollections [rufCompositeGeneralizationVille2022, Sec. 5]. Fork-convexity traced to Žitković, Delbaen's m-stability and Epstein–Schneider rectangularity [ramdasTestingExchangeabilityForkconvexity2021, Sec. 3.1]. Lai 1976 dissected [wangAnytimevalidTtestsConfidence2023, Sec. 4].

## Variants and related concepts
- [villes-inequality](villes-inequality.md), [test-martingale](test-martingale.md), [testing-by-betting](testing-by-betting.md).

## Sources
- [villeEtudeCritiqueNotion1939](../sources/villeEtudeCritiqueNotion1939.md) — primary source.
- [shaferTestingBettingStrategy2021](../sources/shaferTestingBettingStrategy2021.md) — Appendix and reply.
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md) — survey history sections.
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — Sec. 7 related work.
- [vovkEvaluesCalibrationCombination2021](../sources/vovkEvaluesCalibrationCombination2021.md) — naming and calibrator history.
- [ramdasAdmissibleAnytimevalidSequential2022](../sources/ramdasAdmissibleAnytimevalidSequential2022.md), [koningAnytimeValidityFree2026](../sources/koningAnytimeValidityFree2026.md), [perezortizEstatisticsGroupInvariance2024](../sources/perezortizEstatisticsGroupInvariance2024.md) — further history.
- [waudbysmithEstimatingMeansBounded2020](../sources/waudbysmithEstimatingMeansBounded2020.md), [rufCompositeGeneralizationVille2022](../sources/rufCompositeGeneralizationVille2022.md), [ramdasTestingExchangeabilityForkconvexity2021](../sources/ramdasTestingExchangeabilityForkconvexity2021.md), [wangAnytimevalidTtestsConfidence2023](../sources/wangAnytimevalidTtestsConfidence2023.md) — further history.

## Disagreements / open issues
- Wald 1947 (in the bib) and Wald 1945, Kelly 1956, Robbins 1970, Darling and Robbins 1967, Lai 1976, Shafer and Vovk 2019 and Shafer et al. 2011 (not in the bib) are the primary documents for most of this page; none is ingested yet.
