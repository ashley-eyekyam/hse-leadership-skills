"""test_house_template_selection.py — p02 WR-02 (meta.house_template honoured with
fallback) + IN-03 (ValidationError distinguished from a render error) regression.

WR-02: _load_house_template(name) selects templates/<name>.yaml. A bare stem only
(any path component / .yaml suffix is stripped — traversal-safe, T-04-12); a missing
named template falls back to house-standard with a visible warning; the field is no
longer inert (the caller passes meta.get('house_template', ...)).

IN-03: main() distinguishes a jsonschema.ValidationError ('invalid model') from any
other engine/render exception ('render error'), so a renderer bug is not mislabelled
as the user's report.json being invalid.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ENGINE_DIR = Path(__file__).resolve().parents[1]
if str(ENGINE_DIR) not in sys.path:
    sys.path.insert(0, str(ENGINE_DIR))

import generate_report as g  # noqa: E402


def _section_count(house: dict) -> int:
    return len(house.get("sections", []))


def test_named_house_template_loads():
    """A real named template resolves to templates/<name>.yaml."""
    house = g._load_house_template("house-standard")
    assert _section_count(house) == 11


def test_missing_house_template_falls_back(capsys):
    """A missing named template falls back to house-standard with a warning."""
    house = g._load_house_template("does-not-exist")
    assert _section_count(house) == 11  # the fallback layout
    err = capsys.readouterr().err
    assert "does-not-exist" in err and "falling back" in err


def test_house_template_traversal_is_stripped():
    """WR-02 traversal-safety: a path-bearing value is reduced to its bare stem and
    cannot escape templates/ (T-04-12). Falls back rather than reading an outside file."""
    house = g._load_house_template("../../../etc/passwd")
    assert _section_count(house) == 11  # stripped to 'passwd' -> not found -> fallback


def test_default_house_template_when_unspecified():
    """The default arg is the house-standard layout (meta without house_template)."""
    house = g._load_house_template()
    assert _section_count(house) == 11


def test_in03_invalid_model_labelled_invalid(tmp_path, capsys):
    """A schema-invalid model is labelled 'invalid model' (not 'render error')."""
    bad = tmp_path / "bad.json"
    # Missing required 'sections' -> jsonschema.ValidationError.
    bad.write_text(json.dumps({"schema": "hse-report-model/v1", "meta": {"title": "x"}}),
                   encoding="utf-8")
    rc = g.main(["--model", str(bad), "--out", str(tmp_path / "out"), "--formats", "docx"])
    assert rc == 2
    err = capsys.readouterr().err
    if g._HAVE_JSONSCHEMA:
        assert "invalid model" in err
        assert "render error" not in err


def test_in03_render_error_not_mislabelled_invalid(tmp_path, monkeypatch, capsys):
    """A renderer/engine exception is labelled 'render error', NOT 'invalid model'
    (IN-03 — a renderer bug must not be blamed on the user's report.json)."""
    good = tmp_path / "good.json"
    good.write_text(json.dumps({
        "schema": "hse-report-model/v1",
        "meta": {"title": "ok"},
        "sections": [{"type": "heading", "level": 1, "text": "H"}],
    }), encoding="utf-8")

    def _boom(*_a, **_k):
        raise RuntimeError("simulated renderer bug")

    # Force a non-ValidationError exception deep in the pipeline.
    monkeypatch.setattr(g, "generate", _boom)
    rc = g.main(["--model", str(good), "--out", str(tmp_path / "out"), "--formats", "docx"])
    assert rc == 2
    err = capsys.readouterr().err
    assert "render error" in err
    assert "invalid model" not in err
