# Gentzen Sequent Calculus LK Prover Skill

Automated cut-free sequent calculus theorem prover for classical propositional logic.

```mermaid
flowchart TD
    Formula["Input Propositional Formula φ"] --> Root["Root Sequent: ∅ ⟹ φ"]
    Root --> RuleDecomp["Structural & Logical Rule Inversion"]
    RuleDecomp --> Leaves["Leaf Sequents: Γ, A ⟹ Δ, A"]
    Leaves --> AxiomCheck{"All Leaves Axiomatic?"}
    AxiomCheck -- Yes --> Proved["Valid Theorem (Q.E.D.)"]
    AxiomCheck -- No --> Disproved["Counter-model / Non-tautology"]
```

## Features
- **100% Python Standard Library**: Structural proof tree decomposition.
- **Cut Elimination Guarantee**: Analytic proof search guaranteed to terminate.
- **Decidable Propositional Validity**: Exact proof of classical tautologies.
