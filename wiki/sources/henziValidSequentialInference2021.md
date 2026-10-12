---
citekey: henziValidSequentialInference2021
title: "Valid sequential inference on probability forecast performance"
authors: [Alexander Henzi, Johanna F. Ziegel]
year: 2021
status: preprint
public: true
note: "The first application of e-values to forecast comparison: for binary-event probability forecasts and any consistent scoring rule, a one-observation e-value for conditional forecast dominance is characterised exactly, its GROW version is a likelihood ratio with the score's mixing measure in the denominator, products give a test supermartingale valid under optional stopping, and a precipitation case study agrees with Diebold-Mariano tests."
links:
  pdf: "https://arxiv.org/pdf/2103.08402"
  arxiv: "https://arxiv.org/abs/2103.08402"
  doi: "10.48550/arXiv.2103.08402"
  video: ""
tags: [forecast-evaluation, proper-scoring-rules, forecast-dominance, conditional-predictive-ability, brier-score, test-supermartingale, grow, optional-stopping, anytime-valid-p-value, u-statistic-merging, lag-h, diebold-mariano, weather-forecasting, application]
ingested: 2026-10-08
version: "arxiv (2103.08402v3, 1 Jul 2022, 26 pages; published Biometrika 2022, not in this file)"
---

# Valid sequential inference on probability forecast performance

arXiv 2103.08402v3 (stat.ME), dated July 4, 2022; 26 pages including proofs (Appendix A), robustness figures (Appendix B) and untruncated case-study tables (Appendix C). Published in Biometrika in 2022. An R package `eprob` and replication material are on GitHub (Section 4.1). The authors thank Ruodu Wang for introducing them to e-values.

## Summary
A forecast user compares two probability forecasts p_t, q_t ∈ (0,1) for a binary event Y_{t+h}, issued h ≥ 1 steps ahead, with a consistent scoring function S (Brier, logarithmic, spherical, or any member of the Schervish mixture representation S = ∫ S_θ dν(θ)) [henziValidSequentialInference2021, Sec. 2.1, eqs. 2–3]. The null of conditional forecast dominance, in the sense of Giacomini and White, is that E[S(p_t, Y_{t+h}) − S(q_t, Y_{t+h}) | F_t] ≤ 0 at every t, optionally only at times where an F_t-measurable condition c_t = 1 holds; a stronger null asks for dominance under all elementary scores S_θ simultaneously [henziValidSequentialInference2021, eqs. 4–5]. The paper's main contribution is a complete characterisation of one-observation e-values for the single-score null: they are exactly 1 + λ × (score difference) / |score difference at y = 1{p > q}| for λ ∈ (0,1] (Theorem 3.1), the GROW member against alternative probability π_1 is a likelihood ratio whose denominator is the ν-average κ_ν of θ over [min(p,q), max(p,q)) (Theorem 3.2), and under the all-scores null the GROW e-value is the plain likelihood ratio against the forecast p (Theorem 3.3) [henziValidSequentialInference2021]. In the sequential setting with lag h = 1 the running product of these e-values with adapted λ_t is a nonnegative test supermartingale; for lag h > 1 the h lagged products are averaged, U-statistic style, and the resulting process is an e-value at every stopping time shifted by h − 1 (Propositions 3.4–3.5) [henziValidSequentialInference2021, Sec. 3.2]. Simulations show the t-test rejecting at rate 0.12–0.15 under optional stopping at level 0.05 while the e-values stay valid at a power cost, and a case study on probability-of-precipitation postprocessing (IDR vs HCLR, four airports, lags 1–5, ten years of ECMWF data) reaches the same qualitative conclusions as Diebold–Mariano and Ehm–Krüger dominance tests [henziValidSequentialInference2021, Secs 4–5].

