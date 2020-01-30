import numpy as np
import tensornetwork as tn
import project_x as qc

circuit = qc.circuit_init(2)

print(type(circuit))
print("qbit[0] tensor inited: \n", circuit.qbits[0].tensor, "\n")
qc.apply_X(circuit, 0)
result = qc.calculate(circuit)
print("qbit[0] after X gate: \n", result.tensor, "\n")


circuit2 = qc.circuit_init(2)
print(type(circuit2))
print("qbit[0] and qbit[1] tensor inited: \n", circuit2.qbits[0].tensor, "\n", circuit2.qbits[0].tensor, "\n")
qc.apply_X(circuit2, 0)
qc.apply_CNOT(circuit2, 0, 1)
result = qc.calculate(circuit2)
print("state of 2 after X on q1 and CNOT gate: \n", result.tensor, "\n")

circuit3 = qc.circuit_init(2)
qc.apply_H(circuit3, 0)
qc.apply_CNOT(circuit3, 0, 1)
result = qc.calculate(circuit3)
print("qbit[0] after H gate: \n", result.tensor, "\n")
print("pribability of 11: ", qc.get_probability(result, [1, 1]))
print("pribability of 10: ", qc.get_probability(result, [1, 0]))
print("pribability of 10: ", qc.get_probability(result, [0, 1]))
print("pribability of 00: ", qc.get_probability(result, [0, 0]))

print("\n\n")
circuit4 = qc.circuit_init(1)
qc.apply_T(circuit4, 0)
result = qc.calculate(circuit4)
print("qbit[0] after T gate: \n", result.tensor, "\n")

print("\n\n")
circuit5 = qc.circuit_init(1)
qc.apply_Y(circuit5, 0)
result = qc.calculate(circuit5)
print("qbit[0] after Y gate: \n", result.tensor, "\n")






print("\n\n\n\n")
from qiskit import QuantumRegister, QuantumCircuit, execute, Aer

S_simulator = Aer.backends(name='statevector_simulator')[0]
q = QuantumRegister(1)
qubit = QuantumCircuit(q)

qubit.t(q[0])

job = execute(qubit, S_simulator)
result = job.result()
print(result.get_statevector())



circuit_3 = qc.circuit_init(3)
print("qbit[0] and qbit[1] tensor inited: \n", circuit_3.qbits[0].tensor, "\n", circuit_3.qbits[1].tensor, "\n", circuit_3.qbits[2].tensor)
qc.apply_H(circuit_3, 0)
qc.apply_H(circuit_3, 1)
qc.apply_CNOT(circuit_3, 0, 1)
qc.apply_CNOT(circuit_3, 1, 2)
result = qc.calculate(circuit_3)
print("state of 3 after h0, h1, cx10, cx12 : \n", result.tensor, "\n")
print("state shape : \n", result.tensor.shape, "\n")
print("pribability of 101: ", qc.get_probability(result, [1, 1, 0]))



print("qbit not in circuit")

circuit_q = qc.circuit_init(3)
print("qbit[0] and qbit[1] tensor inited: \n", circuit_q.qbits[0].tensor, "\n", circuit_q.qbits[1].tensor, "\n", circuit_q.qbits[2].tensor)
qc.apply_H(circuit_q, 0)
qc.apply_H(circuit_q, 2)
qc.apply_CNOT(circuit_q, 0, 1)
result = qc.calculate(circuit_q)
print("state of 3 after h0, h1, cx10, cx12 : \n", result.tensor, "\n")
print("state shape : \n", result.tensor.shape, "\n")
print("pribability of 101: ", qc.get_probability(result, [1, 1, 0]))
