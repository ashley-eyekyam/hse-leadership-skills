"""
theme.py — the single point of visual truth for the HSE report engine.

`resolve_theme(brand_path)` loads a brand.yaml, validates it against
brand.schema.json, seeds every blank field from the bundled Eyekyam default
brand.yaml, resolves the font-family names to the bundled OFL TTF paths under
fonts/, and returns a `Theme` token object that BOTH renderers
(render_pdf.EyekyamPDF / render_docx.EyekyamDOCX) consume unchanged.

Because both renderers read the same Theme — including the risk-level -> hex
map (`palette["risk"]`) — the two backends stay visually consistent. That is
the decision-1 visual-parity guard from the A4 spec.

Degradation (A4 §4.10): a missing/unresolvable font warns and falls back to the
next bundled family, then to a renderer default; nothing here raises on a
missing asset. Only a schema-invalid brand.yaml is a hard error (V5 input
validation) — and even then resolve_theme can be called with the default.
"""

from __future__ import annotations

import json
import sys
import warnings
from pathlib import Path
from typing import Any, Dict, Optional

import yaml

try:
    import jsonschema
    _HAVE_JSONSCHEMA = True
except Exception:  # pragma: no cover - jsonschema is a declared dep
    _HAVE_JSONSCHEMA = False


_HERE = Path(__file__).resolve().parent
_DEFAULT_BRAND = _HERE / "brand.yaml"
_SCHEMA_PATH = _HERE / "brand.schema.json"
_FONTS_DIR = _HERE / "fonts"

# Map a brand.yaml font-family name -> the bundled TTF basenames (regular, bold).
# These are the OFL Noto families bundled in fonts/. The Devanagari family is
# kept separate so reportlab can select it per-run (reportlab has no automatic
# glyph fallback — see render_pdf.py).
_BUNDLED_FONTS: Dict[str, Dict[str, str]] = {
    "Noto Sans": {
        "regular": "NotoSans-Regular.ttf",
        "bold": "NotoSans-Bold.ttf",
    },
    "Noto Sans Devanagari": {
        "regular": "NotoSansDevanagari-Regular.ttf",
        "bold": "NotoSansDevanagari-Bold.ttf",
    },
    "Noto Sans Mono": {
        "regular": "NotoSansMono-Regular.ttf",
        "bold": "NotoSansMono-Bold.ttf",
    },
}

# Fallback order when a requested family is unknown or its files are missing.
_FONT_FALLBACK_ORDER = ["Noto Sans", "Noto Sans Mono", "Noto Sans Devanagari"]


def _warn(msg: str) -> None:
    """Emit a degradation warning to stderr (never raises)."""
    print(f"[theme] WARNING: {msg}", file=sys.stderr)


def _deep_merge(base: Any, override: Any) -> Any:
    """
    Return a copy of `base` with `override` merged on top. A None / missing
    value in `override` is treated as "blank" and seeded from `base`. Used to
    seed a partial user brand.yaml from the Eyekyam default.
    """
    if isinstance(base, dict) and isinstance(override, dict):
        out = dict(base)
        for key, val in override.items():
            if key in base:
                out[key] = _deep_merge(base[key], val)
            else:
                out[key] = val
        return out
    # Scalars / lists: a blank (None) override falls back to the base default.
    if override is None:
        return base
    return override


class FontSet:
    """Resolved font tokens. `.resolved_files` is the (regular, bold) tuple for
    the body family, the form the port-source renderers expect at the font
    seam. `.family_files` exposes every resolved family for per-run selection
    (Devanagari)."""

    def __init__(
        self,
        heading: str,
        body: str,
        mono: str,
        family_files: Dict[str, Dict[str, Optional[str]]],
    ) -> None:
        self.heading = heading
        self.body = body
        self.mono = mono
        # {family_name: {"regular": path|None, "bold": path|None}}
        self.family_files = family_files

    @property
    def resolved_files(self):
        """(regular_path, bold_path) for the body family — the seam the
        ported reportlab font registration consumes. May be (None, None) if
        no bundled file resolved (renderer then degrades to its built-in)."""
        files = self.family_files.get(self.body, {})
        return (files.get("regular"), files.get("bold"))

    def files_for(self, family: str):
        """(regular, bold) paths for any resolved family, or (None, None)."""
        files = self.family_files.get(family, {})
        return (files.get("regular"), files.get("bold"))


class Theme:
    """Resolved visual tokens consumed unchanged by both renderers.

    Attributes:
        palette: dict {primary, accent, secondary, text, surface,
                       risk:{low,med,high,critical}} — hex strings.
        fonts:   FontSet (family names + resolved TTF paths).
        images:  dict {logo, cover_image, watermark:{path, opacity}} — paths
                 resolved absolute (or None if the asset is missing).
        layout:  dict {page_size, cover, toc, page_numbers}.
        org:     dict {name, tagline, footer, classification} — neutral
                 defaults; identity strings are overlaid downstream from the
                 A9 company-card (kept OUT of brand.yaml by the A4<->A9 split).
    """

    def __init__(self, palette, fonts, images, layout, org) -> None:
        self.palette = palette
        self.fonts = fonts
        self.images = images
        self.layout = layout
        self.org = org


