"""REPORT-02/03 — AC3 dispatch-tree snapshot parity.

Parity = identical dispatched (type, block) sequence across both renderers +
identical theme tokens (NOT pixel identity — D-04 forbids the soffice path). The
shared DISPATCH table is what guarantees this; --debug-tree mechanizes the
assertion with zero PDF-reading dependency (RESEARCH: snapshot-parity RESOLVED).
"""

import generate_report
from theme import resolve_theme
from render_pdf import EyekyamPDF
from render_docx import EyekyamDOCX


def _dispatch_tree(renderer, report, theme):
    tree = []
    generate_report.render(report, theme, renderer, debug_tree=tree)
    return [t for t, _ in tree]


def test_dispatch_tree_equal(tmp_path, example_model):
    """Both renderers walk an IDENTICAL dispatched (type) sequence."""
    theme = resolve_theme()
    pdf = EyekyamPDF(str(tmp_path / "p.pdf"), title="T", theme=theme)
    docx = EyekyamDOCX(str(tmp_path / "p.docx"), title="T", theme=theme)

    pdf_tree = _dispatch_tree(pdf, example_model, theme)
    docx_tree = _dispatch_tree(docx, example_model, theme)

    assert pdf_tree == docx_tree
    # The tree mirrors the fixture's section types in order.
    expected = [s["type"] for s in example_model["sections"]]
    assert pdf_tree == expected


def test_full_block_tree_equal(tmp_path, example_model):
    """The full (type, block) tree — including payload — is identical across
    renderers (same data dispatched in the same order)."""
    theme = resolve_theme()
    pdf = EyekyamPDF(str(tmp_path / "p.pdf"), title="T", theme=theme)
    docx = EyekyamDOCX(str(tmp_path / "p.docx"), title="T", theme=theme)

    pdf_tree, docx_tree = [], []
    generate_report.render(example_model, theme, pdf, debug_tree=pdf_tree)
    generate_report.render(example_model, theme, docx, debug_tree=docx_tree)
    assert pdf_tree == docx_tree


def test_theme_tokens_identical():
    """Both renderers consume the same Theme; the risk-level->hex map is the
    same in both code paths (the parity precondition)."""
    theme = resolve_theme()
    # render_pdf builds reportlab HexColors; render_docx builds hex-without-'#'.
    # Both derive from the SAME theme.palette['risk'] — assert that shared source.
    risk = theme.palette["risk"]
    pdf = EyekyamPDF("/dev/null", title="T", theme=theme)
    docx = EyekyamDOCX("/dev/null", title="T", theme=theme)
    # PDF brand stores reportlab colours; compare their hex value to the source.
    assert pdf.BRAND.HIGH_RISK.hexval()[2:] == risk["high"].lstrip("#").lower()
    # DOCX brand stores uppercase hex without '#'.
    assert docx.BRAND.HIGH_RISK == risk["high"].lstrip("#").upper()
    assert docx.BRAND.CRITICAL_RISK == risk["critical"].lstrip("#").upper()


def test_unknown_block_not_dispatched(tmp_path):
    """An unknown block type is skipped (warned) and NOT appended to the tree —
    both renderers stay matched."""
    theme = resolve_theme()
    report = {
        "schema": "hse-report-model/v1",
        "meta": {"title": "T"},
        "sections": [
            {"type": "heading", "text": "H", "level": 1},
            {"type": "bogus_block", "text": "x"},
            {"type": "paragraph", "text": "p"},
        ],
    }
    pdf = EyekyamPDF(str(tmp_path / "p.pdf"), title="T", theme=theme)
    tree = []
    generate_report.render(report, theme, pdf, debug_tree=tree)
    assert [t for t, _ in tree] == ["heading", "paragraph"]


def test_cli_debug_tree(capsys, example_model_path):
    """--debug-tree prints the dispatched type sequence and exits 0 without
    rendering."""
    import json
    rc = generate_report.main(["--model", str(example_model_path), "--debug-tree"])
    assert rc == 0
    out = capsys.readouterr().out.strip()
    types = json.loads(out)
    assert types[0] == "heading"
    assert "findings" in types
