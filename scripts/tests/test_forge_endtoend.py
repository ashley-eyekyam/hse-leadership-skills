"""test_forge_endtoend.py — the A10 AC#10 deterministic end-to-end proof (FORGE-04).

The forge is the EXECUTABLE form of the A2 contract: scaffold -> lint -> eval must
run end-to-end through it with no hard-fail. This test proves the CI-safe (no API
key, no `claude -p`) portion of that pipeline:

  1. SCAFFOLD a probe skill through scaffold.py (the real born-conformant generator);
  2. LINT it via validate_repo_skill (the lint_skills re-export CI runs) — clean;
  3. EVAL (deterministic only): run the de-id grader against the forge's own fixture
     PAIR — the seeded-leak fixture MUST hard-fail (the gate works), the clean fixture
     must NOT false-positive — and confirm the probe's clean scaffold output trips no
     deterministic hard-fail.

The model-graded >=4.0 bar is NOT exercised here — it needs `claude -p` on the local
subscription (D-03) and is the developer's pre-push gate, documented in the SUMMARY.
This test is pure deterministic Python: no network, no model, no key.

Probe skills are scaffolded UNDER the real repo skills/ tree (rule-9 KB paths are
location-relative to SKILL.md, so they only resolve there) and removed in teardown.
"""

import json
import shutil
import sys
from pathlib import Path

import pytest

# scripts/tests/test_forge_endtoend.py -> repo root, forge scripts, lint+graders
REPO = Path(__file__).resolve().parent.parent.parent
FORGE = REPO / "skills" / "hse-skill-forge"
FORGE_SCRIPTS = FORGE / "scripts"
LINT_SCRIPTS = REPO / "scripts"
FIXTURES = Path(__file__).resolve().parent / "fixtures"

for p in (str(FORGE_SCRIPTS), str(LINT_SCRIPTS)):
    if p not in sys.path:
        sys.path.insert(0, p)

import scaffold  # noqa: E402
import validate_repo_skill  # noqa: E402  (the lint_skills re-export)
from graders import grade_deid  # noqa: E402


@pytest.fixture
def probe_answers() -> dict:
    return json.loads((FIXTURES / "probe_answers.json").read_text(encoding="utf-8"))


@pytest.fixture
def scaffolded():
    """Scaffold a uniquely-named probe under the real skills/ tree; remove it after."""
    created = []

    def _make(name_suffix: str, ans: dict, **kw) -> Path:
        d = scaffold.scaffold_skill(f"ztest-e2e-{name_suffix}", ans, force=True, **kw)
        created.append(d)
        return d

    yield _make
    for d in created:
        shutil.rmtree(d, ignore_errors=True)


# --- 1+2. scaffold -> lint (the re-export CI runs) -----------------------------

def test_probe_scaffolds_and_lints_clean(probe_answers, scaffolded):
    """A probe scaffolds through scaffold.py and validate_repo_skill (the lint_skills
    re-export) passes it with zero hand-edits — born-conformant, A10 AC#1/#8/#10."""
    d = scaffolded("probe", probe_answers)
    report = validate_repo_skill.validate_skill(d)
    assert report.ok, report.errors  # the same verdict CI returns


# --- 3. deterministic eval gate: the de-id fixture PAIR ------------------------

def test_forge_deid_leak_fixture_hard_fails():
    """The forge's seeded-leak fixture MUST trip the deterministic de-id auto-fail —
    proving the privacy gate the flagships (esp. B5) depend on actually catches a leak
    (T-04-07). A vacuous gate that passes everything is the failure mode this guards."""
    leak = (FORGE / "evals" / "files" / "deid-leak.md").read_text(encoding="utf-8")
    verdict = grade_deid(leak)
    assert verdict["auto_fail"] is True, "seeded-leak fixture did NOT hard-fail"
    assert verdict["reasons"], "auto_fail with no reason is not a real catch"


def test_forge_deid_clean_fixture_passes():
    """The forge's clean fixture must NOT false-positive — the gate is precise, not
    just trigger-happy (the born-conformant/standalone eval cases carry this fixture
    and must not trip)."""
    clean = (FORGE / "evals" / "files" / "deid-clean.md").read_text(encoding="utf-8")
    verdict = grade_deid(clean)
    assert verdict["auto_fail"] is False, f"clean fixture false-positived: {verdict['reasons']}"


def test_probe_scaffold_output_no_deid_hardfail(probe_answers, scaffolded):
    """The probe's freshly scaffolded SKILL.md (the forge's actual output) trips no
    deterministic de-id hard-fail — the scaffold seeds no leaked identifier."""
    d = scaffolded("deidclean", probe_answers)
    body = (d / "SKILL.md").read_text(encoding="utf-8")
    verdict = grade_deid(body)
    assert verdict["auto_fail"] is False, f"scaffold output tripped de-id: {verdict['reasons']}"


def test_forge_evalset_wires_leak_into_a_deid_case():
    """The forge's OWN evals.json must wire the seeded-leak fixture into at least one
    case (so the keyless deterministic CI job has real text to hard-fail on — CR-01),
    and must ship >=3 cases (A8 gate)."""
    evals = json.loads((FORGE / "evals" / "evals.json").read_text(encoding="utf-8"))
    cases = evals["evals"]
    assert len(cases) >= 3, "the forge must ship >=3 evals"
    wired = [c for c in cases if any("deid-leak" in f for f in c.get("files", []))]
    assert wired, "no eval case wires evals/files/deid-leak.md (the de-id hard-fail probe)"
