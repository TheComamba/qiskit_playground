from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_ibm_runtime import EstimatorV2 as Estimator

compact_toffoli = QuantumCircuit(3)
compact_toffoli.ccx(0, 1, 2)
print(compact_toffoli.draw())

expanded_toffoli = QuantumCircuit(3)
expanded_toffoli.h(2)
expanded_toffoli.cx(1, 2)
