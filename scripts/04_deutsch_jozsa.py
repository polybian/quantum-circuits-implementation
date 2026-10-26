"""
04 - Deutsch-Jozsa: the first algorithm proven faster than any classical one.

Problem: given a black-box function f on n bits, decide whether f is
CONSTANT (same output for all inputs) or BALANCED (0 for half the
inputs, 1 for the other half). Classically this can need 2^(n-1) + 1
queries in the worst case. Deutsch-Jozsa answers with ONE query.

Here n = 2. We run two oracles:
  * constant: f(x) = 0 for all x  -> measurement must be '00'
  * balanced: f(x) = x0 XOR x1    -> measurement must NOT be '00'

Expected result: '00' for constant, anything-but-'00' for balanced.

Run:
    python scripts/04_deutsch_jozsa.py [--shots 512]
"""

import argparse

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def build_dj_circuit(oracle: str) -> QuantumCircuit:
    # n input qubits + 1 ancilla.
    qc = QuantumCircuit(3, 2)

    # Ancilla starts in |-> state.
    qc.x(2)
    qc.h([0, 1, 2])

    # Oracle.
    if oracle == "constant":
        pass  # f(x) = 0: do nothing.
    elif oracle == "balanced":
        # f(x) = x0 XOR x1: phase kickback via two CNOTs.
        qc.cx(0, 2)
        qc.cx(1, 2)
    else:
        raise ValueError("oracle must be 'constant' or 'balanced'")

    # Final Hadamards on the input register, then measure it.
    qc.h([0, 1])
    qc.measure([0, 1], [0, 1])
    return qc


def run_case(oracle: str, shots: int) -> dict:
    sim = AerSimulator(seed_simulator=99)
    qc = build_dj_circuit(oracle)
    result = sim.run(qc, shots=shots).result()
    return result.get_counts()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--shots", type=int, default=512)
    args = parser.parse_args()

    constant_counts = run_case("constant", args.shots)
    balanced_counts = run_case("balanced", args.shots)

    print(f"Constant oracle (f = 0), {args.shots} shots: {constant_counts}")
    print(f"Balanced oracle (f = x0 XOR x1), {args.shots} shots: {balanced_counts}")

    assert set(constant_counts) == {"00"}, "Constant case misclassified!"
    assert "00" not in balanced_counts, "Balanced case misclassified!"
    print("\nOK - one query distinguished constant from balanced in both cases.")
    print("A classical computer could need up to 3 queries for n = 2.")


if __name__ == "__main__":
    main()
