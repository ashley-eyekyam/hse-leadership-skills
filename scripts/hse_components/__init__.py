"""
hse_components — shared deterministic HSE engines (A7).

The barrel re-exports the public API of each engine so a consuming skill can do
``from hse_components import score, trir`` regardless of which module owns the
name. Each engine is pure-script / stdlib-only and deterministic: identical
input yields byte-identical output.

Engines (all five landed across Plans 03-02 and 03-03):
  - risk_matrix    — L×S scoring with the D-02 LOCKED default bands (03-02)
  - incident_rates — TRIR/DART/LTIFR with LOCKED OSHA bases (03-02)
  - controls       — hierarchy-of-controls ranker + PPE/admin-only flag (03-03)
  - rca            — 5-method causal scaffold + reaches_systemic validator (03-03)
  - smart_actions  — SMART-action validator/tracker (03-03)

This package is the single import surface the portability shim (``_shim.py``)
resolves with the per-skill symlink removed.
"""

from .controls import (
    HIERARCHY,
    NO_CONTROLS_FLAG,
    PPE_ADMIN_ONLY_FLAG,
    classify,
    rank_controls,
    validate_treatment,
)
from .rca import (
    METHODS,
    scaffold,
    validate,
)
from .incident_rates import (
    MILLION_BASE,
    OSHA_BASE,
    benchmark_delta,
    compute_all,
    dart,
    ltifr,
    trir,
)
from .smart_actions import (
    REQUIRED_FIELDS,
    days_until_due,
    validate_action,
    validate_register,
)
from .risk_matrix import (
    DEFAULT_5X5,
    DEFAULT_BANDS,
    MatrixConfig,
    MatrixConfigError,
    load_matrix,
    residual_delta,
    score,
)
# ergonomics
from .ergonomics import (
    ErgonomicsInputError,
    niosh_rwl,
    rula_score,
    reba_score,
    to_report_blocks as ergo_blocks,
)
# arcflash
from .arcflash import (
    ArcFlashInputError,
    incident_energy,
    arc_flash_boundary,
    ppe_category,
    to_report_blocks as arcflash_blocks,
)
# fatigue
from .fatigue import (
    FatigueInputError,
    fmcsa_compliance,
    eu561_compliance,
    fatigue_index,
    to_report_blocks as fatigue_blocks,
)

__all__ = [
    # risk_matrix
    "MatrixConfig",
    "MatrixConfigError",
    "DEFAULT_BANDS",
    "DEFAULT_5X5",
    "load_matrix",
    "score",
    "residual_delta",
    # incident_rates
    "OSHA_BASE",
    "MILLION_BASE",
    "trir",
    "dart",
    "ltifr",
    "compute_all",
    "benchmark_delta",
    # controls
    "HIERARCHY",
    "PPE_ADMIN_ONLY_FLAG",
    "NO_CONTROLS_FLAG",
    "classify",
    "rank_controls",
    "validate_treatment",
    # smart_actions
    "REQUIRED_FIELDS",
    "validate_action",
    "validate_register",
    "days_until_due",
    # rca
    "METHODS",
    "scaffold",
    "validate",
    # ergonomics
    "ErgonomicsInputError",
    "niosh_rwl",
    "rula_score",
    "reba_score",
    "ergo_blocks",
    # arcflash
    "ArcFlashInputError",
    "incident_energy",
    "arc_flash_boundary",
    "ppe_category",
    "arcflash_blocks",
    # fatigue
    "FatigueInputError",
    "fmcsa_compliance",
    "eu561_compliance",
    "fatigue_index",
    "fatigue_blocks",
]
