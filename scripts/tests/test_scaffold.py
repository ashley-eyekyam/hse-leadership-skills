"""test_scaffold.py — the A10 forge scaffolder is born-conformant (FORGE-01/02).

Proves the load-bearing A10 guarantees with real scaffold runs against the real
template/blocks/* + knowledge-base/ authorities:

- born-conformance: scaffold output lints clean with ZERO hand-edits (D1/AC#1);
- block byte-match: each of the 5 inline regions == template/blocks/* (rule-1, D1);
- standalone fallback: --standalone yields a contract-clean skill (D3/FORGE-02);
- roster pre-seed: roster=flagship-b5 emits the FULL B5 4-agent roster; roster=
  single-thread emits the one-liner (A10 §7, SC-1<->SC-5);
- conditional A7: no components -> no scripts/ (B3); components -> scripts/ symlink+shim;
- refuses exit 0 on dirty output (the self-lint gate);
- path-traversal --name is rejected (T-04-01).

Skills are scaffolded UNDER the real repo skills/ tree (rule-9 KB paths are
location-relative to SKILL.md, so they only resolve there) into a uniquely-named
folder, and removed in teardown. No network, no model calls — pure deterministic.
"""

import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

# scripts/tests/test_scaffold.py -> repo root, forge scripts, lint module
REPO = Path(__file__).resolve().parent.parent.parent
FORGE_SCRIPTS = REPO / "skills" / "hse-skill-forge" / "scripts"
LINT_SCRIPTS = REPO / "scripts"
FIXTURES = Path(__file__).resolve().parent / "fixtures"

for p in (str(FORGE_SCRIPTS), str(LINT_SCRIPTS)):
    if p not in sys.path:
        sys.path.insert(0, p)

import scaffold  # noqa: E402
import lint_skills  # noqa: E402


@pytest.fixture
def answers() -> dict:
    return json.loads((FIXTURES / "probe_answers.json").read_text(encoding="utf-8"))


@pytest.fixture
def scaffolded(request):
    """Scaffold a uniquely-named skill under the real skills/ tree; remove it after.

    Returns a callable: scaffolded(name_suffix, answers, **kw) -> skill_dir.
    """
    created = []

    def _make(name_suffix: str, ans: dict, **kw) -> Path:
        name = f"ztest-{name_suffix}"
        d = scaffold.scaffold_skill(name, ans, force=True, **kw)
        created.append(d)
        return d

    yield _make

    for d in created:
        shutil.rmtree(d, ignore_errors=True)


def test_born_conformant(answers, scaffolded):
    """scaffold output lints clean with zero hand-edits (the self-lint already
    enforced this on scaffold; re-assert via the real linter)."""
    d = scaffolded("born", answers)
    report = lint_skills.validate_skill(d)
    assert report.ok, report.errors


def test_fresh_scaffold_is_born_conformant(answers, scaffolded):
    """FND-06 — a freshly scaffolded skill is born-conformant for Rules 11/12.

    Per research §5.3 + Pitfall 2: WARN alone does not raise scaffold's `_self_lint`
    gate (it gates on report.errors only), so born-conformance must be asserted as
    `report.errors == []` AND zero `rule 11`/`rule 12` warnings. The fresh scaffold
    must also emit references/intake.md + references/sme-review.md and cite both in
    SKILL.md (the elicitation-coverage + SME-sign-off half of D-03)."""
    d = scaffolded("bornconf", answers)

    # (a) both reference files are emitted.
    assert (d / "references" / "intake.md").exists(), "fresh scaffold must emit references/intake.md"
    assert (d / "references" / "sme-review.md").exists(), (
        "fresh scaffold must emit references/sme-review.md"
    )

    # (b) the SKILL.md cites both (lean pointers — rule 11/12 SKILL.md checks).
    body = (d / "SKILL.md").read_text(encoding="utf-8")
    assert "references/intake.md" in body, "SKILL.md must cite references/intake.md"
    assert "references/sme-review.md" in body, "SKILL.md must cite references/sme-review.md"

    # (c) born-conformant: validate via the forge re-export, 0 errors AND
    #     0 rule-11/12 warnings (the HARD-ready bar).
    report = lint_skills.validate_skill(d)
    assert report.errors == [], report.errors
    assert [w for w in report.warnings if w.startswith("rule 11")] == [], (
        "fresh scaffold raised rule-11 warnings: "
        f"{[w for w in report.warnings if w.startswith('rule 11')]}"
    )
    assert [w for w in report.warnings if w.startswith("rule 12")] == [], (
        "fresh scaffold raised rule-12 warnings: "
        f"{[w for w in report.warnings if w.startswith('rule 12')]}"
    )


def test_blocks_byte_match(answers, scaffolded):
    """Each of the 5 inline regions in the output equals template/blocks/* after
    _normalize — proving scaffold COPIES the canonical blocks (rule-1, D1)."""
    d = scaffolded("blocks", answers)
    body = (d / "SKILL.md").read_text(encoding="utf-8")
    for block in lint_skills.INLINE_BLOCKS:
        out_inner = lint_skills._inner_region(body, block)
        canon_inner = lint_skills._inner_region(
            (REPO / "template" / "blocks" / f"{block}.md").read_text(encoding="utf-8"), block
        )
        assert out_inner is not None, f"{block} region missing in scaffold output"
        assert lint_skills._normalize(out_inner) == lint_skills._normalize(canon_inner), (
            f"{block} region drifted from template/blocks/{block}.md"
        )


