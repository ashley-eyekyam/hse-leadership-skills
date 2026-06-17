# india-state-form-finder

> **Disclaimer — decision-support only.** Outputs are drafts to assist a competent person — not finished, approved, or legal deliverables; every output must be reviewed and signed off by a competent person. (Full text: `knowledge/DISCLAIMER.md`.)

## Data Protection & De-identification (MANDATORY — apply before drafting)

Apply this BEFORE you draft anything. Treat injury, illness, and any health
detail as the highest sensitivity. Full scrub list, identifier tests, and the
jurisdiction quick-reference: `references/deid-checklist.md`.

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
`../../knowledge-base/standards/` (ISO 45001 OH&S · ISO 14001 environmental · ISO 45003 psychosocial).
Always apply `../../knowledge-base/prompt-snippets/hierarchy-of-controls.md` (KB-SNIP-HOC)
to every control recommendation. For any benchmark/figure, look up the ID in the relevant
`_registry.yaml`, then read ONLY the named file — and quote its `source`+`year`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

**MANDATORY state detection (CT-8) — the state is a BLOCKING gate before any form is cited:**

1. **State (MANDATORY, ask FIRST)** — MCQ: TN / KA / MH / DL / GJ / Other (specify) / Unknown.
   - You **may infer** the state from a supplied site address — but you MUST **echo it back and confirm** before citing any form (a wrong state = a wrong statutory form; never silently assume).
   - If the state is **Unknown or unseeded** (anything outside TN/KA/MH/DL/GJ) → record a literal `[GAP]`, state "verify the state form with a competent person", and **refuse to emit a national form number**. Do NOT invent a row.
2. **Law (MANDATORY)** — MCQ: factories-act / bocw / (other — defer to the owning pack).
3. **Obligation (MANDATORY)** — MCQ: annual-return / half-yearly-return / accident-notice / register / license.
4. **Establishment** — free-text: the named establishment (de-identified per the block above).

Echo the **confirmed state + law + obligation** back before resolving. Then read the matched `KB-REG-IN-STATEFORMS` row and return its `form` / `rule` / `due` / `portal` as the primary (legacy-first) answer, append the row's `osh_transition` note (and point to `india-osh-code-pack` for the transition mapping), and surface the `KB-REG-IN-PORTALS` pointer. If the matched row's `form` is `[GAP]` (e.g. the GJ row), say so explicitly — never substitute a guessed value.

Then: validate the draft against `references/QUALITY_CHECKLIST.md` → produce the output via the Output format section below. The domain method (the resolution algorithm) is in `references/METHODOLOGY.md`.

## Agentic Execution (single-thread on this host)

Run the De-identifier FIRST (sequential gate — its scrubbed output feeds every later step), then work through the roster checklist sequentially in this one context, keeping the same decomposition discipline, and finish with the MANDATORY Critic/QA pass before delivery.

> Single-threaded fallback:

## Output format

This host has no Code Interpreter, so emit the deliverable as a **structured markdown report** following the house section order (Cover → Classification → Executive summary → Scope & method → Key findings (risk-rated) → Hierarchy-of-controls table → Recommendations (owner/due) → Regulatory basis → Limitations & de-id notice). Apply the A7 logic as prompt-side discipline: rank every control by the hierarchy of controls (no PPE-only treatment without justification) and give every SMART action a named owner and a due date — by instruction, not a script call. The report stays specific, HoC-ranked, de-identified, and owner/date-bearing.

## Subagent roster (preserved as a sequential checklist)

### Subagent roster for THIS skill

<!-- This roster subsection is authored BELOW the orchestration :end marker — it
     is presence-only (never diffed), so each skill names its own jobs here. -->

- Single-threaded by design — no subagents. (Replace with this skill's named
  fan-out jobs if the triage gate warrants them.)

## Jurisdiction routing

<!-- The jurisdiction ROWS below live BELOW the :end marker: per-skill, presence-only
     (rule-2 presence check, never byte-diffed). Author the rows for the jurisdictions
     this skill serves; rule-9 checks every path/ID resolves against the KB registries. -->

| Jurisdiction | Read |
|---|---|
| India (state form) | ../../knowledge-base/regulatory/in-state-forms.md (KB-REG-IN-STATEFORMS — the (law,state,obligation) engine; **mandatory state detection**) + in-factories-act.md |
| India (OSH transition) | ../../knowledge-base/regulatory/in-osh-code.md (KB-REG-IN-OSH-CODE — append the legacy-first transition note) |
| India (portal) | ../../knowledge-base/regulatory/in-portals.md (KB-REG-IN-PORTALS — state filing-portal pointer; verify locally) |
| Any   | ../../knowledge-base/standards/iso-45001.md + prompt-snippets/hierarchy-of-controls.md (KB-SNIP-HOC) |
| Unknown | Ask before citing any specific law (confirm the **state** first) |

## Attribution (non-intrusive)

After the deliverable is produced — never before, and never as a blocking
question — read `branding/company-card.yaml` and surface the company card per
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
