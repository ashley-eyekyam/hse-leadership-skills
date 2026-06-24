# Pre-output Quality Checklist — regulatory-returns

The self-check loop before any output. A statutory return is defensible only if every
determination is traced to the named test, the correct form + the exact deadline are
identified, and the output is de-identified. Run this gate before assembling the report.

## Determination
- [ ] The **jurisdiction is resolved** (Q1) before any verdict, form, or deadline.
- [ ] Every recordability/reportability verdict **cites the test it applied**
      (`KB-DATA-RECORDABILITY-TESTS`) — OSHA 1904.5/.6/.7 or RIDDOR reg. 4/7/8.
- [ ] A **first-aid-only case is NOT logged as recordable**; an **over-7-day RIDDOR
      case is NOT missed** — the two classic errors are caught.
- [ ] Where a fact the test needs is missing, the verdict is **`[GAP]`-flagged**, not
      forced to a "yes" or a "no".

## Form + deadline
- [ ] The **correct form** is identified (OSHA 300 / 300A / 301 / 1904.41 electronic;
      RIDDOR category; EU member-state equivalent) from the verdict + return type (Q2).
- [ ] The **exact deadline** is calculated from the jurisdiction's rule + the period
      (RIDDOR 15-day; OSHA 300A Feb 1–Apr 30 posting + 1904.41 date) — **never a
      deadline without the jurisdiction**.

## India deferral
- [ ] For India, **mandatory state detection ran first** and the leg **routes to
      `hse-india`** (`factories-act-returns` / `india-accident-notice` /
      `india-state-form-finder`) via the three-tier degrade.
- [ ] **No national India form number is minted** — an unverified form value is a
      `[GAP]`. The India branch **never hard-blocks**.

## De-identification (one of the 3 highest-sensitivity skills)
- [ ] The de-id pass ran **BEFORE drafting**; every identifier was detected and listed.
- [ ] The **legally-required submission** (named, access-controlled) is distinguished
      from every **internal / shared / working copy** (role-labelled).
- [ ] **`<5` suppression** applied to any aggregated summary (e.g. a 300A by department);
      no injury/illness cell of fewer than 5 is published.
- [ ] **No re-identification key** (and no name↔label mapping) is embedded in the return.

## Evidence + actions
- [ ] Every determination links to the **evidence item** that supports it.
- [ ] Every follow-up action carries a **named (role-label) owner + an ISO due date** —
      no anonymous actions, no "ASAP".
- [ ] No conclusion rests on an unstated assumption (`[ASSUMPTION]` recorded, not invented).
