---
title: "E-world"
suppress-bibliography: true
---

*This is ongoing collection of literature about e-value (methodology),*
*Pls make a pull request in [github](https://github.com/wyq977/e-world).*

## 2026

* [@koningAnytimeValidityFree2026]
    Any level-α test at a fixed sample size N can be turned into an anytime-valid sequential test that coincides with it at time N, by tracking the null-conditional expectation of the test; a [0, 1]-valued test outcome then serves as a conditional significance level for whatever comes next, so optional stopping and continuation need no explicit e-values. [PDF](https://doi.org/10.1093/jrsssb/qkag050) [DOI](10.1093/jrsssb/qkag050)

* [@lindonAnytimeValidInferenceLinear2026]
    Sequential F- and t-tests and confidence sequences for linear-model coefficients, built as the likelihood ratio of the standardised OLS vector under a right-Haar prior on the nuisance parameters and a Gaussian (g-type) prior on the alternative, so that a classical F-statistic converts in closed form into a GROW/REGROW test martingale; then heteroskedasticity-robust asymptotic 't' e-processes and confidence sequences for regression-adjusted average treatment effects in randomised experiments, tested on Netflix A/B data. [arXiv](https://arxiv.org/abs/2210.08589) [DOI](10.1080/01621459.2026.2692052)

## 2025

* [@larssonNumeraireEvariableReverse2025]
    With no assumptions at all on a composite null and a point alternative there is a unique strictly positive e-variable, the numeraire, that is log-optimal and is a likelihood ratio dQ/dP* against a sub-probability measure P* in the effective null; P* is the reverse information projection whenever the classical one exists, strong duality holds, universal inference is dominated, and nonparametric nulls without a reference measure become tractable. [arXiv](https://arxiv.org/abs/2402.18810) [DOI](10.1214/24-AOS2487)

* [@ramdasHypothesisTestingEvalues2025]
    The reference monograph on e-values: validity via Markov and Ville, e-power and log-optimality, calibrators, universal inference, the numeraire and reverse information projection, e-processes, merging, e-BH, and e-confidence intervals, in sixteen chapters with proofs. [PDF](https://www.stat.cmu.edu/~aramdas/ebook-final.pdf) [arXiv](https://arxiv.org/abs/2410.23614) [DOI](10.1561/3600000002)

## 2024

* [@grunwaldAuthorsReplyDiscussion2024]
    The authors' answer to twenty discussants of Safe Testing: they endorse the numeraire as the assumption-free form of their Theorem 1, concede that GROW point priors clash with shrinking confidence intervals and that 'safe' was an unlucky name, take back the 'e-values need more data' line, and show on Greenland's chi-square example that a UMP Bayes factor rejects at p <= 0.007. [DOI](10.1093/jrsssb/qkae069)

* [@grunwaldBeyondNeymanPearsonEvalues2024]
    Why report an e-value instead of a p-value next to the accept/reject decision: in a generalised Neyman–Pearson setting where the loss function is chosen after the data, only e-value-based rules keep Type-I risk under control, and the same holds for confidence intervals via the e-posterior. [PDF](https://www.pnas.org/doi/10.1073/pnas.2302098121) [arXiv](https://arxiv.org/abs/2205.00901) [DOI](10.1073/pnas.2302098121)

* [@grunwaldSafeTesting2024]
    The paper that put e-values and growth-rate optimality on the map: GRO e-variables are Bayes factors with a reverse-information-projection prior on the null; read before the RSS on January 24, 2024 (video), with discussion and authors' reply. [PDF](https://academic.oup.com/jrsssb/article/86/5/1091/7623686) [arXiv](https://arxiv.org/abs/1906.07801) [DOI](10.1093/jrsssb/qkae011) [video](https://www.youtube.com/watch?v=m6mYlHK_c84)

* [@perezortizEstatisticsGroupInvariance2024]
    The anytime-valid Hunt–Stein theorem: for testing problems invariant under an amenable group, the likelihood ratio of a maximally invariant statistic (equivalently the right-Haar Bayes factor) is the GROW and relatively GROW e-statistic among all e-statistics, and it is a test martingale in the invariant filtration; this is the result behind the safe t-test. [PDF](https://arxiv.org/pdf/2208.07610) [arXiv](https://arxiv.org/abs/2208.07610) [DOI](10.1214/24-AOS2394)

* [@terschureAnytimevalidLogrankTest2024]
    The logrank test rebuilt as a test martingale: the ratio of Cox partial likelihoods is an exact e-process under proportional hazards, so survival trials can be monitored continuously, extended indefinitely and pooled into a live meta-analysis without losing type-I error control. [PDF](https://arxiv.org/pdf/2011.06931) [arXiv](https://arxiv.org/abs/2011.06931) [DOI](10.51387/24-NEJSDS65)

* [@turnerGenericEvariablesExact2024]
    Builds exact, anytime-valid k-sample tests from a generic block e-variable whose denominator is a product of per-outcome mixtures of the null, proves it is GRO whenever the single-outcome model is convex (so for 2x2 tables), and shows by simulation that with a Beta(0.18, 0.18) prior it matches Fisher's exact test in sample size while allowing optional stopping. [PDF](https://doi.org/10.1016/j.jspi.2023.106116) [arXiv](https://arxiv.org/abs/2106.02693) [DOI](10.1016/j.jspi.2023.106116)

## 2023

* [@grunwaldEposterior2023]
    The reciprocal of an e-variable, read as a posterior over the parameter: it can be combined with any loss function chosen after the data and gives frequentist risk bounds that get loose rather than wrong when the e-collection is chosen badly, which is what makes e-posterior minimax decisions safer than Bayesian ones. [PDF](https://royalsocietypublishing.org/doi/10.1098/rsta.2022.0146) [arXiv](https://arxiv.org/abs/2301.01335) [DOI](10.1098/rsta.2022.0146)

* [@ramdasGametheoreticStatisticsSafe2023]
    The four-author Statistical Science survey that fixed the vocabulary of safe anytime-valid inference (e-value, test martingale, e-process, confidence sequence, testing by betting) and catalogued the composite-null constructions, from universal inference and the RIPr to nonparametric supermartingales and e-detectors, ending with a list of open problems. [arXiv](https://arxiv.org/abs/2210.01948) [DOI](10.1214/23-STS894)

* [@turnerExactAnytimevalidConfidence2023]
    A short note that turns the two-sample 2x2 e-variables into exact anytime-valid confidence sequences for risk difference, relative risk and odds ratio by projecting the alternative onto a convex null and inverting the resulting test over all effect sizes. [PDF](https://doi.org/10.1016/j.spl.2023.109835) [arXiv](https://arxiv.org/abs/2203.09785) [DOI](10.1016/j.spl.2023.109835)

* [@vovkConfidenceDiscoveriesEvalues2023]
    Turns e-values into confidence regions and into simultaneous lower confidence bounds on the number of true discoveries, valid under arbitrary dependence, with an O(K^2) algorithm for the arithmetic-mean discovery matrix that beats closed-testing p-value bounds in simulations and on the BRCA gene-expression data. [PDF](https://arxiv.org/pdf/1912.13292) [arXiv](https://arxiv.org/abs/1912.13292) [DOI](10.1214/22-STS874)

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

## 2012

* [@brannathProbabilisticFoundationConfirmatory2012]
    Type I error control of adaptive designs by the conditional error or conditional invariance principle is not implied by a single probability model, because conditional probabilities are defined only up to null sets and a data-driven choice of version inflates the error arbitrarily; it is restored by assuming a regression model for the second-stage data given interim data and design, under which an arbitrary, even non-measurable, adaptation rule can be embedded in a probability space. [PDF](https://www.jstor.org/stable/23239614) [DOI](10.1080/01621459.2012.682540)

## 2007

* [@brannathMultiplicityFlexibilityClinical2007]
    A review of flexible designs with strong familywise error control, organised around the conditional invariance principle, conditional error functions and flexible closed tests, followed by a criterion for when one may drop a treatment arm, change the sample size and still use the conventional z-test: whenever its conditional type I error rate is no larger than those of the prespecified design for every intersection hypothesis involved. [DOI](10.1002/pst.302)

## 2002

* [@liuUnifiedTheoryTwoStage2002]
    A measure-theoretic formulation of two-stage adaptation as a measurable rule with countably many options, whose Adaptation Lemma shows that a conditional property shared by every option (unbiasedness, a pivotal distribution, or a conditional type I error bound) is inherited by the adapted statistic; this justifies both the conditional error function and the combination-test approaches, and counterexamples show what fails for non-measurable or uncountable adaptation rules. [PDF](https://www.jstor.org/stable/3085828) [DOI](10.1198/016214502388618852)

## 1999

* [@poschAdaptiveTwoStage1999]
    Four adaptive two-stage designs (Proschan–Hunsberger, Lehmacher–Wassmer, Bauer–Köhne, Shen–Fisher) are each written as a conditional error function A(z₁) integrating to α under the null, which shows that combination tests and conditional error functions describe the same rejection regions and gives a conditional power function for comparing designs and reassessing the sample size. [DOI](10.1002/(SICI)1521-4036(199910)41:6<689::AID-BIMJ689>3.0.CO;2-P)

## 1939

* [@villeEtudeCritiqueNotion1939]
    Ville's doctoral thesis: the critique of von Mises–Wald collectives that introduced the martingale as a gambling system and proved P(sup_n s_n ≥ λ) ≤ 1/λ, the inequality behind every test martingale and e-process. [PDF](http://www.numdam.org/item?id=THESE_1939__218__1_0)

## Preprints

* [@brannathAnytimevalidTestingEvalues2026a]
    Conditional error functions and (recursive) combination tests of confirmatory adaptive designs are the same objects as sequential e-values and test supermartingales, via A_t = min(αM_t, 1); the two cultures differ in emphasis, adaptive designs exhausting the level α while e-values trade exhaustion for optional continuation, data-dependent α and post-hoc losses, and an appendix shows how to buy back the exhausted level with recursive combination tests at the price of that flexibility. [PDF](https://arxiv.org/pdf/2606.00878v1) [arXiv](2606.00878) [DOI](10.48550/arXiv.2606.00878)

* [@choeComparingSequentialForecasters2021]
    Anytime-valid, distribution-free comparison of two forecasters: empirical-Bernstein confidence sequences for the time-varying average score difference, dual sub-exponential e-processes for the weak null 'no better on average', and worked comparisons of baseball and weather forecasts. [PDF](https://arxiv.org/pdf/2110.00115) [arXiv](https://arxiv.org/abs/2110.00115) [DOI](10.48550/arXiv.2110.00115)

* [@dandapanthulaMultipleTestingMultistream2025]
    Shows that no multi-stream change detector with finite average run length can control FDR, FWER or PFER, proposes error over patience (Type I error divided by expected stopping time) as the controllable substitute, and controls it by feeding per-stream e-detectors into e-BH, e-Bonferroni, Holm and sum-of-e-detectors rules under arbitrary cross-stream dependence. [PDF](https://arxiv.org/pdf/2501.04130) [arXiv](https://arxiv.org/abs/2501.04130) [DOI](10.48550/arXiv.2501.04130)

* [@dixitAnytimeValidAsymptotically2023]
    Puts Newton's predictive-recursion fit of a nonparametric mixture in the numerator of a universal-inference e-process, so that each update costs O(1), the result is a genuine e-process by a one-line martingale domination argument, and its log grows at the first-order optimal rate K(P*, P0) - K(P*, Q) with an empirically n^{1/3}-sized gap to the oracle. [PDF](https://arxiv.org/pdf/2309.13441) [arXiv](https://arxiv.org/abs/2309.13441) [DOI](10.48550/arXiv.2309.13441)

* [@fischerAdmissibleOnlineClosed2024]
    Shows that any admissible online procedure bounding true discoveries in data-chosen sets must implicitly run an anytime-valid test, hence a test martingale, for every intersection hypothesis, and builds SeqE-Guard, a one-pass shortcut that multiplies sequential e-values and uniformly improves every existing online true-discovery method. [PDF](https://arxiv.org/pdf/2407.15733v4) [arXiv](https://arxiv.org/abs/2407.15733) [DOI](10.48550/arXiv.2407.15733)

* [@fischerOnlineGeneralizationEBH2024]
    Relax online multiple testing so that an accepted hypothesis may still be rejected later (never the reverse), and BH and e-BH acquire natural online versions: online e-BH controls the FDR at every stopping time under arbitrary dependence and uniformly beats e-LOND, online BH does so under positive or negative dependence at a log(1/α) inflation that is shown to be sharp, and both collapse back to the offline procedures when the horizon is known. [PDF](https://arxiv.org/pdf/2407.20683v5) [arXiv](https://arxiv.org/abs/2407.20683) [DOI](10.48550/arXiv.2407.20683)

* [@giuffridaTestingMaximumEntropy2025]
    Builds growth-optimal e-values for testing one maximum-entropy (exponential random graph type) model against another: exact in closed form when both are microcanonical, and a provably valid, near-optimal stand-in for the intractable canonical case, worked out for 2 x k contingency tables, stochastic block models and bipartite configuration models. [arXiv](https://arxiv.org/abs/2509.01064) [DOI](10.48550/arXiv.2509.01064)

* [@goemanUniformImprovementBenjaminiHochberg2026]
    Closed BH never rejects fewer hypotheses than Benjamini–Hochberg, often rejects many more, stays valid under PRDS, and is built entirely from the e-Closure principle: a family of e-values indexed by subsets of hypotheses. [PDF](https://arxiv.org/pdf/2606.01854) [arXiv](https://arxiv.org/abs/2606.01854) [DOI](10.48550/arXiv.2606.01854)

* [@grunwaldGrowthOptimalEVariablesExtension2024a]
    For a simple null and an alternative given by a set of means, the GROW e-variable is an exponential-family likelihood ratio when the mean set is convex and a two-point boundary mixture when it surrounds the null in one dimension; the e-variable is the object behind the Csiszár–Sanov–Chernoff bound, and a minimax-regret (Shtarkov) relative of it gives a new such bound for surrounding alternatives with a (d−1)/2 log n price. [arXiv](https://arxiv.org/abs/2412.17554) [DOI](10.48550/arXiv.2412.17554)

* [@grunwaldOptimalEValuesExponential2024]
    Gives one checkable condition, a covariance (Loewner) ordering between the null family and the family generated by the alternative, under which the growth-optimal e-variable for a composite exponential family null is just a likelihood ratio against a single null element. [arXiv](https://arxiv.org/abs/2404.19465) [DOI](10.48550/arXiv.2404.19465)

* [@haoEValuesExponentialFamilies2025]
    Derives and compares the RIPr-optimal, conditional, universal-inference and sequential plug-in e-variables for exponential family nulls, including the 'anti-simple' case where the optimal e-variable is not a simple likelihood ratio, and shows the conditional e-variable loses only o(1) e-power against the optimum while UI loses (d/2) log n. [arXiv](https://arxiv.org/abs/2409.11134) [DOI](10.48550/arXiv.2409.11134)

* [@hartogFamilyWiseError2025]
    Closed testing with e-values: averaging e-values inside every intersection test beats Bonferroni on inverse e-values, gives post-hoc and always-valid FWER control that p-value closure cannot, and the e-Holm, e-Fallback and e-graphical (DAG) procedures all get polynomial-time algorithms despite losing consonance. [PDF](https://arxiv.org/pdf/2501.09015v4) [arXiv](https://arxiv.org/abs/2501.09015) [DOI](10.48550/arXiv.2501.09015)

* [@henziValidSequentialInference2021]
    The first application of e-values to forecast comparison: for binary-event probability forecasts and any consistent scoring rule, a one-observation e-value for conditional forecast dominance is characterised exactly, its GROW version is a likelihood ratio with the score's mixing measure in the denominator, products give a test supermartingale valid under optional stopping, and a precipitation case study agrees with Diebold-Mariano tests. [PDF](https://arxiv.org/pdf/2103.08402) [arXiv](https://arxiv.org/abs/2103.08402) [DOI](10.48550/arXiv.2103.08402)

* [@ignatiadisAsymptoticCompoundEvalues2024]
    Formal definitions of compound, approximate and asymptotic e-values, a proof that every FDR procedure is e-BH run on some compound e-values, and an empirical-Bayes construction (nonparametric MLE over the variances) that turns Storey's optimal discovery procedure into asymptotic compound e-values with the first type-I guarantee for its data-driven version. [PDF](https://arxiv.org/pdf/2409.19812v4) [arXiv](https://arxiv.org/abs/2409.19812) [DOI](10.48550/arXiv.2409.19812)

* [@ignatiadisEvaluesUnnormalizedWeights2022]
    When every hypothesis comes with a p-value and an independent e-value, the e-values can be used as weights for Benjamini–Hochberg or Bonferroni without being normalised to sum to the number of hypotheses, which the paper turns into a meta-analysis combiner, a data-driven weighting scheme via compound e-values, and a gene-expression case study with more discoveries. [PDF](https://arxiv.org/pdf/2204.12447v6) [arXiv](https://arxiv.org/abs/2204.12447) [DOI](10.48550/arXiv.2204.12447)

* [@kirschnerConfidenceEstimationSequential2025]
    One recipe for anytime-valid confidence sequences in any realizable likelihood model: threshold the negative log-likelihood by log(1/δ) minus the log of a predictable mixture predictive density, which recovers Robbins' likelihood-ratio and prior-mixture sequences, the prior-posterior ratio set, ELBO and regret-to-confidence sets, and tightens the Abbasi-Yadkori linear-bandit ellipsoid by up to a factor two. [PDF](https://arxiv.org/pdf/2502.14689v1) [arXiv](https://arxiv.org/abs/2502.14689) [DOI](10.48550/arXiv.2502.14689)

* [@koningMeasuringEvidenceExchangeability2023]
    Turns permutation tests into e-values: every exact e-value for invariance under a compact group is a statistic divided by its average over the group orbit, the log-optimal one is the likelihood ratio against the group-averaged alternative, and e-processes are infima of orbit-wise Doob martingales. [PDF](https://arxiv.org/pdf/2310.01153v5) [arXiv](https://arxiv.org/abs/2310.01153) [DOI](10.48550/arXiv.2310.01153)

* [@koningPosthocAlphaHypothesis2023]
    Lets the significance level be chosen after seeing the data by asking only that the expected size-to-level ratio stay at most one, and shows this holds for every data-dependent level exactly when the p-value's reciprocal is an e-value, so e-values are p-values under a stronger guarantee, hidden by p = 1/e. [PDF](https://arxiv.org/pdf/2312.08040v10) [arXiv](https://arxiv.org/abs/2312.08040) [DOI](10.48550/arXiv.2312.08040)

* [@koolenGeneralisationVilleInequality2025]
    Ville's inequality with a time-decreasing floor and a time-increasing threshold: an exact crossing-probability formula, tight via a 'floor-hugging' martingale, used to turn an improper-mixture supermartingale into a clean finite-time law of the iterated logarithm. [PDF](https://arxiv.org/pdf/2502.16019) [arXiv](https://arxiv.org/abs/2502.16019) [DOI](10.48550/arXiv.2502.16019)

* [@lardyReverseInformationProjections2023]
    Extends the reverse information projection, and with it the GRO e-variable, to alternatives at infinite KL distance from a convex null by replacing KL with Topsøe's description gain; the resulting likelihood ratio is the strongest e-statistic in a pairwise sense that strictly generalises GRO, and the paper also shows when the RIPr is a strict sub-probability measure, adapts the Li-Barron greedy algorithm, and gives tight rates for turning approximate projections into approximate e-statistics. [PDF](https://arxiv.org/pdf/2306.16646v3) [arXiv](https://arxiv.org/abs/2306.16646) [DOI](10.48550/arXiv.2306.16646)

* [@larssonCompleteCharacterizationTestable2026]
    A nontrivial test of one set of distributions against another exists if and only if the weak-star closures of their convex hulls in the space of bounded finitely additive measures are separated in total variation; this completes Le Cam's program without a dominating measure, and for a point alternative the countably additive part of that closure is exactly the effective null of the numeraire paper. [PDF](https://arxiv.org/pdf/2601.05217v3) [arXiv](https://arxiv.org/abs/2601.05217) [DOI](10.48550/arXiv.2601.05217)

* [@larssonTestingHypothesesGenerated2025]
    For a null defined by an arbitrary family of measurable constraints (moments, quantiles, sub-Gaussian tails, group symmetries), every e-variable is a weak limit of 1 plus a conic combination of the constraint functions; the paper makes this explicit for finitely many constraints, one-sided sub-psi laws and compact-group invariance, describes the admissible e-variables and minimal complete classes, and proves existence and uniqueness of utility-optimal e-variables, covering GRO, GROW and REGROW. [PDF](https://arxiv.org/pdf/2504.02974v5) [arXiv](https://arxiv.org/abs/2504.02974) [DOI](10.48550/arXiv.2504.02974)

* [@martinRegularizedEprocessesAnytime2024]
    Multiply an e-process by a prior-knowledge 'regularizer' whose upper expectation under an imprecise (possibilistic) prior is at most one; a generalised Ville inequality then keeps anytime validity in a knowledge-dependent sense, buys efficiency, and the reciprocal becomes a possibilistic inferential model with calibrated uncertainty quantification and reliable decisions. [PDF](https://arxiv.org/pdf/2410.01427v4) [arXiv](https://arxiv.org/abs/2410.01427) [DOI](10.48550/arXiv.2410.01427)

* [@ramdasAdmissibleAnytimevalidSequential2022]
    The foundations paper for e-processes, p-processes, sequential tests and confidence sequences: it defines all four, proves they are equivalent to being dominated by nonnegative martingales, and shows that any admissible construction of any of them must, explicitly or implicitly, be built from such martingales. [PDF](https://arxiv.org/pdf/2009.03167) [arXiv](https://arxiv.org/abs/2009.03167) [DOI](10.48550/arXiv.2009.03167)

* [@ramdasTestingExchangeabilityForkconvexity2021]
    The first worked example of a null where every test supermartingale is powerless but a powerful e-process exists: binary exchangeability, attacked with a Jeffreys-mixture-over-maximum-likelihood ratio, and explained by the geometry of fork-convex hulls. [PDF](https://arxiv.org/pdf/2102.00630) [arXiv](https://arxiv.org/abs/2102.00630) [DOI](10.48550/arXiv.2102.00630)

* [@renDerandomizedKnockoffsLeveraging2022]
    Shows that the model-X knockoff filter is exactly e-BH run on the relaxed e-values p·1{W_j ≥ T}/(1 + number of W_k ≤ −T), so averaging these e-values over many independent knockoff draws and applying e-BH gives a derandomized knockoff filter with finite-sample FDR control and no extra assumptions, unlike earlier selection-frequency schemes. [PDF](https://arxiv.org/pdf/2205.15461v5) [arXiv](https://arxiv.org/abs/2205.15461) [DOI](10.48550/arXiv.2205.15461)

* [@rufCompositeGeneralizationVille2022]
    Ville's theorem that null events are exactly those on which some test martingale explodes, lifted to composite nulls: the right replacements are an 'inverse capital' outer measure and e-processes, and a composite strong law of large numbers shows that no (super)martingale can do the job that an e-process does. [PDF](https://arxiv.org/pdf/2203.04485) [arXiv](https://arxiv.org/abs/2203.04485) [DOI](10.48550/arXiv.2203.04485)

* [@sahaNonpartitionedEdetectorsNonparametric2026]
    Change detection when pre- and post-change laws both live in one unknown class: sum point-null e-processes started at every time, take the infimum over candidate no-change laws, and the aggregation weights decide whether you get average-run-length or false-alarm-probability control, with first-order optimal delay log(1/alpha)/KL. [PDF](https://arxiv.org/pdf/2607.28322) [arXiv](https://arxiv.org/abs/2607.28322) [DOI](10.48550/arXiv.2607.28322)

* [@shekharSequentialChangeDetection2023]
    Reduces change detection to estimation: run one forward confidence sequence and, at every time, a fresh backward one on the time-reversed data, and declare a change when the two stop intersecting; the average run length is at least 1/(2α) − 3/2 and the expected delay is a constant times the sample size at which the confidence width drops below the change magnitude, for any parameter or functional that admits a confidence sequence. [PDF](https://arxiv.org/pdf/2302.02544) [arXiv](https://arxiv.org/abs/2302.02544) [DOI](10.48550/arXiv.2302.02544)

* [@shinEdetectorsNonparametricFramework2023]
    The paper that defines e-detectors: sum (or max) e-processes restarted at every time step, stop at 1/α, and the average run length to a false alarm is at least 1/α for any composite, nonparametric, non-i.i.d. pre-change class, with explicit log(1/α)/KL-rate delay bounds for exponential mixtures. [PDF](https://arxiv.org/pdf/2203.03532) [arXiv](https://arxiv.org/abs/2203.03532) [DOI](10.48550/arXiv.2203.03532)

* [@wangAnytimevalidTtestsConfidence2023]
    Two anytime-valid t-tests for a Gaussian mean with unknown variance, one a universal-inference e-process in the data filtration and one a Gaussian-mixed scale-invariant test martingale in the coarser scale-invariant filtration, with Lai's 1976 flat-mixture construction explained as a nonintegrable extended martingale; the width of every t-confidence sequence must grow polynomially like alpha^(-1/n), which the fixed-sample t-interval fails to attain, and the e-power 1/2 log(1 + mu^2/sigma^2) is the reverse-information-projection ceiling. [PDF](https://arxiv.org/pdf/2310.03722) [arXiv](https://arxiv.org/abs/2310.03722) [DOI](10.48550/arXiv.2310.03722)

* [@wangEbacktesting2022]
    The first model-free, non-asymptotic, anytime-valid backtest for Expected Shortfall: backtest e-statistics turn each day's loss and (ES, VaR) forecast into a conditional e-variable, a betting process compounds them into a test supermartingale, and the VaR and ES e-statistics are shown to be essentially the only useful ones. [PDF](https://arxiv.org/pdf/2209.00991v6) [arXiv](https://arxiv.org/abs/2209.00991) [DOI](10.48550/arXiv.2209.00991)

* [@wangFalseDiscoveryRate2021]
    The paper that introduced e-BH: run Benjamini–Hochberg on e-values and the false discovery rate is controlled under any dependence with no log K correction, plus boosting when null distributions are known, and BH and BY recovered as calibrated special cases. [PDF](https://arxiv.org/pdf/2009.02824v5) [arXiv](https://arxiv.org/abs/2009.02824) [DOI](10.48550/arXiv.2009.02824)

* [@wangOnlyAdmissibleWay2024]
    A short proof, via multi-marginal optimal transport duality and Sion's minimax theorem, that every e-merging function valid under arbitrary dependence is dominated by a weighted average of the inputs and the constant 1, so weighted arithmetic means are the only admissible way to combine arbitrarily dependent e-values. [PDF](https://arxiv.org/pdf/2409.19888) [arXiv](https://arxiv.org/abs/2409.19888) [DOI](10.48550/arXiv.2409.19888)

* [@waudbysmithEstimatingMeansBounded2020]
    The betting construction of confidence sequences and intervals for a bounded mean: a capital process that is an exact nonnegative martingale for every distribution with mean m, inverted over m, with adaptive betting strategies that beat Hoeffding, empirical-Bernstein and Bentkus bounds with and without replacement. [PDF](https://arxiv.org/pdf/2010.09686) [arXiv](https://arxiv.org/abs/2010.09686) [DOI](10.48550/arXiv.2010.09686)

* [@waudbysmithTimeuniformCentralLimit2021]
    Defines asymptotic confidence sequences as almost-sure approximations of an unknown nonasymptotic one, builds them universally under CLT-type moment conditions by coupling the sample-average process with a Gaussian process (Strassen) and applying Robbins' normal mixture, and uses them for anytime-valid doubly robust causal inference. [PDF](https://arxiv.org/pdf/2103.06476) [arXiv](https://arxiv.org/abs/2103.06476) [DOI](10.48550/arXiv.2103.06476)

* [@xuBringingClosureFDR2025]
    The short first paper on FDR closure: test every intersection hypothesis with the arithmetic mean of its e-values, accept the largest top-k set whose every intersection e-value beats its FDP over α, and e-BH, minimally adaptive e-BH and Benjamini–Yekutieli all turn out to be inadmissible; superseded by the merged e-Closure paper. [PDF](https://arxiv.org/pdf/2504.11759v3) [arXiv](https://arxiv.org/abs/2504.11759) [DOI](10.48550/arXiv.2504.11759)

* [@xuBringingClosureFalse2025]
    Every multiple testing method that controls an expected loss (FDR, FWER, PFER, FDX, ...) is a closed testing procedure driven by e-values for intersection hypotheses, and reverse-engineering the implicit e-values yields strictly more powerful versions of e-BH, Benjamini–Yekutieli and Su's procedure with free post-hoc choice of rejected set, error metric and even level. [PDF](https://arxiv.org/pdf/2509.02517) [arXiv](https://arxiv.org/abs/2509.02517) [DOI](10.48550/arXiv.2509.02517)

* [@xuOnlineMultipleTesting2023]
    e-LOND: feed e-values instead of p-values into the LOND online FDR algorithm and the usual log-factor penalty for unknown dependence disappears, with randomised variants that reject strictly more and an online false-coverage-rate version for e-confidence intervals. [PDF](https://arxiv.org/pdf/2311.06412v1) [arXiv](https://arxiv.org/abs/2311.06412) [DOI](10.48550/arXiv.2311.06412)

* [@xuPostselectionInferenceEvalue2022]
    Defines e-confidence intervals (inverted e-values) and the e-BY procedure, which reports the selected intervals at level α|S|/K and controls the false coverage rate under any dependence and any selection rule, recovering Benjamini–Yekutieli through a calibrator and beating it on Twitter A/B tests. [PDF](https://arxiv.org/pdf/2203.12572v4) [arXiv](https://arxiv.org/abs/2203.12572) [DOI](10.48550/arXiv.2203.12572)

* [@zhangExistencePowerfulPvalues2023]
    For composite nulls and alternatives that are convex polytopes, an exact e-value with positive e-power (or an exactly uniform p-value with power) exists iff the alternative misses the linear span of the null, and a merely valid one iff the convex hulls are disjoint; proved by simultaneous optimal transport, with an iterative SHINE construction and the first systematic account of when coarsening the filtration is what makes a composite test martingale possible. [PDF](https://arxiv.org/pdf/2305.16539v4) [arXiv](https://arxiv.org/abs/2305.16539) [DOI](10.48550/arXiv.2305.16539)
