---
slug: post-hoc-validity
title: Post-hoc validity and data-dependent α
sources: 4
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

## Variants and related concepts
- [calibrator](calibrator.md), [confidence-sets-and-sequences](confidence-sets-and-sequences.md).

## Sources
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — Chapter 4.
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — reply.
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md) — appendices.
- [grunwaldAuthorsReplyDiscussion2024](../sources/grunwaldAuthorsReplyDiscussion2024.md) — post-hoc losses, (1 − α)/α.

## Disagreements / open issues
- Grünwald 2023 "The e-posterior", Grünwald 2024 "Beyond Neyman–Pearson" and Koning's post-hoc p-value work are the primary sources and are candidates, not yet in the bib.
