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
family is distributed under the **SIL Open Font License 1.1 (OFL-1.1)**. The
exact families are an A4 implementation-phase selection (with India-first
Devanagari and ₹ coverage as a selection criterion); this file lists whatever
A4 bundles, each family named with its OFL-1.1 notice.

- _(Font families to be confirmed and listed by A4 — each under SIL Open Font License 1.1.)_

## Note on `scripts/hse_components/`

The shared deterministic Python modules in `scripts/hse_components/` are
**standard-library only** and introduce no third-party dependency, so they
contribute no entry to this file.
