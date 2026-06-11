"""Benchmark definitions and registry surfaces for Permea Core."""

from .cards import (
    DEFAULT_BENCHMARK_CARD_DIR,
    BenchmarkCardBatchResult,
    BenchmarkCardGenerationResult,
    generate_benchmark_card_file,
    generate_benchmark_cards_from_registry,
    render_benchmark_card,
)
from .output_package import (
    DEFAULT_OUTPUT_PACKAGE_DIR,
    DEFAULT_OUTPUT_PACKAGE_INPUT,
    OUTPUT_PACKAGE_FILES,
    OutputPackageGenerationResult,
    generate_evidence_cards,
    generate_manifest,
    generate_metrics,
    generate_output_package,
    generate_ranking,
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
    "DEFAULT_OUTPUT_PACKAGE_DIR",
    "DEFAULT_OUTPUT_PACKAGE_INPUT",
    "EXPECTED_OUTPUT_ARTIFACTS",
    "OUTPUT_PACKAGE_FILES",
    "BenchmarkCardBatchResult",
    "REQUIRED_REGISTRY_FIELDS",
    "BenchmarkCardGenerationResult",
    "BenchmarkDefinition",
    "BenchmarkRegistry",
    "OutputPackageGenerationResult",
    "RegistryValidationError",
    "RegistryValidationResult",
    "generate_benchmark_card_file",
    "generate_benchmark_cards_from_registry",
    "generate_evidence_cards",
    "generate_manifest",
    "generate_metrics",
    "generate_output_package",
    "generate_ranking",
    "render_benchmark_card",
    "validate_registry_file",
]
