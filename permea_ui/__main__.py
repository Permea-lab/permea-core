"""``python -m permea_ui`` -- start the local Drylab server.

Binds 127.0.0.1 by default. This tool renders unpublished evaluation results and reads
provider credentials from the environment; neither belongs on 0.0.0.0 without a
deliberate, explicit choice.
"""

from __future__ import annotations

import argparse


def _browse_host(host: str) -> str:
    """The host a browser should actually hit.

    ``0.0.0.0`` (and an empty bind address) mean "listen on every interface" -- they are not
    browseable addresses, so a browser must be pointed at loopback instead.
    """
    return "127.0.0.1" if host in ("0.0.0.0", "") else host


def _open_browser_when_up(host: str, port: int, *, timeout: float = 10.0) -> None:
    """Open the default browser once the server is accepting connections.

    Runs on a background daemon thread so it never blocks ``uvicorn.run``. It POLLS the TCP
    port rather than sleeping a fixed guess, so the browser opens only AFTER the server is
    listening -- opening early races the bind and shows a connection error. If the server
    never comes up within ``timeout``, the thread exits silently rather than disturbing the
    server process.
    """
    import socket
    import threading
    import time
    import webbrowser

    target = _browse_host(host)
    url = f"http://{target}:{port}"

    def _wait_and_open() -> None:
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            try:
                with socket.create_connection((target, port), timeout=0.5):
                    break
            except OSError:
                time.sleep(0.1)
        else:
            return  # never came up in time -- do not open a dead URL, do not crash the server
        webbrowser.open(url)

    threading.Thread(target=_wait_and_open, name="permea-drylab-open", daemon=True).start()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="permea-drylab", description=__doc__)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--reload", action="store_true", help="auto-reload on edit (dev)")
    parser.add_argument(
        "--open",
        action="store_true",
        dest="open_browser",
        help="open the UI in the default web browser once the server is up",
    )
    args = parser.parse_args(argv)

    # Start the opener BEFORE uvicorn.run (which blocks); it waits on a background thread for
    # the port to accept connections, then opens the browser. No --open => identical to before.
    if args.open_browser:
        _open_browser_when_up(args.host, args.port)

    import uvicorn

    uvicorn.run("permea_ui.app:app", host=args.host, port=args.port, reload=args.reload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
