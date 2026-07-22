"""FastAPI surface for the Drylab UI. Transport only -- no evaluation logic lives here.

Serialization boundary. ``/api/jobs/{id}`` returns the diagnosis dict VERBATIM as the
engine produced it: no rounding, no re-labelling, no derived fields. The browser formats
for display but computes nothing. Any number a reader sees can be traced to a key in
``Diagnosis.to_dict()``, which is the same property the narration guardrail enforces on
prose -- the two surfaces are held to one standard.

Model identity is deliberately not exposed. The narration payload carries the provider
name but never ``model_id``; which model sits behind the configured endpoint is the
adapter's business, and a demo screen is exactly where that would leak.
"""

from __future__ import annotations

import shutil
import tempfile
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from permea_core.contracts.warnings import WARNINGS
from permea_ui import fixtures, runner
from permea_ui.jobs import REGISTRY, Job

STATIC_DIR = Path(__file__).parent / "static"

app = FastAPI(title="Permea Drylab", docs_url="/api/docs")

#: Fixtures are written once per process, not per request -- they are deterministic, so
#: regenerating them would only churn the sha256 the diagnosis reports for identical data.
_EXAMPLE_DIR = Path(tempfile.gettempdir()) / "permea_drylab_example"
_EXAMPLE: dict[str, Path] | None = None


def _example() -> dict[str, Path]:
    global _EXAMPLE
    if _EXAMPLE is None:
        _EXAMPLE = fixtures.write_example(_EXAMPLE_DIR)
    return _EXAMPLE


def _narration_payload(n: runner.Narration) -> dict[str, Any]:
    """Serialize a Narration. Note the absent `model_id` -- see the module docstring."""
    return {
        "status": n.status,
        "text": n.text,
        "detail": n.detail,
        "provider": n.provider,
        "source_report_sha256": n.source_report_sha256,
        "authoritative": False,  # restated on the wire so the client cannot forget it
    }


def _result_payload(r: runner.DrylabResult) -> dict[str, Any]:
    return {
        "diagnosis": r.diagnosis,  # verbatim engine output
        "narration": _narration_payload(r.narration),
        "dataset_name": r.dataset_name,
        "clusters_name": r.clusters_name,
        "settings": r.settings,
    }


def _analysis(
    dataset: Path,
    clusters: Path,
    *,
    dataset_name: str,
    clusters_name: str,
    seeds: int,
    k: int,
    n_boot: int,
    declare_identity: bool,
    cleanup: Path | None = None,
):
    """Build the worker callable: diagnose, then narrate, then report."""

    def work(job: Job) -> runner.DrylabResult:
        try:
            job.stage = "evaluating"
            # W001 fires whenever identity_definition is None. The checkbox is the user's
            # declaration, not ours to supply -- an unchecked box is a real finding about
            # how the run was configured, so we pass None and let the rule fire.
            identity = {"alignment": "global"} if declare_identity else None
            diagnosis = runner.run_diagnosis(
                dataset, clusters, seeds=seeds, k=k, n_boot=n_boot,
                identity_definition=identity,
            )
            job.stage = "narrating"
            narration = runner.narrate_diagnosis(diagnosis)
            return runner.DrylabResult(
                diagnosis=diagnosis,
                narration=narration,
                dataset_name=dataset_name,
                clusters_name=clusters_name,
                settings={"seeds": seeds, "k": k, "n_boot": n_boot,
                          "identity_declared": declare_identity},
            )
        finally:
            if cleanup is not None:
                shutil.rmtree(cleanup, ignore_errors=True)

    return work


@app.get("/api/warnings")
def warnings_catalog() -> dict[str, Any]:
    """The full registry, ACTIVE and RESERVED alike.

    RESERVED codes are shipped to the client on purpose. W403 (EnvironmentUnpinned) and
    W404 (ClusterArtifactUnarchived) need inputs an EvalRun does not carry, so they can
    never appear in `fired`. Showing them as catalogued-but-unimplemented is honest;
    hiding them would let a viewer read a clean report as a broader all-clear than it is.
    """
    return {
        "codes": [
            {
                "code": w.code, "title": w.title, "family": str(w.family),
                "kind": str(w.kind), "status": str(w.status), "severity": str(w.severity),
                "fire_condition": w.fire_condition, "description": w.description,
                "pillar": w.pillar,
            }
            for w in WARNINGS
        ]
    }


