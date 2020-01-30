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
print("qbit[0] and qbit[1] tensor inited: \n", circuit.qbits[0].tensor, "\n", circuit.qbits[0].tensor, "\n")
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
