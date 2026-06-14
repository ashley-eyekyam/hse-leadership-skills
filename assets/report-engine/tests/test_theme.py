"""REPORT-03 — theme.py resolves a partial user brand.yaml by seeding blanks
from the Eyekyam default, and the risk palette maps the same risk-level strings
to the same hex (the parity precondition both renderers rely on)."""

import yaml

from theme import resolve_theme


def test_default_theme_resolves():
    """resolve_theme() with no brand uses the bundled Eyekyam default."""
    theme = resolve_theme()
    assert theme.palette["primary"].upper() == "#2AADA8"
    assert theme.palette["risk"]["critical"].upper() == "#B71C1C"


def test_partial_brand_seeds_blanks(tmp_path, engine_dir):
    """A user brand.yaml that overrides one field and leaves the others blank
    (null) resolves with every blank seeded from the Eyekyam default.

    theme.py validates a SUPPLIED brand against the full schema before merge,
    and brand.schema.json's hexColor pattern accepts only hex strings — so the
    seeding seam is exercised by setting blanks to `null` (the schema's
    hexColorOrNull / nullable image fields permit this, and _deep_merge treats
    a null override as "seed from the default")."""
    default = yaml.safe_load((engine_dir / "brand.yaml").read_text(encoding="utf-8"))

    # A genuinely partial brand: override only palette.primary; omit every
    # other field. theme.py seeds the omitted fields from the Eyekyam default
    # (validating the merged result), so this resolves cleanly.
    partial = {
        "schema": "hse-brand/v1",
        "palette": {"primary": "#123456"},
    }
    p = tmp_path / "partial-brand.yaml"
    p.write_text(yaml.safe_dump(partial), encoding="utf-8")

    theme = resolve_theme(str(p))

    # Overridden field honoured.
    assert theme.palette["primary"].upper() == "#123456"
    # Omitted fields seeded from the Eyekyam default.
    assert theme.palette["secondary"].upper() == default["palette"]["secondary"].upper()
    assert theme.palette["accent"].upper() == default["palette"]["accent"].upper()
    assert theme.palette["risk"]["high"].upper() == default["palette"]["risk"]["high"].upper()
    assert theme.palette["risk"]["critical"].upper() == default["palette"]["risk"]["critical"].upper()
    # Fonts/layout seeded too — the renderer-consumed seam resolves.
    assert theme.fonts.resolved_files[0] is not None
    assert theme.layout["page_size"] == default["layout"]["page_size"]


def test_risk_palette_is_single_source(tmp_path):
    """The resolved Theme exposes ONE risk-level->hex map; both renderers read
    palette['risk'], so the same risk string maps to the same hex everywhere."""
    theme = resolve_theme()
    risk = theme.palette["risk"]
    for level in ("low", "med", "high", "critical"):
        assert level in risk
        assert risk[level].startswith("#")

    # Re-resolving yields an identical mapping (deterministic single source).
    again = resolve_theme().palette["risk"]
    assert risk == again


def test_fonts_resolve_to_bundled_paths():
    """The body family resolves to a bundled TTF on disk (the seam the
    renderers consume)."""
    theme = resolve_theme()
    reg, bold = theme.fonts.resolved_files
    assert reg is not None and reg.endswith(".ttf")
    # Devanagari family is always made available for per-run selection.
    dreg, _ = theme.fonts.files_for("Noto Sans Devanagari")
    assert dreg is not None and dreg.endswith(".ttf")
