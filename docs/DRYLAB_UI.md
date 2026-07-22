# Drylab web UI

A local web front end over two things that already exist: the diagnose engine
(`permea_core`) and the interpretation layer (`permea_explain`). It adds no evaluation
logic of its own.

## Install and run

```bash
pip install -e ".[ui,explain]"
permea-drylab              # http://127.0.0.1:8000
```

Binds `127.0.0.1` by default. This tool renders unpublished evaluation results and reads
provider credentials from the environment, so exposing it on `0.0.0.0` should be a
deliberate choice (`--host`), not a default.

Narration is optional. Without `PERMEA_LLM_TOKEN`, `PERMEA_LLM_ENDPOINT_ID`, and
`PERMEA_LLM_BASE_URL` the UI runs diagnoses normally and reports the interpretation panel
as *unavailable*.

## What it demonstrates

Load the bundled example and run it twice — once under each cluster assignment. The rows,
the dataset sha256, the cluster count, the model, the metric, and the settings are
identical across both runs. Only the honesty of the clustering changes:

| Cluster assignment | Fires | Reading |
|---|---|---|
| Naive (near-duplicates scattered) | `PERMEA-W501` | Inconclusive — the CI includes zero |
| Identity-aware (near-duplicates held together) | `PERMEA-W101` | Material similarity leakage |

That flip is the argument. An evaluation can look reassuring for no better reason than
that its clustering was too permissive to notice.

The example data is **synthetic**. No PermeaBench dataset is vendored in this repo — see
`acquisition_manifests/b3pred_dataset3.yaml` (`no-redistribution-source-card-only`) — so
the UI ships a stand-in that exhibits the same structure rather than implying a
redistribution right it does not have. Every surface that renders it says so.

## Bring your own data

The **Upload** tab takes the same two files `permea bench diagnose` takes:

- **Dataset CSV** — header required, with `sequence_id`, `sequence`, `label`, and the five
  physchem columns `length`, `charge`, `gravy`, `pI`, `aromaticity`. The physchem values
  are read, never recomputed from the residues, so they stay byte-identical to whatever the
  dataset's own sha256 covers.
- **Cluster TSV** — headerless, `sequence_id<TAB>cluster_id`, one row per sequence. Every
  `sequence_id` in the CSV must appear.

Malformed files are rejected before the job is queued, with a message naming the missing
column or the unassigned ids.

## What the layering guarantees

**Numbers come from the engine only.** The API returns `Diagnosis.to_dict()` verbatim; the
browser formats for display and computes nothing. Every number a reader sees traces to a
key in the report.

**Interpretation is downstream and clearly marked.** `permea_explain.narrate` validates
generated prose before returning it — numeric provenance, forbidden phrasing, and no
warning code that did not actually fire. A failure raises before anything is assembled, so
prose that failed a check is discarded rather than shown; the panel reports *withheld* and
the findings above it are unaffected. The panel is visually distinct from engine output and
labelled *not authoritative*.

**Which model answers is not disclosed.** The narration payload carries the provider name
and the source-report sha256, never a model id.

## Reserved codes are shown on purpose

The registry panel lists every code, including reserved ones such as `PERMEA-W403`
(EnvironmentUnpinned) and `PERMEA-W404` (ClusterArtifactUnarchived). These are catalogued
but have no firing logic — they need inputs an `EvalRun` does not carry — so they can never
appear in a report. Showing them keeps a clean report from being read as a broader
all-clear than it is.

## Operational notes

One evaluation is CPU-bound and claims every core (`RandomForest(n_jobs=-1)`). Jobs run on
a single worker thread and are queued, not parallelised — a second concurrent run would
oversubscribe the machine rather than finish sooner. The UI defaults to demo-scale settings
(2 seeds, k=3, 400 bootstrap resamples, ~10s); the CLI defaults (5 seeds, k=5, 2000
resamples) take roughly a minute.

Job state is in-memory and single-process. That is the right trade for a local tool; a
deployment that outlives a process needs a real broker.
