"""permea-eval/1.0 warning-code registry.

The formal catalog of PermeaBench warning codes -- the "scoring rules" reviewers cite
(e.g. PERMEA-W101). This module is PURE DATA + LOOKUP: it defines what codes exist and
what they mean. It does NOT implement the rule engine that fires them from an evaluation
result -- that is the diagnose layer, which imports this registry (never the reverse).

Dependency boundary: ML-free (no numpy/scikit-learn) and zero imports from ``eval/``.
``fire_condition`` strings name ``EvalRun`` fields as prose only; they are documentation of
the trigger, not code. This keeps the catalog a stable contract that diagnose reads.

CLOSED-SCHEMA SEAM: ``WarningCode`` is a frozen dataclass with only typed, enumerable
fields. A future permea-eval/1.0 warnings schema (additionalProperties: false) maps 1:1 onto
these fields. The schema is intentionally not built here.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class Family(StrEnum):
    """Warning-code family (the leading digit block)."""

    CONFIG = "W0xx"  # run-config self-indictment (how the run was set up)
    LEAKAGE = "W1xx"  # similarity-leakage findings (Paper 1 P1)
    REPRESENTATION = "W2xx"  # representation-inflation findings (P2)
    NEGATIVE_CONFOUND = "W3xx"  # assumed-negative confound findings (P3)
    CROSS_DATASET_PROVENANCE = "W4xx"  # cross-dataset overlap + archival/metadata integrity
    STAT_VALIDITY = "W5xx"  # statistical-validity findings


class Kind(StrEnum):
    """Whether a code indicts the run's own configuration or reports a data finding."""

    DECLARATION = "declaration"  # self-indictment of the run/release's own contract
    FINDING = "finding"  # a finding about the benchmark/data


class Status(StrEnum):
    """Whether firing logic is expected to exist now (ACTIVE) or is catalogued only."""

    ACTIVE = "active"  # diagnose may fire this from an EvalRun today/next task
    RESERVED = "reserved"  # defined + catalogued; no firing logic yet


class Severity(StrEnum):
    """Static v0 severity per code (sophisticated policy comes later)."""

    INFO = "info"
    WARN = "warn"
    CRITICAL = "critical"


@dataclass(frozen=True, slots=True)
class WarningCode:
    """One PermeaBench warning code -- what a reviewer cites."""

    code: str  # e.g. "PERMEA-W101"
    family: Family
    title: str
    kind: Kind
    status: Status
    severity: Severity
    fire_condition: str  # one-line trigger spec (prose; names EvalRun fields)
    description: str  # one paragraph: what fires it and what it means
    pillar: str | None = None  # "P1" | "P2" | "P3" | None


