# Log

Append-only. Header format: `## [YYYY-MM-DD] ingest|query|lint | subject`.

## [2026-10-08] lint | scaffold created
Wiki, templates, scripts and AGENTS.md set up. No sources ingested yet.

## [2026-10-08] query | candidate reading list
Built wiki/candidates.md from the staged Ramdas–Wang bibliography (ranked by in-text citation count), the SAVI 2022 reading list, and a web check. 49 titles in five tiers; 12 already in the bib, 4 staged, 33 missing.

## [2026-10-08] query | candidates: closure, e-posterior, change detection
Added 19 rows (50–68) after the human flagged gaps: e-closure / closed eBH family, Grünwald's e-posterior and post-hoc decision line, Ramdas-group change detection. Republished the reading-queue Artifact.

## [2026-10-08] query | candidates: Koning
Added Tier 8 (rows 69–75) for Nick Koning's post-hoc, permutation and continuous-testing line, from memory and unverified: the web search was refused by the permission layer. Approval of the four staged papers was also refused to the agent; the human runs make approve.

## [2026-10-08] query | candidates: testability foundations
Added rows 76–80 to Tier 1 after the human pointed to the 2026 Larsson–Ruf–Ramdas testability paper; verified titles and authors on arXiv.

## [2026-10-08] ingest | grunwaldSafeTesting2024
Safe testing (Grünwald, de Heide, Koolen, JRSSB 2024 with discussion). Source page written from the publisher text incl. discussion and reply. Concepts touched: e-variable, e-process, test-martingale, villes-inequality, e-power, gro-criterion, numeraire, reverse-information-projection, universal-inference, exponential-family-e-values, bayes-factor-e-variable, mixture-and-plug-in-methods, optional-continuation, optional-stopping, calibrator, confidence-sets-and-sequences, testing-by-betting, post-hoc-validity.

## [2026-10-08] ingest | wassermanUniversalInference2020
Universal inference (Wasserman, Ramdas, Balakrishnan, PNAS 2020). Concepts: e-variable, e-process, test-martingale, villes-inequality, reverse-information-projection, universal-inference, mixture-and-plug-in-methods, confidence-sets-and-sequences, e-merging.

## [2026-10-08] ingest | ramdasHypothesisTestingEvalues2025
Hypothesis testing with e-values (Ramdas, Wang, FnT Statistics 2025; author PDF 2025-09-10). Read selectively (ToC, preface, Ch. 1–3 and 7 in full, openings and notes of the rest). Concepts: all twenty pages; sole source for e-merging and e-bh.

## [2026-10-08] ingest | haoEValuesExponentialFamilies2025
E-values for exponential families: the general case (Hao, Grünwald, arXiv 2409.11134v2). Concepts: e-variable, e-process, e-power, gro-criterion, numeraire, reverse-information-projection, universal-inference, exponential-family-e-values, bayes-factor-e-variable, mixture-and-plug-in-methods, optional-stopping.

## [2026-10-08] lint | first concept layer
Twenty concept pages created by merging the four ingests; 28 alias slugs proposed by the ingest agents were folded into them and links in the source pages rewritten. gaps.md rebuilt (31 rows, cross-referenced to candidates.md). Public list regenerated.

## [2026-10-08] ingest | batch 2: ten sources from the bib
shaferTestingBettingStrategy2021, vovkEvaluesCalibrationCombination2021, ramdasGametheoreticStatisticsSafe2023, howardTimeuniformNonparametricNonasymptotic2021, grunwaldOptimalEValuesExponential2024, koolenLogoptimalAnytimevalidEvalues2022, terschureAnytimevalidLogrankTest2024, turnerGenericEvariablesExact2024, turnerExactAnytimevalidConfidence2023, villeEtudeCritiqueNotion1939. Staged from Zotero, approved on the human's "continue", ingested by ten parallel subagents, merged into the concept layer by the main agent.

## [2026-10-08] lint | concept layer after batch 2
Five new concept pages: confidence-sequence-boundaries, survival-e-values, k-sample-and-contingency-table-e-values, martingale-history, e-detector. Twelve slugs proposed by the agents folded into existing pages (implied-target→e-power, family-wise-validity→e-merging, simple-e-variable→exponential-family-e-values, randomised-stopping-time and filtration-choice→optional-stopping, exponential-supermartingales→confidence-sequence-boundaries, history-of-savi→martingale-history). All twenty existing pages gained batch-2 results and sources. gaps.md gained 16 rows. Metadata defects noticed by agents, for the human to fix in raw/: vovkEvaluesCalibrationCombination2021/meta.yaml says publisher-oa but the text is arXiv 1912.06116v4; villeEtudeCritiqueNotion1939/meta.yaml carries a DOI and URL belonging to the next bib entry (staging bug, fixed in scripts/stage_from_zotero.sh). Also turnerGenericEvariablesExact2024/paper.txt ends at page 15, missing the tail of the reference list; turnerExactAnytimevalidConfidence2023 lacks its supplementary appendix.

