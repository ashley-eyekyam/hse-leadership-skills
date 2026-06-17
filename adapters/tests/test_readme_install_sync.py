"""Install-sync anti-drift test (Plan 07-03, Unit E — Decision 2 / Pitfall 6).

The README's per-platform install blocks are LIFTED from the emitted
adapters/<platform>/<skill>/INSTALL.md — never hand-authored — so a vendor click-path
move (or a build relayout) cannot silently invalidate a hand-copied README step.

This test proves the README's ChatGPT install block matches the canonical steps in
adapters/chatgpt/risk-assessment/INSTALL.md byte-for-byte (per numbered step), for a
representative platform. If the emitted INSTALL.md changes, this test fails until the
README block is re-lifted (the README install section is regenerated from C's outputs,
not hand-maintained).

Run: python -m pytest adapters/tests/test_readme_install_sync.py -x
"""

import re
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent.parent
README = REPO / "README.md"
INSTALL = REPO / "adapters" / "chatgpt" / "risk-assessment" / "INSTALL.md"


def _numbered_steps(text: str) -> list[str]:
    """Extract the ordered '1. … 2. …' step lines from a markdown block, normalised."""
    steps = []
    for line in text.splitlines():
        m = re.match(r"\s*\d+\.\s+(.*)$", line)
        if m:
            steps.append(" ".join(m.group(1).split()))
    return steps


@pytest.fixture(scope="module")
def readme_text() -> str:
    assert README.exists(), "README.md must exist"
    return README.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def install_text() -> str:
    assert INSTALL.exists(), (
        "adapters/chatgpt/risk-assessment/INSTALL.md must exist (emitted by C / 07-02)"
    )
    return INSTALL.read_text(encoding="utf-8")


def test_chatgpt_install_block_lifted_verbatim(readme_text, install_text):
    """Every numbered step from the emitted ChatGPT INSTALL.md must appear, in order,
    inside the README's ChatGPT install block — proving it was lifted, not improvised."""
    install_steps = _numbered_steps(install_text)
    assert install_steps, "No numbered steps found in the emitted INSTALL.md"

    # Isolate the README's ChatGPT <details> block so we compare like-for-like.
    start = readme_text.find("ChatGPT — Custom GPT")
    assert start != -1, "README is missing the ChatGPT install block heading"
    block = readme_text[start : readme_text.find("</details>", start)]
    readme_steps = _numbered_steps(block)

    assert readme_steps == install_steps, (
        "README ChatGPT install block has drifted from adapters/chatgpt/"
        "risk-assessment/INSTALL.md.\n"
        f"  INSTALL.md steps: {install_steps}\n"
        f"  README block steps: {readme_steps}\n"
        "Re-lift the block from the emitted INSTALL.md (Decision 2 — no hand-authoring)."
    )
