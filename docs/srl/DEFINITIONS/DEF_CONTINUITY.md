---
id: DEF_CONTINUITY
type: SRL_DEFINITION_BLOCK
term: Continuity
scope: CRL-0
status: published
surface: constraint-spine
srl_version: v0
---

# DEF_CONTINUITY — Continuity

## Definition

The minimal persistence condition under which admissible ordering remains composable across admissible evolution.

Continuity is a claim condition on composability. It is not a smoothness assumption, not a mechanism, and not an operational test.

## Non-equivalences

- Continuity is not smoothness (in the analytic sense).
- Continuity is not stability (stability implies perturbation response; continuity states composability).
- Continuity is not identity (identity requires persistence over an observation window; continuity is the condition that makes such persistence expressible).
- Continuity is not memory (memory implies storage; continuity implies structural composability under evolution).

## Exclusions

- No detection procedure for continuity is defined or implied.
- No threshold for "sufficient continuity" is stated.
- No metric or measure of continuity is provided.
- No operational test for continuity failure is given.

## Source references

- Paper VII — Continuity as a Structural Condition in Constraint Geometry ([DOI](https://doi.org/10.5281/zenodo.18766848))
- Glossary term #42 (docs/glossary.md)
- Hierarchy ordering: Continuity sits between Boundary+Admissibility and Energy (docs/HIERARCHY.md)

## Notes

Continuity enters the hierarchy as the bridge between boundary constraints and energy cost. Without continuity, admissible ordering is not composable, and identity claims cannot be carried across evolution windows.
