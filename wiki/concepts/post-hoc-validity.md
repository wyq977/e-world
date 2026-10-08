---
slug: post-hoc-validity
title: Post-hoc validity and data-dependent α
sources: 10
updated: 2026-10-08
---

# Post-hoc validity and data-dependent α

## Definition
A family of tests (φ_α) is post-hoc valid if E_P[sup_α φ_α / α] ≤ 1, so that the level, the decision set, or the loss may be chosen after seeing the data [ramdasHypothesisTestingEvalues2025, Definition 4.1]. Thresholding an [e-variable](e-variable.md) at 1/α gives exactly such a family, while p-value tests do not; decisions with three or more actions or data-dependent losses must threshold e-variables [ramdasHypothesisTestingEvalues2025, Thm 4.9]. The same idea underlies e-posteriors and the data-driven α of Grünwald's later work [grunwaldSafeTesting2024, reply].

## Key results
- Post-hoc FDR control in e-BH and post-hoc false coverage rate control in e-BY [ramdasHypothesisTestingEvalues2025, Thms 9.11, 13.7]; see [e-bh](e-bh.md).
- Principal–agent setting [ramdasHypothesisTestingEvalues2025, Prop. 4.11].
- The (1 − α)/α threshold question under likelihood-ratio symmetry, raised in the discussion and answered via the e-posterior [grunwaldSafeTesting2024, reply].
- Survey appendices: the e-posterior gives minimax guarantees for arbitrary post-hoc loss functions and multi-action decisions where Neyman–Pearson is inadequate [ramdasGametheoreticStatisticsSafe2023, Apps A–B].
- E-values allow valid risk assessment of post-hoc loss functions, not reproducible by α-spending-style adjustment; the (1 − α)/α threshold under likelihood-ratio symmetry is answered via the e-posterior and holds only under optional continuation, not as an e-process [grunwaldAuthorsReplyDiscussion2024, Secs 2, 5].
- Primary sources now ingested: generalised Neyman–Pearson problems, compatibility, Type-I risk safety, the BIND condition, safety ⇔ e-compatibility, admissible ⇔ maximally compatible, extension to confidence sets and the roving-α reinterpretation [grunwaldBeyondNeymanPearsonEvalues2024, Def. 1, eqs 10–12, 15, 18–20, Prop. 1, Thm 1, Sec. 5.1]; general-loss multi-action form with the final-risk-checker protocol and the counterexample for confidence distributions [grunwaldEposterior2023, Prop. 1, eq. 16, Examples 6–7]; see [e-posterior](e-posterior.md).
- Multiple testing: simultaneous control equals post-hoc choice of the rejected set, post-hoc choice of error metric, and post-hoc α when the e-collection is α-free [xuBringingClosureFalse2025, Lemma 4, Def. 40, Thms 39, 41, 48]; for closed BH this freedom is negligible [goemanUniformImprovementBenjaminiHochberg2026, Thm 19]; rejection sets chosen after seeing e-values with guarantees uniform in R and j [vovkConfidenceDiscoveriesEvalues2023, Sec. 6]; data-dependent level switching in test induction [koningAnytimeValidityFree2026, Sec. 5.1].

## Variants and related concepts
- [calibrator](calibrator.md), [confidence-sets-and-sequences](confidence-sets-and-sequences.md).

## Sources
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — Chapter 4.
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — reply.
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md) — appendices.
- [grunwaldAuthorsReplyDiscussion2024](../sources/grunwaldAuthorsReplyDiscussion2024.md) — post-hoc losses, (1 − α)/α.
- [grunwaldBeyondNeymanPearsonEvalues2024](../sources/grunwaldBeyondNeymanPearsonEvalues2024.md), [grunwaldEposterior2023](../sources/grunwaldEposterior2023.md) — primary sources.
- [xuBringingClosureFalse2025](../sources/xuBringingClosureFalse2025.md), [goemanUniformImprovementBenjaminiHochberg2026](../sources/goemanUniformImprovementBenjaminiHochberg2026.md), [vovkConfidenceDiscoveriesEvalues2023](../sources/vovkConfidenceDiscoveriesEvalues2023.md), [koningAnytimeValidityFree2026](../sources/koningAnytimeValidityFree2026.md) — multiple testing and induction.

## Disagreements / open issues
- Koning's post-hoc p-value work (2023) is a candidate, not yet in the bib.