@app.get("/api/status")
def status() -> dict[str, Any]:
    return {
        "narration_available": runner.provider_configured(),
        "pending_jobs": REGISTRY.pending(),
        "defaults": {"seeds": runner.DEMO_SEEDS, "k": runner.DEMO_K,
                     "n_boot": runner.DEMO_N_BOOT},
        # Served rather than hardcoded in the page so the "this is not a real dataset"
        # disclaimer has exactly one definition (fixtures.EXAMPLE_LABEL) to keep true.
        "example_label": fixtures.EXAMPLE_LABEL,
    }


@app.post("/api/jobs/example")
def submit_example(
    clustering: str = "naive", seeds: int = runner.DEMO_SEEDS,
    k: int = runner.DEMO_K, n_boot: int = runner.DEMO_N_BOOT,
    # Defaults to False here exactly as it does for uploads: declaring an identity
    # definition is a claim about the run, and the tool does not make that claim on the
    # caller's behalf just because the data happens to be ours.
    declare_identity: bool = False,
) -> dict[str, Any]:
    """Run the bundled synthetic example under one of its two cluster assignments."""
    if clustering not in ("naive", "family"):
        raise HTTPException(400, "clustering must be 'naive' or 'family'")
    ex = _example()
    job = REGISTRY.submit(
        _analysis(
            ex["dataset"], ex[clustering],
            dataset_name=f"{fixtures.EXAMPLE_LABEL} / {ex['dataset'].name}",
            clusters_name=ex[clustering].name,
            seeds=seeds, k=k, n_boot=n_boot, declare_identity=declare_identity,
        ),
        meta={"source": "example", "clustering": clustering},
    )
    return {"job_id": job.id, "queue_depth": REGISTRY.pending()}


@app.post("/api/jobs")
async def submit_upload(
    dataset: UploadFile, clusters: UploadFile,
    seeds: int = runner.DEMO_SEEDS, k: int = runner.DEMO_K,
    n_boot: int = runner.DEMO_N_BOOT, declare_identity: bool = False,
) -> dict[str, Any]:
    """Run a diagnose over an uploaded dataset CSV + cluster TSV."""
    workdir = Path(tempfile.mkdtemp(prefix="drylab_upload_"))
    ds = workdir / "dataset.csv"
    cl = workdir / "clusters.tsv"
    for upload, dest in ((dataset, ds), (clusters, cl)):
        dest.write_bytes(await upload.read())

    # Validate before queueing: a contract violation is the user's to fix now, not
    # something to discover after waiting behind another run for a job that cannot succeed.
    try:
        runner.validate_inputs(ds, cl)
    except runner.InputError as exc:
        shutil.rmtree(workdir, ignore_errors=True)
        raise HTTPException(400, str(exc)) from exc

    job = REGISTRY.submit(
        _analysis(
            ds, cl,
            dataset_name=dataset.filename or "dataset.csv",
            clusters_name=clusters.filename or "clusters.tsv",
            seeds=seeds, k=k, n_boot=n_boot, declare_identity=declare_identity,
            cleanup=workdir,
        ),
        meta={"source": "upload"},
    )
    return {"job_id": job.id, "queue_depth": REGISTRY.pending()}


@app.get("/api/jobs/{job_id}")
def job_state(job_id: str) -> JSONResponse:
    job = REGISTRY.get(job_id)
    if job is None:
        raise HTTPException(404, "unknown job")
    body: dict[str, Any] = {"id": job.id, "status": job.status, "stage": job.stage,
                            "meta": job.meta}
    if job.status == "done":
        body["result"] = _result_payload(job.result)
    elif job.status == "failed":
        body["error"] = job.error
    return JSONResponse(body)


@app.get("/")
def index() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")


app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
