---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-EXPOSURE,
           ELI-OBLIGATIONS, ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-LOCATION: "The unit of a clause-5.2 policy is the organisation (or a named scope within it), captured in Q2 as legal name + scale + number/type of sites — not a single hazard location the way a confined-space RA has. A multi-site org gets one policy appropriate to its size; no separate location-hazard dimension branches the policy."
    ELI-BASELINE: "A policy is a forward commitment, not an assessment of a current state, so there is no maturity/conformance baseline to capture. Any existing policy the user wants reviewed is supplied as free-text context in Q3 (its named risks) rather than as a scored baseline."
    ELI-EVIDENCE: "The policy is not evidence-scored — it commits the organisation to the five clause-5.2 commitments. The 'evidence' is the org's named significant risks (Q3, the anti-boilerplate anchor) that each commitment is context-fit to, captured as free-text, not a numbered evidence log."
    ELI-SCORING: "A policy has no likelihood×severity matrix or maturity scale; it is a structured composition over the five mandatory clause-5.2 commitments, not a calculation. There is no numeric score chosen at intake."
  branches:
    - {when: Q4, option: India, activates_questions: [Q4a], activates_kb_row: KB-REG-IN-FACTORIES, mandatory: true}
---

# Structured intake — hse-policy-generator

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ
where the answer space is enumerable and free-text where it is open; branch on the answers;
**echo the captured facts back for confirmation before any drafting**. This skill **generates
a top-management-signed ISO 45001 clause-5.2 OH&S policy** that is **context-fit to the named
organisation's actual risks** — it does **not** emit a generic boilerplate policy.

**Two hard refuse-on-vague anchors:** **Q2** (a named organisation + its scale) and **Q3**
(the org's **actual significant risks** — refuse a "generic safety policy" naming no real
risk). The **mandatory India→state branch** (Q4 = India → Q4a) **defers to `hse-india`**,
resolves the state before citing any statutory written-policy duty, and **never mints a
national form number**.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **Standard selector** (which policy) | MCQ | ISO 45001 — OH&S (default) / ISO 14001 — environmental / ISO 45003 — psychosocial / Combined → selects the clause-5.2 variant in `KB-SNIP-POLICY-COMMITMENTS` | ELI-SCOPE | always |
| Q2 | **Named organisation + scale** (the specificity anchor) | free-text | "Which organisation is this policy for — its legal name, headcount band, and the number/type of sites? (e.g. 'AcmeCo Ltd, ~140 staff, two warehouses + a chemical store')." **Refuse a request with no named org or scale.** | ELI-SUBJECT | always |
| Q3 | **Sector + the org's actual significant risks** (the anti-boilerplate anchor) | free-text | "What are this organisation's **real** significant HSE risks and its sector? (e.g. forklift traffic, working at height, solvent exposure, lone driving, psychosocial load)." **Refuse 'just a generic safety policy' — every commitment is context-fit to these named risks.** | ELI-INDUSTRY | always |
| Q4 | **Jurisdiction** (statutory written-policy duty) | MCQ | UK / USA / EU / India / Other / Unknown (India → Q4a) — this sits **beside** the policy, never inside it | ELI-JURIS | always |
| Q4a | *(India only)* Which state? | MCQ | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; defers to `hse-india`; never a national form number** | ELI-JURIS | Q4 == India |
| Q5 | **Workforce / worker-representation context** | MCQ + free-text | Union / safety-rep / committee present? trained workforce size — drives the consultation-and-participation commitment (5) and the "appropriate to size" test | ELI-EXPOSURE | always |
| Q6 | **Legal + other requirements** | free-text | "Which legal duties and other requirements (customer codes, ISO certification scope, group standards) does the policy commit to fulfil?" — drives commitment (2) | ELI-OBLIGATIONS | always |
| Q7 | **Output artifact + reader** | MCQ | Signable policy document (board) / Policy + implementation note (leadership) / Policy statement only — and its audience (M / C / E) | ELI-OUTPUT | always |
| Q8 | **Top-management signatory** | free-text | "Which **role/title** will sign the policy (clause 5.2 requires top-management commitment)? — a **role**, e.g. 'Managing Director', never a personal name" | ELI-COMPETENCY | always |
| Q9 | **Communication + review cycle** | MCQ + free-text | How the policy is communicated (induction / intranet / display) + review cadence (annual / on change / other + date) | ELI-TEMPORAL | always |

**Branch map:** `standard-variant` (Q1 = ISO 14001 / ISO 45003 → swap the clause-5.2 variant);
`india-state` (Q4 = India → Q4a; **mandatory**, defers to `hse-india`).

## Echo-back

After the last applicable question (Q9, and Q4a if the India branch ran), **echo a
captured-facts summary** and confirm before any drafting:
"Producing: an ISO 45001 clause-5.2 OH&S policy for AcmeCo Ltd (~140 staff, two warehouses +
a chemical store), context-fit to its real risks (forklift traffic, solvent exposure, lone
driving), UK, signed by the Managing Director, communicated at induction + reviewed annually —
correct?" Confirm the org and its named risks before any drafting.

## Refuse-on-vague anchors

- **Q2 is the specificity anchor** — refuse a request with no named organisation or scale
  ("write me a safety policy"); require the org's legal name, headcount band, and sites.
  Record `[ASSUMPTION]` / `[GAP]`, never invent.
- **Q3 is the anti-boilerplate gate** — **refuse 'just give me a generic safety policy'**
  naming no real risk. Require the org's **actual significant risks**; a policy reciting the
  five commitments but naming no concrete hazard fails specificity. Flag `[GAP]` and elicit
  the real risk before drafting.
- **India statutory written-policy duty** — **defer to `hse-india`** (Q4 = India → Q4a):
  resolve the **state first**; **never mint a national form number** (`[GAP]` when
  unverified). This never hard-blocks the policy.

## Evidence types (the context-fit inputs, not a scored evidence log)

The org's **named significant risks** (Q3) · its **legal + other requirements** (Q6) · its
**workforce/representation context** (Q5). These are the inputs each commitment is context-fit
to — handled under `references/deid-checklist.md` (any personal identifier → role/title label)
before any drafting.
