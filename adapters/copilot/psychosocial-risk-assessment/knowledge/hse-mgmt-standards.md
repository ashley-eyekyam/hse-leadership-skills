<!-- KB-SNIP-HSE-MGMT-STANDARDS -->
# HSE Management Standards — six domains + work-design controls

**Fragment ID:** `KB-SNIP-HSE-MGMT-STANDARDS`
**This is prompt text, applied by the model — not a generator.** It is the six-domain
framework the `psychosocial-risk-assessment` (#18) skill assesses against, each domain with
its **indicative work-design controls**. Benchmark bands come from
`KB-DATA-PSYCHOSOCIAL-INDICATORS`; the standard is `KB-STD-ISO45003`.

> Source: UK HSE Management Standards (demands/control/support/relationships/role/change) · ISO 45003:2021 (psychosocial risk) · Year: 2026 · Reviewed: 2026-06-22 · Volatile: false.

---

## Instruction — assess each selected domain at source (work design, not the individual)

| Domain | The psychosocial hazard | Indicative **work-design** controls (organisational, ranked above individual resilience) |
|---|---|---|
| **Demands** | Workload, work patterns, work environment. | Achievable workloads; job/role design; environment fixes; staffing. |
| **Control** | How much say a person has over their work. | Decision latitude; flexibility; involve in how work is done. |
| **Support** | Encouragement, sponsorship, resources from org/managers/peers. | Manager-support systems; resources; supportive policies. |
| **Relationships** | Conflict; unacceptable behaviour (bullying/harassment). | Anti-bullying policy + enforcement; conflict resolution; reporting routes. |
| **Role** | Whether people understand their role; conflicting roles. | Clear role definitions; resolve conflicting demands. |
| **Change** | How organisational change is managed/communicated. | Early consultation; clear communication; transition support. |

## Discipline

- **Work-design controls first** — an assessment that recommends only "resilience training"
  as the control is flagged (#18 eval case 1) and pushed up the hierarchy (`KB-SNIP-HOC`):
  individual resilience is the **last** resort, never the primary control.
- **Confidentiality / special-category data** — survey/focus-group responses and
  sickness-absence are special-category health data: suppress any breakdown with **<5
  respondents** (#18 eval case 2 — a `de_identification` hard-fail), never attribute a
  finding to a nameable individual ("no individual named as the hazard").
- **Triangulate** across ≥2 data sources — never rate on a single anecdote (#18 eval case 3).

## Output expectation

Hazard-by-domain findings, a risk rating, work-design controls, a confidentiality-protected
action plan. Feeds `hierarchy_of_controls`, `de_identification`, `specificity`.