# --------------------------------------------------------------------------------------
# The catalog. ACTIVE codes are fireable from an EvalRun by the diagnose layer; RESERVED
# codes are defined but need inputs beyond EvalRun (or a field not yet emitted).
# --------------------------------------------------------------------------------------
WARNINGS: tuple[WarningCode, ...] = (
    # ---- W0xx: run-config self-indictment (DECLARATION) ----
    WarningCode(
        code="PERMEA-W001",
        family=Family.CONFIG,
        title="identity_definition undeclared",
        kind=Kind.DECLARATION,
        status=Status.ACTIVE,
        severity=Severity.CRITICAL,
        fire_condition="EvalRun.identity_definition is None (or a built-in default was used, not an explicit declaration)",
        description=(
            "The identity definition governing the clustering was not explicitly declared. "
            "Under permea-eval/1.0 it is required with no default: the entire identity-control "
            "result depends on how identity is defined (alignment, denominator, gap treatment), "
            "so an undeclared or silently-defaulted definition makes the headline number "
            "uninterpretable and non-comparable across runs."
        ),
    ),
    WarningCode(
        code="PERMEA-W002",
        family=Family.CONFIG,
        title="headline condition is not B",
        kind=Kind.DECLARATION,
        status=Status.ACTIVE,
        severity=Severity.CRITICAL,
        fire_condition='EvalRun.headline_condition != "B"',
        description=(
            "The reported headline is not the identity-controlled condition B. permea-eval/1.0 "
            "fixes the headline to the identity-controlled evaluation; reporting the uncontrolled "
            "condition A (or anything else) as the headline re-admits exactly the similarity "
            "leakage the protocol exists to remove."
        ),
    ),
    WarningCode(
        code="PERMEA-W003",
        family=Family.CONFIG,
        title="row-level resampling",
        kind=Kind.DECLARATION,
        status=Status.ACTIVE,
        severity=Severity.WARN,
        fire_condition='EvalRun.resample_unit == "row"',
        description=(
            "The confidence interval was bootstrapped over rows rather than clusters. Under "
            "identity control the independent unit is the cluster, not the row: rows within a "
            "cluster are near-duplicates carrying no independent information, so row-level "
            "resampling understates the interval and overstates significance."
        ),
    ),
    # ---- W1xx: similarity-leakage finding (P1) ----
    WarningCode(
        code="PERMEA-W101",
        family=Family.LEAKAGE,
        title="material similarity leakage",
        kind=Kind.FINDING,
        status=Status.ACTIVE,
        severity=Severity.CRITICAL,
        fire_condition="headline model/metric: delta_point < 0 and ci_excludes_zero (identity control significantly reduces discrimination)",
        description=(
            "Identity-controlled evaluation (B) scores significantly below the uncontrolled "
            "evaluation (A), with the paired-bootstrap CI on the delta excluding zero. This is "
            "the core Paper 1 P1 finding: a material fraction of the uncontrolled performance was "
            "similarity memorisation of near-duplicate train/test peptides, not generalisation. "
            "The magnitude that counts as 'material' is a diagnose-layer policy, not fixed here."
        ),
        pillar="P1",
    ),
    # ---- W5xx: statistical-validity findings (CI-based) ----
    WarningCode(
        code="PERMEA-W501",
        family=Family.STAT_VALIDITY,
        title="inconclusive delta (CI includes zero)",
        kind=Kind.FINDING,
        status=Status.ACTIVE,
        severity=Severity.WARN,
        fire_condition="a reported delta has ci_excludes_zero == False (CI straddles zero)",
        description=(
            "The paired-bootstrap 95% CI on the A-vs-B delta includes zero, so the two conditions "
            "are not statistically distinguishable at that level. The point estimate should not be "
            "reported as a real effect; the result is inconclusive rather than null."
        ),
    ),
    WarningCode(
        code="PERMEA-W502",
        family=Family.STAT_VALIDITY,
        title="underpowered (too few clusters)",
        kind=Kind.FINDING,
        status=Status.ACTIVE,
        severity=Severity.WARN,
        fire_condition="EvalRun.n_clusters < threshold (cluster-count cutoff is a diagnose-layer policy)",
        description=(
            "The number of identity clusters is small enough that cluster-level bootstrap "
            "intervals are unreliable: the independent-unit count, not the row count, sets the "
            "effective sample size. The specific cutoff is tunable diagnose-layer policy; the "
            "registry only names the condition."
        ),
    ),
    # ---- RESERVED: catalogued, no firing logic (need inputs beyond EvalRun) ----
    WarningCode(
        code="PERMEA-W005",
        family=Family.CONFIG,
        title="per-condition threshold re-tuning",
        kind=Kind.DECLARATION,
        status=Status.RESERVED,
        severity=Severity.WARN,
        fire_condition="thresholds re-tuned per condition instead of a fixed shared operating point (needs a threshold_policy field not yet on EvalRun)",
        description=(
            "Re-tuning the decision threshold separately for each condition makes the A-vs-B delta "
            "measure threshold movement rather than generalisation loss. RESERVED: the current "
            "orchestrator always uses a fixed shared threshold and emits no threshold_policy field, "
            "so this cannot yet be detected; promote to ACTIVE when that field is added."
        ),
    ),
    WarningCode(
        code="PERMEA-W201",
        family=Family.REPRESENTATION,
        title="representation inflation",
        kind=Kind.FINDING,
        status=Status.RESERVED,
        severity=Severity.WARN,
        fire_condition="a higher-capacity representation's advantage collapses under identity control (needs multi-representation input)",
        description=(
            "The apparent advantage of a richer representation (e.g. a large embedding) over simple "
            "features largely disappears once similarity leakage is controlled. Paper 1 P2. "
            "RESERVED: requires comparing multiple representations, which a single EvalRun does not carry."
        ),
        pillar="P2",
    ),
    WarningCode(
        code="PERMEA-W301",
        family=Family.NEGATIVE_CONFOUND,
        title="assumed-negative confound",
        kind=Kind.FINDING,
        status=Status.RESERVED,
        severity=Severity.WARN,
        fire_condition="negatives are assumed rather than verified non-penetrators (needs negative-provenance signal)",
        description=(
            "The negative class is assumed (e.g. random Swiss-Prot proteins) rather than "
            "experimentally verified non-penetrators, so measured discrimination may reflect a "
            "positive-vs-random-protein contrast rather than penetration. Paper 1 P3. RESERVED: "
            "requires negative-set provenance, not present in an EvalRun."
        ),
        pillar="P3",
    ),
    WarningCode(
        code="PERMEA-W401",
        family=Family.CROSS_DATASET_PROVENANCE,
        title="cross-dataset positive overlap",
        kind=Kind.FINDING,
        status=Status.RESERVED,
        severity=Severity.WARN,
        fire_condition="benchmark positives substantially overlap another archive's positives (needs cross-dataset input)",
        description=(
            "The benchmark's positive set substantially overlaps an ostensibly independent archive "
            "(e.g. B3Pred positives vs Brainpeps), so 'independent' datasets are not independent and "
            "cross-dataset validation is circular. RESERVED: requires a second dataset, not an EvalRun."
        ),
    ),
    WarningCode(
        code="PERMEA-W403",
        family=Family.CROSS_DATASET_PROVENANCE,
        title="EnvironmentUnpinned",
        kind=Kind.DECLARATION,
        status=Status.RESERVED,
        severity=Severity.WARN,
        fire_condition="all artifact hashes match yet numbers move run-to-run because the schema does not pin python/sklearn/numpy/architecture versions (needs environment metadata)",
        description=(
            "Every artifact checksum matches, yet reported numbers move between runs because the "
            "reproducibility schema pins no execution environment (python / scikit-learn / numpy / "
            "CPU architecture / thread-parallelism). This is the same class of problem as the "
            "RandomForest(n_jobs=-1) ~1e-7 roc_auc drift: byte-identical inputs, non-identical "
            "outputs. RESERVED: firing needs environment metadata, not an EvalRun."
        ),
    ),
    WarningCode(
        code="PERMEA-W404",
        family=Family.CROSS_DATASET_PROVENANCE,
        title="ClusterArtifactUnarchived",
        kind=Kind.DECLARATION,
        status=Status.RESERVED,
        severity=Severity.CRITICAL,
        fire_condition="a reproduction-critical artifact (e.g. the cluster-assignment TSV) is gitignored / not deposited in the permanent archive (needs archival metadata)",
        description=(
            "A reproduction-critical artifact -- typically the cluster-assignment TSV that defines "
            "condition B -- is git-ignored or absent from the permanent archive, so reproduction "
            "depends on an un-guaranteed working directory and is one 'rm -rf' from being "
            "irreproducible. RESERVED: firing needs archival/deposit metadata, not an EvalRun."
        ),
    ),
    WarningCode(
        code="PERMEA-W405",
        family=Family.CROSS_DATASET_PROVENANCE,
        title="false or stale archival-source claim",
        kind=Kind.DECLARATION,
        status=Status.RESERVED,
        severity=Severity.CRITICAL,
        fire_condition="the reproduction path cites a data source that does not actually host the artifact (needs source/metadata cross-check)",
        description=(
            "The reproduction path or provenance documentation cites an archival source that does "
            "not actually host the artifact (e.g. a Zenodo record that contains no machine-readable "
            "data, or a 'staged / not yet public' claim left standing after publication). RESERVED: "
            "firing needs a source-vs-claim cross-check, not an EvalRun."
        ),
    ),
)


REGISTRY: dict[str, WarningCode] = {w.code: w for w in WARNINGS}


def get(code: str) -> WarningCode:
    """Look up a warning by its code (e.g. "PERMEA-W101"). Raises KeyError if unknown."""
    return REGISTRY[code]


def by_family(family: Family) -> tuple[WarningCode, ...]:
    """All warnings in a family, in catalog order."""
    return tuple(w for w in WARNINGS if w.family is family)


def active() -> tuple[WarningCode, ...]:
    """All ACTIVE warnings (those diagnose may fire from an EvalRun), in catalog order."""
    return tuple(w for w in WARNINGS if w.status is Status.ACTIVE)