def _load_schema() -> Optional[dict]:
    try:
        return json.loads(_SCHEMA_PATH.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover
        _warn(f"could not load brand.schema.json ({exc}); skipping validation")
        return None


def _resolve_fonts(font_cfg: Dict[str, str]) -> FontSet:
    """Resolve each configured family to bundled TTF paths, applying the
    §4.10 fallback chain. Never raises."""
    family_files: Dict[str, Dict[str, Optional[str]]] = {}

    def resolve_family(name: str) -> str:
        """Return a family name that has at least a regular file on disk,
        falling back through the bundled order. Records resolved paths in
        family_files for every family it touches."""
        candidates = [name] + [f for f in _FONT_FALLBACK_ORDER if f != name]
        for cand in candidates:
            spec = _BUNDLED_FONTS.get(cand)
            if not spec:
                continue
            reg = _FONTS_DIR / spec["regular"]
            bold = _FONTS_DIR / spec["bold"]
            reg_path = str(reg) if reg.exists() else None
            bold_path = str(bold) if bold.exists() else (reg_path)
            family_files[cand] = {"regular": reg_path, "bold": bold_path}
            if reg_path is not None:
                if cand != name:
                    _warn(
                        f"font family {name!r} unavailable; "
                        f"falling back to {cand!r}"
                    )
                return cand
        _warn(
            f"no bundled font resolved for {name!r}; "
            f"renderer will use its built-in default"
        )
        return name

    heading = resolve_family(font_cfg.get("heading", "Noto Sans"))
    body = resolve_family(font_cfg.get("body", "Noto Sans"))
    mono = resolve_family(font_cfg.get("mono", "Noto Sans Mono"))

    # Always make the Devanagari family available for per-run selection,
    # even if no configured family named it.
    if "Noto Sans Devanagari" not in family_files:
        resolve_family("Noto Sans Devanagari")

    return FontSet(heading=heading, body=body, mono=mono, family_files=family_files)


def _resolve_images(images_cfg: Dict[str, Any], brand_dir: Path) -> Dict[str, Any]:
    """Resolve image paths relative to the brand.yaml dir; missing assets
    become None with a warning (warn + omit, never abort)."""

    def resolve_path(rel: Optional[str], label: str) -> Optional[str]:
        if not rel:
            return None
        p = (brand_dir / rel) if not Path(rel).is_absolute() else Path(rel)
        if p.exists():
            return str(p)
        _warn(f"image {label} not found at {p}; omitting")
        return None

    wm_cfg = images_cfg.get("watermark") or {}
    return {
        "logo": resolve_path(images_cfg.get("logo"), "logo"),
        "cover_image": resolve_path(images_cfg.get("cover_image"), "cover_image"),
        "watermark": {
            "path": resolve_path(wm_cfg.get("path"), "watermark"),
            "opacity": wm_cfg.get("opacity", 0.08),
        },
    }


# Neutral org defaults. Identity strings (real company name / tagline / cta)
# are overlaid downstream from the A9 company-card; brand.yaml carries none.
_DEFAULT_ORG = {
    "name": "",
    "tagline": "",
    "footer": "",
    "classification": "Confidential",
}


def resolve_theme(
    brand_path: Optional[str] = None,
    *,
    org: Optional[Dict[str, str]] = None,
) -> Theme:
    """
    Load + validate a brand.yaml, seed blanks from the Eyekyam default, and
    return a resolved Theme.

    Args:
        brand_path: path to a user brand.yaml. If None or missing, the bundled
            Eyekyam default is used (REPORT-04).
        org: optional organisation identity overlay (from the A9 company-card).
            Merged over the neutral org defaults — brand.yaml never carries it.

    Raises:
        jsonschema.ValidationError: only if a SUPPLIED brand.yaml is malformed
            (e.g. a non-hex palette colour). The default is always valid.
    """
    default_cfg = yaml.safe_load(_DEFAULT_BRAND.read_text(encoding="utf-8")) or {}

    user_cfg: Dict[str, Any] = {}
    brand_dir = _DEFAULT_BRAND.parent
    if brand_path:
        bp = Path(brand_path)
        if bp.exists():
            user_cfg = yaml.safe_load(bp.read_text(encoding="utf-8")) or {}
            brand_dir = bp.resolve().parent
        else:
            _warn(f"brand file {brand_path} not found; using Eyekyam default")

    merged = _deep_merge(default_cfg, user_cfg)

    # Validate a SUPPLIED brand.yaml (V5 input validation). The default is
    # trusted. Validation runs on the MERGED config so a PARTIAL user brand
    # (e.g. just an overridden `palette.primary`, every other field blank) is
    # seeded from the Eyekyam default first, then validated as a whole — a
    # malformed value the user DID supply (e.g. a non-hex palette colour)
    # survives the merge and still fails here.
    if user_cfg and _HAVE_JSONSCHEMA:
        schema = _load_schema()
        if schema is not None:
            jsonschema.validate(merged, schema)

    palette = merged["palette"]
    fonts = _resolve_fonts(merged.get("fonts", {}))
    images = _resolve_images(merged.get("images", {}), brand_dir)
    layout = merged.get("layout", {})

    resolved_org = dict(_DEFAULT_ORG)
    if org:
        resolved_org.update({k: v for k, v in org.items() if v is not None})

    return Theme(
        palette=palette,
        fonts=fonts,
        images=images,
        layout=layout,
        org=resolved_org,
    )
