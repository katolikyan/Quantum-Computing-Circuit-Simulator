import qcsimulator as qcs
import numpy as np
import tensornetwork as tn
import pytest
from qiskit import QuantumRegister, QuantumCircuit, execute, Aer

prob_table_big_end = {"00": 0.4999, "10": 0.24999, "01": 0.0, "11": 0.24999}
prob_table_little_end = {"00": 0.4999, "10": 0.0, "01": 0.24999, "11": 0.24999}
circuit = qcs.circuit_init(2)
circuit.h(0)
circuit.ch(0, 1)
result = circuit.execute()

def test_get_single_probability():
  prob_0 = result.get_bitstr_probability("00");
  prob_1 = result.get_bitstr_probability("10");
  prob_2 = result.get_bitstr_probability("01");
  prob_3 = result.get_bitstr_probability("11");

  assert prob_0["00"] == pytest.approx(prob_table_little_end["00"], 1e-3)
  assert prob_1["10"] == pytest.approx(prob_table_little_end["10"], 1e-3)
  assert prob_2["01"] == pytest.approx(prob_table_little_end["01"], 1e-3)
  assert prob_3["11"] == pytest.approx(prob_table_little_end["11"], 1e-3)

def test_bitstring_as_a_list_test():
  prob_0 = result.get_bitstr_probability([0, 0]);
  prob_2 = result.get_bitstr_probability([0, 1]);

  assert prob_0["00"] == pytest.approx(prob_table_little_end["00"], 1e-3)
  assert prob_2["01"] == pytest.approx(prob_table_little_end["01"], 1e-3)

def test_get_single_big_endian_probability():
  prob_0 = result.get_bitstr_probability("00", little_endian=False);
  prob_1 = result.get_bitstr_probability("10", little_endian=False);
  prob_2 = result.get_bitstr_probability("01", little_endian=False);
  prob_3 = result.get_bitstr_probability("11", little_endian=False);

  assert prob_0["00"] == pytest.approx(prob_table_big_end["00"], 1e-3)
  assert prob_1["10"] == pytest.approx(prob_table_big_end["10"], 1e-3)
  assert prob_2["01"] == pytest.approx(prob_table_big_end["01"], 1e-3)
  assert prob_3["11"] == pytest.approx(prob_table_big_end["11"], 1e-3)

def test_get_random_probability():
  for i in range(5):
    prob = result.get_bitstr_probability();
    for key in prob:
      assert prob[key] == pytest.approx(prob_table_little_end[key], 1e-3)

  for i in range(5):
    prob = result.get_bitstr_probability(little_endian=False);
    for key in prob:
      assert prob[key] == pytest.approx(prob_table_big_end[key], 1e-3)

def test_get_all_probability():
  probs = result.get_all_probabilities()
  for oneprob in probs:
    for key in oneprob:
      assert oneprob[key] == pytest.approx(prob_table_little_end[key], 1e-3)

  probs_big_end = result.get_all_probabilities(little_endian=False)
  for oneprob in probs_big_end:
    for key in oneprob:
      assert oneprob[key] == pytest.approx(prob_table_big_end[key], 1e-3)

def test_global_config():
  qcs.set_global_endian("big-endian")
  probs = result.get_all_probabilities()
  for oneprob in probs:
    for key in oneprob:
      assert oneprob[key] == pytest.approx(prob_table_big_end[key], 1e-3)

  qcs.set_global_endian("little-endian")
  probs = result.get_all_probabilities()
  for oneprob in probs:
    for key in oneprob:
      assert oneprob[key] == pytest.approx(prob_table_little_end[key], 1e-3)

  with(pytest.raises(ValueError)):
    qcs.set_global_endian("littleendian")
  with(pytest.raises(ValueError)):
    qcs.set_global_endian(3)

def test_single_qubit_probability():
  solo_prob = result.get_single_qubit_probability(0)
  keys = list(solo_prob.keys())
  assert solo_prob[keys[0]] == pytest.approx(0.4999, 1e-3)
  assert solo_prob[keys[1]] == pytest.approx(0.4999, 1e-3)

  solo_prob = result.get_single_qubit_probability(1)
  keys = list(solo_prob.keys())
  assert solo_prob[keys[0]] == pytest.approx(0.7499, 1e-3)
  assert solo_prob[keys[1]] == pytest.approx(0.2499, 1e-3)


#   
#   print(result.get_all_probabilities())
#   print(qcs.config.little_endian)
#   
#   qcs.set_global_endian("big-endian")
#   print(result.get_all_probabilities())
#   print(qcs.config.little_endian)
#   circuit = qcs.circuit_init(2)
#   circuit.h(0)
#   circuit.ch(0, 1)
#   result = circuit.execute()
#   print(result.get_all_probabilities())
#print(result.get_single_qubit_probability(0))
