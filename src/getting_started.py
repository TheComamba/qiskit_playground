# Copied from https://qiskit.qotlabs.org/docs/tutorials/hello-world

from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_ibm_runtime import EstimatorV2 as Estimator
from qiskit_ibm_runtime.fake_provider import FakeAlmadenV2
from matplotlib import pyplot

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

print(qc.draw())

observables_labels = ["IZ", "IX", "ZI", "XI", "ZZ", "XX"]
observables = [SparsePauliOp(label) for label in observables_labels]

backend = FakeAlmadenV2()
estimator = Estimator(backend)

preset_pass_manager = generate_preset_pass_manager(backend=backend, optimization_level=1)
isa_circuit = preset_pass_manager.run(qc)
mapped_observables = [
    observable.apply_layout(isa_circuit.layout) for observable in observables
]
 
job = estimator.run([(isa_circuit, mapped_observables)])
 
job_result = job.result()
pub_result = job_result[0]

values = pub_result.data.evs 
errors = pub_result.data.stds
 
pyplot.plot(observables_labels, values, "-o")
pyplot.xlabel("Observables")
pyplot.ylabel("Values")
pyplot.show()
