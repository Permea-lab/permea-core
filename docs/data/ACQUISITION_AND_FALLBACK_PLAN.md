# Acquisition And Fallback Plan

Status: Public planning document

Date: 2026-06-11

## Purpose

This plan defines staged acquisition for online public data sources that may
support Permea benchmark tasks. It does not download datasets, scrape websites,
run machine learning, or commit data. The first deliverable is source
understanding: what the source contains, how it could be acquired later, what
license/access risks exist, and how it maps to benchmark tasks.

## Stage 1: Manual Source Cards

Stage 1 creates manually verified source cards only.

Required work:

- identify public URLs, papers, repositories, or citation placeholders
- record expected data fields without copying row-level datasets
- record license/access notes as `to verify` unless confirmed from the source
- record provenance fields that must be preserved later
- map each source to one or more benchmark candidates
- keep all sources in source-card-only mode when access or license is unclear
- avoid automated scraping, bulk downloads, or automated literature extraction

Expected outputs:

- online source registry
- source cards
- acquisition risk notes
- benchmark mapping notes

## Stage 2: Lightweight Acquisition Or Metadata Harvesting

Stage 2 is allowed only for sources that permit the planned retrieval mode.

Rules:

- use lightweight downloader or metadata harvester scripts only after terms are reviewed
- keep credentials out of the repository
- write outputs only to ignored local directories
- record source version, access date, query parameters, and file hashes when applicable
- preserve source identifiers rather than replacing them with internal-only IDs
- do not redistribute row-level data unless the source license permits it
- prefer metadata-only acquisition for literature sources until text reuse is reviewed

Stage 2 should produce reproducible acquisition notes, not benchmark claims.

## Stage 3: Dataset Cards, Evidence Cards, And Split Proposals

Stage 3 converts reviewed sources into Permea artifacts.

Required work:

- create dataset cards that describe source, labels, readiness, and limitations
- create evidence cards for literature-derived or source-backed claims
- propose benchmark task specs, including labels, metrics, splits, and outputs
- record a provenance ledger with source IDs, version/access date, transformations,
  and reviewer notes
- identify leakage risks, duplicate sequence policy, and label ambiguity policy
- mark positive-only sources as requiring a negative sampling proposal before
  benchmark use

Stage 3 should not imply that a benchmark is reproducible until data, splits,
baselines, outputs, and manifests are present.

## Stage 4: Benchmark-Ready Packages Or Reproducible Acquisition

Stage 4 prepares benchmark-ready datasets only when release posture allows it.

Allowed outcomes:

- packaged benchmark dataset if license permits redistribution
- script-based reproducible acquisition if row-level redistribution is not allowed
- metadata-only benchmark support if data access remains web-only or restricted
- source-card-only archive if access or license remains unclear

Required outputs for benchmark-ready status:

- dataset card
- benchmark task spec
- split policy
- baseline requirements
- evidence card policy
- run manifest requirements
- provenance ledger
- public claim boundary

## Fallback Rules

- If direct download is unavailable, use source-card-only mode.
- If license is unclear, mark the source `no-redistribution`.
- If data is web-only, use manual provenance notes first.
- If a source has positive-only labels, flag negative sampling risk.
- If a source has literature-derived labels, preserve PubMed/DOI provenance.
- If a source is a proxy rather than direct delivery data, mark it as
  proxy/localization axis.
- If a source mixes assays, cargo types, organisms, or modified sequences, keep
  those fields explicit and avoid collapsing them into a single broad label.
- If source records are unavailable but the publication remains useful, retain
  the source card as a citation/evidence pointer rather than inventing rows.

## Current Priority Order

1. BBB sources: B3PDB, BrainPeps, and B3Pred Dataset 3 lineage.
2. CPP sources: CPPsite 2.0 and original CPPsite lineage.
3. Proxy/localization sources: DeepLoc, UniProt subcellular location, SignalP or TargetP.
4. Literature evidence graph sources: PubMed, Europe PMC, and OpenAlex.

## Non-Goals

- no dataset download in this task
- no scraping in this task
- no machine learning execution in this task
- no data committed under `data/` or `datasets/`
- no claim that a source has become benchmark-ready solely because it is listed
