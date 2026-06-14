"""REPORT-01 — report_model_schema.json validates the §4.1 example and rejects
unknown top-level shapes + undefined block types."""

import copy

import jsonschema
import pytest


def test_report_model(report_schema, example_model):
    """The §4.1 worked example validates against report_model_schema.json."""
    jsonschema.validate(example_model, report_schema)


def test_schema_name_token(report_schema):
    """The schema carries the hse-report-model/v1 name token."""
    assert report_schema["properties"]["schema"]["const"] == "hse-report-model/v1"


def test_rejects_unknown_top_level_shape(report_schema, example_model):
    """An unknown top-level property is rejected (additionalProperties:false)."""
    bad = copy.deepcopy(example_model)
    bad["unexpected_top_level"] = {"oops": True}
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(bad, report_schema)


def test_rejects_missing_required_meta(report_schema, example_model):
    """meta.title is required."""
    bad = copy.deepcopy(example_model)
    del bad["meta"]["title"]
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(bad, report_schema)


def test_rejects_empty_table_headers(report_schema, example_model):
    """CR-02 belt-and-suspenders: an empty `table.headers` is rejected at
    validation (minItems:1) so an empty table exits cleanly (exit 2) rather than
    reaching the renderer."""
    bad = copy.deepcopy(example_model)
    bad["sections"].append({"type": "table", "headers": [], "rows": []})
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(bad, report_schema)


def test_rejects_empty_metrics(report_schema, example_model):
    """CR-02 belt-and-suspenders: an empty `metrics.metrics` is rejected at
    validation (minItems:1)."""
    bad = copy.deepcopy(example_model)
    bad["sections"].append({"type": "metrics", "metrics": []})
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(bad, report_schema)


def test_rejects_undefined_block_type(report_schema, example_model):
    """A block with a type not in the schema is rejected."""
    bad = copy.deepcopy(example_model)
    bad["sections"].append({"type": "not_a_real_block", "text": "x"})
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(bad, report_schema)


def test_rejects_unknown_field_on_known_block(report_schema, example_model):
    """A known block type with an unexpected field is rejected."""
    bad = copy.deepcopy(example_model)
    bad["sections"].append({"type": "heading", "text": "x", "bogus": 1})
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(bad, report_schema)


def test_wrong_schema_const_rejected(report_schema, example_model):
    """A wrong schema name token fails validation."""
    bad = copy.deepcopy(example_model)
    bad["schema"] = "hse-report-model/v2"
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(bad, report_schema)


@pytest.mark.parametrize("block", [
    {"type": "heading", "level": 1, "text": "H"},
    {"type": "paragraph", "text": "p"},
    {"type": "bullets", "items": ["a", "b"]},
    {"type": "table", "headers": ["A"], "rows": [["1"]], "risk_column": 0},
    {"type": "metrics", "metrics": [{"label": "L", "value": "1"}]},
    {"type": "callout", "text": "c", "box_type": "info"},
    {"type": "findings", "rows": [{"title": "t", "risk_level": "High", "description": "d"}]},
    {"type": "hoc_table", "rows": [{"control": "c", "tier": "Engineering"}]},
    {"type": "recommendations", "rows": [{"action": "a"}]},
    {"type": "divider"},
    {"type": "page_break"},
    {"type": "spacer"},
])
def test_every_block_type_accepted(report_schema, example_model, block):
    """Every §4.1 block type is schema-defined and validates standalone."""
    doc = {
        "schema": "hse-report-model/v1",
        "meta": {"title": "T"},
        "sections": [block],
    }
    jsonschema.validate(doc, report_schema)
