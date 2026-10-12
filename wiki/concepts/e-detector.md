---
slug: e-detector
title: E-detectors and sequential change detection
sources: 7
updated: 2026-10-12
---

# E-detectors and sequential change detection

## Definition
An e-detector is a nonnegative process M with E_P[M_τ] ≤ E_P[τ] for all stopping times τ and all P in the pre-change class; summing [e-processes](e-process.md) started at consecutive times gives one, and stopping at M_t ≥ 1/α controls the average run length to a false alarm at ≥ 1/α [ramdasGametheoreticStatisticsSafe2023, Sec. 5.7]. It is the change-detection analogue of an e-process, with average run length in place of type-I error.

## Key results
- Near-optimal detection delay of order log(1/α)/D(P ‖ Q) [ramdasGametheoreticStatisticsSafe2023, Sec. 5.7].
- The Shiryaev–Roberts statistic is recovered from likelihood-ratio e-detectors [ramdasGametheoreticStatisticsSafe2023, Sec. 5.7].
- Backward confidence sequences handle unspecified change classes [ramdasGametheoreticStatisticsSafe2023, Sec. 5.7].
- Primary source now ingested: definition E_{P,∞}[M_τ] ≤ E_{P,∞}[τ] for every stopping time and pre-change P; stopping at 1/α gives average run length ≥ 1/α by a one-line proof; mixtures of e-detectors are e-detectors; Shiryaev–Roberts sums and CUSUM maxima of e_j-processes started at each time; baseline increments with sup_P E[L_n | F_{n−1}] ≤ 1 give the classical recursions at O(1) per step; 1/α is tight for e-SR but can be arbitrarily conservative for e-CUSUM [shinEdetectorsNonparametricFramework2023, Def. 2.2, Prop. 2.3, Thm 2.4, Defs 2.5–2.11, Sec. 2.5].
- Delay bounds: worst average delay ≤ g_α/D(Q ‖ P) + Var(log L)/D² + 1 with g_α of order log(1/α) for exponential baseline increments over a geometric grid, matching Lorden's rate; non-separated case with growing grids and zeta weights at O(m log n) per step [shinEdetectorsNonparametricFramework2023, Prop. 2.14, Thms 3.4, 4.3, Cor. 4.6, Algorithm 2]. Bernoulli with time-varying means and bounded-mean shifts via the KL_inf variational formula; basketball application; Lorden's reduction recovered and generalised [shinEdetectorsNonparametricFramework2023, Sec. 5, Lemma 6.1].
- Non-partitioned detection: both pre- and post-change laws unknown in one class; D_t = inf_R Σ_s w_s M^R_{s:t}; unit weights give ARL ≥ A and P(τ ≤ m) ≤ m/A, summable weights give an e-process and global PFA ≤ α at the price −log π_{T+1} ≈ log T; under PFA control the conditional average delay is infinite for any detector, so delay results are high-probability [sahaNonpartitionedEdetectorsNonparametric2026, Thms 2.2–2.3, Sec. 1.1].
- First-order optimal delay (1 + ε)(log A − log w_{T+1})/D(Q ‖ P) via countable local REGROW witness bases, with matching change-of-measure lower bounds; early changes T = o(log(1/α)) are undetectable; explicit detectors for sub-Gaussian and bounded means (Cover's universal portfolio), Gaussian with unknown variance, two-state Markov chains; experiments beat the repeated-confidence-sequence detector [sahaNonpartitionedEdetectorsNonparametric2026, Thms 3.2–3.3, 4.2, 5.2–5.3, 6.13, 7.1–7.3, A.3, Tables 1–2].
- Change-point e-processes via double mixtures over hypothesised change times 2^k, and the separation of sequential testing from change detection [ramdasTestingExchangeabilityForkconvexity2021, Remark 18, Sec. 4.4]; the universal-inference t e-process with power-preserving translation is the per-start input for Gaussian unknown-variance detection [wangAnytimevalidTtestsConfidence2023, eq. 11].
- Confidence-sequence route for the non-partitioned setting: a backward confidence sequence at time n applies any CS construction to the reversed data and re-indexes; the detector stops when the forward CS and the backward CS from the first observation are disjoint; ARL ≥ 1/(2α) − 3/2 by a union bound, delay independent of the change time and of order (log(1/α) + log log(1/Δ))/Δ² for any iterated-logarithm boundary, variance-adaptive for bounded means via empirical Bernstein; Gaussian mean, KS-metric CDFs and kernel-MMD examples; O(t²) per step; CuSum read as repeated backward power-one likelihood-ratio tests; later used as the empirical baseline that non-partitioned e-detectors beat [shekharSequentialChangeDetection2023, Defs 11–12, Thm 13, Props 19, 29, Cors 17, 22–23, App. F].
- Multi-stream detection: any monitor with finite ARL under the global null has worst-case FDR, FWER and GER equal to one, so the paper defines error over patience, the supremum of type-I error at τ divided by E[τ]; per-stream e-detectors fed into e-BH, Bonferroni, Holm or a sum give EOP control; forfeiting ARL with α_t = α/t gives universal fixed-time control under any cross-stream dependence, and e-processes give PFA control at the price of infinite ARL; EOP needs each e-detector valid for the global filtration; piggybacking lowers thresholds after detections [dandapanthulaMultipleTestingMultistream2025, Thms 4.1–4.4, 5.1–5.5, 6.1, 7.2–7.4, Sec. 8, App. B]; see [online-multiple-testing](online-multiple-testing.md).

## Variants and related concepts
- [e-process](e-process.md), [confidence-sequence-boundaries](confidence-sequence-boundaries.md).

## Sources
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md) — Sec. 5.7 only.
- [shinEdetectorsNonparametricFramework2023](../sources/shinEdetectorsNonparametricFramework2023.md) — primary source.
- [sahaNonpartitionedEdetectorsNonparametric2026](../sources/sahaNonpartitionedEdetectorsNonparametric2026.md) — non-partitioned detection and delay theory.
- [ramdasTestingExchangeabilityForkconvexity2021](../sources/ramdasTestingExchangeabilityForkconvexity2021.md), [wangAnytimevalidTtestsConfidence2023](../sources/wangAnytimevalidTtestsConfidence2023.md) — inputs to detectors.
- [shekharSequentialChangeDetection2023](../sources/shekharSequentialChangeDetection2023.md) — backward confidence sequences.
- [dandapanthulaMultipleTestingMultistream2025](../sources/dandapanthulaMultipleTestingMultistream2025.md) — multi-stream detection.

## Disagreements / open issues
- Ram and Ramdas on bounded-mean change detection is in the reading queue, not ingested; no delay theory exists yet for the multi-stream procedures [dandapanthulaMultipleTestingMultistream2025].
