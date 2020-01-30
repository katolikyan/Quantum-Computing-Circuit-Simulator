import tensornetwork as tn
import numpy as np

class Qbit():

  def __init__(self):
   self.qbit = tn.Node(np.array([1, 0]))


class Circuit():

  def __init__(self, number_of_qbits):
    self.qbits = []
    self.edges = []
    self.usage = []
    for i in range(number_of_qbits):
   #   qbit = Qbit()
      qbit = tn.Node(np.array([1.0 + 0j, 0.0 + 0j]))
      self.qbits.append(qbit)
      self.edges.append(qbit[0])
      self.usage.append(False)

#
#    self.qbits = {}
#    for i in range(number_of_qbits):
#        self.qbits[0] = []
#        qbit = Qbit()
#        self.qbits[0].append(qbit)
#        self.qbits[0].append(qbit[0])
#        self.qbits[0].append(False)

def circuit_init(n_qbit):
  if not isinstance(n_qbit, int):
    raise ValueError("The only parametr circuit_init accsepts is a number "
                         "describing number of qbits on the circuit")
  return Circuit(n_qbit)
