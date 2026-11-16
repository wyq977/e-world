---
citekey: topsoeInformationtheoreticalOptimizationTechniques1979
title: "Information-theoretical optimization techniques"
authors: [Flemming Topsøe]
year: 1979
status: published
public: true
note: "Recasts maximum entropy and minimum discrimination information as zero-sum games between an observer choosing a code and nature choosing a distribution; for any convex set the game has a value and a unique optimal code, adapted to a 'center of attraction' that may lie outside the set and satisfies a Pythagorean inequality; the minimax result behind GROW e-variables for a simple null."
links:
  pdf: "http://dml.cz/dmlcz/124320"
  arxiv: ""
  doi: ""
  video: ""
tags: [information-projection, generalized-i-projection, maximum-entropy, minimum-discrimination-information, minimax, game-theory, codes, kl-divergence, pythagorean-theorem, exponential-families, history]
ingested: 2026-11-16
version: "publisher-oa: Kybernetika 15(1):8–27, 1979 (DML-CZ scan)"
---

# Information-theoretical optimization techniques

## Summary
The paper argues that a game-theoretical viewpoint underlies both the maximum entropy principle and the minimum discrimination information principle [topsoeInformationtheoreticalOptimizationTechniques1979]. A code is a set function κ with Σ_{A ∈ π} e^{−κ(A)} = 1 for every countable decomposition π (1), in bijection with distributions through κ(A) = log(1/η(A)) (2). Given a set C of "consistent" distributions, nature picks μ ∈ C and the observer picks a code; the cost is the average code length ⟨κ, μ⟩. In the absolute game (discrete state space) nature's optimal strategies are the maximum entropy ("canonical") distributions; in the relative game (arbitrary state space, reference distribution η, codes replaced by code improvements) they are the minimisers of D(μ ‖ η). The main results hold for every convex C with finite value, with no closedness assumption: there is a unique distribution, the center of attraction, to which every entropy-maximising (or divergence-minimising) sequence converges; it need not belong to C; it satisfies a strengthened inequality that characterises it; the game has a value; and the code adapted to the center of attraction is the observer's unique optimal strategy. A final section works out a discrete system with energy levels, where the centers of attraction form the exponential family and a critical case shows the center of attraction outside C. The author states that the main novelty is the game-theoretical point of view and credits discussions with Csiszár for replacing a general minimax inequality by an intrinsically information-theoretical argument.

