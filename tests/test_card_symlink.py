"""Persistent CARD-03 dual-resolution contract (A9 → A8) — D-06.

This makes the CARD-03 truth "a skill's card resolves via symlink AND after
symlink removal (real-copy fallback)" EXECUTABLE rather than merely documented.

It exercises BOTH resolution paths of the A9 §3.5 override mechanism in one run,
against the shared root card established by this plan:

  Branch 1 — symlink-default: a per-skill `branding/company-card.yaml` is a
             relative symlink to the shared root card. Resolving it (following the
             link, loading the YAML) yields a card that validates against the
             schema and equals the root card. This is the clean dev-tree default
             ("edit once re-brands every skill").

  Branch 2 — real-copy fallback: the symlink is REMOVED and a real copy is
             materialized in its place (the flattened-distribution / per-skill
             override path — survives a zip that strips symlinks). Re-resolving
             loads the real file, which also validates and equals the root card.

Per D-06, the LIVE per-skill symlink wiring lands with the forge `--sync` in
Phase 4; this plan establishes the shared root card + the documented mechanism +
this executable proof on a representative tmp skill. If symlinks prove fragile in
the two-repo / CI setup, the documented fallback is real-copy-everywhere — which
Branch 2 already exercises, so CARD-03 holds either way.

Hosts without symlink support (`os.symlink` raising OSError/NotImplementedError —
e.g. some Windows/CI filesystems) skip Branch 1 gracefully; Branch 2 (real-copy)
still runs so the resolution contract is never left unverified.

Plain pytest, sandbox-offline, no framework config — mirrors the
assets/report-engine/tests style.
"""

import json
import os
import shutil
from pathlib import Path

import jsonschema
import pytest
import yaml

REPO = Path(__file__).resolve().parents[1]

SCHEMA_PATH = REPO / "branding" / "company-card.schema.json"
ROOT_CARD_PATH = REPO / "branding" / "company-card.yaml"


def _load_json(p: Path) -> dict:
    return json.loads(p.read_text(encoding="utf-8"))


def _resolve_card(card_file: Path) -> dict:
    """Follow any symlink and load the YAML the per-skill path resolves to."""
    return yaml.safe_load(card_file.read_text(encoding="utf-8"))


def _symlinks_supported(target: Path, link: Path) -> bool:
    try:
        link.symlink_to(target)
    except (OSError, NotImplementedError):
        return False
    return True


def test_card_resolves_via_symlink_and_real_copy(tmp_path):
    """CARD-03: the per-skill card resolves via symlink AND after real-copy fallback."""
    schema = _load_json(SCHEMA_PATH)

    # Establish a temp "root card" — a copy of the shared default, isolated in tmp.
    root_dir = tmp_path / "branding"
    root_dir.mkdir()
    root_card = root_dir / "company-card.yaml"
    shutil.copyfile(ROOT_CARD_PATH, root_card)
    root_payload = _resolve_card(root_card)
    # sanity: the root card itself validates
    jsonschema.validate(root_payload, schema)

    # A representative per-skill branding dir that should resolve to the root card.
    skill_branding = tmp_path / "skills" / "demo-skill" / "branding"
    skill_branding.mkdir(parents=True)
    skill_card = skill_branding / "company-card.yaml"

    # ---- Branch 1: symlink-default (relative symlink to the shared root card) ----
    rel_target = Path(os.path.relpath(root_card, start=skill_branding))
    if _symlinks_supported(rel_target, skill_card):
        assert skill_card.is_symlink(), "expected a symlink for the default path"
        via_symlink = _resolve_card(skill_card)
        jsonschema.validate(via_symlink, schema)
        assert via_symlink == root_payload, "symlink must resolve to the root card"
        # Tear down Branch 1 before materializing the real copy.
        skill_card.unlink()
    else:
        pytest.skip("os.symlink unsupported on this host; real-copy branch still runs")

    # ---- Branch 2: real-copy fallback (flattened distribution / override) ----
    assert not skill_card.exists(), "symlink should be removed before the real copy"
    shutil.copyfile(root_card, skill_card)
    assert not skill_card.is_symlink(), "fallback must be a real file, not a symlink"
    via_real_copy = _resolve_card(skill_card)
    jsonschema.validate(via_real_copy, schema)
    assert via_real_copy == root_payload, "real copy must equal the root card"


def test_real_copy_branch_always_runs(tmp_path):
    """Real-copy resolution runs even on symlink-less hosts (no skip)."""
    schema = _load_json(SCHEMA_PATH)
    root_payload = _resolve_card(ROOT_CARD_PATH)

    skill_branding = tmp_path / "skills" / "demo-skill" / "branding"
    skill_branding.mkdir(parents=True)
    skill_card = skill_branding / "company-card.yaml"
    shutil.copyfile(ROOT_CARD_PATH, skill_card)

    assert not skill_card.is_symlink()
    resolved = _resolve_card(skill_card)
    jsonschema.validate(resolved, schema)
    assert resolved == root_payload
