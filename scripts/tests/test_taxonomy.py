"""FND-01 (+ FND-02 cross-check) — the elicitation-dimension taxonomy loader.

Asserts the loader contract built in plans 08-01 / 08-05 over
`knowledge-base/elicitation-taxonomy.yaml`:

  * `_taxonomy_ids(REPO)` returns all 13 ELI-* ids, including the 3 universal
    (ELI-SCOPE / ELI-SUBJECT / ELI-OUTPUT);
  * `_taxonomy_universals(REPO)` returns EXACTLY those 3 universal ids;
  * the difference (the conditionals) has 10 ids — documenting the
    spec-prose-vs-file discrepancy: the YAML file carries 10 `universal: false`
    entries (the header comment's "9 conditional" prose is stale; the file is
    the single source of truth);
  * the YAML parses as a 13-item list, each entry carrying exactly
    `{id, name, definition, universal}`;
  * `resolve_kb_id("KB-SNIP-SME-QA", REPO)` is True (FND-02 rule-9 cross-check).

This test file asserts behavior; it NEVER edits `lint_skills.py` or the taxonomy
file. `lint_skills.py` lives in `scripts/` (not `scripts/hse_components/`), so we
insert the scripts dir on sys.path here exactly as `test_lint_skills.py` does.
"""

import sys
from pathlib import Path

import pytest
import yaml

SCRIPTS_DIR = Path(__file__).resolve().parent.parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

REPO = SCRIPTS_DIR.parent
TAXONOMY_FILE = REPO / "knowledge-base" / "elicitation-taxonomy.yaml"

lint_skills = pytest.importorskip(
    "lint_skills", reason="scripts/lint_skills.py not implemented yet (plan 08-05)"
)

UNIVERSALS = {"ELI-SCOPE", "ELI-SUBJECT", "ELI-OUTPUT"}


# --- the taxonomy loader contract --------------------------------------------------

def test_taxonomy_ids_returns_all_thirteen():
    """`_taxonomy_ids(REPO)` returns all 13 ELI-* ids, ⊇ the 3 universal."""
    ids = lint_skills._taxonomy_ids(REPO)
    assert len(ids) == 13, f"expected 13 ELI-* ids, got {len(ids)}: {sorted(ids)}"
    assert UNIVERSALS <= ids, "the 3 universal dims must be present"


def test_taxonomy_universals_are_exactly_the_three():
    """`_taxonomy_universals(REPO)` returns EXACTLY the 3 universal ids."""
    assert lint_skills._taxonomy_universals(REPO) == UNIVERSALS


def test_conditionals_are_ten():
    """The difference (all ids minus universals) is 10 conditional dims.

    Documents the spec-prose-vs-file discrepancy: the YAML has 10
    `universal: false` entries (the header-comment '9 conditional' prose is
    stale; the FILE is the single source of truth the loader reads)."""
    all_ids = lint_skills._taxonomy_ids(REPO)
    universals = lint_skills._taxonomy_universals(REPO)
    conditionals = all_ids - universals
    assert len(conditionals) == 10, (
        f"expected 10 conditional dims, got {len(conditionals)}: {sorted(conditionals)}"
    )


# --- the file shape ----------------------------------------------------------------

def test_taxonomy_file_shape_is_valid():
    """The YAML parses as a 13-item list, each entry carrying exactly
    `{id, name, definition, universal}`."""
    data = yaml.safe_load(TAXONOMY_FILE.read_text(encoding="utf-8"))
    assert isinstance(data, list), "taxonomy file must be a YAML list"
    assert len(data) == 13, f"expected 13 entries, got {len(data)}"
    required = {"id", "name", "definition", "universal"}
    for entry in data:
        assert isinstance(entry, dict), f"each entry must be a mapping: {entry!r}"
        assert set(entry.keys()) == required, (
            f"entry {entry.get('id', '?')!r} keys {set(entry.keys())} != {required}"
        )
        assert isinstance(entry["universal"], bool), (
            f"entry {entry['id']!r} 'universal' must be a bool"
        )


# --- FND-02 cross-check ------------------------------------------------------------

def test_kb_snip_sme_qa_resolves():
    """`resolve_kb_id('KB-SNIP-SME-QA', REPO)` is True under rule 9 (FND-02)."""
    assert lint_skills.resolve_kb_id("KB-SNIP-SME-QA", REPO) is True
