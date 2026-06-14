"""generate_report.py — the A4 report-engine CLI + shared dispatch driver.

One structured `report.json` (schema `hse-report-model/v1`) -> a branded .docx
AND .pdf in the fixed house layout (A4 §4.2). The CLI:

    python generate_report.py --model report.json --brand brand.yaml \
        --out ./out --formats docx,pdf

Flow (§4.2):
  1. validate the model against report_model_schema.json (jsonschema); exit
     nonzero on an invalid model or an unwritable --out.
  2. read --card (A9 company-card) ONLY for report_branding_default + the footer
     org line; resolve the theme via theme.resolve_theme(--brand) seeding blanks
     from the Eyekyam default.
  3. for each requested format: instantiate the renderer with the theme,
     auto-stamp cover + classification + TOC from house-standard.yaml + meta,
     walk sections[] via the SHARED DISPATCH table, auto-stamp the
     limitations/de-id notice, build().

The SAME `DISPATCH` dict drives BOTH renderers, so docx and pdf stay matched
(the AC3 visual-parity guarantee). `callout` maps to `add_callout` (NOT
add_info_box — EyekyamDOCX has no add_info_box; keeping both renderers matched).
`findings`/`hoc_table`/`recommendations` are thin adapters that flatten their
structured rows into `add_table(... risk_col=...)` calls.

Graceful degradation (§4.10): a missing asset warns + omits, never aborts; a
single-format host (missing reportlab OR python-docx) renders the available
format and warns; an unknown block type warns + is skipped. Only a
schema-invalid model or an unwritable --out exits nonzero.

`--debug-tree` is the AC3 parity substrate: it captures the dispatched
(type, block) sequence WITHOUT rendering, so a test can assert both renderers
walk an identical tree (RESEARCH: docx<->pdf snapshot parity, RESOLVED).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import warnings
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

try:
    import jsonschema
    _HAVE_JSONSCHEMA = True
except Exception:  # pragma: no cover - jsonschema is a declared dep
    _HAVE_JSONSCHEMA = False

import yaml

from theme import resolve_theme

_HERE = Path(__file__).resolve().parent
_SCHEMA_PATH = _HERE / "report_model_schema.json"
_HOUSE_TEMPLATE = _HERE / "templates" / "house-standard.yaml"
_DEFAULT_BRAND = _HERE / "brand.yaml"
_DEFAULT_CARD = _HERE / "branding" / "company-card.yaml"

# Default limitations/de-id footer (auto-stamped when meta carries no override).
_DEFAULT_LIMITATIONS = (
    "This report is decision-support only and must be reviewed by a competent "
    "person before use. It is not legal advice. Personal identifiers have been "
    "de-identified; any re-identification key is held separately and is not part "
    "of this document."
)


def _warn(msg: str) -> None:
    """Emit a degradation warning to stderr (never raises)."""
    print(f"[generate_report] WARNING: {msg}", file=sys.stderr)


# ──────────────────────────────────────────────────────────────────────────
# Structured-row adapters: flatten findings / hoc_table / recommendations into
# (headers, rows) for add_table. Each returns (headers, rows) so the dispatch
# can call add_table(*adapter(block["rows"]), risk_col=...).
# ──────────────────────────────────────────────────────────────────────────
def _findings_to_table(rows: List[Dict[str, Any]]) -> Tuple[List[str], List[List[str]]]:
    headers = ["Finding", "Risk", "Description", "Evidence"]
    out = [
        [
            r.get("title", ""),
            r.get("risk_level", ""),
            r.get("description", ""),
            r.get("evidence", ""),
        ]
        for r in rows
    ]
    return headers, out


def _hoc_to_table(rows: List[Dict[str, Any]]) -> Tuple[List[str], List[List[str]]]:
    headers = ["Control", "Tier", "Owner"]
    out = [
        [r.get("control", ""), r.get("tier", ""), r.get("owner", "")]
        for r in rows
    ]
    return headers, out


def _recs_to_table(rows: List[Dict[str, Any]]) -> Tuple[List[str], List[List[str]]]:
    headers = ["Action", "Priority", "Owner", "Due"]
    out = [
        [
            r.get("action", ""),
            r.get("priority", ""),
            r.get("owner", ""),
            r.get("due", ""),
        ]
        for r in rows
    ]
    return headers, out


# ──────────────────────────────────────────────────────────────────────────
# The SHARED type -> method dispatch table. Consumed by BOTH renderers via
# render(). Adding a block type touches this table once; both backends inherit
# it (the matched-API parity guarantee). `callout` -> add_callout (both
# renderers expose it; EyekyamDOCX has NO add_info_box).
# ──────────────────────────────────────────────────────────────────────────
DISPATCH = {
    "heading":         lambda r, b: r.add_heading(b["text"], b.get("level", 1)),
    "paragraph":       lambda r, b: r.add_text(b.get("text", "")),
    "bullets":         lambda r, b: r.add_bullets(b.get("items", [])),
    "table":           lambda r, b: r.add_table(
        b["headers"], b["rows"],
        risk_col=b.get("risk_column"),
        caption=b.get("caption"),
    ),
    "metrics":         lambda r, b: r.add_metrics_row(b.get("metrics", [])),
    "callout":         lambda r, b: r.add_callout(b.get("text", "")),
    "findings":        lambda r, b: r.add_table(
        *_findings_to_table(b.get("rows", [])), risk_col=1
    ),
    "hoc_table":       lambda r, b: r.add_table(*_hoc_to_table(b.get("rows", []))),
    "recommendations": lambda r, b: r.add_table(*_recs_to_table(b.get("rows", []))),
    "divider":         lambda r, b: r.add_divider(),
    "page_break":      lambda r, b: r.add_page_break(),
    "spacer":          lambda r, b: r.add_spacer(b.get("height_cm", 0.5)),
}


def render(report: Dict[str, Any], theme, renderer, *,
           debug_tree: Optional[list] = None) -> None:
    """Walk report["sections"] dispatching block `type` -> renderer method via
    the shared DISPATCH table.

    Args:
        report: the validated report.json dict.
        theme: the resolved Theme (already injected into `renderer`; passed for
            symmetry / future per-block theme reads).
        renderer: an EyekyamPDF or EyekyamDOCX instance.
        debug_tree: if a list is supplied, append (type, block) for each
            dispatched block INSTEAD of relying on render output — the AC3
            parity substrate. Unknown blocks are still warned + skipped and are
            NOT appended (they were not dispatched).
    """
    for block in report.get("sections", []):
        btype = block.get("type")
        fn = DISPATCH.get(btype)
        if fn is None:
            _warn(f"unknown block type {btype!r}; skipping")   # §4.10 degrade
            continue
        if debug_tree is not None:
            debug_tree.append((btype, block))
        fn(renderer, block)


# ──────────────────────────────────────────────────────────────────────────
# House framing — auto-stamp cover / classification / TOC (before body) and the
# limitations/de-id notice (after body). The skill never authors these as blocks.
# ──────────────────────────────────────────────────────────────────────────
def _load_house_template() -> Dict[str, Any]:
    try:
        return yaml.safe_load(_HOUSE_TEMPLATE.read_text(encoding="utf-8")) or {}
    except Exception as exc:  # pragma: no cover
        _warn(f"could not load house template ({exc}); using built-in order")
        return {"sections": []}


def _auto_section_keys(house: Dict[str, Any]) -> set:
    return {
        s["key"]
        for s in house.get("sections", [])
        if s.get("source") == "auto"
    }


def _stamp_front_matter(renderer, meta: Dict[str, Any], house: Dict[str, Any],
                        layout: Dict[str, Any]) -> None:
    """Auto-stamp cover -> classification -> TOC from meta + house template."""
    auto = _auto_section_keys(house)

    # Cover (layout.cover may switch it off).
    if "cover" in auto and layout.get("cover", True):
        renderer.add_cover(
            title=meta.get("title", "Report"),
            subtitle=meta.get("subtitle", ""),
            date=meta.get("date", ""),
        )

    # Classification notice from meta.classification.
    if "classification" in auto and meta.get("classification"):
        renderer.add_callout(f"Classification: {meta['classification']}")

    # Table of contents from the skill-authored house sections (the body
    # sections, not the auto-framed ones).
    if "toc" in auto and layout.get("toc", True):
        toc_titles = [
            s["title"]
            for s in house.get("sections", [])
            if s.get("source") == "skill"
        ]
        if toc_titles:
            renderer.add_toc_placeholder(toc_titles)


def _stamp_back_matter(renderer, meta: Dict[str, Any], house: Dict[str, Any]) -> None:
    """Auto-stamp the limitations/de-id notice as the final section."""
    auto = _auto_section_keys(house)
    if "limitations-deid-notice" not in auto:
        return
    renderer.add_heading("Limitations & De-identification Notice", level=2)
    renderer.add_text(_DEFAULT_LIMITATIONS)
    deid = meta.get("deid_notice")
    if deid:
        renderer.add_text(deid)


# ──────────────────────────────────────────────────────────────────────────
# Validation + IO
# ──────────────────────────────────────────────────────────────────────────
def _load_schema() -> Optional[dict]:
    try:
        return json.loads(_SCHEMA_PATH.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover
        _warn(f"could not load report_model_schema.json ({exc})")
        return None


def validate_model(report: Dict[str, Any]) -> None:
    """Validate report against report_model_schema.json. Raises
    jsonschema.ValidationError on an invalid model (the caller exits nonzero)."""
    if not _HAVE_JSONSCHEMA:
        _warn("jsonschema unavailable; skipping model validation")
        return
    schema = _load_schema()
    if schema is None:
        return
    jsonschema.validate(report, schema)


def _slugify(title: str) -> str:
    slug = re.sub(r"[^\w\s-]", "", title.lower()).strip()
    slug = re.sub(r"[\s_-]+", "-", slug)
    return slug or "report"


def _read_card_flag(card_path: Optional[str]) -> Tuple[bool, Optional[Dict[str, Any]]]:
    """Read ONLY report_branding_default (+ return the card for the footer org
    line). Missing/unreadable card -> (True, None): default branding ON (the
    Eyekyam default applies), which is the safe, branded path."""
    path = Path(card_path) if card_path else _DEFAULT_CARD
    if not path.exists():
        return True, None
    try:
        card = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        flag = card.get("report_branding_default", True)
        return bool(flag), card
    except Exception as exc:
        _warn(f"could not read company card {path} ({exc}); defaulting branding ON")
        return True, None


# ──────────────────────────────────────────────────────────────────────────
# Per-format render
# ──────────────────────────────────────────────────────────────────────────
def _build_one(fmt: str, report: Dict[str, Any], theme, out_path: Path) -> Optional[str]:
    """Instantiate the renderer for `fmt`, stamp the house frame, walk the body,
    and build. Returns the output path, or None if the renderer is unavailable
    on this host (single-format degradation, §4.10)."""
    meta = report.get("meta", {})
    house = _load_house_template()
    layout = theme.layout or {}
    title = meta.get("title", "Report")

    if fmt == "pdf":
        try:
            from render_pdf import EyekyamPDF
        except Exception as exc:
            _warn(f"reportlab/render_pdf unavailable ({exc}); skipping pdf")
            return None
        renderer = EyekyamPDF(str(out_path), title=title,
                              author=meta.get("author", "Eyekyam"), theme=theme)
    elif fmt == "docx":
        try:
            from render_docx import EyekyamDOCX
        except Exception as exc:
            _warn(f"python-docx/render_docx unavailable ({exc}); skipping docx")
            return None
        renderer = EyekyamDOCX(str(out_path), title=title,
                               author=meta.get("author", "Eyekyam"), theme=theme)
    else:
        _warn(f"unknown format {fmt!r}; skipping")
        return None

    _stamp_front_matter(renderer, meta, house, layout)
    render(report, theme, renderer)
    _stamp_back_matter(renderer, meta, house)
    renderer.build()
    return str(out_path)


def generate(model_path: str, *, brand: Optional[str] = None,
             out: str = "./out", formats: str = "docx,pdf",
             card: Optional[str] = None) -> List[str]:
    """Run the full pipeline. Returns the list of written file paths.

    Raises:
        jsonschema.ValidationError: on a schema-invalid model.
        OSError: on an unwritable --out directory.
    """
    report = json.loads(Path(model_path).read_text(encoding="utf-8"))
    validate_model(report)   # exit nonzero on invalid (caller converts)

    # --out must be writable (exit nonzero on failure — do not partially render).
    out_dir = Path(out)
    out_dir.mkdir(parents=True, exist_ok=True)

    branding_default, _card = _read_card_flag(card)

    # Resolve the theme: explicit --brand, else the Eyekyam default when the
    # card's report_branding_default is true (§2 bridge), else a neutral default.
    if brand:
        theme = resolve_theme(brand)
    elif branding_default:
        theme = resolve_theme(str(_DEFAULT_BRAND))
    else:
        theme = resolve_theme()  # neutral built-in (still the bundled default)

    meta = report.get("meta", {})
    slug = _slugify(meta.get("title", "report"))

    fmt_list = [f.strip().lower() for f in formats.split(",") if f.strip()]
    written: List[str] = []
    for fmt in fmt_list:
        ext = "pdf" if fmt == "pdf" else fmt
        out_path = out_dir / f"{slug}.{ext}"
        result = _build_one(fmt, report, theme, out_path)
        if result:
            written.append(result)

    if not written:
        _warn("no formats were produced (no renderer available on this host)")
    return written


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Render an HSE report.json into branded docx + pdf.")
    parser.add_argument("--model", required=True,
                        help="path to report.json (validated against the schema)")
    parser.add_argument("--brand", default=None,
                        help="path to brand.yaml (omitted -> Eyekyam default)")
    parser.add_argument("--out", default="./out", help="output directory")
    parser.add_argument("--formats", default="docx,pdf",
                        help="comma list of formats (docx,pdf)")
    parser.add_argument("--card", default=None,
                        help="path to the A9 company-card.yaml (flag + footer)")
    parser.add_argument("--debug-tree", action="store_true",
                        help="print the dispatched (type) sequence and exit "
                             "without rendering (AC3 parity introspection)")
    args = parser.parse_args(argv)

    # --debug-tree: introspect the dispatch sequence without rendering.
    if args.debug_tree:
        report = json.loads(Path(args.model).read_text(encoding="utf-8"))
        try:
            validate_model(report)
        except Exception as exc:
            print(f"invalid model: {exc}", file=sys.stderr)
            return 2
        tree: list = []
        render(report, None, _NullRenderer(), debug_tree=tree)
        print(json.dumps([t for t, _ in tree]))
        return 0

    try:
        written = generate(
            args.model, brand=args.brand, out=args.out,
            formats=args.formats, card=args.card,
        )
    except FileNotFoundError as exc:
        print(f"model not found: {exc}", file=sys.stderr)
        return 2
    except OSError as exc:
        print(f"unwritable output: {exc}", file=sys.stderr)
        return 2
    except Exception as exc:
        # jsonschema.ValidationError and any other model error -> nonzero.
        print(f"invalid model: {exc}", file=sys.stderr)
        return 2

    for path in written:
        print(path)
    return 0 if written else 1


class _NullRenderer:
    """A no-op renderer used by --debug-tree so render() can walk the dispatch
    table without instantiating a real backend. Every DISPATCH method is a
    no-op; the (type, block) capture happens in render() before the call."""

    def __getattr__(self, _name):
        def _noop(*_a, **_kw):
            return None
        return _noop


if __name__ == "__main__":
    raise SystemExit(main())
