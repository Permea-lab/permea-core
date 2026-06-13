"""Public artifact indexing helpers for Permea Core."""

from permea_core.index.artifact_index import (
    DEFAULT_ARTIFACT_INDEX_PATH,
    collect_artifact_paths,
    generate_artifact_index,
    render_artifact_index,
)

__all__ = [
    "DEFAULT_ARTIFACT_INDEX_PATH",
    "collect_artifact_paths",
    "generate_artifact_index",
    "render_artifact_index",
]
