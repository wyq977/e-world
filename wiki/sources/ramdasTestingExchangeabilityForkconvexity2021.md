---
citekey: ramdasTestingExchangeabilityForkconvexity2021
title: "Testing exchangeability: fork-convexity, supermartingales, and e-processes"
authors: [Aaditya Ramdas, Johannes Ruf, Martin Larsson, Wouter M. Koolen]
year: 2021
status: preprint
public: true
note: "The first worked example of a null where every test supermartingale is powerless but a powerful e-process exists: binary exchangeability, attacked with a Jeffreys-mixture-over-maximum-likelihood ratio, and explained by the geometry of fork-convex hulls."
links:
  pdf: "https://arxiv.org/pdf/2102.00630"
  arxiv: "https://arxiv.org/abs/2102.00630"
  doi: "10.48550/arXiv.2102.00630"
  video: ""
tags: [exchangeability, e-process, nonnegative-supermartingale, fork-convexity, snell-envelope, universal-inference, method-of-mixtures, jeffreys-prior, markov-alternatives, universal-coding, de-finetti, conformal-filtration, game-theoretic-probability, calibrator, adjuster, confidence-sequence, change-point]
ingested: 2026-10-08
version: "arxiv (2102.00630v4, 23 Jul 2021, 34 pages; published in IJAR 141, 2022)"
---

# Testing exchangeability: fork-convexity, supermartingales, and e-processes

arXiv 2102.00630v4 (July 2021), 34 pages; the version of record appeared in the International Journal of Approximate Reasoning 141 (2022). The arXiv v4 file is the one ingested. Several other sources in this wiki cite it as "Ramdas, Ruf, Larsson and Koolen 2021" or "2022".

