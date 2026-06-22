"""Persistent DEID-01/02/03 observable contract (A5 → A8).

This is the durable contract test the A8 quality harness keys off in Phase 3 —
NOT a one-shot inline check. It re-asserts, over the on-disk artifacts:

  (i)   the canonical deid block is finalized (five step tokens, no PLACEHOLDER);
  (ii)  the `hse:block:deid` marked region is byte-identical across
        template/blocks/deid.md, template/SKILL.md, and the fixture SKILL.md
        (the anti-drift contract — manual byte-sync until forge --sync, Phase 4);
  (iii) references/deid-checklist.md enumerates the 18 HIPAA Safe-Harbor
        identifiers + HSE addendum, has secondary suppression, the 3-jurisdiction
        mechanism tokens, and no fabricated statute body;
  (iv)  the re-identification-key separation rule appears in BOTH the deid block
        step 2 AND checklist §7;
  (v)   the fixture checklist is a real copy of the canonical (no placeholder).

Plain pytest, sandbox-offline, no framework config — mirrors the
assets/report-engine/tests style. Paths resolve relative to the repo root so the
suite runs from any working directory.
"""

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

BLOCK = REPO / "template" / "blocks" / "deid.md"
TEMPLATE_SKILL = REPO / "template" / "SKILL.md"
FIXTURE_SKILL = REPO / "examples" / "risk-assessment" / "SKILL.md"
CHECKLIST = REPO / "references" / "deid-checklist.md"
FIXTURE_CHECKLIST = REPO / "examples" / "risk-assessment" / "references" / "deid-checklist.md"
ARCHETYPE = REPO / "knowledge-base" / "prompt-snippets" / "deidentifier-archetype.md"

DEID_REGION_RE = re.compile(
    r"<!-- hse:block:deid:start -->.*?<!-- hse:block:deid:end -->", re.S
)

STEP_TOKENS = [
    "DETECT & FLAG",
    "PSEUDONYMIZE BY DEFAULT",
    "AGGREGATE SMALL NUMBERS",
    "WARN BEFORE WIDE DISTRIBUTION",
    "MINIMIZE & LIMIT PURPOSE",
]


def _read(p):
    return p.read_text(encoding="utf-8")


def _region(p):
    m = DEID_REGION_RE.search(_read(p))
    assert m, f"no hse:block:deid marked region in {p}"
    return m.group(0)


# (i) canonical block finalized -------------------------------------------------

def test_block_has_all_five_step_tokens():
    blk = _read(BLOCK)
    for tok in STEP_TOKENS:
        assert tok in blk, f"deid block missing step token: {tok}"


def test_block_has_no_placeholder():
    assert "PLACEHOLDER" not in _read(BLOCK), "deid block still has PLACEHOLDER"


def test_block_is_pseudonymize_by_default():
    # Active default (D-03), not the softened "offer".
    assert "PSEUDONYMIZE BY DEFAULT" in _read(BLOCK)


# (ii) anti-drift byte-sync -----------------------------------------------------

def test_deid_region_byte_identical_across_block_and_both_skills():
    rb = _region(BLOCK)
    rt = _region(TEMPLATE_SKILL)
    rf = _region(FIXTURE_SKILL)
    assert rb == rt, "template/SKILL.md deid region drifted from blocks/deid.md"
    assert rb == rf, "fixture SKILL.md deid region drifted from blocks/deid.md"


def test_skill_regions_have_no_placeholder():
    assert "PLACEHOLDER" not in _region(TEMPLATE_SKILL)
    assert "PLACEHOLDER" not in _region(FIXTURE_SKILL)


# (iii) checklist substance -----------------------------------------------------

def test_checklist_enumerates_18_hipaa_identifiers():
    c = _read(CHECKLIST)
    # 18 enumerated list items in the scrub-checklist section (1. .. 18.).
    numbered = re.findall(r"(?m)^\d+\.\s", c)
    assert len(numbered) >= 18, f"expected >=18 enumerated identifiers, found {len(numbered)}"


def test_checklist_has_hse_addendum():
    c = _read(CHECKLIST)
    assert "HSE addendum" in c
    assert "Aadhaar" in c, "HSE addendum must include Aadhaar / national-ID"


def test_checklist_has_small_cell_and_secondary_suppression():
    c = _read(CHECKLIST)
    assert "secondary suppression" in c
    # <5 small-cell rule present (either "5" threshold wording).
    assert "fewer than 5" in c or "< 5" in c or "<5" in c


def test_checklist_has_three_jurisdiction_mechanism_tokens():
    c = _read(CHECKLIST)
    for tok in ["29 CFR 1904.29", "Art. 9", "DPDP"]:
        assert tok in c, f"checklist missing jurisdiction mechanism token: {tok}"


def test_checklist_quickref_is_mechanism_only_no_fabricated_statute():
    # Guard against a reproduced statute body. The quick-ref must point at
    # mechanisms, not quote statutory text. Flag obvious statute-body markers.
    c = _read(CHECKLIST).lower()
    fabricated_markers = [
        "section 1 of the",
        "shall mean",
        "hereinafter referred to as",
        "provided that nothing in this",
    ]
    for m in fabricated_markers:
        assert m not in c, f"checklist appears to reproduce statute text: {m!r}"


# (iv) re-id key separation rule in BOTH block step 2 AND checklist §7 ----------

def test_reid_key_separation_rule_in_block_and_checklist():
    blk = _read(BLOCK)
    chk = _read(CHECKLIST)
    # Block step 2: separate key, never in the document.
    assert "SEPARATE re-identification key" in blk
    assert "Never put the key" in blk
    # Checklist §7: separate artifact, never embedded.
    assert "Re-identification key handling" in chk
    assert "never" in chk.lower() and "embedded" in chk.lower()


# (v) fixture checklist is a real copy of the canonical ------------------------

def test_fixture_checklist_is_real_copy_no_placeholder():
    assert FIXTURE_CHECKLIST.exists(), "fixture deid-checklist missing"
    assert not FIXTURE_CHECKLIST.is_symlink(), "fixture checklist must be a real copy, not a symlink"
    f = _read(FIXTURE_CHECKLIST)
    assert "placeholder" not in f.lower(), "fixture checklist still a placeholder"
    assert "secondary suppression" in f
    # Byte-identical real copy of the canonical.
    assert f == _read(CHECKLIST), "fixture checklist is not a verbatim copy of the canonical"


# archetype handed to A6 -------------------------------------------------------

def test_archetype_runs_first_and_returns_key_separately():
    a = _read(ARCHETYPE)
    assert "Runs FIRST" in a or "runs first" in a.lower()
    assert "SEPARATE" in a.upper() or "separate" in a
    assert "tools" in a.lower() and "none" in a.lower(), "archetype must declare no tools"


# =============================================================================
# Phase-14 / MFG-02 ergonomics-assessment de-id fixture-PAIR registration.
#
# Skill-scoped section appended by plan 14-02 (do not reorder/remove the canonical
# contract assertions above, nor any other skill's appended section). It registers
# the ergonomics-assessment de-identification PAIR against the SAME deterministic
# de-id grader the whole pack's non-waivable privacy gate keys off, mirroring the
# scripts/tests/test_b*_deid_pair.py precedent:
#   - the seeded-leak negative (evals/files/ergonomics-leak.md) — a named worker +
#     a reported back-injury / medical-fitness note + a phone + an embedded re-id key
#     + a <5 MSD-injury cell — MUST auto_fail (the gate is live), and
#   - the paired clean positive (evals/files/ergonomics-clean.md), wired into the
#     skill's eval CASE, MUST NOT false-positive (the per-skill gate is not spuriously
#     hard-failed).
# Pure deterministic Python: no network, no model, no key.
# =============================================================================

