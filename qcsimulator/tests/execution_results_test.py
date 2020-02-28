import qcsimulator as qcs
import numpy as np
import tensornetwork as tn
import pytest
from qiskit import QuantumRegister, QuantumCircuit, execute, Aer

# global circuit with known values for tests
prob_table_big_end = {"00": 0.4999, "10": 0.24999, "01": 0.0, "11": 0.24999}
prob_table_little_end = {"00": 0.4999, "01": 0.24999, "10": 0.0, "11": 0.24999}
circuit = qcs.circuit_init(2)
circuit.h(0)
circuit.ch(0, 1)
result = circuit.execute()

def test_disabled_autocalc():
  circuit = qcs.circuit_init(2)
  circuit.h(0)
  circuit.ch(0, 1)
  with(pytest.raises(TypeError)):
    result = circuit.execute(probs_autocalc="no")
  result = circuit.execute(probs_autocalc=False)
  with(pytest.raises(ValueError)):
    result.get_all_probabilities()
  with(pytest.raises(ValueError)):
    result.get_n_qubit_probability(1, 3)
  with(pytest.raises(ValueError)):
    result.get_bitstr_probability()

def test_errors():
  circuit = qcs.circuit_init(2)
  circuit.h(0)
  circuit.ch(0, 1)
  result = circuit.execute()
  with(pytest.raises(TypeError)):
    result.get_single_qubit_probability("0")
    result.get_bitstr_probability(1)
  with(pytest.raises(IndexError)):
    result.get_single_qubit_probability(10)
    result.get_n_qubit_probability(0, -1)
    result.get_n_qubit_probability(0, 10)
  with(pytest.raises(ValueError)):
    result.get_bitstr_probability("1000110")
    result.get_bitstr_probability("123")

def test_get_single_probability():
  prob_0 = result.get_bitstr_probability("00");
  prob_1 = result.get_bitstr_probability("10");
  prob_2 = result.get_bitstr_probability("01");
  prob_3 = result.get_bitstr_probability("11");
  assert prob_0["00"] == pytest.approx(prob_table_little_end["00"], 1e-3)
  assert prob_1["10"] == pytest.approx(prob_table_little_end["10"], 1e-3)
  assert prob_2["01"] == pytest.approx(prob_table_little_end["01"], 1e-3)
  assert prob_3["11"] == pytest.approx(prob_table_little_end["11"], 1e-3)

def test_get_random_probability():
  for i in range(5):
    prob = result.get_bitstr_probability();
    for key in prob:
      assert prob[key] == pytest.approx(prob_table_little_end[key], 1e-3)

def test_get_all_probability():
  probs = result.get_all_probabilities()
  for key in probs:
    assert probs[key] == pytest.approx(prob_table_little_end[key], 1e-3)

def test_single_qubit_probability():
  solo_prob = result.get_single_qubit_probability(0)
  keys = list(solo_prob.keys())
  assert solo_prob[keys[0]] == pytest.approx(0.4999, 1e-3)
  assert solo_prob[keys[1]] == pytest.approx(0.4999, 1e-3)
  solo_prob = result.get_single_qubit_probability(1)
  keys = list(solo_prob.keys())
  assert solo_prob[keys[0]] == pytest.approx(0.7499, 1e-3)
  assert solo_prob[keys[1]] == pytest.approx(0.2499, 1e-3)

def test_n_qubit_probability():
  probs = {"00": 0.0, "10": 0.4999, "01": 0.0, "11": 0.4999}
  circuit = qcs.circuit_init(4)
  circuit.h(0)
  circuit.h(1)
  circuit.x(2)
  circuit.x(3)
  result = circuit.execute()
  slice_probs = result.get_n_qubit_probability(1, 3)
  for key in probs:
    assert slice_probs[key] == pytest.approx(probs[key], 1e-3)

def test_global_config():
  with(pytest.raises(ValueError)):
    qcs.set_global_endian("littleendian")
  with(pytest.raises(ValueError)):
    qcs.set_global_endian(3)
  qcs.set_global_endian("big-endian")
  result_tmp = circuit.execute()
  probs = result_tmp.get_all_probabilities()
  for key in probs:
    assert probs[key] == pytest.approx(prob_table_big_end[key], 1e-3)
  qcs.set_global_endian("little-endian")
  result_tmp = circuit.execute()
  probs = result_tmp.get_all_probabilities()
  for key in probs:
    assert probs[key] == pytest.approx(prob_table_little_end[key], 1e-3)

def test_measure_all():
  circuit = qcs.circuit_init(4)
  circuit.h(2)
  result = circuit.execute()
  strs = result.measure_all()
  assert '0100' in strs
  assert '0000' in strs
  assert '0010' not in strs
  assert '0011' not in strs
  assert '1010' not in strs
  assert '1111' not in strs

# Big-endian tests ----------------------------------------------
qcs.set_global_endian("big-endian")
result_bigend = circuit.execute()

def test_get_single_probability_bigend():
  prob_0 = result_bigend.get_bitstr_probability("00");
  prob_1 = result_bigend.get_bitstr_probability("10");
  prob_2 = result_bigend.get_bitstr_probability("01");
  prob_3 = result_bigend.get_bitstr_probability("11");
  assert prob_0["00"] == pytest.approx(prob_table_big_end["00"], 1e-3)
  assert prob_1["10"] == pytest.approx(prob_table_big_end["10"], 1e-3)
  assert prob_2["01"] == pytest.approx(prob_table_big_end["01"], 1e-3)
  assert prob_3["11"] == pytest.approx(prob_table_big_end["11"], 1e-3)

def test_get_random_probability():
  for i in range(5):
    prob = result_bigend.get_bitstr_probability();
    for key in prob:
      assert prob[key] == pytest.approx(prob_table_big_end[key], 1e-3)

def test_get_all_probability():
  probs = result_bigend.get_all_probabilities()
  for key in probs:
    assert probs[key] == pytest.approx(prob_table_big_end[key], 1e-3)

def test_single_qubit_probability():
  solo_prob = result_bigend.get_single_qubit_probability(0)
  keys = list(solo_prob.keys())
  assert solo_prob[keys[0]] == pytest.approx(0.4999, 1e-3)
  assert solo_prob[keys[1]] == pytest.approx(0.4999, 1e-3)
  solo_prob = result_bigend.get_single_qubit_probability(1)
  keys = list(solo_prob.keys())
  assert solo_prob[keys[0]] == pytest.approx(0.7499, 1e-3)
  assert solo_prob[keys[1]] == pytest.approx(0.2499, 1e-3)

def test_n_qubit_probability():
  probs = {"00": 0.0, "10": 0.4999, "01": 0.0, "11": 0.4999}
  circuit = qcs.circuit_init(4)
  circuit.h(0)
  circuit.h(1)
  circuit.x(2)
  circuit.x(3)
  result_bigend = circuit.execute()
  slice_probs = result_bigend.get_n_qubit_probability(1, 3)
  for key in probs:
    assert slice_probs[key] == pytest.approx(probs[key], 1e-3)
