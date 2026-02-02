# Canon Policy

This repository is the **public source of truth** for the Constraint Program's
declarative spine: scope, exclusions, reading order, controlled vocabulary,
license posture, and governance decisions.

## Rules

1. **Edits require diffs + tags.** Every change is a governance event.
2. **No methods, thresholds, or procedures.** The spine is declarative only.
3. **No silent edits.** CMS-style "just update the page" is not permitted.
4. **Version tags map to public citations.** Use `public-spine-vN` tags.

## What lives here

| Directory | Content |
|-----------|---------|
| `docs/` | Spine pages: index, reading order, glossary, papers, FAQ, licenses |
| `docs/HEADER_STAMP_TEMPLATE.md` | Stamp template for all pages |
| `registry/DECISIONS/` | Governance decision records (ADRs) |

## What does NOT live here

- Detection logic, algorithms, scoring functions
- Calibration procedures or parameter values
- Operational workflows or "how-to" guides
- Bundle artifacts (those live in `constraint-vocabulary`)
- Website rendering code (that lives in `cc-website`)

## Relationship to other repos

| Repo | Role |
|------|------|
| `constraint-spine` (this) | Public canon — source of truth |
| `constraint-vocabulary` | Bundle/release channel (e.g., trf-vocabulary-v0) |
| `cc-website` | Rendered brochure — presentation layer, not canon |
| u3r_lab (private) | Drafting/staging — never public |

## Citation

To cite a specific version of the spine:

```
constraint-spine, tag: public-spine-v0, commit <hash>
```

See [ADR-0008](registry/DECISIONS/ADR-0008.md) for the rationale behind
versioned docs over editable wiki lore.
