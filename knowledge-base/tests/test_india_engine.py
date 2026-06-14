"""A3 India-engine contract (KB-02 — §3.7 / AC5).

Durable on-disk contract over `knowledge-base/regulatory/in-state-forms.md` +
its `_registry.yaml` entry. Asserts the legacy-first India engine:

  - the four seeded states TN / KA / MH / DL are present, plus the BOCW row
    (the five verified seeded rows, §3.7);
  - the cross-sector module slots mines-act / peso / msihc are registered;
  - the `state-detection` topic is registered on the fragment (mandatory state
    detection, §3.7 Decision 5);
  - NO national form number is hard-coded anywhere — every India form is a
    state-prescribed string (T-02-05-03).

Plain pytest, sandbox-offline. Paths resolve from the repo root.
"""

import re
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
REG = REPO / "knowledge-base" / "regulatory" / "_registry.yaml"
FRAGMENT = REPO / "knowledge-base" / "regulatory" / "in-state-forms.md"

SEEDED_STATES = ["TN", "KA", "MH", "DL"]
MODULE_SLOTS = ["mines-act", "peso", "msihc"]


def _entry(kid: str) -> dict:
    for e in yaml.safe_load(REG.read_text(encoding="utf-8")):
        if e["id"] == kid:
            return e
    raise AssertionError(f"{kid} not in regulatory/_registry.yaml")


def test_stateforms_registered():
    e = _entry("KB-REG-IN-STATEFORMS")
    assert e["file"] == "in-state-forms.md"
    assert "IN" in e["facets"]["jurisdiction"]


def test_state_detection_topic_registered():
    e = _entry("KB-REG-IN-STATEFORMS")
    assert "state-detection" in e["facets"]["topics"], "state-detection topic missing (§3.7)"


def test_seeded_states_and_bocw_present():
    body = FRAGMENT.read_text(encoding="utf-8")
    for st in SEEDED_STATES:
        # appears as a `| <state> |` cell in a factories-act row
        assert re.search(rf"\|\s*{st}\s*\|", body), f"seeded state {st} missing from in-state-forms.md"
    assert "bocw" in body.lower(), "BOCW row missing"
    assert "Form XXV" in body, "BOCW Form XXV row missing"


def test_module_slots_present():
    body = FRAGMENT.read_text(encoding="utf-8").lower()
    for slot in MODULE_SLOTS:
        assert slot in body, f"cross-sector module slot {slot} missing"


def test_no_national_form_number():
    """India is legacy-first: no nationwide/national form number anywhere (§3.7)."""
    body = FRAGMENT.read_text(encoding="utf-8")
    # No phrasing that asserts a single national/nationwide/central form NUMBER.
    forbidden = re.compile(
        r"(national|nationwide)\s+form\s+(no\.?|number|#)?\s*[-:]?\s*\d",
        re.IGNORECASE,
    )
    assert not forbidden.search(body), "a national form number appears to be hard-coded"
    # The fragment must explicitly state the no-national-number rule.
    assert "no india form is ever cited as a single nationwide number" in body.lower() or (
        "no nationwide form number" in body.lower()
    ), "fragment does not assert the no-national-form-number rule"
