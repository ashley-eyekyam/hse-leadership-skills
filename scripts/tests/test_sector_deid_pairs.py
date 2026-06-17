"""test_sector_deid_pairs.py — the CORE-VALUE de-id PAIR leak-catch for sector skills (Plan 06-01, Task 3).

The forge seeds a de-id PAIR (`evals/files/deid-clean.md` + `deid-leak.md`, copied from
`examples/deid-canary/{clean,leak}.md`) into every scaffolded skill — but each skill's eval
CASE wires only the CLEAN fixture, which passes trivially. The SEEDED-LEAK catch is what
proves the non-waivable, CORE-VALUE de-id auto-fail actually fires for that skill.

The 10 legacy B-skills carry hand-authored `test_b*_deid_pair.py` files over their own
bespoke fixtures (e.g. `manual-handling-pii.md`). The 38 NEW sector skills do not, and the
forge does NOT emit a per-skill test. This ONE parametrized test auto-discovers every skill
carrying the forge-named PAIR (`skills/*/evals/files/deid-leak.md`) and, for each, asserts:

  - grade_deid(deid-leak.md).auto_fail is True  (the seeded leak MUST hard-fail), and
  - grade_deid(deid-clean.md).auto_fail is False (the clean MUST pass).

So the `-k deid_pair` verify in plans 02-06 covers every new pack skill the moment it lands
(no per-skill test file is authored for the 38 new skills). A canary smoke case keeps the
file from ever collecting zero tests at Wave-0. Pure deterministic Python: no network, no
model, no key — modelled on test_b1_deid_pair.py.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

# scripts/tests/<this> -> repo/scripts on sys.path for `graders`.
REPO = Path(__file__).resolve().parents[2]
SCRIPTS = REPO / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from graders import grade_deid  # noqa: E402


def _discover_sector_pairs():
    """Auto-discover every skill carrying the forge-seeded PAIR.

    The glob keys on the forge-named `deid-leak.md`; the legacy B-skills use bespoke
    fixture names (`manual-handling-pii.md`, …) and so are NOT picked up here — their
    catch is covered by the hand-authored test_b*_deid_pair.py files. Re-asserting a
    forge-named skill (e.g. hse-skill-forge itself) is harmless and still correct.
    Yields (skill_name, leak_path, clean_path) for pairs whose CLEAN sibling exists.
    """
    pairs = []
    for leak in sorted((REPO / "skills").glob("*/evals/files/deid-leak.md")):
        clean = leak.with_name("deid-clean.md")
        if clean.is_file():
            skill_name = leak.parents[2].name  # skills/<name>/evals/files/deid-leak.md
            pairs.append((skill_name, leak, clean))
    return pairs


_PAIRS = _discover_sector_pairs()


@pytest.mark.parametrize(
    "skill_name,leak,clean",
    _PAIRS,
    ids=[p[0] for p in _PAIRS] or None,
)
def test_sector_deid_pair_leak_caught_clean_passes(skill_name, leak, clean):
    """For each forge-seeded sector skill: the seeded leak hard-fails, the clean passes."""
    leak_verdict = grade_deid(leak.read_text(encoding="utf-8"))
    assert leak_verdict["auto_fail"] is True, (
        f"{skill_name}: seeded de-id LEAK fixture did NOT hard-fail (CORE-VALUE gate breach)"
    )
    assert leak_verdict["reasons"], f"{skill_name}: auto_fail with no reason is not a real catch"

    clean_verdict = grade_deid(clean.read_text(encoding="utf-8"))
    assert clean_verdict["auto_fail"] is False, (
        f"{skill_name}: clean fixture false-positived: {clean_verdict['reasons']}"
    )


def test_canary_smoke_pair():
    """Wave-0 floor: the discovery+assertion logic always collects at least one case,
    proven directly against the examples/deid-canary baseline the forge copies from."""
    canary = REPO / "examples" / "deid-canary"
    leak = grade_deid((canary / "leak.md").read_text(encoding="utf-8"))
    clean = grade_deid((canary / "clean.md").read_text(encoding="utf-8"))
    assert leak["auto_fail"] is True and leak["reasons"], "canary leak must hard-fail"
    assert clean["auto_fail"] is False, "canary clean must pass"
