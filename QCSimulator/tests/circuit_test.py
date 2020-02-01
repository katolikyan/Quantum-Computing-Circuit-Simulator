import QCSimulator as qcs
import numpy as np
import tensornetwork as tn
import pytest
from qiskit import QuantumRegister, QuantumCircuit, execute, Aer

def test_circuit_init():
  circuit = qcs.circuit_init(1)
  with(pytest.raises(ValueError)):
    circuit_to_much = qcs.circuit_init(21)
  with(pytest.raises(ValueError)):
    circuit_negative = qcs.circuit_init(-1)
  with(pytest.raises(ValueError)):
    circuit_zero = qcs.circuit_init(0)
  assert len(circuit._qbits) == 1

def test_gates_check_input():
  circuit = qcs.circuit_init(2)
  circuit.x(0)
  circuit.x(-1)
  circuit.cx(-2, -1)
  circuit.cx(1, 0)
  with(pytest.raises(ValueError)):
    circuit.x(2)
  with(pytest.raises(ValueError)):
    circuit.x(-3)
  with(pytest.raises(ValueError)):
    circuit.cx(1, -3)
  with(pytest.raises(ValueError)):
    circuit.cx(4, 0)
  with(pytest.raises(ValueError)):
    circuit.cx(0, 0)
  with(pytest.raises(ValueError)):
    circuit.x("0")


def test_solo_gates_simpletest():
  circuit = qcs.circuit_init(1)
  circuit.x(0)
  circuit.y(0)
  circuit.z(0)
  circuit.h(0)
  circuit.t(0)
  result = circuit.execute()

def test_controlled_gates_simpletest():
  circuit = qcs.circuit_init(2)
  circuit.ch(0, 1)
  circuit.cx(0, 1)
  circuit.cy(0, 1)
  circuit.cz(0, 1)
  result = circuit.execute()

def test_x_gate_qiskit_comparison():
  S_simulator = Aer.backends(name='statevector_simulator')[0]
  q = QuantumRegister(1)
  qubit = QuantumCircuit(q)
  qubit.x(q[0])
  job = execute(qubit, S_simulator)
  result = job.result()
  circuit = qcs.circuit_init(1)
  circuit.x(0)
  res = circuit.execute()
  arr1 = result.get_statevector()
  arr2 = res.tensor.flatten()
  assert np.testing.assert_allclose(arr1, arr2, atol=0, rtol=1e-5) == None

def test_y_gate_qiskit_comparison():
  S_simulator = Aer.backends(name='statevector_simulator')[0]
  q = QuantumRegister(1)
  qubit = QuantumCircuit(q)
  qubit.y(q[0])
  job = execute(qubit, S_simulator)
  result = job.result()
  circuit = qcs.circuit_init(1)
  circuit.y(0)
  res = circuit.execute()
  arr1 = result.get_statevector()
  arr2 = res.tensor.flatten()
  assert np.testing.assert_allclose(arr1, arr2, atol=0, rtol=1e-5) == None

def test_z_gate_qiskit_comparison():
  S_simulator = Aer.backends(name='statevector_simulator')[0]
  q = QuantumRegister(1)
  qubit = QuantumCircuit(q)
  qubit.z(q[0])
  job = execute(qubit, S_simulator)
  result = job.result()
  circuit = qcs.circuit_init(1)
  circuit.z(0)
  res = circuit.execute()
  arr1 = result.get_statevector()
  arr2 = res.tensor.flatten()
  assert np.testing.assert_allclose(arr1, arr2, atol=0, rtol=1e-5) == None


def test_circuit_3_qiskit_compartison():
  circuit_3 = qcs.circuit_init(3)
  circuit_3.y(0)
  circuit_3.h(0)
  circuit_3.x(0)
  circuit_3.cx(0, 1)
  circuit_3.h(0)
  circuit_3.cz(1, 2)
  circuit_3.cy(0, 2)
  circuit_3.cy(0, 2)
  circuit_3.cz(1, 2)
  circuit_3.h(0)
  circuit_3.cx(0, 1)
  circuit_3.x(0)
  circuit_3.h(0)
  circuit_3.y(0)
  result_3 = circuit_3.execute()


  S_simulator = Aer.backends(name='statevector_simulator')[0]
  q = QuantumRegister(3)
  qubit = QuantumCircuit(q)
  qubit.y(q[0])
  qubit.h(q[0])
  qubit.x(q[0])
  qubit.cx(q[0], q[1])
  qubit.h(q[0])
  qubit.cz(q[1], q[2])
  qubit.cy(q[0], q[2])
  qubit.cy(q[0], q[2])
  qubit.cz(q[1], q[2])
  qubit.h(q[0])
  qubit.cx(q[0], q[1])
  qubit.x(q[0])
  qubit.h(q[0])
  qubit.y(q[0])
  job = execute(qubit, S_simulator)
  result_q = job.result()

  arr1 = result_q.get_statevector()
  arr2 = result_3.tensor.flatten()
  assert np.testing.assert_allclose(arr1, arr2, atol=1e-5, rtol=1e-5) == None