## Summary
The paper studies the sequential test of the null H_0 that an infinite binary sequence X_1, X_2, … is exchangeable, with the canonical filtration F_t = σ(X_1, …, X_t) fixed throughout, and uses it as a test-bed for the gap between composite nonnegative supermartingales (NSMs) and composite "safe e-processes" [ramdasTestingExchangeabilityForkconvexity2021, Sec. 1]. By de Finetti, the exchangeable laws Q̄ are the convex hull of the i.i.d. Bernoulli laws Q, and safety is closed under convex hulls, so it suffices to build a Q-safe e-process (Prop. 2). The negative result is geometric: the NSM property is preserved under fork-convex combinations (Lemma 12, Thm 13), the closed fork-convex hull of Q is the set of all laws over binary sequences (Thm 17), and therefore every Q-NSM is almost surely nonincreasing, the only Q-nonnegative-martingale is the constant one, and no NSM-based test has any power against any alternative (Prop. 5, Thm 17). The positive result is the closed-form process R_t = (Jeffreys' mixture over first-order Markov chains)/(maximum likelihood under i.i.d. Bernoulli), eq. (6): it is a Q-safe e-process because for every Ber(p)^∞ it is dominated by the mixture-likelihood-ratio martingale R^{JP,p}_t (Thm 6), it is not itself an NSM, and a universal-coding regret bound gives ln R_t ≥ ℓ(t) − ln t − O(1), where ℓ(t) is the log ratio of Markov to Bernoulli maximum likelihoods (eq. 8). Theorem 7 is pathwise: whenever the transition frequency limits exist, ln R_t / t → r*, a difference of Markov and Bernoulli entropies, which is strictly positive unless α(1 − p) = γp, so the test has power one against every first-order Markov alternative without absorbing states and against a generic dense set of higher-order ones. Section 3 also shows that a composite Snell envelope exists exactly when the null is fork-convex (Thm 14), so a Q-safe e-process is dominated by a Q-NSM if and only if it is already safe for the closed fork-convex hull (Cor. 16). Section 5 contrasts the approach with Vovk's conformal test martingales in a coarsened filtration and reinterprets R_t as the skeptic's worst-case wealth across parallel games, a constructive witness to Ville's theorem for a composite null.

## Main results
- **Prop. 2** (from Ramdas et al. 2020): type-I error control and e-process safety are closed under convex hulls; a Q-safe e-process is Q̄-safe, so i.i.d. Bernoulli tests transfer to exchangeability by de Finetti [ramdasTestingExchangeabilityForkconvexity2021, Sec. 1.2].
- **Remark 3**: (Q + Q')/2 for Q = Ber(0.3)^∞, Q' = Ber(0.7)^∞ is in the convex hull (a sequence that is 70% zeros or 70% ones), while ((Ber(0.3) + Ber(0.7))/2)^∞ is not; the latter lies in the closed fork-convex hull [Sec. 1.2].
- **Prop. 4**: a binary process is k-th order Markov and exchangeable iff it is constant or i.i.d.; Q̄ ∩ P_k = Q ∪ C [Sec. 1.3, App. B].
- **Prop. 5**: every Q-NSM is a P_k-NSM for every k and a P-NSM for every set P, hence a Q-safe e-process with nontrivial power cannot be a Q-NSM [Sec. 1.5].
- **Thm 6**: R_t of eq. (6), with gamma-function closed form in the transition counts n_{0|0}, n_{0|1}, n_{1|0}, n_{1|1} and the Bernoulli MLE (n_1/t)^{n_1}(n_0/t)^{n_0}, is a Q̄-safe e-process; κ_α = inf{t : R_t ≥ 1/α} is a level-α sequential test for exchangeability [Sec. 1.6, Secs 2.1–2.3].
- **Eq. (8)**: Krichevsky–Trofimov regret bound: R_t ≥ (Markov ML / Bernoulli ML) · e^{−ln t − O(1)}; evidence accrues once the Markov MLE beats the Bernoulli MLE by a factor of order t [Sec. 2.3].
- **Thm 7** (pathwise): if the limits α = lim n_{1|1}/t, β = lim n_{0|0}/t, γ = lim n_{1|0}/t, p = lim n_1/t exist, then lim ln R_t / t = r* = γ ln(γ/(1−p)) + β ln(β/(1−p)) + α ln(α/p) + γ ln(γ/p) − p ln p − (1−p) ln(1−p); r* > 0 iff α(1 − p) ≠ γp; under the null R_t → 0 a.s. [Sec. 2.4].
- **Remark 8**: for k-th order chains the condition α(1 − p) ≠ γp holds on an open dense set of transition parameters (real-analyticity), so power one is generic [Sec. 2.4].
- **Example 9**: the 2nd-order chain 0011 0011 … has p = 1/2, α = γ, and R_t ≤ 4^t Γ(t+1)^4/Γ(2t)^2 → 0, so (R_t) has no power there [Sec. 2.4].
- **Sec. 2.5**: order-k, alphabet-d extension R^{k,d}_t by independent Dirichlet(1/2, …, 1/2) (KT) mixtures per context, with regret (d^k(d − 1)/2) ln t + O(1) and R^{k,d}_t → ∞ P-a.s. for P ∈ P_k \ Q.
- **Sec. 2.6** (double mixture): E_t = Σ_k (6/(π²k²)) E^k_t over a countable family of power-one e-processes is a Q-safe e-process with power one against the union; the truncated sum Σ_{k ≤ t} or Σ_{k ≤ f(t)} keeps consistency and saves computation.
- **Sec. 2.7**: R^{NA}_t = (non-anticipating, predictable-mixture likelihood ∏ g_s(X_s))/(null maximum likelihood) is a Q-safe e-process for any predictable g_s, linking to universal inference, predictable mixtures and betting; no regret bound in general.
- **Def. 10–11**: fork-convex combination of Q, Q' with likelihood-ratio processes Z, Z' — Z''_t = Z_t for t ≤ s and hZ_t + (1 − h)Z_s Z'_t/Z'_s for t > s, with s ∈ N_0 and h an F_s-measurable [0,1] variable; fork-convex sets, hulls, closed hulls under L¹(R) convergence at each fixed t; first due to Žitković 2002, related to Delbaen's m-stability and Epstein–Schneider rectangularity; fork-convexity implies convexity [Sec. 3.1].
- **Lemma 12**: a supermartingale under Q and Q' is a supermartingale under every fork-convex combination [Sec. 3.2].
- **Thm 13**: every Q-NSM is an NSM under the closed fork-convex hull Q̃, so NSM-based tests are powerless against Q̃ \ Q; safety is not preserved this way (Q-safe implies conv(Q)-safe but not Q̃-safe) [Sec. 3.2].
- **Thm 14** (composite Snell envelope): if Q is locally dominated and fork-convex and (E_t) is Q-safe, then L_t = ess sup_{Q ∈ Q, τ ≥ t} E_Q[E_τ | F_t] is the smallest Q-NSM dominating (E_t), with L_0 ≤ 1; proof adapts Delbaen 2006, Thm 11 [Sec. 3.3, App. B].
- **Cor. 16**: a Q-safe e-process is dominated by a Q-NSM with L_0 ≤ 1 iff it is already Q̃-safe [Sec. 3.3].
- **Thm 17**: every law over binary sequences lies in the closed fork-convex hull of {Ber(p)^∞ : p ∈ (0,1)} (induction on time, mixing 2^s Bernoulli laws at time s with indicator weights); hence M_t ≡ 1 is the only Q-NM and every Q-NSM is nonincreasing, with zero power at every α [Sec. 3.4].
- **Sec. 4**: simulations — ln R_t decays like −ln t under Bernoulli(0.5), (0.2) (Fig. 3); grows linearly with slope r* under Markov(0.1, 0.9), (0.4, 0.6) (Fig. 4); diverges logarithmically for a sticky time-varying chain with p_{0|0}(t) = p_{1|1}(t) = 1/2 + δ_t, δ_t from F(t) = min{t/2, √t ln(1 + t)}, where r* = 0 (Sec. 4.3, Fig. 5); gains exponentially between n and 2n on Ber(0.1)^{5000} Ber(0.4)^{5000}, with anytime p below 10^{−20}, then decays (Sec. 4.4, Fig. 6); rejects exchangeability of 4404 days of North London rain, 59% rainy (Sec. 4.5, Fig. 7).
- **Sec. 4.4**: a change-point e-process per hypothesised time n = 2^k, with smoothed non-anticipating MLEs before and after n over the null MLE, combined by the double mixture; power but not power one, since no test can have power one against a single change.
- **Sec. 4.6**: C_t = {q : R^{JP,q}_t < 1/α} is a (1 − α)-confidence sequence for p by Ville's inequality; R_t = inf_q R^{JP,q}_t, so inf{t : C_t = ∅} equals κ_α (eq. 16); the running intersection may stop slightly sooner.
- **Sec. 4.7**: (max_{s ≤ t} R_s) is not an e-process but 1/max_{s≤t} R_s is a p-process; calibrating it with f(u) = (1 − u + u ln u)/(u(−ln u)²), or applying the adjuster F(y) = y² ln 2/((1 + y)(ln(1 + y))²) to the running maximum, gives a nondecreasing Q-safe e-process A_t ≤ R_t with A_∞ ≈ 10^{17} in the change-point example where R_∞ = 0; recommended when the alternative may not be Markov.
- **Sec. 5.3**: Vovk's conformal approach replaces (F_t) by the poorer filtration (G_t) of conformal p-values, obtains independent p-variables, calibrates them and multiplies into a (G_t)-martingale; safety then holds only for (G_t)-stopping times, whereas R_t is safe for all (F_t)-stopping times. A third route via reverse martingales in the exchangeable filtration is left to future work.
- **Sec. 5.4**: parallel-games protocol — the skeptic plays one game per m ∈ M = [0,1] with K^m_0 = 1 against Q^m = {Ber(p)^∞}, net wealth K_t = inf_m K^m_t; this is the game-theoretic form of an e-process, whereas the single-game protocol yields a supermartingale. With A = {limits in (9) fail or (10) holds}, inf_Q Q(A) = 1 and R_t → ∞ on A^c, a composite-null analogue of Ville's theorem (Shafer–Vovk 2001, Prop. 8.14).

## Setting and assumptions
- Data: infinite binary sequence; canonical filtration F_t = σ(X_1, …, X_t), no external randomisation; stopping times possibly infinite with E_∞ = lim sup E_t [ramdasTestingExchangeabilityForkconvexity2021, Sec. 1.1].
- Null: Q̄ = all exchangeable laws = conv(Q), Q = {Ber(p)^∞ : p ∈ [0,1]}; reference measure R = Ber(1/2)^∞ locally dominates every binary law (Sec. 3.4). Section 3 allows a general space X with local domination (App. A).
- Alternatives: P_1 time-homogeneous first-order Markov chains with X_1 ~ Ber(1/2); P_k order k; Markov sources over alphabets of size d; countable unions; loosely specified alternatives via predictable mixtures; change points. Testing against all non-exchangeable laws is information-theoretically impossible (first coin Ber(p_1), rest Ber(p)) (Sec. 1.2).
- Validity: sup_Q sup_τ E_Q[E_τ] ≤ 1 over all stopping times; level-α test by Markov's inequality at 1/α; anytime p-process p_t = inf_{s ≤ t} 1/E_s (eqs 2–4). Optional stopping fully allowed in the data filtration.
- Power: consistency means inf_{P ∈ P \ Q} P(κ_α < ∞) = 1 for all α, equivalently lim sup E_t = ∞ P-a.s. (eq. 5).
- Tools: de Finetti's theorem, method of mixtures with Jeffreys (Beta(1/2,1/2)) priors, Fubini swap, maximum likelihood under the null, Krichevsky–Trofimov regret bounds, essential suprema, conditional Fatou.

## Relation to other sources
- [ramdasAdmissibleAnytimevalidSequential2022](ramdasAdmissibleAnytimevalidSequential2022.md): supplies Prop. 2 (closure under convex hulls), the pointwise Snell-envelope answer for singleton nulls, the inf_Q M^Q_t representation of admissible e-processes and the p-process p_t = inf 1/E_s; this paper qualifies the composite answer ("sometimes") via fork-convexity and the composite Snell envelope (Thm 14) [ramdasTestingExchangeabilityForkconvexity2021, Secs 1.1, 1.6, 3].
- [wassermanUniversalInference2020](wassermanUniversalInference2020.md): the maximum-likelihood denominator (Sec. 2.1) and the non-anticipating numerator (Sec. 2.7, Sec. 4.4) are universal inference in sequential form; this paper is the exchangeability instance the survey and the e-process page cite.
- [howardTimeuniformNonparametricNonasymptotic2021](howardTimeuniformNonparametricNonasymptotic2021.md): cited for the method of mixtures and confidence sequences; Howard et al. 2020 (Probability Surveys) is credited with exponential processes dominated by composite NSMs, the characterising property of e-processes (Sec. 1.1, Sec. 5.2).
- [grunwaldSafeTesting2024](grunwaldSafeTesting2024.md): GROW e-variables are ratios of mixtures and safe only at fixed sample size (Sec. 1.4); the question "when is a safe e-value an NSM in disguise" is attributed to that preprint (Sec. 3). Vovk's discussion and the authors' reply ([grunwaldAuthorsReplyDiscussion2024](grunwaldAuthorsReplyDiscussion2024.md)) concern exactly the exchangeability and conformal-filtration issue settled here.
- [shaferTestingBettingStrategy2021](shaferTestingBettingStrategy2021.md): the testing-by-betting protocol of Sec. 5.4 is quoted from Shafer; the parallel-games extension is this paper's.
- [vovkEvaluesCalibrationCombination2021](vovkEvaluesCalibrationCombination2021.md): source of the e-variable terminology and the calibrator f(u) of Sec. 4.7 (their eq. 2).
- [villeEtudeCritiqueNotion1939](villeEtudeCritiqueNotion1939.md): Thm 7 is restated as a composite-null witness to Ville's theorem that every null set is detected by a martingale (Sec. 5.4).
- [ramdasGametheoreticStatisticsSafe2023](ramdasGametheoreticStatisticsSafe2023.md), [ramdasHypothesisTestingEvalues2025](ramdasHypothesisTestingEvalues2025.md): both cite this paper as the canonical example in the existence hierarchy (nulls with e-processes but no nontrivial supermartingale) and for the fork-convexity remark that mixtures are plug-ins only over fork-convex classes.
- [koolenLogoptimalAnytimevalidEvalues2022](koolenLogoptimalAnytimevalidEvalues2022.md): its inf-of-test-martingales representation and non-supermartingale example are the abstract counterpart of R_t = inf_p R^{JP,p}_t.
- [shinEdetectorsNonparametricFramework2023](shinEdetectorsNonparametricFramework2023.md): Remark 2.10 there uses exchangeability e-processes that are not supermartingales as e-detector increments; the change-point discussion of Sec. 4.4 and Remark 18 here draws the line between sequential testing and change detection.
- [perezortizEstatisticsGroupInvariance2024](perezortizEstatisticsGroupInvariance2024.md): another coarsened-filtration construction (maximal invariants), parallel to Vovk's conformal filtration discussed in Sec. 5.3.
- Without link: Waudby-Smith and Ramdas 2020 (predictable mixtures; the fork-convex hull of {E[X_t | F_{t−1}] = μ, product form} is the non-product class, Sec. 3.1) — in the bib as waudbysmithEstimatingMeansBounded2020 but not yet ingested; Vovk 2021 (Testing randomness online, conformal test martingales); Vovk et al. 2021 (conformal change-point martingales); Takeuchi, Kawabata and Barron 2013 (optimality of Jeffreys mixtures for Markov sources); Krichevsky and Trofimov 1981; Kaufmann and Koolen 2018 (mixture martingales); Shin, Ramdas and Rinaldo 2021 (sequential GLR); Žitković 2002 and Delbaen 2006 (fork-convexity, m-stability); Dawid et al. 2011 and Koolen and Vovk 2014 (adjusters); Manole and Ramdas 2021 (reverse submartingales in the exchangeable filtration); Wald 1945, 1947; Wald and Wolfowitz 1948; Robbins and Siegmund 1968–1974.

## Concepts touched
- [e-process](../concepts/e-process.md): the paper that makes the e-process/supermartingale gap concrete (Prop. 5, Thms 6, 13, 17, Cor. 16).
- [test-martingale](../concepts/test-martingale.md): fork-convex closure of the NSM property; the only Q-NM for binary exchangeability is constant.
- [universal-inference](../concepts/universal-inference.md): maximum likelihood under the null plus a mixture or predictable numerator (Secs 2.1, 2.7).
- [mixture-and-plug-in-methods](../concepts/mixture-and-plug-in-methods.md): Jeffreys/KT mixture over Markov chains, regret bound (8), double mixtures (Sec. 2.6), predictable mixtures (Sec. 2.7).
- [testing-by-betting](../concepts/testing-by-betting.md): parallel-games protocol with wealth inf_m K^m_t (Sec. 5.4).
- [optional-stopping](../concepts/optional-stopping.md): safety over all (F_t)-stopping times versus only (G_t)-stopping times for conformal martingales (Sec. 5.3).
- [villes-inequality](../concepts/villes-inequality.md): confidence sequence C_t via Ville (Sec. 4.6); composite-null analogue of Ville's theorem (Sec. 5.4).
- [confidence-sets-and-sequences](../concepts/confidence-sets-and-sequences.md): the equivalence of κ_α with emptiness of C_t (eq. 16).
- [calibrator](../concepts/calibrator.md): calibrated p-processes and adjusters to lock in past wealth (Sec. 4.7).
- [martingale-history](../concepts/martingale-history.md): Ville's theorem on measure-zero sets reinterpreted; Wald's SLRT and mixture SLRT (Secs 1.4, 5.4).
- [e-detector](../concepts/e-detector.md): change-point e-processes and the distinction from change detection (Sec. 4.4, Remark 18).
- fork-convexity (new): fork-convex combinations and hulls, closure of the NSM property, composite Snell envelopes, and the all-laws theorem for binary sequences (Defs 10–11, Lemma 12, Thms 13, 14, 17, Cor. 16).

## Versions
The ingested text is arXiv v4 (July 2021); the IJAR 2022 version of record was not compared. Other wiki sources cite the paper variously as 2020, 2021 and 2022.

## Open questions / gaps
- A general "robust" Ville theorem for composite nulls that recovers Ville's original for singletons is stated as an important open direction [ramdasTestingExchangeabilityForkconvexity2021, Sec. 5.4].
- Formalising when (R_t) is consistent although r* = 0 (the sticky time-varying chain of Sec. 4.3) is left to future work.
- No systematic way is known to find the largest Q-NSM dominating a given e-process; only the smallest (the Snell envelope) is constructed (Sec. 3.3).
- Power of the predictable-mixture e-process R^{NA}_t for generic update rules has no regret bound (Sec. 2.7).
- Reverse martingales in the exchangeable filtration as a third route to testing exchangeability are not explored (Sec. 5.3).
- Order-k, alphabet-d formulas (R^{k,d}_t) are stated without explicit expressions (Sec. 2.5).