## [2026-10-08] ingest | grunwaldAuthorsReplyDiscussion2024
Authors' reply to the discussion of Safe testing. Text layer is the January 2025 manuscript, not the typeset pages. Fourteen concept pages gained reply material; no new slugs.

## [2026-10-08] ingest | giuffridaTestingMaximumEntropy2025
Testing maximum entropy models with e-values (arXiv 2509.01064v1). New concept page mdl-and-maximum-entropy-e-values; k-sample, exponential-family, RIPr, GRO, e-power, Bayes-factor and mixture pages updated.

## [2026-10-08] lint | remaining bib entries
Not ingested and not planned: waldSequentialAnalysis1947 (no PDF in Zotero), johnsonUniformlyMostPowerful2013 (citekey not found in Zotero), and twelve background entries (Brown 1986, Diaconis–Ylvisaker 1979, Dickhaus 2012/2015, Eisinga 2011, Fog 2008, Grünwald 2019 MDL, Mieth 2016, Pérez 1994, Yamanishi 2023). Thirteen queue papers are in Zotero but not in the bib; listed to the human.

## [2026-10-08] query | candidates regrouped by theme
On the human's request: rows 49 and 83 removed; the author-based Tier 8 dissolved; list regrouped into nine themes with an A/B/C priority column and stable row ids; rows 85–86 added for the two newly added bib papers without a row. Thirteen papers added to the bib via scripts/bib_add.py and approved; ingest running.

## [2026-10-08] ingest | batch 3: thirteen sources added to the bib on request
larssonNumeraireEvariableReverse2025, ramdasAdmissibleAnytimevalidSequential2022, perezortizEstatisticsGroupInvariance2024, wangFalseDiscoveryRate2021, vovkConfidenceDiscoveriesEvalues2023, xuBringingClosureFalse2025, goemanUniformImprovementBenjaminiHochberg2026, grunwaldEposterior2023, koolenGeneralisationVilleInequality2025, grunwaldBeyondNeymanPearsonEvalues2024, shinEdetectorsNonparametricFramework2023, sahaNonpartitionedEdetectorsNonparametric2026, koningAnytimeValidityFree2026. Bib entries built from Zotero metadata via scripts/bib_add.py; first agent run was killed by a usage limit and rerun.

## [2026-10-08] lint | concept layer after batch 3
Four new concept pages: e-closure-principle, e-posterior, group-invariance-e-statistics, test-induction. Folded: true-discovery-guarantees→e-closure-principle; admissibility and p-process→e-process; effective-null and reverse-renyi-projection→numeraire; change-detection-delay-bounds→e-detector; e-closure (Goeman)→e-closure-principle. Twenty-five existing pages updated; numeraire page now cites the paper's own numbering; stale "not in bib" notes removed. Eight gap rows retired, ten added. Metadata for the human: raw/vovkConfidenceDiscoveriesEvalues2023/meta.yaml says publisher-oa but the text is arXiv 1912.13292v5; raw/grunwaldEposterior2023 text carries the arXiv v2 stamp (author says identical to the journal version).

## [2026-10-08] lint | mobile layout of the wiki page
The main column had no minimum width, so long citekeys pushed it to 489 px on a 375 px phone, and the 62-link contents sat above the text. Fixed: min-width 0 and overflow-wrap on both pages; contents now a collapsible block, closed on narrow screens, with a jump-back link per page. Verified in the desktop app's browser at 375 px.

## [2026-10-08] ingest | batch 4 staged: 28 arXiv downloads on the human's instruction
The human allowed downloading papers absent from Zotero. 28 queue rows fetched from arXiv (metadata via API, PDF, ghostscript text), bib entries appended via scripts/bib_add.py, approved into raw/. Not fetched: Shafer–Vovk 2019 (book) and Vovk 2021 "Testing randomness online" (arXiv id not found; a wrong guess fetched an unrelated paper and was discarded). Candidates deduplicated (rows 44, 59, 62, 69). AGENTS.md now records the web-download route.
