---
Status: DRAFT
Surface: CC (Declarative)
Claim Ceiling: navigation + structural indexing only
Authority: Observer-only | Non-authoritative | No directives
Exclusions: methods, algorithms, thresholds, calibration, procedures, recipes, enforcement
SRA Version: v0
---

# Surface Readability Layer (SRL)

## Purpose

SRL is a **representation-only** overlay that makes canonical spine documents machine-indexable without altering doctrine.

SRL exposes canon as atomic, extractable structural units: definitions, invariants, and refusals. Each unit links back to its canonical source by anchor. SRL does not duplicate, paraphrase, or extend canon.

## Posture

**CRL-0 / Stage-0 / observer-only / non-authoritative.**

SRL is permitted to:

- Index canonical documents by stable ID
- Extract structural blocks (definitions, invariants, refusals) as navigational units
- Link blocks to source anchors in papers, foundation notes, and program notes
- Declare version pins and status

SRL is forbidden from:

- Introducing new claims, definitions, or invariants not present in canon
- Introducing methods, procedures, thresholds, or detection logic
- Introducing evaluators, scoring, optimization, prediction, or control framing
- Introducing enforcement semantics or automated governance
- Modifying frozen or governed documents
- Widening governance scope or licensing posture
- Using AI scaffolding language or operational verbs

## Structure

```
docs/srl/
├── README.md              ← this file
├── CANON_INDEX.yml         ← machine-traversable document + unit index
├── DEFINITIONS/            ← atomic definition blocks
│   ├── DEF_CONTINUITY.md
│   ├── DEF_RECORD.md
│   └── DEF_ADMISSIBILITY.md
├── INVARIANTS/             ← atomic invariant blocks
│   ├── INV_NON_EQUIVALENCE_IDENTITY_MEMORY_RECORD_CONTINUITY.md
│   └── INV_CONTINUITY_AS_ADMISSIBLE_EXTENSION.md
└── REFUSALS/               ← atomic refusal blocks
    ├── REF_STAGE0_NO_METHODS.md
    ├── REF_NO_EVALUATORS_NO_THRESHOLDS.md
    ├── REF_NO_OPTIMIZATION_PREDICTION_CONTROL.md
    └── REF_NO_SEMANTIC_AUTHORITY.md
```

## Relationship to canon

SRL units are **derived projections**, not authoritative sources. The canonical text lives in:

- [Papers index](../papers.md)
- [Foundation Notes](../foundation-notes/)
- [Glossary](../glossary.md)
- [Claim Rules](../CLAIM_RULES.md)
- [Signature Map](../SIGNATURE_MAP.md)
- [Hierarchy](../HIERARCHY.md)

If SRL content conflicts with canon, canon prevails. SRL units should be regenerated from canon, not edited independently.

## Version discipline

SRL is versioned with the spine tag. SRL additions require a new tag release. SRL does not modify tag-pinned documents.
