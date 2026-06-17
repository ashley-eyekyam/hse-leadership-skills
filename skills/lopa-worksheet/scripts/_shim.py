"""
_shim.py — portability fallback so a symlink-stripped distribution still imports
``hse_components`` (A7 §3.7 / D3).

Default mechanism (clean dev tree / git checkout): a consuming skill has a
relative symlink ``skills/<name>/scripts/ → ../../../scripts/hse_components/`` and
imports the package directly. But a zip/host that strips symlinks (the Phase-C
adapter case) breaks that. This shim is the documented fallback: it walks UP from
the calling file to the repo root (the first ancestor that contains
``scripts/hse_components``) and inserts that ``scripts/`` directory on
``sys.path`` so ``import hse_components`` resolves WITHOUT any symlink.

A consuming helper's first lines run::

    from _shim import ensure_hse_components
    ensure_hse_components(__file__)
    import hse_components

The verbatim 3-line inline form (§3.7) the forge reproduces is preserved in the
module docstring of :func:`ensure_hse_components`. Stdlib only; no I/O beyond
``Path.exists`` directory probing.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Optional

_PACKAGE_NAME = "hse_components"


def find_scripts_root(start: str) -> Optional[Path]:
    """Walk up from ``start`` to the first ancestor containing
    ``scripts/hse_components`` and return that ``scripts/`` directory.

    Returns ``None`` if no such ancestor exists (the package cannot be located).
    Also handles the in-package case where ``start`` is already inside
    ``scripts/hse_components`` (then the package's parent IS the scripts root).
    """
    here = Path(start).resolve()
    # If we are already inside the package, its parent dir is the scripts root.
    for parent in (here, *here.parents):
        if parent.name == _PACKAGE_NAME and (parent / "__init__.py").exists():
            return parent.parent

    # Otherwise ascend until an ancestor holds scripts/hse_components.
    for parent in (here, *here.parents):
        candidate = parent / "scripts" / _PACKAGE_NAME
        if candidate.exists():
            return parent / "scripts"
    return None


def ensure_hse_components(start: str) -> Path:
    """Make ``import hse_components`` resolvable from ``start``'s location.

    Equivalent to the verbatim §3.7 inline shim::

        import sys, pathlib
        root = pathlib.Path(__file__).resolve()
        while root.name and not (root / "scripts" / "hse_components").exists():
            root = root.parent
        sys.path.insert(0, str(root / "scripts"))
        import hse_components            # noqa: E402

    Locates the ``scripts/`` directory that owns the package, inserts it on
    ``sys.path`` (idempotent), and returns it. Raises ``ImportError`` if the
    package cannot be found — fail loud, never a silent no-op that would surface
    later as a confusing ModuleNotFoundError.
    """
    scripts_root = find_scripts_root(start)
    if scripts_root is None:
        raise ImportError(
            f"could not locate the '{_PACKAGE_NAME}' package by walking up from "
            f"{start!r}; the distribution may be missing scripts/hse_components"
        )
    scripts_root_str = str(scripts_root)
    if scripts_root_str not in sys.path:
        sys.path.insert(0, scripts_root_str)
    return scripts_root


__all__ = ["find_scripts_root", "ensure_hse_components"]
