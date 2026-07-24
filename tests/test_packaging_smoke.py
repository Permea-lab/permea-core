"""Clean-install packaging smoke test.

Every other test in this suite runs against an *editable* install, where the whole repo is
on ``sys.path``. That layout structurally cannot catch a packaging regression: a file that
exists in the repo but is never declared to ship (missing ``package-data``, or a data file
that lives outside the three package trees) is still importable in-place, so an editable
test sees it and passes -- while a real ``pip install`` user gets a wheel without it.

This test closes that gap by taking the outside-user path exactly: build a real wheel,
install it into a throwaway venv, then drive the public ``permea bench diagnose`` console
script from a working directory OUTSIDE the repo, on inputs produced by the *installed*
``permea_ui.fixtures.write_example``. If any runtime file failed to ship, this fails.

Marked ``packaging`` (and ``slow``) so fast unit runs can deselect it::

    pytest -m "not packaging"

Needs no network beyond the PyPI dependency resolve that ``build`` (isolated backend) and
``pip install`` perform -- i.e. it is CI-safe wherever PyPI is reachable.
"""

from __future__ import annotations

import subprocess
import sys
import venv
from pathlib import Path

import pytest

pytestmark = [pytest.mark.slow, pytest.mark.packaging]

REPO_ROOT = Path(__file__).resolve().parents[1]


def _run(cmd: list[str], **kwargs: object) -> subprocess.CompletedProcess[str]:
    """Run a subprocess, capturing text output; raise with full output on failure."""
    proc = subprocess.run(cmd, capture_output=True, text=True, **kwargs)  # type: ignore[call-overload]
    if proc.returncode != 0:
        raise AssertionError(
            f"command failed ({proc.returncode}): {' '.join(cmd)}\n"
            f"--- stdout ---\n{proc.stdout}\n--- stderr ---\n{proc.stderr}"
        )
    return proc


def test_wheel_installs_and_diagnose_runs_from_clean_venv(tmp_path: Path) -> None:
    # `python -m build` is the canonical wheel builder; it ships in the `dev` extra. Gate on
    # the ACTUAL capability, not an `import build`: a bare env may have an unrelated module
    # also named `build` on sys.path, which imports fine yet has no runnable CLI. Probe the
    # real invocation and skip (don't fail) when it is unavailable -- CI installs `.[dev]`.
    probe = subprocess.run(
        [sys.executable, "-m", "build", "--version"], capture_output=True, text=True
    )
    if probe.returncode != 0:
        pytest.skip("`python -m build` is unavailable (install the `dev` extra) -- cannot build a wheel")

    # 1. Build a wheel from the repo into a temp dir (isolated backend pulls setuptools).
    dist = tmp_path / "dist"
    _run([sys.executable, "-m", "build", "--wheel", "--outdir", str(dist), str(REPO_ROOT)])
    wheels = list(dist.glob("*.whl"))
    assert len(wheels) == 1, f"expected exactly one wheel, got {wheels}"

    # 2. Fresh venv; install the wheel (this resolves numpy/scikit-learn from PyPI).
    venv_dir = tmp_path / "venv"
    venv.create(venv_dir, with_pip=True)
    win = sys.platform == "win32"
    bin_dir = venv_dir / ("Scripts" if win else "bin")
    py = bin_dir / ("python.exe" if win else "python")
    _run([str(py), "-m", "pip", "install", "--quiet", str(wheels[0])])

    # 3. Materialize the synthetic demo fixture using the INSTALLED package, not the repo.
    fixture_dir = tmp_path / "fixture"
    fixture_dir.mkdir()
    _run([
        str(py), "-c",
        "from pathlib import Path; from permea_ui.fixtures import write_example; "
        f"write_example(Path({str(fixture_dir)!r}))",
    ])
    dataset = fixture_dir / "example_dataset.csv"
    clusters = fixture_dir / "clusters_family.tsv"
    assert dataset.exists() and clusters.exists(), "write_example did not produce the expected files"

    # 4. Drive the console script from OUTSIDE the repo; assert clean exit + a fired code.
    permea = bin_dir / ("permea.exe" if win else "permea")
    proc = subprocess.run(
        [str(permea), "bench", "diagnose", str(dataset), str(clusters)],
        cwd=str(tmp_path),  # deliberately not the repo root
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, f"diagnose exited {proc.returncode}\n{proc.stderr}"
    assert "PERMEA-W" in proc.stdout, f"expected a warning code in output, got:\n{proc.stdout}"
