---
citekey: wangEbacktesting2022
title: "E-backtesting"
authors: [Qiuqi Wang, Ruodu Wang, Johanna Ziegel]
year: 2022
status: preprint
public: true
note: "The first model-free, non-asymptotic, anytime-valid backtest for Expected Shortfall: backtest e-statistics turn each day's loss and (ES, VaR) forecast into a conditional e-variable, a betting process compounds them into a test supermartingale, and the VaR and ES e-statistics are shown to be essentially the only useful ones."
links:
  pdf: "https://arxiv.org/pdf/2209.00991v6"
  arxiv: "https://arxiv.org/abs/2209.00991"
  doi: "10.48550/arXiv.2209.00991"
  video: ""
tags: [backtesting, expected-shortfall, value-at-risk, risk-measures, backtest-e-statistic, e-process, betting-process, e-power, gro, grapa, identification-function, elicitability, model-free, anytime-valid, finance]
ingested: 2026-10-08
version: "arxiv (2209.00991v6, 15 Apr 2026, 67 pages; published in Management Science 2025)"
---

# E-backtesting

## Summary
Regulators must check sequentially reported risk forecasts, in particular Expected Shortfall (ES), which replaced Value-at-Risk (VaR) in the Basel rules but is not elicitable and had no model-free, non-asymptotic backtest [wangEbacktesting2022, Sec. 1, Table 1]. The paper defines *backtest e-statistics*: functions e(x, r, z) of the realised loss x, the forecast r of the risk measure ρ and the forecast z of auxiliary functionals φ, with mean at most one whenever r ≥ ρ(F) and z = φ(F), and mean above one whenever r < ρ(F), whatever z [wangEbacktesting2022, Defs 1–2]. For the pair (ES_p, VaR_p) the statistic e^ES_p(x, r, z) = (x − z)_+ / ((1 − p)(r − z)) is a monotone backtest e-statistic (Theorem 1), proved in four lines from the Rockafellar–Uryasev representation. A regulator forms X_t = e(L_t, r_t, z_t), chooses a predictable betting process λ_t ∈ [0, γ] and compounds M_t = ∏(1 − λ_s + λ_s X_s); under the null that every day's forecasts are conservative, M is a test supermartingale and Ville's inequality gives anytime-valid type-I control (Theorem 2). Three data-driven betting rules (GREE, GREL, GREM) approximate the oracle GRO rule and are asymptotically optimal under different regimes (Theorem 3). Characterisation theorems show every one-sided e-statistic for the mean, variance, VaR and (ES, VaR) is dominated by a mixture 1 − h + h·e of the constant 1 with the paper's simple e-statistic, so the restricted GRO over λ is the unrestricted GRO (Theorems 4–5, Props 5–6). Simulations on AR–GARCH data and NASDAQ and portfolio data from 2005–2021 show early detection of under-reported ES, especially around the 2008 crisis.

