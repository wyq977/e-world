---
slug: post-hoc-validity
title: Post-hoc validity and data-dependent α
sources: 19
updated: 2026-10-12
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
- Primary source for the binary-test characterisation: post-hoc α validity means expected size distortion E[1{p ≤ α̃}/α̃] ≤ 1 for every data-dependent level; p is a post-hoc p-value iff E[1/p] ≤ 1, so post-hoc p-values are exactly reciprocals of e-values and every non-dominated post-hoc test is 1{e ≥ 1/α}, which makes e-values necessary; controlling the maximum distortion instead is vacuous; α-hacking between 0.01 and 0.05 gives expected distortion 1.8 and rejecting 'at level p' gives E[1/p] = ∞; optimality via E_Q[U(1/p)] with log giving the likelihood ratio and x ∧ 1/α* recovering Neyman–Pearson; abstract theory of h-valid, harmonic and geometric e-values; Markov's and Ville's equalities for data-dependent α [koningPosthocAlphaHypothesis2023, Defs 1–2, Thms 2, 3, 9, Cors 2–3, Props 8–11, Examples 1, 4, 5]. Koning's view: Grünwald's non-decision-theoretic definition is why the p-value duality was missed [koningPosthocAlphaHypothesis2023, App. A].
- The post-hoc level bound for e-BY and e-BH, E[sup_α FCP(α)/α] ≤ 1, identified with Wang–Ramdas Lemma 1 and Grünwald's Type-I risk safety [xuPostselectionInferenceEvalue2022, Cor. 1, Sec. 3].
- First strong post-hoc FWER result and post-hoc anytime-valid FWER; p-Holm has infinite post-hoc risk [hartogFamilyWiseError2025, Thms 2.3–2.4, Sec. 2.2]. SupFDR control as FDR validity at any stopping time, the time-axis analogue of post-hoc α [fischerOnlineGeneralizationEBH2024, Sec. 1.2]. Post-hoc level and set for closed e-BH, and post-hoc choice of the error metric; Grünwald's richness condition fails in this GNP problem [xuBringingClosureFDR2025, Prop. 4, Sec. 4, Remark 2]. Query sets, query paths and stopping times all chosen after seeing data under one simultaneous guarantee [fischerAdmissibleOnlineClosed2024, eq. 2, Cor. 3.2]. Error-over-patience guarantees uniform over data-dependent levels [dandapanthulaMultipleTestingMultistream2025]. Validity uniformly over hypotheses chosen after seeing data, including adversarially, for possibilistic inferential models [martinRegularizedEprocessesAnytime2024, Cor. 2]. The hot-hand analysis reported on both the e- and the post-hoc p-scale [koningMeasuringEvidenceExchangeability2023, Table 1].

## Variants and related concepts
- [calibrator](calibrator.md), [confidence-sets-and-sequences](confidence-sets-and-sequences.md).

## Sources
- [ramdasHypothesisTestingEvalues2025](../sources/ramdasHypothesisTestingEvalues2025.md) — Chapter 4.
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — reply.
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md) — appendices.
- [grunwaldAuthorsReplyDiscussion2024](../sources/grunwaldAuthorsReplyDiscussion2024.md) — post-hoc losses, (1 − α)/α.
- [grunwaldBeyondNeymanPearsonEvalues2024](../sources/grunwaldBeyondNeymanPearsonEvalues2024.md), [grunwaldEposterior2023](../sources/grunwaldEposterior2023.md) — primary sources.
- [xuBringingClosureFalse2025](../sources/xuBringingClosureFalse2025.md), [goemanUniformImprovementBenjaminiHochberg2026](../sources/goemanUniformImprovementBenjaminiHochberg2026.md), [vovkConfidenceDiscoveriesEvalues2023](../sources/vovkConfidenceDiscoveriesEvalues2023.md), [koningAnytimeValidityFree2026](../sources/koningAnytimeValidityFree2026.md) — multiple testing and induction.
- [koningPosthocAlphaHypothesis2023](../sources/koningPosthocAlphaHypothesis2023.md) — post-hoc p-values, primary.
- [xuPostselectionInferenceEvalue2022](../sources/xuPostselectionInferenceEvalue2022.md) — post-hoc level in selection.
- [hartogFamilyWiseError2025](../sources/hartogFamilyWiseError2025.md), [fischerOnlineGeneralizationEBH2024](../sources/fischerOnlineGeneralizationEBH2024.md), [xuBringingClosureFDR2025](../sources/xuBringingClosureFDR2025.md), [fischerAdmissibleOnlineClosed2024](../sources/fischerAdmissibleOnlineClosed2024.md), [dandapanthulaMultipleTestingMultistream2025](../sources/dandapanthulaMultipleTestingMultistream2025.md), [martinRegularizedEprocessesAnytime2024](../sources/martinRegularizedEprocessesAnytime2024.md), [koningMeasuringEvidenceExchangeability2023](../sources/koningMeasuringEvidenceExchangeability2023.md) — batch-4 wave-2 contributions.

## Disagreements / open issues
- Koning and Grünwald disagree on framing: Koning holds that e-values are p-values under a stronger guarantee and that the decision-theoretic definition obscured this; Grünwald's generalised Neyman–Pearson setting treats loss-valued decisions [koningPosthocAlphaHypothesis2023, App. A; grunwaldBeyondNeymanPearsonEvalues2024].
