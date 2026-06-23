"""Phase 16-01 negative-mint asserts (D-01 / D-02).

These are the *boundary* guards for Phase 16: they prove that the four-bundle build
does NOT re-mint anything already on disk and does NOT smuggle a new engine. Every
later skill plan (16-02..16-12) only *references* the Wave-1 KB IDs; these asserts
keep that boundary honest.

Pure deterministic Python (stdlib + pyyaml), sandbox-offline. Paths resolve from the
repo root (this file lives in knowledge-base/tests/, so parents[2] == repo root).

Guards:
  (a) engine count unchanged (== 8 .py modules, excluding __init__.py and _shim.py)
      AND scripts/hse_components/fatigue_hos.py does NOT exist  (D-01 — LOG-01 reuses
      the SUB-03 fatigue.py engine; spec-06's fatigue_hos engine is SUPERSEDED).
  (b) the REUSE renewables hazard library exists and KB-HAZ-RENEWABLES is registered
      (P11; REN-01/02/03 reference it, never re-author).
  (c) the REUSE road-safety data-point exists and KB-DATA-ROAD-SAFETY-INDICATORS is
      registered (P13; LEAD-06 owns it, logistics cross-references).
  (d) the old spec id "KB-DP-ROAD-SAFETY-INDICATORS" is NOT minted in any registry
      (CONV-1 normalised KB-DP-* → KB-DATA-*).
  (e) the combined KB-REG-FMCSA-HOS is registered exactly once and NO second fragment
      is minted for FMCSA / EU-561 (no KB-REG-US-FMCSA-HOS / KB-REG-EU-DRIVERS-HOURS-561
      in any registry) — D-02's split spec IDs are reconciled to the existing combined
      fragment, NO double-mint.
"""

from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
KB = REPO / "knowledge-base"
ENGINES = REPO / "scripts" / "hse_components"

_REGISTRY_FOLDERS = ("regulatory", "standards", "data-points", "prompt-snippets")


def _registry_ids(folder: str) -> set:
    reg = KB / folder / "_registry.yaml"
    return {e["id"] for e in yaml.safe_load(reg.read_text(encoding="utf-8"))}


def _all_registry_ids() -> set:
    ids: set = set()
    for folder in _REGISTRY_FOLDERS:
        ids |= _registry_ids(folder)
    return ids


# --- (a) engine boundary (D-01) ------------------------------------------------------

def test_engine_count_unchanged_is_eight():
    """D-01: scripts/hse_components carries exactly 8 engine modules (excluding the
    package __init__.py and the portability _shim.py). Phase 16 mints ZERO engines."""
    engines = sorted(
        p.name
        for p in ENGINES.glob("*.py")
        if p.name not in ("__init__.py", "_shim.py")
    )
    assert len(engines) == 8, f"expected 8 engine modules, found {len(engines)}: {engines}"


def test_fatigue_hos_engine_not_minted():
    """D-01: the spec-06 `fatigue_hos` engine is SUPERSEDED — LOG-01 reuses fatigue.py.
    The fatigue_hos.py file must NOT exist."""
    assert not (ENGINES / "fatigue_hos.py").is_file(), (
        "fatigue_hos.py must NOT exist (D-01 — reuse SUB-03 fatigue.py)"
    )
    # The reused engine IS present.
    assert (ENGINES / "fatigue.py").is_file(), "fatigue.py (SUB-03) must still exist (reused by LOG-01)"


# --- (b) renewables hazard library REUSE (P11) ---------------------------------------

def test_renewables_hazard_library_reused_not_reauthored():
    """D-02: KB-HAZ-RENEWABLES is the P11 negative-mint reuse target — it exists and is
    registered; Phase 16 references it, never re-authors it."""
    assert (KB / "hazard-library" / "renewables.md").is_file(), (
        "hazard-library/renewables.md must exist (P11 reuse target)"
    )
    haz_ids = {e["id"] for e in yaml.safe_load(
        (KB / "hazard-library" / "_registry.yaml").read_text(encoding="utf-8")
    )}
    assert "KB-HAZ-RENEWABLES" in haz_ids, "KB-HAZ-RENEWABLES must be registered (reused)"