## Main results
- **Definition 1–2, Lemma 1.** Point, one-sided and backtest e-statistics for ψ = (ρ, φ); E[E] > 1 iff E[log(1 − λ + λE)] > 0 for some λ ∈ [0, 1], so a backtest e-statistic always yields positive e-power after shrinkage toward 1 [wangEbacktesting2022, Sec. 3.2].
- **Examples 1–4.** Monotone backtest e-statistics: x/r for a nonnegative mean, (x − z)²/r for (var, E), e^Q_p(x, r) = 1{x > r}/(1 − p) for the p-quantile, (ℓ(x) − a)/(r − a) for an expected loss bounded below [wangEbacktesting2022, Sec. 3.3].
- **Theorem 1.** e^ES_p(x, r, z) = (x − z)_+ / ((1 − p)(r − z)) is a monotone backtest e-statistic for (ES_p, VaR_p); (ES, VaR) is a Bayes pair with loss L(z, x) = z + (x − z)_+/(1 − p) [wangEbacktesting2022, Sec. 3.3, eqs 3–5].
- **Theorem 2.** For any one-sided e-statistic and any predictable λ with values in [0, 1], M_t(λ) in eq. 7 is a nonnegative supermartingale under H_0: r_t ≥ ρ(L_t | F_{t−1}), z_t = φ(L_t | F_{t−1}) for all t; P(sup_t M_t ≥ 1/α) ≤ α for any horizon T, fixed, infinite or adaptive [wangEbacktesting2022, Sec. 4.1].
- **Proposition 1 and Example 5–6.** e^ES_p remains an e-variable when z_t ≥ VaR and r_t − z_t ≥ ES − VaR (eq. 10), which covers lifting the level p to q > p (mean (1 − q)/(1 − p) < 1), common multiplicative factors c_1 ≥ c_2 ≥ 1 and common additive shifts b_1 ≥ b_2 ≥ 0; but over-predicting VaR and ES separately (eq. 11) does not suffice, since E[e^ES_p] = ∞ when r = z = ES and P(L > z) > 0 [wangEbacktesting2022, Sec. 4.2].
- **GRO, GREE, GREL, GREM (eqs 12–14, Sec. 5.1).** GRO maximises E^{Q_t}[log(1 − λ + λ e(L_t, r, z))] over λ ∈ [0, γ] and needs the conditional law Q_t; GREE replaces Q_t by the empirical law of past e-statistics e(L_s, r_s, z_s); GREL by the empirical law of past losses evaluated at the current forecast (r_t, z_t); GREM is the betting process of the average of the GREE and GREL e-processes, which exists by Lemma 1 of Vovk and Wang 2024a. A Taylor approximation gives the closed form λ ≈ 0 ∨ (Σ e − (t−1)) / Σ (e − 1)² ∧ γ (eq. 15); γ = 1/2 is the default and optimal λ for tail risk measures are typically below 0.1 (Remark 7) [wangEbacktesting2022, Sec. 5.1, App. A].
- **Proposition 2.** λ^GRO > 0 iff E^{Q_t}[e | F_{t−1}] > 1, and (with γ = 1) λ^GRO < 1 iff E^{Q_t}[1/e | F_{t−1}] > 1; the same holds for the empirical measures, so GREE/GREL bet only when the empirical mean of the e-statistic exceeds one [wangEbacktesting2022, Sec. 5.2].
- **Definition 3 and Theorem 3.** Betting processes are asymptotically equivalent if (log M_T(λ) − log M_T(λ′))/T → 0 in L¹, and asymptotically optimal if equivalent to GRO. Under Assumption 1 (sup_t E|log e| < ∞) and γ = 1: GREE is optimal when (e(L_t, r_t, z_t)) is iid and the forecasts are deterministic; GREL when (L_t) is iid and the forecasts take finitely many values or converge in a compact set; GREM whenever either is. If r_t < ρ(L_t | F_{t−1}) − ε for all t, all three have asymptotic power one with any backtest e-statistic [wangEbacktesting2022, Sec. 5.2, App. C, Prop. EC.2].
- **Example 7, Figs 1–3.** Simulated co-moving losses and forecasts (linear growth, sinusoidal cycle) favour GREE; iid losses with noisy forecasts favour GREL; GREM tracks the better of the two [wangEbacktesting2022, Sec. 5.2].
- **Propositions 3–4.** A monotone, uncapped ρ admitting a backtest e-statistic must be quasi-convex; a monotone backtest e-statistic forces quasi-linearity (hence convex level sets). This rules out ES on its own information, consistent with Acerbi and Székely 2017 [wangEbacktesting2022, Sec. 6.1].
- **Propositions 5–6, Theorems 4–5.** Every one-sided e-statistic for the mean on [a, ∞), for (var, E), for VaR_p, and (among statistics increasing in the loss) for (ES_p, VaR_p) is bounded above by 1 + h(r, z)(e − 1) for the paper's simple e and some 0 ≤ h ≤ 1; it is a backtest e-statistic iff h > 0, and monotone iff h and r ↦ (r − a)/h (resp. r/h, (r − z)/h) are increasing, with h constant in the VaR case; for ES a second term k(r, z)(p − 1{x ≤ z})/(1 − p) is allowed in the one-sided bound but must vanish for a backtest e-statistic [wangEbacktesting2022, Sec. 6.2]. Hence the restricted GRO of eq. 12 is the unrestricted GRO for these functionals (Remark 6).
- **Proposition EC.1 and App. B.** For a non-conservative backtest e-statistic, (v(x, z), 1 − e(x, r, z)) is an identification function for ψ; a functional with a monotone backtest e-statistic must have an identification function bounded below by −1, which excludes the unrestricted expectation [wangEbacktesting2022, App. B].
- **Simulations (Sec. 7, Tables 2–5).** AR(1)–GARCH(1,1) with skewed-t innovations, 500 days, 1,000 runs, GREM with eq. 15: detections at thresholds 2/5/10 for VaR_0.99 forecasts under-reported by 10% with normal innovations 99.6/98.0/94.3%, for exact true forecasts 15.0/1.7/0.2%; for ES_0.975 under-reported with normal innovations 99.8/99.5/98.5% and 35.5/9.2/3.6% for the true model; early warnings at threshold 2 arrive after roughly a quarter of the horizon and decisive ones at 10 after about half [wangEbacktesting2022, Sec. 7.1].
- **Structural change (Sec. 7.2, Fig. 4).** Against the parametric sequential monitor of Hoga and Demetrescu 2023 (threshold 20 for the e-test versus level 5%), the e-backtests detect fewer breaks and 0–30 days later, attributed to being nonparametric and one-sided [wangEbacktesting2022, Sec. 7.2].
- **Data (Sec. 8, Tables 6–7, Figs 5–7).** NASDAQ 2005–2021: ES_0.975 forecasts with normal innovations reach threshold 10 after 713 days (GREM), skewed-t after 2,889 days, and the 10%-over-reported skewed-t forecasts never; most detections cluster 500–700 days in, during the 2008 crisis. GREL beats GREE except against empirical forecasts; GREM is recommended as the default. Similar results for a 22-stock mean–variance portfolio [wangEbacktesting2022, Sec. 8].
- **Type-I errors (App. D.3, Table EC.6).** For true VaR_0.99 forecasts and 10⁵ days, detection rates at thresholds 2/5/10 are 38.8/14.1/7.1% for GREM, below but near the bounds 50/20/10%, while a traditional backtest evaluated at every sample size rejects 89.7% at nominal 5%. A sequential p-value trajectory (App. D.5, Fig. 8) likewise rejects every forecast, including over-reported ones [wangEbacktesting2022, App. D].
- **Gaming (App. E, Table EC.8).** A bank that over-reports for 1,000 days and then under-reports is detected at threshold 2 after about 250–300 further days with a 500-day rolling window and GREM, because GREE keeps λ near 0 during the over-reporting period and GREL ramps up quickly afterwards [wangEbacktesting2022, App. E].

