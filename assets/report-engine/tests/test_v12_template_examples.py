"""SUB-06 — render-smoke + 12-block allowlist over the 10 v1.2 sector exemplars.

The Phase-11 v1.2 milestone ships 10 representative `report.json` exemplars (one
per new bundle) under `assets/report-engine/templates/examples/`. They are the
clone-and-customize scaffolds the Ph12–16 bundle skills copy into their own
`assets/` (D-06). This test proves each exemplar:

  1. is JSON-parseable with `schema == "hse-report-model/v1"`, a top-level
     `sections[]` array, and `meta.house_template == "house-standard"` (Q2);
  2. composes ONLY the 12 existing block types — no new block type, no schema
     edit (D-04);
  3. validates against report_model_schema.json; and
  4. renders cleanly through the EXISTING engine (generate_report.generate) to a
     temp dir with no renderer error, producing output file(s).

D-04 guard: the test asserts every section `type` is in the 12-block allowlist
and never touches `report_model_schema.json`, the renderers, or the DISPATCH.

Degradation fallback (§4.10 / VALIDATION.md): if BOTH renderers (reportlab AND
python-docx) are unavailable on the host, the render assertion is relaxed to
schema-validate-only — the 12-block + schema constraints are still enforced.
"""

from __future__ import annotations

import glob
import json
import sys
from pathlib import Path

import pytest

ENGINE_DIR = Path(__file__).resolve().parents[1]
if str(ENGINE_DIR) not in sys.path:
    sys.path.insert(0, str(ENGINE_DIR))

import generate_report  # noqa: E402

EXAMPLES_DIR = ENGINE_DIR / "templates" / "examples"
BRAND = ENGINE_DIR / "brand.yaml"

# The 12 block types from report_model_schema.json (D-04 — no new type).
ALLOWED_BLOCK_TYPES = {
    "heading", "paragraph", "bullets", "table", "metrics", "callout",
    "findings", "hoc_table", "recommendations", "divider", "page_break", "spacer",
}

# The 10 new v1.2 bundles (one exemplar each).
EXPECTED_BUNDLES = {
    "hse-operations", "hse-leadership", "hse-construction", "hse-manufacturing",
    "hse-utilities-power", "hse-healthcare", "hse-logistics-transport",
    "hse-marine-offshore", "hse-rail", "hse-renewables",
}

EXEMPLARS = sorted(glob.glob(str(EXAMPLES_DIR / "hse-*.report.json")))


def _renderers_available() -> bool:
    """True if at least one backend can render (else schema-validate-only)."""
    try:
        import reportlab  # noqa: F401
        return True
    except Exception:
        pass
    try:
        import docx  # noqa: F401
        return True
    except Exception:
        return False


def test_exactly_ten_exemplars():
    """Exactly 10 exemplars exist, one per new bundle, named hse-<bundle>.report.json."""
    assert len(EXEMPLARS) == 10, f"expected 10 exemplars, found {len(EXEMPLARS)}: {EXEMPLARS}"
    stems = {Path(p).name[: -len(".report.json")] for p in EXEMPLARS}
    assert stems == EXPECTED_BUNDLES, f"bundle set mismatch: {stems ^ EXPECTED_BUNDLES}"


@pytest.mark.parametrize("exemplar", EXEMPLARS, ids=lambda p: Path(p).name)
def test_exemplar_shape_and_block_allowlist(exemplar):
    """Each exemplar uses sections[] + schema v1 + house-standard + only the 12 blocks."""
    data = json.loads(Path(exemplar).read_text(encoding="utf-8"))
    assert data["schema"] == "hse-report-model/v1", exemplar
    assert isinstance(data.get("sections"), list) and data["sections"], (
        "missing or empty sections[]", exemplar
    )
    assert "blocks" not in data, ("must use sections[], not blocks", exemplar)
    assert data["meta"]["house_template"] == "house-standard", exemplar
    for sec in data["sections"]:
        assert sec["type"] in ALLOWED_BLOCK_TYPES, (
            "block type outside the 12-block allowlist (D-04)", sec["type"], exemplar
        )


@pytest.mark.parametrize("exemplar", EXEMPLARS, ids=lambda p: Path(p).name)
def test_exemplar_schema_valid(exemplar):
    """Each exemplar validates against report_model_schema.json (no schema edit)."""
    schema = json.loads(
        (ENGINE_DIR / "report_model_schema.json").read_text(encoding="utf-8")
    )
    jsonschema = pytest.importorskip("jsonschema")
    jsonschema.validate(json.loads(Path(exemplar).read_text(encoding="utf-8")), schema)


@pytest.mark.parametrize("exemplar", EXEMPLARS, ids=lambda p: Path(p).name)
def test_exemplar_renders_through_existing_engine(exemplar, tmp_path):
    """Each exemplar renders through the EXISTING generate_report.generate with no
    renderer error, producing output. Falls back to schema-validate-only when no
    backend is installed (§4.10 / VALIDATION.md)."""
    out = tmp_path / "out"
    if not _renderers_available():
        # Documented fallback: still prove schema + block constraints hold.
        generate_report.validate_model(
            json.loads(Path(exemplar).read_text(encoding="utf-8"))
        )
        pytest.skip("no report renderer (reportlab/python-docx) on host — schema-validated only")
    written = generate_report.generate(
        exemplar, brand=str(BRAND), out=str(out), formats="docx,pdf"
    )
    assert written, f"no output produced for {exemplar}"
    for path in written:
        assert Path(path).exists(), f"missing rendered output {path}"
        assert Path(path).stat().st_size > 0, f"empty rendered output {path}"


def test_utilities_power_carries_arc_flash_boundary_table():
    """SUB-02 distinct output: hse-utilities-power has the arc-flash metrics + table."""
    data = json.loads((EXAMPLES_DIR / "hse-utilities-power.report.json").read_text("utf-8"))
    types = [s["type"] for s in data["sections"]]
    assert "metrics" in types and "table" in types
    blob = json.dumps(data)
    assert "Incident energy" in blob and "Arc-flash boundary" in blob
    assert "Arcing current (kA)" in blob  # the to_report_blocks() table shape


def test_marine_offshore_safety_case_map_is_table_callout_bullets():
    """D-04 canary: the safety-case argument map composes as table + callout + bullets
    (no graph/diagram block, no schema gap)."""
    data = json.loads((EXAMPLES_DIR / "hse-marine-offshore.report.json").read_text("utf-8"))
    types = {s["type"] for s in data["sections"]}
    assert {"table", "callout", "bullets"} <= types
    headers = [s.get("headers") for s in data["sections"] if s["type"] == "table"]
    # The argument-map table carries the goal-structuring columns.
    assert any(
        h and "Claim" in h and "Evidence reference" in h for h in headers
    ), "safety-case argument-map table missing the claim/evidence columns"
    # ALARP assertion present in a callout.
    callouts = " ".join(s.get("text", "") for s in data["sections"] if s["type"] == "callout")
    assert "ALARP" in callouts
