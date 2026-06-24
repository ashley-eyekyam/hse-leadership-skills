"""D-03 — regression for the de-id phone-leak precision post-filter.

`graders.deid._has_phone_leak` is a precision post-filter over the LOOSE
`_PHONE_RE` candidate generator. It must:
  - NOT flag ISO-8601 dates ("2026-06-24") or dotted CFR/IEEE/NFPA citations
    ("29.1926.501", "1584.2018", "70E.130") — so a clean golden does not
    false-fail the non-waivable de-id gate; and
  - STILL flag a real phone number ("Phone 555-867-5309", 10 digits + cue) — so
    a genuine leak trips the gate (the leak is non-waivable; T-17-02).

Both directions are locked here, end-to-end through `grade_deid` (the de-id gate
the runner calls), not just the helper, so the residual-identifier routing is
covered too.

sys.path is wired to scripts/ so `from graders.deid import ...` resolves the
package the way run_evals.py imports it at runtime, regardless of invoking cwd.
"""

import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

REPO = SCRIPTS.parent
PHONE_FIXTURES = REPO / "scripts" / "graders" / "fixtures"
CHECKLIST = REPO / "references" / "deid-checklist.md"

CLEAN = (PHONE_FIXTURES / "deid_phone_clean.md").read_text(encoding="utf-8")
SEEDED = (PHONE_FIXTURES / "deid_phone_seeded.md").read_text(encoding="utf-8")


def _grade(text):
    from graders.deid import grade_deid

    checklist = CHECKLIST if CHECKLIST.exists() else None
    return grade_deid(text, checklist)


def test_phone_filter_clean_golden_does_not_hard_fail():
    """ISO dates + dotted CFR/IEEE/NFPA citations are NOT phone leaks."""
    from graders.deid import _has_phone_leak

    assert _has_phone_leak(CLEAN) is False
    verdict = _grade(CLEAN)
    assert verdict["auto_fail"] is False
    # The residual-identifier reasons must not mention a phone number.
    assert all("phone" not in r.lower() for r in verdict["reasons"])


def test_phone_filter_seeded_leak_hard_fails():
    """A real 10-digit number with a phone cue MUST trip the de-id gate."""
    from graders.deid import _has_phone_leak

    assert _has_phone_leak(SEEDED) is True
    verdict = _grade(SEEDED)
    assert verdict["auto_fail"] is True
    assert any("phone" in r.lower() for r in verdict["reasons"])
