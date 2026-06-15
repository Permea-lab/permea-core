"""Compatibility module for public validator package initialization."""

from .checks import check_artifacts
from .report import render_check_report

__all__ = ["check_artifacts", "render_check_report"]
