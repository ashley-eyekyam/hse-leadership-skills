"""Launch-asset presence + validity contract (Plan 07-03, Unit E — Task 3).

Deterministic, stdlib-only checks (xml.dom.minidom + glob + os) that the visual assets
and the community playbook are in place and in-repo:

  * docs/assets/architecture.svg parses as valid XML (the A2→A3→A7+A4→B/D→C layering).
  * ≥2 de-identified flagship screenshot image files exist in docs/assets/
    (besides architecture.svg), referenced by in-repo relative paths.
  * .github/ISSUE_TEMPLATE/ exists with the new-skill-proposal template, and the
    good-first-issue label convention is documented (the community funnel seed).

Visual-fidelity sign-off (does the diagram read legibly? are the screenshots truly
de-identified?) remains the owner's manual check per 07-VALIDATION.md — this test asserts
the FILES + structure, not the pixels.

Run: python -m pytest tests/test_launch_assets.py -x
"""

import glob
import os
from pathlib import Path
from xml.dom import minidom

import pytest

REPO = Path(__file__).resolve().parent.parent
ASSETS = REPO / "docs" / "assets"
ARCH = ASSETS / "architecture.svg"
ISSUE_TEMPLATE_DIR = REPO / ".github" / "ISSUE_TEMPLATE"


def test_architecture_svg_is_valid_xml():
    assert ARCH.exists(), "docs/assets/architecture.svg must exist"
    # Parses without raising → well-formed XML; root must be <svg>.
    doc = minidom.parse(str(ARCH))
    assert doc.documentElement.tagName == "svg", "architecture.svg root element must be <svg>"
    # The Eyekyam teal palette must appear (Decision 7 — reuse the brand palette).
    text = ARCH.read_text(encoding="utf-8")
    assert "#2AADA8" in text, "architecture.svg must use the Eyekyam teal palette"


def test_at_least_two_flagship_screenshots_present():
    """≥2 screenshot image files in docs/assets/, besides architecture.svg."""
    assert ASSETS.is_dir(), "docs/assets/ must exist"
    image_exts = ("*.svg", "*.png", "*.jpg", "*.jpeg", "*.gif", "*.webp")
    images = []
    for ext in image_exts:
        images.extend(glob.glob(os.path.join(str(ASSETS), ext)))
    screenshots = [p for p in images if os.path.basename(p) != "architecture.svg"]
    assert len(screenshots) >= 2, (
        f"docs/assets/ must carry ≥2 flagship screenshots besides architecture.svg; "
        f"found {[os.path.basename(p) for p in screenshots]}"
    )


def test_screenshots_referenced_by_relative_path_in_readme():
    """The README references the screenshots by in-repo relative paths (no external CDN)."""
    readme = (REPO / "README.md").read_text(encoding="utf-8")
    assert "docs/assets/screenshot-risk-assessment" in readme, (
        "README must reference the flagship screenshots by in-repo relative path"
    )
    assert "docs/assets/architecture.svg" in readme, (
        "README must reference architecture.svg by in-repo relative path"
    )
    # No external CDN hosting of the in-repo visual assets.
    assert "https://cdn." not in readme, "Visual assets must be in-repo, not on an external CDN"


def test_community_playbook_seeded():
    """The new-skill-proposal template + good-first-issue convention seed the funnel."""
    assert ISSUE_TEMPLATE_DIR.is_dir(), ".github/ISSUE_TEMPLATE/ must exist"
    assert (ISSUE_TEMPLATE_DIR / "new_skill.md").exists(), (
        "the new-skill-proposal issue template must be present"
    )
    labels = REPO / ".github" / "LABELS.md"
    assert labels.exists(), ".github/LABELS.md (label convention) must document the funnel"
    label_text = labels.read_text(encoding="utf-8")
    assert "good first issue" in label_text, "the good-first-issue convention must be documented"
