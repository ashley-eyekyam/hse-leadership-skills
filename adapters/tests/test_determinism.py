"""test_determinism.py — the build is deterministic + idempotent (§3.1 / Pitfall 5).

Re-emitting a skill yields byte-identical bundle files (sorted-keys manifest +
trailing newline + POSIX paths) — the invariant the bundle-diff CI job relies on.
"""

import build


def _files(out):
    return {p.relative_to(out).as_posix(): p.read_bytes() for p in sorted(out.rglob("*")) if p.is_file()}


def test_chatgpt_byte_identical_across_reruns(risk_assessment_dir, tmp_path):
    adapted = build.load_skill(risk_assessment_dir)
    platforms = build.load_platforms()
    out1 = tmp_path / "run1"
    out2 = tmp_path / "run2"
    build.emit_chatgpt(adapted, out1, platforms)
    build.emit_chatgpt(adapted, out2, platforms)
    assert _files(out1) == _files(out2), "ChatGPT bundle not byte-identical across re-runs"


def test_all_platforms_byte_identical(incident_investigation_dir, tmp_path):
    adapted = build.load_skill(incident_investigation_dir)
    platforms = build.load_platforms()
    for platform in build.PLATFORMS:
        out1 = tmp_path / "a" / platform
        out2 = tmp_path / "b" / platform
        build.emit(adapted, platform, out1, platforms)
        build.emit(adapted, platform, out2, platforms)
        assert _files(out1) == _files(out2), f"{platform} not byte-identical across re-runs"


def test_manifest_trailing_newline(risk_assessment_dir, tmp_path):
    adapted = build.load_skill(risk_assessment_dir)
    platforms = build.load_platforms()
    out = tmp_path / "chatgpt"
    build.emit_chatgpt(adapted, out, platforms)
    assert (out / "manifest.json").read_bytes().endswith(b"\n")
