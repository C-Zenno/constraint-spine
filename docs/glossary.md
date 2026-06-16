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

**Tier classification:**
- **[P]** Primitive — smallest terms the rest of the framework depends on. Change rarely, only through governance.
- **[D]** Derived — structural consequences of primitives. May reference the primitive they derive from.
- **[G]** Governance — usage constraints, publication posture, drift protection. May be updated more often than primitives.

**Rule:** Definitions describe structural relations and claim boundaries. They do not provide measurement procedures, thresholds, or operational instructions.

---

## Terms

1) **Admissibility** — **[PUBLIC]** **[P]**
A condition that restricts what can be asserted or continued under finite resolution. It is a boundary concept, not a metric and not an instruction.

2) **Observer-only** — **[PUBLIC]** **[G]**
A posture in which outputs do not prescribe actions, optimize outcomes, or escalate authority. Outputs may be descriptive or structural, but not directive.

3) **Non-authoritative** — **[PUBLIC]** **[G]**
Outputs are not warrants for action, correctness, or ground truth—only bounded descriptions under stated limits.

4) **Finite resolution** — **[PUBLIC]** **[P]**
A statement that observation and representation occur with limited granularity (time, bandwidth, sampling, precision). This limits what can be concluded.

5) **Boundary** — **[PUBLIC]** **[P]**
A declared exclusion region: what claims are forbidden, what is refused, and what cannot be upgraded.

6) **Continuation** — **[PUBLIC]** **[P]**
The binary allowance for a claim to remain within a declared regime without expanding scope. Continuation is permitted or refused.

7) **Refusal** — **[PUBLIC]** **[P]**
A permitted outcome where the system declines to produce an output or declines to extend claims beyond allowed scope.

8) **Identity claim** — **[PUBLIC]** **[D]** *(see CG-PN-2.5; see also CG-FN-1 for continuation regimes)*
A continuation claim: it asserts that a declared distinction remains repeatable across an observation window under admissible evolution (within declared bounds and view perturbations), rather than being matched at a single index. Identity is persistence under bounds, not proximity at an instant.

9) **Snapshot** — **[PUBLIC]** **[D]** *(see CG-PN-2.5; see also CG-FN-1 for continuation regimes)*
An instant claim. A snapshot may exhibit pointwise resemblance at a time index under a particular view, but it does not, by itself, carry continuation across a window.

10) **Snapshot-to-identity prohibition** — **[PUBLIC]** **[D]** *(see CG-PN-2.5; see also CG-FN-1 for continuation regimes)*
The program refuses any interpretation that upgrades snapshot resemblance into identity, continuity, or persistence. When continuation cannot be carried (or cannot be made receiptable within declared bounds), snapshot resemblance is undefined for identity purposes.

11) **Regime** — **[PUBLIC]** **[P]**
A region of behavior or stability defined by what remains structurally continuous under finite resolution, without specifying the underlying mechanism.

12) **Coherence** — **[CONTROLLED]** **[P]**
A controlled technical parent term for how strongly a system holds together under perturbation and limited observation. Public surfaces should generally use *structural continuity* as the non-operational synonym unless a bounded technical bridge is explicitly required. No operational measure is defined here.

12a) **Structural continuity** — **[PUBLIC]** **[D]**
The public, non-operational rendering of controlled coherence language. Structural continuity describes whether a structure remains held together, carryable, or persistence-compatible under perturbation and limited observation. It defines no metric, score, threshold, or measurement procedure. Use this term on public doctrine and ZOA framework surfaces when no operational definition is intended.

13) **Deviation** — **[CONTROLLED]** **[D]**
A categorical notion of drift relative to a reference structure. No computation rules are defined here.

14) **Curvature (stability basin)** — **[CONTROLLED]** **[D]**
A geometric metaphor for local robustness/fragility. This surface does not provide formulas or estimation procedures.

15) **Marker** — **[CONTROLLED]** **[D]**
A non-directive indicator that something is changing. Markers are not triggers and must not be mapped into actions.

16) **Threshold** — **[PUBLIC]** **[G]** (prohibited in Stage-0 doctrine)
A numeric trigger boundary. This program explicitly avoids threshold-driven control surfaces in public doctrine.

17) **Instrumentation** — **[PUBLIC]** **[G]**
Any process that turns observations into action-authorizing signals. Instrumentation is excluded from declarative surfaces.

18) **Optimization** — **[PUBLIC]** **[G]**
A process that selects actions to maximize an objective. Optimization is excluded from observer-only posture.

19) **Control** — **[PUBLIC]** **[G]**
Any closed-loop action selection that modifies a system to achieve a target. Control is excluded from observer-only posture.

