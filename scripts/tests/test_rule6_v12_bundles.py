"""SUB-05 — rule-6 resolution of the v1.2 catalog-completion bundle names.

Phase-11 11-06 registered 10 new marketplace bundles additively in
template/metadata-vocab.yaml's `plugin:` list (the SINGLE source of truth for
lint rule 6). This test proves each new name resolves via the linter's OWN
`registered_bundles()` — the same callable rule-6 uses — so a downstream Ph12–16
skill can declare `metadata.plugin: <new-bundle>` and pass lint rule 6.

It also pins the negative (a phantom name does NOT resolve) and a regression
guard that the pre-existing `hse-core` / `hse-all` names still resolve after the
additive edit.

lint_skills.py lives in scripts/ (not scripts/hse_components/), so we insert the
scripts dir on sys.path here — mirroring test_lint_skills.py.
"""

import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent.parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import lint_skills  # noqa: E402  (sys.path wired above)

# The 10 v1.2 bundles registered additively in 11-06 (SUB-05).
V12_BUNDLES = {
    "hse-operations",
    "hse-leadership",
    "hse-construction",
    "hse-manufacturing",
    "hse-utilities-power",
    "hse-healthcare",
    "hse-logistics-transport",
    "hse-marine-offshore",
    "hse-rail",
    "hse-renewables",
}


def test_v12_bundles_registered():
    """Each of the 10 new bundle names resolves via the linter's single source."""
    bundles = lint_skills.registered_bundles()
    missing = V12_BUNDLES - bundles
    assert not missing, f"v1.2 bundles not registered for rule-6: {sorted(missing)}"


def test_phantom_bundle_not_registered():
    """A name that was never registered must NOT resolve (the negative guard)."""
    assert "not-a-bundle" not in lint_skills.registered_bundles()


def test_preexisting_bundles_still_resolve():
    """Regression: the additive edit must not drop the pre-existing names."""
    bundles = lint_skills.registered_bundles()
    assert "hse-core" in bundles
    assert "hse-all" in bundles
