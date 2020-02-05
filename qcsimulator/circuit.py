import tensornetwork as tn
import numpy as np
import qcsimulator.gate_classes as gates
from qcsimulator.execution_results import Execution_result

class Circuit():

  def __init__(self, number_of_qbits: int) -> None:
    self._qbits = []
    self._edges = []
    self._num_of_qbits = number_of_qbits
    #self.crnt_result = None  # current result of the last execution.
    #self.exec_history = []   # stored results for every execution.
    #self.qasm = []           # append qasm notation after every method call.

    for i in range(number_of_qbits):
      qbit = self._qbit_init()
      self._qbits.append(qbit)
      self._edges.append(qbit[0])

    # --- Outer product connecction onprion.
    #self.circuit = tn.outer_product_final_nodes(self._qbits, self._edges)
    #for i, edge in enumerate(self.circuit):
    #  self._edges[i] = edge

    # --- Controlled identity connecction at the begining oprioon.
    #for i in range(len(self._edges) - 1):
    #  self.ci(i, i + 1)

  def _qbit_init(self):
    return tn.Node(np.array([1.0 + 0j, 0.0 + 0j]))

  def _check_input(self, *indexes):
    distinct = []
    for index in indexes:
      if not isinstance(index, int):
        raise ValueError("The values have to be indexes of "
                         "the circuit's qubits.")
      if index >= self._num_of_qbits or index < -self._num_of_qbits:
        raise ValueError("Index passed in is out of range. "
                         "Index represents the qbit you are trying to access.")
      if index not in distinct:
        distinct.append(index)
      else:
        raise ValueError("Indexes of qbits have to be distinct numbers. "
                         "It helps to prevent usless extra  calculations.")

  def i(self, a: int) -> None:
    self._check_input(a)
    i_gate = gates.I_gate()
    self._edges[a] ^ i_gate.node[0]
    self._edges[a] = i_gate.node[1]

  def x(self, i: int) -> None:
    self._check_input(i)
    x = gates.X_gate()
    self._edges[i] ^ x.node[0]
    self._edges[i] = x.node[1]

  def y(self, i: int) -> None:
    self._check_input(i)
    y = gates.Y_gate()
    self._edges[i] ^ y.node[0]
    self._edges[i] = y.node[1]

  def z(self, i: int) -> None:
    self._check_input(i)
    z = gates.Z_gate()
    self._edges[i] ^ z.node[0]
    self._edges[i] = z.node[1]

  def h(self, i: int) -> None:
    self._check_input(i)
    h = gates.H_gate()
    self._edges[i] ^ h.node[0]
    self._edges[i] = h.node[1]

  def t(self, i: int) -> None:
    self._check_input(i)
    t = gates.T_gate()
    self._edges[i] ^ t.node[0]
    self._edges[i] = t.node[1]

  def ci(self, a: int, b: int) -> None:
    self._check_input(a, b)
    ci = gates.CI_gate()
    self._edges[a] ^ ci.node[0]
    self._edges[b] ^ ci.node[1]
    self._edges[a] = ci.node[2]
    self._edges[b] = ci.node[3]

  def cx(self, a: int, b: int) -> None:
    self._check_input(a, b)
    cx = gates.CX_gate()
    self._edges[a] ^ cx.node[0]
    self._edges[b] ^ cx.node[1]
    self._edges[a] = cx.node[2]
    self._edges[b] = cx.node[3]

  def cz(self, a: int, b: int) -> None:
    self._check_input(a, b)
    cz = gates.CZ_gate()
    self._edges[a] ^ cz.node[0]
    self._edges[b] ^ cz.node[1]
    self._edges[a] = cz.node[2]
    self._edges[b] = cz.node[3]

  def cy(self, a: int, b: int) -> None:
    self._check_input(a, b)
    cy = gates.CY_gate()
    self._edges[a] ^ cy.node[0]
    self._edges[b] ^ cy.node[1]
    self._edges[a] = cy.node[2]
    self._edges[b] = cy.node[3]

  def ch(self, a: int, b: int) -> None:
    self._check_input(a, b)
    ch = gates.CH_gate()
    self._edges[a] ^ ch.node[0]
    self._edges[b] ^ ch.node[1]
    self._edges[a] = ch.node[2]
    self._edges[b] = ch.node[3]

  def execute(self) -> Execution_result:
    for i in range(len(self._edges) - 1):
      self.ci(i, i + 1)

    nodes = tn.reachable(self._edges[0])
    result_node = tn.contractors.greedy(nodes, self._edges)
    result = Execution_result(result_node)
    for i in range(len(result_node.tensor.shape)):
      self._edges[i] = result_node.get_edge(i)
    return result


def circuit_init(n_qbit: int) -> Circuit:
  if not isinstance(n_qbit, int):
    raise ValueError("The only parametr circuit_init accsepts is a number "
                     "describing number of qbits on the circuit")
  if n_qbit < 1:
    raise ValueError("The number of qbits have to be a positiv number. (1-20)")
  if n_qbit > 20:
    raise ValueError("The maximum of qbits currently supported is 20")
  return Circuit(n_qbit)