20) **Operationalization** — **[PUBLIC]** **[G]**
The act of turning a concept into a procedure, implementation, or recipe. Operationalization is out of scope here.

21) **Jurisdiction** — **[PUBLIC]** **[P]**
The declared boundary of what a document or system claims authority over (and what it refuses).

22) **Receipt / Receiptable** — **[PUBLIC]** **[P]**
A minimal provenance record that ties a claim to declared view families, bounds, and window semantics, sufficient for audit and refusal.

23) **Claimability** — **[PUBLIC]** **[D]**
A classification of what may be asserted under declared bounds: only repeatable structure under bounded perturbation is claimable in Stage-0.

24) **Governance event** — **[PUBLIC]** **[G]**
Any change that could expand scope, weaken exclusions, or enable operational inference. Governance events require review and explicit rationale.

25) **Admissible evolution** — **[PUBLIC]** **[D]** *(see CG-PN-2.5)*
Evolution of a system that remains within declared admissibility constraints. Identity and persistence are defined with respect to admissible evolution, not arbitrary state change.

26) **Persistence** — **[PUBLIC]** **[P]** *(see CG-PN-2.5)*
The structural property of being carried across admissible evolution over an observation window. Persistence is what distinguishes an identity claim from a snapshot claim. It is not proximity, similarity, or matching at an instant.

27) **Observation window** — **[PUBLIC]** **[P]** *(see CG-PN-2.5)*
A declared interval (temporal, sequential, or parametric) over which continuation and persistence are evaluated. Identity claims are characterized at the level of observation windows, not at single time indices.

28) **Pointwise resemblance** — **[PUBLIC]** **[D]** *(see CG-PN-2.5)*
Resemblance at a single time index or instant. Pointwise resemblance may preserve apparent structure but does not, by itself, carry continuation. Synonym: snapshot resemblance. See *Snapshot* (#9) and *Snapshot-to-identity prohibition* (#10).

29) **Continuation regime** — **[PUBLIC]** **[D]** *(see CG-FN-1)*
A declared region of behavior within which continuation is permitted. Regimes are characterized by what remains structurally continuous, not by what is computed or optimized.

30) **Closure (under admissible iteration)** — **[PUBLIC]** **[D]** *(see CG-FN-1)*
The property that repeated application of admissible evolution does not exit the declared regime. Closure is a structural constraint, not a verification procedure.

31) **Admissible iteration** — **[PUBLIC]** **[D]** *(see CG-FN-1)*
A single step of evolution that remains within declared admissibility bounds. Iterated admissible steps may or may not preserve continuation; this depends on closure.

32) **Anchor ladder** — **[PUBLIC]** **[D]** *(see CG-FN-1)*
A taxonomic ordering of receiptable weight classes (e.g., snapshot < window < regime). The ladder describes categorical distinctions, not scoring rules or numeric thresholds.

33) **Bounded observability** — **[PUBLIC]** **[D]** *(see Claim Rules)*
The declared limits of what is observable within a statement, including explicit unknowns and explicit out-of-scope regions.

34) **Irreversibility** — **[PUBLIC]** **[P]** *(see Claim Rules)*
A one-way commitment created by continuation, disclosure, or action, named when plausible without asserting mechanism or mitigation.

35) **Claim** — **[PUBLIC]** **[P]** *(see Claim Rules)*
A statement that hardens into implied authority or downstream dependence. Claims are treated as expensive under CRL-0 posture.

36) **Stop condition** — **[PUBLIC]** **[G]** *(see Claim Rules)*
The explicit point at which claims must stop. Stop conditions are required language, not optional caution.

37) **Narrative** — **[PUBLIC]** **[D]**
Interpretation offered around a record. Narrative may exist, but governance does not depend on it.

38) **Record** — **[PUBLIC]** **[P]**
A bounded trace attached to a claim, preserving scope and absences without persuasion.

39) **Governance primitive** — **[PUBLIC]** **[G]** *(see Claim Rules)*
A first-class boundary behavior (e.g., refusal, stop condition, receipts) that constrains continuation without asserting control.

40) **Archive edition** — **[PUBLIC]** **[G]**
A reissued citable record with a short preface stating scope, refusals, and version pin.

41) **Hierarchy (Constraint Physics)** — **[PUBLIC]** **[D]** *(see docs/HIERARCHY.md)*
A field-level ordering of primitives and dependent terms used to discipline claims. Not a derivation. Not a mechanism. Not a model. The ordering:
- **Time** (constrained substrate; bookkeeps admissible ordering under finite resolution)
- **Space / geometry** (relational structure)
- **Boundary + admissibility** (constraints on persistence/change under finite resolution)
- **Continuity** (minimal persistence condition under which ordering remains composable across admissible evolution)
- **Energy** (cost label for admissible change)
- **Mass** (stable persistence mode; non-primitive label)
- **Gravity / curvature** (effective geometric response associated with stable persistence)
- **Measurement / record** (boundary-coupling event; finite resolution; irreversibility of record)

