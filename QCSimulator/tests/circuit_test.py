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

def test_single_gates_simpletest():
  circuit = qcs.circuit_init(1)
  circuit.x(0)
  circuit.y(0)
  circuit.z(0)
  circuit.h(0)
  circuit.t(0)
  result = circuit.execute()

def test_controll_gates_simpletest():
  circuit = qcs.circuit_init(2)
  circuit.ch(0, 1)
  circuit.cx(0, 1)
  circuit.cy(0, 1)
  circuit.cz(0, 1)
  result = circuit.execute()

def test_x_gate_qiskit_comparison():
  circuit = qcs.circuit_init(1)
  circuit.x(0)
  result = circuit.execute()

  S_simulator = Aer.backends(name='statevector_simulator')[0]
  q = QuantumRegister(1)
  qubit = QuantumCircuit(q)
  qubit.x(q[0])
  job = execute(qubit, S_simulator)
  result_qkit = job.result()

  sv_qkit = result_qkit.get_statevector()
  sv = result.get_state_vector()

  assert np.testing.assert_allclose(sv, sv_qkit, atol=1e-8, rtol=1e-8) == None

def test_y_gate_qiskit_comparison():
  circuit = qcs.circuit_init(1)
  circuit.y(0)
  result = circuit.execute()

  S_simulator = Aer.backends(name='statevector_simulator')[0]
  q = QuantumRegister(1)
  qubit = QuantumCircuit(q)
  qubit.y(q[0])
  job = execute(qubit, S_simulator)
  result_qkit = job.result()

  sv_qkit = result_qkit.get_statevector()
  sv = result.get_state_vector()
  assert np.testing.assert_allclose(sv, sv_qkit, atol=1e-8, rtol=1e-8) == None

def test_z_gate_qiskit_comparison():
  circuit = qcs.circuit_init(1)
  circuit.z(0)
  result = circuit.execute()

  S_simulator = Aer.backends(name='statevector_simulator')[0]
  q = QuantumRegister(1)
  qubit = QuantumCircuit(q)
  qubit.z(q[0])
  job = execute(qubit, S_simulator)
  result_qkit = job.result()

  sv_qkit = result_qkit.get_statevector()
  sv = result.get_state_vector()
  assert np.testing.assert_allclose(sv, sv_qkit, atol=1e-8, rtol=1e-8) == None

def test_h_gate_qiskit_comparison():
  circuit = qcs.circuit_init(1)
  circuit.h(0)
  result = circuit.execute()

  S_simulator = Aer.backends(name='statevector_simulator')[0]
  q = QuantumRegister(1)
  qubit = QuantumCircuit(q)
  qubit.h(q[0])
  job = execute(qubit, S_simulator)
  result_qkit = job.result()

  sv_qkit = result_qkit.get_statevector()
  sv = result.get_state_vector()
  assert np.testing.assert_allclose(sv, sv_qkit, atol=1e-8, rtol=1e-8) == None

def test_t_gate_qiskit_comparison():
  circuit = qcs.circuit_init(1)
  circuit.t(0)
  result = circuit.execute()

  S_simulator = Aer.backends(name='statevector_simulator')[0]
  q = QuantumRegister(1)
  qubit = QuantumCircuit(q)
  qubit.t(q[0])
  job = execute(qubit, S_simulator)
  result_qkit = job.result()

  sv_qkit = result_qkit.get_statevector()
  sv = result.get_state_vector()
  assert np.testing.assert_allclose(sv, sv_qkit, atol=1e-8, rtol=1e-8) == None

# CNOT, CZ, CY, CH,
def test_cx_gate_qiskit_comparison():
  circuit = qcs.circuit_init(2)
  circuit.h(0)
  circuit.cx(0, 1)
  result = circuit.execute()

  S_simulator = Aer.backends(name='statevector_simulator')[0]
  q = QuantumRegister(2)
  qubit = QuantumCircuit(q)
  qubit.h(q[0])
  qubit.cx(q[0], q[1])
  job = execute(qubit, S_simulator)
  result_qkit = job.result()

  sv_qkit = result_qkit.get_statevector()
  sv = result.get_state_vector()
  assert np.testing.assert_allclose(sv, sv_qkit, atol=1e-8, rtol=1e-8) == None

def test_cz_gate_qiskit_comparison():
  circuit = qcs.circuit_init(2)
  circuit.h(0)
  circuit.cz(0, 1)
  result = circuit.execute()

  S_simulator = Aer.backends(name='statevector_simulator')[0]
  q = QuantumRegister(2)
  qubit = QuantumCircuit(q)
  qubit.h(q[0])
  qubit.cz(q[0], q[1])
  job = execute(qubit, S_simulator)
  result_qkit = job.result()

  sv_qkit = result_qkit.get_statevector()
  sv = result.get_state_vector()
  assert np.testing.assert_allclose(sv, sv_qkit, atol=1e-8, rtol=1e-8) == None

def test_cy_gate_qiskit_comparison():
  circuit = qcs.circuit_init(2)
  circuit.h(0)
  circuit.cy(0, 1)
  result = circuit.execute()

  S_simulator = Aer.backends(name='statevector_simulator')[0]
  q = QuantumRegister(2)
  qubit = QuantumCircuit(q)
  qubit.h(q[0])
  qubit.cy(q[0], q[1])
  job = execute(qubit, S_simulator)
  result_qkit = job.result()

  sv_qkit = result_qkit.get_statevector()
  sv = result.get_state_vector()
  assert np.testing.assert_allclose(sv, sv_qkit, atol=1e-8, rtol=1e-8) == None

def test_ch_gate_qiskit_comparison():
  circuit = qcs.circuit_init(2)
  circuit.h(0)
  circuit.ch(0, 1)
  result = circuit.execute()

  S_simulator = Aer.backends(name='statevector_simulator')[0]
  q = QuantumRegister(2)
  qubit = QuantumCircuit(q)
  qubit.h(q[0])
  qubit.ch(q[0], q[1])
  job = execute(qubit, S_simulator)
  result_qkit = job.result()

  sv_qkit = result_qkit.get_statevector()
  sv = result.get_state_vector()
  assert np.testing.assert_allclose(sv, sv_qkit, atol=1e-8, rtol=1e-8) == None

def test_circuit1_qiskit_compartison():
  circuit = qcs.circuit_init(2)
  circuit.h(0)
  circuit.cx(0, 1)
  result = circuit.execute()

  S_simulator = Aer.backends(name='statevector_simulator')[0]
  q = QuantumRegister(2)
  qubit = QuantumCircuit(q)
  qubit.h(q[0])
  qubit.cx(q[0], q[1])
  job = execute(qubit, S_simulator)
  result_qkit = job.result()

  sv_qkit = result_qkit.get_statevector()
  sv = result.get_state_vector()
  assert np.testing.assert_allclose(sv, sv_qkit, atol=1e-8, rtol=1e-8) == None

def test_circuit2_qiskit_compartison():
  circuit = qcs.circuit_init(2)
  circuit.x(1)
  circuit.cx(0, 1)
  circuit.cx(1, 0)
  circuit.cx(0, 1)
  result = circuit.execute()

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
  sv = result.get_state_vector()
  assert np.testing.assert_allclose(sv, sv_qkit, atol=1e-8, rtol=1e-8) == None

def test_circuit3_qiskit_compartison():
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
  sv = result.get_state_vector()
  assert np.testing.assert_allclose(sv, sv_qkit, atol=1e-8, rtol=1e-8) == None
