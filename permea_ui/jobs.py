"""A single-worker job queue for diagnose runs.

WHY SERIALIZED, NOT POOLED. ``RandomForestClassifier(n_jobs=-1)`` already claims every
core, so a second concurrent diagnose does not halve wall time -- it oversubscribes the
box and makes both runs slower. One worker thread is the correct amount of parallelism
here, and the queue depth is what the UI shows instead of a spinner that means nothing.

WHY THREADS, NOT PROCESSES. The heavy work is scikit-learn/BLAS, which releases the GIL,
so a thread is enough to keep the event loop responsive. A process pool would also mean
re-importing sklearn per worker and shipping the diagnosis back over a pipe, for no gain
at a concurrency of one.

Scope: in-memory, single-process, lost on restart. That is the right trade for a local
demo tool; a deployment that outlives a process needs a real broker, not a bigger dict.
"""

from __future__ import annotations

import queue
import threading
import traceback
import uuid
from dataclasses import dataclass, field
from typing import Any, Callable, Literal

JobStatus = Literal["queued", "running", "done", "failed"]


@dataclass
class Job:
    """One unit of work and whatever it has produced so far."""

    id: str
    status: JobStatus = "queued"
    #: Free-text stage the worker is in, so the UI can say "evaluating" vs "narrating"
    #: rather than showing one opaque spinner across a ~10s run and a ~10s LLM call.
    stage: str = "queued"
    result: Any = None
    error: str | None = None
    meta: dict[str, Any] = field(default_factory=dict)


class JobRegistry:
    """Thread-safe job store fed by one worker thread."""

    def __init__(self) -> None:
        self._jobs: dict[str, Job] = {}
        self._lock = threading.Lock()
        self._queue: queue.Queue[tuple[str, Callable[[Job], Any]]] = queue.Queue()
        self._worker = threading.Thread(target=self._run, daemon=True, name="drylab-worker")
        self._worker.start()

    def submit(self, fn: Callable[[Job], Any], *, meta: dict[str, Any] | None = None) -> Job:
        """Queue ``fn``; it receives its own Job so it can report stage transitions."""
        job = Job(id=uuid.uuid4().hex[:12], meta=meta or {})
        with self._lock:
            self._jobs[job.id] = job
        self._queue.put((job.id, fn))
        return job

    def get(self, job_id: str) -> Job | None:
        with self._lock:
            return self._jobs.get(job_id)

    def pending(self) -> int:
        """Jobs queued or running -- what the UI shows as "N ahead of you"."""
        with self._lock:
            return sum(1 for j in self._jobs.values() if j.status in ("queued", "running"))

    def _run(self) -> None:
        while True:
            job_id, fn = self._queue.get()
            job = self.get(job_id)
            if job is None:  # pragma: no cover - registry is never pruned today
                continue
            job.status, job.stage = "running", "starting"
            try:
                job.result = fn(job)
                job.status, job.stage = "done", "done"
            except Exception:
                # Keep the traceback: these failures are usually malformed uploads
                # (missing physchem column, sequence_id absent from the cluster TSV) and
                # the user needs the specific ValueError, not "something went wrong".
                job.status, job.stage = "failed", "failed"
                job.error = traceback.format_exc(limit=3)
            finally:
                self._queue.task_done()


REGISTRY = JobRegistry()
