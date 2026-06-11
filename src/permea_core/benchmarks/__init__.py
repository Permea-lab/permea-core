"""Benchmark definitions and registry surfaces for Permea Core."""

from .cards import (
    DEFAULT_BENCHMARK_CARD_DIR,
    BenchmarkCardBatchResult,
    BenchmarkCardGenerationResult,
    generate_benchmark_card_file,
    generate_benchmark_cards_from_registry,
    render_benchmark_card,
)
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
    "DEFAULT_BENCHMARK_CARD_DIR",
    "EXPECTED_OUTPUT_ARTIFACTS",
    "BenchmarkCardBatchResult",
    "REQUIRED_REGISTRY_FIELDS",
    "BenchmarkCardGenerationResult",
    "BenchmarkDefinition",
    "BenchmarkRegistry",
    "RegistryValidationError",
    "RegistryValidationResult",
    "generate_benchmark_card_file",
    "generate_benchmark_cards_from_registry",
    "render_benchmark_card",
    "validate_registry_file",
]
