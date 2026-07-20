"""Identity clustering backends (decoupled from evaluation).

A backend maps sequences to identity clusters; the evaluation engine consumes those
clusters as groups. See :data:`PERMEA_IDENTITY_DEFINITION` for the identity convention.
"""

from .identity import (
    PERMEA_IDENTITY_DEFINITION,
    ClusterAssignment,
    build_clusters,
    cluster_align,
    cluster_mmseqs,
    cluster_proxy,
    mmseqs_version,
    read_clusters_tsv,
)

__all__ = [
    "PERMEA_IDENTITY_DEFINITION",
    "ClusterAssignment",
    "build_clusters",
    "cluster_align",
    "cluster_mmseqs",
    "cluster_proxy",
    "mmseqs_version",
    "read_clusters_tsv",
]
