"""Engine -> Voice orchestration. The only module that touches permea_core/permea_explain.

THE ONE-WAY RULE, ENFORCED HERE. ``run_diagnosis`` produces the authoritative numbers.
``narrate_diagnosis`` is handed those numbers and returns prose ABOUT them. Nothing flows
back: the narration result never edits, augments, or reorders the diagnosis dict, and the
web layer renders numbers exclusively from ``DrylabResult.diagnosis``. If narration is
withheld, unavailable, or errors, the diagnosis renders unchanged -- that asymmetry is the
invariant, and it is why the two live in separate fields rather than one merged payload.

Guardrails are not re-implemented here. ``permea_explain.narrate`` raises
``GuardrailViolation`` before assembling anything, so a returned narration is by
construction one that passed. This module's only job is to turn that exception into a
status a UI can render honestly instead of letting it become a 500.
"""

from __future__ import annotations

import hashlib
import json
import logging
import os
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Literal

from permea_core.diagnose import diagnose
from permea_core.diagnose.rules import DiagnosePolicy
from permea_core.eval.run import run_from_dataset

#: Operator-only sink for withheld narrations. The offending prose is logged HERE (server
#: side) so a withheld run can be adjudicated after the fact; it is never returned to the
#: browser -- the HTTP response still carries only the headline. See narrate_diagnosis.
_log = logging.getLogger("permea_ui.narration")

#: Demo-scale evaluation settings. The CLI defaults (seeds=5, k=5, n_boot=2000) take ~53s
#: and saturate every core; these take ~9s on the example fixture and are the settings the
#: W501 -> W101 flip was verified at. A UI knob may raise them -- it must not silently
#: lower n_boot, which would widen CIs and change which codes fire.
DEMO_SEEDS = 2
DEMO_K = 3
DEMO_N_BOOT = 400

NarrationStatus = Literal["ok", "withheld", "unavailable", "error"]

#: All three must be present for ConfiguredProvider to reach a live model
#: (permea_explain/providers/configured.py). Checked up front so "no credentials" reads as
#: `unavailable` rather than surfacing as an opaque RuntimeError mid-run.
_PROVIDER_ENV = ("PERMEA_LLM_TOKEN", "PERMEA_LLM_ENDPOINT_ID", "PERMEA_LLM_BASE_URL")


@dataclass(frozen=True, slots=True)
class Narration:
    """Prose about a diagnosis, plus why it is or is not being shown.

    ``text`` is non-empty only when ``status == "ok"``. Every other status carries a
    ``detail`` the UI shows INSTEAD of prose -- a withheld narration must never be
    partially rendered, because the part that failed the guardrail is exactly the part a
    reader would most likely quote.
    """

    status: NarrationStatus
    text: str | None = None
    detail: str | None = None
    provider: str | None = None
    model_id: str | None = None
    source_report_sha256: str | None = None


@dataclass(frozen=True, slots=True)
class DrylabResult:
    """One completed analysis: authoritative numbers, plus optional prose about them."""

    diagnosis: dict[str, Any]
    narration: Narration
    dataset_name: str
    clusters_name: str
    settings: dict[str, Any] = field(default_factory=dict)


def provider_configured() -> bool:
    """True when every env var a live narration call needs is set and non-empty."""
    return all(os.environ.get(v, "").strip() for v in _PROVIDER_ENV)


class InputError(ValueError):
    """An uploaded file does not meet the loader's record contract."""


def validate_inputs(dataset_path: str | Path, clusters_path: str | Path) -> None:
    """Pre-flight the two uploads and fail with a message a person can act on.

    Without this the loader surfaces the contract violation as a bare ``KeyError:
    'length'`` from deep inside ``physchem_matrix``, several frames below anything the
    uploader recognises. This checks the header and the id coverage only -- the two
    mistakes that account for essentially every rejected upload -- and deliberately does
    not re-validate anything the engine already checks properly. Column names are read
    from the engine's own constants so this cannot drift from the real contract.
    """
    import csv

    from permea_core.represent.physchem import PHYSCHEM_COLS

    dataset_path, clusters_path = Path(dataset_path), Path(clusters_path)
    required = ("sequence_id", "sequence", "label", *PHYSCHEM_COLS)

    try:
        with dataset_path.open(newline="", encoding="utf-8-sig") as fh:
            reader = csv.DictReader(fh)
            header = reader.fieldnames or []
            rows = list(reader)
    except UnicodeDecodeError as exc:
        raise InputError("Dataset must be UTF-8 encoded CSV.") from exc

    missing = [c for c in required if c not in header]
    if missing:
        raise InputError(
            "Dataset CSV is missing required column(s): " + ", ".join(missing)
            + ". Required: " + ", ".join(required) + "."
        )
    if not rows:
        raise InputError("Dataset CSV has a header but no data rows.")

    try:
        cluster_ids = {
            line.split("\t")[0]
            for line in clusters_path.read_text(encoding="utf-8-sig").splitlines()
            if line.strip()
        }
    except UnicodeDecodeError as exc:
        raise InputError("Cluster TSV must be UTF-8 encoded.") from exc

    if not cluster_ids:
        raise InputError("Cluster TSV is empty.")

    unassigned = [r["sequence_id"] for r in rows if r["sequence_id"] not in cluster_ids]
    if unassigned:
        shown = ", ".join(unassigned[:5])
        more = f" (and {len(unassigned) - 5} more)" if len(unassigned) > 5 else ""
        raise InputError(
            f"{len(unassigned)} sequence_id(s) in the dataset have no row in the cluster "
            f"TSV: {shown}{more}. Every sequence must be assigned to a cluster."
        )


