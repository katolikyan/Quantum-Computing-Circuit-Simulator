import tensornetwork as tn
import numpy as np

#class Qbit():
#
#  def __init__(self):
#   self.qbit = tn.Node(np.array([1, 0]))

class Circuit():

  def __init__(self, number_of_qbits):
    self._qbits = []
    self._edges = []
    self._n_qbits = number_of_qbits

    for i in range(number_of_qbits):
      qbit = tn.Node(np.array([1.0 + 0j, 0.0 + 0j]))
      self._qbits.append(qbit)
      self._edges.append(qbit[0])

    self.circuit = tn.outer_product_final_nodes(self._qbits, self._edges)

    for i, edge in enumerate(self.circuit):
      self._edges[i] = edge

  def _qbit_init():
    return tn.Node(np.array([1.0 + 0j, 0.0 + 0j]))




def circuit_init(n_qbit):
  if not isinstance(n_qbit, int):
    raise ValueError("The only parametr circuit_init accsepts is a number "
                         "describing number of qbits on the circuit")
  return Circuit(n_qbit)
