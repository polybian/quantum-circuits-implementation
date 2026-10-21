"""
02 — Quantum teleportation: move a qubit's state without moving the qubit.

The protocol (3 qubits):
  q0 = the unknown state to teleport (here we prepare |1> for clarity)
  q1, q2 = a pre-shared Bell pair between sender (q1) and receiver (q2)

Steps:
  1. Create Bell pair between q1 and q2.
  2. Sender entangles q0 with q1 (CNOT + Hadamard) and measures both.
  3. The two classical bits tell the receiver which correction (X and/or Z)
     to apply to q2.
  4. q2 ends up in the original state of q0 — the state "teleported".

Expected result: q2 measures '1' (the state we prepared on q0) every time.

Run:
    python scripts/02_quantum_teleportation.py [--shots 1024]
"""

import argparse

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit_aer import AerSimulator


def build_teleport_circuit() -> QuantumCircuit:
    q = QuantumRegister(3, "q")
    c0 = ClassicalRegister(1, "c0")   # sender measurement of q0
    c1 = ClassicalRegister(1, "c1")   # sender measurement of q1
    c2 = ClassicalRegister(1, "c2")   # receiver measurement of q2
    qc = QuantumCircuit(q, c0, c1, c2)

    # 1. Prepare the unknown state on q0. We use |1> so we can verify.
    qc.x(q[0])

    # 2. Pre-shared Bell pair between sender (q1) and receiver (q2).
    qc.h(q[1])
    qc.cx(q[1], q[2])

    # 3. Sender's Bell-basis measurement on (q0, q1).
    qc.cx(q[0], q[1])
    qc.h(q[0])
    qc.measure(q[0], c0[0])
    qc.measure(q[1], c1[0])

    # 4. Receiver's conditional corrections on q2.
    with qc.if_test((c1, 1)):
        qc.x(q[2])
    with qc.if_test((c0, 1)):
        qc.z(q[2])

    # 5. Verify: measure q2 into c2.
    qc.measure(q[2], c2[0])
    return qc


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--shots", type=int, default=1024)
    args = parser.parse_args()

    qc = build_teleport_circuit()
    sim = AerSimulator(seed_simulator=7)
    result = sim.run(qc, shots=args.shots).result()
    counts = result.get_counts()

    print(f"Receiver qubit measurements over {args.shots} shots:")
    ok = 0
    for outcome in sorted(counts):
        # outcome format is "c2 c1 c0" — the leftmost bit is q2's result.
        receiver_bit = outcome.split()[0]
        ok += counts[outcome] if receiver_bit == "1" else 0
        print(f"  {outcome}  ->  q2 = {receiver_bit}   ({counts[outcome]} shots)")

    print()
    print(f"q2 == |1> (teleported state) in {ok}/{args.shots} shots "
          f"({100 * ok / args.shots:.1f}%)")
    assert ok == args.shots, "Teleportation failed!"
    print("OK — the state of q0 was teleported to q2.")


if __name__ == "__main__":
    main()
