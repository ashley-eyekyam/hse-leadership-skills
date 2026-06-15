# Contributing to HSE Leadership Skills

Thank you for contributing. This file is the contributor contract. It **points at** the
machine-enforced quality gate, the versioning scheme, the skill contract, and the
dual-review path — it does not restate them. Follow the links for the authoritative detail.

By participating you agree to abide by our [Code of Conduct](./CODE_OF_CONDUCT.md).

## The quality gate

Every skill PR is gated. A change merges only when, in order:

1. The **linter** passes (green).
2. **≥3 evals** run with a weighted score **≥4.0** and **no hard-fail**. Two failures are
   never waivable: a **de-identification leak is an automatic fail**, and an
   **invented / unverifiable regulatory citation is a fail**.
3. A **competent person** completes the HSE-accuracy review.

Run evals **locally before you push** — the model-graded score runs on your Claude
subscription via `python3 scripts/run_evals.py --changed` (CI enforces only the
deterministic hard-blocks + lint, not the ≥4.0 score). Commands and the local-vs-CI
split are in [`docs/AUTHORING_GUIDE.md` §7](./docs/AUTHORING_GUIDE.md#7-local-eval--lint-commands--the-quality-gate).

The full rule detail (the linter rule list, the per-skill folder layout, the six-block
contract) lives in [`docs/AUTHORING_GUIDE.md`](./docs/AUTHORING_GUIDE.md) — read it before
authoring. This file does not duplicate those rules.

## Versioning

- Bump the per-skill **`metadata.version`** (semver) whenever you change a skill.
- Repo releases are tagged **`vX.Y.Z`** (the first public tag is `v1.0.0`).
- Record every change in [`CHANGELOG.md`](./CHANGELOG.md) under `## [Unreleased]`.

## Authoring a skill

- Use **`hse-skill-forge`** (which wraps `skill-creator`) to scaffold a born-conformant skill.
- Every skill satisfies the **six-block contract**: five inline `hse:block:*` regions
  (orchestration, de-identification, kb-selection, report-output, attribution) plus the
  `evals/` folder and `branding/company-card.yaml`. See
  [`docs/AUTHORING_GUIDE.md`](./docs/AUTHORING_GUIDE.md).
- Every skill's **Workflow opens with structured intake** — a multi-step MCQ + free-text
  Q&A, one question at a time, echoing facts back before analysis. This is a Workflow
  convention, not a seventh block. The evals **reward elicited specificity** and penalize
  unstated assumptions, so do not skip intake.

## Review path

Reviews are dual and path-scoped (see [`.github/CODEOWNERS`](./.github/CODEOWNERS)): an
**HSE competent-person reviewer** owns accuracy/defensibility paths (`skills/`,
`knowledge-base/`, `template/blocks/`, `DISCLAIMER.md`), and a **format/code reviewer**
owns code/CI/schema paths. Safety-critical paths request both.

## Disclaimer

All outputs of this pack are **decision-support only** and must be reviewed by a competent
person before they are relied upon; nothing produced is legal advice. By contributing you
acknowledge and preserve the [**DISCLAIMER**](./DISCLAIMER.md) — never weaken or remove it.
