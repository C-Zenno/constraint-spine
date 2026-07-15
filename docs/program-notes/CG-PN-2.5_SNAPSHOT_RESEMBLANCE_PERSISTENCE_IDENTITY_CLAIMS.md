---
Status: Published
Surface: CC (Declarative)
ID: CG-PN-2.5
Claim Ceiling: jurisdictional clarification only (no procedures, evaluators, thresholds, calibration)
Authority: Observer-only | Non-authoritative | No directives
Exclusions: methods, algorithms, thresholds, calibration, procedures, recipes
Date: February 2026
---

# Program Note #2.5 — Snapshot Resemblance, Persistence, and Identity Claims

## Boundary & Scope Notice (CRL-0)

This Program Note is jurisdictional. It clarifies how identity and persistence claims are treated under the Constraint Program. It does not propose procedures, evaluators, thresholds, calibration logic, or operational guidance. No computation or test harness is specified.

---

## Purpose

To prevent a common interpretive error: upgrading **snapshot resemblance** into **identity**. This note formalizes the program's stance that identity depends on supported persistence under declared bounds, not pointwise resemblance.

---

## Interpretive Distinctions

**Identity Over Supported Persistence** — an identity claim is the bounded sameness-claim that may become admissible where a declared distinction remains supportable after passage under stated bounds.

**Snapshot / Pointwise Resemblance (Instant Claim)** — a snapshot claim asserts resemblance at a time index. It may preserve apparent structure, but it does not, by itself, establish continuation, persistence, or identity.

---

## Interpretive Constraint

Pointwise resemblance is **not sufficient** to establish identity. Identity is a bounded sameness-claim over supported persistence, not proximity at a single time.

---

## Refusal (Non-negotiable)

The program refuses any interpretation that upgrades snapshot similarity into identity, continuity, or persistence. When persistence cannot be supported under declared bounds, snapshot fidelity remains **insufficient for identity purposes**.

---

## Interpretive Significance

Many downstream confusions originate from treating "nearby state," "matched magnitude," or "projected back into a library" as equivalent to persistence. This note does not evaluate those moves; it only clarifies the jurisdictional rule: identity depends on supported persistence, not instantaneous resemblance.

---

## Revision History

| Revision | Changes |
|---|---|
| 2026-07 canonical alignment | Removed identity-as-continuation wording; aligned identity with supported persistence while preserving the snapshot refusal. |

---

## Routing Note

This note belongs to **CC** because it constrains interpretation and claim meaning. Any evaluation artifacts that test persistence, where they exist, belong downstream under **ZOA / OEL-1** posture and must remain non-authoritative and non-reconstructive.

---

**Identity claims require supported persistence under declared bounds; pointwise resemblance alone is insufficient.**
