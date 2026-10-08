---
citekey: haoEValuesExponentialFamilies2025
title: "E-values for exponential families: the general case"
authors: [Yunda Hao, Peter D. Grünwald]
year: 2025
status: preprint
public: true
note: "Derives and compares the RIPr-optimal, conditional, universal-inference and sequential plug-in e-variables for exponential family nulls, including the 'anti-simple' case where the optimal e-variable is not a simple likelihood ratio, and shows the conditional e-variable loses only o(1) e-power against the optimum while UI loses (d/2) log n."
links:
  pdf: ""
  arxiv: https://arxiv.org/abs/2409.11134
  doi: 10.48550/arXiv.2409.11134
  video: ""
tags: [e-values, exponential-families, reverse-information-projection, gro, universal-inference, conditional-e-variable, e-power, asymptotics]
ingested: 2026-10-08
version: "arxiv 2409.11134v2 (26 Aug 2025)"
---

# E-values for exponential families: the general case

## Summary
For a composite null P that is a regular d-dimensional exponential family (mean-value parameterisation, i.i.d. data), the paper analyses four e-statistics: the growth-rate-optimal (GRO) RIPr e-variable S_RIP = q(U^n)/p_{RIPr}(U^n), its sequentialised version S_SEQ-RIP built from per-outcome RIPrs, the universal-inference e-variable S_UI = q(U^n)/sup_μ p_μ(U^n), and a conditional e-variable S_COND = q(U^n | Z)/p(U^n | Z) with Z the minimal sufficient statistic [haoEValuesExponentialFamilies2025]. Earlier solved cases (grunwaldOptimalEValuesExponential2024 and the k-sample and regression examples) were all "simple" or "super-simple": the RIPr was a single element of P, so the optimal e-variable reduced to a likelihood ratio. This paper identifies the complementary "anti-simple" case (Σ_q − Σ_p positive semidefinite) in which the RIPr is a genuine Bayes mixture, computes it exactly for Gaussian location families (the RIPr prior is Gaussian with covariance (Σ_q − Σ_p)/n) and asymptotically for general exponential families, and shows S_RIP = S_COND exactly (Gaussian) or up to o(1) in e-power (general). It then gives e-power expansions up to o(1) for all four statistics under both simple and composite (same-sufficient-statistic exponential family) alternatives, with plug-in and Bayes-mixture learning of the alternative. The headline: S_COND, which needs neither a prior nor an estimator, is within o(1) of the optimum; UI loses (d/2) log n + O(1); plug-in SEQ-RIP loses (d_qp/2) log n in the simple case but a linear nε in the anti-simple case [haoEValuesExponentialFamilies2025]. Type-I guarantees of all four are nonasymptotic; only the e-power comparisons are asymptotic.

## Main results

### Objects (Section 1, 1.1)
- E-power of an e-variable S^(n) under simple alternative Q is E_Q[log S^(n)] (eq. 1.1); the GRO e-variable maximising it is S_RIP = q/p_{RIPr(q)} with the RIPr of Q(U^n) onto CONV{P(U^n)} (eq. 1.2), by [grunwaldSafeTesting2024, Thm 1] [haoEValuesExponentialFamilies2025].
- S_SEQ-RIP (eq. 1.3): product over i of q*(U_i | U^{i-1}) divided by the local RIPr of that conditional onto CONV(P(U_i)); an e-process by construction.
- S_COND (eq. 1.6): with Z = n^{1/2} μ̂_n (scaled sufficient statistic), S_COND = q(U^n | Z)/p(U^n | Z); the denominator is the same for every P in P (and every prior W on M_p) by sufficiency, and E_P[S_COND] = 1 by conditioning (eq. 1.13).
- S_UI (eq. 1.7): q(U^n)/p_{μ̂_n}(U^n), the standard instantiation of universal inference [wassermanUniversalInference2020].
- Composite Q handled by prequential plug-in μ̆_n = (x_0 n_0 + Σ x_i)/(n + n_0) (eq. 2.12) giving S_{μ̆,UI}, S_{μ̆,SEQ-RIP} (eq. 2.13), and by Bayes mixtures with prior W_1 on M_q giving S_{W_1,UI}, S_{W_1,RIP} (eq. 2.14).
- Generalised KL D_R(Q‖P) = E_R log q/p = D(R‖P) − D(R‖Q) (eq. 1.14); d_ab = TR(Σ_a Σ_b^{-1}); D_GAUSS(B) = ½(−log det B − (d − TR B)); D_{Σ_r}(Σ_q‖Σ_p) = D_GAUSS(Σ_r Σ_p^{-1}) − D_GAUSS(Σ_r Σ_q^{-1}) (eqs 2.1–2.3).

