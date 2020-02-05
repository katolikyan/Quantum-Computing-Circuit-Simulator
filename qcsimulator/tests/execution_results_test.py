import qcsimulator as qcs
import numpy as np
import tensornetwork as tn
import pytest
from qiskit import QuantumRegister, QuantumCircuit, execute, Aer

prob_table = {"00": 0.4999, "10": 0.24999, "01": 0.0, "11": 0.24999}
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

  assert prob_0["00"] == pytest.approx(prob_table["00"], 1e-3)
  assert prob_1["10"] == pytest.approx(prob_table["10"], 1e-3)
  assert prob_2["01"] == pytest.approx(prob_table["01"], 1e-3)
  assert prob_3["11"] == pytest.approx(prob_table["11"], 1e-3)

def test_bitstring_as_a_list_test():
  prob_0 = result.get_bitstr_probability([0, 0]);
  prob_2 = result.get_bitstr_probability([0, 1]);

  assert prob_0["00"] == pytest.approx(prob_table["00"], 1e-3)
  assert prob_2["01"] == pytest.approx(prob_table["01"], 1e-3)

def test_get_single_little_endian_probability():
  prob_0 = result.get_bitstr_probability("00", little_endian=True);
  prob_1 = result.get_bitstr_probability("10", little_endian=True);
  prob_2 = result.get_bitstr_probability("01", little_endian=True);
  prob_3 = result.get_bitstr_probability("11", little_endian=True);

  assert prob_0["00"] == pytest.approx(prob_table_little_end["00"], 1e-3)
  assert prob_1["10"] == pytest.approx(prob_table_little_end["10"], 1e-3)
  assert prob_2["01"] == pytest.approx(prob_table_little_end["01"], 1e-3)
  assert prob_3["11"] == pytest.approx(prob_table_little_end["11"], 1e-3)

def test_get_random_probability():
  for i in range(5):
    prob = result.get_bitstr_probability();
    for key in prob:
      assert prob[key] == pytest.approx(prob_table[key], 1e-3)

  for i in range(5):
    prob = result.get_bitstr_probability(little_endian=True);
    for key in prob:
      assert prob[key] == pytest.approx(prob_table_little_end[key], 1e-3)

def test_get_all_probability():
  probs = result.get_all_probabilities()
  probs_end = result.get_all_probabilities(little_endian=True)

  for oneprob in probs:
    for key in oneprob:
      assert oneprob[key] == pytest.approx(prob_table[key], 1e-3)

  for oneprob in probs_end:
    for key in oneprob:
      assert oneprob[key] == pytest.approx(prob_table_little_end[key], 1e-3)
