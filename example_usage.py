"""Example demonstrating Gentzen LK Sequent Calculus proof search."""
from client import SequentProver

def main():
    p = ('ATOM', 'P')
    q = ('ATOM', 'Q')
    
    # Prove Law of Excluded Middle: P OR NOT P
    lem = ('OR', p, ('NOT', p))
    print("Proving P OR NOT P:", SequentProver.prove(lem))
    
    # Prove Peirce's Law: ((P -> Q) -> P) -> P
    peirce = ('IMP', ('IMP', ('IMP', p, q), p), p)
    print("Proving Peirce's Law:", SequentProver.prove(peirce))

if __name__ == "__main__":
    main()
