"""`permea bench` group: benchmark diagnostics.

`permea bench diagnose DATASET CLUSTERS` runs the completed library pipeline end-to-end:
run_from_dataset -> EvalRun -> diagnose -> Diagnosis, then formats and exits. It calls
existing functions only; no evaluation logic or numbers live here.
"""

from __future__ import annotations

import argparse
import json
import os
import sys

from permea_core.diagnose import DEFAULT_POLICY


def register(groups: argparse._SubParsersAction) -> None:
    bench = groups.add_parser("bench", help="benchmark diagnostics")
    commands = bench.add_subparsers(dest="bench_command", required=True)

    d = commands.add_parser(
        "diagnose",
        help="diagnose a benchmark run for permea-eval/1.0 warning codes",
        description="Run the honest-evaluation pipeline on a dataset + clusters and report "
        "the fired warning codes.",
    )
    # positional inputs
    d.add_argument("dataset", help="dataset CSV (sequence_id, sequence, label, physchem cols)")
    d.add_argument("clusters", help="cluster TSV (sequence_id <TAB> cluster_id)")
    # evaluation passthroughs (-> run_from_dataset)
    d.add_argument("--representation", default="physchem", help="v0: physchem only")
    d.add_argument("--seeds", type=int, default=5, help="number of seeds; uses range(seeds)")
    d.add_argument("--k", type=int, default=5, help="CV folds")
    d.add_argument("--n-boot", type=int, default=2000, dest="n_boot", help="bootstrap iterations")
    d.add_argument(
        "--identity-definition",
        default=None,
        dest="identity_definition",
        help='identity definition as a JSON object string, e.g. \'{"alignment":"global"}\'',
    )
    # DiagnosePolicy overrides (defaults sourced from DEFAULT_POLICY to avoid drift)
    d.add_argument("--headline-model", default=DEFAULT_POLICY.headline_model, dest="headline_model")
    d.add_argument("--headline-metric", default=DEFAULT_POLICY.headline_metric, dest="headline_metric")
    d.add_argument("--materiality", type=float, default=DEFAULT_POLICY.materiality_min_abs_delta,
                   help="absolute materiality threshold for W101")
    d.add_argument("--min-clusters", type=int, default=DEFAULT_POLICY.min_clusters, dest="min_clusters",
                   help="cluster-count cutoff for W502")
    # output
    d.add_argument("--json", action="store_true", help="emit the closed Diagnosis as JSON")
    d.add_argument("-o", "--output", default=None, help="write to file (default: stdout)")
    d.add_argument("--fail-on-warn", action="store_true", dest="fail_on_warn",
                   help="exit 1 if any warning fired")
    d.set_defaults(func=run_diagnose)


def run_diagnose(args: argparse.Namespace) -> int:
    """Handler for `permea bench diagnose`. Returns the exit code (0 / 1 / 2)."""
    # Heavy imports are deferred so `permea --help` and arg errors stay fast/ML-free.
    from permea_core.diagnose import DiagnosePolicy, diagnose
    from permea_core.eval.run import run_from_dataset

    from ._format import render_text

    identity_definition = None
    if args.identity_definition is not None:
        try:
            identity_definition = json.loads(args.identity_definition)
        except json.JSONDecodeError as exc:
            print(f"error: --identity-definition is not valid JSON: {exc}", file=sys.stderr)
            return 2
        if not isinstance(identity_definition, dict) or not all(
            isinstance(k, str) and isinstance(v, str) for k, v in identity_definition.items()
        ):
            print("error: --identity-definition must be a JSON object of string->string", file=sys.stderr)
            return 2

    try:
        run = run_from_dataset(
            args.dataset,
            args.clusters,
            representation=args.representation,
            seeds=tuple(range(args.seeds)),
            k=args.k,
            n_boot=args.n_boot,
            identity_definition=identity_definition,
        )
    except (ValueError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    policy = DiagnosePolicy(
        headline_model=args.headline_model,
        headline_metric=args.headline_metric,
        materiality_min_abs_delta=args.materiality,
        min_clusters=args.min_clusters,
    )
    try:
        diag = diagnose(run, policy)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.json:
        text = json.dumps(diag.to_dict(), indent=2)
    else:
        text = render_text(diag, os.path.basename(args.dataset))

    if args.output:
        with open(args.output, "w") as fh:
            fh.write(text + "\n")
    else:
        print(text)

    if args.fail_on_warn and diag.summary.total > 0:
        return 1
    return 0
