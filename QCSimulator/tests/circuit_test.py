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
