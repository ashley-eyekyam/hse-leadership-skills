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
