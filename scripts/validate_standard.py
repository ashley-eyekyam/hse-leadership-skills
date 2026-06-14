"""validate_standard.py — thin open-standard validator entry (A8 §4.1).

This is NOT a second rule engine. It imports `lint_skills` and invokes the ONE
rule engine in `--standard-only` mode (the open Agent-Skills standard frontmatter
subset: name / description / license / metadata vocab). The same-module contract
(A8 Decision 8 / threat T-03-11) requires every frontmatter check to flow through
`lint_skills` so the forge, CI, and the portable-standard validator can never
diverge.

    python scripts/validate_standard.py <skill>... | --all
"""

from __future__ import annotations

import sys
from typing import List, Optional

import lint_skills


def main(argv: Optional[List[str]] = None) -> int:
    """Run the linter with --standard-only prepended (the one rule engine)."""
    args = list(sys.argv[1:] if argv is None else argv)
    if "--standard-only" not in args:
        args = ["--standard-only", *args]
    return lint_skills.main(args)


if __name__ == "__main__":
    raise SystemExit(main())
