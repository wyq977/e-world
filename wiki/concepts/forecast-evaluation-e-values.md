---
slug: forecast-evaluation-e-values
title: Forecast evaluation and backtesting with e-values
sources: 4
updated: 2026-10-12
---

# Forecast evaluation and backtesting with e-values

## Definition
Anytime-valid evaluation of sequential probability forecasts and risk forecasts through scoring rules: the score-differential or exceedance process is a martingale in the game filtration, so test supermartingales, e-processes and confidence sequences apply without distributional assumptions on forecasts or outcomes. Two nulls are distinguished: the strong null "no better at any step" (conditional dominance δ_t ≤ 0 for all t) and the weak null "no better on average" (Δ_t ≤ 0 for all t); rejecting the strong null only shows one forecaster was better at some time [henziValidSequentialInference2021, eq. 4; choeComparingSequentialForecasters2021, Sec. 4.4]. Backtesting of risk forecasts uses backtest e-statistics e(x, r, z) with mean at most one when the forecast r is conservative and above one whenever it under-reports [wangEbacktesting2022, Defs 1–2].

## Key results
- Binary forecasts, strong null: all one-observation e-values for the interval null are 1 + λ (S(p, y) − S(q, y))/|S(p, 1{p > q}) − S(q, 1{p > q})|; the GROW e-value is a likelihood ratio with the score-dependent boundary point κ_ν (Brier (p + q)/2) in the denominator, an instance of Safe Testing's Theorem 1; lag-h forecasts average h lagged products; precipitation case study at four airports [henziValidSequentialInference2021, Thms 3.1–3.3, Props 3.4–3.5, Table 1, Sec. 5]; see [gro-criterion](gro-criterion.md).
- Weak null, adversarial Reality: empirical-Bernstein confidence sequence Δ̂_t ± u(V̂_t)/t with any predictable centring and any bounded score; the purely empirical exp{λ Σ δ̂_i − ψ_E(λ) V̂_t} is an e-process dominated by a P-dependent supermartingale; Winkler skill scores handle unbounded proper scores; lag-h via sequential e-values, harmonic p-merging and calibration; Diebold–Mariano and Giacomini–White exceed cumulative type-I error 0.05 after about 100 and 1000 steps; MLB and weather data [choeComparingSequentialForecasters2021, Thms 1–3, Props 1, 3–6, App. H.2, Secs 5.2–5.3].
- Backtesting: the ES–VaR pair has the monotone backtest e-statistic (x − z)_+/((1 − p)(r − z)) from the Rockafellar–Uryasev representation, the quantile 1{x > r}/(1 − p); ES alone is not backtestable (quasi-convexity); every one-sided e-statistic for the mean, variance, VaR and (ES, VaR) is dominated by 1 + h(e − 1); products with predictable λ_t ∈ [0, 1] are test supermartingales at any horizon; betting processes GRO, GREE, GREL and GREM with asymptotic optimality under i.i.d.-type assumptions the authors call "perhaps unrealistic"; AR–GARCH simulations detect 10% under-reported ES in 98.5% of runs; NASDAQ 2005–2021 detections cluster in 2008; a rolling window defeats over-then-under-report gaming [wangEbacktesting2022, Thms 1–5, Props 3–6, Sec. 5.1, Tables 2–5, App. E].
- The e-power term: this version attributes it to Vovk and Wang's nonparametric e-tests, which conflicts with other pages' "coined in e-backtesting"; unresolved without v1 [wangEbacktesting2022, Open questions]; see [e-power](e-power.md).
- Sub-exponential supermartingale for lower-bounded variables with predictable bounds, extending Howard et al. [choeComparingSequentialForecasters2021, Prop. 1]; see [confidence-sequence-boundaries](confidence-sequence-boundaries.md).

## Variants and related concepts
- [testing-by-betting](testing-by-betting.md), [e-process](e-process.md), [e-merging](e-merging.md).

## Sources
- [henziValidSequentialInference2021](../sources/henziValidSequentialInference2021.md) — strong-null forecast dominance.
- [choeComparingSequentialForecasters2021](../sources/choeComparingSequentialForecasters2021.md) — weak-null confidence sequences and e-processes.
- [wangEbacktesting2022](../sources/wangEbacktesting2022.md) — backtest e-statistics.
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — backtest e-statistics in Chapter 16.

## Disagreements / open issues
- Henzi and Ziegel build no confidence sequences and no calibration e-value; the weak-null sequences of Choe and Ramdas fill that gap [henziValidSequentialInference2021, Open questions].
- Casgrain, Larsson and Ziegel on elicitable functionals and Arnold, Henzi and Ziegel on calibration tests are not in the bib.
