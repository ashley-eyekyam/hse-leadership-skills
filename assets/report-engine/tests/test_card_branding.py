"""CR-01 regression — the A9 company-card identity must reach the rendered
report on the DEFAULT (no --card, no --brand) path.

Two compounding defects let the org line ("Eyekyam") silently degrade to
"HSE Report Engine" in every code path: the default-card path pointed at a
non-existent dir, and generate() never threaded the card's company block into
resolve_theme(org=...). These tests pin both halves of the bridge:

  1. _DEFAULT_CARD actually exists on disk (the path-resolution half).
  2. On the default no-arg path the resolved theme carries the card's org name,
     AND the rendered .docx footer XML contains it (the threading half — the
     coverage hole that let this ship green).
"""

import zipfile

import generate_report
from theme import resolve_theme


def test_default_card_path_exists():
    """CR-01a: the bundled default company-card must resolve to a real file
    (the old _HERE/'branding' path did not exist)."""
    assert generate_report._DEFAULT_CARD.exists(), (
        f"default card not found at {generate_report._DEFAULT_CARD}"
    )


def test_default_card_read_carries_org_name():
    """CR-01b: reading the default card yields the Eyekyam company block."""
    flag, card = generate_report._read_card_flag(None, is_default=True)
    assert flag is True
    assert card is not None
    assert card.get("company", {}).get("name") == "Eyekyam"


def test_default_path_theme_org_is_eyekyam(monkeypatch, tmp_path, example_model_path):
    """CR-01c: on the default no-arg generate() path, resolve_theme is called
    with an org overlay carrying the card name, so theme.org.name == 'Eyekyam'."""
    captured = {}
    real_resolve = generate_report.resolve_theme

    def spy(brand_path=None, *, org=None):
        captured["org"] = org
        return real_resolve(brand_path, org=org)

    monkeypatch.setattr(generate_report, "resolve_theme", spy)

    out = tmp_path / "out"
    written = generate_report.generate(
        str(example_model_path), out=str(out), formats="docx"
    )
    assert len(written) == 1
    assert captured["org"] is not None
    assert captured["org"]["name"] == "Eyekyam"
    # The tagline (or blurb) becomes the footer line.
    assert captured["org"]["footer"]


def test_default_path_docx_footer_contains_eyekyam(tmp_path, example_model_path):
    """CR-01d: the rendered .docx footer XML carries 'Eyekyam' on the default
    path — the end-to-end assertion the prior suite was missing."""
    out = tmp_path / "out"
    written = generate_report.generate(
        str(example_model_path), out=str(out), formats="docx"
    )
    docx_path = [p for p in written if p.endswith(".docx")][0]
    with zipfile.ZipFile(docx_path) as zf:
        footer_xml = "".join(
            zf.read(n).decode("utf-8")
            for n in zf.namelist()
            if n.startswith("word/footer")
        )
    assert "Eyekyam" in footer_xml
    assert "HSE Report Engine" not in footer_xml


def test_org_overlay_reaches_theme_directly():
    """Sanity: resolve_theme(org=...) sets theme.org.name (the mechanism the
    fix relies on)."""
    theme = resolve_theme(org={"name": "Eyekyam", "footer": "tagline"})
    assert theme.org["name"] == "Eyekyam"
    assert theme.org["footer"] == "tagline"
