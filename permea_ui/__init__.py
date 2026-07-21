"""Drylab web UI -- a thin layer over the diagnose engine and the narration task.

Dependency direction, matching the boundary ``tests/test_explain_boundary.py`` already
enforces one level down: permea_ui imports permea_core and permea_explain; neither of
them ever imports permea_ui. The UI is a viewer, not a participant.
"""

from __future__ import annotations

__all__ = ["__version__"]

__version__ = "0.1.0"
