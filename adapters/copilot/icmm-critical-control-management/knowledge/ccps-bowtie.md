<!-- KB-STD-CCPS-BOWTIE -->
# CCPS / EI Bowtie & Barrier-Based Risk Management (method map)

**Fragment ID:** `KB-STD-CCPS-BOWTIE`
**What this is:** a copyright-safe **method map** for the bowtie / barrier-based
risk-management method (CCPS / Energy Institute) and ICMM Critical Control
Management (CCM) — top event, threat/consequence phrasing, and the
effective-independent-auditable barrier criteria with performance standards.
**What this is NOT:** a reproduction of the source guidance's text. The CCPS/EI
and ICMM publications are copyrighted; the user holds their own licensed copy.
Cite the method structure and topics only — never paste the guidance wording.

> Source: CCPS/EI bowtie method; ICMM Critical Control Management — method structure (user holds the guidance) · Year: 2026 · Reviewed: 2026-05-15 · Volatile: false (multi-year revision cycle).

The bowtie centres a **top event** (loss of control of a hazard) with threats and
preventive barriers on the left, consequences and mitigative barriers on the
right. It grounds `bowtie-builder` and is the shared method for chemicals
(process bowties) and mining (ICMM CCM critical controls).

## Method structure → diagram elements

| Element | Topic | Phrasing / criterion |
|---|---|---|
| Hazard | The energy/material with potential to harm | named, specific |
| Top event | Loss of control of the hazard | the release/escalation point |
| Threats | Causes that could release the top event | one threat → one line |
| Preventive barriers | Controls on the threat side | each **effective · independent · auditable** with a performance standard |
| Consequences | Outcomes if the top event escalates | phrased "**[Damage] due to [Event]**" |
| Mitigative barriers | Controls on the consequence side | each effective-independent-auditable, HoC-ranked (`controls`) |
| Critical control (CCM) | A barrier that prevents/mitigates an MAE | performance standard + verification activity + owner |

## Assistive + HoC discipline (load-bearing)
- The team supplies the barrier judgements; the skill structures the bowtie and
  records them — a barrier is not declared effective without the team's
  performance-standard evidence (`[GAP]` otherwise).
- A barrier set that is **administrative/PPE-only** without a higher-order
  engineering barrier (interlock, relief, SIS) is flagged (`controls.ppe_admin_only`).
