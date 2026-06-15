<!-- TODO: author this skill's Workflow body (the standalone-fallback skeleton) -->

This is the generic Workflow skeleton `scaffold.py` seeds into a new skill's
`SKILL.md` when `skill-creator` is unavailable (the standalone fallback, A10 §3.3).
The five inline blocks and the seeded intake STEP are placed by the scaffolder; the
author replaces the analyse → method → validate → output spine below with the
skill's real domain method.

## Workflow (skeleton)

1. **Structured intake** — the seeded `templates/intake-todo.md` STEP. Author the
   skill's domain question set here (one question at a time, MCQ where enumerable,
   free-text where open; branch and echo facts back before any drafting). The
   runtime intake pattern is `KB-SNIP-INTAKE`.

2. **Analyse / apply the domain method** — author the method in
   `references/METHODOLOGY.md`. Ground every conclusion in evidence; resolve the
   jurisdiction first; apply the hierarchy of controls (`KB-SNIP-HOC`) to every
   control recommendation; never accept a vague or PPE-only treatment.

3. **Validate the draft** — against `references/QUALITY_CHECKLIST.md` (every finding
   traced to evidence; named owner + date on every action; de-id pass complete).

4. **Produce the output** — via the `report-output` block: assemble one `report.json`
   and render the branded DOCX + PDF through the shared engine.

5. **Critic / QA** — the mandatory adversarial final pass (orchestration Step 4).
