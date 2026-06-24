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
# WR-03 (14-REVIEW / P17 17-07): include the HAZ → hazard-library mapping so a fixture
# citing a KB-HAZ-* id resolves to its folder instead of erroring "unknown folder prefix"
# — mirrors the sibling test_kb_registry.FOLDER_ID_PREFIX which already carries it.
PREFIX_FOLDER = {
    "REG": "regulatory",
    "STD": "standards",
    "SNIP": "prompt-snippets",
    "DATA": "data-points",
    "RES": "research",
    "HAZ": "hazard-library",
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


def _all_kb_folders() -> tuple:
    """Every KB folder that carries a _registry.yaml, discovered from disk (not a
    hardcoded subset). WR-02 (14-REVIEW / P17 17-07): the never-minted absence
    assertions must scan ALL registries (incl. research/ + hazard-library/) so a
    re-mint into a folder the old hardcoded list omitted can no longer slip through —
    mirrors the registry-level twin in test_kb_registry which iterates the same glob."""
    return tuple(sorted(p.parent.name for p in KB.glob("*/_registry.yaml")))


def test_dryrun():
    skill_text = SKILL.read_text(encoding="utf-8")
    rows = _kb_selection_rows(skill_text)

    # rule 2 — presence: the rows subsection exists and carries real markdown DATA rows.
    # WR-04 (14-REVIEW / P17 17-07): the old `"India" in rows` + `rows.count("|") > 4` check
    # passed on a header-only table plus the bare word "India" in prose. Assert instead that
    # there are >=2 genuine DATA rows — pipe table rows that are neither the header nor the
    # `|---|` separator and that carry actual cell content — so an empty / header-only /
    # garbage kb-selection table hard-fails as intended.
    def _is_data_row(ln: str) -> bool:
        s = ln.strip()
        if not s.startswith("|"):
            return False
        cells = [c.strip() for c in s.strip("|").split("|")]
        # separator row (|---|---|) — all cells are dashes/colons only
        if all(set(c) <= set("-: ") and c for c in cells):
            return False
        # at least one non-empty cell of real content (not just whitespace)
        return any(c for c in cells)

    pipe_rows = [ln for ln in rows.splitlines() if ln.strip().startswith("|")]
    data_rows = [ln for ln in pipe_rows if _is_data_row(ln)]
    # drop the single header row (first data-shaped pipe row) from the count of real rows
    real_data_rows = max(0, len(data_rows) - 1)
    assert real_data_rows >= 2, (
        "kb-selection rows subsection has fewer than 2 markdown data rows "
        f"(found {real_data_rows}) — empty/header-only/garbage table"
    )

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
    for folder in _all_kb_folders():
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


# --- Phase 14-01: the 18 NEW construction + manufacturing KB fragments (rule-9) ---
#
# Every Wave-2/3 CON-/MFG- skill plan depends_on 14-01 and references these IDs by name
# via its kb-selection; this asserts each resolves in its folder's _registry.yaml AND its
# .md file exists on disk (opening with its own ID marker), so no downstream skill hits a
# rule-9 dead-ref / vacuous kb-selection. The id→folder mapping reuses PREFIX_FOLDER
# (REG→regulatory, STD→standards, DATA→data-points, SNIP→prompt-snippets). Each id lands
# in its PREFIX folder (KB-REG-LOLER-BS7121 → regulatory/, like every other KB-REG- id).
CONSTRUCTION_NEW_IDS = [
    "KB-REG-LOLER-BS7121",  # lives in regulatory/ (KB-REG- prefix → regulatory/, resolves via Rule-9)
    "KB-SNIP-CPP-STRUCTURE",
    "KB-SNIP-PCI-CHECKLIST",
    "KB-SNIP-HS-FILE-CONTENT",
    "KB-DATA-LIFT-CATEGORIES",
    "KB-SNIP-TRAFFIC-SEGREGATION",
    "KB-SNIP-CONSTRUCTION-CLAUSE-MAP",
]
MANUFACTURING_NEW_IDS = [
    "KB-REG-OSHA1910-O",
    "KB-STD-ISO12100-14120",
    "KB-SNIP-GUARD-SELECTION",
    "KB-STD-ISO11228",
    "KB-SNIP-ERGO-CONTROLS",
    "KB-REG-OSHA1910-95",
    "KB-STD-ISO1999-9612",
    "KB-SNIP-NOISE-CONTROL-HIERARCHY",
    "KB-REG-OSHA1910-I",
    "KB-SNIP-PPE-MATRIX-LOGIC",
    "KB-SNIP-MANUFACTURING-CLAUSE-MAP",
]

# The folder each new id actually resides in (every id sits in its PREFIX folder; the
# KB-REG-LOLER-BS7121 lifting-regulation map resolves cleanly via regulatory/ like all KB-REG-).
PHASE14_ID_FOLDER = {
    "KB-REG-LOLER-BS7121": "regulatory",
    "KB-SNIP-CPP-STRUCTURE": "prompt-snippets",
    "KB-SNIP-PCI-CHECKLIST": "prompt-snippets",
    "KB-SNIP-HS-FILE-CONTENT": "prompt-snippets",
    "KB-DATA-LIFT-CATEGORIES": "data-points",
    "KB-SNIP-TRAFFIC-SEGREGATION": "prompt-snippets",
    "KB-SNIP-CONSTRUCTION-CLAUSE-MAP": "prompt-snippets",
    "KB-REG-OSHA1910-O": "regulatory",
    "KB-STD-ISO12100-14120": "standards",
    "KB-SNIP-GUARD-SELECTION": "prompt-snippets",
    "KB-STD-ISO11228": "standards",
    "KB-SNIP-ERGO-CONTROLS": "prompt-snippets",
    "KB-REG-OSHA1910-95": "regulatory",
    "KB-STD-ISO1999-9612": "standards",
    "KB-SNIP-NOISE-CONTROL-HIERARCHY": "prompt-snippets",
    "KB-REG-OSHA1910-I": "regulatory",
    "KB-SNIP-PPE-MATRIX-LOGIC": "prompt-snippets",
    "KB-SNIP-MANUFACTURING-CLAUSE-MAP": "prompt-snippets",
}


def test_phase14_new_ids_count():
    """Exactly 18 NEW fragments (7 construction + 11 manufacturing). NOT 21."""
    assert len(CONSTRUCTION_NEW_IDS) == 7
    assert len(MANUFACTURING_NEW_IDS) == 11
    all_ids = CONSTRUCTION_NEW_IDS + MANUFACTURING_NEW_IDS
    assert len(all_ids) == 18
    assert len(set(all_ids)) == 18  # no dupes
    assert set(all_ids) == set(PHASE14_ID_FOLDER)  # folder map covers exactly these


@pytest.mark.parametrize("kid", CONSTRUCTION_NEW_IDS + MANUFACTURING_NEW_IDS)
def test_phase14_new_id_resolves_in_registry_and_on_disk(kid):
    """Each NEW Phase-14 id resolves in its folder's _registry.yaml AND its .md file
    exists on disk, opening with its own ID marker comment (anti-mismatch)."""
    folder = PHASE14_ID_FOLDER[kid]
    assert kid in _registry_ids(folder), f"{kid} not in {folder}/_registry.yaml"
    reg = yaml.safe_load((KB / folder / "_registry.yaml").read_text(encoding="utf-8"))
    entry = next(e for e in reg if e["id"] == kid)
    target = KB / folder / entry["file"]
    assert target.is_file(), f"{kid} file '{entry['file']}' missing in {folder}/"
    assert target.read_text(encoding="utf-8").lstrip().startswith(
        f"<!-- {kid} -->"
    ), f"{target.name} does not open with <!-- {kid} -->"


def test_phase14_cdm2015_carries_schedule3_traffic_row():
    """CON-05: KB-REG-CDM2015 is EXTENDED in place with a Reg 27 + Schedule 3 traffic
    row (same id, same file — no second CDM fragment minted)."""
    text = (KB / "regulatory" / "cdm-2015.md").read_text(encoding="utf-8")
    assert "Schedule 3" in text, "cdm-2015.md must carry the Schedule 3 traffic row"
    assert "Reg 27" in text or "Regulation 27" in text, "cdm-2015.md must cite Reg 27"
    # exactly one CDM fragment exists (no duplicate id)
    cdm_count = sum(
        1 for e in yaml.safe_load((KB / "regulatory" / "_registry.yaml").read_text())
        if e["id"] == "KB-REG-CDM2015"
    )
    assert cdm_count == 1, "exactly one KB-REG-CDM2015 entry must exist"


def test_phase14_clause_maps_carry_the_crosswalk():
    """Both bundle clause-maps carry their axis (D-04/D-06)."""
    con = (KB / "prompt-snippets" / "construction-clause-map.md").read_text(encoding="utf-8")
    for clause in ("Reg 4", "Reg 12", "Reg 27", "LOLER"):
        assert clause in con, f"{clause} missing from construction-clause-map.md"
    mfg = (KB / "prompt-snippets" / "manufacturing-clause-map.md").read_text(encoding="utf-8")
    for token in ("6.1.2", "12100"):
        assert token in mfg, f"{token} missing from manufacturing-clause-map.md"


def test_phase14_ergonomics_scores_fragment_not_authored():
    """D-02: KB-DATA-ERGONOMICS-SCORES is NEVER minted — the ergonomics.py engine is the
    single scores source (a KB copy is a drift surface). Asserted absent from EVERY
    registry and not on disk under either the CONV-1 or legacy id."""
    for folder in _all_kb_folders():
        assert "KB-DATA-ERGONOMICS-SCORES" not in _registry_ids(folder), (
            f"KB-DATA-ERGONOMICS-SCORES must NOT be minted (found in {folder}/)"
        )
        assert "KB-DP-ERGONOMICS-SCORES" not in _registry_ids(folder), (
            f"legacy KB-DP-ERGONOMICS-SCORES must NOT be minted (found in {folder}/)"
        )
    assert not (KB / "data-points" / "ergonomics-scores.md").is_file()


def test_phase14_loto_isolation_snippet_not_authored():
    """RESEARCH reconciliation (D-03 OBE): KB-SNIP-LOTO-ISOLATION is NEVER authored —
    MFG-01 reuses the shipped KB-REG-LOTO. Asserted absent + KB-REG-LOTO resolves."""
    for folder in _all_kb_folders():
        assert "KB-SNIP-LOTO-ISOLATION" not in _registry_ids(folder), (
            f"KB-SNIP-LOTO-ISOLATION must NOT be authored (found in {folder}/)"
        )
    assert "KB-REG-LOTO" in _registry_ids("regulatory"), "KB-REG-LOTO must still resolve (reused by MFG-01)"


# --- Phase 15-01: the 20 NEW utilities-power + healthcare KB fragments (rule-9) --
#
# Every Wave-2/3 UTIL-/HC- skill plan depends_on 15-01 and references these IDs by
# name via its kb-selection; this asserts each resolves in its folder's
# _registry.yaml AND its .md file exists on disk (opening with its own ID marker),
# so no downstream skill hits a rule-9 dead-ref / vacuous kb-selection. The 20 count
# is the BOTH-REUSED figure (OQ1: KB-STD-NFPA70E reused not minted; OQ2:
# KB-REG-WPV-OSHA3148 reused/extended not minted). The id→folder mapping reuses
# PREFIX_FOLDER (REG→regulatory, STD→standards, SNIP→prompt-snippets).
PHASE15_NEW_IDS = [
    # 7 utilities (3 regulatory + 4 prompt-snippets)
    "KB-REG-OSHA1910-269",
    "KB-REG-UK-EAWR",
    "KB-REG-IN-ELECTRICAL",
    "KB-SNIP-DEENERGIZE-FIRST",
    "KB-SNIP-SWITCHING-SEQUENCE",
    "KB-SNIP-LIVE-WORK-JUSTIFICATION",
    "KB-SNIP-UTILITIES-CLAUSE-MAP",
    # 13 healthcare (4 regulatory + 3 standards + 6 prompt-snippets)
    "KB-REG-OSHA-BBP",
    "KB-REG-EU-SHARPS-2010-32",
    "KB-REG-UK-MHOR",
    "KB-REG-IN-BMW2016",
    "KB-STD-IPC-CDC-WHO",
    "KB-STD-SPHM",
    "KB-STD-BIOSAFETY-BMBL-WHO",
    "KB-SNIP-SHARPS-HIERARCHY",
    "KB-SNIP-IPC-PRECAUTIONS",
    "KB-SNIP-TILE-PEOPLE",
    "KB-SNIP-WPV-CONTROLS",
    "KB-SNIP-BIOSAFETY-RA",
    "KB-SNIP-HEALTHCARE-CLAUSE-MAP",
]

# The folder each new id resides in (every id sits in its PREFIX folder; Rule-9 LOCKED:
# KB-REG-*→regulatory/, KB-STD-*→standards/, KB-SNIP-*→prompt-snippets/).
PHASE15_ID_FOLDER = {
    "KB-REG-OSHA1910-269": "regulatory",
    "KB-REG-UK-EAWR": "regulatory",
    "KB-REG-IN-ELECTRICAL": "regulatory",
    "KB-SNIP-DEENERGIZE-FIRST": "prompt-snippets",
    "KB-SNIP-SWITCHING-SEQUENCE": "prompt-snippets",
    "KB-SNIP-LIVE-WORK-JUSTIFICATION": "prompt-snippets",
    "KB-SNIP-UTILITIES-CLAUSE-MAP": "prompt-snippets",
    "KB-REG-OSHA-BBP": "regulatory",
    "KB-REG-EU-SHARPS-2010-32": "regulatory",
    "KB-REG-UK-MHOR": "regulatory",
    "KB-REG-IN-BMW2016": "regulatory",
    "KB-STD-IPC-CDC-WHO": "standards",
    "KB-STD-SPHM": "standards",
    "KB-STD-BIOSAFETY-BMBL-WHO": "standards",
    "KB-SNIP-SHARPS-HIERARCHY": "prompt-snippets",
    "KB-SNIP-IPC-PRECAUTIONS": "prompt-snippets",
    "KB-SNIP-TILE-PEOPLE": "prompt-snippets",
    "KB-SNIP-WPV-CONTROLS": "prompt-snippets",
    "KB-SNIP-BIOSAFETY-RA": "prompt-snippets",
    "KB-SNIP-HEALTHCARE-CLAUSE-MAP": "prompt-snippets",
}


def test_phase15_new_ids_count():
    """Exactly 20 NEW fragments (7 utilities + 13 healthcare). Both reuse targets
    (KB-STD-NFPA70E / KB-REG-WPV-OSHA3148) are NOT counted (OQ1/OQ2 reuse)."""
    assert len(PHASE15_NEW_IDS) == 20
    assert len(set(PHASE15_NEW_IDS)) == 20  # no dupes
    assert set(PHASE15_NEW_IDS) == set(PHASE15_ID_FOLDER)  # folder map covers exactly these


@pytest.mark.parametrize("kid", PHASE15_NEW_IDS)
def test_phase15_new_id_resolves_in_registry_and_on_disk(kid):
    """Each NEW Phase-15 id resolves in its folder's _registry.yaml AND its .md file
    exists on disk, opening with its own ID marker comment (anti-mismatch)."""
    folder = PHASE15_ID_FOLDER[kid]
    assert kid in _registry_ids(folder), f"{kid} not in {folder}/_registry.yaml"
    reg = yaml.safe_load((KB / folder / "_registry.yaml").read_text(encoding="utf-8"))
    entry = next(e for e in reg if e["id"] == kid)
    target = KB / folder / entry["file"]
    assert target.is_file(), f"{kid} file '{entry['file']}' missing in {folder}/"
    assert target.read_text(encoding="utf-8").lstrip().startswith(
        f"<!-- {kid} -->"
    ), f"{target.name} does not open with <!-- {kid} -->"


def test_phase15_clause_maps_carry_the_crosswalk():
    """Both CONV-10 clause-maps carry their axis (utilities: Article 120 / 130.5;
    healthcare: 6.1.2 / PPE)."""
    util = (KB / "prompt-snippets" / "utilities-clause-map.md").read_text(encoding="utf-8")
    for token in ("Article 120", "130.5"):
        assert token in util, f"{token} missing from utilities-clause-map.md"
    hc = (KB / "prompt-snippets" / "healthcare-clause-map.md").read_text(encoding="utf-8")
    for token in ("6.1.2", "PPE"):
        assert token in hc, f"{token} missing from healthcare-clause-map.md"


def test_phase15_india_pointers_route_to_hse_india():
    """India electrical + BMW pointers route to hse-india and leave unverified
    state values as [GAP] (CONV-8; no national form minted)."""
    for fname in ("regulatory/in-electrical.md", "regulatory/in-bmw2016.md"):
        text = (KB / fname).read_text(encoding="utf-8")
        assert "hse-india" in text, f"{fname} must point into hse-india"
        assert "[GAP]" in text, f"{fname} must leave unverified India values as [GAP]"


def test_phase15_arcflash_ieee1584_datapoint_not_authored():
    """D-02: KB-DP-ARCFLASH-IEEE1584 is NEVER minted — the arcflash.py engine is the
    single source of truth for the arc-flash bands (a KB copy is a drift surface).
    Asserted absent from EVERY registry and not on disk under either id form."""
    for folder in _all_kb_folders():
        assert "KB-DP-ARCFLASH-IEEE1584" not in _registry_ids(folder), (
            f"KB-DP-ARCFLASH-IEEE1584 must NOT be minted (found in {folder}/)"
        )
        assert "KB-DATA-ARCFLASH-IEEE1584" not in _registry_ids(folder), (
            f"KB-DATA-ARCFLASH-IEEE1584 must NOT be minted (found in {folder}/)"
        )
    assert not (KB / "data-points" / "arcflash-ieee1584.md").is_file()


def test_phase15_nfpa70e_reg_not_minted():
    """OQ1: KB-REG-NFPA70E is NOT minted — UTIL-01 reuses the shipped KB-STD-NFPA70E
    (standards/nfpa-70e.md). Asserted absent from the regulatory registry + no
    regulatory/nfpa-70e.md; the reused KB-STD-NFPA70E still resolves."""
    assert "KB-REG-NFPA70E" not in _registry_ids("regulatory"), (
        "KB-REG-NFPA70E must NOT be minted (OQ1 — reuse KB-STD-NFPA70E)"
    )
    assert not (KB / "regulatory" / "nfpa-70e.md").is_file()
    assert "KB-STD-NFPA70E" in _registry_ids("standards"), (
        "KB-STD-NFPA70E must still resolve (reused by UTIL-01)"
    )


def test_phase15_wpv_osha3148_reg_not_minted():
    """OQ2: KB-REG-OSHA-WPV-3148 (the transposed id) is NOT minted — HC-04 reuses /
    extends the shipped KB-REG-WPV-OSHA3148 in place. Asserted absent + the existing
    KB-REG-WPV-OSHA3148 still resolves and carries the extended taxonomy."""
    assert "KB-REG-OSHA-WPV-3148" not in _registry_ids("regulatory"), (
        "KB-REG-OSHA-WPV-3148 must NOT be minted (OQ2 — reuse/extend KB-REG-WPV-OSHA3148)"
    )
    assert not (KB / "regulatory" / "osha-wpv-3148.md").is_file()
    assert "KB-REG-WPV-OSHA3148" in _registry_ids("regulatory"), (
        "KB-REG-WPV-OSHA3148 must still resolve (reused/extended by HC-04)"
    )
    # The in-place extension added the type-1–4 taxonomy + Cal/OSHA 8 CCR 3342.
    text = (KB / "regulatory" / "wpv-osha-3148.md").read_text(encoding="utf-8")
    assert "Type 2" in text, "wpv-osha-3148.md must carry the type-1–4 taxonomy"
    assert "3342" in text, "wpv-osha-3148.md must carry the Cal/OSHA 8 CCR 3342 row"


# --- Phase 16-01: the 30 NEW logistics / marine / rail / renewables KB fragments ---
#
# Every Wave-2+ skill plan (16-02..16-12) depends_on 16-01 and references these IDs by
# name via its kb-selection; this asserts each resolves in its folder's _registry.yaml
# AND its .md file exists on disk (opening with its own ID marker), so no downstream
# skill hits a rule-9 dead-ref / vacuous kb-selection. The id→folder mapping reuses the
# Rule-9 PREFIX_FOLDER convention (REG→regulatory, STD→standards, DATA→data-points,
# SNIP→prompt-snippets). The 30 = 26 genuinely-new fragments + 4 bundle clause-maps;
# the REUSE fragments (FMCSA-HOS / OFFSHORE-SCR / ROGS / HAZ-RENEWABLES /
# ROAD-SAFETY-INDICATORS) are NOT counted (asserted in test_p16_negative_mint.py).
PHASE16_NEW_IDS = [
    # 12 regulatory (KB-REG-*)
    "KB-REG-MHE-PIT",
    "KB-REG-IN-MTW",
    "KB-REG-DROPS",
    "KB-REG-PFEER",
    "KB-REG-SOLAS-LSA",
    "KB-REG-IN-OFFSHORE",
    "KB-REG-CSM-RA",
    "KB-REG-LX-TRACKWORKER",
    "KB-REG-IN-RAIL",
    "KB-REG-WAH2005",
    "KB-REG-LONE-WORKING",
    "KB-REG-IN-RENEWABLES",
    # 3 standards (KB-STD-*)
    "KB-STD-EN15635-SEMA",
    "KB-STD-GWO-WAH-RESCUE",
    "KB-STD-BS8484",
    # 3 data-points (KB-DATA-*)
    "KB-DATA-DROPS-IMPACT",
    "KB-DATA-ALCRM-BANDS",
    "KB-DATA-WEATHER-THRESHOLDS",
    # 8 control-logic snippets + 4 bundle clause-maps (KB-SNIP-*)
    "KB-SNIP-FATIGUE-FRMS",
    "KB-SNIP-RACKING-MHE",
    "KB-SNIP-DROPS-SECURING",
    "KB-SNIP-EER-MUSTER",
    "KB-SNIP-LX-HIERARCHY",
    "KB-SNIP-RESCUE-PLAN",
    "KB-SNIP-CHECKIN-ESCALATION",
    "KB-SNIP-DYNAMIC-RA",
    "KB-SNIP-LOGISTICS-CLAUSE-MAP",
    "KB-SNIP-MARINE-CLAUSE-MAP",
    "KB-SNIP-RAIL-CLAUSE-MAP",
    "KB-SNIP-RENEWABLES-CLAUSE-MAP",
]


def test_phase16_new_ids_count():
    """Exactly 30 NEW fragments (12 regulatory + 3 standards + 3 data-points +
    12 prompt-snippets [8 control-logic + 4 clause-maps])."""
    assert len(PHASE16_NEW_IDS) == 30
    assert len(set(PHASE16_NEW_IDS)) == 30  # no dupes


@pytest.mark.parametrize("kid", PHASE16_NEW_IDS)
def test_phase16_new_id_resolves_in_registry_and_on_disk(kid):
    """Each NEW Phase-16 id resolves in its folder's _registry.yaml (via the Rule-9
    PREFIX_FOLDER map) AND its .md file exists on disk, opening with its own ID marker
    comment (anti-mismatch)."""
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


def test_phase16_clause_maps_carry_the_crosswalk():
    """All 4 CONV-10 bundle clause-maps carry their bundle axis + the current-standard
    + cite-not-reproduce currency notes (SI 2015/398 not SCR 2005; BS 7121-1 2016)."""
    log = (KB / "prompt-snippets" / "logistics-clause-map.md").read_text(encoding="utf-8")
    for token in ("FMCSA", "EN 15635"):
        assert token in log, f"{token} missing from logistics-clause-map.md"
    mar = (KB / "prompt-snippets" / "marine-clause-map.md").read_text(encoding="utf-8")
    assert "2015/398" in mar, "marine clause-map must cite SI 2015/398 as current"
    assert "DROPS" in mar, "marine clause-map must carry the DROPS axis"
    rail = (KB / "prompt-snippets" / "rail-clause-map.md").read_text(encoding="utf-8")
    for token in ("ROGS", "CSM-RA"):
        assert token in rail, f"{token} missing from rail-clause-map.md"
    ren = (KB / "prompt-snippets" / "renewables-clause-map.md").read_text(encoding="utf-8")
    assert "BS 7121-1" in ren, "renewables clause-map must cite BS 7121-1"
    # Must never cite the SUPERSEDED 2006 edition as current — the current edition is
    # 2016. (A disclaimer that names "2006 edition" to reject it is allowed; a positive
    # "BS 7121-1:2006" citation is not.)
    assert "BS 7121-1:2006" not in ren and "BS 7121-1 2006" not in ren, (
        "renewables clause-map must NOT cite the 2006 edition of BS 7121-1 as current"
    )
    assert "2016" in ren, "renewables clause-map must name the current BS 7121-1 (2016) edition"


def test_phase16_offshore_uses_current_si_2015_398_not_scr2005():
    """T-16-01-01: the marine clause-map cites SI 2015/398 as current and qualifies
    SCR 2005 as legacy only (regulatory_citation_accuracy HARD-fail otherwise)."""
    mar = (KB / "prompt-snippets" / "marine-clause-map.md").read_text(encoding="utf-8")
    assert "2015/398" in mar, "current offshore safety-case regime = SI 2015/398"
    # SCR 2005, where mentioned, must be qualified as legacy — never presented as current.
    if "SCR 2005" in mar:
        assert "legacy" in mar.lower(), "SCR 2005 must be qualified as legacy, not current"


def test_phase16_assumed_anchors_flagged_gap():
    """D-03: the four [ASSUMED] licensed/baseline anchors (A1 DROPS bands, A2 ALCRM
    bands, A4 ≈15 m/s wind cut-off) and the NR/L2/OHS/019 issue (A3) carry an explicit
    [GAP] / [ASSUMED] / user-confirmed flag — licensed values are never embedded."""
    drops = (KB / "data-points" / "drops-impact.md").read_text(encoding="utf-8")
    assert "[GAP]" in drops and "A1" in drops, "DROPS bands must be [GAP]/[ASSUMED A1]"
    alcrm = (KB / "data-points" / "alcrm-bands.md").read_text(encoding="utf-8")
    assert "[GAP]" in alcrm and "A2" in alcrm, "ALCRM bands must be [GAP]/[ASSUMED A2]"
    weather = (KB / "data-points" / "weather-thresholds.md").read_text(encoding="utf-8")
    assert "A4" in weather and "7 m/s" in weather, (
        "weather thresholds must flag ≈15 m/s as [ASSUMED A4] and carry the verified 7 m/s anchor"
    )
    lx = (KB / "regulatory" / "lx-trackworker.md").read_text(encoding="utf-8")
    assert "A3" in lx and "[GAP]" in lx, "NR/L2/OHS/019 issue/date must be [GAP]/[ASSUMED A3]"
