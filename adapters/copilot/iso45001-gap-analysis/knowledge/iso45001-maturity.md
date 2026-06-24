<!-- KB-DATA-ISO45001-MATURITY -->
# ISO 45001 conformance / maturity — a 5-level scale per clause

**Fragment ID:** `KB-DATA-ISO45001-MATURITY`
**What this is:** the shared **5-level conformance/maturity scale** the
`iso45001-gap-analysis` (#19) skill scores each ISO 45001 clause against (and which
`training-needs-analysis` #13 reuses to band a competence-system's maturity). Each level
carries an **evidence test** — what proof moves a clause from one level to the next.
**What this is NOT:** the ISO 45001 standard text, an audit certification decision, or a
substitute for a certification-body assessment. It is a **scoring convention** over the
clause→artifact map in `KB-STD-ISO45001`; the binding clause requirements are read from
that standards fragment (the user holds the licensed standard).

> Source: ISO 45001:2018 (clause structure 4–10) · ISO/IEC 17021-1 (certification-audit principles, framing readiness) · staged-maturity convention · Year: 2026 · Reviewed: 2026-06-22 · Volatile: false.

---

## The 5-level conformance/maturity scale (score each clause)

| Level | Label | Conformance meaning | Evidence test |
|---|---|---|---|
| 0 | **Absent** | No process for this clause. | Nothing documented or practised. |
| 1 | **Ad hoc / informal** | Done reactively, undocumented, person-dependent. | Anecdote only; no records, no defined process. |
| 2 | **Documented** | A defined process exists on paper. | Procedure/policy exists; limited evidence it is followed. |
| 3 | **Implemented (conformant)** | Process is followed and produces records across scope. | Records show the clause's requirements met consistently; meets the clause = certification-ready for that clause. |
| 4 | **Measured & improving** | Process effectiveness is monitored and acted on. | Performance data, internal audit, and management-review evidence of improvement against the clause. |

**Certification-readiness rule:** a clause at **level ≤ 2** that the standard makes
mandatory (e.g. 5.2 policy, 6.1.2 hazard identification, 9.2 internal audit, 10.2
incident/nonconformity) is a **certification-blocker**, not a minor gap — flagged
explicitly in the gap register (#19 eval case 2).

## How the skills use this fragment

- **#19 iso45001-gap-analysis** scores every clause (4–10) on this scale from the supplied
  evidence, marks any mandatory clause at level ≤ 2 as a certification-blocker, and orders
  the costed remediation roadmap by (gap size × certification-blocking severity, see
  `KB-SNIP-GAP-PRIORITISATION`). The same scale is reused for ISO 14001 / ISO 45003 via
  the standard selector.
- **#13 training-needs-analysis** reuses the scale to band the **maturity of the competence
  system** (cl. 7.2) — distinct from the per-role competence band in
  `KB-DATA-COMPETENCE-LEVELS`.
