<!-- KB-SNIP-POLICY-COMMITMENTS -->
# OH&S policy commitments — ISO 45001 clause 5.2 mandatory set + context-fit

**Fragment ID:** `KB-SNIP-POLICY-COMMITMENTS`
**This is prompt text, applied by the model — not a generator.** It is the clause-5.2 commitment set
the `hse-policy-generator` skill builds a top-management-signed OH&S policy from. A generic template
that names no real risks **fails** the specificity gate — every commitment must reflect the named
org's actual risks and scale. The hazard-elimination commitment is phrased via `KB-SNIP-HOC`. The
India statutory written-policy duty **defers to `hse-india`** (CONV-8 — state detection first, no
national-form minting). Cited to the standard.

> Source: ISO 45001:2018 clause 5.2 (OH&S policy) · variants: ISO 14001:2015 clause 5.2 (environmental) · ISO 45003:2021 (psychosocial) · UK HSWA 1974 s.2(3) (written-policy duty, 5+ employees) · Year: 2026 · Reviewed: 2026-06-22 · Volatile: false.

---

## Instruction — the five mandatory clause-5.2 commitments

The OH&S policy **must** include commitments to:

1. provide a **framework for setting OH&S objectives**;
2. **fulfil legal requirements and other requirements**;
3. **eliminate hazards and reduce OH&S risks** (ranked via the hierarchy of controls — phrase through
   `KB-SNIP-HOC`, never a PPE-only or admin-only statement);
4. **continual improvement** of the OH&S management system;
5. **consultation and participation** of workers (and workers' representatives where they exist).

A policy missing any of these five commitments fails the citation-accuracy gate.

## Plus — the clause-5.2 characteristics

- **Appropriate to the purpose, size and context** of the organisation and the specific nature of
  its OH&S risks (the anti-boilerplate test).
- Available as **documented information**; **communicated** within the organisation; available to
  interested parties.
- **Signed by top management** — clause 5.2 requires demonstrated top-management commitment.

## Variants (selected at intake)

| Variant | Clause / duty | When |
|---|---|---|
| Environmental policy | ISO 14001:2015 clause 5.2 | environmental management scope. |
| Psychosocial commitment | ISO 45003:2021 | psychosocial-risk policy statement. |
| UK statutory written policy | HSWA 1974 s.2(3) | 5+ employees in GB. |
| **India statutory written policy** | **defers to `hse-india`** | state detection first; **no national-form number minted** (CONV-8). |

## Anti-boilerplate context-fit guidance

Every commitment must reference the named organisation's **actual** risks and scale. A template that
recites the five commitments but names no real hazard, sector, or workforce context is **boilerplate**
and fails specificity. Tie each commitment to a concrete obligation or risk the org actually carries.

## How the skill uses this fragment

`hse-policy-generator` assembles the five mandatory commitments + the clause-5.2 characteristics,
selects the variant at intake, phrases hazard-elimination via `KB-SNIP-HOC`, context-fits to the named
org's risks, and produces a documented, communicated, **top-management-signed** policy — decision-support
only, reviewed by a competent person.
