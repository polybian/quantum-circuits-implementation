"""
03 - Grover's search: quadratic speedup for unstructured search.

Problem: find the marked item '11' among 4 possibilities (2 qubits).
Classically you need ~2.25 queries on average. Grover's algorithm
finds it with a single oracle call by amplifying the amplitude of
the marked state.

Circuit:
  1. Hadamard on all qubits -> uniform superposition.
  2. Oracle: flips the phase of |11> (implemented with CZ).
  3. Diffuser: inversion about the mean (H, X, CZ, X, H).
  4. Measure.

Expected result: '11' dominates the counts (~100% for 2 qubits,
one iteration is optimal here).

Run:
    python scripts/03_grover_search.py [--shots 1024]
"""

import argparse

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def build_grover_circuit() -> QuantumCircuit:
    qc = QuantumCircuit(2, 2)

    # 1. Uniform superposition.
    qc.h([0, 1])

    # 2. Oracle: mark |11> by flipping its phase.
    qc.cz(0, 1)

    # 3. Diffuser: inversion about the mean.
    qc.h([0, 1])
    qc.x([0, 1])
    qc.cz(0, 1)
    qc.x([0, 1])
    qc.h([0, 1])

    qc.measure([0, 1], [0, 1])
    return qc


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--shots", type=int, default=1024)
    args = parser.parse_args()

    qc = build_grover_circuit()
    print("Circuit:")
    print(qc.draw(output="text"))
    print()

    sim = AerSimulator(seed_simulator=123)
    result = sim.run(qc, shots=args.shots).result()
    counts = result.get_counts()

    print(f"Results ({args.shots} shots), marked item = '11':")
    for outcome in sorted(counts):
        bar = "#" * int(40 * counts[outcome] / args.shots)
        marker = "  <-- marked" if outcome == "11" else ""
        print(f"  {outcome}  {counts[outcome]:>5}  {bar}{marker}")

    success = 100 * counts.get("11", 0) / args.shots
    print(f"\nMarked item found in {success:.1f}% of shots.")
    assert success > 95, "Grover amplification failed!"
    print("OK - amplitude amplification concentrated probability on |11>.")


if __name__ == "__main__":
    main()
