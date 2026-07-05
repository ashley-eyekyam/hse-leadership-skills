# Rule-13 fixtures (FND-05 — completeness / mode-manifest presence floor)

Minimal skill-shaped directories exercising `lint_skills._rule13_completeness`
in isolation. Each variant carries ONLY `references/sme-review.md` — the single
file rule 13 reads. They live under `scripts/tests/fixtures/` (NOT `skills/`),
so they are invisible to the catalog, the rubric re-stamp, and `lint --all`.

All fixture prose is deliberately generic placeholder text (no domain content).

| Variant | What it exercises |
|---------|-------------------|
| `well-formed/` | A structurally valid `modes:` map (1 mode, `detected_by`, 3 floor items each with `id`/`description`/`anchors`/`min_matches`, all anchors compile) plus an `## Omission lens` section referencing the completeness KB snippet id — must yield ZERO rule-13 findings. |
| `broken-modes/` | Multiple structural breaks at once: mode missing `detected_by`; floor with only 2 items (<3); an item missing `id`; an empty `anchors` list; `min_matches: 0`; and NO `## Omission lens` section — each break fires its own specific finding, all routed per `RULE_13_LEVEL`. |
| `bad-anchor/` | Identical to `well-formed/` except ONE anchor is an invalid regex (`([unclosed`). Proves an un-compilable author anchor is reported as a finding and NEVER raises (T-18-02-01 lint-time `re.error` safety). |

The paired test suite is `scripts/tests/test_rule13_completeness.py`, which pins:
WARN-routing under `RULE_13_LEVEL == "warn"`, ERROR-routing only under a
monkeypatched `"error"` level (the single-token Phase-20 flip), the zero-finding
clean pass, and the anchor-compile crash-safety.
