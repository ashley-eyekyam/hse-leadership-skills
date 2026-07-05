---
sme-review:
  personas:
    - role: "Fixture reviewer"
      expertise: "Generic fixture expertise (placeholder)."
      lens: "generic fixture lens (placeholder)"
modes:
  default:
    floor:
      - id: only-item
        description: "Only fully-formed floor item — the floor is deliberately short."
        anchors: ["alpha"]
        min_matches: 1
      - description: "Deliberately missing its id; anchors empty; min_matches invalid."
        anchors: []
        min_matches: 0
---

# SME Review & Sign-off — rule13 broken fixture

## Domain checklist
- [ ] generic fixture check one
- [ ] generic fixture check two
- [ ] generic fixture check three

## Sign-off note
This fixture deliberately has NO Omission lens section.