## Main results
- **Absolute game (discrete state space).** α = sup_{μ ∈ C} inf_κ ⟨κ, μ⟩, β = inf_κ sup_{μ ∈ C} ⟨κ, μ⟩; α ≤ β; the value exists if they agree. A code is cost-stable if ⟨κ, μ⟩ is finite and constant over C. Lemmas 2–3: ⟨κ, μ⟩ = H(μ) + D(μ ‖ η) for κ adapted to η, so min_κ ⟨κ, μ⟩ = H(μ), attained only by the code adapted to μ when H(μ) < ∞; hence α = H_max(C) = sup_{μ ∈ C} H(μ) and nature's optimal strategies are the canonical distributions. Lemma 4: H(Σ p_ν μ_ν) = Σ p_ν H(μ_ν) + Σ p_ν D(μ_ν ‖ Σ p_ν μ_ν) [topsoeInformationtheoreticalOptimizationTechniques1979].
- **Theorem 1 (center of attraction).** If C is convex and H_max(C) < ∞, there is a unique distribution μ_C with μ_n → μ_C for every sequence in C with H(μ_n) → H_max(C). Proof by Lemma 4 at the midpoint and Pinsker's inequality: the sequence is Cauchy in total variation. μ_C lies in the closure of C and H(μ_C) ≤ H_max(C); neither μ_C ∈ C nor H(μ_C) = H_max(C) need hold. "We do not wish to assume that C is closed" [topsoeInformationtheoreticalOptimizationTechniques1979].
- **Theorem 2.** For every μ ∈ C: H(μ) + D(μ ‖ μ_C) ≤ H_max(C). Proposition 1: this inequality characterises μ_C. The paper remarks that results up to here are analogous to Csiszár 1975 [topsoeInformationtheoreticalOptimizationTechniques1979].
- **Theorem 3 (value of the absolute game).** For convex C with H_max(C) < ∞ the value exists and equals H_max(C); the code κ_C adapted to μ_C is optimal for the observer and uniquely so: for any code κ adapted to η, sup_{μ ∈ C} ⟨κ, μ⟩ ≥ H_max(C) + D(μ_C ‖ η) (14). Nature has an optimal strategy iff μ_C ∈ C and H(μ_C) = H_max(C) [topsoeInformationtheoreticalOptimizationTechniques1979].
- **Theorems 4–5 (cost-stability).** If μ_C is canonical and an algebraic inner point of C, then κ_C is cost-stable. Conversely, if κ* adapted to μ* is cost-stable and μ* satisfies an approximation condition slightly stronger than lying in the closure of C, then H_max(C) < ∞ and μ* = μ_C [topsoeInformationtheoreticalOptimizationTechniques1979].
- **Theorems 6–7 (topology).** Conditions for H_max(C) < ∞ (Baire-space arguments; sets cut out by an affine lower semicontinuous function), and: a convex C with H_max(C) < ∞ is relatively compact. H_max(C) < ∞ does not imply H_max(co(C)) < ∞ in general (one-point masses) [topsoeInformationtheoreticalOptimizationTechniques1979].
- **Relative game (arbitrary state space).** Reference distribution η with reference code; a code improvement Δ; M_η the distributions and K_η the code improvements relative to η. Lemma 5 (a restatement of Csiszár 1975, eq. 2.6): for Δ* adapted to μ*, ⟨Δ*, μ⟩ = D(μ ‖ η) − D(μ ‖ μ*) whenever the right side is well defined. Lemma 6: max_Δ ⟨Δ, μ⟩ = D(μ ‖ η), so nature's optimal strategies minimise D(μ ‖ η) over C. Lemma 7: Σ p_ν D(μ_ν ‖ η) = D(Σ p_ν μ_ν ‖ η) + Σ p_ν D(μ_ν ‖ Σ p_ν μ_ν). D(· ‖ ·) is jointly lower semicontinuous in the weak topology; sublevel sets of D(· ‖ η) are weakly compact and convex but, as Csiszár pointed out to the author, need not be strongly compact [topsoeInformationtheoreticalOptimizationTechniques1979].
- **Theorem 8 (relative center of attraction).** Let C ⊆ M_η be convex with D_min(C ‖ η) = inf_{μ ∈ C} D(μ ‖ η) < ∞. Then there is a unique μ_{C‖η} ∈ M_η with μ_n → μ_{C‖η} strongly for every sequence in C with D(μ_n ‖ η) → D_min(C ‖ η), and for every μ ∈ C, (17) D(μ ‖ η) ≥ D_min(C ‖ η) + D(μ ‖ μ_{C‖η}). Proof "analogous to the proofs of Theorems 1 and 2"; "a slight improvement over" Csiszár 1975. (17) also characterises μ_{C‖η}. Checked against the page image (p. 21) [topsoeInformationtheoreticalOptimizationTechniques1979].
- **Theorem 9 (value of the relative game).** Let C ⊆ M_η be convex with D(μ ‖ η) < ∞ for all μ ∈ C. Then the value of the relative game exists and is D_min(C ‖ η); the code improvement Δ_{C‖η} adapted to μ_{C‖η} is the observer's optimal strategy, uniquely: for any Δ* with distribution μ*, inf_{μ ∈ C} ⟨Δ*, μ⟩ ≤ D_min(C ‖ η) − D(μ_{C‖η} ‖ μ*). μ_{C‖η} is optimal for nature iff it is in C. The author writes that the theorem "probably" holds under the weaker assumption D_min(C ‖ η) < ∞ and says what would have to be proved [topsoeInformationtheoreticalOptimizationTechniques1979].
- **Theorem 10.** In the discrete case, if the code adapted to η is cost-stable for the absolute game C, then μ_{C‖η} = μ_C: maximising entropy and minimising divergence from η coincide [topsoeInformationtheoreticalOptimizationTechniques1979].
- **A special case (after Ingarden and Urbanik).** Countably many states with energies E_i, partition function Z(x) = Σ e^{−xE_i}, abscissa of convergence γ, distributions μ_x(i) = e^{−xE_i}/Z(x), C(E) the distributions with mean energy E (or at most E). Theorem 11, for γ < ∞: H_max(E) < ∞; the codes κ_x are cost-stable for C(E); for E_min < E ≤ E_crit the center of attraction is canonical and is the unique member of the exponential family (μ_x) with mean energy E; for E_crit < E < ∞ the center of attraction is μ_γ, which is not canonical: its mean energy is below E and H(μ_γ) < H_max(E). So {μ : ⟨E, μ⟩ ≤ E} can be a compact convex set with finite maximal entropy and no maximum entropy distribution. Theorem 12: every distribution with finite mean energy has finite entropy iff γ < ∞ [topsoeInformationtheoreticalOptimizationTechniques1979].

