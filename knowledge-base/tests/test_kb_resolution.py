"""A3 AC8 worked dry-run — the rule-9 KB-resolution proof (KB-01).

This is the in-sandbox resolver the §3.11 rule-9 contract describes; A8 implements
the *enforcing* linter in Phase 3. Here it proves the A3 seam CLOSES against the
seeded registries, using the risk-assessment fixture as the worked sample skill:

  rule 9 (path form)  — every `../../knowledge-base/<folder>/<file>.md` referenced
                        in the fixture's kb-selection rows AND in references/_skill-kb.md
                        resolves on disk (paths resolved relative to the referring file);
  rule 9 (ID form)    — every `KB-…` id referenced (incl. KB-STD-ISO45001 via
                        standards/_registry.yaml) exists in the named folder's registry;
  rule 2 (presence)   — the kb-selection rows subsection (below :end) is present and
                        non-empty.

Plain pytest, sandbox-offline. Paths resolve from the repo root.
"""

import re
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parents[2]
KB = REPO / "knowledge-base"
FIXTURE = REPO / "examples" / "risk-assessment"
SKILL = FIXTURE / "SKILL.md"
SKILL_KB = FIXTURE / "references" / "_skill-kb.md"

PATH_RE = re.compile(r"(\.\./)+knowledge-base/[A-Za-z0-9_./-]+\.md")
ID_RE = re.compile(r"KB-[A-Z0-9]+-[A-Z0-9-]+")

# Map an id prefix to the folder whose _registry.yaml must carry it (§3.3).
PREFIX_FOLDER = {
    "REG": "regulatory",
    "STD": "standards",
    "SNIP": "prompt-snippets",
    "DATA": "data-points",
    "RES": "research",
}


def _kb_selection_rows(text: str) -> str:
    """The rows subsection below the kb-selection :end marker (rule-2 presence)."""
    end = text.index("<!-- hse:block:kb-selection:end -->")
    after = text[end:]
    # stop at the next top-level block marker / heading start so we only grab the rows
    nxt = re.search(r"<!-- hse:block:", after[len("<!-- hse:block:kb-selection:end -->"):])
    if nxt:
        after = after[: len("<!-- hse:block:kb-selection:end -->") + nxt.start()]
    return after


def _resolve_path(ref: str, base_file: Path) -> Path:
    """Resolve a `../../knowledge-base/...` reference relative to the referring file."""
    return (base_file.parent / ref).resolve()


def _registry_ids(folder: str) -> set:
    reg = KB / folder / "_registry.yaml"
    return {e["id"] for e in yaml.safe_load(reg.read_text(encoding="utf-8"))}


def test_dryrun():
    skill_text = SKILL.read_text(encoding="utf-8")
    rows = _kb_selection_rows(skill_text)

    # rule 2 — presence: the rows subsection exists and is non-empty (has table rows).
    assert "| India |" in rows or "India" in rows, "kb-selection rows subsection empty/missing"
    assert rows.count("|") > 4, "kb-selection rows subsection has no resolvable rows"

    manifest_text = SKILL_KB.read_text(encoding="utf-8")

    # rule 9 (path form) — every referenced KB path resolves on disk.
    checked_paths = 0
    for src, base in ((rows, SKILL), (manifest_text, SKILL_KB)):
        for m in PATH_RE.finditer(src):
            target = _resolve_path(m.group(0), base)
            assert target.is_file(), f"dead KB path: {m.group(0)} (from {base.name}) -> {target}"
            checked_paths += 1
    assert checked_paths >= 4, f"expected several KB paths to resolve, got {checked_paths}"

    # rule 9 (ID form) — every KB-… id exists in the named folder's registry.
    ids = set(ID_RE.findall(rows)) | set(ID_RE.findall(manifest_text))
    assert "KB-STD-ISO45001" in ids, "fixture must reference KB-STD-ISO45001 (AC8/AC10)"
    assert "KB-REG-IN-STATEFORMS" in ids, "fixture must reference KB-REG-IN-STATEFORMS (India)"
    cache: dict[str, set] = {}
    for kid in ids:
        prefix = kid.split("-")[1]
        folder = PREFIX_FOLDER.get(prefix)
        assert folder, f"id {kid} has unknown folder prefix {prefix}"
        if folder not in cache:
            cache[folder] = _registry_ids(folder)
        assert kid in cache[folder], f"dead KB id: {kid} not in {folder}/_registry.yaml"


def test_iso45001_resolves_via_standards_registry():
    """AC10 — a sample skill resolves KB-STD-ISO45001 via standards/_registry.yaml."""
    assert "KB-STD-ISO45001" in _registry_ids("standards")
    assert (KB / "standards" / "iso-45001.md").is_file()


