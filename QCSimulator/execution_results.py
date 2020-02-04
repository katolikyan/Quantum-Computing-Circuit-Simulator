import tensornetwork as tn
import numpy as np
from typing import Union
from random import choices
import itertools

class Execution_result():

  def __init__(self, state_node: tn.Node) -> None:
    self.__state_node = state_node
    #self.__probs_tensor   ...    #calculate all probs in advance?

  def get_state_vector(self) -> np.ndarray:
    return self.__state_node.tensor.flatten('F')

  def get_state_tensor(self) -> np.ndarray:
    return self.__state_node.tensor

  def get_bitstr_probability(self, bitstring: Union[str, list] = None, \
                             little_endian: bool = False) -> dict:
    demention = len(self.__state_node.tensor.shape)
    if bitstring:
      if not isinstance(bitstring, (str, list)):
        raise ValueError("The bitstring have to be represented as a string or "
                        "as a list of indexes.")
    else:
      bitstring = ''.join(choices("10", k=demention))
    if demention != len(bitstring):
      raise ValueError("The bitstring length have to be exactly equal to "
                       "number of qbits.")
    if not isinstance(little_endian, bool):
      raise  ValueError("The little_endian parametr is a bool.")

    bitstring_key = bitstring
    if little_endian:
      bitstring = bitstring[::-1]
    crnt = self.__state_node.tensor
    for i in range(demention):
      crnt = crnt[int(bitstring[i])]
    return {bitstring_key: (crnt * np.conj(crnt)).real}

#    def _find(demention, bitstring, tensor):
#      crnt = tensor
#      for i in range(demention):
#        crnt = crnt[int(bitstring[i])]
#      return {bitstring: (crnt * np.conj(crnt)).real}
#
#    if little_endian:
#      bitstring = bitstring[::-1]
#    return _find(demention, bitstring, self.__state_node.tensor)
#
  def get_all_probabilities(self, little_endian: bool = False) -> list:
    demention = len(self.__state_node.tensor.shape)
    strs = ["".join(seq) for seq in itertools.product("01", repeat=demention)]
    prob_result = []

    for string in strs:
      prob_result.append(self.get_bitstr_probability(string, little_endian))
    return prob_result

# something to return instead of dictionaries ?
#class Probability():
#
#  def __init__():
#
#  def __str__():