### Simple vs anti-simple (Definition 1, Section 3.1)
- P and Q are "matching pairs" if both regular, same sufficient statistic, M_q ⊆ M_p and B_p ⊆ B_q for every matching canonical parameterisation. Simple case: matching pair and Σ_q(μ) − Σ_p(μ) negative semidefinite for all μ (strictly simple: negative definite). μ-anti-simple: Σ_q(μ) − Σ_p(μ) positive semidefinite (strict: positive definite); matching is not required. The simple case is from grunwaldOptimalEValuesExponential2024; the anti-simple case is new here [haoEValuesExponentialFamilies2025].
- In the simple case the RIPr of Q_{μ*}^{(n)} is P_{μ*}^{(n)} and S_RIP = q_{μ*}/p_{μ*} (corollary of grunwaldOptimalEValuesExponential2024, Thm 1).

### Gaussian location, simple Q (Theorem 1, Section 2.1)
P = N(μ, Σ_p), Q = N(μ*, Σ_q), data i.i.d. R with mean μ* and covariance Σ_r (R ≠ Q allowed: misspecified). Then:
1. UI: E_R[log S_UI] = n D_R(Q‖P_{μ*}) − d_rp/2 (eq. 2.6).
2. COND: E_R[log S_COND] = (n − 1) D_R(Q‖P_{μ*}) = n D_R − D_{Σ_r}(Σ_q‖Σ_p) (eq. 2.7).
3. Simple case (Σ_q − Σ_p ≤ 0): S_RIP = S_SEQ-RIP = q/p_{μ*}, e-power n D_R (eq. 2.8). Anti-simple case (≥ 0): S_SEQ-RIP ≡ 1, trivial.
4. Anti-simple case: S_RIP = q(U^n)/p_{W_0}(U^n) = S_COND exactly, with W_0 = N(μ*, (Σ_q − Σ_p)/n) the RIPr prior (eq. 2.9). Key mechanism: under P_{W_0} the sufficient statistic Z has the same law as under Q, so the Bayes factor equals the conditional ratio (Lemma 1, Prop. 2) [haoEValuesExponentialFamilies2025].
- Corollary 1: E_Q[log S_RIP/S_UI] = d/2 + ½ Σ_j log λ_j > d/2 (strict anti-simple) and = d_qp/2 < d/2 (strict simple), λ_j the eigenvalues of Σ_p^{-1/2} Σ_q Σ_p^{-1/2}; the gap is O(1), not growing in n.

### Gaussian location, composite Gaussian Q (Theorem 2, Section 2.2)
1. UI: E_R[log S_{μ̆,UI}] = n D_R(Q_{μ*}‖P_{μ*}) − (d_rq/2) log n + O(1) (eq. 2.15); E_R[log S_{W_1,UI}] = n D_R − (d/2) log(n/2π) + O(1) (eq. 2.16), with explicit O(1) terms in eq. 2.17 and Remark 5.
2. COND: E_R[log S_COND] = (n − 1) D_{Σ_r}(Σ_q‖Σ_p) (eq. 2.18).
3. Simple case: local RIPr of Q_{μ̆_{i-1}} is P_{μ̆_{i-1}}, and E_R[log S_{μ̆,SEQ-RIP}] = n D_R + ((d_rp − d_rq)/2) log n + O(1) (eq. 2.19). Anti-simple: S_{μ̆,SEQ-RIP} ≡ 1.
4. General: whenever Π_1 + (Σ_q − Σ_p)/n ≥ 0 (always in the anti-simple case), the RIPr of Q_{W_1}(U^n) is P_{W_0} with W_0 = N(μ_1, Π_1 + (Σ_q − Σ_p)/n) and S_{W_1,RIP} = S_COND exactly (eqs 2.20–2.21).
- Corollary 2: E_Q[log S_COND] > nε; S_{W_1,UI} vs S_{μ̆,UI} differ by O(1); COND beats UI by (d/2) log n + O(1); SEQ-RIP beats UI by (d_qp/2) log n + O(1) with d_qp ≤ d in the simple case; S_{W_1,RIP}/S_COND has e-power gap 0 in the anti-simple case.
- Remark 6 / eq. 2.24: the right-Haar-prior Bayes factor S_HAAR of Pérez-Ortiz et al. (perezortizEStatisticsGroupInvariance2024, not in bib) has e-power (n − 1) D_{Σ_r}(Σ_q‖Σ_p), hence S_HAAR = S_COND by GROW uniqueness [haoEValuesExponentialFamilies2025].