# --- Phase 12-01: the 19 NEW hse-operations KB fragments resolve (rule-9 root) ----
#
# Every Wave-2/3 OPS skill plan depends_on 12-01 and references these IDs by name; this
# asserts each resolves in its folder's _registry.yaml AND its .md file exists on disk,
# so no downstream skill hits a rule-9 dead-ref / vacuous kb-selection. The id→folder
# mapping reuses the PREFIX_FOLDER convention (DATA→data-points, SNIP→prompt-snippets).
OPS_NEW_IDS = [
    # 8 data-points (KB-DATA-*)
    "KB-DATA-COMPETENCE-LEVELS",
    "KB-DATA-ISO45001-MATURITY",
    "KB-DATA-DRILL-FREQ",
    "KB-DATA-CONTRACTOR-TIERS",
    "KB-DATA-PSYCHOSOCIAL-INDICATORS",
    "KB-DATA-OBLIGATION-FAMILIES",
    "KB-DATA-RTO-RPO-GUIDANCE",
    "KB-DATA-RECORDABILITY-TESTS",
    # 10 method snippets + the bundle clause-map (KB-SNIP-*)
    "KB-SNIP-TNA-METHOD",
    "KB-SNIP-INDUCTION-BASELINE",
    "KB-SNIP-ERP-SCENARIOS",
    "KB-SNIP-PQQ-BANK",
    "KB-SNIP-HSE-MGMT-STANDARDS",
    "KB-SNIP-GAP-PRIORITISATION",
    "KB-SNIP-LEGAL-REGISTER-METHOD",
    "KB-SNIP-SURVEILLANCE-TRIGGERS",
    "KB-SNIP-BIA-METHOD",
    "KB-SNIP-RETURNS-METHOD",
    "KB-SNIP-OPS-CLAUSE-MAP",
]


def test_ops_new_ids_count():
    """Exactly 19 NEW OPS fragments (8 data-points + 11 prompt-snippets)."""
    assert len(OPS_NEW_IDS) == 19
    assert len(set(OPS_NEW_IDS)) == 19  # no dupes


@pytest.mark.parametrize("kid", OPS_NEW_IDS)
def test_ops_new_id_resolves_in_registry_and_on_disk(kid):
    """Each NEW OPS id resolves in its folder registry AND its .md file exists."""
    prefix = kid.split("-")[1]
    folder = PREFIX_FOLDER.get(prefix)
    assert folder, f"id {kid} has unknown folder prefix {prefix}"
    # resolves in the named folder's _registry.yaml
    assert kid in _registry_ids(folder), f"{kid} not in {folder}/_registry.yaml"
    # the .md file the registry row points at exists on disk in that folder
    reg = yaml.safe_load((KB / folder / "_registry.yaml").read_text(encoding="utf-8"))
    entry = next(e for e in reg if e["id"] == kid)
    target = KB / folder / entry["file"]
    assert target.is_file(), f"{kid} file '{entry['file']}' missing in {folder}/"
    # the .md opens with its own ID marker comment (anti-mismatch)
    assert target.read_text(encoding="utf-8").lstrip().startswith(
        f"<!-- {kid} -->"
    ), f"{target.name} does not open with <!-- {kid} -->"


def test_ops_clause_map_carries_the_seven_clause_crosswalk():
    """KB-SNIP-OPS-CLAUSE-MAP (D-10) carries the 7-clause operations cross-walk."""
    text = (KB / "prompt-snippets" / "ops-clause-map.md").read_text(encoding="utf-8")
    for clause in ("6.1.3", "7.2", "7.3", "8.1.4", "8.2", "9.1", "9.1.2"):
        assert clause in text, f"clause {clause} missing from ops-clause-map.md"


def test_ops_india_rows_point_into_hse_india_no_minted_form():
    """India obligation/recordability rows route to hse-india; no national form minted."""
    for fname in ("data-points/obligation-families.md", "data-points/recordability-tests.md"):
        text = (KB / fname).read_text(encoding="utf-8")
        assert "hse-india" in text, f"{fname} must point into hse-india"
        assert "[GAP]" in text, f"{fname} must leave unverified India ids as [GAP]"


