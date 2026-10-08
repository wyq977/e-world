---
slug: mdl-and-maximum-entropy-e-values
title: MDL, regret, and e-values for maximum entropy models
sources: 2
updated: 2026-10-08
---

# MDL, regret, and e-values for maximum entropy models

## Definition
Maximum entropy models maximise Shannon entropy under constraints on observables c(x): hard constraints give the microcanonical model, uniform on {x : c(x) = c}; soft constraints give the canonical model, an exponential family with uniform carrier whose Lagrange multipliers are the canonical parameters. Erdős–Rényi, configuration and stochastic block models are instances [giuffridaTestingMaximumEntropy2025, Sec. II]. Testing one such model against another with the same carrier but different sufficient statistics is the mirror image of the same-statistic setting of [exponential-family-e-values](exponential-family-e-values.md). The MDL bridge: −log S of a GRO e-variable is a code-length difference with a frequentist guarantee, and the worst-case regret of the GRO e-variable with a universal-distribution numerator is bounded by that numerator's redundancy, so Bayes mixtures with regular priors and NML give regret (d_1/2) log m + O(1) [giuffridaTestingMaximumEntropy2025, eqs 21–22, S1]. The authors present this as a two-model answer to Open Problem 9 of Grünwald's MDL book, which lacked type-I guarantees.

## Key results
- Microcanonical GRO e-variable in closed form: the RIPr prior on the null is the push-forward of the alternative's universal distribution onto the null sufficient statistic, a convolution under independent group priors, discrete Gaussian for many groups; E_0[S] = 1 for every null element [giuffridaTestingMaximumEntropy2025, eqs 29–33, 68, 95].
- Canonical GRO is generally uncomputable; the microcanonical approximation gives a valid canonical e-variable by conditioning, and a non-e-variable "pseudo approximation" upper-bounds canonical e-power, yielding a computable sandwich of width r [giuffridaTestingMaximumEntropy2025, eqs 38–49].
- Theorem 1: under a Bayes marginal of a canonical model with regular prior, the law of the normalised sufficient statistic matches the prior up to O(log m / m) on INECCSI sets, via Csiszár's multivariate Chernoff bound; only heuristically implies r → 0 [giuffridaTestingMaximumEntropy2025, Thm 1].
- Regret rate ((d_1 − d_0)/2) log m + O(1) for nested model pairs, using the Hao–Grünwald asymptotics [giuffridaTestingMaximumEntropy2025, eq. 87, S6].
- Simulations for 2 × 2 and 2 × k binary tables: microcanonical e-power converges to the numerically computed canonical GRO from below; the sandwich closes as m grows and when k and m grow together, failing only when m = O(1/k); regret slope dichotomy at Beta prior γ = 1, so Jeffreys' prior (γ = 1/2), MDL-minimax, is regret-suboptimal for e-values [giuffridaTestingMaximumEntropy2025, Sec. IV, Fig. 5].
- Network dictionary: Erdős–Rényi vs stochastic block model is a 2 × k test; bipartite ER vs partial configuration model is 2 × k with equal group sizes; same for stationarity of binary time series [giuffridaTestingMaximumEntropy2025, Sec. IV.C].
- The ingest agent's own observation, not in the paper: the microcanonical GRO e-variable is the conditional e-variable of Hao and Grünwald with Z = c_0 and a Bayes or NML numerator, hence generally not an e-process [haoEValuesExponentialFamilies2025, Prop. 7].
- Safe Testing's REGROW for a simple null is the redundancy–capacity problem, with Jeffreys' prior asymptotically optimal and regret (d/2) log n [grunwaldSafeTesting2024, Example 5]; the maximum-entropy results refine this for two-model tests; see [gro-criterion](gro-criterion.md).

## Variants and related concepts
- [k-sample-and-contingency-table-e-values](k-sample-and-contingency-table-e-values.md), the 2 × k instances.
- [reverse-information-projection](reverse-information-projection.md), [bayes-factor-e-variable](bayes-factor-e-variable.md).

## Sources
- [giuffridaTestingMaximumEntropy2025](../sources/giuffridaTestingMaximumEntropy2025.md) — all results above.
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — REGROW as redundancy–capacity.

## Disagreements / open issues
- Optional stopping and e-process-ness are not discussed in the paper; products across independent studies are valid, within-study stopping is not addressed.
- grunwaldMinimumDescriptionLength2019 and yamanishiLearningMinimumDescription2023 are in the bib as MDL background and not ingested; Grünwald, Hao and Balsubramani 2024 on growth-optimal e-variables and the Csiszár–Sanov–Chernoff extension is not in the bib.
