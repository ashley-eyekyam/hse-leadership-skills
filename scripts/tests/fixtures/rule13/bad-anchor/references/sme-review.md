---
sme-review:
  personas:
    - role: "Fixture reviewer"
      expertise: "Generic fixture expertise (placeholder)."
      lens: "generic fixture lens (placeholder)"
modes:
  default:
    detected_by: always
    floor:
      - id: item-1
        description: "First generic floor item for the fixture."
        anchors: ["alpha"]
        min_matches: 1
      - id: item-2
        description: "Second item — its second anchor is an invalid regex on purpose."
        anchors: ["beta", "([unclosed"]
        min_matches: 1
      - id: item-3
        description: "Third generic floor item for the fixture."
        anchors: ["gamma"]
        min_matches: 1
---

# SME Review & Sign-off — rule13 bad-anchor fixture

## Domain checklist
- [ ] generic fixture check one
- [ ] generic fixture check two
- [ ] generic fixture check three

## Omission lens
Run the omission pass per KB-SNIP-COMPLETENESS before reconciling the floor;
surface any miss as a [GAP] entry — never fabricate.
