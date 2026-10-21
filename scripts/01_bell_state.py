"""
01 — Bell state: the simplest entangled two-qubit system.

What it does:
  1. Puts qubit 0 into superposition with a Hadamard gate.
  2. Entangles qubit 1 with qubit 0 via a CNOT gate.
  3. Measures both qubits.

Expected result: the outcomes are ALWAYS correlated — you only ever
see '00' or '11', roughly 50/50. You never see '01' or '10'.
That perfect correlation, with each individual qubit still random,
is entanglement.

Run:
    python scripts/01_bell_state.py [--shots 2048]
"""

import argparse

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def build_bell_circuit() -> QuantumCircuit:
    qc = QuantumCircuit(2, 2)
    qc.h(0)          # superposition on qubit 0
    qc.cx(0, 1)      # entangle qubit 1 with qubit 0
    qc.measure([0, 1], [0, 1])
    return qc


def ascii_histogram(counts: dict, shots: int) -> str:
    lines = []
    for outcome in sorted(counts):
        bar = "#" * int(40 * counts[outcome] / shots)
        lines.append(f"  {outcome}  {counts[outcome]:>5}  {bar}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--shots", type=int, default=2048)
    args = parser.parse_args()

    qc = build_bell_circuit()
    print("Circuit:")
    print(qc.draw(output="text"))
    print()

    sim = AerSimulator(seed_simulator=42)
    result = sim.run(qc, shots=args.shots).result()
    counts = result.get_counts()

    print(f"Results ({args.shots} shots):")
    print(ascii_histogram(counts, args.shots))
    print()

    correlated = counts.get("00", 0) + counts.get("11", 0)
    print(f"Correlated outcomes (00 or 11): {correlated}/{args.shots} "
          f"({100 * correlated / args.shots:.1f}%)")
    assert correlated == args.shots, "Entanglement broken: saw 01 or 10!"
    print("OK — perfect correlation confirmed: the qubits are entangled.")


if __name__ == "__main__":
    main()
