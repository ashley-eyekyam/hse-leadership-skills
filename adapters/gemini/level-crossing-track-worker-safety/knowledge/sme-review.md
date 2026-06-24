---
sme-review:
  personas:
    - role: "Level-crossing / track-worker safety SME (Network Rail safety-of-people-on-or-near-the-line competent person)"
      expertise: "NR/L2/OHS/019 (Safety of People Working On or Near the Line) practice, the level-crossing remedial hierarchy (closure -> grade separation -> engineering -> sighting/signage/admin), the track-worker protection hierarchy (separation/green-zone/line-blockage/possession -> SSOW -> warning/TOWS -> lookout-only), COSS role and Sentinel competence, ORR level-crossing strategic-risk guidance and the LXRMTK, and how the ALCRM model bands and prioritises crossings (a recorded model output, never recomputed in an artifact)"
      lens: "would a rail safety regulator / Network Rail competent person accept this safe system of work — is the crossing led by closure / grade separation / engineering (NOT new signage where a higher order is reasonably practicable), is the track work led by separation (green-zone / line blockage / possession, NOT a lookout alone), is the ALCRM band RECORDED from the user's licensed model output and never invented/recomputed, and is every COSS / Sentinel / lookout role-holder de-identified to a role label?"
---

# SME Review & Sign-off — level-crossing-track-worker-safety

This skill carries **one** SME lens, narrowing the level-crossing / track-safety archetype
(`KB-SNIP-ARCHETYPES`). The crossing-remediation view and the track-worker-protection view
are a lens *within* the same reviewer, so a 2nd persona is not justified. The universal hard
gates (de-id leak, citation accuracy, HoC/no-lower-order-only, owned-and-dated actions) are
the enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **The level-crossing treatment is led by the remedial hierarchy** — **closure → grade separation → engineering (barriers / obstacle detection / MSL / full-barrier) → sighting / signage / administrative LAST.** Flag any crossing whose *lead* control is new signage / admin while closure, grade separation, or engineering is reasonably practicable — that is the indefensible "controlled it with a sign" failure (`KB-SNIP-LX-HIERARCHY`).
- [ ] **The track-work system is led by separation** — **green-zone working / line blockage / possession → safe systems of work → warning (TOWS) → lookout-only LAST.** Flag any track task whose *lead* control is a lookout alone (red-zone) while separation is reasonably practicable; red-zone working must be minimised, never the default.
- [ ] **The ALCRM band is RECORDED, never invented or recomputed.** The artifact records the user's individual/collective band (or `[GAP]` if none was supplied) and uses it to prioritise the crossing. Flag any artifact that fabricates an ALCRM band, recomputes one, or hard-codes numeric ALCRM thresholds — the band values are the licensed RSSB/NR model output (D-03).
- [ ] **NR/L2/OHS/019 and the ALCRM/LX guidance are cited by reference, not reproduced.** The NR/L2/OHS/019 issue/date is `[ASSUMED A3]` → confirm the current issue/date is correct and citable before LOCK; never paste the standard's text.
- [ ] **The COSS / Sentinel competence framing is present and role-labelled** — the site-safety roles (COSS, lookout, PICOP, engineering supervisor, crossing keeper) are named *as roles* with their accountabilities, never as personal names or Sentinel numbers.
- [ ] **Residual risk is scored on the 5×5 matrix** and every `[GAP]` (the ALCRM band, the issue/date, site specifics) is closed with a SMART action carrying a named **role** owner and a due date — never an invented value.
- [ ] **Site specificity** — names *this* crossing / work site; a generic "a level crossing" artifact is flagged.
- [ ] **India** content cites the Railways Act 1989 / CRS framing and defers state-specific content to `hse-india` after state detection — no national form invented.
- [ ] **Sibling boundary** — the artifact does not rebuild the rail SMS (RAIL-01) or the ROGS application pack (RAIL-02); it references them where relevant (CONV-12).

## Sign-off note
SME review: ran (persona: Level-crossing / track-worker safety SME — NR/L2/OHS/019 +
ALCRM); this is **decision-support only**. It **precedes — and never replaces, never emits —
the human competent-person (rail-SME / accountable-manager) sign-off**, and it never outputs
the affirmative claim "approved by a competent person". A FLAG it raises is recorded, never
merge-blocking; the deterministic hard blocks (de-id leak, invented citation) are a separate
enforcement class.
