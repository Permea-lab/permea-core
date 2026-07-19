"""Pure text rendering of a Diagnosis for the terminal. No new numbers, formatting only."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from permea_core.diagnose import Diagnosis


def render_text(diag: "Diagnosis", dataset_name: str) -> str:
    """Human-readable report. Every value comes from the Diagnosis; this only lays it out."""
    c = diag.context
    ident = "(none declared)" if c.identity_definition is None else _fmt_identity(c.identity_definition)
    sha = c.data_sha256 or "(none)"
    sha_disp = f"{sha[:8]}…{sha[-8:]}" if len(sha) == 64 else sha

    lines = [
        f"PermeaBench diagnose — {dataset_name}",
        f"dataset:  n={c.n}  (pos={c.pos}  neg={c.neg})   clusters={c.n_clusters}   "
        f"representation={c.representation}",
        f"headline: condition={c.headline_condition}     resample_unit={c.resample_unit}",
        f"identity_definition: {ident}",
        f"data_sha256: {sha_disp}",
        "",
    ]

    s = diag.summary
    if s.total == 0:
        lines.append("No warnings fired.")
        return "\n".join(lines)

    lines.append(
        f"{s.total} warning{'s' if s.total != 1 else ''} fired   "
        f"(critical={s.critical}  warn={s.warn}  info={s.info})"
    )
    lines.append("")
    # Pad the severity tag to a fixed width so the CODE/title columns align.
    tag_w = max(len(str(f.severity)) for f in diag.fired) + 2  # +2 for the brackets
    indent = " " * (tag_w + 1)  # align evidence line under the title
    for f in diag.fired:
        tag = f"[{str(f.severity).upper()}]".ljust(tag_w)
        lines.append(f"{tag} {f.code}  {f.title}")
        lines.append(f"{indent}{f.evidence_str}")
    return "\n".join(lines)


def _fmt_identity(defn: dict[str, str]) -> str:
    return "{" + ", ".join(f"{k}={v}" for k, v in defn.items()) + "}"
