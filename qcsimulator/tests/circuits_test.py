import qcsimulator as qcs
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

def test_circuit1_qiskit_comparison():
  circuit = qcs.circuit_init(2)
  circuit.h(0)
  circuit.cx(0, 1)
  result = circuit.execute()
  sv = result.get_state_vector()

  S_simulator = Aer.backends(name='statevector_simulator')[0]
  q = QuantumRegister(2)
  qubit = QuantumCircuit(q)
  qubit.h(q[0])
  qubit.cx(q[0], q[1])
  job = execute(qubit, S_simulator)
  result_qkit = job.result()
  sv_qkit = result_qkit.get_statevector()

  assert np.testing.assert_allclose(sv, sv_qkit, atol=1e-8, rtol=1e-8) == None

def test_circuit2_qiskit_comparison():
  circuit = qcs.circuit_init(2)
  circuit.x(1)
  circuit.cx(0, 1)
  circuit.cx(1, 0)
  circuit.cx(0, 1)
  result = circuit.execute()
  sv = result.get_state_vector()

  S_simulator = Aer.backends(name='statevector_simulator')[0]
  q = QuantumRegister(2)
  qubit = QuantumCircuit(q)
  qubit.x(q[1])
  qubit.cx(q[0], q[1])
  qubit.cx(q[1], q[0])
  qubit.cx(q[0], q[1])
  job = execute(qubit, S_simulator)
  result_qkit = job.result()
  sv_qkit = result_qkit.get_statevector()

  assert np.testing.assert_allclose(sv, sv_qkit, atol=1e-8, rtol=1e-8) == None

def test_circuit3_qiskit_comparison():
  circuit = qcs.circuit_init(3)
  circuit.y(0)
  circuit.h(0)
  circuit.x(0)
  circuit.cx(0, 1)
  circuit.h(0)
  circuit.cz(1, 2)
  circuit.cy(0, 2)
  circuit.cy(0, 2)
  circuit.cz(1, 2)
  circuit.h(0)
  circuit.cx(0, 1)
  circuit.x(0)
  circuit.h(0)
  circuit.y(0)
  result = circuit.execute()
  sv = result.get_state_vector()

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
  result_qkit = job.result()
  sv_qkit = result_qkit.get_statevector()

  assert np.testing.assert_allclose(sv, sv_qkit, atol=1e-8, rtol=1e-8) == None

def test_circuit4_qiskit_comparison():
  circuit = qcs.circuit_init(4)
  circuit.h(2)
  result = circuit.execute()
  sv = result.get_state_vector()

  S_simulator = Aer.backends(name='statevector_simulator')[0]
  q = QuantumRegister(4)
  qubit = QuantumCircuit(q)
  qubit.h(q[2])
  job = execute(qubit, S_simulator)
  result_qkit = job.result()
  sv_qkit = result_qkit.get_statevector()

  assert np.testing.assert_allclose(sv, sv_qkit, atol=1e-8, rtol=1e-8) == None

def test_empty_circuit_qiskit_comparison():
  circuit = qcs.circuit_init(10)
  result = circuit.execute()
  sv = result.get_state_vector()

  S_simulator = Aer.backends(name='statevector_simulator')[0]
  q = QuantumRegister(10)
  qubit = QuantumCircuit(q)
  job = execute(qubit, S_simulator)
  result_qkit = job.result()
  sv_qkit = result_qkit.get_statevector()

  assert np.testing.assert_allclose(sv, sv_qkit, atol=1e-8, rtol=1e-8) == None

def test_ones_circuit_qiskit_comparison():
  circuit = qcs.circuit_init(10)
  for i in range(10):
    circuit.x(i)
  result = circuit.execute()
  sv = result.get_state_vector()

  S_simulator = Aer.backends(name='statevector_simulator')[0]
  q = QuantumRegister(10)
  qubit = QuantumCircuit(q)
  for i in range(10):
    qubit.x(q[i])
  job = execute(qubit, S_simulator)
  result_qkit = job.result()
  sv_qkit = result_qkit.get_statevector()

  assert np.testing.assert_allclose(sv, sv_qkit, atol=1e-8, rtol=1e-8) == None

def test_h_ch_circuit_qiskit_comparison():
  circuit = qcs.circuit_init(2)
  circuit.h(0)
  circuit.ch(0, 1)
  result = circuit.execute()
  sv = result.get_state_vector()

  S_simulator = Aer.backends(name='statevector_simulator')[0]
  q = QuantumRegister(2)
  qubit = QuantumCircuit(q)
  qubit.h(q[0])
  qubit.ch(q[0], q[1])
  job = execute(qubit, S_simulator)
  result_qkit = job.result()
  sv_qkit = result_qkit.get_statevector()

  assert np.testing.assert_allclose(sv, sv_qkit, atol=1e-8, rtol=1e-8) == None
