<!-- KB-STD-ICAO-ANNEX19 -->
# ICAO Annex 19 — Safety Management (four-pillar clause→artifact map)

**Fragment ID:** `KB-STD-ICAO-ANNEX19`
**What this is:** a copyright-safe **four-pillar element → output-artifact map** —
the ICAO Annex 19 Safety Management System (SMS) framework's *pillar/element*
structure plus how each pillar grounds an `hse-aviation` skill. It is the aviation
analogue of the ISO 45001 clause→artifact map.
**What this is NOT:** a reproduction of the Annex 19 normative text or of ICAO
Doc 9859 (Safety Management Manual). ICAO documents are copyrighted; the user holds
their own licensed copy. Cite pillar/element *topics* only — never paste the
standard's wording.

> Source: ICAO Annex 19 (2nd ed., 2016) + ICAO Doc 9859 Safety Management Manual (4th ed.) — element structure only; user holds the licensed documents · Year: 2016 · Reviewed: 2026-05-15 · Volatile: false (multi-year ICAO revision cycle).

ICAO Annex 19 is the cross-cutting aviation-safety backbone every `hse-aviation`
skill leans on, **independent of jurisdiction** — an SMS is built to the four
pillars whether the operator is certificated by the DGCA (India), the FAA (US), or
EASA (EU). The four-pillar SMS is operated by aircraft operators / airports / approved
maintenance & training organisations under a **State Safety Programme** (the DGCA
SSP in India — see `../regulatory/in-dgca.md`).

## The four pillars → element topic → skill it grounds

| Pillar | Element topic | Grounds (skill / artifact) |
|---|---|---|
| **1. Safety Policy & Objectives** | Safety policy & accountable-manager commitment | **aviation-sms-builder** (the signed policy + safety objectives) |
| 1 | Safety accountabilities & responsibilities | aviation-sms-builder (accountabilities table) |
| 1 | Appointment of key safety personnel (Safety Manager) | aviation-sms-builder (key-personnel table) |
| 1 | Coordination of emergency-response planning | aviation-sms-builder (ERP coordination) |
| 1 | SMS documentation | aviation-sms-builder (SMS manual structure) |
| **2. Safety Risk Management** | Hazard identification | **aviation-hazard-register** (hazard ID → register) |
| 2 | Safety risk assessment & mitigation | **aviation-hazard-register** + **aviation-change-safety-assessment** (5×5 RCS via `risk_matrix`; HoC mitigation) |
| 2 | Management of change | **aviation-change-safety-assessment** (new/changed hazards on a change) |
| **3. Safety Assurance** | Safety performance monitoring & measurement (SPI/SPT) | **aviation-spi-spt-framework** (SPIs/SPTs + alert/target levels) |
| 3 | The management of change (assurance side) | aviation-change-safety-assessment |
| 3 | Continuous improvement of the SMS (management review / SRB) | **aviation-srb-minutes** (Safety Review Board record) |
| 3 | Operational-data monitoring inputs (FDM/FOQA) | **aviation-fdm-foqa-analysis** (assistive — structures user-supplied exceedance summaries) |
| **4. Safety Promotion** | Training & education | aviation-sms-builder (training plan) |
| 4 | Safety communication & just culture | **aviation-just-culture-policy** (policy + decision tree) |
| 4 | Voluntary / confidential safety reporting | **aviation-confidential-reporting** (reporting system design) |

## The ICAO 5×5 Risk Classification Scheme

Pillar 2's safety-risk-assessment matrix (severity × likelihood → acceptability
band) is **not** authored here as code — it is the `KB-DATA-AVI-RISK-MATRIX`
`MatrixConfig` (`../data-points/aviation-risk-matrix.md`) consumed by the shared A7
`risk_matrix.score()` engine. The aviation pack supplies *config* (the ICAO axis
labels + acceptability bands), never a forked matrix.

## Usage note

Every aviation skill grounds in `KB-STD-ICAO-ANNEX19` (the SMS framework) and, where
India is the jurisdiction, in `KB-REG-IN-DGCA` (the State Safety Programme that adopts
Annex 19 in India). Mitigations in pillar 2 are ranked through the hierarchy of
controls (`KB-SNIP-HOC`) — an SMS that "manages" a hazard by a new procedure alone is
challenged to justify why a higher-order barrier is not reasonably practicable.
DGCA SSP alignment is a **KB capability** (`KB-REG-IN-DGCA`), not a separate skill.
