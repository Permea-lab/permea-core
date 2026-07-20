"""The `permea` unified CLI dispatcher.

`permea <group> <command> ...` -- the first real dispatcher (deliberately not the loose
scripts/permea_*.py convention). Groups register their own subparsers; v0 ships `bench`
(with `diagnose`), leaving clean room for future groups such as `permea drylab`.

The dispatcher orchestrates existing library functions only -- it adds no evaluation logic
and no new numbers.
"""

from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="permea", description="PermeaBench CLI.")
    groups = parser.add_subparsers(dest="group", required=True)

    from permea_core.cli.bench import register as register_bench

    register_bench(groups)
    # future: from permea_core.cli.drylab import register as register_drylab; register_drylab(groups)
    return parser


def main(argv: list[str] | None = None) -> int:
    """Entry point (see [project.scripts] permea). Returns the process exit code."""
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
