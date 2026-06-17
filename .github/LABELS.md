# Issue & PR label conventions

These labels seed the contribution funnel for HSE Leadership Skills. They are a
**convention** documented here (and applied in the repo's GitHub label set); the README's
"Roadmap & community" section links the filtered lists. The skill-authoring on-ramp itself
is [`hse-skill-forge`](../skills/hse-skill-forge/) and the
[`docs/AUTHORING_GUIDE.md`](../docs/AUTHORING_GUIDE.md).

## Contribution-funnel labels

| Label | Use it for | Linked from |
|---|---|---|
| `good first issue` | Small, well-scoped, low-context tasks ideal for a first-time contributor (a doc fix, a single eval case, a KB facet note). | README → [good-first-issues list](https://github.com/ashley-eyekyam/hse-leadership-skills/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) |
| `new-skill` | A proposal to add a new HSE skill (auto-applied by the [new-skill-proposal template](ISSUE_TEMPLATE/new_skill.md)). | The new-skill issue template |
| `help wanted` | Tasks the maintainers would welcome external help on. | README community section |
| `sme-review` | Needs competent-person HSE-accuracy review before it can merge (the quality gate). | The PR template + `CONTRIBUTING.md` |
| `de-id` | Touches the de-identification gate — the core-value hard-fail surface; extra review. | `CONTRIBUTING.md` |

## Good-first-issue convention

A `good first issue` should:

1. Be doable without deep knowledge of the build or the six-block contract.
2. Have a clear acceptance criterion in the issue body.
3. Not touch a hard-fail surface (de-identification, citation accuracy) — those carry the
   `de-id` / `sme-review` labels and need competent-person review.

Good first issues are how new HSE practitioners and developers start contributing — pair
them with the "contribute in 5 minutes with `hse-skill-forge`" CTA in the README.

## Featured community skills

Community-contributed skills that pass the quality gate (≥ 3 evals · weighted ≥ 4.0 · no
hard-fail · competent-person review) are featured in the README's "Featured community
skills" section. Submit via the [new-skill-proposal template](ISSUE_TEMPLATE/new_skill.md)
and the standard PR path — the same gate applies to every contributed skill.
