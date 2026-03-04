---
Title: "CG-SR-0 — Descriptive Claim Schema"
Version: v0.1
Status: Canonical (public)
Surface: CC (Declarative)
Claim Ceiling: L0 — descriptive only
Authority: This document defines claim form only. Implementation-specific artifacts are out of scope.
Exclusions:
  - Methods, algorithms, procedures
  - Thresholds, coefficients, parameters
  - Evaluators, rankings, performance metrics
  - Detection or calibration logic
  - Deployment authorization
---

# CG-SR-0 — Descriptive Claim Schema

**Version:** v0.1
**Posture:** Stage-0 / observer-only / non-authoritative
**Claim ceiling:** L0 (descriptive only)
**Scope:** Defines citeable claim forms and receipt requirements.
**Explicit exclusions:** No procedures. No thresholds. No evaluators. No rankings. No deployment authorization.

---

## 0. Purpose

This document defines the structural form required for a citeable descriptive claim within Constraint Geometry.

It does not define how claims are produced.

---

## 1. Terms

**Descriptive coordinate space:** a bounded descriptive coordinate space used to label observational artifacts under declared constraints.

This is a claim-form schema only. It does not authorize classification, diagnosis, ranking, or policy use.

---

## 2. Allowed Claim Forms

### Regime Label (RL)

Descriptive tag applied under declared bounds.

Required:

* artifact identifier
* regime name
* bounds declaration
* view-family declaration
* version
* receipt references

---

### Clarity Envelope (CE)

Statement that description remains intelligible under declared perturbations.

Required:

* artifact identifier
* perturbation family declaration
* bounds declaration
* version
* receipt references

---

### View-Family Tag (VFT)

Declaration of interpretive coordinate system used.

Required:

* artifact identifier
* view-family declaration
* bounds declaration
* version
* receipt references

---

## 3. Minimum Claim Requirements

All claims must include:

* Unique claim identifier
* Artifact reference
* Claim form
* Declared bounds
* Declared view family
* Version tag
* Receipt references
* Explicit exclusions statement

Claims missing any required element are non-admissible.

---

## 4. Refusal Conditions

Claims are refused if they:

* Omit bounds
* Omit receipts
* Imply procedures or thresholds
* Assert evaluation, ranking, or performance
* Attach the schema to a specific domain as a classifier

---

## 5. Claim Ceiling

All claims under SR-0 are capped at L0 descriptive status.

This schema does not authorize:

* Measurement procedures
* Optimization
* Comparative evaluation
* Deployment in live environments

---

## 6. Status

SR-0 defines claim structure only.

It does not define implementation.
