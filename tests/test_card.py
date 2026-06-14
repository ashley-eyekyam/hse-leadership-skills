"""Persistent CARD-01/03 observable contract (A9 → A8).

This is the durable contract test the A8 quality harness keys off in Phase 3 —
NOT a one-shot inline check. It re-asserts, over the on-disk artifacts:

  (i)   the shared default `branding/company-card.yaml` validates against
        `branding/company-card.schema.json` and is the Eyekyam default
        (report_branding_default: true, placement: footer);
  (ii)  the clean A4↔A9 boundary — the card carries NO `logo` and NO `palette`
        (top-level OR under `company`); the schema REJECTS such a card
        (additionalProperties:false at both object levels);
  (iii) a mutated card with an out-of-enum placement (`header`) FAILS validation;
  (iv)  the fixture card (examples/risk-assessment/branding/company-card.yaml) is
        a real copy (no "placeholder") that also validates.

Plain pytest, sandbox-offline, no framework config — mirrors the
assets/report-engine/tests style. Paths resolve relative to the repo root so the
suite runs from any working directory.
"""

import copy
import json
from pathlib import Path

import jsonschema
import pytest
import yaml

REPO = Path(__file__).resolve().parents[1]

SCHEMA_PATH = REPO / "branding" / "company-card.schema.json"
CARD_PATH = REPO / "branding" / "company-card.yaml"
FIXTURE_CARD_PATH = REPO / "examples" / "risk-assessment" / "branding" / "company-card.yaml"


def _load_json(p: Path) -> dict:
    return json.loads(p.read_text(encoding="utf-8"))


def _load_yaml(p: Path) -> dict:
    return yaml.safe_load(p.read_text(encoding="utf-8"))


def test_artifacts_exist():
    """The schema, the shared default card, and the fixture card are all on disk."""
    assert SCHEMA_PATH.is_file(), f"missing {SCHEMA_PATH}"
    assert CARD_PATH.is_file(), f"missing {CARD_PATH}"
    assert FIXTURE_CARD_PATH.is_file(), f"missing {FIXTURE_CARD_PATH}"


def test_schema_name_token():
    """The schema pins the hse-company-card/v1 name token as a const."""
    schema = _load_json(SCHEMA_PATH)
    assert schema["properties"]["schema"]["const"] == "hse-company-card/v1"


def test_default_card_validates():
    """The shipped Eyekyam default validates against the schema."""
    schema = _load_json(SCHEMA_PATH)
    card = _load_yaml(CARD_PATH)
    jsonschema.validate(card, schema)


def test_default_card_is_eyekyam_default():
    """The default carries the spec-verbatim identity + the A4 bridge flag."""
    card = _load_yaml(CARD_PATH)
    assert card["schema"] == "hse-company-card/v1"
    assert card["show"] is True
    assert card["placement"] == "footer"
    assert card["report_branding_default"] is True
    assert card["company"]["name"] == "Eyekyam"
    assert card["company"]["contact_email"] == "ashley@eyekyam.com"


def test_card_carries_no_logo_or_palette():
    """A4↔A9 boundary: the card holds NO logo/palette (top-level or under company)."""
    card = _load_yaml(CARD_PATH)
    for key in ("logo", "palette"):
        assert key not in card, f"card must not carry top-level {key!r}"
        assert key not in card.get("company", {}), f"card.company must not carry {key!r}"


def test_schema_rejects_logo_or_palette():
    """The schema fails-closed on a card declaring logo/palette (boundary guard)."""
    schema = _load_json(SCHEMA_PATH)
    card = _load_yaml(CARD_PATH)

    bad_top = copy.deepcopy(card)
    bad_top["logo"] = "assets/logo.png"
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(bad_top, schema)

    bad_palette = copy.deepcopy(card)
    bad_palette["palette"] = {"primary": "#008080"}
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(bad_palette, schema)

    bad_company_logo = copy.deepcopy(card)
    bad_company_logo["company"]["logo"] = "assets/logo.png"
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(bad_company_logo, schema)


def test_schema_rejects_bad_placement():
    """An out-of-enum placement (header) fails validation."""
    schema = _load_json(SCHEMA_PATH)
    card = _load_yaml(CARD_PATH)
    bad = copy.deepcopy(card)
    bad["placement"] = "header"
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(bad, schema)


def test_schema_rejects_wrong_schema_const():
    """A wrong schema name token fails validation."""
    schema = _load_json(SCHEMA_PATH)
    card = _load_yaml(CARD_PATH)
    bad = copy.deepcopy(card)
    bad["schema"] = "hse-company-card/v2"
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(bad, schema)


def test_schema_requires_core_keys():
    """show, placement, company.name, and report_branding_default are required."""
    schema = _load_json(SCHEMA_PATH)
    card = _load_yaml(CARD_PATH)
    for key in ("show", "placement", "report_branding_default"):
        bad = copy.deepcopy(card)
        del bad[key]
        with pytest.raises(jsonschema.ValidationError):
            jsonschema.validate(bad, schema)
    bad_name = copy.deepcopy(card)
    del bad_name["company"]["name"]
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(bad_name, schema)


def test_fixture_card_is_real_copy_and_validates():
    """The fixture card is a real copy (no 'placeholder') and validates."""
    schema = _load_json(SCHEMA_PATH)
    raw = FIXTURE_CARD_PATH.read_text(encoding="utf-8")
    assert "placeholder" not in raw.lower(), "fixture card not reconciled (still a placeholder)"
    fixture = _load_yaml(FIXTURE_CARD_PATH)
    jsonschema.validate(fixture, schema)
    # the fixture is a real copy of the canonical default (same identity payload)
    canonical = _load_yaml(CARD_PATH)
    assert fixture == canonical, "fixture card must be a real copy of the shared default"
