---
slug: e-detector
title: E-detectors and sequential change detection
sources: 1
updated: 2026-10-08
---

# E-detectors and sequential change detection

## Definition
An e-detector is a nonnegative process M with E_P[M_τ] ≤ E_P[τ] for all stopping times τ and all P in the pre-change class; summing [e-processes](e-process.md) started at consecutive times gives one, and stopping at M_t ≥ 1/α controls the average run length to a false alarm at ≥ 1/α [ramdasGametheoreticStatisticsSafe2023, Sec. 5.7]. It is the change-detection analogue of an e-process, with average run length in place of type-I error.

## Key results
- Near-optimal detection delay of order log(1/α)/D(P ‖ Q) [ramdasGametheoreticStatisticsSafe2023, Sec. 5.7].
- The Shiryaev–Roberts statistic is recovered from likelihood-ratio e-detectors [ramdasGametheoreticStatisticsSafe2023, Sec. 5.7].
- Backward confidence sequences handle unspecified change classes [ramdasGametheoreticStatisticsSafe2023, Sec. 5.7].

## Variants and related concepts
- [e-process](e-process.md), [confidence-sequence-boundaries](confidence-sequence-boundaries.md).

## Sources
- [ramdasGametheoreticStatisticsSafe2023](../sources/ramdasGametheoreticStatisticsSafe2023.md) — Sec. 5.7 only.

## Disagreements / open issues
- Thin page: the primary works (Shin, Ramdas, Rinaldo on e-detectors; Shekhar and Ramdas on backward confidence sequences; the 2025–2026 multi-stream, bounded-mean and non-partitioned papers) are in the reading queue, Tier 7, and not yet ingested.
