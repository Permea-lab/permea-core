"""``python -m permea_ui`` -- start the local Drylab server.

Binds 127.0.0.1 by default. This tool renders unpublished evaluation results and reads
provider credentials from the environment; neither belongs on 0.0.0.0 without a
deliberate, explicit choice.
"""

from __future__ import annotations

import argparse


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="permea-drylab", description=__doc__)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--reload", action="store_true", help="auto-reload on edit (dev)")
    args = parser.parse_args(argv)

    import uvicorn

    uvicorn.run("permea_ui.app:app", host=args.host, port=args.port, reload=args.reload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
