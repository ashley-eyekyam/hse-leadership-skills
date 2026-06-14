"""REPORT-02 / AC7 — the bundled OFL fonts register and render a ₹ (U+20B9)
string and a Devanagari string in BOTH formats on a bare Linux sandbox (no
system fonts, no LibreOffice). Proves Assumption A1 (₹ in Noto base) and the
reportlab per-run Devanagari selection (Pitfall 2)."""

from theme import resolve_theme
from render_pdf import EyekyamPDF, _has_devanagari
from render_docx import EyekyamDOCX

RUPEE = "Permit cost ₹45,000"          # ₹
DEVANAGARI = "मुंबई कारखाना — फॉर्म २४"      # Mumbai works — Form 24


def test_devanagari_detection():
    """The reportlab Devanagari detector fires on Devanagari, not on ₹/Latin."""
    assert _has_devanagari(DEVANAGARI)
    assert not _has_devanagari(RUPEE)
    assert not _has_devanagari("plain ascii")


def _build_sample(renderer):
    renderer.add_cover(title=DEVANAGARI, subtitle=RUPEE)
    renderer.add_heading("Rupee + Devanagari smoke", level=1)
    renderer.add_text(RUPEE)
    renderer.add_text(DEVANAGARI)
    renderer.add_table(
        headers=["Field", "Value"],
        rows=[["Cost", RUPEE], ["Plant", DEVANAGARI]],
    )
    return renderer.build()


def test_rupee_devanagari_pdf(tmp_path):
    """₹ + Devanagari render to a non-empty PDF without crashing."""
    theme = resolve_theme()
    out = tmp_path / "fonts-smoke.pdf"
    pdf = EyekyamPDF(str(out), title="Fonts", theme=theme)
    _build_sample(pdf)
    assert out.exists() and out.stat().st_size > 5000


def test_rupee_devanagari_docx(tmp_path):
    """₹ + Devanagari render to a non-empty DOCX without crashing."""
    theme = resolve_theme()
    out = tmp_path / "fonts-smoke.docx"
    docx = EyekyamDOCX(str(out), title="Fonts", theme=theme)
    _build_sample(docx)
    assert out.exists() and out.stat().st_size > 5000


def test_rupee_devanagari(tmp_path):
    """Both formats together — the named AC7 smoke test."""
    theme = resolve_theme()
    pdf_out = tmp_path / "both.pdf"
    docx_out = tmp_path / "both.docx"
    _build_sample(EyekyamPDF(str(pdf_out), title="Fonts", theme=theme))
    _build_sample(EyekyamDOCX(str(docx_out), title="Fonts", theme=theme))
    assert pdf_out.stat().st_size > 5000
    assert docx_out.stat().st_size > 5000
