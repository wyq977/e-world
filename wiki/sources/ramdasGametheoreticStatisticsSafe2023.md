---
citekey: ramdasGametheoreticStatisticsSafe2023
title: "Game-theoretic statistics and safe anytime-valid inference"
authors: [Aaditya Ramdas, Peter Grünwald, Vladimir Vovk, Glenn Shafer]
year: 2023
status: published
public: true
note: "The four-author Statistical Science survey that fixed the vocabulary of safe anytime-valid inference (e-value, test martingale, e-process, confidence sequence, testing by betting) and catalogued the composite-null constructions, from universal inference and the RIPr to nonparametric supermartingales and e-detectors, ending with a list of open problems."
links:
  pdf: ""
  arxiv: "https://arxiv.org/abs/2210.01948"
  doi: "10.1214/23-STS894"
  video: ""
tags: [survey, savi, e-process, test-martingale, confidence-sequence, testing-by-betting, villes-inequality, universal-inference, reverse-information-projection, gro, nonparametric, change-detection, e-bh, history, open-problems]
ingested: 2026-10-08
version: "publisher-oa (Statistical Science 38(4):576-601, Nov 2023; arXiv 2210.01948)"
---

# Game-theoretic statistics and safe anytime-valid inference

Statistical Science 38(4), 576–601 (2023). A 26-page survey by the four people most associated with the modern e-value literature (Ramdas, Grünwald, Vovk, Shafer). No new theorems; its value is that it fixes definitions, names the general principles, and sorts the 2017–2023 literature into a few construction patterns. All claims below are attributed to [ramdasGametheoreticStatisticsSafe2023] unless another citekey is given.

## Summary
Safe anytime-valid inference (SAVI) is defined as the programme of producing measures of evidence (e-processes for testing) and certainty (confidence sequences for estimation) that remain valid at every stopping time, so that continuous monitoring, optional stopping and optional continuation "for any reason" are permitted (Abstract, Sec. 1.2) [ramdasGametheoreticStatisticsSafe2023]. The technical heart is the test martingale, a nonnegative martingale started at one, read game-theoretically as the wealth of a Skeptic betting against Forecaster's probabilities: under the null no betting strategy can reliably make money, under the alternative a smart bettor can, and the wealth itself is the evidence ("testing by betting", Sec. 1.2) [ramdasGametheoreticStatisticsSafe2023]. Section 2 defines e-values, test (super)martingales, composite test martingales, e-processes (two equivalent definitions), Ville's theorem and inequality, sequential tests, anytime-valid p-values, confidence sequences, and averaging and multiplication of e-values. Section 3 gives the design principles: likelihood ratios are GRO for simple-vs-simple (Kelly/Breiman), plug-in and mixture methods for composite alternatives, REGROW/GROW for choosing a prior, and for composite nulls universal inference (always an e-process) versus the reverse information projection (always an e-value, sometimes an e-process, and then dominating UI). Sections 4 and 5 catalogue parametric examples (monotone-LR and logrank, the t-test and group invariance, conditional e-values, independence and k-sample tests) and nonparametric case studies (sub-Gaussian, heavy-tailed and bounded means, symmetry, exchangeability and log-concavity, convex functionals via reverse submartingales, change detection, asymptotic confidence sequences). Section 6 covers e-BH, e-BY, ALL-IN meta-analysis and "e-hacking"; Section 8 and the appendices give connections to Bayes, MDL and online learning, four open problems, and a discussion of whether SAVI "comes at a price".

## Main results

