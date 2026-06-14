"""test_sme_review_nonblocking.py — QA-05 / SME-02 / SME-03 contract.

Proves the automated HSE-SME-persona review (scripts/sme_review.py, A8 §4.5) is
the FLAG-but-DON'T-BLOCK enforcement class, kept DISTINCT from the deterministic
hard-block class (de-id leak / invented citation / weighted <4.0 in run_evals.py):

  - a FLAG verdict yields exit 0 (a FLAG NEVER self-blocks) ............ QA-05
  - the review records that it RAN (SME-03 — no merge without a recorded pass)
  - the module NEVER emits a competent-person sign-off string ......... SME-02

The shared conftest only puts hse_components/ on sys.path, so (mirroring
test_lint_skills.py) we add scripts/ here to import the top-level module.
"""

import sys
from pathlib import Path

import pytest

SCRIPTS_DIR = Path(__file__).resolve().parent.parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

sme_review = pytest.importorskip(
    "sme_review", reason="scripts/sme_review.py must be importable (A8 §4.5)")


# An artifact engineered to trip every defensibility check — guarantees a FLAG.
FLAGGING_ARTIFACT = """\
# Risk Assessment

- Ensure appropriate controls are in place.
- The dust hazard is controlled by PPE and a toolbox talk.

Action: clean the area weekly.

Control: lock-out the panel.

Conclusion: the residual risk is acceptable.
"""

# A clean artifact: specific controls, named owners, review dates, cited
# conclusions — should PASS with no findings.
CLEAN_ARTIFACT = """\
# Confined-Space Entry Risk Assessment — Tank T-204, 2026-06-14

Control: continuous forced-air ventilation of tank T-204 at >= 20 air changes/hr,
isolated and LOTO-locked at panel P-3. Owner: Shift Supervisor (role). Review date:
2026-12-14; re-assessment trigger: any change to the entry permit.

Action: install the fixed gas-detection interlock on T-204 by 2026-07-01.
Owner: Maintenance Lead (role).

Conclusion: residual risk is Low (per HSG274, 2013) after the engineering control.
"""


def test_flag_yields_exit_zero():
    """QA-05: a FLAG verdict NEVER self-blocks — main() returns 0."""
    rc = sme_review.main(["--text", FLAGGING_ARTIFACT])
    assert rc == 0, "a FLAG must NOT exit nonzero (QA-05)"


def test_flag_verdict_is_actually_a_flag():
    """The flagging artifact really does produce FLAG findings (not a false PASS
    that trivially exits 0)."""
    record = sme_review.review(FLAGGING_ARTIFACT)
    assert record["verdict"] == sme_review.VERDICT_FLAG
    assert record["findings"], "expected at least one FLAG finding"


def test_clean_artifact_passes_and_exits_zero():
    record = sme_review.review(CLEAN_ARTIFACT)
    assert record["verdict"] == sme_review.VERDICT_PASS
    assert record["findings"] == []
    assert sme_review.main(["--text", CLEAN_ARTIFACT]) == 0


def test_review_ran_is_recorded():
    """SME-03: the review records that it RAN (the recorded-as-ran marker)."""
    record = sme_review.review(FLAGGING_ARTIFACT)
    assert record["review_ran"] is True
    assert record["marker"] == sme_review.REVIEW_RAN_MARKER


def test_never_emits_competent_person_sign_off():
    """SME-02: the module never emits a human competent-person sign-off — the
    record's sign_off is None and no forbidden string appears in its output."""
    record = sme_review.review(FLAGGING_ARTIFACT)
    assert record["sign_off"] is None

    rendered = sme_review._render_human(record).lower()
    for forbidden in sme_review.SIGN_OFF_FORBIDDEN:
        assert forbidden not in rendered, (
            f"SME-02 violated: emitted a competent-person sign-off string: {forbidden!r}")


def test_two_enforcement_classes_stay_distinct():
    """sme_review.py must NOT import or invoke the deterministic hard-block
    graders — the FLAG class and the HARD-BLOCK class are separate modules."""
    source = (SCRIPTS_DIR / "sme_review.py").read_text(encoding="utf-8")
    # No import of the deterministic grader package / run_evals hard-block path.
    assert "import grade_deid" not in source
    assert "from graders" not in source
    assert "auto_fail" not in source.replace("# ", ""), (
        "sme_review must not raise the deterministic auto_fail hard block")


def test_main_exit_zero_via_file(tmp_path):
    """The file-path entrypoint also exits 0 on a FLAG."""
    artifact = tmp_path / "artifact.md"
    artifact.write_text(FLAGGING_ARTIFACT, encoding="utf-8")
    assert sme_review.main([str(artifact)]) == 0
