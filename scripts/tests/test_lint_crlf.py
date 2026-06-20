"""WR-03 regression — CRLF-authored reference manifests must parse.

`lint_skills._read` returns raw UTF-8, and `_split_frontmatter` matches the
LF-only `^---\\n...\\n---\\n` frontmatter delimiter. Before WR-03, a CRLF-authored
`references/intake.md` or `references/sme-review.md` (e.g. written on Windows)
failed that match and yielded `fm={}` — surfacing a FALSE "manifest
absent/unparseable" finding even though the manifest was present and valid.

These fixtures write CRLF-line-ending reference files into a tmp_path skill_dir,
call `_rule11_intake_coverage` / `_rule12_sme_review` directly (bypassing the
frozen-example exemption gate, mirroring test_rule11_intake.py), and assert that
NO "manifest absent/unparseable" finding is produced. They also assert the
`_split_frontmatter` helper itself parses a CRLF document.

This test file asserts behavior; it NEVER edits `lint_skills.py`.
"""

import shutil
import sys
import textwrap
from pathlib import Path

import pytest

SCRIPTS_DIR = Path(__file__).resolve().parent.parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

REPO = SCRIPTS_DIR.parent
FIXTURE = REPO / "examples" / "risk-assessment"

lint_skills = pytest.importorskip(
    "lint_skills", reason="scripts/lint_skills.py not implemented yet"
)

# Reuse the byte-identical clean baselines from the Rule-11/12 fixture suites so a
# CRLF-encoded copy is a faithful round-trip of a known-clean manifest.
from test_rule11_intake import CLEAN_INTAKE  # noqa: E402
from test_rule12_sme import CLEAN_SME  # noqa: E402


def _crlf(text: str) -> str:
    """Re-encode a (LF) string with Windows CRLF line endings."""
    return text.replace("\n", "\r\n")


# --- the helper itself ----------------------------------------------------------

def test_split_frontmatter_parses_crlf_document():
    doc = _crlf(
        textwrap.dedent(
            """\
            ---
            intake-coverage:
              covers: [ELI-SCOPE]
            ---
            body line
            """
        )
    )
    fm, body = lint_skills._split_frontmatter(doc)
    assert isinstance(fm.get("intake-coverage"), dict), (
        "CRLF frontmatter must parse to a dict, not fall back to fm={}"
    )
    assert "body line" in body


# --- Rule 11: a CRLF intake.md manifest is FOUND, not falsely absent ------------

def test_crlf_intake_manifest_is_found(tmp_path):
    dst = tmp_path / "fixture-skill"
    shutil.copytree(FIXTURE, dst)
    # Write the clean intake with CRLF line endings.
    (dst / "references" / "intake.md").write_text(_crlf(CLEAN_INTAKE), encoding="utf-8")
    # Ensure the SKILL.md lean pointer is present (step 10), as make_skill does.
    skill_md = dst / "SKILL.md"
    body = skill_md.read_text(encoding="utf-8")
    if "references/intake.md" not in body:
        body = body + "\n- `references/intake.md` — the structured-intake coverage contract.\n"
        skill_md.write_text(body, encoding="utf-8")

    report = lint_skills.Report(skill="fixture-skill")
    lint_skills._rule11_intake_coverage(report, body, dst, REPO)
    findings = [w for w in report.warnings if w.startswith("rule 11")]
    assert not any("manifest absent/unparseable" in f for f in findings), findings
    # A CRLF copy of the known-clean intake should produce ZERO rule-11 findings.
    assert findings == [], findings


# --- Rule 12: a CRLF sme-review.md manifest is FOUND, not falsely absent --------

def test_crlf_sme_review_manifest_is_found(tmp_path):
    dst = tmp_path / "fixture-skill"
    shutil.copytree(FIXTURE, dst)
    (dst / "references" / "sme-review.md").write_text(_crlf(CLEAN_SME), encoding="utf-8")
    # Inject a roster reference below orchestration:end (step 5), as make_skill does.
    orch_end = "<!-- hse:block:orchestration:end -->"
    skill_md = dst / "SKILL.md"
    body = skill_md.read_text(encoding="utf-8")
    roster_line = (
        orch_end
        + "\n\n- **SME Reviewer** — applies the personas in "
        + "`references/sme-review.md` as a recorded (non-blocking) review.\n"
    )
    body = body.replace(orch_end, roster_line, 1)
    skill_md.write_text(body, encoding="utf-8")

    report = lint_skills.Report(skill="fixture-skill")
    lint_skills._rule12_sme_review(report, body, dst)
    findings = [w for w in report.warnings if w.startswith("rule 12")]
    assert not any("manifest absent/unparseable" in f for f in findings), findings
    # A CRLF copy of the known-clean sme-review should produce ZERO rule-12 findings.
    assert findings == [], findings
