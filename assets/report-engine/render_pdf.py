"""
render_pdf.py — ported EyekyamPDF renderer (ReportLab), theme-token driven.

PORT of ~/.claude/skills/eyekyam-pdf/scripts/create_pdf.py's EyekyamPDF class.
The public method set (add_cover, add_heading, add_text, add_bullets,
add_section, add_spacer, add_page_break, add_callout, add_divider, add_table,
add_metrics_row, add_image, add_diagram, add_numbered_steps, add_info_box,
add_comparison_columns, add_two_columns, add_code_block, add_contact_section,
add_toc_placeholder, build) is preserved byte-for-byte in behaviour — that
matched API IS the dispatch contract the shared generate_report.py driver
(Plan 02-06) keys off, and it must stay identical to render_docx.EyekyamDOCX.

Exactly three surgical edits were applied to the port source:

  Edit 1 (font seam): _register_unicode_fonts() no longer points at the
    non-portable Windows system-font directory. It registers the bundled OFL
    Noto Sans (body) from the
    resolved Theme, plus Noto Sans Devanagari as a SEPARATE reportlab family.
    reportlab does NO automatic glyph fallback, so cells/runs containing
    Devanagari codepoints are rendered in the Devanagari family
    (_select_font / whole-field selection — A4 RESEARCH Pitfall 2).

  Edit 2 (brand/company seam): the module-level `class BRAND` / `class COMPANY`
    constant reads are replaced by values pulled from an injected Theme on the
    EyekyamPDF constructor. Palette colours come from theme.palette.*, the org
    footer/name from theme.org.*, and the logo from theme.images['logo'].

  Edit 3 (logo-on-teal): the white-rounded-rectangle backing behind the cover
    logo is preserved (so the transparent PNG stays legible on the teal hero),
    with the Pillow import guarded — absent Pillow degrades to the raw logo
    rather than crashing (A4 §4.10).
"""

import os
import re
from pathlib import Path
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, Image, KeepTogether
)
from reportlab.graphics.shapes import Drawing, Rect, String
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from theme import resolve_theme


# ──────────────────────────────────────────────
#  DEVANAGARI DETECTION (reportlab has no glyph fallback)
# ──────────────────────────────────────────────
_DEVANAGARI_RE = re.compile(r"[ऀ-ॿ]")


def _has_devanagari(text) -> bool:
    return bool(_DEVANAGARI_RE.search(str(text)))


