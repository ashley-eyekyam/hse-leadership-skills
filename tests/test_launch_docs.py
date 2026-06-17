"""Launch-doc anchor contract (Plan 07-03, Unit E — Task 2).

Deterministic, stdlib-only checks that the three launch docs carry their required
anchors so they cannot silently regress to placeholders or drift from their purpose:

  * docs/BRANDING.md  — markets the two-file override + scripts the T-402 demo, and
                        points at (does not restate) the A4/A9 schemas (Decision 8).
  * docs/USER_JOURNEYS.md — ships ≥6 situation-first journey cards (D-07).
  * docs/USER_MANUAL.md — de-staled to "Getting Started" with a pointer to USER_JOURNEYS (D-04).

Run: python -m pytest tests/test_launch_docs.py -x
"""

from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
DOCS = REPO / "docs"
BRANDING = DOCS / "BRANDING.md"
JOURNEYS = DOCS / "USER_JOURNEYS.md"
MANUAL = DOCS / "USER_MANUAL.md"


def _read(p: Path) -> str:
    assert p.exists(), f"{p.relative_to(REPO)} must exist"
    return p.read_text(encoding="utf-8")


def test_branding_markets_two_file_override_and_demo():
    text = _read(BRANDING)
    # The two-file override mechanism.
    assert "company-card" in text, "BRANDING.md must reference company-card.yaml (A9 identity file)"
    assert "brand.yaml" in text, "BRANDING.md must reference brand.yaml (A4 visual theme file)"
    # The scripted demo scenario (the T-402 risk-assessment end-to-end).
    assert "T-402" in text, "BRANDING.md must script the T-402 demo-GIF scenario (D-11)"
    # Decision 8: point at the schemas, do not restate them — the Eyekyam palette is present
    # as the default, and it must still be a placeholder-free narrative.
    assert "#2AADA8" in text, "BRANDING.md must document the Eyekyam default palette"
    assert "🚧" not in text, "BRANDING.md must no longer be the A1 placeholder"


def test_user_journeys_has_six_plus_cards():
    text = _read(JOURNEYS)
    headers = [ln for ln in text.splitlines() if ln.startswith("## Journey ")]
    assert len(headers) >= 6, (
        f"USER_JOURNEYS.md must carry ≥6 journey cards (D-07); found {len(headers)}"
    )
    # Each card must carry the D-06 depth markers somewhere in the doc.
    for marker in ("**Situation:**", "**Chain:**", "**Why this order:**", "**Handoffs:**", "**Opening prompts:**"):
        assert marker in text, f"USER_JOURNEYS.md cards must carry the {marker} depth marker (D-06)"


def test_user_manual_destaled_to_getting_started():
    text = _read(MANUAL)
    assert "Getting Started" in text, "USER_MANUAL.md must be relabelled 'Getting Started' (D-04)"
    assert "USER_JOURNEYS.md" in text, "USER_MANUAL.md must point readers to USER_JOURNEYS.md (D-04)"
    assert "Scope of this guide" in text, "USER_MANUAL.md must carry the honest scope note (D-04)"
