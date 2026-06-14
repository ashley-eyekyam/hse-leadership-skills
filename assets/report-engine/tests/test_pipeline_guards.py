"""Regression tests for the Phase-02 code-review pipeline guards:

  WR-03 — a malformed/invalid --card is validated against company-card.schema.json
          and the rejection is NAMED on stderr before falling back (branding ON).
  WR-05 — a path-escaping --out (a `..` component) is refused with a clean
          nonzero exit, not written wherever the process can write.
  WR-01 — meta.brand is honoured as a fallback when --brand is absent, resolved
          relative to the model file's directory (previously a silent dead field).
"""

import json

import yaml

import generate_report


# ── WR-03: card validation ──────────────────────────────────────────────────
def test_invalid_card_is_rejected_with_named_warning(tmp_path, capsys):
    """A supplied --card that fails company-card.schema.json warns (naming the
    failure) and falls back to branding ON, returning no card."""
    bad_card = {
        # missing required keys (show/placement/company/report_branding_default)
        "schema": "hse-company-card/v1",
    }
    cp = tmp_path / "bad-card.yaml"
    cp.write_text(yaml.safe_dump(bad_card), encoding="utf-8")

    flag, card = generate_report._read_card_flag(str(cp), is_default=False)
    assert flag is True          # fallback: branding stays ON
    assert card is None          # the invalid card is not used
    err = capsys.readouterr().err.lower()
    assert "failed validation" in err
    assert "bad-card.yaml" in err


def test_valid_card_passes_validation(tmp_path):
    """A schema-valid supplied card is accepted and returned."""
    good = {
        "schema": "hse-company-card/v1",
        "show": True,
        "placement": "footer",
        "company": {
            "name": "Acme HSE",
            "tagline": "Safety first",
            "website": "https://acme.example",
        },
        "report_branding_default": True,
    }
    cp = tmp_path / "good-card.yaml"
    cp.write_text(yaml.safe_dump(good), encoding="utf-8")
    flag, card = generate_report._read_card_flag(str(cp), is_default=False)
    assert flag is True
    assert card["company"]["name"] == "Acme HSE"


# ── WR-05: --out confinement ────────────────────────────────────────────────
def test_out_with_dotdot_is_refused(tmp_path, example_model_path, capsys):
    """generate() raises ValueError on a `..`-escaping --out (mapped to exit 2
    in main)."""
    import pytest
    with pytest.raises(ValueError):
        generate_report.generate(
            str(example_model_path), out="../../escape", formats="pdf"
        )


def test_main_refuses_escaping_out(example_model_path, capsys):
    """main() converts the escaping --out into a clean nonzero exit + message."""
    rc = generate_report.main([
        "--model", str(example_model_path),
        "--out", "../../escape",
        "--formats", "pdf",
    ])
    assert rc == 2
    assert "refused output path" in capsys.readouterr().err.lower()


def test_clean_relative_out_is_allowed(tmp_path, example_model_path, monkeypatch):
    """A clean (no `..`) relative --out is allowed (operator-normal path)."""
    monkeypatch.chdir(tmp_path)
    written = generate_report.generate(
        str(example_model_path), out="out", formats="pdf"
    )
    assert len(written) == 1


# ── WR-01: meta.brand fallback ──────────────────────────────────────────────
def test_meta_brand_is_honoured_when_no_cli_brand(tmp_path, example_model, monkeypatch):
    """When --brand is absent, generate() resolves meta.brand relative to the
    model file's directory (previously silently dropped)."""
    # Drop a model whose meta.brand points at a sibling brand.yaml.
    model = dict(example_model)
    model["meta"] = dict(model["meta"], brand="my-brand.yaml")
    model_path = tmp_path / "report.json"
    model_path.write_text(json.dumps(model), encoding="utf-8")

    brand = {"schema": "hse-brand/v1", "palette": {"primary": "#123456"}}
    (tmp_path / "my-brand.yaml").write_text(yaml.safe_dump(brand), encoding="utf-8")

    captured = {}
    real_resolve = generate_report.resolve_theme

    def spy(brand_path=None, *, org=None):
        captured["brand_path"] = brand_path
        return real_resolve(brand_path, org=org)

    monkeypatch.setattr(generate_report, "resolve_theme", spy)

    out = tmp_path / "out"
    generate_report.generate(str(model_path), out=str(out), formats="pdf")
    assert captured["brand_path"] is not None
    assert captured["brand_path"].endswith("my-brand.yaml")
    # Resolved relative to the model file's dir.
    assert str(tmp_path) in captured["brand_path"]


def test_cli_brand_overrides_meta_brand(tmp_path, example_model, monkeypatch):
    """An explicit --brand wins over meta.brand."""
    model = dict(example_model)
    model["meta"] = dict(model["meta"], brand="meta-brand.yaml")
    model_path = tmp_path / "report.json"
    model_path.write_text(json.dumps(model), encoding="utf-8")

    cli_brand = {"schema": "hse-brand/v1", "palette": {"primary": "#abcdef"}}
    cli_path = tmp_path / "cli-brand.yaml"
    cli_path.write_text(yaml.safe_dump(cli_brand), encoding="utf-8")

    captured = {}
    real_resolve = generate_report.resolve_theme

    def spy(brand_path=None, *, org=None):
        captured["brand_path"] = brand_path
        return real_resolve(brand_path, org=org)

    monkeypatch.setattr(generate_report, "resolve_theme", spy)

    out = tmp_path / "out"
    generate_report.generate(
        str(model_path), brand=str(cli_path), out=str(out), formats="pdf"
    )
    assert captured["brand_path"] == str(cli_path)
