<!-- KB-REG-OSHA1910-I -->
# United States — OSHA 29 CFR 1910 Subpart I (Personal Protective Equipment map)

**Fragment ID:** `KB-REG-OSHA1910-I`
**What this is:** a copyright-safe **duty → artifact map** for OSHA's PPE standards (29
CFR 1910 Subpart I) — 1910.132 the PPE hazard assessment + the **written certification**
of that assessment (1910.132(d)(2)), and the body-region sections (eye/face .133, head
.135, foot .136, hand .138).
**What this is NOT:** a reproduction of 29 CFR 1910 text. Cite the CFR section numbers
and the duty topics only — never paste the regulation wording.

> Source: OSHA 29 CFR 1910 Subpart I (Personal Protective Equipment) — citation map · Year: 2026 · Reviewed: 2026-06-22 · Volatile: false (stable CFR structure; refresh on review).

29 CFR 1910 Subpart I grounds a PPE-matrix skill (MFG-04) with the **assess → certify →
select** duty, applied through the hierarchy of controls — PPE is the residual-only,
documented last line after higher-order controls.

## Duty / topic → section → artifact it grounds

| Duty / topic | Section | Artifact it grounds |
|---|---|---|
| PPE hazard assessment | 1910.132(d)(1) | assess the workplace for hazards requiring PPE, by body region and task |
| **Written certification** of the assessment | 1910.132(d)(2) | the certification block (who assessed, what was assessed, date) — a mandatory written record |
| Eye & face protection | 1910.133 | eye/face PPE selection against the named hazard (cite the conformity standard) |
| Head protection | 1910.135 | head PPE selection |
| Foot protection | 1910.136 | foot PPE selection |
| Hand protection | 1910.138 | hand PPE selection |

## How the skill uses this fragment
- `ppe-matrix` resolves the body-region hazards, applies the **controls-first gate**
  (`KB-SNIP-PPE-MATRIX-LOGIC` + `KB-SNIP-HOC`) so PPE is the residual-only control, then
  selects PPE against the conformity standard (`KB-DATA-PPE-STANDARDS`).
- The **written certification** (1910.132(d)(2)) is always produced — omitting it is a
  citation failure.
- A missing input (no task, no hazard) is a `[GAP]`; PPE is never the headline control.
