---
id: DEF_ADMISSIBILITY
type: SRL_DEFINITION_BLOCK
term: Admissibility
scope: CRL-0
status: published
surface: constraint-spine
srl_version: v0
---

# DEF_ADMISSIBILITY — Admissibility

## Definition

A condition that restricts what can be asserted or continued under finite resolution. Admissibility is a boundary concept. It is not a metric and not an instruction.

## Non-equivalences

- Admissibility is not validity (validity is binary; admissibility is a regime constraint).
- Admissibility is not permission (permission is granted; admissibility is structurally available or not).
- Admissibility is not feasibility (feasibility asks "can it be done"; admissibility asks "can it be asserted under declared bounds").
- Admissibility is not correctness (correctness implies ground truth; admissibility implies bounded assertability).

## Exclusions

- No procedure for determining admissibility is defined here.
- No numeric threshold for admissibility is stated.
- No admissibility score, metric, or ranking is provided.
- No operational test for admissibility violation is given.

## Source references

- Paper IV — Admissibility Under Constraint ([DOI](https://doi.org/10.5281/zenodo.18370414))
- Glossary term #1 (docs/glossary.md)
- Hierarchy ordering: Admissibility sits at the Boundary layer (docs/HIERARCHY.md)

## Notes

Admissibility is the central constraint of the program. All other concepts (continuation, identity, persistence, closure) are defined with respect to what is admissible under declared bounds and finite resolution.
