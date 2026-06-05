# Permea Scientific Thesis

## Core Scientific Thesis

Delivery-relevant biological behavior is not fully random.

Sequence-derived features may contain delivery-relevant signal for specific benchmark tasks. That signal can be studied with transparent datasets, baseline models, metrics, and provenance.

Computational benchmarks can support candidate prioritization before experimental follow-up. They can help teams rank candidates, inspect feature profiles, compare against baseline tasks, and document uncertainty.

This does not equal physical transport proof, biological mechanism proof, therapeutic performance, or clinical validation. Permea's scientific position is deliberately conservative: computational evidence can guide prioritization, but experimental validation remains a separate evidence level.

## Delivery as a Benchmarkable Problem

Delivery should be studied as a set of benchmark tasks, not as one universal prediction problem.

Examples include:

- BBB peptide crossing
- cell membrane penetration and CPP
- localization and targeting
- RNA and mRNA delivery-adjacent tasks
- literature-derived evidence graph construction

Each benchmark task needs:

- task definition
- input object
- label definition
- source attribution
- inclusion and exclusion criteria
- split policy
- metric set
- baseline models
- limitations
- provenance record
- public release posture

Task definitions matter because delivery labels are context-dependent. A label from one assay, source, or biological context should not automatically be treated as universal biological truth. Metrics matter because class imbalance, ranking behavior, and threshold behavior can change interpretation.

## Evidence Ladder

Permea uses a staged evidence ladder.

| Level | Name | Meaning |
| --- | --- | --- |
| Level 0 | Literature mention | A delivery-relevant claim, sequence, assay, or dataset is mentioned in a source. |
| Level 1 | Curated evidence card | The source claim has been converted into a structured, reviewable evidence object. |
| Level 2 | Benchmark candidate dataset | A dataset appears suitable for benchmark review but is not yet execution-ready. |
| Level 3 | Benchmark-ready dataset | The dataset has a defined task, label policy, source attribution, limitations, and release posture. |
| Level 4 | Reproducible computational benchmark | The benchmark can be run with documented metrics, baselines, outputs, and provenance. |
| Level 5 | External wet-lab validation | Independent experimental testing supports a candidate, task, or model claim. |
| Level 6 | In-vivo or translational validation | Later-stage biological or translational evidence supports the claim. |

Current Permea evidence should be described carefully. The first evidence package is a computational benchmark surface for BBB-related peptide prioritization. It supports bounded computational prioritization before experimental follow-up. It should not be described as experimental, in-vivo, translational, or clinical evidence.

## Current Initial Evidence

Permea starts with BBB peptide benchmark evidence.

The first wedge is the B3Pred Dataset_3 and B3Pred-derived benchmark surface. In current manuscript materials, this surface is described at aggregate level as 269 BBB-positive peptides and 2,690 non-BBB negatives across 2,959 peptide sequences.

Permea Signal ML is the first evidence package. It studies whether BBB-related peptide permeability signal can be learned from sequence-derived physicochemical features such as length, charge, hydrophobicity summary, pI, and aromaticity.

This is not the whole platform. It is a narrow, measurable, reproducible starting surface. It supports computational candidate prioritization before experimental follow-up, and it should remain bounded by its dataset, feature set, baseline models, split policies, and release posture.

## Benchmark and Metrics Doctrine

Benchmark metrics are evidence summaries, not biological proof.

ROC-AUC helps summarize ranking discrimination. PR-AUC is important under class imbalance because positive examples may be sparse. MCC provides a balanced binary-classification summary that accounts for all confusion-matrix cells.

Baseline comparison matters because simple, transparent models can reveal whether a benchmark surface contains learnable signal before moving to more complex models.

Aggregate metrics do not prove experimental transport, mechanism, therapeutic effect, or clinical utility. They show behavior under a defined computational task.

Provenance and reproducibility matter because delivery evidence must be inspectable. A benchmark result is more useful when readers can understand the dataset source, task definition, split policy, features, model family, metric set, output artifacts, and limitations.

## Scientific Non-Claims

Permea public scientific materials should preserve this checklist:

- no wet-lab validation claim
- no in-vivo validation claim
- no clinical performance claim
- no universal delivery prediction claim
- no state-of-the-art claim unless later formally established
- no claim of maturity comparable to AlphaFold
- no dataset ownership overclaim
- no row-level public availability overclaim
- no matched comparator claim unless datasets, labels, splits, metrics, and evaluation policies are matched
- no causal biology claim from feature importance alone

## Research Expansion Roadmap

Permea should expand across delivery tasks while keeping each task bounded and reviewable.

Near-term public-safe roadmap:

- BBB: extend the first peptide benchmark surface and evidence package.
- CPP / cell membrane: add membrane-penetration task candidates and dataset cards.
- Localization / targeting: define proxy tasks and evidence objects for localization and targeting.
- RNA/delivery-adjacent: identify sequence or formulation-adjacent benchmark surfaces where public evidence can be structured.
- Literature evidence graph: convert claims, sources, datasets, assays, and limitations into structured evidence cards.

Expansion should prioritize source clarity, label clarity, reproducibility, and conservative interpretation over broad unsupported claims.

## Closing

Permea's scientific contribution is not merely a model result.

It is an attempt to make delivery engineering benchmarkable, reproducible, and open.