## Main results
- **Theorem 3.1** (characterisation): for consistent S with ν([min(p,q), max(p,q))) > 0 and p ≠ q, E(y) is an e-value with null H_S = {π : E_π[S(p,Y) − S(q,Y)] ≤ 0} and alternative its complement iff E(y) = E_{p,q;λ}(y) = 1 + λ (S(p,y) − S(q,y)) / |S(p,1{p>q}) − S(q,1{p>q})| for some λ ∈ (0,1] [henziValidSequentialInference2021, eq. 6]. The proof solves the two linear constraints E_π[E] ≤ 1 with equality at the boundary π_0 of H_S [Appendix A.1, eqs. 8–10].
- **H_S is an interval**: for p < q, H_S = [0, κ_ν([p,q))] with κ_ν([a,b)) = ∫_{[a,b)} θ dν(θ) / ν([a,b)); for the all-scores null H = [0, p] (mirror images for p > q) [henziValidSequentialInference2021, Sec. 3.1].
- **Theorem 3.2** (GROW): E_{π_1}[log E_{p,q;λ}] is maximised at λ = π_1 + (1 − π_1)(S(p,0) − S(q,0))/(S(p,1) − S(q,1)) for p < q (symmetric formula for p > q), giving E^{π_1}_{p,q}(0) = (1 − π_1)/(1 − κ_ν), E^{π_1}_{p,q}(1) = π_1/κ_ν with κ_ν = κ_ν([min(p,q), max(p,q))); the authors note this also follows from Theorem 1 of Safe Testing because κ_ν is the boundary of H_S [henziValidSequentialInference2021, Thm 3.2 and remark].
- **Table 1**: κ_ν([p,q)) for p < q is (p+q)/2 for the Brier score (ν density 2), log((1−p)/(1−q)) / log(q(1−p)/(p(1−q))) for the logarithmic score (density θ^{−1}(1−θ)^{−1}), and ((q−1)‖p‖ − (p−1)‖q‖)/((2q−1)‖p‖ − (2p−1)‖q‖) for the spherical score [henziValidSequentialInference2021, Table 1].
- **Theorem 3.3** (all scoring rules): the GROW e-value for H = [0,p] (or [p,1]) against π_1 ∉ H is the likelihood ratio E^{π_1*}_{p,q}(y) = (1−π_1)/(1−p) for y = 0 and π_1/p for y = 1; it does not depend on q except through the admissible alternatives [henziValidSequentialInference2021, Thm 3.3].
- **Proposition 3.4** (sequential, lag h): with (Y_t, c_t, p_t, q_t, λ_t) adapted, λ_t = 0 whenever c_t = 0, and S strictly consistent, e_T = (1/h) Σ_{k=1}^h Π_{l ∈ I_k} E_{p_l,q_l;λ_l}(Y_{l+h}) with I_k = {k + hs : s = 0, …, ⌊(T−k)/h⌋ − 1} is an e-value under H_{S;c} for every T ≥ h + 1; for h = 1 the product Π_{j ≤ t} E_{p_j,q_j;λ_j}(Y_{j+1}) is a nonnegative supermartingale [henziValidSequentialInference2021, Sec. 3.2].
- **Proposition 3.5** (optional stopping): for any stopping time τ, E_Q[e_{τ+h−1}] ≤ 1 for Q ∈ H_S; proved by writing e_t as an average of h supermartingales M^{[k]} in sub-filtrations F^{[k]} and showing f_k(τ) ∈ {τ, …, τ + h − 1} is an F^{[k]}-stopping time [henziValidSequentialInference2021, Appendix A.1].
- **Stopping rules and anytime-valid p-values**: τ_α = min{T, inf(t ≥ 2 : e_t ≥ 1/α)} for h = 1; for h > 1, τ_{α,h} stops when e_t ≥ max_{j=t−h+1,…,t−1} E_{p_j,q_j;λ_j}(1{p_j > q_j})^{−1}/α, which guarantees e_{t+h−1} ≥ 1/α whatever the h − 1 pending outcomes are (Appendix A.2); anytime-valid p-values p_{t_0} = min{1, inf_{s ≤ t_0} 1/e_s} for h = 1, with the same correction factor for h > 1 [henziValidSequentialInference2021, Sec. 3.2].
- **Simulation 4.1** (Brier, T = 600, α = 0.05): one-sided t-test with optional stops at 150, 300, 450 rejects at rate 0.12 at the null boundary (up to 0.15 in the introduction's summary); the stopped e-value e_{τ_0.05} is uniformly more powerful than e_T; heuristic alternatives η_t(ξ) = ξ(p_t+q_t)/2 + (1−ξ)q_t, averaged over k = 5 values of ξ, nearly match the oracle alternative π_t and beat η_t = q_t; the oracle π_t has lower power than the heuristics near the boundary because growth-rate optimality is not finite-sample threshold power [henziValidSequentialInference2021, Fig. 1].
- **Simulation 4.2** (moving-average time series, lags 1–3): e-values lose power relative to Diebold–Mariano, more so at lags 2–3 where the averaging merger is weaker; Diebold–Mariano is valid there only because the forecasts are ideal and the process stationary [henziValidSequentialInference2021, Fig. 2].
- **Case study** (Section 5): HCLR does not beat IDR at lags 1–3 but gives substantial-to-strong evidence (E = 4.8–17) at lags 4–5 for Brussels and Zurich; IDR beats HCLR⁻ at lags 1–3 (E > 100); HCLR beats HCLR⁻ at short lags, with the Brussels lag-1 case E > 100 (1.3 × 10²) yet Diebold–Mariano p = 0.07, attributed to the e-value's smaller null (dominance at every t) accumulating a mean Brier difference of 0.001; conditional tests c_t = 1{max(p_t,q_t) ≥ 0.5} for extreme-precipitation warnings use the all-scores null and give E = 3703 for Brussels lag 1 and little evidence elsewhere; evidence read on the Vovk–Wang scale 3.16/10/31.6/100 [henziValidSequentialInference2021, Tables 2–4, Fig. 3].

## Setting and assumptions
- Data: (Y_t, p_t, q_t) adapted to a filtration (F_t) on a probability space with unknown law Q; forecasts p_t, q_t ∈ (0,1) are for Y_{t+h}, lag h ≥ 1 fixed; no stationarity, independence or model assumptions [henziValidSequentialInference2021, Sec. 2.2].
- Null H_{S;c}: conditional (given F_t) expected score difference ≤ 0 at all t with c_t = 1, c_t ∈ {0,1} F_t-measurable; H_c: the same under all elementary scores S_θ. The authors stress these nulls are strong (dominance at every time point), so the tests suit comparing a new method to a benchmark; Diebold–Mariano and dominance tests have larger nulls (average score difference ≤ 0) [henziValidSequentialInference2021, Secs 2.2, 5.2].
- Alternative: the user must specify an alternative probability η_t (or λ_t) adaptively; heuristic convex mixtures between (p_t + q_t)/2 and q_t are recommended, and 0.25 p_t + 0.75 q_t is used in the case study [henziValidSequentialInference2021, Secs 4.1, 5.2].
- Optional stopping: fully allowed for h = 1; for h > 1 the stopped e-value depends on h − 1 pending outcomes, handled by the conservative rule τ_{α,h} and Proposition 3.5 [henziValidSequentialInference2021, Sec. 3.2].
- Scoring functions require ν to charge [min(p,q), max(p,q)) (Theorem 3.1) or strict consistency (Proposition 3.4). Power is below fixed-sample tests, which the authors accept as the price of anytime validity [henziValidSequentialInference2021, Sec. 1].

## Relation to other sources
- [grunwaldSafeTesting2024](grunwaldSafeTesting2024.md): Theorems 3.2–3.3 are instances of Theorem 1 there (GROW = likelihood ratio against the boundary point of the null, the reverse information projection of a Bernoulli alternative onto an interval null); the paper cites the 2020 ITA version [henziValidSequentialInference2021, Secs 3.1, A.1].
- [shaferTestingBettingStrategy2021](shaferTestingBettingStrategy2021.md): the betting score terminology, Kelly growth and the reading of a product of e-values as accumulated capital are taken from there [henziValidSequentialInference2021, Sec. 3.1].
- [vovkEvaluesCalibrationCombination2021](vovkEvaluesCalibrationCombination2021.md): source of the term e-value, of the U-statistic merging that motivates the lag-h averaging in Proposition 3.4, and of the discrete evidence scale used to read Tables 2–3 [henziValidSequentialInference2021, Secs 1, 3.2, 5.2].
- [ramdasAdmissibleAnytimevalidSequential2022](ramdasAdmissibleAnytimevalidSequential2022.md): cited (as the 2020 arXiv) for the supermartingale analysis behind Proposition 3.5 and for anytime-valid p-values [henziValidSequentialInference2021, Secs 1, 3.2].
- [waudbysmithEstimatingMeansBounded2020](waudbysmithEstimatingMeansBounded2020.md): Proposition 2 there has the same 1 + λ × (centred increment) form as eq. 6; also cited for the power cost of time-uniform versus fixed-sample inference [henziValidSequentialInference2021, Secs 1, 3.1].
- [wangFalseDiscoveryRate2021](wangFalseDiscoveryRate2021.md): cited for e-value FDR control as the route to comparing forecasts across many grid locations, not pursued in the paper [henziValidSequentialInference2021, Sec. 1].
- choeComparingSequentialForecasters2021 (in the bib, no source page yet): the sibling paper that builds confidence sequences and e-processes for average score differences of general sequential forecasters; the present paper instead tests conditional dominance at every time point for binary forecasts and uses the exact GROW form of the single-step e-value.
- Without a page: Giacomini and White 2006 (conditional predictive ability, the null adopted here); Diebold and Mariano 1995; Ehm and Krüger 2018 (forecast dominance testing via sign randomisation, Hs hypothesis and the lag-1 comparison test); Schervish 1989 and Gneiting et al. 2007 (elementary-score representation); Seillier-Moiseiwitsch and Dawid 1993 and Lai, Gross and Shen 2011 (martingale-based forecast evaluation); Zhu and Timmermann 2020 (equal conditional accuracy is basically never satisfied).

## Concepts touched
- forecast-evaluation-e-values (new)
- [E-variable](../concepts/e-variable.md): Theorem 3.1 characterises all one-observation e-variables for an interval null on a Bernoulli parameter.
- [GRO, GROW, REGROW and log-optimality](../concepts/gro-criterion.md): Theorems 3.2–3.3, κ_ν as the boundary point of the null.
- [Test martingale](../concepts/test-martingale.md): the h = 1 product is a test supermartingale; the lag-h construction averages h supermartingales in sub-filtrations.
- [E-process](../concepts/e-process.md): Proposition 3.5 and the anytime-valid p-values for h = 1 and h > 1.
- [Optional stopping and sequential decomposability](../concepts/optional-stopping.md): the t-test's 0.12–0.15 rejection rate under stopping, the stopping rules τ_α and τ_{α,h}, and the remark that stopping equals setting future λ_t = 0.
- [Testing by betting](../concepts/testing-by-betting.md): the capital interpretation of products, Kelly betting, and the observation that GROW does not imply optimal finite-sample threshold power.
- [Merging e-values and p-values](../concepts/e-merging.md): the lag-h U-statistic-style averaging of h products, with its power loss at higher lags.
- [Mixture and plug-in methods for composite alternatives](../concepts/mixture-and-plug-in-methods.md): adapted alternatives η_t and averaging over k heuristic mixing weights ξ_j.

## Versions
arXiv v3 (July 2022) is the file here; it is dated after acceptance and matches the Biometrika 2022 article in structure as far as the authors indicate. No material differences are known.

## Open questions / gaps
- Extending the characterisation of Theorem 3.1 beyond binary-event forecasts to score differences for general probabilistic forecasts is left open; the authors point to the bounded-mean betting representation as the likely route [henziValidSequentialInference2021, Sec. 3.1].
- The lag-h average merger loses power relative to the h = 1 supermartingale (Figs 2, 10 and Table 2); a better merging of overlapping lagged products is not given.
- The alternative η_t must be chosen by the user; only heuristics (convex mixtures, averaging over k weights) are offered, and the oracle alternative is not power-optimal at a fixed threshold.
- Testing calibration itself (p_t = P(Y_{t+h} = 1 | F_t)) is mentioned only as the canonical member of the null; no calibration e-value is constructed.
- FDR control across many locations via e-BH is suggested but not carried out.
- Cited works not in the bib: Giacomini and White 2006; Diebold and Mariano 1995; Ehm and Krüger 2018; Yen and Yen 2021; Schervish 1989; Gneiting, Balabdaoui and Raftery 2007; Seillier-Moiseiwitsch and Dawid 1993; Lai, Gross and Shen 2011; Vovk and Wang 2020 (true and false discoveries with independent e-values); Zhu and Timmermann 2020; Patton 2020; Henzi, Ziegel and Gneiting 2021 (isotonic distributional regression, the case-study data).