# --- Phase 13-01: the 11 NEW hse-leadership KB fragments resolve (rule-9 root) -----
#
# Every Wave-2/3 leadership skill plan depends_on 13-01 and references these IDs by name
# via its kb-selection; this asserts each resolves in its folder's _registry.yaml AND its
# .md file exists on disk, so no downstream skill hits a rule-9 dead-ref / vacuous
# kb-selection. The id→folder mapping reuses PREFIX_FOLDER (DATA→data-points,
# SNIP→prompt-snippets).
LEADERSHIP_NEW_IDS = [
    # 4 data-points (KB-DATA-*)
    "KB-DATA-CULTURE-MATURITY",
    "KB-DATA-BBS-METRICS",
    "KB-DATA-LEADING-INDICATORS",
    "KB-DATA-ROAD-SAFETY-INDICATORS",
    # 7 prompt-snippets (KB-SNIP-*) incl. the bundle clause-map
    "KB-SNIP-LEADERSHIP-CLAUSE-MAP",
    "KB-SNIP-CULTURE-MODELS",
    "KB-SNIP-BBS-METHOD",
    "KB-SNIP-ESG-ASSURANCE",
    "KB-SNIP-POLICY-COMMITMENTS",
    "KB-SNIP-GEMBA-PROMPTS",
    "KB-SNIP-KPI-DESIGN",
]


def test_leadership_new_ids_count():
    """Exactly 11 NEW leadership fragments (4 data-points + 7 prompt-snippets)."""
    assert len(LEADERSHIP_NEW_IDS) == 11
    assert len(set(LEADERSHIP_NEW_IDS)) == 11  # no dupes


@pytest.mark.parametrize("kid", LEADERSHIP_NEW_IDS)
def test_leadership_new_id_resolves_in_registry_and_on_disk(kid):
    """Each NEW leadership id resolves in its folder registry AND its .md file exists,
    opening with its own ID marker comment (anti-mismatch)."""
    prefix = kid.split("-")[1]
    folder = PREFIX_FOLDER.get(prefix)
    assert folder, f"id {kid} has unknown folder prefix {prefix}"
    assert kid in _registry_ids(folder), f"{kid} not in {folder}/_registry.yaml"
    reg = yaml.safe_load((KB / folder / "_registry.yaml").read_text(encoding="utf-8"))
    entry = next(e for e in reg if e["id"] == kid)
    target = KB / folder / entry["file"]
    assert target.is_file(), f"{kid} file '{entry['file']}' missing in {folder}/"
    assert target.read_text(encoding="utf-8").lstrip().startswith(
        f"<!-- {kid} -->"
    ), f"{target.name} does not open with <!-- {kid} -->"


def test_leadership_clause_map_crosswalks_iso45001_5x_9x():
    """KB-SNIP-LEADERSHIP-CLAUSE-MAP (CONV-10) cross-walks ISO 45001 5.1/5.2/5.4/9.1."""
    text = (KB / "prompt-snippets" / "leadership-clause-map.md").read_text(encoding="utf-8")
    for clause in ("5.1", "5.2", "5.4", "9.1"):
        assert clause in text, f"clause {clause} missing from leadership-clause-map.md"


def test_esg_reuses_gri403_no_disclosures_minted():
    """D-02: ESG reuses the shipped KB-STD-ESG-GRI403 (referenced, not duplicated); the
    KB-DP-ESG-DISCLOSURES id is never minted as a fragment or registry entry."""
    assert "KB-STD-ESG-GRI403" in _registry_ids("standards")
    assert not (KB / "data-points" / "esg-disclosures.md").is_file()
    for folder in ("data-points", "prompt-snippets", "standards"):
        assert "KB-DP-ESG-DISCLOSURES" not in _registry_ids(folder), (
            f"KB-DP-ESG-DISCLOSURES must NOT be minted (found in {folder}/)"
        )


def test_culture_maturity_schein_is_gap_rubric_not_bands():
    """D-05: KB-DATA-CULTURE-MATURITY carries a Schein espoused-vs-enacted GAP rubric,
    NOT Schein maturity bands; the literal phrase 'Schein Level 4' never appears."""
    text = (KB / "data-points" / "culture-maturity.md").read_text(encoding="utf-8")
    assert "espoused" in text.lower(), "Schein gap rubric must speak of espoused-vs-enacted"
    assert "Schein Level 4" not in text, "Schein must not be forced into a maturity band"


def test_road_safety_indicators_cite_iso39001_single_home():
    """D-01: KB-DATA-ROAD-SAFETY-INDICATORS is the single home of road-safety KPIs,
    cited to ISO 39001:2012, and cross-references (not computes) fatigue/HOS."""
    text = (KB / "data-points" / "road-safety-indicators.md").read_text(encoding="utf-8")
    assert "39001" in text, "road-safety indicators must cite ISO 39001"
