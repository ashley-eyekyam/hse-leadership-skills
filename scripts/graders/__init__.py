"""scripts/graders — the A8 deterministic graders (A8 §4.4, QA-02).

Three pure-code graders that form the NON-WAIVABLE hard-block enforcement class.
They run BEFORE the model grader in run_evals.py and short-circuit a case on any
hard-fail, so a stochastic judge never gets to "pass" a privacy leak or an
invented citation (threat T-03-16):

    grade_deid             — a de-id leak (A5 §3.5 four conditions) is a
                             deterministic auto_fail that overrides the weighted
                             mean (T-03-14).
    grade_citation         — a cited KB id that does not resolve to a
                             knowledge-base _registry.yaml fragment forces
                             regulatory_citation_accuracy below 4 = FAIL (T-03-15).
    grade_report_produced  — report.json validates against the report-engine
                             schema AND a renderer produced docx/pdf (or the A4
                             §4.10 degraded path).

Stdlib + pyyaml only. The citation grader REUSES the lint_skills rule-9 resolver
(no second resolver). The report grader REUSES generate_report.py's validate_model
+ generate (no re-derived schema).
"""

from .deid import grade_deid
from .citation import grade_citation
from .report import grade_report_produced

__all__ = ["grade_deid", "grade_citation", "grade_report_produced"]
