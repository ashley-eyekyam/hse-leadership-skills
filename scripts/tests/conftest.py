"""Shared pytest fixtures + sys.path wiring for the A7 hse_components tests.

The deterministic engine modules (risk_matrix, incident_rates, and — in Plan 03
— controls, rca, smart_actions) live in scripts/hse_components/, one level up
and into the package from this tests/ folder. Put that package dir on sys.path
so the engine tests import them with bare names (`from risk_matrix import
score`), exactly the way the portability shim resolves them at runtime,
regardless of the invoking cwd.

This conftest is SHARED across all A7/A8 engine tests in scripts/tests/ — Plan
03's controls/rca/smart_actions tests reuse it; do not duplicate it there.

Mirrors assets/report-engine/tests/conftest.py's sys.path-insert idiom, with the
inserted dir swapped to the hse_components package.
"""

import json
import sys
from pathlib import Path

import pytest

COMPONENTS_DIR = Path(__file__).resolve().parent.parent / "hse_components"
FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"

if str(COMPONENTS_DIR) not in sys.path:
    sys.path.insert(0, str(COMPONENTS_DIR))


@pytest.fixture(scope="session")
def components_dir() -> Path:
    return COMPONENTS_DIR


@pytest.fixture(scope="session")
def fixtures_dir() -> Path:
    return FIXTURES_DIR


@pytest.fixture(scope="session")
def risk_matrix_cases_path() -> Path:
    return FIXTURES_DIR / "risk_matrix_cases.json"


@pytest.fixture
def risk_matrix_cases(risk_matrix_cases_path) -> list:
    return json.loads(risk_matrix_cases_path.read_text(encoding="utf-8"))


@pytest.fixture(scope="session")
def rca_cases_path() -> Path:
    return FIXTURES_DIR / "rca_cases.json"


@pytest.fixture
def rca_cases(rca_cases_path) -> dict:
    return json.loads(rca_cases_path.read_text(encoding="utf-8"))
