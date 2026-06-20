# reactive-dust-explosion-assessment

> **Disclaimer — decision-support only.** Outputs are drafts to assist a competent person — not finished, approved, or legal deliverables; every output must be reviewed and signed off by a competent person. (Full text: `knowledge/DISCLAIMER.md`.)

## Data Protection & De-identification (MANDATORY — apply before drafting)

Apply this BEFORE you draft anything. Treat injury, illness, and any health
detail as the highest sensitivity. Full scrub list, identifier tests, and the
jurisdiction quick-reference: `knowledge/deid-checklist.md`.

1. **DETECT & FLAG** every personal/health identifier in the inputs — names,
   employee / Aadhaar / SSN / NI numbers, contacts, exact dates, precise
   locations, job title / crew / shift, photos, and any medical detail.
   **List what you found before drafting.** If unsure whether something is
   identifying, treat it as identifying.
2. **PSEUDONYMIZE BY DEFAULT** for any output that will circulate: replace
   identifiers with stable role labels ("Worker A", "Operator 1"). Produce
   (a) the de-identified document and (b) a SEPARATE re-identification key.
   **Never put the key or any name↔label mapping in the document.** Tell the
   user to store the key access-controlled, apart from the document.
3. **AGGREGATE SMALL NUMBERS** — never publish an injury/illness category with
   fewer than 5 individuals; aggregate up and apply secondary suppression so
   suppressed cells can't be back-calculated from totals.
4. **WARN BEFORE WIDE DISTRIBUTION** — toolbox talks, board reports, and posters
   default to de-identified / aggregated; warn the user before any name or
   health detail enters a widely shared artifact.
5. **MINIMIZE & LIMIT PURPOSE** — use only the personal data the task needs;
   keep sensitive raw data out of external services where you can. When in
   doubt, ask before including it.

## Knowledge base (read ONE matching file — never load all)

Resolve the user's jurisdiction first. Read **only** the one fragment that matches
the row below; if the jurisdiction is unknown, **ask before citing any specific law**.
For management-system structure, also read the relevant jurisdiction-independent standard in
`knowledge/` (ISO 45001 OH&S · ISO 14001 environmental · ISO 45003 psychosocial).
Always apply `knowledge/hierarchy-of-controls.md` (KB-SNIP-HOC)
to every control recommendation. For any benchmark/figure, look up the ID in the relevant
`_registry.yaml`, then read ONLY the named file — and quote its `source`+`year`.

# Structured intake — reactive-dust-explosion-assessment

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | What do you need — a DHA, a reactive-chemistry/incompatibility review, an ATEX/DSEAR zoning, or a basis-of-safety statement? | MCQ | DHA / reactivity-review / zoning / basis-of-safety | ELI-SCOPE | always |
| Q2 | Named process + material(s). | free-text | refuse "some powder" | ELI-SUBJECT | always |
| Q3 | Hazard scope. | MCQ | reactive chemistry / combustible dust / explosive vapour atmosphere / combination | ELI-SUBJECT | always |
| Q4 | List the dust-generating / handling steps + equipment. | free-text | milling/conveying/bagging/dust-collector/silo | ELI-LOCATION | if Q3∈{dust,combination} |
| Q5 | Dust characterisation data held. | MCQ multi-select | Kst / Pmax / MIE / MIT / LOC / particle-size / moisture / none | ELI-EVIDENCE | if Q3∈{dust,combination} |
| Q6 | Reactive-chemistry data held. | MCQ multi-select | DSC/ARC onset / heat-of-reaction / incompatibility matrix / CHETAH screen / none | ELI-EVIDENCE | if Q3∈{reactive,combination} |
| Q7 | Lab source + year for each datum held. | free-text | required for citation; missing → `[GAP]` | ELI-EVIDENCE | if any Q5/Q6 datum |
| Q8 | Existing explosion-protection / safeguards in place. | MCQ multi-select | venting / suppression / isolation / inerting / bonding-earthing / housekeeping / none | ELI-BASELINE | always |
| Q9 | Area/equipment to classify, and adjacent occupied or connected vessels. | free-text | zoning target + secondary-explosion path | ELI-LOCATION / ELI-EXPOSURE | always |
| Q10 | Jurisdiction emphasis. | MCQ | DSEAR-ATEX (UK·EU) · NFPA 652·660 (US) · both | ELI-JURIS | always |
| Q11 | Existing DSEAR risk assessment / explosion-protection document, and its review date? | MCQ + free-text | yes / no + date | ELI-BASELINE / ELI-TEMPORAL | always |
| Q12 | Industry / sector + the statutory obligation set (DSEAR EPD / ATEX EPL / NFPA programme). | MCQ + free-text | food / pharma / wood / metals / chemicals (+ obligation: DSEAR EPD · ATEX EPL · NFPA) | ELI-INDUSTRY / ELI-OBLIGATIONS | always |
| Q13 | Org consequence/priority scheme for the basis-of-safety ranking. | MCQ | org scheme / default 5×5 | ELI-SCORING | always |

