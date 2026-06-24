# Install `safety-authorisation` as a ChatGPT Custom GPT

1. Create a new Custom GPT (Configure tab).
2. Paste `instructions.md` into the **Instructions** field.
3. Upload every file under `knowledge/` as **Knowledge**.
4. Enable **Code Interpreter & Data Analysis**, then upload the canonical report engine from `assets/report-engine/` (`generate_report.py`, `render_docx.py`, `render_pdf.py`, `theme.py`, the schemas, `brand.yaml`, `house-standard.yaml`, and the `fonts/` directory).
5. Upload the A7 deterministic engines from `scripts/hse_components/` (`risk_matrix.py`, `controls.py`, `rca.py`, `smart_actions.py`, `incident_rates.py`, `__init__.py`, `_shim.py`).
6. The GPT runs `generate_report.py` in Code Interpreter to produce the branded DOCX + PDF.

_Heavy Code-Interpreter assets are shared from the repo's single canonical copy (D-09) — they are named here, not duplicated into this bundle._