# --- (c) road-safety data-point REUSE (P13) -----------------------------------------

def test_road_safety_indicators_reused_not_reauthored():
    """D-02: KB-DATA-ROAD-SAFETY-INDICATORS is the P13 negative-mint reuse target — it
    exists and is registered; logistics cross-references it, LEAD-06 owns it."""
    assert (KB / "data-points" / "road-safety-indicators.md").is_file(), (
        "data-points/road-safety-indicators.md must exist (P13 reuse target)"
    )
    assert "KB-DATA-ROAD-SAFETY-INDICATORS" in _registry_ids("data-points"), (
        "KB-DATA-ROAD-SAFETY-INDICATORS must be registered (reused)"
    )


# --- (d) old spec id normalised away (CONV-1) ---------------------------------------

def test_kb_dp_road_safety_indicators_old_id_not_minted():
    """CONV-1: the old spec id KB-DP-ROAD-SAFETY-INDICATORS must NEVER appear in any
    registry (normalised to KB-DATA-ROAD-SAFETY-INDICATORS)."""
    for folder in _REGISTRY_FOLDERS:
        assert "KB-DP-ROAD-SAFETY-INDICATORS" not in _registry_ids(folder), (
            f"KB-DP-ROAD-SAFETY-INDICATORS must NOT be minted (found in {folder}/)"
        )
    assert not (KB / "data-points" / "road-safety-indicators-dp.md").is_file()


# --- (e) FMCSA / EU-561 no double-mint (D-02 reconciliation) -------------------------

def test_fmcsa_hos_registered_exactly_once_no_split_mint():
    """D-02: the combined KB-REG-FMCSA-HOS (US + EU drivers' hours) is registered
    exactly once; LOG-01 cites this single id. The split spec IDs
    KB-REG-US-FMCSA-HOS / KB-REG-EU-DRIVERS-HOURS-561 are reconciled to it — NO second
    fragment is minted (no double-mint)."""
    reg = yaml.safe_load((KB / "regulatory" / "_registry.yaml").read_text(encoding="utf-8"))
    fmcsa_count = sum(1 for e in reg if e["id"] == "KB-REG-FMCSA-HOS")
    assert fmcsa_count == 1, "exactly one KB-REG-FMCSA-HOS entry must exist"
    assert (KB / "regulatory" / "fmcsa-hos.md").is_file(), "fmcsa-hos.md must exist (reused by LOG-01)"
    all_ids = _all_registry_ids()
    for split_id in ("KB-REG-US-FMCSA-HOS", "KB-REG-EU-DRIVERS-HOURS-561"):
        assert split_id not in all_ids, (
            f"{split_id} must NOT be minted (reconciled to the combined KB-REG-FMCSA-HOS)"
        )
    for split_file in ("us-fmcsa-hos.md", "eu-drivers-hours-561.md"):
        assert not (KB / "regulatory" / split_file).is_file(), (
            f"{split_file} must NOT exist (no FMCSA/EU double-mint)"
        )


def test_offshore_scr_and_rogs_reused_not_reauthored():
    """D-02: the other already-on-disk REUSE fragments (OFFSHORE-SCR, ROGS) are
    registered exactly once each and are referenced, not re-authored, by Phase 16."""
    reg = yaml.safe_load((KB / "regulatory" / "_registry.yaml").read_text(encoding="utf-8"))
    for kid in ("KB-REG-OFFSHORE-SCR", "KB-REG-ROGS"):
        count = sum(1 for e in reg if e["id"] == kid)
        assert count == 1, f"exactly one {kid} entry must exist (reused, not re-authored)"
