# Architecture

## What this is

A hands-on introduction to quantum computing built with **Qiskit** (IBM's
open-source quantum SDK). Four self-contained implementations run from the
command line — no quantum hardware needed, everything executes on a
local statevector simulator (`qiskit-aer`).

## Layout

```
quantum-circuits-implementation/
├── README.md                  # overview, quickstart, validation results
├── requirements.txt           # qiskit + qiskit-aer
├── run_all.sh                 # runs all four implementations in order
├── scripts/
│   ├── 01_bell_state.py        # entanglement: H + CNOT, 2 qubits
│   ├── 02_quantum_teleportation.py  # teleport |1> using a Bell pair + 2 classical bits
│   ├── 03_grover_search.py     # amplitude amplification finds |11> in 1 query
│   └── 04_deutsch_jozsa.py     # constant vs balanced, decided in 1 query
├── docs/
│   └── architecture.md        # this file
└── simplified-explanation.md   # plain-language guide (Spanish)
```

## How it runs

```
┌──────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Python      │     │  Qiskit Aer      │     │  Your terminal  │
│  script      │────▶│  statevector     │────▶│  ASCII results  │
│  builds the  │     │  simulator       │     │  + assertions   │
│  circuit     │     │  (local CPU)     │     │                 │
└──────────────┘     └──────────────────┘     └─────────────────┘
```

Each script:
1. Builds a `QuantumCircuit` gate by gate.
2. Runs it on `AerSimulator` with a fixed seed (reproducible results).
3. Prints the circuit diagram and an ASCII histogram of outcomes.
4. Asserts the quantum-mechanical prediction (e.g. "only 00/11 appear").

## Simulator vs. real hardware

The Aer simulator is noise-free: results match theory exactly. Real
quantum processors (IBM Quantum's free tier at quantum.ibm.com) add
decoherence and gate errors, so the same circuits show statistical
spread instead of perfect outcomes. The scripts are written so the
only change needed to run on real hardware is swapping the backend:

```python
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler
service = QiskitRuntimeService()          # needs a free IBM Quantum token
backend = service.least_busy(operational=True, simulator=False)
```

That one-line swap is the bridge from "classroom exercise" to "I ran this
on a real quantum computer" — a strong line for an application.

## Design choices

- **Scripts, not notebooks**: runnable headless, testable in CI, easy to
  diff in git. (Notebooks are great for exploration; scripts are great
  for a portfolio.)
- **Fixed simulator seeds**: anyone who clones the repo gets the same
  numbers, which makes the validation section of the README checkable.
- **Assertions as specifications**: each script encodes the physics it
  demonstrates (`assert correlated == shots`), so "it works" is not a
  vibe — it's a passing check.