### General exponential family, simple Q (Theorem 3, Section 3.2)
Requires 3 moments of X under R and Q, D_R(Q‖P_{μ*}) finite. Regularity: Condition 1 (COND): X has an MGF under Q and R, is either lattice or has a bounded continuous density, common support, and log p_{μ*}/q grows at most polynomially (eq. 3.2); needed for a multivariate local CLT with rates (Bhattacharya–Rao). Condition 2 (UI ≥): E_R[1{‖μ̂_n − μ*‖ ≥ n^{-γ}} n D(P_{μ̂_n}‖P_{μ*})] = o(1).
1. UI: E_R[log S_UI] ≤ n D_R − d_rp(μ*)/2 + o(1), equality under Condition 2 (eq. 3.3). With Q ∈ P this is Wilks' phenomenon (expected χ²_d/2).
2. COND: under Condition 1, E_R[log S_COND] ≥ n D_R − D_{Σ_r}(Σ_q‖Σ_p(μ*)) + o(1); equality if Condition 1 also holds with q and p_{μ*} swapped (eq. 3.4).
3. Simple case: S_RIP = S_SEQ-RIP = q/p_{μ*} for all n (eq. 3.5). Strict anti-simple: E_Q[log S_SEQ-RIP] = n(D(Q‖P_{μ*}) − ε) with ε = D(Q‖P_{μ*}) − D(Q‖P_{RIPr(Q(U))}) > 0 (eq. 3.6), so a linear loss.
4. Anti-simple: with W_{0,(n)} = N(μ*, (Σ_q − Σ_p)/n), E_Q[log S_RIP] ≤ E_Q[log q/p_{W_{0,(n)}}] ≤ n D(Q‖P_{μ*}) − D_{Σ_q}(Σ_q‖Σ_p(μ*)) + o(1) (eq. 3.7; Lemma 2); with Condition 1, equalities up to o(1) and E_Q[log S_RIP] = E_Q[log S_COND] + o(1). Whether q/p_{W_{0,(n)}} is itself an e-variable is left open; S_COND is the provably valid near-GRO substitute.
- Corollary 3: Corollary 1 carries over with d_qp = d_qp(μ*).
- Proposition 1: if Q(X) = P_{μ*}(X) for some μ* (simultaneously nonstrict simple and anti-simple), then S_RIP = S_SEQ-RIP = S_COND = q(U^n | X^n)/p(U^n | X^n) exactly, e-power n D_R(Q‖P_{μ*}); covers Gaussian-location and Poisson k-sample tests (Example 1; haoEValuesKSampleTests2024, not in bib).

### General exponential family, composite exponential-family Q (Theorem 4, Section 3.3)
P, Q matching pairs, P ∩ Q = ∅, M_q ⊆ M_p. Condition 3 (plug-in): m ≥ 3 odd moments under R and E_R[1{‖μ̂_n − μ*‖ ≥ n^{-γ}} n D(Q_{μ*}‖Q_{μ̆_n})] = o(1); sufficient condition eq. 3.9 (at most polynomial KL growth matched by moments). Conditions 2 and 3 are "dual" (KL in opposite directions). Verified for Bernoulli, Poisson, geometric, binomial, negative binomial, Gaussian location-scale (needs 5 moments, Example 2) and Gamma; fails for the Landau family.
1. UI: E_R[log S_{μ̆,UI}] ≤ n D_R − (d_rq(μ*)/2) log n + O(1) (eq. 3.12); E_R[log S_{W_1,UI}] ≤ n D_R − (d/2) log(n/2π) + O(1) (eq. 3.13); equalities under Condition 2.
2. COND: E_R[log S_COND] ≥ n D_R − D_{Σ_r}(Σ_q(μ*)‖Σ_p(μ*)) + o(1) (eq. 3.14), equality with the symmetric Condition 1.
3. Simple case: E_R[log S_{μ̆,SEQ-RIP}] = n D_R + ((d_rp − d_rq)/2) log n + O(1) (eq. 3.15). Strict anti-simple: E_Q[log S_{μ̆,SEQ-RIP}] ≤ n(D − ε) (eq. 3.16).
4. "Most remarkable result": for any prior W_1 with positive continuous density near μ*, E_Q[log S_{W_1,RIP}] ≤ E_Q[log q_{W_1}/p_{W_1}] = n D − D_{Σ_q}(Σ_q(μ*)‖Σ_p(μ*)) + o(1) (eq. 3.17), equality under Condition 1: the RIPr of the Bayes mixture Q_{W_1} is approximately the Bayes marginal P_{W_1} under the same prior, in simple and anti-simple cases alike (Laplace approximation, eq. 6.3) [haoEValuesExponentialFamilies2025].
- Corollary 4 (= eqs 1.9–1.12): E_Q[log S_RIP/S_COND] = o(1); E_Q[log S_COND/S_UI] ≥ (d/2) log n + O(1); E_Q[log S_SEQ-RIP/S_UI] ≥ (d_qp(μ*)/2) log n + O(1) with d_qp ≤ d in the simple case; E_Q[log S_SEQ-RIP/S_COND] ≤ −nε in the strict anti-simple case. The (d/2) log n term is the BIC penalty, from the same Laplace approximation.