## Setting and assumptions
- Absolute game: discrete (countable) state space. Relative game: arbitrary measurable space with a fixed reference distribution η.
- C is convex and has finite value (H_max or D_min); it is never assumed closed. Theorem 9 additionally assumes D(μ ‖ η) < ∞ for every μ ∈ C.
- Codes are idealised: real-valued lengths with equality in Kraft's inequality.
- No sampling, no tests, no e-values. The author calls the setting "very simple" and asks for extensions.

## Relation to other sources
- [csiszarIDivergenceGeometryProbability1975](csiszarIDivergenceGeometryProbability1975.md): Theorems 1–2 and 8 are the analogues of its Theorems 2.1–2.2 with the closedness assumption removed; Lemma 5 is its identity (2.6).
- [csiszarSanovPropertyGeneralized1984](csiszarSanovPropertyGeneralized1984.md): renames the relative center of attraction the generalized I-projection and cites Theorem 8 for the Pythagorean inequality in that generality.
- [grunwaldGrowthOptimalEVariablesExtension2024a](grunwaldGrowthOptimalEVariablesExtension2024a.md): its Proposition 1 is described on that page as weakening Theorem 9 here, which needs D(μ ‖ η) finite on all of C. Wiki's reading of the dictionary: η is the simple null P_0, C the alternative, a code improvement Δ = log(q/p_0) is the logarithm of an e-variable, ⟨Δ, μ⟩ is its growth rate under μ, the value of the relative game is GROW, and the observer's optimal strategy is the GROW e-variable p*/p_0 with p* the density of the relative center of attraction. The paper itself has no such vocabulary.
- [grunwaldSafeTesting2024](grunwaldSafeTesting2024.md): cites this paper, with Grünwald–Dawid 2004, in the proof of its Theorem 1 in full generality (per that source page).
- [giuffridaTestingMaximumEntropy2025](giuffridaTestingMaximumEntropy2025.md): maximum-entropy models as the object of testing; this paper is the game-theoretic account of the principle those models rest on. Wiki's reading.

## Concepts touched
- [information-projection](../concepts/information-projection.md)
- [reverse-information-projection](../concepts/reverse-information-projection.md)
- [gro-criterion](../concepts/gro-criterion.md)
- [mdl-and-maximum-entropy-e-values](../concepts/mdl-and-maximum-entropy-e-values.md)
- [testing-by-betting](../concepts/testing-by-betting.md) (observer-versus-nature game; Wiki's reading)
- [exponential-family-e-values](../concepts/exponential-family-e-values.md)

## Versions
Only the Kybernetika version exists, freely available from the Czech Digital Mathematics Library. The Zotero record gives the pages as "(8)–27". The text layer is the library's OCR, with most displays garbled; Theorems 1–3, 8–11, Proposition 1 and Lemmas 3–7 were read from page images, the rest (Theorems 4–7, 12, the proofs of the special case) from OCR only.

## Open questions / gaps
- Whether Theorem 9 holds assuming only D_min(C ‖ η) < ∞ (left open by the author; the CSC paper's Proposition 1 addresses the simple-null case).
- Whether an algebraic-inner center of attraction must be canonical ("probably not true"), and whether all cost-stable codes in the special case are of the form κ_x ("probably").
- The results analogous to Theorems 4–5 for the relative game are "left to the reader".
- Cited works not in the bib: Ingarden and Urbanik 1962 (Quantum informational thermodynamics); Čencov 1972; Kullback 1959; Jaynes 1957; Barndorff-Nielsen 1978 (Information and exponential families; in Zotero); Topsøe 1974 (Informationstheorie); Rényi 1962; Perez 1957; Kallianpur 1960; Bayer and Ochs 1973; Vincze 1972.
