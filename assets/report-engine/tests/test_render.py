"""REPORT-02 — generate_report.py renders one report.json into BOTH a non-empty
.docx and .pdf in the house layout, with no system-font / LibreOffice
dependency (bare Linux sandbox)."""

from pathlib import Path

import generate_report


def test_both_formats(tmp_path, example_model_path):
    """The example fixture emits both out/<slug>.docx and out/<slug>.pdf,
    each above a ~15KB size floor."""
    out = tmp_path / "out"
    written = generate_report.generate(
        str(example_model_path), out=str(out), formats="docx,pdf"
    )
    assert len(written) == 2

    slug = "confined-space-entry-risk-assessment"
    docx_path = out / f"{slug}.docx"
    pdf_path = out / f"{slug}.pdf"
    assert docx_path.exists(), f"missing {docx_path}"
    assert pdf_path.exists(), f"missing {pdf_path}"
    assert docx_path.stat().st_size > 15000, "docx below size floor"
    assert pdf_path.stat().st_size > 15000, "pdf below size floor"


def test_slug_from_title(tmp_path, example_model_path):
    """Output filenames are slugified from meta.title."""
    out = tmp_path / "out"
    written = generate_report.generate(
        str(example_model_path), out=str(out), formats="pdf"
    )
    assert len(written) == 1
    assert Path(written[0]).name == "confined-space-entry-risk-assessment.pdf"


def test_single_format_narrowing(tmp_path, example_model_path):
    """--formats narrows to a single format."""
    out = tmp_path / "out"
    written = generate_report.generate(
        str(example_model_path), out=str(out), formats="docx"
    )
    assert len(written) == 1
    assert written[0].endswith(".docx")


def test_main_exit_zero(tmp_path, example_model_path):
    """main() exits 0 on a valid model and writes both formats."""
    out = tmp_path / "out"
    rc = generate_report.main([
        "--model", str(example_model_path),
        "--out", str(out),
        "--formats", "docx,pdf",
    ])
    assert rc == 0
    assert list(out.glob("*.pdf"))
    assert list(out.glob("*.docx"))


def test_main_invalid_model_exits_nonzero(tmp_path):
    """A schema-invalid model exits nonzero (does not render)."""
    bad = tmp_path / "bad.json"
    bad.write_text('{"schema": "hse-report-model/v1", "meta": {}, "sections": []}',
                   encoding="utf-8")  # meta.title missing -> invalid
    out = tmp_path / "out"
    rc = generate_report.main([
        "--model", str(bad), "--out", str(out), "--formats", "pdf",
    ])
    assert rc != 0
