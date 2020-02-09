import tensornetwork as tn
import numpy as np
from typing import Union
from random import choices
import qcsimulator.config as config
import itertools

# --- ! This class is a mess, need to be refactored !

# --- Store all the probabilities ones to skip useless calculations everytime!

# --- Having all the results stored in specific endian, config,
#     and ability to change endian in each function look like a foot gun!
#     mb concider to remove all the options in functions and just use config.

class Execution_result():

  def __init__(self, state_node: tn.Node) -> None:
    self.__state_node = state_node
    #self._all_probabilities = None   # all probs to not calc them mult times
    #self.__endian = config.little_endian # info about endian
    #self.__probs_tensor   ...    # calculate all probs as a tensor?

  #@property
  #def endian(self):
  #  return self.__endian

  def get_state_vector(self) -> np.ndarray:
    return self.__state_node.tensor.flatten('F')

  def get_state_tensor(self) -> np.ndarray:
    return self.__state_node.tensor

  def get_bitstr_probability(self, bitstring: Union[str, list] = None, \
                                          little_endian: bool = None) -> dict:
    if little_endian == None:
      little_endian = config.little_endian
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

    if isinstance(bitstring, list):
      bitstring_key = ''.join(str(i) for i in bitstring)
    else:
      bitstring_key = bitstring

    if little_endian:
      bitstring = bitstring[::-1]
    crnt = self.__state_node.tensor
    for i in range(demention):
      crnt = crnt[int(bitstring[i])]
    return {bitstring_key: (crnt * np.conj(crnt)).real}

  def get_all_probabilities(self, little_endian: bool = None) -> list:
    if little_endian == None:
      little_endian = config.little_endian
    #if self._all_probabilities != None:
    #  return self.__all_probabilities

    demention = len(self.__state_node.tensor.shape)
    strs = ["".join(seq) for seq in itertools.product("01", repeat=demention)]
    prob_result = []
    for string in strs:
      prob_result.append(self.get_bitstr_probability(string, little_endian))
    #self._all_probabilities = prob_result
    #return self._all_probabilities
    return prob_result

  def get_single_qubit_probability(self, n_qubit: int, \
                                          little_endian: bool = None) -> list:
    if little_endian == None:
      little_endian = config.little_endian
    if not isinstance(n_qubit, int):
      raise ValueError("pass the particular qubit index")
    bitstr_len = len(self.__state_node.tensor.shape)
    if n_qubit >= bitstr_len or n_qubit < -1 * bitstr_len:
      raise ValueError("index is out of range")

    prob_for_0 = []
    prob_for_1 = []
    all_probs = self.get_all_probabilities()

    for prob in all_probs:
      for key in prob:
        if little_endian:
          qubit = key[::-1][n_qubit]
        if qubit == "0":
          prob_for_0.append(prob[key])
        else:
          prob_for_1.append(prob[key])
    return {"0": sum(prob_for_0), "1": sum(prob_for_1)}


# --- something more interesting to return instead of dictionaries ?
#     class Probability(dict):
#
#       def __init__():
#
#       def __str__():
