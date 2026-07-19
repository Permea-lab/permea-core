"""The honest-evaluation engine.

Ported from permea-bbb-audit/harness/honest_eval.py (read-only source, DOI
10.5281/zenodo.21134112). The frozen harness was already representation-agnostic and
cluster-agnostic; this port preserves its numerics exactly and replaces the CLI with
function signatures.

NUMERICAL CONTRACT: this engine must reproduce Paper 1's published numbers exactly. The
engine that produced the paper and the engine in Permea Core are the same engine. Every
constant below (400 trees, random_state=42, the 19-point threshold grid, k=5) is
load-bearing -- do not "clean up" any of them.

Condition A = uncontrolled (StratifiedKFold).
Condition B = identity-controlled (StratifiedGroupKFold on identity clusters).
The DELTA is the finding: it estimates how much of the reported performance was
similarity memorisation rather than generalisation.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Sequence

import numpy as np
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    average_precision_score,
    balanced_accuracy_score,
    f1_score,
    matthews_corrcoef,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import StratifiedGroupKFold, StratifiedKFold
from sklearn.preprocessing import StandardScaler

RANK_METRICS = ("roc_auc", "pr_auc")
THRESHOLD_METRICS = ("mcc", "f1", "balanced_acc", "precision", "recall")
ALL_METRICS = RANK_METRICS + THRESHOLD_METRICS


@dataclass(frozen=True)
class ModelSpec:
    """A model under evaluation. `scale` mirrors the frozen harness: only logreg scales."""

    name: str
    factory: Callable[[], object]
    scale: bool


def default_models() -> list[ModelSpec]:
    """The Paper 1 model set. Constants are load-bearing (see module docstring)."""
    return [
        ModelSpec("dummy", lambda: DummyClassifier(strategy="most_frequent"), False),
        ModelSpec(
            "logreg",
            lambda: LogisticRegression(max_iter=2000, class_weight="balanced"),
            True,
        ),
        ModelSpec(
            "rf",
            lambda: RandomForestClassifier(
                n_estimators=400,
                class_weight="balanced",
                random_state=42,
                n_jobs=-1,
            ),
            False,
        ),
    ]


@dataclass
class ConditionResult:
    """Per-condition out-of-fold predictions, tuned thresholds, and per-seed metrics."""

    oofs: list[np.ndarray] = field(default_factory=list)
    thresholds: list[float] = field(default_factory=list)
    metrics: list[dict[str, float]] = field(default_factory=list)

    def mean_std(self, key: str) -> tuple[float, float]:
        v = np.array([m[key] for m in self.metrics], dtype=float)
        return float(np.nanmean(v)), float(np.nanstd(v))


def oof_predict(X, y, splitter, split_args, factory, scale) -> np.ndarray:
    """Out-of-fold positive-class scores."""
    oof = np.zeros(len(y))
    for tr, te in splitter.split(X, y, *split_args):
        Xtr, Xte = X[tr], X[te]
        if scale:
            sc = StandardScaler().fit(Xtr)
            Xtr, Xte = sc.transform(Xtr), sc.transform(Xte)
        clf = factory()
        clf.fit(Xtr, y[tr])
        oof[te] = (
            clf.predict_proba(Xte)[:, 1]
            if hasattr(clf, "predict_proba")
            else clf.predict(Xte)
        )
    return oof


def tune_threshold(y, oof) -> float:
    """F1-maximising threshold on a 19-point grid. Grid size is load-bearing."""
    if len(np.unique(oof)) <= 1:
        return 0.5
    ths = np.linspace(0.05, 0.95, 19)
    return float(max(ths, key=lambda t: f1_score(y, (oof >= t).astype(int), zero_division=0)))


def metrics_at(y, oof, thr) -> dict[str, float]:
    out: dict[str, float] = {}
    try:
        out["roc_auc"] = roc_auc_score(y, oof)
        out["pr_auc"] = average_precision_score(y, oof)
    except ValueError:
        out["roc_auc"] = float("nan")
        out["pr_auc"] = float("nan")
    pred = (oof >= thr).astype(int)
    out["mcc"] = matthews_corrcoef(y, pred) if len(np.unique(pred)) > 1 else 0.0
    out["f1"] = f1_score(y, pred, zero_division=0)
    out["balanced_acc"] = balanced_accuracy_score(y, pred)
    out["precision"] = precision_score(y, pred, zero_division=0)
    out["recall"] = recall_score(y, pred, zero_division=0)
    return out


def run_condition(
    X: np.ndarray,
    y: np.ndarray,
    groups: np.ndarray | None,
    model: ModelSpec,
    seeds: Sequence[int],
    k: int = 5,
) -> ConditionResult:
    """Run one condition across seeds.

    groups is None  -> Condition A (StratifiedKFold, uncontrolled)
    groups provided -> Condition B (StratifiedGroupKFold, identity-controlled)
    """
    res = ConditionResult()
    for s in seeds:
        if groups is None:
            sp = StratifiedKFold(k, shuffle=True, random_state=s)
            sa: tuple = ()
        else:
            sp = StratifiedGroupKFold(k, shuffle=True, random_state=s)
            sa = (groups,)
        oof = oof_predict(X, y, sp, sa, model.factory, model.scale)
        thr = tune_threshold(y, oof)
        res.oofs.append(oof)
        res.thresholds.append(thr)
        res.metrics.append(metrics_at(y, oof, thr))
    return res


def evaluate(
    X: np.ndarray,
    y: np.ndarray,
    groups: np.ndarray,
    models: list[ModelSpec] | None = None,
    seeds: Sequence[int] = (0, 1, 2, 3, 4),
    k: int = 5,
) -> dict[str, dict[str, ConditionResult]]:
    """Run Conditions A and B for every model.

    Returns {model_name: {"A": ConditionResult, "B": ConditionResult}}.
    """
    models = models or default_models()
    out: dict[str, dict[str, ConditionResult]] = {}
    for m in models:
        out[m.name] = {
            "A": run_condition(X, y, None, m, seeds, k),
            "B": run_condition(X, y, groups, m, seeds, k),
        }
    return out
