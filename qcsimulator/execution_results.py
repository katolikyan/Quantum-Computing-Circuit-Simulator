import tensornetwork as tn
import numpy as np
from typing import Union
from random import choices
import qcsimulator.config as config
import itertools

class Execution_result():

  def __init__(self, state_node: tn.Node, probs_autocalc: bool = True) -> None:
    self.__state_node = state_node
    self._little_endian = config.little_endian
    self._demention = len(self.__state_node.tensor.shape)
    self._all_probs = None
    if probs_autocalc:
      self._all_probs = self._calc_all_probabilities()

  def _calc_all_probabilities(self) -> dict:
    strs = ["".join(seq) for seq in \
            itertools.product("01", repeat=self._demention)]
    all_probs = {}
    for bitstring in strs:
      bitstring_key = bitstring
      if self._little_endian:
        bitstring = bitstring[::-1]
      crnt = self.__state_node.tensor
      for i in range(self._demention):
        crnt = crnt[int(bitstring[i])]
      prob = (crnt * np.conj(crnt)).real
      all_probs[bitstring_key] = prob
    return all_probs

  def calculate_probabilities():
      self._all_probs = self._calc_all_probabilities()

  def get_state_vector(self) -> np.ndarray:
    return self.__state_node.tensor.flatten('F')

  def get_state_tensor(self) -> np.ndarray:
    return self.__state_node.tensor

  def get_all_probabilities(self) -> dict:
    if not self._all_probs:
      raise ValueError("autocalc was disabled, need to calculate probs first.")
    return self._all_probs

  def get_bitstr_probability(self, bitstring: str = None) -> dict:
    if not self._all_probs:
      raise ValueError("autocalc was disabled, need to calculate probs first.")
    if bitstring:
      if not isinstance(bitstring, str):
        raise TypeError("bitstring parameter have to be a string.")
      if self._demention != len(bitstring):
        raise ValueError("Number of indecies in bitstring have to be equal to "
                         "the number of qbits.")
      if any((not char in "01") for char in bitstring):
        raise ValueError("bitstring have to contain only with 0 and 1 chars. ")
    else:
      bitstring = ''.join(choices("10", k=self._demention))
    return {bitstring: self._all_probs[bitstring]}

  def get_single_qubit_probability(self, n_qubit: int) -> list:
    if not self._all_probs:
      raise ValueError("Autocalc was disabled, need to calculate probs first.")
    if not isinstance(n_qubit, int):
      raise TypeError("n_qubit have to be an integer and valid qubit index")
    if n_qubit >= self._demention or n_qubit < -1 * self._demention:
      raise IndexError("index is out of range")
    prob_for_0 = 0
    prob_for_1 = 0
    for bitstr in self._all_probs:
      qubit = bitstr[::-1][n_qubit] if self._little_endian else bitstr[n_qubit]
      if qubit == "0":
        prob_for_0 += self._all_probs[bitstr]
      else:
        prob_for_1 += self._all_probs[bitstr]
    return {"0": prob_for_0, "1": prob_for_1}

  def get_n_qubit_probability(self, start: int, stop: int) -> list:
    if not self._all_probs:
      raise ValueError("autocalc was disabled, need to calculate probs first.")
    if start < 0 or stop < 0:
      raise IndexError("Currently get_n_qubit_probability accepts only "
                       "positive indecies.")
    if start > self._demention or stop > self._demention:
      raise IndexError("start or stop value is out of range.")

    count = stop - start
    bitstrings = ["".join(seq) for seq in \
                  itertools.product("01", repeat=count)]
    all_probs = self.get_all_probabilities()
    n = self._demention
    slice_probs = {}
    for bitstring in bitstrings:
      slice_probs[bitstring] = 0
    for bitstring in all_probs:
      if self._little_endian:
        slice_probs[bitstring[n - stop:n - start]] += all_probs[bitstring]
      else:
        slice_probs[bitstring[start:stop]] += all_probs[bitstring]
    return slice_probs

#  def __str__(self):
#    print("qcsimulator.execution_results.Execution_result object")
#    if self._little_endian:
#      print("Probabilities are in little endian")
#    else:
#      print("Probabilities are in big endian")
#    print("State tensor info:")
#    print(self.__state_node)


# --- something more interesting to return instead of dictionaries ?
#     class Probability(dict):
#
#       def __init__():
#
#       def __str__():
