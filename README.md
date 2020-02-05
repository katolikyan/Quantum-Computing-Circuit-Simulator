# Quantum Circuit Simulator

#### A high-level library for building quantum circuits. Calculations based on [TensorNetwork](https://github.com/google/TensorNetwork) library.
#### Work in progress. Version 0.1.0

### Instalation

```bash
$> git clone https://github.com/katolikyan/QCSimulator.git
$> pip3 install QCSimulator/
```

### Usage 
[Basic QCSimulator API tutorial](https://colab.research.google.com/drive/1T0vml0bgntL4Wlog3c_28DKCZQ1FSPiV)

> There is no documentation for the library yet. Sorry.

### Very first basic circuit
```python
import qcsimulator as qcs

# Circuit initialization:
circuit = qcs.circuit_init(2)
# Applying some gates:
circuit.h(0)
circuit.cx(0, 1)
# Getting the execution result:
result = circuit.execute()
# Getting the state vector
sv = result.get_state_vector()
# Printing Probabilities (in big-endian):
print(result.get_all_probabilities())

```
Supported gates:
* `I` - Identity
* `X`- X gate
* `Y`- Y gate
* `Z`- Z gate
* `T` - T gate
* `H` - Hadamart gate
* `CX` - Control X gate (CNOT)
* `CH` - Control Hadamart gate
* `CY` - Control Y gate
* `CZ` - Control Z gate
* `CI` - Identity matrix (2 node connection)

### Getting data after execution
All the probabilities are returned in big-endian by default. \
To change that pass `little_endian=True` parameter into probability methods.
 
```python
result.get_state_vector() # returns state vector
result.get_state_tensor() # returns state tensor

#returns all possible bitstring probabilities
result.get_all_probabilities(little_endian=True) 

# returns specific bitstring probability
result.get_bitstr_probability("10", little_endian=True)
# if the bitstr function doesn't recive a bitstring -> random bitstring probability is returned
result.get_bitstr_probability(little_endian=True) # returns rundom bitstring probability.
```
