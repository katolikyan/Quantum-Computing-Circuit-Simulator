import qcsimulator as qcs
import numpy as np
import tensornetwork as tn
import pytest
from qiskit import QuantumRegister, QuantumCircuit, execute, Aer
import random
from inspect import signature

n_of_circuits_generated = 100
n_of_gates_per_circuit = 15

def test_random_circuit_generator_qiskit_comparison():
  gates_c = ["circuit.i({})", "circuit.x({})", "circuit.y({})", \
             "circuit.z({})", "circuit.h({})", "circuit.t({})", \
             "circuit.cx({}, {})", "circuit.cy({}, {})", \
             "circuit.cz({}, {})", "circuit.ch({}, {})"]
  gates_qkit = ["qubit.iden(q_reg[{}])", "qubit.x(q_reg[{}])", \
                "qubit.y(q_reg[{}])", "qubit.z(q_reg[{}])", \
                "qubit.h(q_reg[{}])", "qubit.t(q_reg[{}])", \
                "qubit.cx(q_reg[{}], q_reg[{}])", \
                "qubit.cy(q_reg[{}], q_reg[{}])", \
                "qubit.cz(q_reg[{}], q_reg[{}])", \
                "qubit.ch(q_reg[{}], q_reg[{}])"]
  gate_n_params = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2]
  func_len = len(gates_c)
  S_simulator = Aer.backends(name='statevector_simulator')[0]
  #errors = 0

  # number of circuits generated
  for _ in range(n_of_circuits_generated):
    n_qbit = random.randrange(2, 21)
    circuit = qcs.circuit_init(n_qbit)
    q_reg = QuantumRegister(n_qbit)
    qubit = QuantumCircuit(q_reg)

    # number of gates on circuit
    for _ in range(n_of_gates_per_circuit):
      q = random.randrange(0, n_qbit - 1)
      gate_choice = random.randrange(0, func_len)
      my_gate = gates_c[gate_choice]
      qiskit_gate = gates_qkit[gate_choice]
      params = gate_n_params[gate_choice]

      # single gate
      if (params == 1):
        exec(my_gate.format(q))
        exec(qiskit_gate.format(q))

      # controlled gate
      else:
        side = random.choice(["up", "down"])
        if (q == n_qbit - 1):
          q = q - 1
        if side == "up":
          exec(my_gate.format(q, q + 1))
          exec(qiskit_gate.format(q, q + 1))
        if side == "down":
          exec(my_gate.format(q + 1, q))
          exec(qiskit_gate.format(q + 1, q))

    result = circuit.execute()
    sv = result.get_state_vector()
    job = execute(qubit, S_simulator)
    result_qkit = job.result()
    sv_qkit = result_qkit.get_statevector()

    assert np.testing.assert_allclose(sv, sv_qkit, atol=1e-8, rtol=1e-8) \
                                                                      == None

    #if np.testing.assert_allclose(sv, sv_qkit, atol=1e-8, rtol=1e-8) != None:
    #  errors += 1
    #print("\n\n -------- TOTAL ERRRORS:\n Number of circuits: {}\n Fails: "
    #      "{}".format(n_of_circuits_generated, errors), end='\r', flush=True)

#test_random_circuit_generator_qiskit_comparison()