42) **Continuity** — **[PUBLIC]** **[P]** *(see docs/HIERARCHY.md)*
The minimal persistence condition under which admissible ordering remains composable across admissible evolution. Continuity is a claim condition on composability, not a smoothness assumption or a mechanism.

43) **Boundary Fixture** — **[PUBLIC]** **[D]**
A domain where admissibility boundaries are known to exist, used as a structural stress test for claim language. No solving posture. Not a target; a reference fixture.

44) **Calibration Anchor** — **[PUBLIC]** **[D]**
A boundary fixture used specifically to stabilize admissibility vocabulary. Reference landmarks for claim discipline. Not an optimization objective.

45) **Multiplicity (pre-settlement)** — **[PUBLIC]** **[D]** *(see CG-PN-3.5)*
The condition in which multiple admissible trajectories may exist prior to settlement within an observation window. Multiplicity describes the geometry of admissible continuation before a claim is finalized. Multiplicity does not alter the binary nature of continuation.

46) **Settlement** — **[PUBLIC]** **[D]** *(see CG-PN-3.5)*
The point at which a continuation decision resolves into a single receiptable claim. Settlement selects one trajectory within the admissible manifold. Only settled claims are receiptable.

47) **Singular claim** — **[PUBLIC]** **[D]** *(see CG-PN-3.5)*
A claim referring to one trajectory following settlement. Claims remain singular even when multiplicity exists prior to settlement.

48) **Dynamic admissible space** — **[PUBLIC]** **[D]** *(see CG-PN-3.5)*
The region of admissible continuation available under current constraints and bounded observability. This region may expand or contract as regimes, boundaries, or observation limits change. Admissible space is structural and time-dependent.

49) **Constraint load** — **[PUBLIC]** **[D]** *(see CG-PN-3.5)*
The accumulated structural demand placed on a boundary by constraints, interactions, or regime conditions. Constraint load may alter admissible continuation without specifying measurement or thresholds.

50) **Disturbance projection** — **[PUBLIC]** **[D]** *(see CG-PN-3.5)*
The mapping of a shared disturbance into subsystem-specific constraint violations. Local failures may represent projections of a common upstream disturbance. Errors occur when projected disturbance intersects subsystem constraints in an inadmissible way.

51) **Settlement window** — **[PUBLIC]** **[D]** *(see CG-PN-3.5)*
The portion of an observation window in which multiplicity must resolve into a singular claim or refusal.

52) **Admissible manifold** — **[PUBLIC]** **[D]** *(see CG-PN-3.5)*
The set of trajectories permitted under current admissibility constraints within an observation window. Multiplicity describes the geometry of this manifold prior to settlement.

---

## Stack-aligned terms

Vocabulary tokens made publicly visible by the Admissibility Reading Posture view. Section headers in the stack remain section headers and are not promoted into doctrine primitives here.

53) **Identity** — **[PUBLIC]** **[P]**
A primitive distinction the program tracks across admissible evolution. Identity is a continuation property characterized at the level of an observation window; it is not pointwise resemblance or instantaneous match. See also #8 Identity claim.

54) **Memory** — **[PUBLIC]** **[P]**
A primitive distinction describing the structural condition under which past content remains carryable into a later observation. The term is a vocabulary token; no storage mechanism, retrieval procedure, or capacity claim is implied.

55) **Encoded persistence** — **[PUBLIC]** **[D]**
A relation governing primitives: the condition under which a primitive distinction is held in a way that survives admissible evolution. Structural condition only; no encoding scheme, format, or measurement is defined here.

56) **Boundary coupling** — **[PUBLIC]** **[D]**
A relation governing primitives: the way primitive distinctions are coupled to declared boundaries. Structural relation only; no interface specification, protocol, or signaling rule is defined here.

57) **Transport** — **[PUBLIC]** **[D]** *(see CG-FN-4)*
A transition-and-carry concept: the structural condition for moving a distinction across an observation window without violating admissibility. Names a boundary, not a transfer mechanism or routing procedure.

58) **Carry** — **[PUBLIC]** **[D]** *(see CG-FN-4)*
A transition-and-carry concept: the structural relation by which a distinction remains receiptable under admissible evolution. Carry is a claimability discipline; it does not assert preservation of identity, authority, capability, intent, interpretation, legitimacy, or continuation by default.