def test_no_embedded_block_text():
    """scaffold.py embeds NO canonical block bodies — it reads template/blocks/*
    (a second source of truth is the drift risk D1 forbids). The block PROSE must not
    be hard-coded; only the read path may mention template/blocks."""
    src = (FORGE_SCRIPTS / "scaffold.py").read_text(encoding="utf-8")
    assert "template/blocks" in src or "BLOCKS_DIR" in src, "scaffold must read template/blocks/*"
    # The unique deid prose line must NOT be embedded verbatim in scaffold.py.
    assert "PSEUDONYMIZE BY DEFAULT" not in src, "scaffold.py must not embed canonical block text"


def test_standalone_fallback(answers, scaffolded):
    """--standalone (no skill-creator) yields a contract-clean, domain-TODO skill."""
    d = scaffolded("standalone", answers, standalone=True)
    report = lint_skills.validate_skill(d)
    assert report.ok, report.errors
    # The seeded intake STEP is a TODO scaffold (forge never invents domain values).
    body = (d / "SKILL.md").read_text(encoding="utf-8")
    assert "TODO: author this skill's intake question set" in body


def test_flagship_roster_preseed(answers, scaffolded):
    """roster=flagship-b5 pre-seeds the FULL examined B5 4-agent roster below
    orchestration:end (SC-1<->SC-5 coupling, A10 §7)."""
    ans = dict(answers)
    ans["roster"] = "flagship-b5"
    ans["a7_components"] = ["rca", "smart_actions", "incident_rates"]
    d = scaffolded("flagship", ans)
    body = (d / "SKILL.md").read_text(encoding="utf-8")
    below = body.split("hse:block:orchestration:end -->", 1)[1].split(
        "hse:block:report-output:start", 1
    )[0]
    assert "De-identifier" in below
    assert "Critic/QA" in below
    for agent in (
        "Evidence & Timeline",
        "Root-Cause Analyst",
        "Regulatory Reportability Checker",
        "Corrective-Action Drafter",
    ):
        assert agent in below, f"missing fan-out agent {agent!r}"


def test_single_thread_roster(answers, scaffolded):
    """roster=single-thread emits the one-liner (the non-flagship default)."""
    ans = dict(answers)
    ans["roster"] = "single-thread"
    d = scaffolded("single", ans)
    body = (d / "SKILL.md").read_text(encoding="utf-8")
    assert "Single-threaded by design — no subagents." in body


def test_b3_no_scripts_symlink(answers, scaffolded):
    """No A7 components declared -> NO scripts/ dir (the B3 toolbox-talk shape)."""
    ans = dict(answers)
    ans.pop("a7_components", None)
    ans.pop("components", None)
    d = scaffolded("noscripts", ans)
    assert not (d / "scripts").exists(), "B3-shaped skill must have no scripts/ dir"


def test_a7_creates_scripts(answers, scaffolded):
    """A7 components declared -> scripts/ with a verbatim _shim.py + hse_components."""
    ans = dict(answers)
    ans["a7_components"] = ["risk_matrix"]
    d = scaffolded("withscripts", ans)
    assert (d / "scripts" / "_shim.py").exists()
    assert (d / "scripts" / "hse_components").exists()
    # the shim is byte-verbatim with the package copy.
    assert (d / "scripts" / "_shim.py").read_bytes() == (
        REPO / "scripts" / "hse_components" / "_shim.py"
    ).read_bytes()


def test_refuses_exit0_on_dirty(answers, tmp_path, monkeypatch):
    """If the scaffold output does not lint clean, scaffold_skill raises (never a
    silent exit 0). Force drift by pointing the block-copy at a corrupted blocks dir."""
    # Build a corrupted template/blocks by copying the repo template into tmp and
    # mutating deid.md, then repoint scaffold's BLOCKS_DIR at it.
    bad_blocks = tmp_path / "blocks"
    shutil.copytree(REPO / "template" / "blocks", bad_blocks)
    deid = bad_blocks / "deid.md"
    # Mutate INSIDE the marked region so the scaffolded inner region drifts from the
    # real canonical block the self-lint diffs against.
    bad = deid.read_text(encoding="utf-8").replace(
        "Apply this BEFORE you draft anything.", "Apply this DRIFTED.", 1
    )
    deid.write_text(bad, encoding="utf-8")
    monkeypatch.setattr(scaffold, "BLOCKS_DIR", bad_blocks)

    out_root = REPO / "skills"
    name = "ztest-dirty"
    try:
        with pytest.raises(RuntimeError, match="does NOT lint clean"):
            scaffold.scaffold_skill(name, answers, force=True)
    finally:
        shutil.rmtree(out_root / name, ignore_errors=True)


def test_name_traversal_rejected(answers):
    """A path-traversal --name is rejected before any write (T-04-01)."""
    for bad in ("../evil", "Evil", "a/b", "with space"):
        with pytest.raises(ValueError):
            scaffold.scaffold_skill(bad, answers, force=True)


def test_cli_standalone_then_lints(answers):
    """The plan's acceptance command: scaffold --standalone then lint exits 0."""
    name = "ztest-cli"
    out = REPO / "skills" / name
    try:
        r1 = subprocess.run(
            [sys.executable, str(FORGE_SCRIPTS / "scaffold.py"),
             "--name", name, "--answers", str(FIXTURES / "probe_answers.json"),
             "--standalone", "--force"],
            cwd=str(REPO), capture_output=True, text=True,
        )
        assert r1.returncode == 0, r1.stderr
        r2 = subprocess.run(
            [sys.executable, str(LINT_SCRIPTS / "lint_skills.py"), f"skills/{name}"],
            cwd=str(REPO), capture_output=True, text=True,
        )
        assert r2.returncode == 0, r2.stderr + r2.stdout
    finally:
        shutil.rmtree(out, ignore_errors=True)
