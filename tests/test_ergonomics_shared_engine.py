"""LANDMINE-A — the ergonomics shared-engine golden-equality contract (MFG-02).

`ergonomics-assessment` (MFG-02, #2 in hse-manufacturing) and `health-risk-assessment`
(#25, home hse-operations) are the **two consumers of the single `ergonomics.py` engine**
(SUB-01, "one engine, two consumers" — matrix §5 / build card §evals). This skill mints NO
second scorer and copies NO KB band table: every RULA/REBA/NIOSH number in either skill is the
SAME deterministic engine's output. This durable contract test proves that, over the on-disk
artifacts:

  (i)   ONE ENGINE — both skills' `scripts/hse_components/ergonomics.py` symlinks resolve to
        the SAME repo engine file (no forked/re-implemented scorer);
  (ii)  TWO CONSUMERS, IDENTICAL SCORES — for every golden case in
        scripts/tests/fixtures/ergonomics_cases.json, the engine loaded via the
        ergonomics-assessment symlink and the engine loaded via the health-risk-assessment
        symlink return byte-identical results for identical inputs;
  (iii) GOLDEN-EQUALITY — those results match the fixture's expected RWL/LI/grand_score/
        final_score (the same golden anchors test_ergonomics.py asserts), so the shared engine
        is provably the verified one.

Plain pytest, sandbox-offline, no network/model/key. Paths resolve relative to the repo root so
the suite runs from any working directory. Each consumer's engine is loaded by absolute file
path under its own symlink so the test asserts what the SKILLS actually import at run time.
"""

import importlib.util
import json
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]

CASES_PATH = REPO / "scripts" / "tests" / "fixtures" / "ergonomics_cases.json"

# Each consumer imports the engine through its own scripts/hse_components symlink.
ERGO_ENGINE = REPO / "skills" / "ergonomics-assessment" / "scripts" / "hse_components" / "ergonomics.py"
HRA_ENGINE = REPO / "skills" / "health-risk-assessment" / "scripts" / "hse_components" / "ergonomics.py"

RWL_TOL = 0.05   # NIOSH RWL tolerance (kg) — matches the fixture notes.
LI_TOL = 0.01    # NIOSH Lifting Index tolerance — matches the fixture notes.


def _load_engine(path: Path, mod_name: str):
    """Load the engine module from the consumer's symlinked path as `mod_name`."""
    spec = importlib.util.spec_from_file_location(mod_name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _score(engine, case: dict) -> dict:
    """Run the case's engine method with its inputs and return the engine result dict."""
    kind = case["engine"]
    inp = case["inputs"]
    if kind == "niosh":
        return engine.niosh_rwl(**inp)
    if kind == "rula":
        return engine.rula_score(**inp)
    if kind == "reba":
        return engine.reba_score(**inp)
    raise AssertionError(f"unknown engine kind in fixture: {kind!r}")


@pytest.fixture(scope="module")
def cases():
    data = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    c = data.get("cases", [])
    assert c, "golden ergonomics cases fixture is empty"
    return c


@pytest.fixture(scope="module")
def ergo_engine():
    assert ERGO_ENGINE.exists() or ERGO_ENGINE.is_symlink(), "ergonomics-assessment engine symlink missing"
    return _load_engine(ERGO_ENGINE, "_ergo_consumer_engine")


@pytest.fixture(scope="module")
def hra_engine():
    assert HRA_ENGINE.exists() or HRA_ENGINE.is_symlink(), "health-risk-assessment engine symlink missing"
    return _load_engine(HRA_ENGINE, "_hra_consumer_engine")


# (i) ONE ENGINE ---------------------------------------------------------------

def test_both_consumers_symlink_the_same_engine_file():
    """The two skills must reach the SAME on-disk ergonomics.py — no forked scorer."""
    assert ERGO_ENGINE.resolve() == HRA_ENGINE.resolve(), (
        "ergonomics-assessment and health-risk-assessment resolve to DIFFERENT engine files — "
        "LANDMINE-A: there must be one engine, not two"
    )
    # And that single resolved file is the repo engine (not a vendored copy).
    assert ERGO_ENGINE.resolve() == (REPO / "scripts" / "hse_components" / "ergonomics.py").resolve()


# (ii) TWO CONSUMERS, IDENTICAL SCORES -----------------------------------------

def test_two_consumers_produce_identical_scores_for_identical_inputs(cases, ergo_engine, hra_engine):
    """For every golden input, the engine loaded via each consumer's symlink returns the
    byte-identical result — the 'two consumers, one engine' guarantee."""
    for case in cases:
        r_ergo = _score(ergo_engine, case)
        r_hra = _score(hra_engine, case)
        assert r_ergo == r_hra, (
            f"{case['engine']} case diverged between consumers for inputs {case['inputs']}: "
            f"ergonomics-assessment={r_ergo} vs health-risk-assessment={r_hra}"
        )


# (iii) GOLDEN-EQUALITY (the shared engine is the verified one) -----------------

def test_shared_engine_matches_golden_anchors(cases, ergo_engine):
    """The shared engine reproduces the fixture's golden RWL/LI/grand_score/final_score —
    integers EXACT, NIOSH floats within the published tolerance."""
    for case in cases:
        r = _score(ergo_engine, case)
        kind = case["engine"]
        if kind == "niosh":
            assert abs(r["rwl"] - case["expected_rwl"]) <= RWL_TOL, (
                f"NIOSH RWL {r['rwl']} != expected {case['expected_rwl']} ({case['inputs']})"
            )
            if case.get("expected_li") is not None and r["li"] is not None:
                assert abs(r["li"] - case["expected_li"]) <= LI_TOL, (
                    f"NIOSH LI {r['li']} != expected {case['expected_li']} ({case['inputs']})"
                )
        elif kind == "rula":
            assert r["grand_score"] == case["expected_grand_score"], (
                f"RULA grand_score {r['grand_score']} != expected {case['expected_grand_score']}"
            )
        elif kind == "reba":
            assert r["final_score"] == case["expected_final_score"], (
                f"REBA final_score {r['final_score']} != expected {case['expected_final_score']}"
            )


def test_report_blocks_are_identical_across_consumers(cases, ergo_engine, hra_engine):
    """to_report_blocks(result) — the [metrics, table] pair the skills drop into report.json —
    is also identical across the two consumers (the report path shares the engine too)."""
    for case in cases:
        b_ergo = ergo_engine.to_report_blocks(_score(ergo_engine, case))
        b_hra = hra_engine.to_report_blocks(_score(hra_engine, case))
        assert b_ergo == b_hra, f"to_report_blocks diverged for {case['engine']} {case['inputs']}"