def run_diagnosis(
    dataset_path: str | Path,
    clusters_path: str | Path,
    *,
    seeds: int = DEMO_SEEDS,
    k: int = DEMO_K,
    n_boot: int = DEMO_N_BOOT,
    identity_definition: dict[str, str] | None = None,
    policy: DiagnosePolicy | None = None,
) -> dict[str, Any]:
    """Evaluate the dataset and return ``Diagnosis.to_dict()`` -- the closed contract.

    In-process by design: ``eval/run.py`` names the Drylab UI as an intended caller, and
    ``diagnose()`` is a pure function over the resulting ``EvalRun``. Shelling out to the
    CLI would only add a serialization round-trip and an argparse namespace to fake.

    Blocking and CPU-bound (RandomForest with ``n_jobs=-1``). Callers must run it off the
    request thread; see ``jobs.py``, which also serializes runs so two of them cannot
    fight over the same cores.
    """
    run = run_from_dataset(
        str(dataset_path),
        str(clusters_path),
        seeds=tuple(range(seeds)),
        k=k,
        n_boot=n_boot,
        identity_definition=identity_definition,
    )
    return diagnose(run, policy or DiagnosePolicy()).to_dict()


def narrate_diagnosis(diagnosis: dict[str, Any], *, provider: Any = None) -> Narration:
    """Narrate a diagnosis, converting every failure mode into a renderable status.

    ``permea_explain.narrate`` reads a FILE and sha256s its bytes -- the hash is a receipt
    binding the prose to an exact report, so there is no dict-accepting overload to use
    instead. We write the diagnosis to a temp file and let it hash what it actually read.

    Failure taxonomy, all non-fatal to the diagnosis:
      withheld    - output failed a guardrail (untraced number, forbidden phrase, unfired
                    code). The prose is discarded, not shown.
      unavailable - no provider credentials configured.
      error       - transport/timeout/anything else.
    """
    # Import here: permea_explain pulls optional transport deps, and a UI that only ever
    # runs diagnoses should not fail to boot because the `explain` extra is missing.
    from permea_explain import GuardrailViolation, narrate

    if provider is None and not provider_configured():
        missing = [v for v in _PROVIDER_ENV if not os.environ.get(v, "").strip()]
        return Narration(
            status="unavailable",
            detail="Narration provider not configured (missing: " + ", ".join(missing) + ")",
        )

    with tempfile.TemporaryDirectory() as tmp:
        report_path = Path(tmp) / "diagnosis.json"
        report_path.write_text(
            json.dumps(diagnosis, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        try:
            result = narrate(str(report_path), provider=provider, output_language="korean")
        except GuardrailViolation as exc:
            # Show that a check failed and how many -- never the offending text, which the
            # exception appends after a `--- offending output ---` marker.
            message = str(exc)
            headline = message.split("\n--- offending output ---", 1)[0]
            # OPERATOR-ONLY observability: the full exception still holds the offending prose
            # after the marker. Log it here (server side) with the report hash so a withheld
            # narration can be adjudicated later. This never reaches the browser -- the
            # returned Narration below carries only the headline, and app.py serializes no
            # more than that. `message` is logged whole: headline + the offending prose.
            source_report_sha256 = hashlib.sha256(report_path.read_bytes()).hexdigest()
            _log.warning(
                "narration withheld [source_report_sha256=%s]: %s",
                source_report_sha256,
                message,
            )
            return Narration(status="withheld", detail=headline)
        except Exception as exc:  # transport, timeout, malformed response
            return Narration(status="error", detail=f"{type(exc).__name__}: {exc}")

    return Narration(
        status="ok",
        text=result["narrative"]["summary"],
        provider=result["model"]["provider"],
        model_id=result["model"]["model_id"],
        source_report_sha256=result["source_report_sha256"],
    )
