<!-- KB-SNIP-SME-QA -->
# SME Review & Sign-off — canonical mandatory-gate pattern

**Fragment ID:** `KB-SNIP-SME-QA`
**This is prompt text — the mandatory review gate every skill runs before ANY output.**

> Source: A6 orchestration §3 / A8 §4.5 SME-review · Year: 2026 · Reviewed: 2026-06-20 · Volatile: false.

---

## The gate (run after synthesis, before ANY output — markdown OR rendered)

1. **Adopt the skill's SME persona** from `references/sme-review.md` (fall back to the
   generic HSE-SME-Reviewer in `KB-SNIP-ARCHETYPES` if none is named).
2. **Apply BOTH** of these in the same pass:
   - the **universal hard gates** — no error or unsupported claim, every regulatory
     trigger caught, no lower-order-only (PPE/admin-only) control without a
     justify-or-escalate note, and **ZERO de-identification leak**; and
   - the **persona's domain checklist** in `references/sme-review.md`.
3. **The review MUST PASS before any output is presented** — markdown OR a rendered
   PDF/DOCX. Fix everything it raises and **re-run until clean**.
4. Stamp the artifact with the provenance line below.

## Platform-neutral degradation (§2.5)

On a host without subagents, perform the review yourself in-context — same persona,
same checklist, same gate — before presenting markdown or a rendered PDF/DOCX.

## Boundary (SME-02 / SME-03)

Decision-support only. This review **PRECEDES — and never replaces, never emits — the
human competent-person sign-off**. It never outputs "approved by a competent person".

## Provenance line (stamp on the artifact)

> "SME review: ran (persona: \<role\>); decision-support — competent-person review still required."

See also: `KB-SNIP-ARCHETYPES` (the HSE-SME-Reviewer hook + sector-persona slots).
