# Ingest brief for subagents

You are ingesting ONE paper into the markdown wiki at /Users/yongqi/projects/e-world.
Read /Users/yongqi/projects/e-world/AGENTS.md first.

Hard limits
- Write only the single file wiki/sources/<citekey>.md. Nothing else.
- Never touch raw/, e-world.bib, inbox/, or anything under ~/Zotero. No web tools, no Zotero tools.

Inputs
- Text: raw/<citekey>/paper.txt (read fully unless told otherwise). PDF: raw/<citekey>/paper.pdf (only for figures/tables).
- Metadata: raw/<citekey>/meta.yaml and the bib entry (grep the citekey in e-world.bib).
- Template: wiki/templates/source.md. Fill every frontmatter field. public: true. ingested: 2026-10-08.
  note: one sentence for a public reading list, human-facing. links: doi and arxiv as given; pdf if an open URL is obvious from the paper; video "".
  version: from meta.yaml.

Existing pages you may link to
- Sources: every file in wiki/sources/ (run `ls wiki/sources`), plus the other papers of the current batch named in your prompt. Link as [citekey](citekey.md). Mention any other work by author-year without a link.
- Concepts (link as [Name](../concepts/slug.md)): every file in wiki/concepts/ (run `ls wiki/concepts`); read a concept page before linking it so the link fits.
  Prefer these. Propose a NEW slug only for a concept with real substance in this paper that none of them covers (e.g. confidence-sequence boundaries, logrank/survival e-values, p-value calibration families, martingale history). List new slugs in "Concepts touched" as plain text with "(new)".

Body sections (keep the template headings): Summary (3–6 sentences); Main results (list, one line each, with the paper's own numbering: Theorem/Proposition/Section); Setting and assumptions; Relation to other sources; Concepts touched; Versions (only if relevant); Open questions / gaps. Attach [citekey] to claims. Precise and quantitative. Under about 200 lines.

Final message to return
1. 6–8 takeaway bullets.
2. For each concept slug touched (existing or new): 2–4 sentences on what THIS paper contributes, with theorem/section numbers. For new slugs also give a 2–4 sentence definition.
3. Up to 8 cited works central to e-value methodology that are NOT among the bib citekeys listed in AGENTS.md's project (the 28 keys: brownFundamentalsStatisticalExponential1986 diaconisConjugatePriorsExponential1979 dickhausHowAnalyzeMany2012 dickhausSimultaneousBayesianAnalysis2015 eisingaSaddlepointApproximationsMean2011 fogSamplingMethodsWallenius2008 giuffridaTestingMaximumEntropy2025 grunwaldAuthorsReplyDiscussion2024 grunwaldMinimumDescriptionLength2019 grunwaldOptimalEValuesExponential2024 grunwaldSafeTesting2024 haoEValuesExponentialFamilies2025 howardTimeuniformNonparametricNonasymptotic2021 johnsonUniformlyMostPowerful2013 koolenLogoptimalAnytimevalidEvalues2022 miethCombiningMultipleHypothesis2016 perezCaseStudyBayesian1994 ramdasGametheoreticStatisticsSafe2023 ramdasHypothesisTestingEvalues2025 shaferTestingBettingStrategy2021 terschureAnytimevalidLogrankTest2024 turnerExactAnytimevalidConfidence2023 turnerGenericEvariablesExact2024 villeEtudeCritiqueNotion1939 vovkEvaluesCalibrationCombination2021 waldSequentialAnalysis1947 wassermanUniversalInference2020 yamanishiLearningMinimumDescription2023): title, authors, year, why it matters.
