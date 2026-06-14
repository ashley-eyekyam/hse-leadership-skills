"""Shared pytest fixtures + sys.path wiring for the A4 report-engine tests.

The engine modules (theme, render_pdf, render_docx, generate_report) live in
the report-engine directory, one level up from this tests/ folder. Put that dir
on sys.path so the tests import them the same way generate_report.py does
(`from theme import resolve_theme`), regardless of the invoking cwd.
"""

import json
import sys
from pathlib import Path

import pytest

ENGINE_DIR = Path(__file__).resolve().parent.parent
FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"

if str(ENGINE_DIR) not in sys.path:
    sys.path.insert(0, str(ENGINE_DIR))


@pytest.fixture(scope="session")
def engine_dir() -> Path:
    return ENGINE_DIR


@pytest.fixture(scope="session")
def fixtures_dir() -> Path:
    return FIXTURES_DIR


@pytest.fixture(scope="session")
def example_model_path() -> Path:
    return FIXTURES_DIR / "example_report.json"


@pytest.fixture
def example_model(example_model_path) -> dict:
    return json.loads(example_model_path.read_text(encoding="utf-8"))


@pytest.fixture(scope="session")
def report_schema(engine_dir) -> dict:
    return json.loads(
        (engine_dir / "report_model_schema.json").read_text(encoding="utf-8")
    )


@pytest.fixture(scope="session")
def brand_schema(engine_dir) -> dict:
    return json.loads(
        (engine_dir / "brand.schema.json").read_text(encoding="utf-8")
    )
