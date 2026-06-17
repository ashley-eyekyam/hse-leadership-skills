# HSE Leadership Skills — Getting Started

**A complete, step-by-step guide for people who have never used Claude Code or "Agent Skills" before.**

This manual teaches you how to install and use the safety tools in this pack to produce **consultant-grade** HSE artifacts — risk assessments, toolbox talks, and incident investigations — for real workplaces. No prior coding or AI experience is assumed. If you can describe a job to a colleague, you can use these skills.

> **Scope of this guide.** "Getting Started" covers one-time setup, the five universal rules, and a single-skill walkthrough for the three **flagship** skills (risk assessment, toolbox talk, incident investigation). It is deliberately *not* a tour of all 48 skills.
> - To **chain several skills** for a real end-to-end task, see [`USER_JOURNEYS.md`](USER_JOURNEYS.md).
> - For the **full catalog** of every skill and sector pack, see the [README catalog](../README.md#whats-in-the-box-the-catalog).
> - The setup and the five rules below apply to **every** skill in the pack, not just the three shown here.

> ⚠️ **Read this first — it is the most important sentence in the manual.**
> Everything these skills produce is a **draft to assist a qualified professional — not a finished or approved document.** Every output **must be reviewed and signed off by a competent person** (a suitably qualified, experienced HSE professional) before you rely on it or act on it. Nothing here is legal advice or a guarantee of compliance. See [`DISCLAIMER.md`](../DISCLAIMER.md).

---

## Table of Contents

1. [Part 0 — What is all this? (Plain-English orientation)](#part-0--what-is-all-this)
2. [Part 1 — One-time setup](#part-1--one-time-setup)
3. [Part 2 — Five rules that apply to every skill](#part-2--five-rules-that-apply-to-every-skill)
4. [Part 3 — How to use any skill (the general loop)](#part-3--how-to-use-any-skill-the-general-loop)
5. [Part 4 — The three HSE skills, one at a time](#part-4--the-three-hse-skills)
   - [4A. Risk Assessment (HIRA / HIRARC)](#4a-risk-assessment-hira--hirarc)
   - [4B. Toolbox Talk](#4b-toolbox-talk)
   - [4C. Incident Investigation](#4c-incident-investigation)
6. [Part 5 — Turning a result into a branded PDF / Word report](#part-5--turning-a-result-into-a-branded-pdf--word-report)
7. [Part 6 — Putting your own company branding on reports](#part-6--putting-your-own-company-branding-on-reports)
8. [Part 7 — Troubleshooting & FAQ](#part-7--troubleshooting--faq)
9. [Part 8 — One-page cheat sheet](#part-8--one-page-cheat-sheet)

---

## Part 0 — What is all this?

If the words "Claude Code," "Agent Skill," and "plugin" mean nothing to you, start here. Three quick definitions:

| Term | What it actually means for you |
|---|---|
| **Claude** | An AI assistant you talk to in plain English, like a very capable colleague. |
| **Claude Code** | A version of Claude that runs in a terminal window (or in your code editor / desktop app) and can read files, write files, and run small programs on your computer. That's what lets it produce a finished PDF report instead of just chatting. |
| **Agent Skill ("skill")** | A pre-written instruction pack that teaches Claude how to do **one specific job really well** — e.g. "write a defensible risk assessment." You don't read the skill; you just trigger it, and Claude follows it for you. |

**This repository ("the pack") contains three HSE skills:**

| Skill | What it makes | Who it's for |
|---|---|---|
| **`risk-assessment`** | A task- and site-specific risk assessment (HIRA / HIRARC) with a scored risk matrix, ranked controls, and SMART actions. | Safety leaders, managers, supervisors, consultants |
| **`toolbox-talk`** | A short, ready-to-read pre-task safety briefing **plus a sign-off / attendance sheet**. | Supervisors and frontline leaders |
| **`incident-investigation`** | A defensible, de-identified incident report: timeline, evidence log, root-cause analysis, corrective-action plan, and a "is this reportable?" verdict. | Safety managers and consultants |

**The one idea that makes this pack different:** every skill **forces specificity and the hierarchy of controls.** It will refuse to write generic, copy-paste safety paperwork. It pushes you to name the exact task, the exact site, the real hazards, and real controls ranked from "eliminate the hazard" down to "wear PPE" — so the result can survive a regulator's challenge.

---

## Part 1 — One-time setup

You do this **once**. Budget 15–20 minutes the first time.

### Step 1.1 — Install Claude Code

Claude Code is available as a terminal CLI, a desktop app (Mac/Windows), a web app at **claude.ai/code**, and as an extension for VS Code and JetBrains editors. Pick whichever you're comfortable with.

- **Easiest for non-technical users:** the **desktop app** or the **web app** (claude.ai/code).
- **Most common:** the **terminal CLI**. Install instructions are at the official Claude Code documentation. After installing, open a terminal and type `claude` to start it.

You will need a Claude account (a Claude.ai subscription or API access). Sign in when prompted.

> ✅ **Checkpoint:** you can open Claude Code and type a message like "hello" and get a reply.

### Step 1.2 — Get the pack onto your computer

The skills live in a Git repository. The simplest way to download it is with Git:

```bash
git clone https://github.com/ashley-eyekyam/hse-leadership-skills.git
cd hse-leadership-skills
```

If you don't have Git, you can also download the repository as a ZIP from its web page and unzip it. Either way, you end up with a folder called `hse-leadership-skills` containing folders like `skills/`, `knowledge-base/`, and `assets/`.

> 📌 Keep the **whole folder** together. The skills share common machinery (the report engine, the knowledge base, the branding files) that lives at the top level of this folder. Don't move a single skill out on its own — it relies on its neighbours.

### Step 1.3 — Make the skills available to Claude Code

There are two ways. **Method A (plugin marketplace) is the recommended one** — use it unless you have a reason not to. Method B (a project folder of shortcuts) is a fallback.

> 🧷 **One rule underneath both methods: keep the whole folder together, and start Claude Code from inside it.** The skills share machinery — the report engine, the knowledge base, and some shared code — that lives at the *top* of the `hse-leadership-skills` folder. A single skill on its own can't reach that machinery, so **don't copy one skill out by itself** — it will quietly stop working. Keep the whole folder intact and, when you use the skills, run Claude Code from inside that folder.

#### Method A — Install as a plugin (recommended)

This pack ships a marketplace manifest at [`.claude-plugin/marketplace.json`](../.claude-plugin/marketplace.json) that bundles the three HSE skills into the **`hse-core`** plugin (`risk-assessment`, `toolbox-talk`, `incident-investigation`). Installing it brings the whole folder along, so all the shared machinery comes with it.

Inside Claude Code, register the marketplace and install the core plugin. In the Claude Code prompt, type:

```
/plugin marketplace add /full/path/to/hse-leadership-skills
/plugin install hse-core@hse-leadership-skills
```

(Replace `/full/path/to/hse-leadership-skills` with the real location of the folder you cloned, or use the GitHub URL.) Then **restart Claude Code** so it picks up the new skills.

#### Method B — A project folder of shortcuts (fallback)

If the plugin method doesn't work for you, you can point Claude Code at the skills with a small folder of **shortcuts** (symlinks) that lead back to the skills inside the repo. The shortcuts matter: they keep each skill connected to the shared machinery it needs. (Plain copies would sever that connection and break the skills — that's why we use shortcuts, not copies.)

From inside the `hse-leadership-skills` folder, run:

```bash
mkdir -p .claude/skills
ln -s ../../skills/risk-assessment        .claude/skills/risk-assessment
ln -s ../../skills/toolbox-talk           .claude/skills/toolbox-talk
ln -s ../../skills/incident-investigation .claude/skills/incident-investigation
```

Then **start Claude Code from inside the `hse-leadership-skills` folder** (and restart it if it was already open). Because you launched it from here, it finds the shortcuts in `.claude/skills/`, and every skill can still reach the report engine and knowledge base at the top of the folder.

> ✅ **Checkpoint:** Ask Claude Code, *"What skills do you have available for safety work?"* It should mention risk-assessment, toolbox-talk, and incident-investigation. If it doesn't, you're most likely **not running Claude Code from inside the `hse-leadership-skills` folder**, or Claude Code needs a **restart** after the install. (Want to put the pack through a proper test? See the [Local Testing Guide](LOCAL_TESTING_GUIDE.md).)

### Step 1.4 — Install Python (only needed for branded PDF/Word reports)

The skills will do all their **thinking and writing** without anything extra. But to turn the result into a **branded, formatted PDF and Word document**, the pack uses a small Python program (the "report engine").

- Check if you already have Python: open a terminal and type `python3 --version`. If you see a version number (3.9 or newer), you're set.
- If not, install **Python 3** from python.org (or your OS package manager).
- Then install the two libraries the report engine needs:

  ```bash
  pip3 install reportlab python-docx pyyaml
  ```

> You can skip this step for now. The skills are fully useful for drafting even without it — you only need Python when you want the polished, branded file. Come back to it before [Part 5](#part-5--turning-a-result-into-a-branded-pdf--word-report).

---

## Part 2 — Five rules that apply to every skill

These five behaviours are baked into **all** the HSE skills. Understand them once and every skill makes sense.

### Rule 1 — Be specific, or it won't proceed

Every skill opens by interviewing you and **refuses vague answers.** "Assess general site safety" or "write a toolbox talk about working at height" will be bounced back. You must name **the exact task, broken into steps, at a named place**, e.g.:

> *"Confined-space entry to clean tank T-402 at Plant 3: isolate → purge → gas-test → enter → clean → exit."*

This is the single most important habit. The specificity you provide is what makes the output defensible instead of generic.

### Rule 2 — The hierarchy of controls is enforced

Whenever the skill recommends controls, it ranks them in this order and **leads with the strongest**:

1. **Elimination** — remove the hazard entirely
2. **Substitution** — swap it for something less dangerous
3. **Engineering** — guard, ventilate, isolate, interlock
4. **Administrative** — procedures, training, permits, signage
5. **PPE** — personal protective equipment (the **last** line, never the only line)

If a skill ever proposes **PPE-only** (or admin-only) controls, it must add a higher-order control **or** write an explicit justification ("higher-order controls not reasonably practicable because…"). A PPE-only fix with no justification is treated as a defect.

### Rule 3 — Personal data is de-identified automatically (and this is a hard rule)

Before drafting anything, every skill scans your inputs for personal and health identifiers — **names, employee/Aadhaar/SSN/NI numbers, phone, address, exact dates, job titles, photos, medical details** — lists what it found, and replaces them with **stable role labels** ("Worker A," "Operator 1," "Witness W-1").

It produces two things: the **de-identified document** and a **separate re-identification key** (the "Worker A = real name" mapping). **The key is never put inside the report.** It is handed back to you separately, and *your* job is to store it somewhere secure and access-controlled, away from the report.

It also **aggregates small numbers** — it will never publish an injury category with fewer than 5 people in it.

> 🔒 A de-identification leak is an **automatic, non-waivable failure.** If a real name or health detail ever appears in a finished report, that report is rejected. Treat de-id as sacred.

### Rule 4 — Decision-support only; a competent person must sign off

The skills are deliberately rigorous, but they are **not** a substitute for professional judgement, the law, or a licensed standard. Every output is a **draft for review.** Regulatory references are **pointers to verify** against the current, authoritative source for your jurisdiction — laws and forms change. Always route the output to a competent person before it's used.

### Rule 5 — Output comes as a branded PDF + Word document

The skills assemble their findings into a structured file (`report.json`) and the **report engine** renders it as **both a PDF and an editable Word (.docx) document**, branded with a logo and colour palette. The default branding is **Eyekyam** (teal palette); you can swap in your own — see [Part 6](#part-6--putting-your-own-company-branding-on-reports).

---

## Part 3 — How to use any skill (the general loop)

Every skill follows the same five-beat rhythm. Learn it once.

**1. Trigger the skill.** Just describe what you want in plain English. You don't type commands or filenames. Examples that automatically wake the right skill:

- *"I need a risk assessment for confined-space entry to clean tank T-402."*
- *"Write me a toolbox talk for re-roofing Bay 3 — the cherry-picker is out of service."*
- *"Help me investigate a hand injury on the Line 4 press and tell me if it's reportable."*

Claude recognises the intent and loads the matching skill. (You'll usually see it announce something like *"Using risk-assessment to…"*.)

**2. Answer the interview — one question at a time.** The skill asks a short series of questions (multiple-choice or free-text). Answer honestly. If you don't know something, say so — the skill marks unknowns as `[GAP]` rather than inventing facts. **Don't volunteer real names** if you can avoid it; use roles ("the fitter," "the supervisor").

**3. Confirm the echo-back.** After the questions, the skill repeats back what it understood — *"Assessing: confined-space entry to tank T-402, Plant 3, Maharashtra, own workers + contractors, 5×5 matrix, baseline — correct?"* Check it. Fix anything wrong **before** it starts the analysis.

**4. Let it do the work.** It de-identifies, identifies hazards/causes, scores risk, ranks controls, writes SMART actions, checks regulations, and runs an internal quality/critic pass. You'll get a draft in the chat.

**5. Generate the branded report (optional but recommended).** Ask Claude to render the result as a PDF + Word document. See [Part 5](#part-5--turning-a-result-into-a-branded-pdf--word-report). Then send it to a competent person for sign-off.

> 💡 **Tip:** You can interrupt at any time to add information ("actually, there are also contractors involved") or to redirect. It's a conversation, not a form you submit once.

---

## Part 4 — The three HSE skills

Each skill below has the same layout: **what it's for → what to have ready → the exact interview → what you get → a worked example → tips.**

---

### 4A. Risk Assessment (HIRA / HIRARC)

#### What it's for

Produces a **consultant-grade, task-specific risk assessment.** You give it a concrete task broken into steps; it identifies the hazards in each step, scores each on your organisation's risk matrix, ranks controls by the hierarchy, **re-scores the residual risk after controls**, and assigns SMART corrective actions with named owners and due dates. It can optionally cover **environmental aspects & impacts** (ISO 14001) in the same run.

**Trigger phrases:** "risk assessment," "HIRA," "HIRARC," "hazard identification," "risk matrix," "likelihood and severity," "hierarchy of controls," "residual risk," "risk register," "environmental aspects."

**Do *not* use it for:** vague/whole-site requests, generic templates, or investigating something that already happened (use Incident Investigation for that).

#### Have these ready before you start

1. The **exact task, broken into steps** (this is non-negotiable).
2. **Jurisdiction** (India / UK / USA / EU / Other) — and **if India, the state** (mandatory).
3. **Industry** (construction, manufacturing, oil & gas, chemicals, mining, other).
4. The **specific site/area/asset** ("Plant 3, tank farm, bay 2").
5. **Who is exposed** (own workers, contractors, public, nearby community).
6. **Existing controls** already in place for the task.
7. Your **risk-matrix size** (3×3, 4×4, or **5×5 default**) and how your org defines likelihood/severity bands.
8. **Assessment type:** baseline (whole task), issue-based (one hazard/change), or continuous (reviewing an existing RA).

#### The interview, in order

First a **scope gate**, then the main questions:

| # | Question | How to answer |
|---|---|---|
| **Q0** | Scope | **Occupational safety** (default) · **Environmental aspects** · **Both**. "Both" adds an extra environmental mini-interview (Q-E1…Q-E5). |
| **Q1** | Jurisdiction | India / UK / USA / EU / Other. **If India → Q1a asks the state** (Tamil Nadu, Karnataka, Maharashtra, Delhi/Central, Other). |
| **Q2** | Industry / sector | Construction · Manufacturing · Oil & Gas · Chemicals · Mining · General/Other. |
| **Q3** | **The task, broken into steps** | **Free text — the anchor.** Be concrete: *"Confined-space entry to clean tank T-402: isolate → purge → gas-test → enter → clean → exit."* Vague answers are rejected. |
| **Q4** | Location / site | *"Plant 3, tank farm, bay 2."* |
| **Q5** | Who is exposed? | Own workers · Contractors · Public/visitors · Nearby community (choose all that apply). |
| **Q6** | Existing controls | What's already in place ("generic permit; portable O₂ monitor"). |
| **Q7** | Likelihood band | 1 Rare · 2 Unlikely · 3 Possible · 4 Likely · 5 Almost certain. |
| **Q8** | Severity band | 1 Negligible · 2 Minor · 3 Moderate · 4 Major · 5 Catastrophic. |
| **Q9** | Matrix size | 3×3 · 4×4 · **5×5 (default)** · "I'll supply my own." |
| **Q10** | Assessment type | Baseline · Issue-based · Continuous. |

*(If Q0 = Environmental or Both, it also asks: **Q-E1** the activity, **Q-E2** the aspects — air/water/waste/land/resource/energy/noise, **Q-E3** the impacts, **Q-E4** operating condition — normal/abnormal/emergency, **Q-E5** compliance obligations/permits.)*

#### What you get

A branded **PDF + Word** report with these sections: cover & contents → executive summary → scope & method → **risk register** (each hazard scored) → *(environmental aspects register, if requested)* → **hierarchy-of-controls table** → **residual-risk movement table** → **SMART recommendations** (owner + ISO date) → regulatory basis → limitations & de-id notice. A separate **re-identification key** file is handed to you if any personal data was involved.

#### Worked example (abbreviated)

> **You:** "Risk assessment for confined-space entry to clean tank T-402, Plant 3, Maharashtra. Own workers and contractors. 5×5 matrix, baseline."
>
> **Skill (after the interview):** Identifies per-step hazards — **oxygen deficiency on entry** (L4×S4 = 16, **Critical**), **residual hydrocarbon vapour** (16, **Critical**), **engulfment by sludge** (9, Medium). Ranks controls: *Elimination* — clean externally via CIP where feasible; *Engineering* — continuous forced-air ventilation + continuous gas monitoring; *Administrative* — entry permit + standby attendant + rescue plan; *PPE* — supplied-air (not the sole control). **Residual after controls:** oxygen deficiency drops Critical → Medium. **SMART actions:** "Install a fixed continuous gas monitor on T-402 with interlock — Owner: Maintenance Lead, Due: 2026-07-01." **Regulatory basis:** ISO 45001 cl. 6.1.2 + the resolved Maharashtra state form (never a national form number).

#### Tips & gotchas

- **Spend your effort on Q3.** "Working at height" → rejected. "Working at height doing *what*, on which building, with which equipment?" → accepted.
- A **residual risk that stays High/Critical** is flagged as needing *more controls or a stop-work decision* — never "accept and proceed."
- **Actions must be SMART:** named owner (never "the safety team"), ISO date (never "ASAP"), measurable, linked to a hazard.
- **India = state detection is mandatory.** The skill confirms the state before citing any form.
- Sign-off by a competent person is required before the first entry.

---

### 4B. Toolbox Talk

#### What it's for

Produces a **short, ready-to-deliver pre-task safety briefing** (a.k.a. tailgate / pre-start / pre-job brief / take-5 / safety moment) **plus a fillable attendance / sign-off sheet.** The talk names the real hazards of *today's* job, ranks controls by the hierarchy, references a recent relevant incident (de-identified) **or a clearly-labelled typical example**, and gives the supervisor discussion prompts and 3–5 takeaways. Default length: **under 5 minutes.**

**Trigger phrases:** "toolbox talk," "tailgate," "pre-start," "pre-job brief," "take-5," "safety moment," "daily/shift safety briefing," "sign-off / attendance sheet."

**Do *not* use it for:** full risk assessments (use Risk Assessment), step-by-step job safety analyses, or investigating an event (use Incident Investigation).

#### Have these ready before you start

- The **exact task and site/area** ("re-roofing Bay 3, cherry-picker out of service, working off the leading edge").
- The **crew/trade** receiving it (electricians, operators, mixed crew…).
- The **primary hazard(s)** of the task.
- A **target length** (<5 min default).
- *(Optional)* a **real recent incident/near-miss** — names will be scrubbed. Leave blank and a labelled typical example is used instead.
- The crew's **reading level/language**.

#### The interview, in order

| # | Question | How to answer |
|---|---|---|
| **Q1** | Topic / primary hazard | Working at height · Confined space · Manual handling · Electrical/LOTO · Hot work · Mobile plant · Hazardous substances · Slips/trips · Lifting · Heat/cold · Other. |
| **Q2** | Trade / crew | Construction · Maintenance · Electrical · Mechanical · Operators · Drivers · Cleaners · Mixed · Other. Sets language level. |
| **Q3** | **Site/area + exact task today** | **Free text — the anchor.** *"Re-roofing Bay 3, cherry-picker out of service, working off the leading edge."* Vague answers rejected. |
| **Q4** | Duration | **<5 min (default)** · 5–10 · 10–15. |
| **Q5** | Recent incident (optional) | A real near-miss (gets de-identified), **or leave blank** for a clearly-labelled typical example. **Never** a fabricated "this happened here" story. |
| **Q6** | Reading level / language | Plain English (default) · Standard · ESL-friendly · Other language. |
| **Q7** | Jurisdiction (light) | India (which state?) · UK · USA · EU · **Not jurisdiction-specific (default)**. Only matters if you must cite a local law. |

#### What you get

A branded **PDF + Word** document with a fixed 7-part structure: **Hook** → **the specific hazards on this task** → **key controls (hierarchy-ranked, with owners)** → **"Learn from this"** (de-identified incident or labelled typical example) → **discussion prompts** → **takeaways (3–5)** → **attendance & sign-off sheet** (name/role · signature · date). Ready to print, post, or read aloud.

#### Worked example (abbreviated)

> **You:** "Toolbox talk — working at height, re-roofing Bay 3, cherry-picker out of service, mixed crew, under 5 minutes, plain English." (no incident provided)
>
> **Skill produces:** a hook ("A fall from this roof is life-changing or fatal — this five-minute talk is about keeping everyone off that edge unprotected"), the specific hazards (unprotected leading edge ~6 m; MEWP unavailable; mixed-crew familiarity; dropped objects), a controls table (Elimination: pre-assemble at ground level; Engineering: temporary edge guardrail + harness/running line; Administrative: permit + exclusion zone; PPE: hard hats + harnesses — *last line*), a **labelled typical near-miss** (not a fake local one), three discussion prompts, four takeaways, and a blank sign-off table.

#### Tips & gotchas

- **Q3 is everything.** "Maintenance work" is rejected; "changing the pump seals on Tank B" is accepted.
- **Never invent an incident.** If you don't have a real one, accept the labelled typical example — a crew that catches you faking it loses trust in the whole talk.
- The **sign-off sheet is the auditable proof** the briefing happened — don't skip it.
- Keep it to **<5 minutes** and **use the discussion prompts** — a talk that asks beats a talk that lectures.

---

### 4C. Incident Investigation

#### What it's for

Turns an incident — injury, illness, near-miss, property or environmental loss — into a **defensible, de-identified investigation report:** a factual timeline, a numbered evidence log, a **root-cause analysis** (you choose the method), root & contributing causes **each traced to evidence**, a **hierarchy-of-controls corrective-action plan (CAPA)** with owners and due dates, and a **jurisdiction-specific reportability verdict** (RIDDOR / OSHA 29 CFR 1904 / India state form).

**Trigger phrases:** "investigate an incident/accident," "root cause analysis," "RCA," "5-Whys," "ICAM," "SCAT," "Fishbone," "Swiss-Cheese," "write up an incident," "CAPA," "is this reportable," "RIDDOR," "OSHA recordable," "India accident form."

**Do *not* use it for:** live emergency response, or routine incident-**rate** dashboards across time (a different tool).

#### Have these ready before you start

- A **narrative of what happened** — the sequence of events, not your conclusions.
- **Date, time, location** (these get de-identified — you can withhold them).
- **Who was involved** — names/roles/witnesses (these get pseudonymised; prefer roles).
- **Severity/outcome.**
- The **evidence** — statements, photos, logs, maintenance/training records, procedures, readings.
- **Jurisdiction** — and **if India, the state** (mandatory for the correct accident form).

#### The interview, in order

| # | Question | Notes |
|---|---|---|
| **Q1** | What happened? | The event sequence (facts, not causes). |
| **Q2** | When & where? | Date/time/location — **flagged for de-identification.** |
| **Q3** | Incident type | Injury · Illness · Near-miss · Property · Environmental · Dangerous occurrence. |
| **Q4** | Severity / outcome | Fatality · Lost-time · Medical treatment · First aid · No-injury near-miss · Property only · Environmental only. |
| **Q5** | People involved | **Pseudonymised immediately** into role labels. |
| **Q6** | Immediate / obvious causes | The *starting* point for analysis, never the end. |
| **Q7** | Evidence available | Becomes the numbered evidence log (E-1, E-2…). Missing items → `[GAP]`. |
| **Q8** | RCA method | **5-Whys** (quick, minor events) · **ICAM** (systems/organisational; serious events) · **SCAT** (loss-causation & management control) · **Fishbone** (causes spread across Man/Machine/Method/Material/Measurement/Environment) · **Swiss-Cheese** (failed defence layers). Unsure? Take the skill's suggestion based on severity. |
| **Q9** | Jurisdiction | India (**→ which state**) · UK · USA · EU · Other. |
| **Q10** | *(Optional)* hours worked + recordable counts | Only if you want a single contextual incident rate (LTIFR/TRIR). Leave blank to skip — it never invents a denominator. |

#### What it does that you should trust

- **De-identification runs first**, before any analysis.
- **Every cause must cite a numbered evidence item.** A claim with no evidence is dropped or tagged `[ASSUMPTION]` — it cannot be a root cause.
- **The analysis must reach a systemic cause.** It will not stop at "the operator was careless" or "didn't follow the procedure" — it drives to the organisational factor (ambiguous procedure, lapsed training, informal practice under production pressure). If it can't, it rejects its own analysis and redoes it.
- **CAPAs are hierarchy-ranked** with named owners, ISO dates, a measure, and a link to the cause.
- **Reportability is always stated** (even "not reportable"), cited to the matched rule and with the **deadline** (e.g. UK RIDDOR specified injury → 15 days; OSHA fatality/hospitalisation/amputation/eye-loss → 24 h; India state form, e.g. within 24 h).

#### What you get

A branded **PDF + Word** report: cover (with de-id notice) → executive summary → KPI metrics → **timeline** → **evidence log** → **root-cause analysis** (your chosen method, populated) → **root & contributing causes** (each cites evidence) → **CAPA table** → **hierarchy-of-controls table** → **regulatory basis / reporting verdict**. Plus a **separate re-identification key** for you to store securely.

#### Worked example (abbreviated)

> **You:** "Investigate a lost-time hand injury on the Line 4 press — a worker removed the fixed guard to clear a jam and the press cycled. UK… actually India, Maharashtra. Use ICAM."
>
> **Skill:** de-identifies the worker to "Worker A," builds the timeline (T-00:15 jam → T-00:12 guard removed without isolation → T-00:00 press cycles → T+00:05 alarm), logs evidence E-1…E-6, runs **ICAM** and populates the **Organisational factors** row (ambiguous jam-clearance procedure; lapsed guard-safety refresher; informal guard removal under output pressure) so it **reaches systemic**. CAPAs: *Engineering* — fit a guard interlock so the press can't cycle with the guard removed (Owner: Maintenance Lead, Due: 2026-07-10); *Administrative* — rewrite the procedure to mandate isolation before guard removal (Owner: HSE Manager, Due: 2026-07-05). **Verdict:** reportable — Maharashtra state accident form within 24 h.

#### Tips & gotchas

- **Store the re-identification key separately and securely.** If the key and the report are found together, the de-identification is worthless.
- **Evidence is the anchor.** No evidence → no root cause. Honest `[GAP]`s are fine; invented facts are not.
- **Owners are role labels** ("Maintenance Lead"), **dates are ISO** (`2026-07-10`) — never "ASAP."
- **Reportability deadlines are tight** — the report surfaces the deadline so you know when to file. Verify against the live, authoritative source.

---

## Part 5 — Turning a result into a branded PDF / Word report

The skills can hand the assembled findings to a small **report engine** that produces a polished, branded **PDF and Word** document from a single data file (`report.json`).

The easiest path: **just ask Claude to do it.** After a skill finishes its draft, say:

> *"Generate the branded PDF and Word report."*

Claude writes the `report.json` and runs the engine for you. If you'd rather run it yourself, the command is:

```bash
python3 assets/report-engine/generate_report.py \
  --model report.json \
  --brand assets/report-engine/brand.yaml \
  --out ./out \
  --formats docx,pdf
```

- `--model` — the data file the skill produced.
- `--brand` — the visual theme (omit it to use the Eyekyam default; see [Part 6](#part-6--putting-your-own-company-branding-on-reports)).
- `--out` — the folder where the finished files land (here, an `out/` folder).
- `--formats` — `docx,pdf` (or just one).

> **Prerequisite:** Python 3 with `reportlab`, `python-docx`, and `pyyaml` installed (see [Step 1.4](#step-14--install-python-only-needed-for-branded-pdfword-reports)). If a logo or font is missing, the engine warns and carries on rather than failing.

You end up with `report.pdf` and `report.docx` in your output folder — and a separate re-identification key file if personal data was involved. **Send these to a competent person for review and sign-off before use.**

---

## Part 6 — Putting your own company branding on reports

By default, reports come out in **Eyekyam** branding (teal palette, Eyekyam logo, and a footer identity line). You can replace **both** layers with your own.

**There are two separate files, on purpose:**

| File | Controls | Default |
|---|---|---|
| [`assets/report-engine/brand.yaml`](../assets/report-engine/brand.yaml) | **Visual theme** — colour palette, fonts, logo image, page size, whether to show a cover/contents/page-numbers. | Eyekyam teal (`primary #2AADA8`, `secondary #1A7070`), Noto Sans fonts, Eyekyam logo. |
| [`branding/company-card.yaml`](../branding/company-card.yaml) | **Organisation identity** — the name, tagline, website, contact, and call-to-action shown on the report (e.g. in the footer). | Eyekyam ("HSE Leadership, operationalised with AI."). |

**To brand reports as your company:**

1. **Copy** `brand.yaml` to a new file, e.g. `my-brand.yaml`, and edit the colours, fonts, and `logo` path to your own. Any field you leave out is filled in from the Eyekyam default automatically.
2. **Edit** `branding/company-card.yaml` — change `company.name`, `tagline`, `website`, `contact_email`, `blurb`, and `cta` to yours. Set `show: false` if you want no identity line at all. `placement` can be `footer`, `after-output`, or `on-request`.
3. **Point the report engine at your theme** with `--brand my-brand.yaml` (and `--card branding/company-card.yaml`):

   ```bash
   python3 assets/report-engine/generate_report.py \
     --model report.json --brand my-brand.yaml \
     --card branding/company-card.yaml --out ./out --formats docx,pdf
   ```

That's it — every future report inherits your look. (Or just tell Claude: *"Use my-brand.yaml for the branding."*)

---

## Part 7 — Troubleshooting & FAQ

**"Claude doesn't seem to know about the skills."**
Re-check [Step 1.3](#step-13--make-the-skills-available-to-claude-code). Restart Claude Code after installing the plugin. Ask directly: *"List the safety skills you have."* The most common cause is **not running Claude Code from inside the `hse-leadership-skills` folder** — start it from there. If you used Method B, also confirm the shortcuts exist in `.claude/skills/` inside the folder.

**"It found the skill, but it says it can't find a file / the knowledge base / the report engine."**
The skill has been cut off from the shared machinery it needs. This happens if a single skill was **copied out on its own**, or if Claude Code wasn't started from inside the `hse-leadership-skills` folder. Fix it by using the **plugin** (Method A) or the **shortcuts** (Method B) from [Step 1.3](#step-13--make-the-skills-available-to-claude-code), keeping the whole folder together, and **starting Claude Code from inside that folder**.

**"It keeps refusing my request and asking for more detail."**
That's by design (Rule 1). Give it the exact task broken into steps, at a named site. "General site safety" will always be rejected; "isolating and replacing the conveyor drive motor in Despatch Bay 2" will be accepted.

**"The PDF/Word step failed."**
You need Python 3 plus `reportlab`, `python-docx`, and `pyyaml` ([Step 1.4](#step-14--install-python-only-needed-for-branded-pdfword-reports)). Run `pip3 install reportlab python-docx pyyaml`. The drafting itself works without these — only the branded file needs them.

**"Where did the re-identification key go?"**
The skill hands it to you **separately** from the report (never inside it). Save it somewhere access-controlled — a password-protected file or a locked drive — apart from the report. This is your responsibility (Rule 3).

**"Can I use these without revealing real names?"**
Yes — and you should. Refer to people by role ("the fitter," "the supervisor"). The skill de-identifies anyway, but the less personal data you feed in, the better.

**"It cited a regulation / form — can I rely on it?"**
Treat every regulatory reference as a **pointer to verify** against the current, authoritative source for your jurisdiction. Laws and prescribed forms change. The skill is conservative and (for India) confirms the state first, but the final check is yours and the competent person's.

**"Is the output ready to submit?"**
No. It is a **draft for a competent person to review and sign off.** Always. (Rule 4.)

---

## Part 8 — One-page cheat sheet

**Setup (once):** install Claude Code → `git clone` the pack → install `hse-core` plugin (or copy skill folders to `~/.claude/skills/`) → `pip3 install reportlab python-docx pyyaml` for branded reports.

**Every job — five beats:** trigger in plain English → answer the interview (one question at a time, be specific) → confirm the echo-back → let it work → ask for the branded PDF/Word → send to a competent person.

**Pick the right skill:**

| You want to… | Say something like… | Skill |
|---|---|---|
| Assess risk of a task **before** doing it | "Risk assessment for *[exact task, steps]* at *[site]*." | **risk-assessment** |
| Brief a crew **right before** a task | "Toolbox talk for *[exact task]*, *[crew]*, under 5 min." | **toolbox-talk** |
| Work out **what went wrong** after an event | "Investigate *[incident]*; run an RCA; is it reportable?" | **incident-investigation** |

**The five rules:** (1) be specific or it won't proceed · (2) controls ranked Eliminate→Substitute→Engineer→Admin→PPE · (3) personal data auto-de-identified, key kept separate, leak = auto-fail · (4) decision-support only — competent-person sign-off required · (5) output = branded PDF + Word.

**Golden habit:** the quality of the output equals the **specificity of your Q3 answer**. Name the task, the steps, the place, the people exposed. Everything else follows.

---

*HSE Leadership Skills — Apache-2.0, © 2026 Eyekyam. Decision-support only; see [`DISCLAIMER.md`](../DISCLAIMER.md). Built to turn safety standards into defensible, day-to-day practice.*
