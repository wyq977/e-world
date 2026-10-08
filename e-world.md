---
title: "E-world"
suppress-bibliography: true
---

*This is ongoing collection of literature about e-value (methodology),*
*Pls make a pull request in [github](https://github.com/wyq977/e-world).*

## 2025

* [@ramdasHypothesisTestingEvalues2025]
    The reference monograph on e-values: validity via Markov and Ville, e-power and log-optimality, calibrators, universal inference, the numeraire and reverse information projection, e-processes, merging, e-BH, and e-confidence intervals, in sixteen chapters with proofs. [PDF](https://www.stat.cmu.edu/~aramdas/ebook-final.pdf) [arXiv](https://arxiv.org/abs/2410.23614) [DOI](10.1561/3600000002)

## 2024

* [@grunwaldAuthorsReplyDiscussion2024]
    The authors' answer to twenty discussants of Safe Testing: they endorse the numeraire as the assumption-free form of their Theorem 1, concede that GROW point priors clash with shrinking confidence intervals and that 'safe' was an unlucky name, take back the 'e-values need more data' line, and show on Greenland's chi-square example that a UMP Bayes factor rejects at p <= 0.007. [DOI](10.1093/jrsssb/qkae069)

* [@grunwaldSafeTesting2024]
    The paper that put e-values and growth-rate optimality on the map: GRO e-variables are Bayes factors with a reverse-information-projection prior on the null; read before the RSS on January 24, 2024 (video), with discussion and authors' reply. [PDF](https://academic.oup.com/jrsssb/article/86/5/1091/7623686) [arXiv](https://arxiv.org/abs/1906.07801) [DOI](10.1093/jrsssb/qkae011) [video](https://www.youtube.com/watch?v=m6mYlHK_c84)

* [@terschureAnytimevalidLogrankTest2024]
    The logrank test rebuilt as a test martingale: the ratio of Cox partial likelihoods is an exact e-process under proportional hazards, so survival trials can be monitored continuously, extended indefinitely and pooled into a live meta-analysis without losing type-I error control. [PDF](https://arxiv.org/pdf/2011.06931) [arXiv](https://arxiv.org/abs/2011.06931) [DOI](10.51387/24-NEJSDS65)

* [@turnerGenericEvariablesExact2024]
    Builds exact, anytime-valid k-sample tests from a generic block e-variable whose denominator is a product of per-outcome mixtures of the null, proves it is GRO whenever the single-outcome model is convex (so for 2x2 tables), and shows by simulation that with a Beta(0.18, 0.18) prior it matches Fisher's exact test in sample size while allowing optional stopping. [PDF](https://doi.org/10.1016/j.jspi.2023.106116) [arXiv](https://arxiv.org/abs/2106.02693) [DOI](10.1016/j.jspi.2023.106116)

## 2023

* [@ramdasGametheoreticStatisticsSafe2023]
    The four-author Statistical Science survey that fixed the vocabulary of safe anytime-valid inference (e-value, test martingale, e-process, confidence sequence, testing by betting) and catalogued the composite-null constructions, from universal inference and the RIPr to nonparametric supermartingales and e-detectors, ending with a list of open problems. [arXiv](https://arxiv.org/abs/2210.01948) [DOI](10.1214/23-STS894)

* [@turnerExactAnytimevalidConfidence2023]
    A short note that turns the two-sample 2x2 e-variables into exact anytime-valid confidence sequences for risk difference, relative risk and odds ratio by projecting the alternative onto a convex null and inverting the resulting test over all effect sizes. [PDF](https://doi.org/10.1016/j.spl.2023.109835) [arXiv](https://arxiv.org/abs/2203.09785) [DOI](10.1016/j.spl.2023.109835)

## 2022

* [@koolenLogoptimalAnytimevalidEvalues2022]
    Extends the GRO criterion from fixed sample size to optional stopping: the log-optimal anytime-valid e-value against a composite null is characterised by a reverse information projection over mixtures of stopped null distributions, with examples where it is a plain likelihood ratio and a numerical example where it is not even a supermartingale. [PDF](https://doi.org/10.1016/j.ijar.2021.09.010) [DOI](10.1016/j.ijar.2021.09.010)

## 2021

* [@howardTimeuniformNonparametricNonasymptotic2021]
    The toolkit paper for confidence sequences: four recipes (stitching, conjugate mixtures, discrete mixtures, inverted stitching) that turn any sub-psi supermartingale into a curved anytime-valid boundary, with an empirical-Bernstein bound, matrix LIL and A/B-testing applications. [PDF](https://arxiv.org/pdf/1810.08240) [arXiv](https://arxiv.org/abs/1810.08240) [DOI](10.1214/20-AOS1991)

* [@shaferTestingBettingStrategy2021]
    The manifesto for reporting a test as the outcome of a bet: betting scores are likelihood ratios, the implied target replaces power, (1/alpha)-warranties replace confidence, and the discussion is where betting scores, e-values and Bayes factors are first set side by side; read before the RSS on September 9, 2020. [PDF](https://academic.oup.com/jrsssa/article/184/2/407/7056412) [arXiv](https://arxiv.org/abs/1903.06991) [DOI](10.1111/rssa.12647)

* [@vovkEvaluesCalibrationCombination2021]
    The paper that fixed the name and definition of e-values and showed why they are easy to combine: average arbitrarily dependent e-values, multiply independent or sequential ones, and build multiple-testing procedures from these two rules. [PDF](https://arxiv.org/pdf/1912.06116) [arXiv](https://arxiv.org/abs/1912.06116) [DOI](10.1214/20-AOS2020)

## 2020

* [@wassermanUniversalInference2020]
    The split likelihood-ratio test: an e-value built from any estimator on half the data and the null MLE on the other half, valid in finite samples for any model, with a running-MLE e-process version. [PDF](https://www.pnas.org/doi/10.1073/pnas.1922664117) [arXiv](https://arxiv.org/abs/1912.11436) [DOI](10.1073/pnas.1922664117)

## 1939

* [@villeEtudeCritiqueNotion1939]
    Ville's doctoral thesis: the critique of von Mises–Wald collectives that introduced the martingale as a gambling system and proved P(sup_n s_n ≥ λ) ≤ 1/λ, the inequality behind every test martingale and e-process. [PDF](http://www.numdam.org/item?id=THESE_1939__218__1_0)

## Preprints

* [@giuffridaTestingMaximumEntropy2025]
    Builds growth-optimal e-values for testing one maximum-entropy (exponential random graph type) model against another: exact in closed form when both are microcanonical, and a provably valid, near-optimal stand-in for the intractable canonical case, worked out for 2 x k contingency tables, stochastic block models and bipartite configuration models. [arXiv](https://arxiv.org/abs/2509.01064) [DOI](10.48550/arXiv.2509.01064)

* [@grunwaldOptimalEValuesExponential2024]
    Gives one checkable condition, a covariance (Loewner) ordering between the null family and the family generated by the alternative, under which the growth-optimal e-variable for a composite exponential family null is just a likelihood ratio against a single null element. [arXiv](https://arxiv.org/abs/2404.19465) [DOI](10.48550/arXiv.2404.19465)

* [@haoEValuesExponentialFamilies2025]
    Derives and compares the RIPr-optimal, conditional, universal-inference and sequential plug-in e-variables for exponential family nulls, including the 'anti-simple' case where the optimal e-variable is not a simple likelihood ratio, and shows the conditional e-variable loses only o(1) e-power against the optimum while UI loses (d/2) log n. [arXiv](https://arxiv.org/abs/2409.11134) [DOI](10.48550/arXiv.2409.11134)