### Definitions fixed (Section 2)
- **E-variable / e-value** (Sec. 2.1): a nonnegative random variable E with E_P[E] ≤ 1 for all P in the null P; its realised value is the e-value. When E_P[E] = 1 it is a "unit bet against P"; a unit bet against a single P is exactly a likelihood ratio dQ/dP for some Q (q := E·p is a density) [ramdasGametheoreticStatisticsSafe2023].
- **Test (super)martingale** (Sec. 2.2, eqs. 2–5): a (super)martingale that is nonnegative with M_0 = 1. For a simple P every test martingale is a likelihood ratio process q(X^t)/p(X^t) with Q ≪ P (eq. 4), decomposed into conditional unit bets B_t = q(X_t|X^{t-1})/p(X_t|X^{t-1}) (eq. 5); choosing a test martingale "comes down to choosing an alternative Q". By optional stopping E_P[M_τ] ≤ 1 for any τ, so M_τ is an e-value.
- **Composite test martingale** (Sec. 2.3): a test martingale for every P in P simultaneously; it decomposes as q_P(X^t)/p(X^t) for a P-dependent Q_P (Ramdas et al. 2020, Prop. 4), i.e. composite test martingales are "simultaneous likelihood ratios". Nontrivial means not constant or decreasing; for rich P none may exist.
- **E-process** (Sec. 2.4, eqs. 6–7): a nonnegative process E with E_t ≤ M^P_t for every P in P, for some test martingale family (M^P); equivalently (Grünwald–de Heide–Koolen's implicit definition) E_P[E_τ] ≤ 1 for all stopping times τ and P in P. Ramdas et al. (2020) proved the equivalence and that for "locally dominated" P admissible e-processes satisfy E_t = ess inf_P M^P_t (eq. 7). Game reading: minimum wealth across parallel games against each P in P. The running maximum is not an e-process but a "lookback calibrator" fixes it (Shafer et al. 2011, Dawid et al. 2011).
- **Ville's theorem and inequality** (Sec. 2.5, eqs. 8–10): P(A) < ε iff some test martingale for P exceeds 1/ε on A (Ville's theorem; composite version by Ruf et al. 2022 needs e-processes). P(sup_t M_t ≥ α) ≤ 1/α (eq. 8); for an e-process, sup_P P(∃t : E_t ≥ 1/α) ≤ α (eq. 9), equivalently P(E_τ ≥ 1/α) ≤ α for all τ (eq. 10, by Howard et al. 2021a Lemma 3). Equality holds for continuous-path martingales such as exp(λB_t − tλ²/2); in discrete time looseness is "overshoot", a second-order effect. Wang & Ramdas (2023a) extend Ville to nonintegrable supermartingales from improper priors.
- **Sequential test** (Sec. 2.6, eq. 11): an increasing 0–1 process ψ with P(∃t : ψ_t = 1) ≤ α; ψ_t := 1(sup_{s≤t} M_s ≥ 1/α) is one. Contrasted with Wald's SPRT (prespecified stopping rule, may accept) and aligned with Darling–Robbins power-one tests.
- **Anytime-valid p-value** (Sec. 2.7): a process with P(p_τ ≤ u) ≤ u for all τ, P, u; 1/max_{s≤t} M_s is one. The paper treats sequential tests and AV p-values as "secondary and derivative" of e-processes.
- **Confidence sequence** (Sec. 2.8, eq. 12): (C_t) with P(∀t : φ(P) ∈ C_t) ≥ 1 − α, equivalently coverage at every stopping time; built by inverting a test martingale family, C_t := {θ : M^θ_t < 1/α}.
- **Averaging and multiplying** (Secs. 2.9–2.10, eq. 13): convex combinations of arbitrarily dependent e-values are e-values (weights chosen before data; admissible per vovkEvaluesCalibrationCombination2021); products of conditionally valid e-values E[S_t | F_{t-1}] ≤ 1 form a test supermartingale.