## Setting and assumptions
- Data: a loss sequence (L_t) adapted to a filtration (F_t) that may contain anything the forecaster used, including randomisation; forecasts (r_t, z_t) are F_{t−1}-measurable and otherwise arbitrary, no time-series model, stationarity or mixing is assumed [wangEbacktesting2022, Sec. 4.1].
- Null: r_t ≥ ρ(L_t | F_{t−1}) and z_t = φ(L_t | F_{t−1}) for every t (eq. 6); for ES the auxiliary equality on VaR can be relaxed to the joint inequality of eq. 10. The alternative is under-forecasting at some t; over-forecasting ES is rewarded by monotone e-statistics, while testing over-estimation of ES is left open (Remark 5).
- The e-statistic must not depend on the law of L ("model-free"); the betting process λ_t ∈ [0, γ] is predictable from past losses and current forecasts and can even be announced after seeing (r_t, z_t) (footnote 4).
- Optional stopping and continuation are allowed: T may be fixed, infinite or data-dependent, and the test stops at min{T, inf{t : M_t ≥ 1/α}} [wangEbacktesting2022, Thm 2, Remark 3].
- Thresholds 2, 5, 10 are used as a multi-zone early-warning scheme analogous to the Basel three-zone test, with only 50%, 20%, 10% nominal type-I guarantees [wangEbacktesting2022, Remarks 3, 9].
- Asymptotic optimality (Theorem 3) needs iid structure in either the e-statistics or the losses, Assumption 1, and γ = 1; the authors call these "strong, and perhaps unrealistic" [wangEbacktesting2022, Sec. 5.2].

