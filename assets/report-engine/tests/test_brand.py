"""REPORT-04/05 — brand.schema.json validates the default teal brand.yaml,
rejects a malformed (non-hex) palette, and house-standard.yaml has exactly the
11 §4.7 sections in order."""

import copy

import jsonschema
import pytest
import yaml


# Canonical §4.7 order (11 sections).
HOUSE_ORDER = [
    "cover",
    "classification",
    "toc",
    "executive-summary",
    "scope-method",
    "key-findings",
    "hierarchy-of-controls",
    "recommendations",
    "regulatory-basis",
    "appendices",
    "limitations-deid-notice",
]

AUTO_SECTIONS = {"cover", "classification", "toc", "limitations-deid-notice"}


@pytest.fixture(scope="module")
def default_brand(engine_dir):
    return yaml.safe_load((engine_dir / "brand.yaml").read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def house_template(engine_dir):
    path = engine_dir / "templates" / "house-standard.yaml"
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_default_brand_validates(brand_schema, default_brand):
    """The bundled Eyekyam teal brand.yaml validates against brand.schema.json."""
    jsonschema.validate(default_brand, brand_schema)


def test_default_brand_is_teal(default_brand):
    """The default carries the verified Eyekyam teal palette."""
    assert default_brand["palette"]["primary"].upper() == "#2AADA8"
    assert default_brand["palette"]["secondary"].upper() == "#1A7070"
    assert default_brand["palette"]["accent"].upper() == "#47C4BE"


def test_non_hex_palette_fails(brand_schema, default_brand):
    """A malformed (non-hex) palette colour fails validation."""
    bad = copy.deepcopy(default_brand)
    bad["palette"]["primary"] = "teal"
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(bad, brand_schema)


def test_house_has_eleven_sections(house_template):
    """house-standard.yaml has exactly 11 sections."""
    sections = house_template["sections"]
    assert len(sections) == 11


def test_house_order(house_template):
    """The 11 sections are in the canonical §4.7 order."""
    keys = [s["key"] for s in house_template["sections"]]
    assert keys == HOUSE_ORDER


def test_house_auto_sections_marked(house_template):
    """cover / classification / toc / limitations-deid-notice are engine-auto;
    the rest are skill-authored."""
    for s in house_template["sections"]:
        expected = "auto" if s["key"] in AUTO_SECTIONS else "skill"
        assert s["source"] == expected, f"{s['key']} should be {expected}"


def test_house_limitations_last(house_template):
    """The limitations/de-id notice is the final auto-stamped section."""
    last = house_template["sections"][-1]
    assert last["key"] == "limitations-deid-notice"
    assert last["source"] == "auto"
    assert "Limitations" in last["title"]
