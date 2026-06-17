"""Shared pytest fixtures + sys.path wiring for the adapter build tests.

The adapter build tool lives in adapters/build.py, one level up from this tests/
folder. Put that adapters/ dir on sys.path so the tests import it with a bare name
(`import build`), regardless of the invoking cwd — mirrors scripts/tests/conftest.py's
sys.path-insert idiom with the inserted dir swapped to adapters/.

The three spec exemplars (C §3.0 / §5 acceptance #2) exercise the build's variance:
  - risk-assessment       — moderate 3-agent roster + an A7 dependency (scripts/).
  - toolbox-talk          — single-thread roster, NO A7 dependency (no scripts/).
  - incident-investigation — 4-agent fan-out roster + an A7 dependency.
"""

import sys
from pathlib import Path

import pytest

ADAPTERS_DIR = Path(__file__).resolve().parent.parent
REPO = ADAPTERS_DIR.parent
SKILLS_DIR = REPO / "skills"

if str(ADAPTERS_DIR) not in sys.path:
    sys.path.insert(0, str(ADAPTERS_DIR))


@pytest.fixture(scope="session")
def adapters_dir() -> Path:
    return ADAPTERS_DIR


@pytest.fixture(scope="session")
def repo() -> Path:
    return REPO


@pytest.fixture(scope="session")
def skills_dir() -> Path:
    return SKILLS_DIR


@pytest.fixture(scope="session")
def risk_assessment_dir() -> Path:
    """Moderate roster + A7 (scripts/hse_components present)."""
    return SKILLS_DIR / "risk-assessment"


@pytest.fixture(scope="session")
def toolbox_talk_dir() -> Path:
    """Single-thread roster, NO A7 (no scripts/)."""
    return SKILLS_DIR / "toolbox-talk"


@pytest.fixture(scope="session")
def incident_investigation_dir() -> Path:
    """4-agent fan-out roster + A7."""
    return SKILLS_DIR / "incident-investigation"


@pytest.fixture(scope="session")
def exemplar_dirs(
    risk_assessment_dir, toolbox_talk_dir, incident_investigation_dir
) -> dict:
    """The three spec exemplars keyed by name."""
    return {
        "risk-assessment": risk_assessment_dir,
        "toolbox-talk": toolbox_talk_dir,
        "incident-investigation": incident_investigation_dir,
    }
