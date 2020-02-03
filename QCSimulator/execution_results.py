import tensornetwork as tn
import numpy as np
from typing import Union
import itertools

class Execution_result():

  def __init__(self, state_node: tn.Node) -> None:
    self.__state_node = state_node
    #self.__probs_tensor   ...    #calculate all probs in advance?

  def get_state_vector(self) -> np.ndarray:
    return self.__state_node.tensor.flatten('F')

  def get_state_tensor(self) -> np.ndarray:
    return self.__state_node.tensor

  def get_bitstr_probability(self, bitstring: Union[str, list] = None) \
                                                                -> complex:
    if not isinstance(bitstring, (str, list)):
      raise ValueError("The bitstring have to be represented as a string or "
                       "as a list of indexes.")
    demention = len(self.__state_node.tensor.shape)
    if not demention == len(bitstring):
      raise ValueError("The bitstring length have to be exactly equal to "
                       "number of qbits.")

    def _find(demention, bitstring, tensor):
      crnt = tensor
      for i in range(demention):
        crnt = crnt[int(bitstring[i])]
      return crnt * np.conj(crnt)

    if bitstring:
      return _find(demention, bitstring, self.__state_node.tensor)
    else:
      bitstring = np.random.randint(2, size=len(demention))
      return _find(demention, bitstring, self.__state_node.tensor)

  # experemental
  def get_all_probabilities(self) -> np.ndarray:
    demention = len(self.__state_node.tensor.shape)
    probs = ["".join(seq) for seq in itertools.product("01", repeat=demention)]
    prob_results = {}

    for prob in probs:
      prob_results[prob] = self.get_bitstr_probability(prob)
    return prob_results