### General principles (Section 3)
- **Simple vs simple** (Sec. 3.1, eq. 14): dQ/dP maximises E_Q[log E_τ] for every stopping time τ (Gibbs' inequality); this is grunwaldSafeTesting2024's GRO criterion. Reasons for the log: compounding/LLN (Kelly 1956), Breiman (1961) exponent optimality and asymptotic (α → 0) minimal expected hitting time of 1/α via Wald's identity, and no "betting the farm" (an e-process hitting zero can never recover).
- **Composite alternative** (Sec. 3.2): plug-in method (Wald 1947 eq. 10.10; Robbins–Siegmund 1974; Dawid prequential; Rissanen predictive MDL; never raw MLE on discrete data, smooth it), mixture method (not a special case of plug-in because Q̄ ∉ Q unless Q is "fork-convex"), Bayes factors as mixture martingales (R updated by Bayes' rule gives the same numerator; correspondence breaks for composite nulls), and REGROW (eq. 15 with γ = 1) versus GROW (γ = 0): maximise inf_Q E_Q[log M_τ − γ log M^Q_τ]. Jeffreys' prior is asymptotically REGROW for i.i.d. exponential families with simple null. GRAPA (Waudby-Smith & Ramdas 2023) targets the growth of a smoothed empirical alternative instead.
- **Composite null** (Sec. 3.3): universal inference E^UI_t = q̄(X^t)/sup_P p(X^t) (eq. 16) is always an e-process, a "middle ground" between the GLR and the composite Bayes factor, neither of which is an e-process in general. RIPr: for each τ a unique sub-probability P^τ attaining inf_W D(Q̄^τ ‖ P^τ_W) (eq. 17), and q̄/p^τ is the GRO e-variable among functions of X^τ (grunwaldSafeTesting2024 Thm 1, after Li 1999). The sequence of RIPr e-variables is sometimes an e-process (then E^UI_t ≤ E^RIPr_t with the same numerator) and sometimes not; in k-sample tests it is one for a fixed point alternative but not for a learned Q̄, so one mixes e-processes directly, E^R_τ := ∫ E^λ_τ dR(λ) (Sec. 3.3.3).

### Parametric examples (Section 4)
- **Monotone LR and logrank** (Sec. 4.1.1): for a 1-d exponential family with null θ ≤ θ_0 and alternative θ_1 > θ_0, the GRO e-variable is the simple likelihood ratio ∏ p_{θ_1}/p_{θ_0} (grunwaldSafeTesting2024 Example 4); it needs only MLR, hence also for noncentral t and for terSchureAnytimevalidLogrankTest2024's logrank martingale (hazard ratio θ ≤ θ_max < 1 vs θ ≥ 1, Bernoulli event-allocation per event time). Cox regression with covariates: efficient implementation "a work in progress".
- **t-test and group invariance** (Sec. 4.1.2, eq. 18): coarsen to V_i := X_i/|X_1|; the scale-free likelihood ratio p_{δ_1}(V^t)/p_{δ_0}(V^t) is a test martingale in the coarsened filtration, equals the right-Haar (1/σ) Bayes factor on the original data (Cox 1952; Rushton 1950; Lai 1976a used it anytime-valid and inverted it), and is simultaneously GROW and REGROW for all τ and every γ because E[log E^RIPr] is constant in σ (Pérez-Ortiz et al. 2022). With a heavy-tailed prior on δ it is the Jeffreys/Rouder Bayesian t-test, which thereby acquires type-I safety. Extends to location, rotation and affine groups (regression).
- **Conditional e-values** (Sec. 4.1.3, eq. 19): with Z sufficient under the null, q(Y|Z)/p(Y|Z) is an e-variable (Wald 1945's sequential 2×2 test), but usually not (RE)GRO(W) for exponential-family nulls (Hao et al. 2023, i.e. haoEValuesExponentialFamilies2025 line).
- **Parametric alternative, nonparametric null** (Sec. 4.2, eq. 20): for independence of Y from X with known X-law R, s_q(X,Y) := q(Y|X)/∫q(Y|x)dR(x) is an e-variable, and its denominator is the RIPr, so s_q is GRO for the point alternative q (Grünwald–Henzi–Lardy 2023); extends to model-X conditional independence, and "flattened" to k data streams for turnerGenericEvariablesExact2024's exact k-sample tests, turnerExactAnytimevalidConfidence2023's bounded-effect confidence sequences, and a safe Cochran–Mantel–Haenszel test.

### Nonparametric case studies (Section 5, cases A–D)
The section is organised by four phenomena: (A) test martingales for composite nonparametric P without a common reference measure, (B) test supermartingales where no martingales exist, (C) e-processes where no supermartingales exist, (D) confidence sequences from reversed submartingales.
- **Sub-Gaussian means (B)** (Sec. 5.1, eqs. 21–22): exp(λΣ(X_i − μ) − λ²σ²t/2) is a test supermartingale (Darling–Robbins 1968); a Gaussian mixture over λ gives the closed-form CS Y_t/t ± σ√((tρ²+1)/(t²ρ²) · log((tρ²+1)/α²)), scaling σt^{-1/2}√(log t + log α^{-1}); √log log t is attainable with mixing densities unbounded at 0 (howardTimeuniformNonparametricNonasymptotic2021). Predictable λ_i also work.
- **Heavy tails (B)** (Sec. 5.2): Catoni-style exp(Σφ(λ(X_i − μ)) − λ²σ²t/2) with φ(x) = ±log(1 ± x + x²/2) is a test supermartingale under a conditional variance bound; the resulting CSs look "almost identical" to sub-Gaussian ones.
- **Bounded means (A)** (Sec. 5.3, eqs. 23–24): sub-exponential supermartingale with ψ(λ) = −log(1−λ) − λ and empirical variance Σ(X_i − μ̂_i)²; and the betting martingale K^μ_t = ∏(1 + λ^μ_i(X_i − μ)), a genuine test martingale for the bounded class, the "most statistically powerful" route (Hendriks 2018; Waudby-Smith & Ramdas 2023; Orabona & Jun 2021 via universal portfolios).
- **Symmetry (A)** (Sec. 5.4, eq. 25): de la Peña's exp(λΣX_i − λ²ΣX_i²/2) is a test supermartingale but inadmissible; M is an admissible test martingale iff its unit bets B_t − 1 are odd functions of X_t, and mirroring g gives a strictly better martingale (Ramdas et al. 2020).
- **Exchangeability and log-concavity (C)** (Sec. 5.5): binary exchangeability has no nontrivial test supermartingale in the data filtration yet a powerful UI e-process (Ramdas et al. 2022); shrinking the filtration to conformal p-values restores test martingales (Vovk 2021), less powerful in the binary case. Log-concave densities: no test supermartingale, but a UI e-process (Gangrade–Rinaldo–Ramdas 2023). Some nulls admit no nontrivial e-process at all (Ruf et al. 2022).
- **Convex functionals (D)** (Sec. 5.6): φ(P̂_t) is a reverse submartingale in the exchangeable filtration for convex φ, with a reverse Ville inequality, giving CSs for entropy, divergences, Gaussian-process suprema, U-statistics (Manole & Ramdas 2023); a game-theoretic interpretation is "unknown".
- **Change detection** (Sec. 5.7): an e-detector is a nonnegative M with E_P[M_τ] ≤ E_P[τ]; summing e-processes started at each time gives one, with ARL ≥ 1/α at τ* = inf{t : M_t ≥ 1/α} and near-optimal delay log(1/α)/D(P‖Q) in parametric cases, recovering Shiryaev–Roberts (Shin–Ramdas–Rinaldo 2022); backward confidence sequences handle unspecified pre/post classes.
- **Asymptotic CSs** (Sec. 5.8): defined by symmetric-difference-to-a-true-CS vanishing faster than √(log log t / t); eq. 22 with σ̂_t is universal under 2+ moments, giving a time-uniform CLT and doubly-robust CSs for the ATE (Waudby-Smith et al. 2021).
- **Others** (Sec. 5.9): exponential supermartingale compendium exp(λ·sum_t − ψ(λ)·variance_t) as "the" nonparametric generalisation of the exponential-family likelihood ratio; quantile and DKW-type CSs; sequential two-sample and independence testing by betting; sampling without replacement and election audits.

### Multiple testing and meta-analysis (Section 6)
- ALL-IN meta-analysis multiplies study-level unit bets, safe under optional continuation even when RIPr gives no outcome-level e-process; interleaving studies needs study-level e-processes (Sec. 6.1).
- e-BH: reject the k* largest e-values with k* = max{k : e_[k] ≥ K/(kα)}; FDR ≤ α under arbitrary dependence, also for any S e-values all ≥ K/(Sα), and for stopped e-processes in bandit multiple testing (Sec. 6.2). e-values as unnormalised weights in weighted-p FDR methods.
- e-BY: reporting (1 − α|S|/K) e-CIs controls FCR under any dependence and any selection rule; every CI becomes an e-CI via a calibrator f (nonincreasing, ∫f = 1) at level α' = f^{-1}(1/α) (Sec. 6.3).
- "e-hacking" (Sec. 6.4): peeking is legitimised, reporting the best of many betting strategies is not; the GRO analysis identifies Shafer's "implied alternative", usable at preregistration.

### History as told by the paper
- Sampling to a foregone conclusion: Feller 1940 (ESP), Anscombe 1954, Robbins 1952; 56% of surveyed psychologists admitted to it (John et al. 2012); the "power posing" retraction (Sec. 1).
- Sequential analysis launched by Wald, Anscombe, Robbins in the 1940s–50s; confidence sequences and power-one tests by Robbins, Darling, Siegmund, Lai stayed a niche until about 2017, when generic composite-null proposals appeared "almost out of the blue" (Secs. 1, 1.2). Barnard's 1947 review of Wald asked for statisticians embedded in sequential deliberation, which the game-theoretic view captures better than a prespecified stopping rule.
- Ville (1939) formulated test martingales (calling them martingales), proved Ville's theorem and the "theorem of gamblers' ruin" (Ville's inequality) (Sec. 2.5) [villeEtudeCritiqueNotion1939]. The method of mixtures runs Ville 1939, Wald 1945/1947, Robbins 1970, Cover 1974; plug-in from Wald 1947 (eq. 10.10) via Robbins–Siegmund 1974, Dawid 1984, Rissanen 1984. Log-optimality from Kelly 1956 and Breiman 1961.
- The sequential t-test by marginalisation (Rushton 1950; Cox 1952 as right-Haar Bayes factor; Lai 1976a first anytime-valid use) and sequential 2×2 by conditioning (Wald 1945) prefigure the reduction-to-simple-null strategy (Sec. 4.1). Darling–Robbins 1967/1968 supply the sub-Gaussian supermartingale and the first quantile CSs. Group-sequential/α-spending methods share the 1970s roots but require prespecified sample size and look times (Sec. 8.1.2).
- Testing by betting "arguably has roots dating back (at least) to Ville"; point-null treatment in Shafer et al. 2011 and shaferTestingBettingStrategy2021; composite nulls in grunwaldSafeTesting2024 and Waudby-Smith & Ramdas 2023 (Sec. 1.2). The "sub-ψ process" of Howard et al. 2020 and the implicit definition in Grünwald–de Heide–Koolen are named as the two origins of the e-process definition (Sec. 2.4).

### Open problems (Section 8.2)
1. **Existence**: for which P are there nontrivial (a) test martingales, (b) only test supermartingales, (c) only e-processes, (d) nothing? Separations known from Ramdas et al. 2022 and Ruf et al. 2022; convex-geometry/optimal-transport progress in Zhang–Ramdas–Wang 2023 (Sec. 8.2.1).
2. **Choice of filtration**: coarsening trades safety (fewer stopping times are covered) for power or existence; conformal martingales for exchangeability, and Pérez-Ortiz et al.'s group-invariance martingales, which are not e-processes in the original filtration yet maximise growth among all e-processes. When does coarsening help? (Sec. 8.2.2).
3. **Admissibility**: necessary (E_t = inf_P M^P_t under a dominating measure) and sufficient conditions in Ramdas et al. 2020 do not match; UI has the infimum form yet is sometimes inadmissible; external randomisation changes the picture (Ramdas & Manole 2023) (Sec. 8.2.3).
4. **RIPr**: when does per-t RIPr yield an e-process rather than a sequence of e-variables; how much is lost by substituting UI; power of UI itself (Dunn et al. 2023 for Gaussians); practical algorithms beyond Li 1999's slow one (Sec. 8.2.4).
Also flagged as open in the body: a game-theoretic reading of reverse submartingales (Sec. 5.6); a codelength interpretation of e-processes for composite nulls (Sec. 8.1.3); a "full understanding" of why a hidden game underlies most nonparametric problems (Sec. 1.2).

### Appendices
- **Appendix A** (SAVI as middle ground): with simple nulls admissible e-processes and Bayes factors coincide; with composite parametric nulls sometimes (group invariance); nonparametrically they diverge. The e-confidence interval {θ : 1/E^θ_τ > α} from a prior-posterior-ratio family requires P̄(θ|X^τ) ≥ α pointwise, whereas a credible interval requires it only on average over the prior, so credible intervals are narrower; for simple nulls and k < 1 the Bayesian k-support interval (Wagenmakers et al. 2020) equals the (1−k)-e-CI (Pawel–Ly–Wagenmakers 2022). P̄(θ|X^τ) := 1/E^θ_τ is proposed as an "e-posterior" with minimax decision guarantees for arbitrary post-hoc losses (Grünwald 2022, 2023).
- **Appendix B** (price of SAVI): at a fixed n, a GRO e-variable has less power than the UMP Neyman–Pearson test and CSs are "between 1.5 and 2 times as wide" as CIs; under optional stopping expected stopping times are "about the same or even smaller" than the fixed NP n; the authors argue power is the wrong metric for the SAVI objective (growth under any alternative, no growth under any null).

## Setting and assumptions
- Filtered sample space, data X = (X_1, X_2, ...) not necessarily i.i.d., null P and alternative Q sets of distributions over the whole sequence; stopping times include ones that never stop (Sec. 1.1). The filtration may be coarser (discarded information, Sec. 4.1.2) or richer (external randomisation) than σ(X^t) [ramdasGametheoreticStatisticsSafe2023].
- Measurability and measure-theoretic details are "left implicit so far as possible" (Sec. 2). The simple-null identifications (unit bet = likelihood ratio; test martingale = likelihood ratio process) need Q ≪ P; the RIPr needs a common reference measure and a finite infimum in eq. 17.
- Optional stopping is permitted by construction for every e-process (eq. 10); optional continuation at the study level needs only conditional validity of each unit bet (eq. 13, Sec. 6.1). Peeking is allowed; choosing among strategies after seeing data is not (Sec. 6.4).
- Case studies in Section 5 use conditional (martingale-difference) versions of the nonparametric classes: sub-Gaussian with known σ, variance bounded by known σ², bounded in [0,1], conditional symmetry; σ cannot be learned except in the bounded case (Sec. 5.3).

## Relation to other sources
- [grunwaldSafeTesting2024](grunwaldSafeTesting2024.md): source of GRO/GROW/REGROW, the RIPr theorem (eq. 17 here is its Theorem 1), the "safe under optional continuation" terminology, Example 4 (MLR GRO e-variable) and the asymptotic-REGROW status of Jeffreys' prior; this survey positions RIPr as "always an e-value, sometimes an e-process" against UI.
- [wassermanUniversalInference2020](wassermanUniversalInference2020.md): universal inference (eq. 16) as the always-applicable e-process for composite nulls, the plug-in numerator, derandomisation by averaging (Sec. 2.9), and the UI e-processes for exchangeability and log-concavity; the survey states UI is dominated by RIPr whenever the latter is an e-process and that UI's power is "quite open" (Sec. 8.2.4).
- [ramdasHypothesisTestingEvalues2025](ramdasHypothesisTestingEvalues2025.md): the later monograph expands every section here (e-processes Ch. 7, numeraire/RIPr Ch. 6, UI Ch. 5, e-BH Ch. 9, e-CIs Ch. 13); the admissibility and RIPr-existence questions left open in Sec. 8.2 are the ones the numeraire theory addresses.
- [haoEValuesExponentialFamilies2025](haoEValuesExponentialFamilies2025.md): cited (as Hao et al. 2023) for conditional e-values with exponential-family nulls generally lacking (RE)GRO(W) status (Sec. 4.1.3).
- [howardTimeuniformNonparametricNonasymptotic2021](howardTimeuniformNonparametricNonasymptotic2021.md): Lemma 3 (equivalence of "for all t" and "at every τ" statements, used for eqs. 9–10, AV p-values and CSs), the sub-exponential supermartingale (eq. 23), √log log t rates, the confseq package.
- [shaferTestingBettingStrategy2021](shaferTestingBettingStrategy2021.md): betting score terminology, Gibbs-inequality proof of log-optimality, the "implied alternative" used against e-hacking (Sec. 6.4).
- [vovkEvaluesCalibrationCombination2021](vovkEvaluesCalibrationCombination2021.md): averaging as the admissible symmetric merger of dependent e-values (Sec. 2.9); calibrators (Sec. 6.3).
- [koolenLogoptimalAnytimevalidEvalues2022](koolenLogoptimalAnytimevalidEvalues2022.md): not cited directly; the t-test discussion (Sec. 4.1.2) relies on Pérez-Ortiz et al. 2022, of which that paper is the log-optimality companion.
- [terschureAnytimevalidLogrankTest2024](terschureAnytimevalidLogrankTest2024.md): the logrank e-process as the non-i.i.d. instance of the MLR reduction (Sec. 4.1.1), the GRO-vs-REGROW simulations, Gaussian-approximation logrank in ALL-IN (Sec. 6.1), group-sequential comparison (Sec. 8.1.2).
- [turnerGenericEvariablesExact2024](turnerGenericEvariablesExact2024.md), [turnerExactAnytimevalidConfidence2023](turnerExactAnytimevalidConfidence2023.md): k-sample "flattened" e-variables with (RE)GROW properties and bounded-dependence CSs (Sec. 4.2); the k-sample case where learned-alternative RIPr is not an e-process (Sec. 3.3.2).
- [villeEtudeCritiqueNotion1939](villeEtudeCritiqueNotion1939.md): origin of test martingales, Ville's theorem and inequality (Sec. 2.5).
- Without a link: waldSequentialAnalysis1947 (plug-in method eq. 10.10, SPRT contrast), grunwaldOptimalEValuesExponential2024 (the exponential-family GRO line continued in Sec. 4.1.1).

## Concepts touched
- [e-variable](../concepts/e-variable.md)
- [test-martingale](../concepts/test-martingale.md)
- [e-process](../concepts/e-process.md)
- [villes-inequality](../concepts/villes-inequality.md)
- [testing-by-betting](../concepts/testing-by-betting.md)
- [confidence-sets-and-sequences](../concepts/confidence-sets-and-sequences.md)
- [optional-stopping](../concepts/optional-stopping.md)
- [optional-continuation](../concepts/optional-continuation.md)
- [gro-criterion](../concepts/gro-criterion.md)
- [e-power](../concepts/e-power.md)
- [mixture-and-plug-in-methods](../concepts/mixture-and-plug-in-methods.md)
- [universal-inference](../concepts/universal-inference.md)
- [reverse-information-projection](../concepts/reverse-information-projection.md)
- [bayes-factor-e-variable](../concepts/bayes-factor-e-variable.md)
- [exponential-family-e-values](../concepts/exponential-family-e-values.md)
- [e-merging](../concepts/e-merging.md)
- [e-bh](../concepts/e-bh.md)
- [calibrator](../concepts/calibrator.md)
- [post-hoc-validity](../concepts/post-hoc-validity.md)
- exponential-supermartingales (new)
- filtration-choice (new)
- e-detector (new)
- history-of-savi (new)

## Versions
arXiv 2210.01948 (Oct 2022) and the Statistical Science version of record (Nov 2023) are the same paper; the text layer here is the published version, so section and equation numbers refer to it. The survey cites several works by their 2022–2023 preprint status (Safe testing "to appear", Pérez-Ortiz et al. arXiv 2208.07610, Hao et al. arXiv 2303.0047) that have since been published under the bib keys noted above.

## Open questions / gaps
- The four stated open problems (existence hierarchy, filtration choice, admissibility characterisation, RIPr-as-e-process and RIPr algorithms), Sec. 8.2.
- Whether reverse submartingale CSs have a betting interpretation (Sec. 5.6); whether e-processes for composite nulls have a codelength reading (Sec. 8.1.3).
- The "price of SAVI" is argued qualitatively (Appendix B); the quantitative claims (CSs 1.5–2× wider; expected stopping times at or below NP's n) are delegated to cited papers, notably grunwaldSafeTesting2024 Sec. 6.
- Cited works central to the methodology but not in the bib: Ramdas–Ruf–Larsson–Koolen 2020 (admissibility must rely on martingales), Ramdas–Ruf–Larsson–Koolen 2022 (testing exchangeability, fork-convexity), Ruf–Larsson–Koolen–Ramdas 2022 (composite Ville theorem), Waudby-Smith & Ramdas 2023 (betting CSs for bounded means), Pérez-Ortiz–Lardy–de Heide–Grünwald 2022 (group invariance), Howard–Ramdas–McAuliffe–Sekhon 2020 (time-uniform Chernoff bounds), Shafer–Shen–Vereshchagin–Vovk 2011 (test martingales, Bayes factors and p-values), Wang & Ramdas 2022 (e-BH), Shin–Ramdas–Rinaldo 2022 (e-detectors), Grünwald–Henzi–Lardy 2023 (model-X conditional independence), Xu–Wang–Ramdas 2022 (e-BY), Manole & Ramdas 2023 (reverse submartingales), Zhang–Ramdas–Wang 2023 (existence of powerful e-values). Record in `wiki/gaps.md`.