class EyekyamPDF:
    """
    High-level interface for creating Eyekyam-branded PDF documents, driven by
    a resolved Theme (theme.py). Ported from the eyekyam-pdf skill; the public
    method names/signatures are the matched-API dispatch contract.

    Args:
        output_path (str): Where to save the PDF.
        title (str): Document title shown in header and metadata.
        doc_type (str): One of 'report', 'proposal', 'brief', 'factsheet'.
        author (str): Author name for PDF metadata.
        subject (str): PDF subject metadata.
        theme: A resolved Theme (theme.resolve_theme(...)). Defaults to the
            bundled Eyekyam default brand if not supplied.
    """

    def __init__(self, output_path: str, title: str = "Report",
                 doc_type: str = "report", author: str = "Eyekyam",
                 subject: str = "Eyekyam Risk Analysis",
                 theme=None):
        self.output_path = output_path
        self.title = title
        self.doc_type = doc_type
        self.theme = theme if theme is not None else resolve_theme()
        self._story = []
        self._cover_data = None  # set when add_cover() is called

        # ── Edit 1: font registration from the bundled OFL Noto bundle ──
        self._register_unicode_fonts()

        # ── Edit 2: palette + page geometry from the injected Theme ──
        self._build_brand()
        self.STYLES = self._build_styles()

        page_size = LETTER if str(self.theme.layout.get("page_size")) == "Letter" else A4
        self.PAGE_W, self.PAGE_H = page_size
        self.MARGIN = 2 * cm

        self._doc = SimpleDocTemplate(
            output_path,
            pagesize=page_size,
            leftMargin=self.MARGIN,
            rightMargin=self.MARGIN,
            topMargin=self.MARGIN + 1.4 * cm,   # below header
            bottomMargin=self.MARGIN + 0.9 * cm,  # above footer
            title=title,
            author=author,
            subject=subject,
            creator="HSE Report Engine — ReportLab",
        )
        self._doc._doc_title = title

    # ── Edit 1: Unicode/OFL font registration ─────────────────────
    def _register_unicode_fonts(self):
        """Register the bundled OFL fonts. Body family -> EyekyamFont; the
        Devanagari family is registered separately for per-run selection
        (reportlab has no automatic glyph fallback)."""
        self._unicode_font_registered = False
        self._unicode_font_name = "EyekyamFont"
        self._unicode_font_bold = "EyekyamFont-Bold"
        self._deva_font_name = "EyekyamDeva"
        self._deva_font_bold = "EyekyamDeva-Bold"
        self._deva_registered = False

        # Body family from the resolved theme (Noto Sans by default).
        regular, bold = self.theme.fonts.resolved_files
        if regular and os.path.exists(regular):
            try:
                pdfmetrics.registerFont(TTFont(self._unicode_font_name, regular))
                bold_path = bold if (bold and os.path.exists(bold)) else regular
                pdfmetrics.registerFont(TTFont(self._unicode_font_bold, bold_path))
                pdfmetrics.registerFontFamily(
                    self._unicode_font_name,
                    normal=self._unicode_font_name,
                    bold=self._unicode_font_bold,
                )
                self._unicode_font_registered = True
            except Exception:
                self._unicode_font_registered = False

        # Devanagari family (separate — selected per-run for Devanagari text).
        deva_reg, deva_bold = self.theme.fonts.files_for("Noto Sans Devanagari")
        if deva_reg and os.path.exists(deva_reg):
            try:
                pdfmetrics.registerFont(TTFont(self._deva_font_name, deva_reg))
                deva_bold_path = deva_bold if (deva_bold and os.path.exists(deva_bold)) else deva_reg
                pdfmetrics.registerFont(TTFont(self._deva_font_bold, deva_bold_path))
                pdfmetrics.registerFontFamily(
                    self._deva_font_name,
                    normal=self._deva_font_name,
                    bold=self._deva_font_bold,
                )
                self._deva_registered = True
            except Exception:
                self._deva_registered = False
        return self._unicode_font_registered

    def _get_font(self, base="Helvetica"):
        """Return the bundled Unicode font name if available, else fall back to
        the reportlab built-in (degradation, §4.10)."""
        if self._unicode_font_registered:
            if base.endswith("-Bold") or base.endswith("-BoldOblique"):
                return self._unicode_font_bold
            return self._unicode_font_name
        return base

    def _select_font(self, text, base="Helvetica"):
        """Whole-field font selection: render in the Devanagari family if the
        text contains Devanagari codepoints (reportlab has no auto-fallback —
        A4 Pitfall 2). v1.0 = whole-field granularity."""
        bold = base.endswith("-Bold") or base.endswith("-BoldOblique")
        if self._deva_registered and _has_devanagari(text):
            return self._deva_font_bold if bold else self._deva_font_name
        return self._get_font(base)

    # ── Edit 2: palette + org from the injected Theme ─────────────
    def _build_brand(self):
        """Build instance brand tokens from the resolved Theme palette
        (replaces the port source's module-level `class BRAND`)."""
        p = self.theme.palette

        def hx(key, fallback):
            return colors.HexColor(p.get(key, fallback))

        risk = p.get("risk", {})

        class _Brand:
            PRIMARY_TEAL = hx("primary", "#2AADA8")
            DEEP_TEAL = hx("secondary", "#1A7070")
            LIGHT_TEAL = hx("accent", "#47C4BE")
            NEAR_BLACK = hx("text", "#1A1A1A")
            WHITE = colors.white
            LIGHT_GRAY = hx("surface", "#F5F5F5")
            MID_GRAY = colors.HexColor("#9E9E9E")
            BORDER_LIGHT = colors.HexColor("#D0ECEB")
            ACCENT_AMBER = colors.HexColor(risk.get("med", "#E9A94B"))
            ACCENT_RED = colors.HexColor(risk.get("high", "#E05252"))
            ACCENT_GREEN = colors.HexColor(risk.get("low", "#4CAF50"))
            ACCENT_CRITICAL = colors.HexColor(risk.get("critical", "#B71C1C"))
            HIGH_RISK = ACCENT_RED
            MED_RISK = ACCENT_AMBER
            LOW_RISK = ACCENT_GREEN
            CRITICAL_RISK = ACCENT_CRITICAL
            BRAND_INK = NEAR_BLACK
            BRAND_MAIN = PRIMARY_TEAL

        self.BRAND = _Brand
        # org footer line (identity comes from the A9 card via theme.org)
        org = self.theme.org or {}
        self._org_name = org.get("name") or ""
        self._org_footer = org.get("footer") or ""
        self._classification = org.get("classification") or "Confidential"
        # logo path resolved by theme (may be None -> warn+omit)
        self._logo_path = self.theme.images.get("logo")

    def _build_styles(self):
        base = getSampleStyleSheet()
        BRAND = self.BRAND

        def add(name, **kw):
            if name in base:
                base[name].__dict__.update(kw)
            else:
                base.add(ParagraphStyle(name=name, **kw))
            return base[name]

        fn = self._get_font("Helvetica")
        fn_bold = self._get_font("Helvetica-Bold")

        add("Normal", fontName=fn, fontSize=10, leading=15,
            textColor=BRAND.NEAR_BLACK, spaceAfter=6)
        add("BodyText", fontName=fn, fontSize=10, leading=15,
            textColor=BRAND.NEAR_BLACK, spaceAfter=6, alignment=TA_JUSTIFY)
        add("h1", fontName=fn_bold, fontSize=20, leading=26,
            textColor=BRAND.PRIMARY_TEAL, spaceBefore=14, spaceAfter=8, keepWithNext=1)
        add("h2", fontName=fn_bold, fontSize=14, leading=18,
            textColor=BRAND.DEEP_TEAL, spaceBefore=12, spaceAfter=6, keepWithNext=1)
        add("h3", fontName=fn_bold, fontSize=11, leading=15,
            textColor=BRAND.NEAR_BLACK, spaceBefore=8, spaceAfter=4, keepWithNext=1)
        add("Caption", fontName=fn, fontSize=8, leading=11,
            textColor=BRAND.MID_GRAY, spaceAfter=4, alignment=TA_CENTER)
        add("TableHeader", fontName=fn_bold, fontSize=9, leading=12,
            textColor=BRAND.WHITE, alignment=TA_LEFT)
        add("TableCell", fontName=fn, fontSize=9, leading=12,
            textColor=BRAND.NEAR_BLACK, alignment=TA_LEFT)
        add("Callout", fontName=fn, fontSize=10, leading=14,
            textColor=BRAND.DEEP_TEAL, backColor=colors.HexColor("#E8F7F7"),
            borderPadding=(8, 10, 8, 10), spaceAfter=10,
            borderWidth=1, borderColor=BRAND.LIGHT_TEAL)
        add("Footer", fontName=fn, fontSize=8, leading=10,
            textColor=BRAND.MID_GRAY, alignment=TA_CENTER)
        add("BulletItem", fontName=fn, fontSize=10, leading=15,
            textColor=BRAND.NEAR_BLACK, spaceAfter=4, leftIndent=12, bulletIndent=0)
        return base

    # ── Page callbacks (closures over self) ───────────────────────
    def _make_cover_callback(self, cover_data):
        BRAND = self.BRAND
        PAGE_W, PAGE_H, MARGIN = self.PAGE_W, self.PAGE_H, self.MARGIN
        logo_path = self._logo_path
        org_name = self._org_name
        org_footer = self._org_footer
        classification = self._classification

        def _draw(canvas, doc):
            canvas.saveState()
            w, h = PAGE_W, PAGE_H

            # Background
            canvas.setFillColor(BRAND.PRIMARY_TEAL)
            canvas.rect(0, 0, w, h, fill=1, stroke=0)

            # Diagonal right panel
            canvas.setFillColor(colors.HexColor("#229994"))
            p = canvas.beginPath()
            p.moveTo(w * 0.6, 0)
            p.lineTo(w, 0)
            p.lineTo(w, h)
            p.lineTo(w * 0.75, h)
            p.close()
            canvas.setFillColor(colors.HexColor("#229994"))
            canvas.drawPath(p, fill=1, stroke=0)

            # Bottom stripe
            canvas.setFillColor(BRAND.DEEP_TEAL)
            canvas.rect(0, 0, w, 3.5 * cm, fill=1, stroke=0)

            # ── Edit 3: logo on teal — white rounded-rect backing,
            #    Pillow-guarded (degrade to raw logo if Pillow absent) ──
            if logo_path and Path(logo_path).exists():
                try:
                    logo_h = 2.2 * cm
                    logo_x = MARGIN
                    logo_y = h - 3.2 * cm
                    try:
                        from PIL import Image as PILImage
                        pil_img = PILImage.open(str(logo_path))
                        iw, ih = pil_img.size
                        logo_w = logo_h * (iw / ih)
                    except Exception:
                        # Pillow absent — square fallback width, still draw card
                        logo_w = logo_h * 3
                    pad = 0.15 * cm
                    canvas.setFillColor(BRAND.WHITE)
                    canvas.roundRect(logo_x - pad, logo_y - pad,
                                     logo_w + 2 * pad, logo_h + 2 * pad,
                                     radius=4, fill=1, stroke=0)
                    canvas.drawImage(str(logo_path), logo_x, logo_y,
                                     width=logo_w, height=logo_h,
                                     preserveAspectRatio=True, mask="auto")
                except Exception:
                    pass

            _fn_bold = self._get_font("Helvetica-Bold")
            _fn = self._get_font("Helvetica")

            # Title (multi-line via \n). Devanagari-aware per-line font.
            title_lines = cover_data.get("title", "Report").split("\n")
            y = h * 0.62
            canvas.setFillColor(BRAND.WHITE)
            for line in title_lines:
                canvas.setFont(self._select_font(line, "Helvetica-Bold"), 30)
                canvas.drawString(MARGIN, y, line)
                y -= 38

            # Subtitle (word-wrapped)
            subtitle = cover_data.get("subtitle", "")
            if subtitle:
                _sf = self._select_font(subtitle, "Helvetica")
                canvas.setFont(_sf, 16)
                canvas.setFillColor(colors.HexColor("#D0ECEB"))
                max_subtitle_w = w - 2 * MARGIN - w * 0.15
                words = subtitle.split()
                lines = []
                current_line = ""
                for word in words:
                    test = (current_line + " " + word).strip()
                    if canvas.stringWidth(test, _sf, 16) <= max_subtitle_w:
                        current_line = test
                    else:
                        if current_line:
                            lines.append(current_line)
                        current_line = word
                if current_line:
                    lines.append(current_line)
                for line in lines:
                    canvas.drawString(MARGIN, y - 10, line)
                    y -= 22
                y -= 10

            # Divider
            canvas.setStrokeColor(BRAND.LIGHT_TEAL)
            canvas.setLineWidth(1.5)
            canvas.line(MARGIN, y - 8, MARGIN + w * 0.45, y - 8)
            y -= 28

            # Client + date + tagline
            canvas.setFont(_fn, 11)
            canvas.setFillColor(colors.HexColor("#9EDEDD"))
            client = cover_data.get("client", "")
            if client:
                canvas.setFont(self._select_font(client, "Helvetica"), 11)
                canvas.drawString(MARGIN, y, f"Prepared for: {client}")
                canvas.setFont(_fn, 11)
                y -= 18
            date = cover_data.get("date", datetime.now().strftime("%B %Y"))
            canvas.drawString(MARGIN, y, f"Date: {date}")
            y -= 18
            tagline = cover_data.get("tagline", "")
            if tagline:
                canvas.drawString(MARGIN, y, tagline)

            # Bottom footer — org name + footer line + classification
            if org_name:
                canvas.setFont(_fn_bold, 8)
                canvas.setFillColor(BRAND.WHITE)
                canvas.drawString(MARGIN, 1.8 * cm, org_name)
            if org_footer:
                canvas.setFont(_fn, 8)
                canvas.setFillColor(colors.HexColor("#9EDEDD"))
                canvas.drawString(MARGIN, 1.2 * cm, org_footer)
            canvas.setFont(_fn, 8)
            canvas.setFillColor(colors.HexColor("#9EDEDD"))
            year = datetime.now().year
            owner = org_name or "HSE Report Engine"
            canvas.drawString(MARGIN, 0.7 * cm,
                              f"© {year} {owner}  |  {classification}")

            canvas.restoreState()
        return _draw

    def _make_header_footer(self):
        BRAND = self.BRAND
        PAGE_W, PAGE_H, MARGIN = self.PAGE_W, self.PAGE_H, self.MARGIN
        logo_path = self._logo_path
        org_name = self._org_name
        org_footer = self._org_footer

        def _draw_header_footer(canvas, doc):
            canvas.saveState()
            w, h = PAGE_W, PAGE_H

            # Header bar
            canvas.setFillColor(BRAND.PRIMARY_TEAL)
            canvas.rect(0, h - 1.4 * cm, w, 1.4 * cm, fill=1, stroke=0)

            if logo_path and Path(logo_path).exists():
                try:
                    canvas.drawImage(str(logo_path), MARGIN, h - 1.25 * cm,
                                     height=1.0 * cm, preserveAspectRatio=True,
                                     mask="auto")
                except Exception:
                    pass

            canvas.setFont(self._select_font(self.title, "Helvetica-Bold"), 9)
            canvas.setFillColor(BRAND.WHITE)
            title = getattr(doc, "_doc_title", "Report")
            canvas.drawRightString(w - MARGIN, h - 0.9 * cm, title)

            # Footer bar
            canvas.setFillColor(BRAND.DEEP_TEAL)
            canvas.rect(0, 0, w, 0.9 * cm, fill=1, stroke=0)

            canvas.setFont(self._get_font("Helvetica"), 8)
            canvas.setFillColor(BRAND.WHITE)
            year = datetime.now().year
            owner = org_name or "HSE Report Engine"
            footer_bits = org_footer or ""
            canvas.drawString(MARGIN, 0.32 * cm,
                              f"© {year} {owner}  |  {footer_bits}".rstrip(" |"))
            canvas.drawRightString(w - MARGIN, 0.32 * cm, f"Page {doc.page}")

            canvas.restoreState()
        return _draw_header_footer

    # ── Cover page ────────────────────────────
    def add_cover(self, title: str = None, subtitle: str = "",
                  client: str = "", date: str = None,
                  tagline: str = ""):
        """Add a full-bleed branded cover page (drawn via canvas)."""
        self._cover_data = {
            "title": title or self.title,
            "subtitle": subtitle,
            "client": client,
            "date": date or datetime.now().strftime("%B %Y"),
            "tagline": tagline,
        }
        self._story.append(PageBreak())

    # ── Section heading ───────────────────────
    def add_heading(self, text: str, level: int = 1):
        STYLES = self.STYLES
        style = {1: "h1", 2: "h2", 3: "h3"}.get(level, "h2")
        # Devanagari-aware: clone the style with the Devanagari font if needed.
        st = STYLES[style]
        if self._deva_registered and _has_devanagari(text):
            st = ParagraphStyle(f"{style}_deva_{id(text)}", parent=STYLES[style],
                                fontName=self._select_font(text, "Helvetica-Bold"))
        if level == 1:
            self._story.append(KeepTogether([
                HRFlowable(width="100%", thickness=2,
                           color=self.BRAND.PRIMARY_TEAL, spaceAfter=4),
                Paragraph(text, st),
            ]))
        else:
            self._story.append(Paragraph(text, st))

    # ── Body text ─────────────────────────────
    def add_text(self, text: str, style: str = "BodyText"):
        """Add a paragraph of body text. Supports HTML: <b>, <i>, <br/>, <font color>."""
        STYLES = self.STYLES
        st = STYLES[style]
        if self._deva_registered and _has_devanagari(text):
            st = ParagraphStyle(f"{style}_deva_{id(text)}", parent=STYLES[style],
                                fontName=self._select_font(text, "Helvetica"))
        self._story.append(Paragraph(text, st))

    # ── Bullet list ───────────────────────────
    def add_bullets(self, items: list, symbol: str = "•"):
        STYLES = self.STYLES
        for item in items:
            st = STYLES["BulletItem"]
            if self._deva_registered and _has_devanagari(item):
                st = ParagraphStyle(f"Bullet_deva_{id(item)}", parent=STYLES["BulletItem"],
                                    fontName=self._select_font(item, "Helvetica"))
            self._story.append(Paragraph(f"{symbol} &nbsp; {item}", st))

    # ── Section (heading + text together) ────
    def add_section(self, heading: str, body: str, level: int = 1):
        self.add_heading(heading, level)
        if body:
            self.add_text(body)
        self.add_spacer(0.3)

    # ── Spacer ────────────────────────────────
    def add_spacer(self, height_cm: float = 0.5):
        self._story.append(Spacer(1, height_cm * cm))

    # ── Page break ────────────────────────────
    def add_page_break(self):
        self._story.append(PageBreak())

    # ── Callout / info box ────────────────────
    def add_callout(self, text: str):
        """Teal-tinted info box for key insights."""
        self._story.append(Paragraph(text, self.STYLES["Callout"]))
        self._story.append(Spacer(1, 0.3 * cm))

    # ── Divider line ──────────────────────────
    def add_divider(self):
        self._story.append(HRFlowable(
            width="100%", thickness=1, color=self.BRAND.BORDER_LIGHT,
            spaceBefore=4, spaceAfter=8))

    # ── Data table ────────────────────────────
    def add_table(self, headers: list, rows: list,
                  col_widths: list = None, caption: str = None,
                  risk_col: int = None):
        """Add a styled data table (risk-colour column, repeat header rows)."""
        STYLES = self.STYLES
        BRAND = self.BRAND
        PAGE_W, MARGIN = self.PAGE_W, self.MARGIN
        usable_w = PAGE_W - 2 * MARGIN
        n = len(headers)
        # CR-02 §4.10: a schema-valid model can carry an empty table; skip
        # rather than ZeroDivisionError. Mirrors the DOCX add_metrics_row guard.
        if n == 0:
            return
        if not col_widths:
            col_widths = [usable_w / n] * n
        else:
            if max(col_widths) >= 25:
                col_widths = list(col_widths)
            else:
                col_widths = [w * cm for w in col_widths]
            total = sum(col_widths)
            if total > usable_w:
                scale = usable_w / total
                col_widths = [w * scale for w in col_widths]

        def _cell_para(value, style_name):
            text = str(value)
            st = STYLES[style_name]
            if self._deva_registered and _has_devanagari(text):
                base = "Helvetica-Bold" if style_name == "TableHeader" else "Helvetica"
                st = ParagraphStyle(f"{style_name}_deva_{id(text)}",
                                    parent=STYLES[style_name],
                                    fontName=self._select_font(text, base))
            return Paragraph(text, st)

        header_row = [_cell_para(h, "TableHeader") for h in headers]
        data = [header_row]
        for row in rows:
            data.append([_cell_para(c, "TableCell") for c in row])

        style = TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), BRAND.PRIMARY_TEAL),
            ("TEXTCOLOR",  (0, 0), (-1, 0), BRAND.WHITE),
            ("FONTNAME",   (0, 0), (-1, 0), self._get_font("Helvetica-Bold")),
            ("FONTSIZE",   (0, 0), (-1, 0), 9),
            ("TOPPADDING", (0, 0), (-1, 0), 7),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 7),
            ("FONTNAME",   (0, 1), (-1, -1), self._get_font("Helvetica")),
            ("FONTSIZE",   (0, 1), (-1, -1), 9),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [BRAND.WHITE, BRAND.LIGHT_GRAY]),
            ("TOPPADDING", (0, 1), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 1), (-1, -1), 5),
            ("GRID", (0, 0), (-1, -1), 0.4, BRAND.BORDER_LIGHT),
            ("LINEBELOW", (0, 0), (-1, 0), 1.5, BRAND.DEEP_TEAL),
            ("LEFTPADDING",  (0, 0), (-1, -1), 8),
            ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ])

        # CR-02 §4.10 / AC3 parity: only apply risk colouring when risk_col is in
        # range; per-row skip short rows. A schema-valid model may carry a
        # risk_column past the header count or rows shorter than risk_col —
        # neither should IndexError (DOCX survives both; PDF now matches).
        if risk_col is not None and 0 <= risk_col < n:
            risk_map = {
                "high": BRAND.HIGH_RISK,
                "medium": BRAND.MED_RISK,
                "med": BRAND.MED_RISK,
                "low": BRAND.LOW_RISK,
                "critical": BRAND.CRITICAL_RISK,
            }
            for i, row in enumerate(rows, start=1):
                if risk_col >= len(row):
                    continue
                val = str(row[risk_col]).strip().lower()
                color = risk_map.get(val)
                if color:
                    style.add("TEXTCOLOR", (risk_col, i), (risk_col, i), color)
                    style.add("FONTNAME",  (risk_col, i), (risk_col, i),
                              self._get_font("Helvetica-Bold"))

        t = Table(data, colWidths=col_widths, repeatRows=1)
        t.setStyle(style)
        self._story.append(t)

        if caption:
            self._story.append(Spacer(1, 0.2 * cm))
            self._story.append(Paragraph(caption, STYLES["Caption"]))
        self._story.append(Spacer(1, 0.5 * cm))

    # ── Key metrics row ───────────────────────
    def add_metrics_row(self, metrics: list):
        """Render 2–4 KPI boxes in a horizontal row."""
        PAGE_W, MARGIN = self.PAGE_W, self.MARGIN
        n = len(metrics)
        # CR-02 §4.10: an empty metrics row would ZeroDivisionError; skip it
        # (mirrors the DOCX add_metrics_row `if n == 0: return` guard).
        if n == 0:
            return
        usable_w = PAGE_W - 2 * MARGIN
        cell_w = (usable_w - (n - 1) * 0.3 * cm) / n
        box_h = 2.4 * cm
        primary_hex = self.theme.palette.get("primary", "#2AADA8")

        def metric_cell(m):
            bg = m.get("color", primary_hex)
            d = Drawing(cell_w, box_h)
            d.add(Rect(0, 0, cell_w, box_h,
                       fillColor=colors.HexColor(bg), strokeColor=None, rx=4, ry=4))
            val_text = str(m.get("value", "")) + str(m.get("unit", ""))
            d.add(String(cell_w / 2, box_h * 0.5, val_text,
                         fontName=self._select_font(val_text, "Helvetica-Bold"),
                         fontSize=22, fillColor=colors.white, textAnchor="middle"))
            d.add(String(cell_w / 2, box_h * 0.2, m.get("label", ""),
                         fontName=self._select_font(m.get("label", ""), "Helvetica"),
                         fontSize=9, fillColor=colors.white, textAnchor="middle"))
            return d

        cells = [[metric_cell(m) for m in metrics]]
        col_widths = [cell_w] * n
        t = Table(cells, colWidths=col_widths)
        t.setStyle(TableStyle([
            ("ALIGN",        (0, 0), (-1, -1), "CENTER"),
            ("VALIGN",       (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING",  (0, 0), (-1, -1), 2),
            ("RIGHTPADDING", (0, 0), (-1, -1), 2),
            ("TOPPADDING",   (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ]))
        self._story.append(t)
        self._story.append(Spacer(1, 0.6 * cm))

    # ── Image ─────────────────────────────────
    def add_image(self, path: str, width_cm: float = 14,
                  caption: str = None, align: str = "CENTER"):
        img = Image(path, width=width_cm * cm)
        img.hAlign = align
        self._story.append(img)
        if caption:
            self._story.append(Spacer(1, 0.15 * cm))
            self._story.append(Paragraph(caption, self.STYLES["Caption"]))
        self._story.append(Spacer(1, 0.5 * cm))

    # ── Diagram (branded image wrapper) ───────
    def add_diagram(self, image_path: str, caption: str = None,
                    width_cm: float = 14):
        """Embed a diagram image with branded presentation (Pillow-guarded)."""
        PAGE_W, PAGE_H, MARGIN = self.PAGE_W, self.PAGE_H, self.MARGIN
        BRAND = self.BRAND
        usable_w = PAGE_W - 2 * MARGIN
        max_h = PAGE_H - 2 * MARGIN - 1.4 * cm - 0.9 * cm - 2 * cm
        img_w = min(width_cm * cm, usable_w)
        try:
            from PIL import Image as PILImage
            pil_img = PILImage.open(image_path)
            iw, ih = pil_img.size
            pil_img.close()
            scaled_h = img_w * (ih / iw)
            if scaled_h > max_h:
                scaled_h = max_h
                img_w = max_h * (iw / ih)
            img = Image(image_path, width=img_w, height=scaled_h)
        except Exception:
            # Pillow absent / unreadable — let reportlab size it
            img = Image(image_path, width=img_w)
        img.hAlign = "CENTER"

        t = Table([[img]], colWidths=[img_w + 0.4 * cm])
        t.setStyle(TableStyle([
            ("BOX",           (0, 0), (-1, -1), 0.5, BRAND.BORDER_LIGHT),
            ("TOPPADDING",    (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ("LEFTPADDING",   (0, 0), (-1, -1), 6),
            ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
            ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
        ]))
        self._story.append(t)
        if caption:
            self._story.append(Spacer(1, 0.15 * cm))
            self._story.append(Paragraph(caption, self.STYLES["Caption"]))
        self._story.append(Spacer(1, 0.5 * cm))

    # ── Numbered steps ────────────────────────
    def add_numbered_steps(self, steps: list, color=None):
        """Render a list of sequential numbered steps with branded styling."""
        BRAND = self.BRAND
        STYLES = self.STYLES
        default_color = color if color else BRAND.PRIMARY_TEAL
        elements = []
        for i, step in enumerate(steps, 1):
            is_critical = step.get("critical", False)
            step_color = BRAND.ACCENT_RED if is_critical else default_color
            if isinstance(step_color, str):
                step_color = colors.HexColor(step_color)
            num_text = f'<font color="{step_color.hexval()}"><b>{i}.</b></font>'
            title_color = step_color.hexval()
            title = step.get("title", "")
            desc = step.get("description", "")
            para_text = (f'{num_text} '
                         f'<font color="{title_color}"><b>{title}</b></font>'
                         f'<br/>{desc}')
            elements.append(Paragraph(para_text, STYLES["BodyText"]))
            elements.append(Spacer(1, 0.15 * cm))
        self._story.extend(elements)
        self._story.append(Spacer(1, 0.3 * cm))

    # ── Info / alert box ──────────────────────
    def add_info_box(self, text: str, box_type: str = "info"):
        """Render a colored alert/info box with type-based styling."""
        BRAND = self.BRAND
        STYLES = self.STYLES
        config = {
            "info": {"border": BRAND.PRIMARY_TEAL, "bg": colors.HexColor("#E8F7F7"), "prefix": "Key Insight"},
            "warning": {"border": BRAND.ACCENT_AMBER, "bg": colors.HexColor("#FEF6E8"), "prefix": "Important"},
            "critical": {"border": BRAND.ACCENT_RED, "bg": colors.HexColor("#FDECEC"), "prefix": "Critical"},
            "tip": {"border": BRAND.ACCENT_GREEN, "bg": colors.HexColor("#EDF7EE"), "prefix": "Tip"},
        }
        c = config.get(box_type, config["info"])
        prefix = c["prefix"]
        full_text = f'<font color="{c["border"].hexval()}"><b>{prefix}:</b></font> {text}'
        style = ParagraphStyle(
            f"InfoBox_{box_type}_{id(text)}",
            parent=STYLES["BodyText"],
            backColor=c["bg"],
            borderPadding=(10, 12, 10, 12),
            borderWidth=1.5,
            borderColor=c["border"],
            spaceAfter=10,
        )
        if self._deva_registered and _has_devanagari(text):
            style.fontName = self._select_font(text, "Helvetica")
        self._story.append(Paragraph(full_text, style))
        self._story.append(Spacer(1, 0.3 * cm))

    # ── Comparison columns ────────────────────
    def add_comparison_columns(self, left_title: str, left_items: list,
                                right_title: str, right_items: list,
                                left_color=None, right_color=None):
        """Side-by-side comparison layout with colored header bars."""
        BRAND = self.BRAND
        STYLES = self.STYLES
        PAGE_W, MARGIN = self.PAGE_W, self.MARGIN
        lc = left_color or BRAND.PRIMARY_TEAL
        rc = right_color or BRAND.ACCENT_RED
        if isinstance(lc, str):
            lc = colors.HexColor(lc)
        if isinstance(rc, str):
            rc = colors.HexColor(rc)
        usable_w = PAGE_W - 2 * MARGIN
        col_w = (usable_w - 0.5 * cm) / 2
        left_hdr = Paragraph(
            f'<font color="white"><b>{left_title}</b></font>',
            ParagraphStyle(f"CompHdrL_{id(left_title)}", parent=STYLES["TableHeader"], alignment=TA_CENTER))
        right_hdr = Paragraph(
            f'<font color="white"><b>{right_title}</b></font>',
            ParagraphStyle(f"CompHdrR_{id(right_title)}", parent=STYLES["TableHeader"], alignment=TA_CENTER))
        left_bullets = [Paragraph(f"&bull; &nbsp; {item}", STYLES["BulletItem"]) for item in left_items]
        right_bullets = [Paragraph(f"&bull; &nbsp; {item}", STYLES["BulletItem"]) for item in right_items]
        hdr_table = Table([[left_hdr, right_hdr]], colWidths=[col_w, col_w])
        hdr_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (0, 0), lc),
            ("BACKGROUND", (1, 0), (1, 0), rc),
            ("TOPPADDING", (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ("LEFTPADDING", (0, 0), (-1, -1), 8),
            ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ]))
        self._story.append(hdr_table)
        content_table = Table([[left_bullets, right_bullets]], colWidths=[col_w, col_w])
        content_table.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ("LEFTPADDING", (0, 0), (-1, -1), 8),
            ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ("BOX", (0, 0), (0, 0), 0.5, lc),
            ("BOX", (1, 0), (1, 0), 0.5, rc),
        ]))
        self._story.append(content_table)
        self._story.append(Spacer(1, 0.5 * cm))

    # ── Two-column layout ─────────────────────
    def add_two_columns(self, left_content: list, right_content: list,
                        left_w_pct: float = 0.5):
        """Side-by-side layout. Each content list is a list of tuples."""
        STYLES = self.STYLES
        PAGE_W, MARGIN = self.PAGE_W, self.MARGIN
        usable_w = PAGE_W - 2 * MARGIN - 0.5 * cm
        lw = usable_w * left_w_pct
        rw = usable_w * (1 - left_w_pct)

        def _build(items):
            out = []
            for item in items:
                typ = item[0]
                if typ == "text":
                    out.append(Paragraph(item[1], STYLES["BodyText"]))
                elif typ == "heading":
                    out.append(Paragraph(item[1], STYLES["h2"]))
                elif typ == "bullets":
                    for b in item[1]:
                        out.append(Paragraph(f"• &nbsp; {b}", STYLES["BulletItem"]))
                elif typ == "spacer":
                    h = item[1] if len(item) > 1 else 0.5
                    out.append(Spacer(1, h * cm))
            return out

        left = _build(left_content)
        right = _build(right_content)
        t = Table([[left, right]], colWidths=[lw, rw])
        t.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ]))
        self._story.append(t)
        self._story.append(Spacer(1, 0.5 * cm))

    # ── Code block ──────────────────────────────
    def add_code_block(self, lines: list, font_size: int = 8, title: str = None):
        """Render a monospace code block with a light-grey background."""
        BRAND = self.BRAND
        if title:
            self.add_heading(title, level=3)
        mono_font = self._get_font_mono()
        code_style = ParagraphStyle(
            f"EyekyamCode_{id(lines)}",
            fontName=mono_font,
            fontSize=font_size,
            leading=font_size * 1.5,
            textColor=BRAND.NEAR_BLACK,
            backColor=BRAND.LIGHT_GRAY,
            borderPadding=(9, 10, 9, 10),
            borderWidth=0.5,
            borderColor=colors.HexColor("#CCCCCC"),
            spaceAfter=0,
        )
        safe_text = "<br/>".join(
            line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            for line in lines
        )
        self._story.append(Paragraph(safe_text, code_style))
        self._story.append(Spacer(1, 0.4 * cm))

    def _get_font_mono(self):
        """Resolve + register the bundled mono family on first use; fall back
        to Courier (§4.10)."""
        reg, bold = self.theme.fonts.files_for("Noto Sans Mono")
        if reg and os.path.exists(reg):
            name = "EyekyamMono"
            try:
                if name not in pdfmetrics.getRegisteredFontNames():
                    pdfmetrics.registerFont(TTFont(name, reg))
                return name
            except Exception:
                pass
        return "Courier"

    # ── Logo override ────────────────────────────
    def set_logo(self, path: str):
        """Override the resolved logo with a custom image (instance-scoped)."""
        self._logo_path = str(path)

    # ── Contact section ──────────────────────────
    def add_contact_section(self, heading: str = "Contact Us"):
        """Add a branded contact block from the theme org tokens."""
        BRAND = self.BRAND
        PAGE_W, MARGIN = self.PAGE_W, self.MARGIN
        self.add_heading(heading, level=2)
        self._story.append(Spacer(1, 0.2 * cm))
        org = self.theme.org or {}
        contact_rows = []
        if org.get("name"):
            contact_rows.append(["Company", org["name"]])
        if org.get("footer"):
            contact_rows.append(["Contact", org["footer"]])
        if not contact_rows:
            contact_rows = [["Contact", "—"]]
        usable_w = PAGE_W - 2 * MARGIN
        t = Table(contact_rows, colWidths=[3.5 * cm, usable_w - 3.5 * cm])
        t.setStyle(TableStyle([
            ("FONTNAME", (0, 0), (0, -1), self._get_font("Helvetica-Bold")),
            ("FONTNAME", (1, 0), (1, -1), self._get_font("Helvetica")),
            ("FONTSIZE", (0, 0), (-1, -1), 10),
            ("TEXTCOLOR", (0, 0), (0, -1), BRAND.PRIMARY_TEAL),
            ("TEXTCOLOR", (1, 0), (1, -1), BRAND.NEAR_BLACK),
            ("TOPPADDING", (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("LINEBELOW", (0, -1), (-1, -1), 0.5, BRAND.BORDER_LIGHT),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ]))
        self._story.append(t)
        self._story.append(Spacer(1, 0.5 * cm))

    def add_toc_placeholder(self, sections: list, auto_number=None):
        """Render a table of contents, then page break."""
        _NUMBERED_RE = re.compile(r"^\s*\d+(\.\d+)*\.?\s")
        items = []
        for s in sections:
            if isinstance(s, (tuple, list)) and len(s) >= 2:
                items.append((s[0], s[1]))
            else:
                items.append(("section", str(s)))
        if auto_number is None:
            section_items = [t for k, t in items if k == "section"]
            check_pool = section_items if section_items else [t for _, t in items]
            if check_pool:
                pre_numbered = sum(1 for t in check_pool if _NUMBERED_RE.match(t))
                auto_number = pre_numbered < max(1, len(check_pool) / 2)
            else:
                auto_number = True
        self.add_heading("Table of Contents", level=2)
        section_counter = 1
        for kind, title in items:
            title_text = str(title)
            if kind == "sub":
                indent = "&nbsp;&nbsp;&nbsp;&nbsp;"
                opener, closer = "", ""
            elif kind == "phase":
                indent = "&nbsp;&nbsp;&nbsp;&nbsp;"
                opener, closer = "<i>", "</i>"
            else:
                indent = ""
                opener, closer = "<b>", "</b>"
            if auto_number and kind == "section":
                prefix = f"<b>{section_counter}.</b>&nbsp; "
                section_counter += 1
            else:
                prefix = ""
            self._story.append(Paragraph(
                f"{indent}{prefix}{opener}{title_text}{closer}",
                self.STYLES["BulletItem"]))
        self.add_page_break()

    # ── Build ─────────────────────────────────
    def build(self):
        """Finalise and write the PDF to output_path."""
        if self._cover_data:
            first_page_cb = self._make_cover_callback(self._cover_data)
        else:
            first_page_cb = self._make_header_footer()
        self._doc.build(
            self._story,
            onFirstPage=first_page_cb,
            onLaterPages=self._make_header_footer(),
        )
        return self.output_path