### Examples and simulations (Section 4, Appendix D)
- Bernoulli 2-sample test (simple case; d = 1): Q_GEN is the set of (μ_a, μ_b) with fixed log-odds ratio δ*; uniform prior on β ∈ [−10, 10]; δ* ∈ {1, 2, 2 log 19 ≈ 5.9}. S_{W_1,RIP}, S_COND and the pseudo-e-variable q_{W_1}/p_{W_1} converge in e-power at small n; S_COND loss converges to D_GAUSS(d_qp) ≈ 0.425 for (0.95, 0.05). SEQ-RIP loses c log n with c = (μ_a − μ_b)²/(2(μ_a + μ_b)(2 − μ_a − μ_b)) (eq. 4.3), near 0 except at extreme corners. Computing S_{W_1,RIP} by numerical KL minimisation was infeasible for δ* ≈ 5.9; the valid S_COND is squeezed between the two computable curves [haoEValuesExponentialFamilies2025].
- Exponential 2-sample test (strict anti-simple; effect size δ = 1/μ_a − 1/μ_b, δ* = −1, D ≈ 0.2877): S_COND and q_{W_1}/p_{W_1} are indistinguishable; S_{μ̆,SEQ-RIP} loses linearly as eq. 3.16 predicts, though it beats UI in a large initial regime (n ≤ 200 computed).

### E-process-ness (Section 7, Appendix E)
- Proposition 7: if S^(n) = q(U^n)/p_{W_n}(U^n) are e-variables with Q(P_{W_n}(U^n) ≠ P_{W_{n+1}}(U^n)) > 0 for some n, then (S^(n)) is not an e-process in the data filtration. Hence S_RIP = S_COND is not an e-process in the Gaussian anti-simple cases (W_0 depends on n); S_HAAR is an e-process only in the coarser filtration of (X_i − X_1). S_COND is an e-process in the Proposition 1 settings. In the composite general case the approximate RIPr prior W_1 does not depend on n, suggesting "approximate" optional stopping [haoEValuesExponentialFamilies2025].

## Setting and assumptions
- Null: regular d-dimensional exponential family P = {P_μ : μ ∈ M_p}, M_p open convex, Σ_p(μ) positive definite; data U_1, U_2, … i.i.d.; sufficient statistic X = t(U), distinguished from U in general (Example 1).
- Alternative: simple Q with E_Q[X] = μ* ∈ M_p (Thms 1, 3) or a second regular exponential family with the same sufficient statistic forming a matching pair (Thms 2, 4); e-power evaluated under R with the same mean μ* (misspecification allowed).
- Composite Q learned by prequential plug-in with anchor (x_0, n_0 > 0) or Bayes mixture; Gaussian priors only in Theorem 2, general priors in Theorem 4.
- Regularity: Conditions 1–3 above; 3 (or m ≥ 3 odd) moments; MGF of X under Q for the COND result.
- Optional continuation: all four are e-variables at each fixed n. Optional stopping: S_UI and S_SEQ-RIP are e-processes; S_COND and S_RIP generally are not (Appendix E).
- Proof tools: Gaussian KL identities and a nonstandard Laplace approximation with n-dependent prior (Section 5), multivariate local CLT with rates plus exponential concentration (Lemma 6), prequential log-loss analysis generalising grunwaldDeRooij2005 / kotlowskiGrunwald2011 (Proposition 4, Lemma 3).

