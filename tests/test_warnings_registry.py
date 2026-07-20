"""Tests for the permea-eval/1.0 warning-code registry (contracts/warnings.py)."""

from __future__ import annotations

import pytest

from permea_core.contracts.warnings import (
    REGISTRY,
    WARNINGS,
    Family,
    Kind,
    Severity,
    Status,
    WarningCode,
    active,
    by_family,
    get,
)

# leading digit after "W" -> expected family
DIGIT_TO_FAMILY = {
    "0": Family.CONFIG,
    "1": Family.LEAKAGE,
    "2": Family.REPRESENTATION,
    "3": Family.NEGATIVE_CONFOUND,
    "4": Family.CROSS_DATASET_PROVENANCE,
    "5": Family.STAT_VALIDITY,
}

EXPECTED_ACTIVE = {"PERMEA-W001", "PERMEA-W002", "PERMEA-W003",
                   "PERMEA-W101", "PERMEA-W501", "PERMEA-W502"}
EXPECTED_RESERVED = {"PERMEA-W005", "PERMEA-W201", "PERMEA-W301",
                     "PERMEA-W401", "PERMEA-W403", "PERMEA-W404", "PERMEA-W405"}


def test_ids_unique():
    codes = [w.code for w in WARNINGS]
    assert len(codes) == len(set(codes))


def test_id_number_matches_family():
    for w in WARNINGS:
        assert w.code.startswith("PERMEA-W"), w.code
        digit = w.code.split("-W")[1][0]
        assert digit in DIGIT_TO_FAMILY, w.code
        assert w.family is DIGIT_TO_FAMILY[digit], (w.code, w.family)


def test_registry_covers_catalog():
    assert len(REGISTRY) == len(WARNINGS)
    assert set(REGISTRY) == {w.code for w in WARNINGS}
    for w in WARNINGS:
        assert REGISTRY[w.code] is w


def test_get_and_unknown():
    assert get("PERMEA-W101").title == "material similarity leakage"
    with pytest.raises(KeyError):
        get("PERMEA-W999")


def test_all_fields_nonempty_and_typed():
    for w in WARNINGS:
        assert isinstance(w, WarningCode)
        assert w.code and w.title and w.fire_condition and w.description
        assert isinstance(w.family, Family)
        assert isinstance(w.kind, Kind)
        assert isinstance(w.status, Status)
        assert isinstance(w.severity, Severity)
        assert w.pillar is None or w.pillar in {"P1", "P2", "P3"}


def test_active_and_reserved_sets():
    assert {w.code for w in active()} == EXPECTED_ACTIVE
    assert all(w.status is Status.ACTIVE for w in active())
    reserved = {w.code for w in WARNINGS if w.status is Status.RESERVED}
    assert reserved == EXPECTED_RESERVED
    # catalog is exactly active + reserved, disjoint
    assert EXPECTED_ACTIVE.isdisjoint(EXPECTED_RESERVED)
    assert {w.code for w in WARNINGS} == EXPECTED_ACTIVE | EXPECTED_RESERVED


def test_by_family():
    w0 = by_family(Family.CONFIG)
    assert {w.code for w in w0} == {"PERMEA-W001", "PERMEA-W002", "PERMEA-W003", "PERMEA-W005"}
    # by_family preserves catalog order
    assert list(w0) == [w for w in WARNINGS if w.family is Family.CONFIG]
    assert by_family(Family.LEAKAGE) == (get("PERMEA-W101"),)


def test_pillar_mapping():
    assert get("PERMEA-W101").pillar == "P1"
    assert get("PERMEA-W201").pillar == "P2"
    assert get("PERMEA-W301").pillar == "P3"
    # config/stat-validity/provenance codes carry no pillar
    for code in ("PERMEA-W001", "PERMEA-W501", "PERMEA-W405"):
        assert get(code).pillar is None


def test_declaration_vs_finding_kinds():
    # W0xx are declarations; W1xx/W5xx active findings are findings
    for code in ("PERMEA-W001", "PERMEA-W002", "PERMEA-W003"):
        assert get(code).kind is Kind.DECLARATION
    for code in ("PERMEA-W101", "PERMEA-W501", "PERMEA-W502"):
        assert get(code).kind is Kind.FINDING
