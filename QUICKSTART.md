# Permea Core Quickstart

This quickstart is the first-user path for Permea Core. It is designed for researchers and developers who want one successful local result in under five minutes without downloading datasets, executing acquisition, or running a model workflow.

## Setup Assumptions

- Python 3 is available as `python3`.
- The repository has been cloned locally.
- Commands are run from the repository root.
- No private data, external service, dataset download, or model run is required.

## What Permea Core Is

Permea Core is a public execution and specification layer for benchmark-first delivery evidence artifacts. It provides artifact standards, deterministic examples, local validators, evidence links, and claim boundaries so computational delivery evidence can be inspected before experimental follow-up.

## What The Example Packages Demonstrate

The copyable packages under [examples/](examples/) demonstrate the current artifact standard:

- dataset cards
- benchmark cards
- evidence cards
- run manifests
- output packages
- validation results
- explicit non-claims and claim-boundary wording

The examples are reference fixtures. They demonstrate package structure and validation compatibility, not biological or model results.

## One Command To Run

From the repository root:

```bash
python3 scripts/permea_demo.py
```

## What Output To Expect

The demo prints:

- a short description of Permea Core
- discovered example packages
- validator status for each package
- links to evidence and claim-boundary surfaces
- generated evaluation and evidence output paths
- explicit non-claims
- next recommended commands

A successful run ends with:

```text
Status: PASS
```

## How To Validate Examples

Validate all built-in public examples and generated artifacts:

```bash
python3 scripts/permea_check.py
```

Validate one example package:

```bash
python3 scripts/permea_check.py examples/synthetic_reference_example
```

Run the broader local validation bundle:

```bash
python3 scripts/permea_validate.py
python3 scripts/validate_permea_artifacts.py
```

## How To Inspect Evidence And Claim Boundaries

Start with:

- [Evidence index](docs/evidence/evidence-index.md)
- [Evidence layer](docs/evidence/README.md)
- [Claim registry](docs/claims/claim-registry.md)
- [Claim boundary](docs/CLAIM_BOUNDARY.md)
- [External examples](examples/README.md)
- [Generated evaluation packet](docs/examples/generated/EVALUATION_PACKET.md)
- [Generated evidence matrix](docs/examples/generated/EVIDENCE_MATRIX.md)
- [Generated evidence surface](docs/examples/generated/README.md)

These surfaces explain which claims are supported by current public artifacts, which claims are unsupported, and which validation commands reviewers should run.

## What Is Not Claimed

- no dataset downloaded
- no acquisition executed
- no redistribution rights confirmed
- no wet-lab validation by Permea
- no clinical efficacy claim
- no model performance claim
- no SOTA claim
- no solved-delivery claim

## Next Recommended Commands

```bash
python3 scripts/permea_check.py
python3 scripts/permea_specs.py
python3 scripts/permea_evaluate.py
python3 scripts/permea_reproduce.py
python3 scripts/permea_validate.py
```

## Troubleshooting

- If the demo cannot find examples, confirm you are running from the repository root.
- If validation fails, run `python3 scripts/permea_check.py path/to/example` for the failing package.
- If generated files look stale, run `python3 scripts/permea_reproduce.py`.
