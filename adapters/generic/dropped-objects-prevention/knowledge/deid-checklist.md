# De-identification Checklist — dropped-objects-prevention (A5, lower tier)

> The deep reference the mandatory `hse:block:deid` block points to. Apply it BEFORE
> drafting any output. A de-identification leak is an eval **hard-fail** (A8) and
> cannot be waived. The byte-identical `deid` block is the contract; this checklist is
> the skill-authored reinforcement (CONV-7) — the block text is never edited.

## Tier — LOWER (asset/installation data dominates)

A dropped-objects-prevention artifact is **mostly asset/installation data** — at-height
inventories, securing standards, DROPS survey findings, masses and fall heights — which carry **no
personal data**. This is the **lower de-id tier**. The one sensitive surface is a **prior struck-by
/ fatality dropped-object incident** cited as context: a named injured/killed worker from that
incident is **special-category health data** (GDPR Art. 9 / India DPDP / OSHA privacy-case). The
de-id pass therefore focuses on the prior-incident context, not the asset data.

## The five steps (apply BEFORE drafting)

1. **DETECT & FLAG** every personal/health identifier in the inputs and **list them up front** —
   names (esp. an injured/killed worker from a prior dropped-object incident), contact numbers,
   employee/badge IDs, exact dates, precise crew/shift, photos showing faces, and any medical
   outcome. If unsure whether something is identifying, treat it as identifying.
2. **PSEUDONYMIZE BY DEFAULT** to stable **role labels** ("Deck Crew (role)", "Banksman (role)",
   "Injured worker (role)") for any output that will circulate. Keep the **re-identification key
   SEPARATE** — never put the key or any name↔label mapping in the document.
3. **AGGREGATE SMALL NUMBERS** — never publish a dropped-object struck-by / injury cell of **fewer
   than 5** individuals; aggregate up and apply secondary suppression so a suppressed cell cannot be
   back-calculated from totals. A `<5` struck-by cell on a named installation de-anonymizes the
   worker involved.
4. **WARN BEFORE WIDE DISTRIBUTION** — the DROPS register and survey report default to
   de-identified / aggregated; warn the user before any name or health detail enters a widely
   shared artifact.
5. **MINIMIZE & LIMIT PURPOSE** — the survey needs the at-height item, its securing status, and the
   mass/height; it does **not** need the injured worker's name. Carry prior-incident context at
   **role level only**.

## Workflow de-id step (reinforcement)

The **De-identifier subagent runs FIRST** (sequential dependency) — it scrubs the prior struck-by /
fatality context to role labels before any survey analysis, and returns the re-identification key
SEPARATELY to the orchestrator, never to a sibling. Every downstream job consumes only the scrubbed
output.

## Golden eval-output convention (`evals/output/*.md`)

When you author this skill's golden output (the LOCKed exemplar the grader scores against):

1. **Owners by role label, never a realistic personal name** ("DROPS Coordinator (role)", "OIM
   (role)"). A personal name reads as a de-id leak; the role fully satisfies the "named owner"
   defensibility requirement.
2. **No process meta-narration in the deliverable prose** — cut "de-identification ran first" /
   "(by design)" lines from the artifact body. KEEP the honest `[ASSUMPTION]` / `[GAP]` flags.
3. **Representative deliverable depth** — real DROPS register density, no padding.

Full convention + do/don't examples: `docs/AUTHORING_GUIDE.md` section 7 (Golden eval-output
authoring).
