<!-- KB-SNIP-CULTURE-MODELS -->
# Safety-culture models — four selectable, combinable diagnostic lenses

**Fragment ID:** `KB-SNIP-CULTURE-MODELS`
**This is prompt text, applied by the model — not a generator.** It is the model bank the
`safety-culture-assessment` skill maps survey/observation results against. Three are **maturity
ladders** (Bradley · Hudson/Parker · Westrum); the fourth — **Schein three-levels** — is a
**diagnostic-levels lens, NOT a fourth ladder** (D-05). All four are selectable AND combinable;
the chosen lens(es) is set at intake. Maturity-band figures resolve from `KB-DATA-CULTURE-MATURITY`.
Each model is cited as **method, not law**.

> Source: DuPont Sustainable Solutions (Bradley Curve) · Hudson/Parker "Hearts & Minds" ladder (Leiden/Shell) · Ron Westrum, "A typology of organisational cultures", BMJ Qual Saf 2004 · Edgar H. Schein, *Organizational Culture and Leadership* · Year: 2026 · Reviewed: 2026-06-22 · Volatile: false.

---

## Instruction — never rate culture on a single survey

A maturity rating is only defensible with **a named model + a named population + ≥2 data sources**
(survey + behaviour/outcome corroboration). A rating from a single survey, with no behavioural or
outcome triangulation, is flagged (defensibility · specificity). Pick the lens at intake; combine
lenses where the user wants both a ladder position and a values diagnosis.

### Lens 1 — DuPont Bradley Curve (maturity ladder, ownership-of-safety)

Four progressive stages, each defined by **where ownership of safety sits**:

| Stage | "Safety by…" | Marker |
|---|---|---|
| **Reactive** | natural instinct | compliance is the goal; safety delegated to the safety manager; little management involvement. |
| **Dependent** | supervision | management commitment, rules & procedures, supervisor control/emphasis, fear/discipline, value of people. |
| **Independent** | self | personal knowledge/commitment/standards; internalisation; care for self; habits; individual recognition. |
| **Interdependent** | teams | help others conform; others'-keeper; networking contributor; care for others; organisational pride. |

*Probe:* "Who is seen to own safety here — the safety dept, supervisors, each worker, or the team?"

### Lens 2 — Hudson / Parker "Hearts & Minds" ladder (maturity ladder, five rungs)

Built on Westrum's typology; read through how *leadership* thinks, how *workers* act, how
*information* flows, how *incidents* are treated:

| Rung | Diagnostic marker |
|---|---|
| **Pathological** | safety is a cost/brake; corners cut because that is rewarded; bad news buried; incidents blamed on the nearest individual. |
| **Reactive** | safety gets attention only after an incident; effort spikes after accidents, decays in quiet periods. |
| **Calculative** | has a process AND uses it, but risks "going through the motions"; heavy on systems/measurement. |
| **Proactive** | uses the systems to anticipate problems before they arise. |
| **Generative** | safety integrated into how the org runs everything; near-misses openly shared as learning, not hidden. |

### Lens 3 — Westrum organisational typology (maturity lens, information flow)

Three types defined by **how information flows**. Hudson's 5-rung ladder is an *extension* of this
typology — present them as related, not competing.

| Type | Information handling |
|---|---|
| **Pathological** | power-oriented; information hidden; messengers shot; bridging discouraged; failure → scapegoating. |
| **Bureaucratic** | rule-oriented; information may be ignored; messengers tolerated; failure → justice/blame. |
| **Generative** | performance-oriented; information actively sought; messengers trained/rewarded; failure → inquiry. |

### Lens 4 — Schein three levels of culture (diagnostic-levels lens, NOT a ladder) — D-05

A **values diagnosis**, not a maturity rating. Standalone Schein output names **gaps**, it does not
assign a stage. The advancement input is the **espoused-vs-enacted gap** (see the Schein rubric in
`KB-DATA-CULTURE-MATURITY`).

| Level | What it is | Probe |
|---|---|---|
| **Artifacts** | visible structures & processes (signage, PPE use, what gets posted) — easy to observe, hard to decode. | "What do you see/hear when you walk the floor about safety?" |
| **Espoused beliefs & values** | stated strategies, goals, "safety is our #1 priority" slogans, policy statements. | "What does the organisation SAY it values about safety?" |
| **Basic underlying assumptions** | unconscious, taken-for-granted beliefs that actually drive behaviour. | "When schedule and safety collide on a real job, which wins — and is that ever said out loud?" |

## How the skill uses this fragment

`safety-culture-assessment` selects one or more lenses at intake, bands each against
`KB-DATA-CULTURE-MATURITY`, triangulates across ≥2 sources, and routes the gap to a
`smart_actions` advancement roadmap. Schein output stays a **diagnosis** (named gaps), never a
single maturity number.