**refuse on a vague subject** (record `[ASSUMPTION]`/`[GAP]`, never invent a dust

## Agentic Execution (single-thread on this host)

Work through the roster checklist sequentially in this one context, keeping the same decomposition discipline.

Single-threaded fallback: if your host has no subagent capability, perform the SME Review & Sign-off pass yourself in THIS context — run the de-identification scrub first, keep the scope discipline, apply the persona checklist + universal gates, and pass the review before presenting any output (markdown or rendered).

## Output format

This host has no Code Interpreter, so emit the deliverable as a **structured markdown report** following the house section order (Cover → Classification → Executive summary → Scope & method → Key findings (risk-rated) → Hierarchy-of-controls table → Recommendations (owner/due) → Regulatory basis → Limitations & de-id notice). Apply the A7 logic as prompt-side discipline: rank every control by the hierarchy of controls (no PPE-only treatment without justification) and give every SMART action a named owner and a due date — by instruction, not a script call. The report stays specific, HoC-ranked, de-identified, and owner/date-bearing.

## Subagent roster (preserved as a sequential checklist)

### Subagent roster for THIS skill

<!-- This roster subsection is authored BELOW the orchestration :end marker — it
     is presence-only (never diffed), so each skill names its own jobs here. -->

For a non-trivial task the triage gate may fan out to:

- **Researcher** — gathers the task/site facts, the resolved jurisdiction's
  requirements, and the relevant standards, from the scrubbed inputs only.
- **Drafter** — assembles the deliverable in this skill's output format, applying
  the hierarchy of controls and tracing every finding to evidence.
- **Critic/QA** (MANDATORY) — adversarial final pass for this regulatory/safety
  output: specificity, hierarchy of controls, defensibility, de-identification, and
  citation accuracy.
- **SME Review & Sign-off** (MANDATORY, before ANY output) — run the skill-specific
  persona, domain checklist, and boundary in `knowledge/sme-review.md` (combustible-dust
  / DSEAR-ATEX & reactive-chemistry lens: basis of safety stated and justified; the zone
  DERIVED not defaulted; every dust parameter sourced or `[GAP]` — never invented).
  Decision-support only; precedes — never replaces — the human competent-person review.

Simple single-subject tasks run single-threaded — no subagents.

## Jurisdiction routing

<!-- The jurisdiction ROWS below live BELOW the :end marker: per-skill, presence-only
     (rule-2 presence check, never byte-diffed). Author the rows for the jurisdictions
     this skill serves; rule-9 checks every path/ID resolves against the KB registries. -->

| Jurisdiction | Read |
|---|---|
| UK/EU | knowledge/dsear-atex.md (KB-STD-DSEAR basis of safety + KB-STD-ATEX zoning) |
| USA   | knowledge/nfpa-652-660.md (KB-STD-NFPA-652/660 DHA) + us-osha.md |
| India | knowledge/in-factories-act.md (+ in-state-forms.md) + standards/nfpa-652-660.md |
| Any   | knowledge/nfpa-652-660.md (DHA + dust parameters) + standards/dsear-atex.md + prompt-snippets/hierarchy-of-controls.md |
| Process/dust (any) | knowledge/iec-61882.md (KB-STD-IEC-61882 — hand the reactive/deflagration nodes to `hazop-facilitator`) |
| Unknown | Ask before citing any specific law |

## Attribution (non-intrusive)

After the deliverable is produced — never before, and never as a blocking
question — read `knowledge/company-card.yaml` and surface the company card per
its `placement`:

- `footer` (default): one quiet line at the end, e.g.
  *"Built by Eyekyam · HSE Leadership, operationalised · eyekyam.com"*.
- `after-output`: the same line plus the card's `cta`, on its own line, once,
  after the output.
- `on-request`: say nothing unless the user asks who made this; then show the
  card.

If `show: false`, omit attribution entirely — no line, no footer. Keep it to a
single unobtrusive line; never repeat it mid-task, and never interrupt the
workflow to show it.
