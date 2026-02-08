---
Status: DRAFT
Surface: CC (Declarative)
Claim Ceiling: controlled vocabulary (no methods)
Authority: Observer-only | Non-authoritative | No directives
Exclusions: methods, algorithms, thresholds, calibration, procedures, recipes
---

# Glossary (Controlled Vocabulary)

**Legend (IP status markers):**
- **[PUBLIC]** Safe to define categorically.
- **[CONTROLLED]** Name may be public; definition must stay non-operational.
- **[INTERNAL]** Term may be referenced but not defined here.

**Rule:** Definitions describe **what a term *means*** at a categorical level, not **how to compute, detect, calibrate, or act**.

---

## Terms

1) **Admissibility** — **[PUBLIC]**
A condition that restricts what can be asserted or continued under finite resolution. It is a boundary concept, not a metric and not an instruction.

2) **Observer-only** — **[PUBLIC]**
A posture in which outputs do not prescribe actions, optimize outcomes, or escalate authority. Outputs may be descriptive or structural, but not directive.

3) **Non-authoritative** — **[PUBLIC]**
Outputs are not warrants for action, correctness, or ground truth—only bounded descriptions under stated limits.

4) **Finite resolution** — **[PUBLIC]**
A statement that observation and representation occur with limited granularity (time, bandwidth, sampling, precision). This limits what can be concluded.

5) **Boundary** — **[PUBLIC]**
A declared exclusion region: what claims are forbidden, what is refused, and what cannot be upgraded.

6) **Continuation** — **[PUBLIC]**
The allowance to remain within a declared regime without expanding scope. Continuation is not guaranteed; refusal is permitted.

7) **Refusal** — **[PUBLIC]**
A permitted outcome where the system declines to produce an output or declines to extend claims beyond allowed scope.

8) **Identity claim** — **[PUBLIC]** *(see CG-PN-2.5; see also CG-FN-1 for continuation regimes)*
A continuation claim: it asserts that a declared distinction remains repeatable across an observation window under admissible evolution (within declared bounds and view perturbations), rather than being matched at a single index. Identity is persistence under bounds, not proximity at an instant.

9) **Snapshot** — **[PUBLIC]** *(see CG-PN-2.5; see also CG-FN-1 for continuation regimes)*
An instant claim. A snapshot may exhibit pointwise resemblance at a time index under a particular view, but it does not, by itself, carry continuation across a window.

10) **Snapshot-to-identity prohibition** — **[PUBLIC]** *(see CG-PN-2.5; see also CG-FN-1 for continuation regimes)*
The program refuses any interpretation that upgrades snapshot resemblance into identity, continuity, or persistence. When continuation cannot be carried (or cannot be made receiptable within declared bounds), snapshot resemblance is undefined for identity purposes.

11) **Regime** — **[PUBLIC]**
A region of behavior or stability defined by what remains coherent under finite resolution, without specifying the underlying mechanism.

12) **Coherence** — **[CONTROLLED]**
A structural property describing how strongly a system holds together under perturbation and limited observation. No operational measure is defined here.

13) **Deviation** — **[CONTROLLED]**
A categorical notion of drift relative to a reference structure. No computation rules are defined here.

14) **Curvature (stability basin)** — **[CONTROLLED]**
A geometric metaphor for local robustness/fragility. This surface does not provide formulas or estimation procedures.

15) **Marker** — **[CONTROLLED]**
A non-directive indicator that something is changing. Markers are not triggers and must not be mapped into actions.

16) **Threshold** — **[PUBLIC]** (prohibited in Stage-0 doctrine)
A numeric trigger boundary. This program explicitly avoids threshold-driven control surfaces in public doctrine.

17) **Instrumentation** — **[PUBLIC]**
Any process that turns observations into action-authorizing signals. Instrumentation is excluded from declarative surfaces.

18) **Optimization** — **[PUBLIC]**
A process that selects actions to maximize an objective. Optimization is excluded from observer-only posture.

19) **Control** — **[PUBLIC]**
Any closed-loop action selection that modifies a system to achieve a target. Control is excluded from observer-only posture.