## Relation to other sources
- [grunwaldSafeTesting2024](grunwaldSafeTesting2024.md): supplies the GRO criterion, the RIPr characterisation (Thm 1) and the uniqueness corollary ("at most one prior W_0 makes the Bayes factor an e-variable, and then it is GRO") used in Lemma 1 and in the proofs of Theorems 1–3; this paper computes the RIPr explicitly in a regime where it is nondegenerate.
- [wassermanUniversalInference2020](wassermanUniversalInference2020.md): S_UI is the split/plug-in universal inference statistic; this paper quantifies its e-power deficit as exactly d_rp/2 (simple Q) and (d/2) log n + O(1) (composite Q) relative to S_COND and the GRO optimum.
- [ramdasHypothesisTestingEvalues2025](ramdasHypothesisTestingEvalues2025.md): background on e-processes, method of mixtures and plug-in; this paper's Appendix E gives concrete exponential family cases where the optimal e-variable sequence fails to be an e-process.
- grunwaldOptimalEValuesExponential2024: defines the simple case and proves the RIPr is P_{μ*} there (Thm 1) and that q/p_{μ*} is not an e-variable in the strict anti-simple case (Prop. 2); the present paper is its sequel, covering the anti-simple case and all asymptotics.
- turnerGenericEvariablesExact2024: k-sample Bernoulli (contingency table) tests cited as a "simple yet not super-simple" setting whose e-power loss from SEQ-RIP was previously unquantified.
- ramdasGametheoreticStatisticsSafe2023: cited as the general introduction and for the method of mixtures and plug-in.
- shaferTestingBettingStrategy2021, vovkEvaluesCalibrationCombination2021: cited as key e-value publications only.

## Concepts touched
- [exponential-family-e-values](../concepts/exponential-family-e-values.md)
- [reverse-information-projection](../concepts/reverse-information-projection.md)
- [gro-criterion](../concepts/gro-criterion.md)
- [conditional-e-variable](../concepts/exponential-family-e-values.md)
- [universal-inference](../concepts/universal-inference.md)
- [simple-vs-anti-simple-case](../concepts/exponential-family-e-values.md)
- [sequential-ripr-plug-in](../concepts/exponential-family-e-values.md)
- [method-of-mixtures](../concepts/mixture-and-plug-in-methods.md)
- [e-power](../concepts/e-power.md)
- [e-process](../concepts/e-process.md)

## Versions
The ingested text is arXiv v2 (26 Aug 2025, Bernoulli-style formatting); v1 appeared in September 2024. The text does not state what changed between versions, so no diff is recorded [haoEValuesExponentialFamilies2025].

## Open questions / gaps
- Is q(U^n)/p_{W_{0,(n)}}(U^n) with the Gaussian O(1/n)-variance prior actually an e-variable for general exponential family nulls, or only o(1)-close in e-power? Not resolved (below Theorem 3).
- No general n-free sufficient condition for Condition 2 (UI ≥) in multivariate families; only verified case by case (Poisson, Appendix C.1).
- Formalising "approximate optional stopping" for S_COND and S_RIP, possibly via asymptotic anytime-validity (waudby-smith et al. 2024, time-uniform CLT) or coarser filtrations (Section 7, Appendix E).
- RIPr for plug-in Q* and sequential RIPr for Bayesian Q* not analysed (Remark 3).
- Whether the e-variables remain near-GROW when testing the one-sided alternative δ ≥ δ* rather than δ = δ* (Section 4.1).
- Anti-simple case under misspecification R ≠ Q in the general exponential family setting stated only for R = Q (below Theorem 3).
- Cited works not in the bib: Hao, Grünwald, Lardy, Long, Adams 2024 (k-sample tests); Lardy, Grünwald, Harremoës 2024 (RIPr and optimal e-statistics); Larsson, Ramdas, Ruf 2024 (numéraire e-variable); Pérez-Ortiz, Lardy, de Heide, Grünwald 2024 (group invariance); Hendriksen, de Heide, Grünwald 2021 (optional stopping with Bayes factors); Grünwald and de Rooij 2005; Kotłowski and Grünwald 2011; Waudby-Smith et al. 2024 (asymptotic confidence sequences); Lindon et al. 2024 (anytime-valid linear models); Tse and Davison 2022 (note on UI); Wang, Wang, Ziegel 2022 (e-backtesting, source of the term "e-power").
