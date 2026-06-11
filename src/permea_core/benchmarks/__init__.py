"""Benchmark definitions and registry surfaces for Permea Core."""

from .registry import (
    ALLOWED_MATURITY_LEVELS,
    EXPECTED_OUTPUT_ARTIFACTS,
    REQUIRED_REGISTRY_FIELDS,
    BenchmarkDefinition,
    BenchmarkRegistry,
    RegistryValidationError,
    RegistryValidationResult,
    validate_registry_file,
)

__all__ = [
    "ALLOWED_MATURITY_LEVELS",
    "EXPECTED_OUTPUT_ARTIFACTS",
    "REQUIRED_REGISTRY_FIELDS",
    "BenchmarkDefinition",
    "BenchmarkRegistry",
    "RegistryValidationError",
    "RegistryValidationResult",
    "validate_registry_file",
]
