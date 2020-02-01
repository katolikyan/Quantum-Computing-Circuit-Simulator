import tensornetwork as tn
import numpy as np

class CX_gate():

  def __init__(self):
    gate_op = np.array([[1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 0, 1],
                        [0, 0, 1, 0]]).reshape(2, 2, 2, 2)
    self.node = tn.Node(gate_op)

class X_gate():

  def __init__(self):
    gate_op = np.array([[0, 1],
                        [1, 0]])
    self.node = tn.Node(gate_op)

class Y_gate():

  def __init__(self):
    gate_op = np.array([[0, 0 - 1j],
                        [0 + 1j, 0]])
    self.node = tn.Node(gate_op)

class Z_gate():

  def __init__(self):
    gate_op = np.array([[1, 0],
                        [0,-1]])
    self.node = tn.Node(gate_op)

class H_gate():

  def __init__(self):
    gate_op = np.array([[1, 1],
                        [1,-1]]) / np.sqrt(2)
    self.node = tn.Node(gate_op)

class T_gate():

  def __init__(self):
    gate_op = np.array([[1, 0],
                        [0, np.exp(1j * np.pi / 4)]])
    self.node = tn.Node(gate_op)

class CZ_gate():

  def __init__(self):
    gate_op = np.array([[1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0,-1]]).reshape(2, 2, 2, 2)
    self.node = tn.Node(gate_op)

class CY_gate():

  def __init__(self):
    gate_op = np.array([[1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 0, 0 - 1j],
                        [0, 0, 0 + 1j, 0]]).reshape(2, 2, 2, 2)
    self.node = tn.Node(gate_op)


class CH_gate():

  def __init__(self):
    gate_op = np.array([[1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 1 / np.sqrt(2),  1 / np.sqrt(2)],
                        [0, 0, 1 / np.sqrt(2), -1 / np.sqrt(2)]]).\
                        reshape(2, 2, 2, 2)
    self.node = tn.Node(gate_op)
