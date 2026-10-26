# quantum-circuits-implementation

Four hands-on quantum computing implementations built with **Qiskit** (IBM's
open-source quantum SDK), runnable from the command line on a local
simulator: no quantum hardware, no account, no cost.

The same "rebuild it
yourself until you can explain it" method I used for networking,
identity, and cloud implementations, now applied to quantum computing, which I study as a hobby.

## The four implementations

| # | Script | What it demonstrates |
|---|--------|----------------------|
| 1 | `01_bell_state.py` | **Entanglement**: two qubits, always correlated (00 or 11, never 01/10) |
| 2 | `02_quantum_teleportation.py` | **Teleportation**: a qubit's state moves via a Bell pair + 2 classical bits |
| 3 | `03_grover_search.py` | **Quantum speedup**: finds the marked item in 1 query instead of ~2.25 |
| 4 | `04_deutsch_jozsa.py` | **Quantum advantage**: constant vs balanced, decided in a single query |

## Architecture

```
┌──────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Python      │     │  Qiskit Aer      │     │  Your terminal  │
│  script      │────▶│  statevector     │────▶│  circuit diagram│
│  builds the  │     │  simulator       │     │  + ASCII results│
│  circuit     │     │  (local CPU)     │     │  + assertions   │
└──────────────┘     └──────────────────┘     └─────────────────┘
```

Each script builds the circuit gate by gate, runs it on a seeded
simulator (reproducible), prints the results, and **asserts the
quantum-mechanical prediction**, so "it works" is a passing check,
not a vibe. See [docs/architecture.md](docs/architecture.md).

## Quickstart

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# run everything:
bash run_all.sh

# or a single implementation:
python3 scripts/01_bell_state.py --shots 2048
```

## Validation

All four implementations were executed on Qiskit Aer 2.6.0 (seeded simulator).
Measured results, 2026-10-21:

| Implementation | Prediction | Measured |
|------------|-----------|----------|
| Bell state (2048 shots) | only `00`/`11`, ~50/50 | `00`: 1001 (48.9%), `11`: 1047 (51.1%); correlated 2048/2048, assertion passed |
| Teleportation (1024 shots) | receiver qubit always `\|1⟩` | `\|1⟩` in 1024/1024 shots (100%): assertion passed |
| Grover (1024 shots) | marked `\|11⟩` dominates | `\|11⟩`: 1024/1024 (100%): assertion passed |
| Deutsch-Jozsa (512 shots ×2) | constant→`00`; balanced→≠`00` | constant: `{'00': 512}`; balanced: `{'11': 512}`: both classified correctly in 1 query, assertion passed |

(The exact counts above come from the seeded simulator run; re-running
reproduces them bit-for-bit. Unseeded runs fluctuate around the same
means, exactly as quantum mechanics predicts.)

## Going further

The circuits are hardware-ready. To run on a **real quantum processor**
(free tier at [quantum.ibm.com](https://quantum.ibm.com)), swap the
backend:

```python
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler
service = QiskitRuntimeService()  # free IBM Quantum token
backend = service.least_busy(operational=True, simulator=False)
```

On real hardware the same patterns appear with noise: decoherence and
gate errors spread the histograms. That gap between theory and hardware
is the central engineering challenge of the field, and the reason I
want to study quantum *engineering*, not just quantum theory.

Planned next steps: Bernstein-Vazirani and Simon algorithms, then a
small VQE (variational quantum eigensolver) for H₂, the "hello world"
of quantum chemistry.

## Plain-language guide

[simplified-explanation.md](simplified-explanation.md):
everything in this repo explained as if you were eight years old
(Spanish).
