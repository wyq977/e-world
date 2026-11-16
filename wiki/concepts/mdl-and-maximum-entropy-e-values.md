---
slug: mdl-and-maximum-entropy-e-values
title: MDL, regret, and e-values for maximum entropy models
sources: 6
updated: 2026-11-16
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
- Finite minimax regret with the NML (Shtarkov) distribution in the null certifies RIPr existence [lardyReverseInformationProjections2023, Prop. 4].
- Simple null, alternative a set of means M_1 partitioned into pieces touching its boundary: the relative GROW e-variable in the minimax individual-sequence-regret sense is the Shtarkov (NML) distribution q(y) = p̄_{r̆(y)}(y)/∫ p̄_{r̆(y)} dρ relative to the boundary set R, divided by p_0, with constant regret mmreg(r̆); minimax redundancy mmred(H_1) is the expected-loss counterpart; for a sample mean of n observations and a boundary with four bounded derivatives both equal ((d − 1)/2) log n + O(1), by Takeuchi–Barron 2013 (upper) and Clarke–Barron 1994 (lower), the BIC complexity of the (d − 1)-dimensional boundary family; the result feeds a new Csiszár–Sanov–Chernoff bound and an asymptotic GROW rate for KL-ball alternatives [grunwaldGrowthOptimalEVariablesExtension2024a, eqs 3.8–3.10, Thms 4–6, eq. 4.5, Prop. 3].
- Maximum entropy as a zero-sum game: for a convex set C of distributions with finite maximal entropy the game between a code-choosing observer and nature has value H_max(C), and the observer's unique optimal code is adapted to the center of attraction, the limit of every entropy-maximising sequence, which need not lie in C or attain H_max(C); with mean-energy constraints the centers of attraction form the exponential family, except above a critical energy where no maximum entropy distribution exists [topsoeInformationtheoreticalOptimizationTechniques1979, Thms 1–3, 11].
- Conditional limit justification of maximum entropy: given that a sample mean of ψ lies in a convex set C, the observations are asymptotically quasi-independent with limiting law the exponential-family member dP*/dP_X = c·exp ϑ*(ψ), the generalized I-projection [csiszarSanovPropertyGeneralized1984, Thm 4].

## Variants and related concepts
- [k-sample-and-contingency-table-e-values](k-sample-and-contingency-table-e-values.md), the 2 × k instances.
- [reverse-information-projection](reverse-information-projection.md), [bayes-factor-e-variable](bayes-factor-e-variable.md).

## Sources
- [giuffridaTestingMaximumEntropy2025](../sources/giuffridaTestingMaximumEntropy2025.md) — all results above.
- [grunwaldSafeTesting2024](../sources/grunwaldSafeTesting2024.md) — REGROW as redundancy–capacity.
- [lardyReverseInformationProjections2023](../sources/lardyReverseInformationProjections2023.md) — NML certificate.
- [grunwaldGrowthOptimalEVariablesExtension2024a](../sources/grunwaldGrowthOptimalEVariablesExtension2024a.md) — Shtarkov e-variables over a boundary, (d − 1)/2 log n regret.
- [topsoeInformationtheoreticalOptimizationTechniques1979](../sources/topsoeInformationtheoreticalOptimizationTechniques1979.md) — maximum entropy and minimum discrimination as games.
- [csiszarSanovPropertyGeneralized1984](../sources/csiszarSanovPropertyGeneralized1984.md) — conditional limit theorem.

## Disagreements / open issues
- Optional stopping and e-process-ness are not discussed in the paper; products across independent studies are valid, within-study stopping is not addressed.
- grunwaldMinimumDescriptionLength2019 and yamanishiLearningMinimumDescription2023 are in the bib as MDL background and not ingested; Grünwald, Hao and Balsubramani 2024 on growth-optimal e-variables and the Csiszár–Sanov–Chernoff extension was ingested on 2026-10-19 as grunwaldGrowthOptimalEVariablesExtension2024a.