59) **Bounded structural access** — **[PUBLIC]** **[D]** *(see CG-P-0-A)*
A domain invariant: the declared limit on what structural content is accessible under finite resolution. Names a boundary; not an access protocol, permission system, or query interface.

60) **Universal coupling constraint** — **[PUBLIC]** **[D]**
A domain invariant: a categorical constraint on how primitives couple under admissibility. Describes structural ordering; not a numerical constant or measurable coupling.

61) **Resolution-depth constraint** — **[PUBLIC]** **[D]**
A domain invariant: the declared limit on resolution-depth pairs admissible within the boundary. Names a structural exclusion; not a depth setting, sampling rule, or resolution parameter.

62) **Contracted view** — **[PUBLIC]** **[D]** *(see CG-P-VIII)*
A resolution effect: a view in which observable structure is contracted relative to admissible structure. Categorical; not a parameter setting or filter configuration.

63) **Appearance class** — **[PUBLIC]** **[D]** *(see CG-P-VIII)*
A resolution effect: a category of how structure appears under a particular contracted view. Descriptive category; not a score, signature, or feature vector.

64) **Projection / coarse-graining** — **[PUBLIC]** **[D]**
A resolution effect: the structural relation that collapses admissible structure into a contracted view. Names a category of relation; not a transformation, mask, or filter definition.

65) **Apparent irreversibility** — **[PUBLIC]** **[D]**
A resolution effect: irreversibility observed under a contracted view that may not hold in the admissible substrate. Categorical observation; not a measurement or rate.

66) **Observer window** — **[PUBLIC]** **[D]**
A bounded subsystem concept: the declared region within which a bounded subsystem observes. Structural; not a temporal duration setting or sampling interval. See also #27 Observation window.

67) **Agency** — **[CONTROLLED]** **[D]**
A bounded subsystem term describing categorical capacity for admissible action within an observer window. Public surfaces should treat as conceptual posture only; no measurement procedure, scoring, or authority claim is defined here.

68) **Macro freedom** — **[CONTROLLED]** **[D]**
A bounded subsystem term describing categorical room for variation within admissible constraints. Public surfaces should treat as conceptual posture only; no degrees-of-freedom count, optimization, or capacity claim is defined here.

69) **Ledger cost** — **[CONTROLLED]** **[D]**
A conceptual cost label for the structural burden of remaining defined. Not an accounting construct, measurement, budget, or rate. No units or thresholds are defined here.

70) **Boundary rent** — **[CONTROLLED]** **[D]**
A conceptual cost label for the structural burden imposed by maintaining a boundary. Not an accounting construct, measurement, budget, or rate. No units or thresholds are defined here.

71) **Constraint affordability** — **[CONTROLLED]** **[D]**
A conceptual label for whether a constraint can be sustained under bounded observation. No affordability metric, budget, scoring, or evaluation rule is defined here.

---

## Side-branch terms (Learning Studies)

The following terms are side-branch vocabulary made publicly visible by the Admissibility Reading Posture view. They are not core admissibility primitives; they extend the framework into bounded learning under finite resolution.

72) **Learning Studies** — **[PUBLIC]** **[D]** *(side branch)*
A side-branch family that examines learning relative to admissibility discipline. Side-branch vocabulary; not a core admissibility primitive.

73) **Object-first learning** — **[PUBLIC]** **[D]** *(side branch; see CG-P-0-B)*
A side-branch posture treating objects as bounded, receiptable structures before explanation, prediction, or optimization. Claim discipline; not a learning algorithm, training procedure, or representation method.

74) **Situated object** — **[PUBLIC]** **[D]** *(side branch)*
A side-branch concept for an object considered together with its declared frame and admissibility limits. Categorical; not a data structure or representation format.

75) **Bounded frame** — **[PUBLIC]** **[D]** *(side branch; see CG-P-0-B)*
A side-branch concept for the declared frame within which a situated object is observed. Structural; not a configuration file, scope variable, or context window.

76) **Frame transit** — **[PUBLIC]** **[D]** *(side branch)*
A side-branch concept for the structural condition of crossing frames within Learning Studies. Names a boundary; not a transition algorithm or routing rule.

77) **Carried object identity** — **[PUBLIC]** **[D]** *(side branch; see CG-P-0-B, CG-FN-4)*
A side-branch concept for the condition under which an object's identity is carried across bounded frames. Categorical relation; not an identity-matching, similarity, or verification procedure.

78) **Transfer horizon** — **[PUBLIC]** **[D]** *(side branch; see CG-FN-4.5)*
A side-branch concept for the declared limit beyond which transfer ceases to be claimable. Structural; not a distance metric, runtime budget, or rate constant.
