"""REPORT-03 — each §4.10 degradation path warns and still produces a valid
document (or a clean result), never raises:

  1. missing logo            -> warn + omit, document still builds
  2. missing/unresolvable font -> warn + fall back, document still builds
  3. no brand.yaml           -> Eyekyam default applies, document still builds
  4. single-format host      -> render the available format, warn on the other
  5. invalid block type      -> warn + skip the block, continue
"""

import builtins
import json

import pytest
import yaml

import generate_report
from theme import resolve_theme
from render_pdf import EyekyamPDF
from render_docx import EyekyamDOCX


# ── Path 1: missing logo ────────────────────────────────────────────────
def test_missing_logo_still_builds(tmp_path, capsys):
    """A brand pointing at a non-existent logo warns + omits, still builds."""
    brand = {
        "schema": "hse-brand/v1",
        "palette": {"primary": "#2AADA8"},
        "images": {"logo": "does-not-exist.png", "cover_image": None,
                   "watermark": {"path": None, "opacity": 0.08}},
    }
    bp = tmp_path / "brand.yaml"
    bp.write_text(yaml.safe_dump(brand), encoding="utf-8")
    theme = resolve_theme(str(bp))
    assert theme.images["logo"] is None  # warned + omitted

    out = tmp_path / "no-logo.pdf"
    pdf = EyekyamPDF(str(out), title="No logo", theme=theme)
    pdf.add_cover(title="No logo")
    pdf.add_text("body")
    pdf.build()
    assert out.exists() and out.stat().st_size > 1000


# ── Path 2: missing / unresolvable font ─────────────────────────────────
def test_unresolvable_font_falls_back(tmp_path, capsys):
    """An unknown font family warns + falls back through the bundled order;
    the renderer still builds."""
    brand = {
        "schema": "hse-brand/v1",
        "fonts": {"heading": "No Such Font", "body": "No Such Font",
                  "mono": "No Such Font"},
    }
    bp = tmp_path / "brand.yaml"
    bp.write_text(yaml.safe_dump(brand), encoding="utf-8")
    theme = resolve_theme(str(bp))
    err = capsys.readouterr().err
    assert "font family" in err.lower() or "falling back" in err.lower()

    out = tmp_path / "fallback.docx"
    docx = EyekyamDOCX(str(out), title="Fallback", theme=theme)
    docx.add_heading("H", level=1)
    docx.add_text("body")
    docx.build()
    assert out.exists() and out.stat().st_size > 1000


# ── Path 3: no brand.yaml ───────────────────────────────────────────────
def test_no_brand_uses_default(tmp_path, example_model_path, capsys):
    """With no --brand and no card, the Eyekyam default applies and both
    formats build (branding ON is the safe default)."""
    out = tmp_path / "out"
    written = generate_report.generate(
        str(example_model_path), brand=None, out=str(out), formats="docx,pdf"
    )
    assert len(written) == 2


def test_missing_brand_path_warns_and_defaults(tmp_path, example_model_path, capsys):
    """A --brand path that does not exist warns + falls back to the default."""
    out = tmp_path / "out"
    written = generate_report.generate(
        str(example_model_path), brand=str(tmp_path / "nope.yaml"),
        out=str(out), formats="pdf"
    )
    assert len(written) == 1
    assert "not found" in capsys.readouterr().err.lower()


# ── Path 4: single-format host ──────────────────────────────────────────
def test_single_format_host(tmp_path, example_model_path, monkeypatch, capsys):
    """Simulate a host missing python-docx: docx is skipped + warned, pdf still
    renders. _build_one imports render_docx lazily, so block that import."""
    real_import = builtins.__import__

    def fake_import(name, *args, **kwargs):
        if name == "render_docx":
            raise ImportError("simulated: python-docx not installed")
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", fake_import)

    out = tmp_path / "out"
    written = generate_report.generate(
        str(example_model_path), out=str(out), formats="docx,pdf"
    )
    # Only the pdf was produced; the run did not abort.
    assert len(written) == 1
    assert written[0].endswith(".pdf")
    assert "docx" in capsys.readouterr().err.lower()


# ── Path 5: invalid block type ──────────────────────────────────────────
def test_invalid_block_type_skipped(tmp_path, capsys):
    """An unknown block type warns + is skipped; surrounding blocks still
    render and the document builds."""
    theme = resolve_theme()
    report = {
        "schema": "hse-report-model/v1",
        "meta": {"title": "Bad block"},
        "sections": [
            {"type": "heading", "text": "Before", "level": 1},
            {"type": "totally_unknown", "text": "x"},
            {"type": "paragraph", "text": "After"},
        ],
    }
    out = tmp_path / "badblock.pdf"
    pdf = EyekyamPDF(str(out), title="Bad block", theme=theme)
    tree = []
    generate_report.render(report, theme, pdf, debug_tree=tree)
    pdf.build()
    assert out.exists() and out.stat().st_size > 1000
    assert [t for t, _ in tree] == ["heading", "paragraph"]
    assert "unknown block type" in capsys.readouterr().err.lower()


def test_invalid_block_does_not_raise_in_generate(tmp_path):
    """A report with an unknown block (but otherwise valid against a relaxed
    flow) does not crash generate()'s render walk. Validation is bypassed here
    by writing the model and calling render() directly with a real renderer."""
    theme = resolve_theme()
    report = {
        "schema": "hse-report-model/v1",
        "meta": {"title": "T"},
        "sections": [{"type": "mystery"}],
    }
    docx = EyekyamDOCX(str(tmp_path / "x.docx"), title="T", theme=theme)
    generate_report.render(report, theme, docx)  # must not raise
    docx.build()