## Relation to other sources
- [ramdasHypothesisTestingEvalues2025](ramdasHypothesisTestingEvalues2025.md): Chapter 16 (Defs 16.5–16.6, Thm 16.11) restates backtest e-statistics and the ES–VaR pair from this paper; the book is cited here for the general treatment of e-values.
- [vovkEvaluesCalibrationCombination2021](vovkEvaluesCalibrationCombination2021.md): source of the e-variable definition, the "e-value" name and the evidence thresholds (10 = strong) adopted here [wangEbacktesting2022, Sec. 3.1, Remark 3].
- [grunwaldSafeTesting2024](grunwaldSafeTesting2024.md) and [shaferTestingBettingStrategy2021](shaferTestingBettingStrategy2021.md): GRO and the Kelly/betting reading that the betting process λ_t operationalises [wangEbacktesting2022, Sec. 5.1].
- [waudbysmithEstimatingMeansBounded2020](waudbysmithEstimatingMeansBounded2020.md): GREE/GREL are built on the GRAPA idea (their Sec. B.2) and the universal representation of their Prop. 3; the differences are the use of backtest e-statistics and of forecasts as inputs [wangEbacktesting2022, Secs 4.1, 5.1].
- [wangOnlyAdmissibleWay2024](wangOnlyAdmissibleWay2024.md): its Lemma 2 refines Lemma EC.2 of this paper (domination of functions of a mean-bounded variable by 1 − h + h x/r); and "Vovk and Wang 2024a" (martingale merging) is invoked for the admissibility of the product form eq. 7 and the existence of the GREM betting process.
- [wangFalseDiscoveryRate2021](wangFalseDiscoveryRate2021.md): its Section 2 is cited as the list of reasons for e-values, and the paper's variance e-variable (x − z)²/r echoes the constructions there.
- [villeEtudeCritiqueNotion1939](villeEtudeCritiqueNotion1939.md): Theorem 2 is Ville's inequality applied to eq. 7.
- [ramdasGametheoreticStatisticsSafe2023](ramdasGametheoreticStatisticsSafe2023.md), [wassermanUniversalInference2020](wassermanUniversalInference2020.md): cited for anytime validity and for universal inference as an early use of e-values.
- [haoEValuesExponentialFamilies2025](haoEValuesExponentialFamilies2025.md): credits this paper as the source of the term "e-power"; this paper itself attributes the term to Vovk and Wang (2022, "Efficiency of nonparametric e-tests"; 2024b, "Nonparametric e-tests of symmetry") [wangEbacktesting2022, Secs 3.2, 5.1].
- Mentioned without link: Henzi and Ziegel 2022 (in the bib as henziValidSequentialInference2021; forecast-dependent betting processes, probability forecast evaluation); Casgrain, Larsson and Ziegel 2024 (anytime-valid tests for elicitable functionals via supermartingales); Agrawal, Koolen and Juneja 2021 (confidence sequences for tail risk measures); Nolde and Ziegel 2017 (conditional calibration tests, of which these are anytime-valid analogues); Hoga and Demetrescu 2023 (sequential monitoring benchmark); Du and Escanciano 2017 (cumulative violations); Fissler and Ziegel 2016 (identification functions, Osband's principle); Rockafellar and Uryasev 2002 (ES–VaR variational formula); Kelly 1956.

## Concepts touched
- backtesting-e-statistics (new)
- [E-variable](../concepts/e-variable.md)
- [E-process](../concepts/e-process.md)
- [Test martingale](../concepts/test-martingale.md)
- [Ville's inequality](../concepts/villes-inequality.md)
- [E-power](../concepts/e-power.md)
- [GRO criterion](../concepts/gro-criterion.md)
- [Testing by betting](../concepts/testing-by-betting.md)
- [Mixture and plug-in methods](../concepts/mixture-and-plug-in-methods.md)
- [Optional stopping](../concepts/optional-stopping.md)

## Versions
The ingested file is arXiv v6 (15 April 2026), which postdates the Management Science publication (2025); footnote 12 says the statements and proofs of Lemma EC.1 and Proposition EC.2 (the asymptotic optimality machinery behind Theorem 3) were revised and corrected in April 2026, so Theorem 3's supporting results may differ from the journal version. Section numbering of the e-companion (A–E, Proposition EC.1–EC.2, Lemmas EC.1–EC.5, Tables EC.1–EC.8) follows v6.

## Open questions / gaps
- Testing over-estimation of ES has no method here; the asymmetry is attributed to ES being a one-sided tail functional (Remark 5).
- Theorem 3's optimality holds only under iid structure and γ = 1; "theoretically optimal betting processes using some data-driven procedures under practical assumptions" is named as the main open task (Sec. 9).
- Theorem 5 characterises (ES, VaR) e-statistics only among those increasing in the loss; whether non-monotone one-sided e-statistics for the pair exist that are not dominated is left open.
- The e-backtests lose to parametric sequential monitoring in detection rate and speed under structural change (Fig. 4); the flexibility–power trade-off is acknowledged but not quantified beyond the simulations.
- The wiki's statement that "e-power" was coined in the e-backtesting literature [e-power page] conflicts with this version's own attribution to Vovk and Wang; the v1 of September 2022 is not in `raw/`, so which paper first printed the term cannot be settled from the sources here.
- Cited but not in the bib: Vovk and Wang 2022 (Efficiency of nonparametric e-tests) and 2024b (Nonparametric e-tests of symmetry); Vovk and Wang 2024a (Merging sequential e-values via martingales); Casgrain, Larsson and Ziegel 2024; Agrawal, Koolen and Juneja 2021; Nolde and Ziegel 2017; Hoga and Demetrescu 2023; Shafer, Shen, Vereshchagin and Vovk 2011; Darling and Robbins 1967; Jang, Jun, Kuzborskij and Orabona 2023 (coin-betting posterior on λ).
