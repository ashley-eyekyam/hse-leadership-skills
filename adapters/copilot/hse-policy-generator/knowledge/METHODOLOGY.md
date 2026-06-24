# Methodology — hse-policy-generator (ISO 45001:2018 clause-5.2 OH&S policy)

This skill produces a **top-management-signed OH&S policy** that satisfies **ISO 45001:2018
clause 5.2**, is **context-fit** to the named organisation's actual risks and scale (never
boilerplate), and **defers the India statutory written-policy duty to `hse-india`**. The
commitment set is `KB-SNIP-POLICY-COMMITMENTS`; the hazard-elimination commitment is phrased
via `KB-SNIP-HOC`; the bundle clause cross-walk is `KB-SNIP-LEADERSHIP-CLAUSE-MAP`.

> Source: ISO 45001:2018 clause 5.2 (OH&S policy) `[CITED: ISO 45001:2018 clause 5.2]` ·
> variants: ISO 14001:2015 clause 5.2 (environmental) · ISO 45003:2021 (psychosocial) ·
> UK HSWA 1974 s.2(3) (written-policy duty, 5+ employees).

---

## 1. The five mandatory clause-5.2 commitments

The OH&S policy **must** include commitments to:

1. **A framework for setting OH&S objectives** — the policy provides the basis from which
   measurable OH&S objectives are derived.
2. **Fulfilling legal requirements and other requirements** — the org's applicable legal
   duties and other requirements it subscribes to.
3. **Eliminating hazards and reducing OH&S risks** — ranked up the **hierarchy of controls**
   (`KB-SNIP-HOC`: eliminate → substitute → engineer → administrate → PPE). **Never** a
   PPE-only or admin-only commitment.
4. **Continual improvement** of the OH&S management system.
5. **Consultation and participation** of workers, and workers' representatives where they
   exist.

**A policy missing any one of these five commitments is a `regulatory_citation_accuracy`
HARD-FAIL.** Each is named explicitly; none is silently dropped or merged away.

## 2. The clause-5.2 characteristics

- **Appropriate to the purpose, size and context** of the organisation and the **specific
  nature of its OH&S risks** — the **anti-boilerplate test** (see §3).
- Available as **documented information**; **communicated** within the organisation;
  **available to interested parties**.
- **Signed by top management** — clause 5.2 requires demonstrated top-management commitment;
  the signatory is captured as a **role/title** (e.g. "Managing Director"), never personal data.

## 3. The anti-boilerplate context-fit test (the core-value lever)

Every commitment must reference the **named organisation's actual risks and scale**. A
template that recites the five commitments but names **no real hazard, sector, or workforce
context** is **boilerplate** and **fails specificity**. Method:

- From the intake, take the org's **named significant risks** (e.g. "forklift traffic in the
  two warehouses", "solvent exposure in the paint line", "lone driving"). Tie each commitment
  to a concrete obligation or risk the org **actually carries**.
- A generic "we are committed to safety" statement with no named risk is **refused** — record
  `[GAP]` and elicit the real risk, never invent one.
- "Appropriate to size" — a 12-person workshop and a 4,000-person multi-site operation get
  different policies; the commitment to objectives, legal compliance, and consultation scale
  with the organisation.

## 4. Variants (selected at intake, Q1)

| Variant | Clause / standard | When |
|---|---|---|
| OH&S policy (default) | ISO 45001:2018 clause 5.2 | occupational health & safety scope. |
| Environmental policy | ISO 14001:2015 clause 5.2 | environmental management scope. |
| Psychosocial commitment | ISO 45003:2021 | psychosocial-risk policy statement. |
| Combined | each selected standard's clause 5.2 | assemble each variant in turn. |

## 5. The statutory written-policy duty branch (beside the policy, never inside it)

Whether the **law compels a written policy** is a jurisdiction branch resolved separately
from the policy content:

- **UK** — HSWA 1974 **s.2(3)**: a written health-and-safety policy is required at **5+
  employees**.
- **India** — **defers to `hse-india`** (CONV-8): **resolve the STATE first**, route via the
  `hse-india` engine for the state-specific statutory position; **mint NO national-form
  number** (`[GAP]` when unverified). This **never hard-blocks** the policy.
- **USA / EU** — no single federal written-policy mandate (US, note state-plan variation);
  EU Framework Directive 89/391/EEC policy duty.

## 6. Defensibility & the SME boundary

The policy is **decision-support**: it is a draft for the organisation's own competent person
to review, and it **must not read as a final legal document**. The literal phrase "approved by
a competent person" never appears in the policy or the skill. The SME persona is the **Senior
HSE Manager / Director** (`references/sme-review.md`), who precedes — never replaces — the
human competent-person review.