20) **Operationalization** — **[PUBLIC]**
The act of turning a concept into a procedure, implementation, or recipe. Operationalization is out of scope here.

21) **Jurisdiction** — **[PUBLIC]**
The declared boundary of what a document or system claims authority over (and what it refuses).

22) **Receipt / Receiptable** — **[PUBLIC]**
A minimal provenance record that ties a claim to declared view families, bounds, and window semantics, sufficient for audit and refusal.

23) **Claimability** — **[PUBLIC]**
A classification of what may be asserted under declared bounds: only repeatable structure under bounded perturbation is claimable in Stage-0.

24) **Governance event** — **[PUBLIC]**
Any change that could expand scope, weaken exclusions, or enable operational inference. Governance events require review and explicit rationale.

25) **Admissible evolution** — **[PUBLIC]** *(see CG-PN-2.5)*
Evolution of a system that remains within declared admissibility constraints. Identity and persistence are defined with respect to admissible evolution, not arbitrary state change.

26) **Persistence** — **[PUBLIC]** *(see CG-PN-2.5)*
The structural property of being carried across admissible evolution over an observation window. Persistence is what distinguishes an identity claim from a snapshot claim. It is not proximity, similarity, or matching at an instant.

27) **Observation window** — **[PUBLIC]** *(see CG-PN-2.5)*
A declared interval (temporal, sequential, or parametric) over which continuation and persistence are evaluated. Identity claims are characterized at the level of observation windows, not at single time indices.

28) **Pointwise resemblance** — **[PUBLIC]** *(see CG-PN-2.5)*
Resemblance at a single time index or instant. Pointwise resemblance may preserve apparent structure but does not, by itself, carry continuation. Synonym: snapshot resemblance. See *Snapshot* (#9) and *Snapshot-to-identity prohibition* (#10).

29) **Continuation regime** — **[PUBLIC]** *(see CG-FN-1)*
A declared region of behavior within which continuation is permitted. Regimes are characterized by what remains coherent, not by what is computed or optimized.

30) **Closure (under admissible iteration)** — **[PUBLIC]** *(see CG-FN-1)*
The property that repeated application of admissible evolution does not exit the declared regime. Closure is a structural constraint, not a verification procedure.

31) **Admissible iteration** — **[PUBLIC]** *(see CG-FN-1)*
A single step of evolution that remains within declared admissibility bounds. Iterated admissible steps may or may not preserve continuation; this depends on closure.

32) **Anchor ladder** — **[PUBLIC]** *(see CG-FN-1)*
A taxonomic ordering of receiptable weight classes (e.g., snapshot < window < regime). The ladder describes categorical distinctions, not scoring rules or numeric thresholds.

33) **Bounded observability** — **[PUBLIC]** *(see Claim Rules)*
The declared limits of what is observable within a statement, including explicit unknowns and explicit out-of-scope regions.

34) **Irreversibility** — **[PUBLIC]** *(see Claim Rules)*
A one-way commitment created by continuation, disclosure, or action, named when plausible without asserting mechanism or mitigation.

35) **Claim** — **[PUBLIC]** *(see Claim Rules)*
A statement that hardens into implied authority or downstream dependence. Claims are treated as expensive under CRL-0 posture.

36) **Stop condition** — **[PUBLIC]** *(see Claim Rules)*
The explicit point at which claims must stop. Stop conditions are required language, not optional caution.

37) **Narrative** — **[PUBLIC]** *(see Signature Map)*
Interpretation offered around a record. Narrative may exist, but governance does not depend on it.

38) **Record** — **[PUBLIC]** *(see Signature Map)*
A bounded trace attached to a claim, preserving scope and absences without persuasion.

39) **Governance primitive** — **[PUBLIC]** *(see Claim Rules)*
A first-class boundary behavior (e.g., refusal, stop condition, receipts) that constrains continuation without asserting control.

40) **Archive edition** — **[PUBLIC]**
A reissued citable record with a short preface stating scope, refusals, and version pin.