import sys as _ergo_sys  # noqa: E402

_ERGO_SCRIPTS = REPO / "scripts"
if str(_ERGO_SCRIPTS) not in _ergo_sys.path:
    _ergo_sys.path.insert(0, str(_ERGO_SCRIPTS))

from graders import grade_deid as _ergo_grade_deid  # noqa: E402

_ERGO_FILES = REPO / "skills" / "ergonomics-assessment" / "evals" / "files"
_ERGO_LEAK = _ERGO_FILES / "ergonomics-leak.md"
_ERGO_CLEAN = _ERGO_FILES / "ergonomics-clean.md"


def test_ergonomics_seeded_leak_fixture_is_caught():
    """The seeded-leak negative MUST trip the deterministic de-id auto-fail (gate is live)."""
    verdict = _ergo_grade_deid(_ERGO_LEAK.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is True, "ergonomics-assessment seeded-leak fixture did NOT hard-fail"
    assert verdict["reasons"], "auto_fail with no reason is not a real catch"


def test_ergonomics_clean_fixture_passes():
    """The paired clean positive must NOT false-positive (no spurious per-skill hard-fail)."""
    verdict = _ergo_grade_deid(_ERGO_CLEAN.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is False, (
        f"ergonomics-assessment clean fixture false-positived: {verdict['reasons']}"
    )


# =============================================================================
# Phase-14 / MFG-03 noise-exposure-health-surveillance de-id fixture-PAIR registration.
#
# Skill-scoped section appended by plan 14-03 (do not reorder/remove the canonical
# contract assertions above, nor the MFG-02 ergonomics section, nor any other skill's
# appended section). This is the STRICTEST de-id tier in the phase: audiometric /
# standard-threshold-shift (STS) results are special-category health data. It registers
# the noise-exposure-health-surveillance de-identification PAIR against the SAME
# deterministic de-id grader the whole pack's non-waivable privacy gate keys off:
#   - the seeded-leak negative (evals/files/noise-leak.md) — a named worker + a reported
#     audiometric STS / NIHL result + a phone + an embedded re-id key + a <5 audiometric
#     cell — MUST auto_fail (the gate is live), and the small-cell <5 suppression catch
#     is asserted EXPLICITLY (T-14-03-SC2 — the strictest-tier requirement), and
#   - the paired clean positive (evals/files/noise-clean.md), wired into the skill's eval
#     CASE, MUST NOT false-positive (the per-skill gate is not spuriously hard-failed).
# Pure deterministic Python: no network, no model, no key.
# =============================================================================

import sys as _noise_sys  # noqa: E402

_NOISE_SCRIPTS = REPO / "scripts"
if str(_NOISE_SCRIPTS) not in _noise_sys.path:
    _noise_sys.path.insert(0, str(_NOISE_SCRIPTS))

from graders import grade_deid as _noise_grade_deid  # noqa: E402

_NOISE_FILES = REPO / "skills" / "noise-exposure-health-surveillance" / "evals" / "files"
_NOISE_LEAK = _NOISE_FILES / "noise-leak.md"
_NOISE_CLEAN = _NOISE_FILES / "noise-clean.md"


def test_noise_seeded_leak_fixture_is_caught():
    """The seeded-leak negative MUST trip the deterministic de-id auto-fail (gate is live)."""
    verdict = _noise_grade_deid(_NOISE_LEAK.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is True, "noise seeded-leak fixture did NOT hard-fail"
    assert verdict["reasons"], "auto_fail with no reason is not a real catch"


def test_noise_seeded_leak_small_cell_suppression_caught():
    """STRICTEST TIER (T-14-03-SC2): the sub-5 audiometric breakdown MUST be caught as a
    small-cell leak — the <5 STS suppression rule is the noise skill's defining de-id gate."""
    verdict = _noise_grade_deid(_NOISE_LEAK.read_text(encoding="utf-8"))
    assert verdict["conditions"]["no_small_cell"] is False, (
        "noise seeded-leak <5 audiometric cell was NOT caught — small-cell suppression gate is dead"
    )
    assert any("small-cell" in r for r in verdict["reasons"]), (
        "the <5 small-cell leak is not among the auto_fail reasons"
    )


def test_noise_clean_fixture_passes():
    """The paired clean positive must NOT false-positive (no spurious per-skill hard-fail)."""
    verdict = _noise_grade_deid(_NOISE_CLEAN.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is False, (
        f"noise clean fixture false-positived: {verdict['reasons']}"
    )


# =============================================================================
# Phase-14 / MFG-04 ppe-matrix de-id fixture-PAIR registration.
#
# Skill-scoped section appended by plan 14-04 (do not reorder/remove the canonical
# contract assertions above, nor the MFG-02 ergonomics section, nor the MFG-03 noise
# section, nor any other skill's appended section). ppe-matrix handles respiratory
# medical-clearance / fitness-for-respirator notes — GDPR Art. 9 / India DPDP
# special-category health data. It registers the ppe-matrix de-identification PAIR
# against the SAME deterministic de-id grader the whole pack's non-waivable privacy
# gate keys off:
#   - the seeded-leak negative (evals/files/ppe-leak.md) — a named worker + a reported
#     respiratory medical-clearance / fitness note + a phone + an embedded re-id key +
#     a <5 respiratory-clearance illness/injury cell — MUST auto_fail (the gate is live), and
#   - the paired clean positive (evals/files/ppe-clean.md), wired into the skill's eval
#     CASE, MUST NOT false-positive (the per-skill gate is not spuriously hard-failed).
# Pure deterministic Python: no network, no model, no key.
# =============================================================================

import sys as _ppe_sys  # noqa: E402

_PPE_SCRIPTS = REPO / "scripts"
if str(_PPE_SCRIPTS) not in _ppe_sys.path:
    _ppe_sys.path.insert(0, str(_PPE_SCRIPTS))

from graders import grade_deid as _ppe_grade_deid  # noqa: E402

_PPE_FILES = REPO / "skills" / "ppe-matrix" / "evals" / "files"
_PPE_LEAK = _PPE_FILES / "ppe-leak.md"
_PPE_CLEAN = _PPE_FILES / "ppe-clean.md"


def test_ppe_matrix_seeded_leak_fixture_is_caught():
    """The seeded-leak negative MUST trip the deterministic de-id auto-fail (gate is live)."""
    verdict = _ppe_grade_deid(_PPE_LEAK.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is True, "ppe-matrix seeded-leak fixture did NOT hard-fail"
    assert verdict["reasons"], "auto_fail with no reason is not a real catch"


def test_ppe_matrix_clean_fixture_passes():
    """The paired clean positive must NOT false-positive (no spurious per-skill hard-fail)."""
    verdict = _ppe_grade_deid(_PPE_CLEAN.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is False, (
        f"ppe-matrix clean fixture false-positived: {verdict['reasons']}"
    )


# =============================================================================
# Phase-14 / MFG-01 machine-guarding-assessment de-id fixture-PAIR registration.
#
# Skill-scoped section appended by plan 14-05 (do not reorder/remove the canonical
# contract assertions above, nor the MFG-02 ergonomics section, nor the MFG-03 noise
# section, nor the MFG-04 ppe-matrix section, nor any other skill's appended section).
# machine-guarding-assessment is a LOW-PII / asset-level skill, but a guarding assessment
# routinely cites a PRIOR AMPUTATION / CRUSH INCIDENT on the machine — and a named injured
# operator from that incident is GDPR Art. 9 / India DPDP special-category health data. It
# registers the machine-guarding de-identification PAIR against the SAME deterministic de-id
# grader the whole pack's non-waivable privacy gate keys off:
#   - the seeded-leak negative (evals/files/guarding-leak.md) — a named operator from a prior
#     amputation incident + a phone + an embedded re-id key + a <5 amputation/crush injury cell —
#     MUST auto_fail (the gate is live), and
#   - the paired clean positive (evals/files/guarding-clean.md), wired into the skill's eval CASE,
#     MUST NOT false-positive (the per-skill gate is not spuriously hard-failed).
# Pure deterministic Python: no network, no model, no key.
# =============================================================================

import sys as _guard_sys  # noqa: E402

_GUARD_SCRIPTS = REPO / "scripts"
if str(_GUARD_SCRIPTS) not in _guard_sys.path:
    _guard_sys.path.insert(0, str(_GUARD_SCRIPTS))

from graders import grade_deid as _guard_grade_deid  # noqa: E402

_GUARD_FILES = REPO / "skills" / "machine-guarding-assessment" / "evals" / "files"
_GUARD_LEAK = _GUARD_FILES / "guarding-leak.md"
_GUARD_CLEAN = _GUARD_FILES / "guarding-clean.md"


def test_machine_guarding_seeded_leak_fixture_is_caught():
    """The seeded-leak negative MUST trip the deterministic de-id auto-fail (gate is live)."""
    verdict = _guard_grade_deid(_GUARD_LEAK.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is True, "machine-guarding seeded-leak fixture did NOT hard-fail"
    assert verdict["reasons"], "auto_fail with no reason is not a real catch"


def test_machine_guarding_clean_fixture_passes():
    """The paired clean positive must NOT false-positive (no spurious per-skill hard-fail)."""
    verdict = _guard_grade_deid(_GUARD_CLEAN.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is False, (
        f"machine-guarding clean fixture false-positived: {verdict['reasons']}"
    )


# =============================================================================
# Phase-14 / CON-01 construction-phase-plan de-id fixture-PAIR registration.
#
# Skill-scoped section appended by plan 14-06 (do not reorder/remove the canonical
# contract assertions above, nor the MFG-02 ergonomics section, nor the MFG-03 noise
# section, nor the MFG-04 ppe-matrix section, nor the MFG-01 machine-guarding section,
# nor any other skill's appended section). construction-phase-plan (the CDM 2015 Reg 12
# Construction Phase Plan) is a DISTRIBUTED, site-wide document, and a CPP routinely
# cites a PRIOR FALL-FROM-HEIGHT / WORK-AT-HEIGHT NEAR-MISS — a named injured operative
# from that incident is GDPR Art. 9 / India DPDP special-category health data. It
# registers the construction-phase-plan de-identification PAIR against the SAME
# deterministic de-id grader the whole pack's non-waivable privacy gate keys off:
#   - the seeded-leak negative (evals/files/construction-phase-leak.md) — a named operative
#     from a prior fall-from-height near-miss + a phone + an embedded re-id key + a <5
#     fall-injury cell — MUST auto_fail (the gate is live), and
#   - the paired clean positive (evals/files/construction-phase-clean.md), wired into the
#     skill's eval CASE, MUST NOT false-positive (the per-skill gate is not spuriously
#     hard-failed) — proving the named-DUTY-HOLDERS exception (the deliberately-appointed
#     principal contractor / CDM construction manager / site manager stay named as a
#     legitimate record) does not trip the gate.
# Pure deterministic Python: no network, no model, no key.
# =============================================================================

import sys as _cpp_sys  # noqa: E402

_CPP_SCRIPTS = REPO / "scripts"
if str(_CPP_SCRIPTS) not in _cpp_sys.path:
    _cpp_sys.path.insert(0, str(_CPP_SCRIPTS))

from graders import grade_deid as _cpp_grade_deid  # noqa: E402

_CPP_FILES = REPO / "skills" / "construction-phase-plan" / "evals" / "files"
_CPP_LEAK = _CPP_FILES / "construction-phase-leak.md"
_CPP_CLEAN = _CPP_FILES / "construction-phase-clean.md"


def test_construction_phase_seeded_leak_fixture_is_caught():
    """The seeded-leak negative MUST trip the deterministic de-id auto-fail (gate is live)."""
    verdict = _cpp_grade_deid(_CPP_LEAK.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is True, "construction-phase-plan seeded-leak fixture did NOT hard-fail"
    assert verdict["reasons"], "auto_fail with no reason is not a real catch"


def test_construction_phase_clean_fixture_passes():
    """The paired clean positive must NOT false-positive (no spurious per-skill hard-fail)."""
    verdict = _cpp_grade_deid(_CPP_CLEAN.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is False, (
        f"construction-phase-plan clean fixture false-positived: {verdict['reasons']}"
    )


# =============================================================================
# Phase-14 / CON-02 pre-construction-information de-id fixture-PAIR registration.
#
# Skill-scoped section appended by plan 14-07 (do not reorder/remove the canonical
# contract assertions above, nor the MFG-02 ergonomics section, nor the MFG-03 noise
# section, nor the MFG-04 ppe-matrix section, nor the MFG-01 machine-guarding section,
# nor the CON-01 construction-phase-plan section, nor any other skill's appended section).
# pre-construction-information (the CDM 2015 Reg 4 Pre-Construction Information pack) is
# ISSUED to every designer and contractor being appointed or considered (Reg 4(4)), so it
# circulates beyond the client. Existing-structure surveys routinely cite a NAMED OCCUPIER /
# RESIDENT WITH A HEALTH DETAIL (an asbestos / access survey naming a resident's respiratory
# condition) — special-category health data under GDPR Art. 9 / India DPDP. It registers the
# pre-construction-information de-identification PAIR against the SAME deterministic de-id
# grader the whole pack's non-waivable privacy gate keys off:
#   - the seeded-leak negative (evals/files/pre-construction-leak.md) — a named occupier +
#     a survey-sourced COPD / respiratory health detail + a phone + an embedded re-id key +
#     a <5 occupier-health cell — MUST auto_fail (the gate is live), and
#   - the paired clean positive (evals/files/pre-construction-clean.md), wired into the
#     skill's eval CASE, MUST NOT false-positive (the per-skill gate is not spuriously
#     hard-failed) — proving the named-OWNERS exception (the deliberately-supplied client /
#     asbestos duty-holder / principal designer + gap-action owners stay named as a legitimate
#     record) does not trip the gate.
# Pure deterministic Python: no network, no model, no key.
# =============================================================================

import sys as _pci_sys  # noqa: E402

_PCI_SCRIPTS = REPO / "scripts"
if str(_PCI_SCRIPTS) not in _pci_sys.path:
    _pci_sys.path.insert(0, str(_PCI_SCRIPTS))

from graders import grade_deid as _pci_grade_deid  # noqa: E402

_PCI_FILES = REPO / "skills" / "pre-construction-information" / "evals" / "files"
_PCI_LEAK = _PCI_FILES / "pre-construction-leak.md"
_PCI_CLEAN = _PCI_FILES / "pre-construction-clean.md"


def test_pre_construction_seeded_leak_fixture_is_caught():
    """The seeded-leak negative MUST trip the deterministic de-id auto-fail (gate is live)."""
    verdict = _pci_grade_deid(_PCI_LEAK.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is True, "pre-construction-information seeded-leak fixture did NOT hard-fail"
    assert verdict["reasons"], "auto_fail with no reason is not a real catch"


def test_pre_construction_clean_fixture_passes():
    """The paired clean positive must NOT false-positive (no spurious per-skill hard-fail)."""
    verdict = _pci_grade_deid(_PCI_CLEAN.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is False, (
        f"pre-construction-information clean fixture false-positived: {verdict['reasons']}"
    )


# =============================================================================
# Phase-14 / CON-03 health-safety-file de-id fixture-PAIR registration.
#
# Skill-scoped section appended by plan 14-08 (do not reorder/remove the canonical
# contract assertions above, nor the MFG-02 ergonomics section, nor the MFG-03 noise
# section, nor the MFG-04 ppe-matrix section, nor the MFG-01 machine-guarding section,
# nor the CON-01 construction-phase-plan section, nor the CON-02 pre-construction-information
# section, nor any other skill's appended section). health-safety-file (the CDM 2015 Reg
# 12(5)-(9) Health & Safety File) is the as-built residual-risk record HANDED TO THE CLIENT and
# consulted by future maintenance / cleaning / refurbishment / demolition workers, so it
# circulates beyond the project team. Commissioning, survey, and as-built records routinely
# NAME AN INDIVIDUAL WITH A HEALTH/INCIDENT DETAIL (a commissioning engineer with a back-injury /
# musculoskeletal note) — special-category health data under GDPR Art. 9 / India DPDP, and no
# worker health detail belongs in the file at all. It registers the health-safety-file
# de-identification PAIR against the SAME deterministic de-id grader the whole pack's
# non-waivable privacy gate keys off:
#   - the seeded-leak negative (evals/files/health-safety-file-leak.md) — a named commissioning
#     engineer + a back-injury / musculoskeletal health detail + a phone + an embedded re-id key
#     + a <5 musculoskeletal-incident cell — MUST auto_fail (the gate is live), and
#   - the paired clean positive (evals/files/health-safety-file-clean.md), wired into the
#     skill's eval CASE, MUST NOT false-positive (the per-skill gate is not spuriously
#     hard-failed) — proving the named-DUTY-HOLDERS exception (the deliberately-supplied
#     principal designer / client + open-item owners stay named as a legitimate record) does not
#     trip the gate.
# Pure deterministic Python: no network, no model, no key.
# =============================================================================

import sys as _hsf_sys  # noqa: E402

_HSF_SCRIPTS = REPO / "scripts"
if str(_HSF_SCRIPTS) not in _hsf_sys.path:
    _hsf_sys.path.insert(0, str(_HSF_SCRIPTS))

from graders import grade_deid as _hsf_grade_deid  # noqa: E402

_HSF_FILES = REPO / "skills" / "health-safety-file" / "evals" / "files"
_HSF_LEAK = _HSF_FILES / "health-safety-file-leak.md"
_HSF_CLEAN = _HSF_FILES / "health-safety-file-clean.md"


def test_health_safety_file_seeded_leak_fixture_is_caught():
    """The seeded-leak negative MUST trip the deterministic de-id auto-fail (gate is live)."""
    verdict = _hsf_grade_deid(_HSF_LEAK.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is True, "health-safety-file seeded-leak fixture did NOT hard-fail"
    assert verdict["reasons"], "auto_fail with no reason is not a real catch"


def test_health_safety_file_clean_fixture_passes():
    """The paired clean positive must NOT false-positive (no spurious per-skill hard-fail)."""
    verdict = _hsf_grade_deid(_HSF_CLEAN.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is False, (
        f"health-safety-file clean fixture false-positived: {verdict['reasons']}"
    )


# =============================================================================
# Phase-14 / CON-04 lift-plan de-id fixture-PAIR registration.
#
# Skill-scoped section appended by plan 14-09 (do not reorder/remove the canonical
# contract assertions above, nor the MFG-02 ergonomics section, nor the MFG-03 noise
# section, nor the MFG-04 ppe-matrix section, nor the MFG-01 machine-guarding section,
# nor the CON-01 construction-phase-plan section, nor the CON-02 pre-construction-information
# section, nor the CON-03 health-safety-file section, nor any other skill's appended section).
# lift-plan (the LOLER 1998 Reg 8 / BS 7121 lifting plan) is a NAMED-PERSONNEL document by
# design — the appointed person, crane operator, and slinger / signaller are DELIBERATELY
# NAMED for the competence record (a legitimate contractual record, not leaked PII) — so the
# de-id challenge is PRECISE: keep the duty-holder names while scrubbing any worker
# MEDICAL-FITNESS / health detail (a named operator with a fitness-for-duty / back-injury
# restriction note is GDPR Art. 9 / India DPDP special-category health data) and any
# incident-derived name. It registers the lift-plan de-identification PAIR against the SAME
# deterministic de-id grader the whole pack's non-waivable privacy gate keys off:
#   - the seeded-leak negative (evals/files/lift-leak.md) — a named crane operator + a
#     medical-fitness / back-injury restriction note + a phone + an embedded re-id key +
#     a <5 dropped-load injury cell — MUST auto_fail (the gate is live), and
#   - the paired clean positive (evals/files/lift-clean.md), wired into the skill's eval CASE,
#     MUST NOT false-positive (the per-skill gate is not spuriously hard-failed) — proving the
#     named-DUTY-HOLDERS exception (the deliberately-named appointed person / crane operator /
#     slinger stay named as a legitimate competence record) does not trip the gate.
# Pure deterministic Python: no network, no model, no key.
# =============================================================================

import sys as _lift_sys  # noqa: E402

_LIFT_SCRIPTS = REPO / "scripts"
if str(_LIFT_SCRIPTS) not in _lift_sys.path:
    _lift_sys.path.insert(0, str(_LIFT_SCRIPTS))

from graders import grade_deid as _lift_grade_deid  # noqa: E402

_LIFT_FILES = REPO / "skills" / "lift-plan" / "evals" / "files"
_LIFT_LEAK = _LIFT_FILES / "lift-leak.md"
_LIFT_CLEAN = _LIFT_FILES / "lift-clean.md"


def test_lift_plan_seeded_leak_fixture_is_caught():
    """The seeded-leak negative MUST trip the deterministic de-id auto-fail (gate is live)."""
    verdict = _lift_grade_deid(_LIFT_LEAK.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is True, "lift-plan seeded-leak fixture did NOT hard-fail"
    assert verdict["reasons"], "auto_fail with no reason is not a real catch"


def test_lift_plan_clean_fixture_passes():
    """The paired clean positive must NOT false-positive (no spurious per-skill hard-fail)."""
    verdict = _lift_grade_deid(_LIFT_CLEAN.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is False, (
        f"lift-plan clean fixture false-positived: {verdict['reasons']}"
    )


# =============================================================================
# Phase-14 / CON-05 traffic-management-plan de-id fixture-PAIR registration.
#
# Skill-scoped section appended by plan 14-10 (do not reorder/remove the canonical
# contract assertions above, nor the MFG-02 ergonomics section, nor the MFG-03 noise
# section, nor the MFG-04 ppe-matrix section, nor the MFG-01 machine-guarding section,
# nor the CON-01 construction-phase-plan section, nor the CON-02 pre-construction-information
# section, nor the CON-03 health-safety-file section, nor the CON-04 lift-plan section,
# nor any other skill's appended section).
# traffic-management-plan (the CDM 2015 Reg 27 / Schedule 3 construction traffic plan) is the
# LOWEST-PII document in the pack — it is a SITE / ROUTE-LEVEL plan that carries NO named
# individual (it names routes, gates, bays, and zones — not people). So the de-id challenge
# is strict-and-simple: every personal name in the inputs is input-derived PII to scrub. It
# registers the traffic-management-plan de-identification PAIR against the SAME deterministic
# de-id grader the whole pack's non-waivable privacy gate keys off:
#   - the seeded-leak negative (evals/files/traffic-leak.md) — a named HGV driver + a
#     fitness-for-duty / back-injury restriction note + a phone + an embedded re-id key +
#     a <5 reversing struck-by injury cell — MUST auto_fail (the gate is live), and
#   - the paired clean positive (evals/files/traffic-clean.md), wired into the skill's eval CASE,
#     MUST NOT false-positive (the per-skill gate is not spuriously hard-failed) — proving the
#     site/route-level plan (which names routes, gates, and zones, not people) does not trip the
#     gate.
# Pure deterministic Python: no network, no model, no key.
# =============================================================================

_TMP_FILES = REPO / "skills" / "traffic-management-plan" / "evals" / "files"
_TMP_LEAK = _TMP_FILES / "traffic-leak.md"
_TMP_CLEAN = _TMP_FILES / "traffic-clean.md"


def test_traffic_management_plan_seeded_leak_fixture_is_caught():
    """The seeded-leak negative MUST trip the deterministic de-id auto-fail (gate is live)."""
    verdict = _lift_grade_deid(_TMP_LEAK.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is True, "traffic-management-plan seeded-leak fixture did NOT hard-fail"
    assert verdict["reasons"], "auto_fail with no reason is not a real catch"


def test_traffic_management_plan_clean_fixture_passes():
    """The paired clean positive must NOT false-positive (no spurious per-skill hard-fail)."""
    verdict = _lift_grade_deid(_TMP_CLEAN.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is False, (
        f"traffic-management-plan clean fixture false-positived: {verdict['reasons']}"
    )


# =============================================================================
# Phase-15 / UTIL-01 arc-flash-assessment de-id fixture-PAIR registration.
#
# Skill-scoped section appended by plan 15-02 (do not reorder/remove the canonical
# contract assertions above, nor any Phase-14 MFG/CON section, nor any other skill's
# appended section). arc-flash-assessment is a LOW-PII / asset-level skill (the
# equipment / IEEE 1584 parameters dominate), but an arc-flash assessment routinely
# cites a PRIOR ARC-FLASH BURN / ELECTROCUTION INCIDENT on the equipment — and a named
# injured worker from that incident is GDPR Art. 9 / India DPDP special-category health
# data. It registers the arc-flash de-identification PAIR against the SAME deterministic
# de-id grader the whole pack's non-waivable privacy gate keys off:
#   - the seeded-leak negative (evals/files/arc-flash-leak.md) — a named electrician from a
#     prior arc-flash burn incident + a phone + an embedded re-id key + a <5 arc-flash/shock
#     injury cell — MUST auto_fail (the gate is live), and
#   - the paired clean positive (evals/files/arc-flash-clean.md), wired into the skill's eval
#     CASE, MUST NOT false-positive (the per-skill gate is not spuriously hard-failed).
# This is the LOW de-id tier (no dedicated small-cell assertion needed for utilities).
# Pure deterministic Python: no network, no model, no key.
# =============================================================================

import sys as _arc_sys  # noqa: E402

_ARC_SCRIPTS = REPO / "scripts"
if str(_ARC_SCRIPTS) not in _arc_sys.path:
    _arc_sys.path.insert(0, str(_ARC_SCRIPTS))

from graders import grade_deid as _arc_grade_deid  # noqa: E402

_ARC_FILES = REPO / "skills" / "arc-flash-assessment" / "evals" / "files"
_ARC_LEAK = _ARC_FILES / "arc-flash-leak.md"
_ARC_CLEAN = _ARC_FILES / "arc-flash-clean.md"


def test_arc_flash_seeded_leak_fixture_is_caught():
    """The seeded-leak negative MUST trip the deterministic de-id auto-fail (gate is live)."""
    verdict = _arc_grade_deid(_ARC_LEAK.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is True, "arc-flash-assessment seeded-leak fixture did NOT hard-fail"
    assert verdict["reasons"], "auto_fail with no reason is not a real catch"


def test_arc_flash_clean_fixture_passes():
    """The paired clean positive must NOT false-positive (no spurious per-skill hard-fail)."""
    verdict = _arc_grade_deid(_ARC_CLEAN.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is False, (
        f"arc-flash-assessment clean fixture false-positived: {verdict['reasons']}"
    )


# =============================================================================
# Phase-15 / UTIL-02 electrical-permit-switching-program de-id fixture-PAIR registration.
#
# Skill-scoped section appended by plan 15-03 (do not reorder/remove the canonical
# contract assertions above, nor any Phase-14 MFG/CON section, nor the UTIL-01
# arc-flash section, nor any other skill's appended section).
# electrical-permit-switching-program is a LOW-PII / apparatus-level skill (the
# named apparatus / points of isolation dominate, and the authorised/senior
# authorised person is a legitimate retained operational record), but a switching
# program routinely cites a PRIOR SWITCHING / ELECTROCUTION INCIDENT on the
# apparatus — and a named injured operator from that incident is GDPR Art. 9 /
# India DPDP special-category health data. It registers the switching-program
# de-identification PAIR against the SAME deterministic de-id grader the whole
# pack's non-waivable privacy gate keys off:
#   - the seeded-leak negative (evals/files/switching-leak.md) — a named operator from a
#     prior switching incident + a phone + an embedded re-id key + a <5 shock/burn injury
#     cell — MUST auto_fail (the gate is live), and
#   - the paired clean positive (evals/files/switching-clean.md), wired into the skill's eval
#     CASE, MUST NOT false-positive (the per-skill gate is not spuriously hard-failed).
# This is the LOW de-id tier (no dedicated small-cell assertion needed for utilities).
# Pure deterministic Python: no network, no model, no key.
# =============================================================================

import sys as _switching_sys  # noqa: E402

_SWITCHING_SCRIPTS = REPO / "scripts"
if str(_SWITCHING_SCRIPTS) not in _switching_sys.path:
    _switching_sys.path.insert(0, str(_SWITCHING_SCRIPTS))

from graders import grade_deid as _switching_grade_deid  # noqa: E402

_SWITCHING_FILES = REPO / "skills" / "electrical-permit-switching-program" / "evals" / "files"
_SWITCHING_LEAK = _SWITCHING_FILES / "switching-leak.md"
_SWITCHING_CLEAN = _SWITCHING_FILES / "switching-clean.md"


def test_switching_seeded_leak_fixture_is_caught():
    """The seeded-leak negative MUST trip the deterministic de-id auto-fail (gate is live)."""
    verdict = _switching_grade_deid(_SWITCHING_LEAK.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is True, "electrical-permit-switching-program seeded-leak fixture did NOT hard-fail"
    assert verdict["reasons"], "auto_fail with no reason is not a real catch"


def test_switching_clean_fixture_passes():
    """The paired clean positive must NOT false-positive (no spurious per-skill hard-fail)."""
    verdict = _switching_grade_deid(_SWITCHING_CLEAN.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is False, (
        f"electrical-permit-switching-program clean fixture false-positived: {verdict['reasons']}"
    )


# =============================================================================
# Phase-15 / UTIL-03 live-working-risk-assessment de-id fixture-PAIR registration.
#
# Skill-scoped section appended by plan 15-04 (do not reorder/remove the canonical
# contract assertions above, nor any Phase-14 MFG/CON section, nor the UTIL-01
# arc-flash section, nor the UTIL-02 switching section, nor any other skill's
# appended section). live-working-risk-assessment is a LOW-PII / apparatus-level
# skill (the named task / live conductors / approach boundaries dominate, and the
# live-work authority is a legitimate retained operational record on the
# energized-work permit), but a live-working assessment routinely cites a PRIOR
# CONTACT / ELECTROCUTION / ARC-FLASH BURN INCIDENT on the apparatus — and a named
# injured worker from that incident is GDPR Art. 9 / India DPDP special-category
# health data. It registers the live-working de-identification PAIR against the
# SAME deterministic de-id grader the whole pack's non-waivable privacy gate keys
# off:
#   - the seeded-leak negative (evals/files/live-working-leak.md) — a named worker from a
#     prior contact/electrocution incident + a phone + an embedded re-id key + a <5
#     electrocution/arc-flash injury cell — MUST auto_fail (the gate is live), and
#   - the paired clean positive (evals/files/live-working-clean.md), wired into the skill's eval
#     CASE, MUST NOT false-positive (the per-skill gate is not spuriously hard-failed).
# This is the LOW de-id tier (no dedicated small-cell assertion needed for utilities).
# Pure deterministic Python: no network, no model, no key.
# =============================================================================

import sys as _live_working_sys  # noqa: E402

_LIVE_WORKING_SCRIPTS = REPO / "scripts"
if str(_LIVE_WORKING_SCRIPTS) not in _live_working_sys.path:
    _live_working_sys.path.insert(0, str(_LIVE_WORKING_SCRIPTS))

from graders import grade_deid as _live_working_grade_deid  # noqa: E402

_LIVE_WORKING_FILES = REPO / "skills" / "live-working-risk-assessment" / "evals" / "files"
_LIVE_WORKING_LEAK = _LIVE_WORKING_FILES / "live-working-leak.md"
_LIVE_WORKING_CLEAN = _LIVE_WORKING_FILES / "live-working-clean.md"


def test_live_working_seeded_leak_fixture_is_caught():
    """The seeded-leak negative MUST trip the deterministic de-id auto-fail (gate is live)."""
    verdict = _live_working_grade_deid(_LIVE_WORKING_LEAK.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is True, "live-working-risk-assessment seeded-leak fixture did NOT hard-fail"
    assert verdict["reasons"], "auto_fail with no reason is not a real catch"


def test_live_working_clean_fixture_passes():
    """The paired clean positive must NOT false-positive (no spurious per-skill hard-fail)."""
    verdict = _live_working_grade_deid(_LIVE_WORKING_CLEAN.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is False, (
        f"live-working-risk-assessment clean fixture false-positived: {verdict['reasons']}"
    )


# =============================================================================
# Phase-15 / HC-01 sharps-needlestick-management de-id fixture-PAIR registration.
#
# Skill-scoped section appended by plan 15-05 (do not reorder/remove the canonical
# contract assertions above, nor any other skill's appended section). This is the
# catalog's HIGHEST-PHI tier: bloodborne-pathogen exposure data — the source
# patient's identity + serostatus and the injured worker's post-exposure (PEP)
# medical record — is special-category health data (PHI). It registers the
# sharps-needlestick-management de-identification PAIR against the SAME deterministic
# de-id grader the whole pack's non-waivable privacy gate keys off:
#   - the seeded-leak negative (evals/files/sharps-leak.md) — a named injured worker +
#     the source patient's identity & HIV/HCV serostatus + the worker's PEP record + a
#     phone + an embedded re-id key + a <5 sharps-injury cell — MUST auto_fail (the
#     gate is live), and the small-cell <5 suppression catch is asserted EXPLICITLY
#     (the D-03 HARD-fail — a sub-5 sharps-injury cell that allows re-identification of
#     a worker's exposure/serostatus must be suppressed), and
#   - the paired clean positive (evals/files/sharps-clean.md), wired into the skill's
#     eval CASE, MUST NOT false-positive (the per-skill gate is not spuriously
#     hard-failed).
# This append is a SERIAL / orchestrator-batched edit (D-04) — applied in order with
# the other Wave-3 appends; parallel executors must NOT race-write this shared file.
# Pure deterministic Python: no network, no model, no key.
# =============================================================================

import sys as _sharps_sys  # noqa: E402

_SHARPS_SCRIPTS = REPO / "scripts"
if str(_SHARPS_SCRIPTS) not in _sharps_sys.path:
    _sharps_sys.path.insert(0, str(_SHARPS_SCRIPTS))

from graders import grade_deid as _sharps_grade_deid  # noqa: E402

_SHARPS_FILES = REPO / "skills" / "sharps-needlestick-management" / "evals" / "files"
_SHARPS_LEAK = _SHARPS_FILES / "sharps-leak.md"
_SHARPS_CLEAN = _SHARPS_FILES / "sharps-clean.md"


def test_sharps_seeded_leak_fixture_is_caught():
    """The seeded-leak negative MUST trip the deterministic de-id auto-fail (gate is live)."""
    verdict = _sharps_grade_deid(_SHARPS_LEAK.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is True, "sharps seeded-leak fixture did NOT hard-fail"
    assert verdict["reasons"], "auto_fail with no reason is not a real catch"


def test_sharps_small_cell_suppression_caught():
    """HIGHEST-PHI TIER (T-15-05-02): the sub-5 sharps-injury breakdown MUST be caught as a
    small-cell leak — the <5 suppression rule (with secondary back-calc) is the sharps skill's
    defining D-03 de-id HARD-fail (a <5 cell de-anonymizes a worker's exposure/serostatus)."""
    verdict = _sharps_grade_deid(_SHARPS_LEAK.read_text(encoding="utf-8"))
    assert verdict["conditions"]["no_small_cell"] is False, (
        "sharps seeded-leak <5 sharps-injury cell was NOT caught — small-cell suppression gate is dead"
    )
    assert any("small-cell" in r for r in verdict["reasons"]), (
        "the <5 small-cell leak is not among the auto_fail reasons"
    )


def test_sharps_clean_fixture_passes():
    """The paired clean positive must NOT false-positive (no spurious per-skill hard-fail)."""
    verdict = _sharps_grade_deid(_SHARPS_CLEAN.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is False, (
        f"sharps clean fixture false-positived: {verdict['reasons']}"
    )


# =============================================================================
# Phase-15 / HC-02 infection-control-plan de-id fixture-PAIR registration.
#
# Skill-scoped section appended by plan 15-06 (do not reorder/remove the canonical
# contract assertions above, nor any other skill's appended section). This is the
# catalog's HIGHEST-PHI tier: healthcare infection data — a patient's infection /
# colonisation status and any outbreak / cluster surveillance — is special-category
# health data (PHI). It registers the infection-control-plan de-identification PAIR
# against the SAME deterministic de-id grader the whole pack's non-waivable privacy
# gate keys off:
#   - the seeded-leak negative (evals/files/infection-control-leak.md) — a named IPC
#     lead + phone + a named patient's TB-positive infection status + a 3-case TB
#     outbreak on the named Ward 4B + an embedded re-id key — MUST auto_fail (the
#     gate is live), and the small-cell <5 suppression catch is asserted EXPLICITLY
#     (the D-03 HARD-fail — a sub-5 cluster on a named ward de-anonymizes patients
#     via the small-cell back-calculation, and must be suppressed), and
#   - the paired clean positive (evals/files/infection-control-clean.md), wired into
#     the skill's eval CASE, MUST NOT false-positive (the per-skill gate is not
#     spuriously hard-failed).
# This append is a SERIAL / orchestrator-batched edit (D-04) — applied in order with
# the other Wave-3 appends; parallel executors must NOT race-write this shared file.
# Pure deterministic Python: no network, no model, no key.
# =============================================================================

import sys as _infection_control_sys  # noqa: E402

_INFECTION_CONTROL_SCRIPTS = REPO / "scripts"
if str(_INFECTION_CONTROL_SCRIPTS) not in _infection_control_sys.path:
    _infection_control_sys.path.insert(0, str(_INFECTION_CONTROL_SCRIPTS))

from graders import grade_deid as _infection_control_grade_deid  # noqa: E402

_INFECTION_CONTROL_FILES = REPO / "skills" / "infection-control-plan" / "evals" / "files"
_INFECTION_CONTROL_LEAK = _INFECTION_CONTROL_FILES / "infection-control-leak.md"
_INFECTION_CONTROL_CLEAN = _INFECTION_CONTROL_FILES / "infection-control-clean.md"


def test_infection_control_seeded_leak_fixture_is_caught():
    """The seeded-leak negative MUST trip the deterministic de-id auto-fail (gate is live)."""
    verdict = _infection_control_grade_deid(_INFECTION_CONTROL_LEAK.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is True, "infection-control seeded-leak fixture did NOT hard-fail"
    assert verdict["reasons"], "auto_fail with no reason is not a real catch"


def test_infection_control_small_cell_suppression_caught():
    """HIGHEST-PHI TIER (T-15-06-02): the sub-5 TB cluster on a named ward MUST be caught as a
    small-cell leak — the <5 suppression rule (with secondary back-calc) is the IPC skill's
    defining D-03 de-id HARD-fail (a 3-case cluster on a named ward de-anonymizes patients)."""
    verdict = _infection_control_grade_deid(_INFECTION_CONTROL_LEAK.read_text(encoding="utf-8"))
    assert verdict["conditions"]["no_small_cell"] is False, (
        "infection-control seeded-leak <5 ward cluster was NOT caught — small-cell suppression gate is dead"
    )
    assert any("small-cell" in r for r in verdict["reasons"]), (
        "the <5 small-cell leak is not among the auto_fail reasons"
    )


def test_infection_control_clean_fixture_passes():
    """The paired clean positive must NOT false-positive (no spurious per-skill hard-fail)."""
    verdict = _infection_control_grade_deid(_INFECTION_CONTROL_CLEAN.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is False, (
        f"infection-control clean fixture false-positived: {verdict['reasons']}"
    )


# =============================================================================
# Phase-15 / HC-03 patient-handling-assessment de-id fixture-PAIR registration.
#
# Skill-scoped section appended by plan 15-07 (do not reorder/remove the canonical
# contract assertions above, nor any other skill's appended section). This is the
# catalog's HIGHEST-PHI tier: patient-handling health data — a patient's mobility /
# dependency / diagnosis and a worker's musculoskeletal / back-condition
# occupational-health record — is special-category health data (PHI). It registers
# the patient-handling-assessment de-identification PAIR against the SAME deterministic
# de-id grader the whole pack's non-waivable privacy gate keys off:
#   - the seeded-leak negative (evals/files/patient-handling-leak.md) — a named,
#     diagnosed patient (ward/bay + MRN) + a named handler's back-condition OH record +
#     phone + a 3-case back / 2-case shoulder handling-injury cell + an embedded re-id
#     key — MUST auto_fail (the gate is live), and the small-cell <5 suppression catch
#     is asserted EXPLICITLY (the D-03 HARD-fail — a sub-5 handling-injury cell on a
#     named ward de-anonymizes the injured handlers via the small-cell back-calculation,
#     and must be suppressed), and
#   - the paired clean positive (evals/files/patient-handling-clean.md), wired into the
#     skill's eval CASE, MUST NOT false-positive (the per-skill gate is not spuriously
#     hard-failed).
# This append is a SERIAL / orchestrator-batched edit (D-04) — applied in order with
# the other Wave-3 appends; parallel executors must NOT race-write this shared file.
# Pure deterministic Python: no network, no model, no key.
# =============================================================================

import sys as _patient_handling_sys  # noqa: E402

_PATIENT_HANDLING_SCRIPTS = REPO / "scripts"
if str(_PATIENT_HANDLING_SCRIPTS) not in _patient_handling_sys.path:
    _patient_handling_sys.path.insert(0, str(_PATIENT_HANDLING_SCRIPTS))

from graders import grade_deid as _patient_handling_grade_deid  # noqa: E402

_PATIENT_HANDLING_FILES = REPO / "skills" / "patient-handling-assessment" / "evals" / "files"
_PATIENT_HANDLING_LEAK = _PATIENT_HANDLING_FILES / "patient-handling-leak.md"
_PATIENT_HANDLING_CLEAN = _PATIENT_HANDLING_FILES / "patient-handling-clean.md"


def test_patient_handling_seeded_leak_fixture_is_caught():
    """The seeded-leak negative MUST trip the deterministic de-id auto-fail (gate is live)."""
    verdict = _patient_handling_grade_deid(_PATIENT_HANDLING_LEAK.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is True, "patient-handling seeded-leak fixture did NOT hard-fail"
    assert verdict["reasons"], "auto_fail with no reason is not a real catch"


def test_patient_handling_small_cell_suppression_caught():
    """HIGHEST-PHI TIER (T-15-07-02): the sub-5 handling-injury cell on a named ward MUST be caught as
    a small-cell leak — the <5 suppression rule (with secondary back-calc) is the patient-handling
    skill's defining D-03 de-id HARD-fail (a <5 cell de-anonymizes the injured handlers)."""
    verdict = _patient_handling_grade_deid(_PATIENT_HANDLING_LEAK.read_text(encoding="utf-8"))
    assert verdict["conditions"]["no_small_cell"] is False, (
        "patient-handling seeded-leak <5 handling-injury cell was NOT caught — small-cell suppression gate is dead"
    )
    assert any("small-cell" in r for r in verdict["reasons"]), (
        "the <5 small-cell leak is not among the auto_fail reasons"
    )


def test_patient_handling_clean_fixture_passes():
    """The paired clean positive must NOT false-positive (no spurious per-skill hard-fail)."""
    verdict = _patient_handling_grade_deid(_PATIENT_HANDLING_CLEAN.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is False, (
        f"patient-handling clean fixture false-positived: {verdict['reasons']}"
    )


# =============================================================================
# Phase-15 / HC-04 workplace-violence-prevention de-id fixture-PAIR registration.
#
# Skill-scoped section appended by plan 15-08 (do not reorder/remove the canonical
# contract assertions above, nor any other skill's appended section). This is the
# catalog's HIGHEST-PHI tier: workplace-violence incident data — a named victim,
# assailant, or known-risk patient and any behavioural-health flag — is
# special-category health data (PHI). It registers the workplace-violence-prevention
# de-identification PAIR against the SAME deterministic de-id grader the whole pack's
# non-waivable privacy gate keys off:
#   - the seeded-leak negative (evals/files/workplace-violence-leak.md) — a named
#     triage nurse + phone + a named assailant patient with a behavioural-health flag
#     + a 2-incident type-1 / 3-incident type-2 category on the named Ward 4B + an
#     embedded re-id key — MUST auto_fail (the gate is live), and the small-cell <5
#     suppression catch is asserted EXPLICITLY (the D-03 HARD-fail — a sub-5 incident
#     category on a named ward de-anonymizes the people involved via the small-cell
#     back-calculation, and must be suppressed), and
#   - the paired clean positive (evals/files/workplace-violence-clean.md), wired into
#     the skill's eval CASE, MUST NOT false-positive (the per-skill gate is not
#     spuriously hard-failed).
# This append is a SERIAL / orchestrator-batched edit (D-04) — applied in order with
# the other Wave-3 appends; parallel executors must NOT race-write this shared file.
# Pure deterministic Python: no network, no model, no key.
# =============================================================================

import sys as _workplace_violence_sys  # noqa: E402

_WORKPLACE_VIOLENCE_SCRIPTS = REPO / "scripts"
if str(_WORKPLACE_VIOLENCE_SCRIPTS) not in _workplace_violence_sys.path:
    _workplace_violence_sys.path.insert(0, str(_WORKPLACE_VIOLENCE_SCRIPTS))

from graders import grade_deid as _workplace_violence_grade_deid  # noqa: E402

_WORKPLACE_VIOLENCE_FILES = REPO / "skills" / "workplace-violence-prevention" / "evals" / "files"
_WORKPLACE_VIOLENCE_LEAK = _WORKPLACE_VIOLENCE_FILES / "workplace-violence-leak.md"
_WORKPLACE_VIOLENCE_CLEAN = _WORKPLACE_VIOLENCE_FILES / "workplace-violence-clean.md"


def test_workplace_violence_seeded_leak_fixture_is_caught():
    """The seeded-leak negative MUST trip the deterministic de-id auto-fail (gate is live)."""
    verdict = _workplace_violence_grade_deid(_WORKPLACE_VIOLENCE_LEAK.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is True, "workplace-violence seeded-leak fixture did NOT hard-fail"
    assert verdict["reasons"], "auto_fail with no reason is not a real catch"


def test_workplace_violence_small_cell_suppression_caught():
    """HIGHEST-PHI TIER (T-15-08-02): the sub-5 WPV-incident category on a named ward MUST be caught as
    a small-cell leak — the <5 suppression rule (with secondary back-calc) is the WPV skill's defining
    D-03 de-id HARD-fail (a 2-incident category on a named ward de-anonymizes the people involved)."""
    verdict = _workplace_violence_grade_deid(_WORKPLACE_VIOLENCE_LEAK.read_text(encoding="utf-8"))
    assert verdict["conditions"]["no_small_cell"] is False, (
        "workplace-violence seeded-leak <5 incident cell was NOT caught — small-cell suppression gate is dead"
    )
    assert any("small-cell" in r for r in verdict["reasons"]), (
        "the <5 small-cell leak is not among the auto_fail reasons"
    )


def test_workplace_violence_clean_fixture_passes():
    """The paired clean positive must NOT false-positive (no spurious per-skill hard-fail)."""
    verdict = _workplace_violence_grade_deid(_WORKPLACE_VIOLENCE_CLEAN.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is False, (
        f"workplace-violence clean fixture false-positived: {verdict['reasons']}"
    )


# =============================================================================
# Phase-15 / HC-05 lab-biosafety-assessment de-id fixture-PAIR registration.
#
# Skill-scoped section appended by plan 15-09 (do not reorder/remove the canonical
# contract assertions above, nor any other skill's appended section). This is the
# catalog's HIGHEST-PHI tier: laboratory biosafety inputs are special-category health
# data (PHI) — the specimen-source patient's identity & clinical/serostatus detail and
# the worker's serological-surveillance / occupational-health record. It registers the
# lab-biosafety-assessment de-identification PAIR against the SAME deterministic de-id
# grader the whole pack's non-waivable privacy gate keys off:
#   - the seeded-leak negative (evals/files/biosafety-leak.md) — a named specimen-source
#     patient + a named worker's serological-surveillance record + a phone + an embedded
#     re-id key + a <5 lab-incident/exposure cell — MUST auto_fail (the gate is live),
#     and the small-cell <5 suppression catch is asserted EXPLICITLY (the D-03 HARD-fail
#     — a sub-5 lab-incident cell that allows re-identification of a worker's exposure
#     must be suppressed), and
#   - the paired clean positive (evals/files/biosafety-clean.md), wired into the skill's
#     eval CASE, MUST NOT false-positive (the per-skill gate is not spuriously
#     hard-failed).
# This append is a SERIAL / orchestrator-batched edit (D-04) — applied in order with
# the other Wave-3 appends; parallel executors must NOT race-write this shared file.
# Pure deterministic Python: no network, no model, no key.
# =============================================================================

import sys as _biosafety_sys  # noqa: E402

_BIOSAFETY_SCRIPTS = REPO / "scripts"
if str(_BIOSAFETY_SCRIPTS) not in _biosafety_sys.path:
    _biosafety_sys.path.insert(0, str(_BIOSAFETY_SCRIPTS))

from graders import grade_deid as _biosafety_grade_deid  # noqa: E402

_BIOSAFETY_FILES = REPO / "skills" / "lab-biosafety-assessment" / "evals" / "files"
_BIOSAFETY_LEAK = _BIOSAFETY_FILES / "biosafety-leak.md"
_BIOSAFETY_CLEAN = _BIOSAFETY_FILES / "biosafety-clean.md"


def test_biosafety_seeded_leak_fixture_is_caught():
    """The seeded-leak negative MUST trip the deterministic de-id auto-fail (gate is live)."""
    verdict = _biosafety_grade_deid(_BIOSAFETY_LEAK.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is True, "biosafety seeded-leak fixture did NOT hard-fail"
    assert verdict["reasons"], "auto_fail with no reason is not a real catch"


def test_biosafety_small_cell_suppression_caught():
    """HIGHEST-PHI TIER (T-15-09-01): the sub-5 lab-incident/exposure breakdown MUST be caught as a
    small-cell leak — the <5 suppression rule (with secondary back-calc) is the D-03 de-id HARD-fail
    (a <5 lab-incident cell de-anonymizes a worker's exposure)."""
    verdict = _biosafety_grade_deid(_BIOSAFETY_LEAK.read_text(encoding="utf-8"))
    assert verdict["conditions"]["no_small_cell"] is False, (
        "biosafety seeded-leak <5 lab-incident cell was NOT caught — small-cell suppression gate is dead"
    )
    assert any("small-cell" in r for r in verdict["reasons"]), (
        "the <5 small-cell leak is not among the auto_fail reasons"
    )


def test_biosafety_clean_fixture_passes():
    """The paired clean positive must NOT false-positive (no spurious per-skill hard-fail)."""
    verdict = _biosafety_grade_deid(_BIOSAFETY_CLEAN.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is False, (
        f"biosafety clean fixture false-positived: {verdict['reasons']}"
    )
