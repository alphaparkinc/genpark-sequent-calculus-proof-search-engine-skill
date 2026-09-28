"""Gentzen Propositional LK Sequent Calculus Proof Engine.
100% Python Standard Library.
"""

class SequentProver:
    """Decides propositional validities via cut-free Gentzen sequent calculus."""
    @staticmethod
    def prove(formula):
        """Proves whether formula is a tautology (i.e. empty => [formula] is derivable)."""
        return SequentProver._prove_sequent([], [formula])

    @staticmethod
    def _prove_sequent(gamma, delta):
        # Axiom check: if Gamma and Delta share an atomic formula -> closed leaf
        for g in gamma:
            if g[0] == 'ATOM' and any(d == g for d in delta):
                return True

        # Left rules (decompose in Gamma)
        for i, g in enumerate(gamma):
            rest = gamma[:i] + gamma[i+1:]
            op = g[0]
            if op == 'NOT':
                return SequentProver._prove_sequent(rest, delta + [g[1]])
            elif op == 'AND':
                return SequentProver._prove_sequent(rest + [g[1], g[2]], delta)
            elif op == 'OR':
                return (SequentProver._prove_sequent(rest + [g[1]], delta) and
                        SequentProver._prove_sequent(rest + [g[2]], delta))
            elif op == 'IMP':
                return (SequentProver._prove_sequent(rest, delta + [g[1]]) and
                        SequentProver._prove_sequent(rest + [g[2]], delta))

        # Right rules (decompose in Delta)
        for i, d in enumerate(delta):
            rest = delta[:i] + delta[i+1:]
            op = d[0]
            if op == 'NOT':
                return SequentProver._prove_sequent(gamma + [d[1]], rest)
            elif op == 'AND':
                return (SequentProver._prove_sequent(gamma, rest + [d[1]]) and
                        SequentProver._prove_sequent(gamma, rest + [d[2]]))
            elif op == 'OR':
                return SequentProver._prove_sequent(gamma, rest + [d[1], d[2]])
            elif op == 'IMP':
                return SequentProver._prove_sequent(gamma + [d[1]], rest + [d[2]])

        return False
