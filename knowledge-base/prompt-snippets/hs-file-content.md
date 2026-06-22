<!-- KB-SNIP-HS-FILE-CONTENT -->
# Health & Safety File — L153 Appendix-4 content list (CDM 2015 Reg 12(5))

**Fragment ID:** `KB-SNIP-HS-FILE-CONTENT`
**This is prompt text, applied by the model — not a generator.** It is the CDM 2015
Health & Safety File content list from HSE L153 Appendix 4, grounded in Regulation
12(5) (the principal designer prepares and maintains the file) and Reg 12(6)–(9)
(review, update, handover to the client at completion, client retention). It enforces
the **"could-not-reasonably-anticipate"** residual-hazard test. Consumed by
`health-and-safety-file` (CON-03).

> Source: CDM 2015 (SI 2015/51) Reg 12(5)–(9) + HSE L153 ACOP Appendix 4 · Year: 2026 · Reviewed: 2026-06-22 · Volatile: false.

---

## Instruction — the L153 Appendix-4 H&S file content list

The Health & Safety File is the **as-built residual-risk record** handed to the client
for future construction, maintenance, cleaning, refurbishment and demolition. Capture
only the information a future worker would need and **could not reasonably
anticipate** — not the full general specification. Walk these heads:

1. **Structure description & use** — what was built and its intended use.
2. **As-built & services information** — key as-built drawings, and the **location of
   services** and isolation points.
3. **Residual & unusual hazards** — the residual and unusual hazards (with locations) a
   future worker could not reasonably anticipate.
4. **Hazardous materials in situ** — materials left in place (asbestos register,
   coatings, insulation) and their locations.
5. **Cleaning / maintenance / refurb / demolition arrangements** — the safety
   information for future work on the structure.
6. **Information gaps** — unknowns recorded as `[GAP]`; revision control on the file.

## The residual-hazard test
Include an item only if a competent future worker **could not reasonably anticipate**
it from the structure itself. A file that dumps the full general spec instead of the
residual/unusual hazards is a specificity/defensibility failure.

## Discipline
- Preparation is the **principal designer's** duty (Reg 12(5)) — attributing it to the
  wrong duty-holder, or omitting the handover duty, is a citation failure.
- Maintenance/demolition arrangements still rank controls via `KB-SNIP-HOC`.

## How the skill uses this fragment
`health-and-safety-file` references `KB-SNIP-HS-FILE-CONTENT` for the content list and
the residual-hazard test, grounds the Reg 12(5) duty on `KB-REG-CDM2015`, and emits the
file. The PCI → CPP → H&S File chain is cross-walked in
`KB-SNIP-CONSTRUCTION-CLAUSE-MAP`.
