import tensornetwork as tn
import numpy as np
import QCSimulator.gate_classes as gates

#class Qbit():
#
#  def __init__(self):
#   self.qbit = tn.Node(np.array([1, 0]))

class Circuit():

  def __init__(self, number_of_qbits):
    self._qbits = []
    self._edges = []
    self._num_of_qbits = number_of_qbits
    #self.crnt_result = None  # current result of the last execution.
    #self.exec_history = []   # stored results for every execution.
    #self.qasm = []           # append qasm notation after every function call.

    for i in range(number_of_qbits):
      qbit = tn.Node(np.array([1.0 + 0j, 0.0 + 0j]))
      self._qbits.append(qbit)
      self._edges.append(qbit[0])

    self.circuit = tn.outer_product_final_nodes(self._qbits, self._edges)

    for i, edge in enumerate(self.circuit):
      self._edges[i] = edge

  def _qbit_init():
    return tn.Node(np.array([1.0 + 0j, 0.0 + 0j]))

  def _check_input(self, *indexes):
    for index in indexes:
      if not isinstance(index, int):
        raise ValueError("Starting from second argument the values have to be "
                         "indexes of circuit qubits")
      if index >= self._num_of_qbits or index < -self._num_of_qbits:
        raise ValueError("Index passed in is out of range. "
                         "Index represents the qbit you are trying to access.")

  def x(self, i):
    self._check_input(i)
    x = gates.X_gate()
    self._edges[i] ^ x.node[0]
    self._edges[i] = x.node[1]

  def y(self, i):
    self._check_input(i)
    y = gates.Y_gate()
    self._edges[i] ^ y.node[0]
    self._edges[i] = y.node[1]

  def z(self, i):
    self._check_input(i)
    z = gates.Z_gate()
    self._edges[i] ^ z.node[0]
    self._edges[i] = z.node[1]

  def h(self, i):
    self._check_input(i)
    h = gates.H_gate()
    self._edges[i] ^ h.node[0]
    self._edges[i] = h.node[1]

  def t(self, i):
    self._check_input(i)
    t = gates.T_gate()
    self._edges[i] ^ t.node[0]
    self._edges[i] = t.node[1]

  def cx(self, a, b):
    self._check_input(a, b)
    cx = gates.CX_gate()
    self._edges[a] ^ cx.node[0]
    self._edges[b] ^ cx.node[1]
    self._edges[a] = cx.node[2]
    self._edges[b] = cx.node[3]

  def cz(self, a, b):
    self._check_input(a, b)
    cz = gates.CZ_gate()
    self._edges[a] ^ cz.node[0]
    self._edges[b] ^ cz.node[1]
    self._edges[a] = cz.node[2]
    self._edges[b] = cz.node[3]

  def cy(self, a, b):
    self._check_input(a, b)
    cy = gates.CY_gate()
    self._edges[a] ^ cy.node[0]
    self._edges[b] ^ cy.node[1]
    self._edges[a] = cy.node[2]
    self._edges[b] = cy.node[3]

  def ch(self, a, b):
    self._check_input(a, b)
    ch = gates.CH_gate()
    self._edges[a] ^ ch.node[0]
    self._edges[b] ^ ch.node[1]
    self._edges[a] = ch.node[2]
    self._edges[b] = ch.node[3]

  def execute(self):
    nodes = tn.reachable(self._edges[0])
    result = tn.contractors.optimal(nodes, self._edges)
    for i in range(len(result.tensor.shape)):
      self._edges[i] = result.get_edge(i)
    return result

  def get_bitstring_probability(self, result, bitstring):
    demention = len(result.tensor.shape)
    if not demention == len(bitstring):
      raise ValueError("The bitstring have to be equal to number of qbits.")
    crnt = result.tensor
    for i in range(demention):
      crnt = crnt[bitstring[i]]
    return (crnt * crnt)


def circuit_init(n_qbit):
  if not isinstance(n_qbit, int):
    raise ValueError("The only parametr circuit_init accsepts is a number "
                     "describing number of qbits on the circuit")
  if n_qbit < 1:
    raise ValueError("The number of qbits have to be a positiv number. (1-20)")
  if n_qbit > 20:
    raise ValueError("The maximum of qbits currently supported is 20")
  return Circuit(n_qbit)
