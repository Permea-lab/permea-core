# Delivery Taxonomy

## Purpose

This document defines an initial canonical Permea taxonomy for sequence-first delivery work. Its role is to provide a reusable language layer for benchmark docs, evidence packages, architecture notes, and future paper or deck material.

## Design principles

The taxonomy is intentionally narrow, legible, and reusable. It is not presented as universal or final. It is a first-pass Permea structure for describing delivery problems, intended objectives, failure patterns, and evidence status without overstating what current work can justify.

## Barrier classes

Barrier classes describe the boundary or context that constrains successful transport.

- cell membrane
- blood-brain barrier (BBB)
- nuclear membrane / nuclear localization boundary
- tissue-specific or barrier-mimetic contexts

These classes are useful because transport claims are often only meaningful relative to a specific barrier surface.

## Transport objective classes

Transport objective classes describe what successful movement or access is meant to accomplish.

- uptake / internalization
- endosomal escape
- intracellular localization
- nuclear localization
- selective tissue access

Separating objective classes helps avoid collapsing distinct biological problems into a single notion of "delivery."

## Failure mode classes

Failure mode classes describe common ways a candidate can fail even when some movement is observed.

- no internalization
- low transport efficiency
- degradation before action
- off-target diffusion
- non-productive uptake
- inadequate localization after entry

These categories help keep benchmark framing tied to specific failure surfaces rather than broad success language.

## Evidence classes

Evidence classes describe the type of support available for a delivery-related statement.

- computational evidence
- literature-grounded plausibility
- in vitro evidence
- barrier-mimetic validation
- stronger biological validation

These classes should be used to constrain interpretation, not to inflate it.

## Why this taxonomy exists

Permea needs a stable field grammar for benchmark-first work. Without a consistent taxonomy, delivery discussions become difficult to compare across datasets, models, documents, and validation stages. This taxonomy gives Permea an initial canonical structure for describing barrier-specific work with clearer scope and claim discipline.
