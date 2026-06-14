# Third-Party Notices

This project distributes, or depends at runtime on, the third-party components
listed below. Each is used under its own license; the full license texts are
available from each project's canonical source. This file is maintained by the
A1 scaffold; the exact bundled font families are confirmed by A4 at its
implementation phase.

## Runtime dependencies

| Component | License | Used by |
|-----------|---------|---------|
| **PyYAML** (`pyyaml`) | MIT | Harness scripts (linter, eval runner) and the YAML registries / company cards |
| **ReportLab** (`reportlab`) | BSD (BSD-3-Clause) | PDF rendering — `assets/report-engine/render_pdf.py` |
| **python-docx** | MIT | DOCX rendering — `assets/report-engine/render_docx.py` |

## Development / CI dependencies

| Component | License | Used by |
|-----------|---------|---------|
| **pytest** | MIT | Test runner — development and CI only; not a runtime dependency |

## Bundled assets — fonts

The report engine bundles font files under `assets/report-engine/fonts/`. Each
family is distributed under the **SIL Open Font License 1.1 (OFL-1.1)**,
Copyright The Noto Project Authors. The families were selected for India-first
Devanagari and ₹ (U+20B9) coverage with zero system-font dependency. Source:
the official Noto release at <https://github.com/notofonts/notofonts.github.io>
(`fonts/<family>/unhinted/ttf/`).

| Family | License | Files bundled |
|--------|---------|---------------|
| **Noto Sans** | SIL OFL-1.1 | `NotoSans-Regular.ttf`, `NotoSans-Bold.ttf` (Latin/Latin-Ext, ₹ U+20B9) |
| **Noto Sans Devanagari** | SIL OFL-1.1 | `NotoSansDevanagari-Regular.ttf`, `NotoSansDevanagari-Bold.ttf` (Devanagari) |
| **Noto Sans Mono** | SIL OFL-1.1 | `NotoSansMono-Regular.ttf`, `NotoSansMono-Bold.ttf` (monospace, ₹ U+20B9) |

Each font is the unmodified TTF from the official Noto release (not subset or
re-hosted). SHA-256 of the bundled files (provenance record):

```
f3961a9cde016d41a4879aecda1474d3a36d6bf54fa0e4643de029cc2248b0e8  NotoSans-Regular.ttf
87cb2d84472a7d66da659ee47b6cdb9552326e8c128245231f191b6ac72529d9  NotoSans-Bold.ttf
216921eded5a97435fa0638deca66496bf51f52fa3467f566deb9938c25a71de  NotoSansDevanagari-Regular.ttf
0bf2924e12d627371446121a663e275f9173033048c4f4ccb514394950bbf577  NotoSansDevanagari-Bold.ttf
87f8ce0522a6c99b743ee5fc75b4073cfdd575639119672828b7b9944b65b4f4  NotoSansMono-Regular.ttf
1100772b2f79c102402a1011df5e2226517d0f40ac553a25fb12fdbad8c11b85  NotoSansMono-Bold.ttf
```

## Note on `scripts/hse_components/`

The shared deterministic Python modules in `scripts/hse_components/` are
**standard-library only** and introduce no third-party dependency, so they
contribute no entry to this file.
