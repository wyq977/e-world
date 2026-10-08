---
citekey: koolenGeneralisationVilleInequality2025
title: "A generalisation of Ville's inequality to monotonic lower bounds and thresholds"
authors: [Wouter M. Koolen, Muriel F. Pérez-Ortiz, Tyron Lardy]
year: 2025
status: preprint
public: true
note: "Ville's inequality with a time-decreasing floor and a time-increasing threshold: an exact crossing-probability formula, tight via a 'floor-hugging' martingale, used to turn an improper-mixture supermartingale into a clean finite-time law of the iterated logarithm."
links:
  pdf: "https://arxiv.org/pdf/2502.16019"
  arxiv: "https://arxiv.org/abs/2502.16019"
  doi: "10.48550/arXiv.2502.16019"
  video: ""
tags: [villes-inequality, supermartingale, anytime-valid, law-of-iterated-logarithm, improper-mixture, method-of-mixtures, sub-gaussian, confidence-sequence, stitching, multiple-testing, tightness]
ingested: 2026-10-08
version: "arxiv (2502.16019v1, 22 Feb 2025, 17 pages; submitted to the Statistics & Probability Letters e-values special issue)"
---

# A generalisation of Ville's inequality to monotonic lower bounds and thresholds

## Summary
Classic [Ville's inequality](../concepts/villes-inequality.md) bounds P(∃n : M_n ≥ C) ≤ E[M_0]/C for a nonnegative supermartingale, with both the floor (zero) and the threshold (C) constant in time [koolenGeneralisationVilleInequality2025, Thm 1.1]. The paper replaces both by monotone curves: for a supermartingale with M_n ≥ −f(n) and a target g(n), with f and g non-decreasing, it gives an exact upper bound on P(∃n : M_n ≥ g(n)) as an infinite product over time (Theorem 2.1(a)), and shows the bound is attained by a "floor-hugger" martingale that sits on −f(n) and at each step either jumps to g(n+1) or drops to −f(n+1) (Theorem 2.1(b)). The upper bound is proved by applying classic Ville to an auxiliary nonnegative supermartingale K_n that depends on the *future* of f and g through the floor-hugger's survival probability s(n); the authors show that no history-only auxiliary process can work (Section 2.2). A continuous relaxation (Corollary 3.1) turns the product into exp(−∫ f'/(g+f)), with explicit families of admissible threshold curves (quadratic, Example 3.2; exp-concave dampeners, Appendix A). The motivating application is the improper-mixture supermartingale M_n = (2π)^{−1/2} ∫ {e^{ηS_n − η²n/2} − 1} e^{−η²/2} dη/|η| of Koolen and van Erven 2015, which is bounded below only by −ln(1+n)/√(2π); the new inequality yields a finite-time law of the iterated logarithm for independent sub-Gaussian observations with every constant explicit (Lemma 4.1, Appendix B). The discussion concedes the extension is not strictly more general than Ville (since the proof reduces to it) but argues it is more usable, and reads the receding floor as a subsidy that buys repeated all-or-nothing bets, i.e. an exact multiple-testing correction (Section 5).

## Main results
- **Theorem 1.1 (classic Ville)**: nonnegative supermartingale, P{∃n ≥ 0 : M_n ≥ C} ≤ E[M_0]/C; the inverse proportionality of threshold and probability is what frees supermartingale tests from a Bonferroni union bound over time [koolenGeneralisationVilleInequality2025, Sec. 1].
- **Theorem 2.1(a) (generalised Ville)**: f, g non-decreasing on {0, 1, …} with −f(0) < g(0); for any supermartingale with M_n ≥ −f(n) and E[M_0] ∈ [−f(0), g(0)],
  P{∃n : M_n ≥ g(n)} ≤ 1 − ((g(0) − E[M_0])/(g(0) + f(0))) · ∏_{n≥1} (g(n) + f(n−1))/(g(n) + f(n)) (eq. 4). Constant f ≡ 0, g ≡ C recovers Theorem 1.1.
- **Theorem 2.1(b) (tightness)**: for every admissible initial mean there is a martingale with M ≥ −f attaining (4) with equality.
- **Floor-hugger martingale (Sec. 2.1)**: from M_n = −f(n) jump to g(n+1) with probability p_n = (f(n+1) − f(n))/(g(n+1) + f(n+1)) (eq. 5), else drop to −f(n+1); its probability of never reaching g from time n is s(n) = ∏_{t≥n} (1 − p_t) ∈ [0, 1] (eq. 6). Initial means strictly inside (−f(0), g(0)] are handled by randomising the start between −f(0) and g(0).
- **Lemma 2.2 and Corollary 2.3 (upper bound)**: K_n := 1 − s(n)(g(n) − M_n)/(g(n) + f(n)) (eq. 7) is a nonnegative supermartingale (uses M_n ≥ −f(n), the supermartingale property, and the recurrence s(n) = (1 − p_n) s(n+1)); M_n ≥ g(n) implies K_n ≥ 1, so classic Ville on K gives (4).
- **Impossibility of a history-only reduction (Sec. 2.2)**: any nonnegative supermartingale L_n built from (M_i, f(i), g(i))_{i≤n} with M_n ≥ g(n) ⇒ L_n ≥ 1 must satisfy L_n ≥ 1 for all n, because a floor-hugger jump with f(n+1) → ∞ succeeds with probability arbitrarily close to one; K_n must look ahead through s(n).
- **Corollary 3.1 (continuous relaxation)**: f, g : R_+ → R_+ increasing, f differentiable; P{∃n : M_n ≥ g(n)} ≤ 1 − ((g(0) − E[M_0])/(g(0) + f(0))) exp(−∫_0^∞ f'(t)/(g(t) + f(t)) dt). Looser than (4) in discrete time, tight in continuous time, and invariant under increasing reparametrisations of time.
- **Example 3.2 (quadratic threshold)**: f(0) = 0, f ↑ ∞, g(t) = (a f(t) + b)² − f(t) (increasing if 2ab ≥ 1) gives exponent −1/(ab), so crossing probability ≤ 1 − e^{−1/(ab)}; set ab = 1/(−ln(1−δ)) for level δ.
- **Example 3.3 (counterexample)**: if g = O(f) with f diverging, the integral diverges and the bound is the trivial 1; the threshold must grow super-linearly in the floor.
- **Example A.1 (exp-concave dampener)**: for twice-differentiable 1-exp-concave h with h(∞) = 0, g(t) = −1/h'(f(t)) − f(t) is non-decreasing and the bound is 1 − e^{−h(0)}; choose h(0) = −ln(1−δ). Polynomial h(ξ) = (aξ+b)^{1−c}/(a(c−1)), c > 1, ac ≥ b^{1−c} (quadratic is c = 2); fat-tailed h(ξ) = 1/ln(aξ+b)^{c−1}, b ≥ e, c > 1, gives g(n) ∼ f(n)(ln f(n))^c.
- **Improper-mixture supermartingale (eq. 8, Lemma B.2)**: for S_n = Σ_{i≤n}(X_i − μ) with conditionally 1-sub-Gaussian increments, M_n = (2π)^{−1/2} ∫_R {exp(ηS_n − η²n/2) − 1} e^{−η²/2} dη/|η| is a supermartingale (martingale for Gaussian data) equal to I(S_n/√(n+1)) − ln(1+n)/√(2π), where I(x) = ∫_0^x e^{u²/2} erf(u/√2) du ≥ 0 (eq. B.1); hence M_n ≥ −ln(1+n)/√(2π) and f(n) = ln(1+n)/√(2π) is the floor. Proof by Feynman's trick (Appendix B.1).
- **Lemma 4.1 (finite-time LIL)**: independent sub-Gaussian X_i with common mean μ, δ ≤ 3/5, δ' := −ln(1−δ): with probability > 1 − δ, for all n, |S_n/√(n+1)| ≤ √(2 ln{1 + ln(n+1)/√π + (e√2/δ') ln²(ln(n+1)/√(2π) + e)}) + 1/√2. The RHS is √(2 ln(ln n/δ))(1 + o(1)), the iterated-logarithm form (2) with explicit lower-order terms.
- **Lemma B.1 (sharper form)**: same bound with the constant 1/√2 replaced by an explicit increasing residual R(n) ≤ 1/√2, R(n) ∼ (1/√2)(1 − 1/√(2 ln ln n)). Rescaling the prior to e^{−η²κ²/2} dη/|η| rescales the bound to S_n ≤ κ F_δ(n/κ²).
- **Lemma B.3 (implicit bound)** and **Lemma B.5 (threshold choice)**: with f(x) = ln(1+x)/√(2π), u(x) = (e+x) ln(e+x)²/d and g = u∘f − f, g ≥ f is increasing for 0 < d ≤ 1 and ∫ f'/(f+g) = d; d = δ' gives P(∃n : I(S_n/√(n+1)) ≥ u(f(n))) ≤ 1 − e^{−δ'} = δ, valid for δ ≤ 1 − e^{−1} ≈ 0.63. The threshold corresponds to the fat-tailed dampener h(x) = d/ln(e+x) of Example A.1 with c = 2.
- **Lemmas B.4, B.6, B.7 (inversion)**: I(x) ≥ l(x) := √((e^{x²/2} − 1)³/(x² e^{x²/2})), via the identity I(x) = √(2/π) ∫_0^∞ {e^{x² sech²(w)/2} − 1} dw (eq. B.4); l is convex, so a tangent at ξ = √(2 ln(1+√(2τ))) inverts I(x) ≤ τ into |x| ≤ ξ + R(τ).
- **Discussion (Sec. 5)**: (i) the extension is not strictly more general, since classic Ville on K_n proves it; (ii) it is "more empowering" because K_n was found last and is unintuitive; (iii) proper mixtures over η with density 1/(|η|(ln|η|)^{1+c}) require bounding an integral by 1/δ, while the improper mixture reduces to I(S_n/√(n+1)) ≤ (ln n/δ)(ln ln n)^{1+c}, separating the deviation from the sample size and making the LIL a matter of inverting one function; (iv) a one-sided improper mixture (η ≥ 0 only) is well defined but unbounded below as S_n → −∞; (v) the worst-case nonnegative martingale makes a single all-or-nothing attempt, whereas a receding floor lets the floor-hugger make a fresh independent attempt each time f grows, so non-constant floors are exactly multiple-testing scenarios, equivalently M_n + f(n) is a nonnegative semimartingale with a deterministic "subsidy" f.

## Setting and assumptions
- Filtered probability space (Ω, F, (F_n)_{n≥0}, P), discrete time; a supermartingale is adapted with E[M_{n+1} | F_n] ≤ M_n and E|M_n| < ∞ (eq. 1), so the integrability condition of the extended Ville inequality of Wang and Ramdas 2023 is kept [koolenGeneralisationVilleInequality2025, Sec. 1].
- f and g are deterministic, non-decreasing, with −f(0) < g(0); Theorem 2.1 requires E[M_0] ∈ [−f(0), g(0)] (the statement of part (b) prints [−f(n), g(n)], evidently a typo). Corollary 3.1 additionally needs f differentiable and f, g ≥ 0 on R_+.
- Single P (simple null); the composite extension of Ruf et al. 2022 is cited as an orthogonal direction (Sec. 1).
- The LIL (Section 4) assumes X_1, X_2, … independent and conditionally sub-Gaussian with common mean μ, meaning E[e^{η(X_{n+1} − μ)} | F_n] ≤ e^{η²/2} for all η ∈ R (footnote 1); variance proxy 1 (general κ by rescaling, Appendix B). Lemma B.3, the implicit step, is stated for i.i.d. standard normal data while Lemmas 4.1 and B.1 are stated for sub-Gaussian data; the supermartingale property of (8) under sub-Gaussianity is what carries the argument over.
- The guarantee is time-uniform (∀n simultaneously), hence valid under arbitrary stopping; confidence level restricted to δ ≤ 3/5 in Lemma 4.1 (δ ≤ 1 − e^{−1} in Lemma B.3) because d = δ' ≤ 1 is needed for g to be increasing.
- Tightness in Theorem 2.1(b) is over all supermartingales with the given floor and initial mean, not over sub-Gaussian data; nothing is claimed about optimality of the resulting LIL constants.

## Relation to other sources
- [villeEtudeCritiqueNotion1939](villeEtudeCritiqueNotion1939.md): the object generalised; Theorem 1.1 is Ville's Chapter V Theorem 1 for supermartingales. Ville's own LIL work (Chapter V, Petrowsky's upper-class test via an exponential mixture) is the ancestor of the mixture route the paper compares against [koolenGeneralisationVilleInequality2025, Sec. 1].
- [howardTimeuniformNonparametricNonasymptotic2021](howardTimeuniformNonparametricNonasymptotic2021.md): the two standard routes to curved boundaries there, stitching over geometric epochs (Thm 1, a weighted union bound) and proper mixtures (Lemma 2, √(v log v) for continuous priors, log log for Balsubramani's 1/(λ log^s λ^{−1}) density), are exactly the "slicing" and proper-mixture constructions the paper wants to replace. The improper prior e^{−η²/2} dη/|η| is the infinite-mass endpoint of that family: it reaches the √(2 ln(ln n/δ)) rate with a single integral and no epoch bookkeeping, at the price of a supermartingale that is not nonnegative. The multiple-testing reading of the receding floor (Sec. 5) is the exact counterpart of the union bound inside stitching, now with an exact rather than Bonferroni price [koolenGeneralisationVilleInequality2025, Secs 1, 4, 5].
- [ramdasGametheoreticStatisticsSafe2023](ramdasGametheoreticStatisticsSafe2023.md): cited for Ville's inequality as the workhorse of e-values; that survey's Sec. 2.5 records the other generalisations the paper positions itself against (composite Ville's theorem of Ruf et al. 2022, nonintegrable extension of Wang and Ramdas 2023) [koolenGeneralisationVilleInequality2025, Sec. 1].
- [ramdasHypothesisTestingEvalues2025](ramdasHypothesisTestingEvalues2025.md): the monograph's Fact 7.6 and the randomised Markov material are the fixed-floor, fixed-threshold statements; the paper's Theorem 2.1 adds the time-varying axis. The randomised Ville of Ramdas and Manole 2023 under external stopping is mentioned as a third, separate direction.
- [koolenLogoptimalAnytimevalidEvalues2022](koolenLogoptimalAnytimevalidEvalues2022.md): same first author; that paper studies which e-process to use under optional stopping, this one studies the inequality that certifies any of them. Both rely on a worst-case construction (there a mixture of stopped nulls, here the floor-hugger).
- [shaferTestingBettingStrategy2021](shaferTestingBettingStrategy2021.md): the betting reading of Section 5 (a subsidy f that permits repeated all-or-nothing bets and dilutes the surprise of a gain g) is testing-by-betting language; Shafer and Vovk 2001 Sec. 5.5 is the cited history of LIL via game-theoretic probability.
- [grunwaldSafeTesting2024](grunwaldSafeTesting2024.md): the continuation guarantee "Ville–Robbins" that safe tests rest on is the constant-floor case; the paper does not cite it.
- Without a page: Koolen and van Erven 2015 (COLT), source of the improper-mixture supermartingales (3) bounded below by −1 − ln n, used there for individual-sequence prediction via defensive forecasting; Kaufmann and Koolen 2021 and Balsubramani and Ramdas 2016, proper-mixture finite LILs the paper aims to simplify; Darling and Robbins 1967, Robbins 1970, de la Peña 1999 for the classical LIL inequalities; Ruf, Larsson, Koolen and Ramdas 2022 (composite Ville), Wang and Ramdas 2023 (extended Ville for nonintegrable supermartingales), Ramdas and Manole 2023 (randomised Markov/Ville); Wald 1952 and Shafer and Vovk 2001, 2019 as the fields that use Ville.

## Concepts touched
- [villes-inequality](../concepts/villes-inequality.md)
- [confidence-sequence-boundaries](../concepts/confidence-sequence-boundaries.md)
- [test-martingale](../concepts/test-martingale.md)
- [mixture-and-plug-in-methods](../concepts/mixture-and-plug-in-methods.md)
- [optional-stopping](../concepts/optional-stopping.md)
- [testing-by-betting](../concepts/testing-by-betting.md)

## Versions
arXiv v1 only (22 Feb 2025); the header says "Preprint submitted to SPL: E-values Special Issue". No published version known at ingest; result numbering above follows v1 (Theorem 2.1, Lemma 2.2, Corollary 2.3, Corollary 3.1, Examples 3.2–3.3, Lemma 4.1, Example A.1, Lemmas B.1–B.7, equations (1)–(8), (B.1)–(B.7)).

## Open questions / gaps
- Whether the one-sided improper mixture can be repaired: mixing only over η ≥ 0 gives a well-defined process that is unbounded below as S_n → −∞, so Theorem 2.1 does not apply; the authors call this "a curious downside that invites further investigation" [koolenGeneralisationVilleInequality2025, Sec. 5].
- No comparison of the constants in Lemma 4.1 with the stitched and mixture constants tabulated in Howard et al. (Appendix G there), nor any unimprovability statement for the improper-mixture LIL.
- The bound is tight over supermartingales with a given floor, but the floor f(n) = ln(1+n)/√(2π) of (8) need not be the tightest floor for sub-Gaussian data; how much is lost between the data model and the worst-case floor-hugger is not quantified.
- Composite nulls (uniform-in-P supermartingales), nonintegrable supermartingales, and randomised sharpening are each noted as orthogonal and not combined with the monotone-curve extension (Sec. 1).
- Continuous time: Corollary 3.1 is said to be tight "by an analogue of the floor hugger", but no continuous-time theorem or proof is given.
- Lemma B.3 is stated for i.i.d. standard normal data while Lemma 4.1 claims the sub-Gaussian case; the bridging step is implicit.
- Not in the bib: Koolen and van Erven 2015; Kaufmann and Koolen 2021; Ruf, Larsson, Koolen and Ramdas 2022; Wang and Ramdas 2023; Ramdas and Manole 2023; Balsubramani and Ramdas 2016; Darling and Robbins 1967; Robbins 1970; de la Peña 1999; Shafer and Vovk 2001, 2019.
