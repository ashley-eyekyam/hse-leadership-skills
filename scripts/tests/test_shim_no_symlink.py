"""AC7 — the portability shim resolves hse_components with the symlink REMOVED.

Spec-locked correctness trap (A7 §3.7 / Pitfall 7): the reference mechanism must
work BOTH with the per-skill symlink present AND after it is stripped (the
flattened-distribution / zipped-host case). This test proves the symlink-removed
path: it materialises a representative tree in tmp_path with a real `scripts/`
directory (NO symlink), drops in a consuming helper whose first lines run the
`_shim.py` sys.path walk, executes that helper in a CLEAN subprocess (so the test
process's own sys.path can't mask the failure), and asserts the helper imported
`hse_components` and called a real engine function.

Mirrors tests/test_card_symlink.py's "copy tree, remove the symlink, re-resolve"
idiom. Plain pytest, sandbox-offline, no framework config.
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

# scripts/tests/test_shim_no_symlink.py -> scripts/hse_components
COMPONENTS_DIR = Path(__file__).resolve().parent.parent / "hse_components"
SHIM_PATH = COMPONENTS_DIR / "_shim.py"


def test_shim_py_exists_and_uses_sys_path():
    """The shim file exists and is a sys.path fallback (contains the marker)."""
    assert SHIM_PATH.exists(), "_shim.py must exist (the portability fallback)"
    text = SHIM_PATH.read_text(encoding="utf-8")
    assert "sys.path" in text


def test_import_resolves_with_symlink_removed(tmp_path):
    """A consuming helper imports hse_components from a flattened tree that has
    NO symlink — the shim walks up to the package and injects it on sys.path."""
    # Build a representative repo-shaped tree: <root>/scripts/hse_components (real
    # copy, NOT a symlink) + <root>/skills/demo-skill/scripts/helper.py.
    root = tmp_path / "flat-distribution"
    pkg_parent = root / "scripts"
    pkg_parent.mkdir(parents=True)
    shutil.copytree(COMPONENTS_DIR, pkg_parent / "hse_components")

    skill_scripts = root / "skills" / "demo-skill" / "scripts"
    skill_scripts.mkdir(parents=True)

    # Prove there is NO symlink anywhere in the consuming skill's path.
    assert not any(
        p.is_symlink() for p in skill_scripts.parents if p != p.parent
    ) and not skill_scripts.is_symlink(), "test tree must contain no symlinks"

    helper = skill_scripts / "helper.py"
    helper.write_text(
        "from _shim import ensure_hse_components\n"
        "ensure_hse_components(__file__)\n"
        "import hse_components\n"
        "from hse_components import score, trir\n"
        "# Exercise a real engine to prove the import is live, not just resolvable.\n"
        "assert score(4, 5)['score'] == 20\n"
        "assert trir(3, 290_000) == 2.07\n"
        "print('SHIM_OK')\n",
        encoding="utf-8",
    )

    # The helper must be able to import _shim itself first. In a real skill the
    # symlink/relative layout puts hse_components (and _shim) reachable; here we
    # emulate the worst case where ONLY the package dir is discoverable by walking
    # up — so seed sys.path with the package dir the way a bootstrap line would,
    # but DO NOT pre-seed hse_components' parent (that's the shim's job to find).
    pkg_dir = pkg_parent / "hse_components"

    env = dict(os.environ)
    # A clean child: no inherited PYTHONPATH that could mask a shim failure.
    env.pop("PYTHONPATH", None)
    # Bootstrap only enough to import _shim (it lives inside the package dir);
    # the shim itself is then responsible for putting `scripts/` on sys.path so
    # `import hse_components` resolves WITHOUT any symlink.
    env["PYTHONPATH"] = str(pkg_dir)

    result = subprocess.run(
        [sys.executable, str(helper)],
        cwd=str(skill_scripts),
        env=env,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"helper failed (symlink-removed import did not resolve):\n"
        f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
    )
    assert "SHIM_OK" in result.stdout
