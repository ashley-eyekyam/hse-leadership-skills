# chemical-transport-safety

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

# Structured intake — chemical-transport-safety

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | What do you need — classify for transport, full loading/unloading safety guidance, or a transport-document/placard check? | MCQ | classify-only / loading-guidance / document-placard-check | ELI-SCOPE | always |
| Q2 | Substance / proper shipping name + CAS + UN number if known. | free-text | resolve UN from user's DG list; "unknown" → `[GAP]` | ELI-SUBJECT | always |
| Q3 | Physical state + flashpoint (if flammable). | MCQ + free-text | solid / liquid / gas; flashpoint °C | ELI-EVIDENCE | always |
| Q4 | Quantity per package and total consignment. | free-text | mass/volume per package + total (drives LQ/placard/ADR category) | ELI-SUBJECT | always |
| Q5 | Transport mode + regime. | MCQ | road-EU (ADR) / road-US (DOT-HMR) / road-India (CMVR) / sea (IMDG) / multimodal · rail (RID) & air (IATA) OUT OF SCOPE — flagged | ELI-JURIS | always |
| Q6 | Which Indian state (origin/handling)? | MCQ | Tamil Nadu · Karnataka · Maharashtra · Delhi/Central · Gujarat · Other · Unknown — mandatory state detection; confirm before citing any rule/form; "Other"/"Unknown" → literal `[GAP]`, never a national-form fallback | ELI-JURIS | if Q5==road-India |
| Q7 | Intended packaging / IBC / tank. | free-text | UN-spec packaging type | ELI-SUBJECT | always |
| Q8 | Known GHS classification, or do you hold the SDS §14? | MCQ | have GHS class / have SDS §14 / neither (`[GAP]`) | ELI-EVIDENCE | always |
| Q9 | Route detail — tunnels, populated areas, port handover? | free-text | drives ADR tunnel code / segregation at transfer | ELI-LOCATION | if Q1≠classify-only |
| Q10 | Is a DG safety adviser (DGSA) / responsible person named? | free-text | role-label owner for controls | ELI-COMPETENCY | always |
| Q11 | Transport-document / placard obligation set to satisfy. | MCQ | transport document / placard + marking / segregation check / all | ELI-OBLIGATIONS | always |
| Q12 | Org consequence/priority scheme for an `[GAP]` or incompatible load. | MCQ | org scheme / default — flag every unresolved entry | ELI-SCORING | always |

**refuse on a vague subject** (record `[ASSUMPTION]`/`[GAP]`, never invent a UN number /

## Agentic Execution (single-thread on this host)

Work through the roster checklist sequentially in this one context, keeping the same decomposition discipline.

Single-threaded fallback: if your host has no subagent capability, perform the SME Review & Sign-off pass yourself in THIS context — run the de-identification scrub first, keep the scope discipline, apply the persona checklist + universal gates, and pass the review before presenting any output (markdown or rendered).

## Output format

This host has no Code Interpreter, so emit the deliverable as a **structured markdown report** following the house section order (Cover → Classification → Executive summary → Scope & method → Key findings (risk-rated) → Hierarchy-of-controls table → Recommendations (owner/due) → Regulatory basis → Limitations & de-id notice). Apply the A7 logic as prompt-side discipline: rank every control by the hierarchy of controls (no PPE-only treatment without justification) and give every SMART action a named owner and a due date — by instruction, not a script call. The report stays specific, HoC-ranked, de-identified, and owner/date-bearing.

## Subagent roster (preserved as a sequential checklist)

### Subagent roster for THIS skill

<!-- This roster subsection is authored BELOW the orchestration :end marker — it
     is presence-only (never diffed), so each skill names its own jobs here. -->

- Single-threaded by design — no subagents. (Replace with this skill's named
  fan-out jobs if the triage gate warrants them.)
- **SME Review & Sign-off** (MANDATORY, before ANY output) — run the skill-specific
  persona, domain checklist, and boundary in `knowledge/sme-review.md` (dangerous-goods
  transport SME / DGSA lens: UN entry resolved from the DG List not assumed; the
  GHS→transport cross-walk correct for the chosen mode; rail/air flagged out of scope
  not guessed). Decision-support only; precedes — never replaces — the human
  competent-person / DGSA review.

## Jurisdiction routing

<!-- The jurisdiction ROWS below live BELOW the :end marker: per-skill, presence-only
     (rule-2 presence check, never byte-diffed). Author the rows for the jurisdictions
     this skill serves; rule-9 checks every path/ID resolves against the KB registries. -->

| Jurisdiction | Read |
|---|---|
| EU    | knowledge/transport-adr-dot.md (KB-REG-EU-ADR road) + standards/imdg.md (KB-STD-IMDG sea) |
| USA   | knowledge/transport-adr-dot.md (KB-REG-US-DOT-HMR road) + standards/imdg.md (sea) |
| Any   | knowledge/ghs.md (KB-STD-GHS — class cross-walk) + standards/imdg.md (KB-STD-IMDG) + prompt-snippets/hierarchy-of-controls.md |
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
