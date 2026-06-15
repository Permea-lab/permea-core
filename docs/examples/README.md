# Permea Examples

Status: Public documentation

## What Examples Are For

Examples show the expected shape of Permea Core benchmark artifacts before contributors create or review their own.

They are meant to make public specifications easier to use by showing placeholder structures, toy identifiers, and public-safe output layouts.

Examples should help reviewers answer practical questions:

- What files should a benchmark run export?
- What metadata belongs in a run manifest?
- What should remain in limitation notes?
- How should example candidates be represented without exposing sensitive or unreleased material?
- Which claims are outside the artifact boundary?

## Current Example Types

Current and planned example types include:

- output package structure
- future benchmark registry examples
- future dataset card examples
- future run manifest examples

The first example document is:

- [Example Output Package](EXAMPLE_OUTPUT_PACKAGE.md)

## What Examples Are Not

Examples are not wet-lab validation.

Examples are not clinical claims.

Examples are not broad prediction across delivery contexts.

Examples are not evidence that a benchmark is complete, reproducible, or community-reviewed unless the example explicitly links to reviewed public artifacts that support that status.

## How Contributors Can Use Examples

Contributors can use examples to:

- structure a proposed benchmark output package
- check that artifact names match Permea Core conventions
- separate aggregate metrics from candidate-level review material
- include limitation notes with every output package
- keep public claims tied to computational review
- avoid adding private infrastructure or unreleased candidate details

Examples should be treated as starting points. A real contribution still needs a dataset card, benchmark task spec, run manifest, evidence cards where relevant, and review against the public claim boundary.
