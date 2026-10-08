---
slug: optional-stopping
title: Optional stopping and sequential decomposability
sources: 9
updated: 2026-10-08
---

# Optional stopping and sequential decomposability

## Definition
Optional stopping means ending a single data stream at a data-dependent time. An e-value test is safe under optional stopping only if its e-specification is sequentially decomposable (seqdec), that is, s[n] factors as a product of conditional e-variables s_i, and the stopping time is adapted to the e-variable's possibly coarsened filtration [grunwaldSafeTesting2024, Sec. 5]. Otherwise one can construct fake conditional e-variables and lose the guarantee. Under these conditions the product is a [test martingale](test-martingale.md) and [Ville's inequality](villes-inequality.md) applies; the general object that is valid at every stopping time is the [e-process](e-process.md) [ramdasHypothesisTestingEvalues2025, Def. 7.3].

## Key results
- Seqdec has three properties: it permits stopping within studies, concatenated-data martingales, and coherence of local and global analysis; plug-in versus sequential application and the t-test coarsened-filtration caveat [grunwaldSafeTesting2024, Sec. 5, Fig. 3].
- REGROW for the 2×2 table is not seqdec, but a Beta(0.18, 0.18) sequential prior is almost REGROW [grunwaldSafeTesting2024, Example 9].
- Expected and worst-case sample sizes under optional stopping [grunwaldSafeTesting2024, Sec. 6]; see [e-power](e-power.md).
- The Safe Testing authors concede that "safe" was a poor name and that the "fewer samples" claim refers only to binary decisions [grunwaldSafeTesting2024, reply].
- SAVI (safe anytime-valid inference) versus Wald's sequential paradigm is contrasted on four points [ramdasHypothesisTestingEvalues2025, Sec. 7.2].
- Randomised (behavioural) stopping times τ: X^{≤T} → [0,1] and stopped distributions P^τ; closed under mixtures, which Lagrange duality needs; the alternative's stopping time σ is a prediction and the log-optimal e-value depends on it except in point-RIPr cases [koolenLogoptimalAnytimevalidEvalues2022, eq. 1, Prop. 6, Thms 8, 12].
- Filtration choice as a design parameter: shrinking the filtration (an Intermediary discarding information, conformal p-values, the scale-free V_i = X_i/|X_1|) can create nontrivial test martingales and raise growth, at the cost of safety only for stopping times measurable in the shrunk filtration [ramdasGametheoreticStatisticsSafe2023, Secs 1.2, 4.1.2, 5.5, 8.2.2].
- Time-uniform validity makes arbitrary stopping harmless; the running-intersection and reset discussion shows a failure mode when stationarity is false [howardTimeuniformNonparametricNonasymptotic2021, Lemma 3, Sec. 6].
- Ville derived the martingale condition from fairness under every non-randomised stopping rule, with expectation one when the game ends almost surely [villeEtudeCritiqueNotion1939, Ch. V §1].
- Applied: block-wise stopping with pre-fixed block sizes, Fisher's exact test losing type-I control under the same stopping [turnerGenericEvariablesExact2024, Sec. 3.1, Fig. S4.1]; level α at any random time for survival data, no anytime-valid trial is 'doomed' [terschureAnytimevalidLogrankTest2024, Prop. 3.1, Sec. 8.3].
- Composite alternatives under (RE)GROW may need a coarser filtration; interim analysis is a bonus 'not always' available; 'design by filtration change' floated as possibly unifiable with information projection [grunwaldAuthorsReplyDiscussion2024, Secs 1, 4].

## Variants and related concepts
- [optional-continuation](optional-continuation.md), the study-level version.
- [confidence-sets-and-sequences](confidence-sets-and-sequences.md).

## Sources
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — Section 5 in full, Example 9, eq. 31.
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — e-process definition, Chapter 7.
- [koolenLogoptimalAnytimevalidEvalues2022](../sources/koolenLogoptimalAnytimevalidEvalues2022.md) — randomised stopping times.
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md) — filtration choice.
- [howardTimeuniformNonparametricNonasymptotic2021](../sources/howardTimeuniformNonparametricNonasymptotic2021.md), [villeEtudeCritiqueNotion1939](../sources/villeEtudeCritiqueNotion1939.md) — time-uniform validity, fairness.
- [turnerGenericEvariablesExact2024](../sources/turnerGenericEvariablesExact2024.md), [terschureAnytimevalidLogrankTest2024](../sources/terschureAnytimevalidLogrankTest2024.md) — applied guarantees.
- [grunwaldAuthorsReplyDiscussion2024](../sources/grunwaldAuthorsReplyDiscussion2024.md) — filtration coarsening.

## Disagreements / open issues
- When a GRO criterion admits a seqdec or ε-seqdec specification is open [grunwaldSafeTesting2024, eq. 31].
- Approximate optional stopping for non-e-process e-variables is conjectured [haoEValuesExponentialFamilies2025, Sec. 7].
