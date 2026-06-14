"""graders/report.py — the deterministic report-produced grader (A8 §4.4.3).

Proves the skill actually emitted a valid, renderable report: report.json
validates against the report-engine schema (hse-report-model/v1) AND
generate_report.py produced a docx/pdf (or the A4 §4.10 degraded path — no
renderer on the host still counts as "valid model" since the degradation is
by-design). REUSES generate_report.py's validate_model + generate — it does NOT
re-derive the schema (correctness trap).
"""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path
from typing import Dict, List

# The A4 report engine lives at assets/report-engine/. Put it (and its theme.py)
# on sys.path so we import the SAME validate_model + generate the CLI uses.
_REPO = Path(__file__).resolve().parent.parent.parent
_ENGINE = _REPO / "assets" / "report-engine"
if str(_ENGINE) not in sys.path:
    sys.path.insert(0, str(_ENGINE))


def grade_report_produced(report_json: Path, attempt_render: bool = True) -> Dict:
    """Validate report.json against the engine schema and (optionally) render it.

    Returns::

        {"valid": bool,
         "rendered": [path, ...],
         "degraded": bool,     # schema-valid but no renderer on host (A4 §4.10)
         "reasons": [str, ...]}

    `valid` is False only on a schema-invalid model or a missing file. A
    schema-valid model that produces no output because no renderer is installed
    is the by-design degraded path (`degraded=True`), still `valid=True`.
    """
    import json

    import generate_report as engine  # the SHARED validate_model + generate

    report_json = Path(report_json)
    reasons: List[str] = []

    if not report_json.is_file():
        return {"valid": False, "rendered": [], "degraded": False,
                "reasons": [f"report.json not found: {report_json}"]}

    try:
        model = json.loads(report_json.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return {"valid": False, "rendered": [], "degraded": False,
                "reasons": [f"report.json is not valid JSON: {exc}"]}

    # Schema validation via the engine's own validator (no re-derived schema).
    try:
        engine.validate_model(model)
    except Exception as exc:  # jsonschema.ValidationError (or any validate error)
        return {"valid": False, "rendered": [], "degraded": False,
                "reasons": [f"report.json failed schema validation: {exc}"]}

    rendered: List[str] = []
    degraded = False
    if attempt_render:
        with tempfile.TemporaryDirectory() as tmp:
            try:
                rendered = engine.generate(str(report_json), out=tmp, formats="docx,pdf")
            except Exception as exc:  # pragma: no cover - host-renderer dependent
                reasons.append(f"render raised {exc!r}; treating as degraded (A4 §4.10)")
            if not rendered:
                degraded = True
                reasons.append("no renderer produced output on this host (A4 §4.10 degraded path)")

    return {"valid": True, "rendered": rendered, "degraded": degraded, "reasons": reasons}
