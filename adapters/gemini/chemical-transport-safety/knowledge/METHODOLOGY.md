# Methodology — chemical transport safety + classification cross-walk

## Method (single-thread — classification lookup + assembly)
1. **De-identify first** — any driver/handler PII → role labels.
2. **Resolve the substance + UN entry** from the intake; resolve UN number / proper shipping name
   from the user's Dangerous Goods List — **never assumed**.
3. **Cross-walk** the GHS class (`KB-STD-GHS`) to the transport class + packing group for the chosen
   mode: ADR (`KB-REG-EU-ADR`, EU road), DOT HMR (`KB-REG-US-DOT-HMR`, US road, §172.101 HMT), IMDG
   (`KB-STD-IMDG`, sea). **Rail (RID) / air (IATA/ICAO-TI) are out of scope — flag, do not guess.**
4. **Marking / placarding / segregation** for the mode; segregation respects incompatibilities.
5. **Loading/unloading controls** — HoC-ranked with `controls`.

## Output discipline
- An unknown UN entry / class is `[GAP]`-flagged, never invented (citation accuracy).
- Out-of-scope modes (rail/air) are explicitly flagged, not answered.
