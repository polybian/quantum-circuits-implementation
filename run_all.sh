#!/usr/bin/env bash
# Runs every implementation in order.
set -euo pipefail
cd "$(dirname "$0")"

# Prefer the project's venv (where qiskit lives); fall back to python3.
if [ -x ".venv/bin/python" ]; then
  PY=".venv/bin/python"
else
  PY="python3"
fi

echo "=== 01 - Bell state (entanglement) ==="
$PY scripts/01_bell_state.py
echo
echo "=== 02 - Quantum teleportation ==="
$PY scripts/02_quantum_teleportation.py
echo
echo "=== 03 - Grover's search ==="
$PY scripts/03_grover_search.py
echo
echo "=== 04 - Deutsch-Jozsa ==="
$PY scripts/04_deutsch_jozsa.py
echo
echo "All four implementations completed successfully."
