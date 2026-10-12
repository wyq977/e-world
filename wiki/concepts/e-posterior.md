---
slug: e-posterior
title: E-posterior and post-hoc decisions
sources: 8
updated: 2026-10-12
---

# E-posterior and post-hoc decisions

## Definition
An e-collection assigns one [e-variable](e-variable.md) S_θ to every parameter value, with E_P[S_θ] ≤ 1 whenever φ(P) = θ; the e-posterior is P̄(θ | y) = 1/S_θ(y) [grunwaldEposterior2023, eqs 3–4]. It is used with any loss, specified after seeing the data, through the risk bound R̄(δ) = sup_θ P̄(θ | Y) L(θ, δ(Y)) and the e-posterior minimax rule; for any collection, any rule and any loss, E_{P_θ}[L(θ, δ(Y))/R̄(δ)] ≤ 1, so a data-dependent weight bounded a priori by B·R̄(δ) ≤ ℓ gives expected loss at most ℓ [grunwaldEposterior2023, Prop. 1, eqs 5–6, 15–16]. A bad e-collection makes the bound loose where a bad prior makes a Bayesian assessment wrong. Its level sets {θ : P̄ ≥ α} are (1 − α) e-confidence sets, so the e-posterior summarises all of them [grunwaldBeyondNeymanPearsonEvalues2024, Sec. 3.4].

## Key results
- Generalised Neyman–Pearson: p-value rules are Type-I risk safe only under binary losses fixed independently of the data; with four actions and losses 0/20/100/500·ℓ the naive p-rule has risk 2.6ℓ and risk grows without bound as actions are added. The maximally compatible rule "largest a with L(0, a) ≤ S(y)·ℓ" with any pre-fixed e-variable is safe for any number of actions; Type-I risk safety is equivalent to e-compatibility, and every admissible rule is maximally compatible with some e-variable [grunwaldBeyondNeymanPearsonEvalues2024, eqs 4–7, 15, Prop. 1, Thm 1].
- Roving α: α̂ = ℓ/S(y) is wrong as a conditional error rate but right as a roving bound ℓ/α̂ on the Type-I loss one may incur, the quasi-conditional paradigm; ℓ itself must be data-independent [grunwaldBeyondNeymanPearsonEvalues2024, Sec. 5.1–5.2; grunwaldEposterior2023, Sec. 2].
- Confidence distributions, objective-Bayes and fiducial posteriors can have infinite true risk under data-dependent weights, while the e-posterior remains valid; the flat-prior posterior N(θ̂, 1/n) can believe risk 1 when actual risk exceeds any k* under a stopping rule [grunwaldEposterior2023, Example 7; grunwaldBeyondNeymanPearsonEvalues2024, Sec. 3.3].
- Tightness: the two-point UMP-Bayes-factor e-process for Gaussian location gives max_θ (θ − θ̂)² P̄ = 1.45/n, the MLE is e-posterior minimax, extended to regular one-dimensional exponential families; the e-CI is about 1.4 times wider than the classical one (2.72/√n vs 1.96/√n at α = 0.05) but valid at unknown stopping times [grunwaldEposterior2023, eq. 24, SM Thm 1, Prop. 3; grunwaldBeyondNeymanPearsonEvalues2024, Example 4].
- Berger–Brown–Wolpert conditional error probabilities, Kiefer's conditional confidence and Vovk's confidence estimators are degenerate e-posteriors, e-specifications rather than e-processes; the (1 − α)/α device is the BBW collection at w = 1/2 and does not extend to an e-process [grunwaldEposterior2023, Sec. 3.2, eqs 31–33].
- Capped and dampened e-posteriors: min{1, P̄}, Condition Zero, dampening (1 − γ) + γS costs only a log n factor; twice the capped risk is valid for every rule and continuation-friendly [grunwaldEposterior2023, Def. 1, eq. 35, Prop. 2].
- For simple nulls GRO e-variables are pure Savage–Dickey, which assess estimation worse (R̄ ≳ n^{−1/2}) than the two-point collection (1.45/n), so GRO is not the design criterion for e-collections and no reference-e-collection theory exists [grunwaldEposterior2023, Example 11, Conclusion].
- The reply to the Safe Testing discussion uses the e-posterior to answer the (1 − α)/α threshold question and to remove right-Haar non-uniqueness [grunwaldAuthorsReplyDiscussion2024, Secs 3, 5]; the survey's appendices present the e-posterior as the decision-theoretic summary where Neyman–Pearson is inadequate [ramdasGametheoreticStatisticsSafe2023, Apps A–B].
- Koning and van Meer's test induction reports a whole family of tests per null element for continuation, a construction they connect to the e-posterior [koningAnytimeValidityFree2026, Thm 6].
- Koning's binary setting is the two-action special case; the roving α̂ = ℓ/S(y) and 'reject at level p = 1/e' are the same device [koningPosthocAlphaHypothesis2023, App. A]. The betting paper's plots of 1/K_t(m) against m, an unnormalised 'confidence distribution' whose superlevel sets are confidence sequences, are the independent e-posterior plot credited on this page [waudbysmithEstimatingMeansBounded2020, App. D.5].
- The capped e-posterior min{1, 1/e_θ} is the contour of an anytime-valid possibilistic inferential model; its Choquet upper-expected-loss guarantee generalises the capped e-posterior risk bound and allows data-dependent actions; with a knowledge-based regularizer the same holds under an upper joint distribution [martinRegularizedEprocessesAnytime2024, Thms 2–4, Sec. 4.3]; see [regularized-e-processes](regularized-e-processes.md).

## Variants and related concepts
- [post-hoc-validity](post-hoc-validity.md), [confidence-sets-and-sequences](confidence-sets-and-sequences.md), [bayes-factor-e-variable](bayes-factor-e-variable.md).

## Sources
- [grunwaldEposterior2023](../sources/grunwaldEposterior2023.md) — primary source.
- [grunwaldBeyondNeymanPearsonEvalues2024](../sources/grunwaldBeyondNeymanPearsonEvalues2024.md) — generalised Neyman–Pearson, roving α, e-CIs.
- [grunwaldAuthorsReplyDiscussion2024](../sources/grunwaldAuthorsReplyDiscussion2024.md) — uses in the reply.
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md) — appendices.
- [koningAnytimeValidityFree2026](../sources/koningAnytimeValidityFree2026.md) — families of tests and continuation.
- [koningPosthocAlphaHypothesis2023](../sources/koningPosthocAlphaHypothesis2023.md), [waudbysmithEstimatingMeansBounded2020](../sources/waudbysmithEstimatingMeansBounded2020.md) — related constructions.
- [martinRegularizedEprocessesAnytime2024](../sources/martinRegularizedEprocessesAnytime2024.md) — inferential-model reading.

## Disagreements / open issues
- GRO e-values are unavailable for GLMs and Cox models without model-X; the authors see the bigger obstacle as sociological [grunwaldBeyondNeymanPearsonEvalues2024, Secs 4.1, 5.4].
- The reciprocal 1/S_θ was plotted earlier by Waudby-Smith and Ramdas and by Pawel, Ly and Wagenmakers; the decision-theoretic use is the novelty [grunwaldEposterior2023, Sec. 1].
