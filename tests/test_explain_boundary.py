"""Import-graph boundary: permea_core -> (permea_explain | LLM SDK | network) is forbidden.

permea_explain imports permea_core (one-way). No module reachable from permea_core may
import permea_explain, an LLM SDK, or a network-transport library -- a plugin hook is a
write path, so there deliberately isn't one. This test is the enforcement.

Note: URL *string* parsing (``urllib.parse``) is allowed -- it opens no connection. Only
network-*transport* modules are forbidden.
"""
from __future__ import annotations

import ast
import subprocess
import sys
from pathlib import Path

import permea_core

# A module is forbidden if it equals one of these or is a submodule of it.
FORBIDDEN = (
    "permea_explain",
    "openai",
    "anthropic",
    "requests",
    "httpx",
    "aiohttp",
    "socket",
    "http.client",
    "http.server",
    "urllib.request",
    "ftplib",
    "smtplib",
    "telnetlib",
)


def _forbidden_root(mod: str) -> str | None:
    for f in FORBIDDEN:
        if mod == f or mod.startswith(f + "."):
            return f
    return None


def _iter_imports(tree: ast.AST):
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                yield node.lineno, alias.name
        elif isinstance(node, ast.ImportFrom):
            # level == 0 -> absolute import; relative imports stay inside permea_core.
            if node.module and node.level == 0:
                yield node.lineno, node.module


def test_permea_core_source_has_no_forbidden_imports():
    root = Path(permea_core.__file__).parent
    violations: list[str] = []
    for path in sorted(root.rglob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for lineno, mod in _iter_imports(tree):
            f = _forbidden_root(mod)
            if f is not None:
                violations.append(f"{path.relative_to(root)}:{lineno} imports {mod!r} (forbidden: {f})")
    assert not violations, (
        "permea_core must not import permea_explain / an LLM SDK / a network library:\n"
        + "\n".join(violations)
    )


def test_importing_permea_core_pulls_no_forbidden_module():
    """Fresh subprocess so other tests importing permea_explain/openai don't pollute sys.modules."""
    code = (
        "import sys\n"
        "import permea_core\n"
        "import permea_core.diagnose, permea_core.eval.run, permea_core.contracts.warnings\n"
        "banned = {'permea_explain','openai','anthropic','requests','httpx','aiohttp'}\n"
        "bad = sorted(m for m in sys.modules if m.split('.')[0] in banned)\n"
        "print(';'.join(bad))\n"
        "sys.exit(1 if bad else 0)\n"
    )
    r = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True)
    assert r.returncode == 0, (
        f"importing permea_core pulled forbidden modules: {r.stdout.strip()!r} {r.stderr.strip()!r}"
    )
