# Quantum Circuit Simulator

#### A high-level library for building quantum circuits. Calculations based on [TensorNetwork](https://github.com/google/TensorNetwork) library. 
#### Version 0.1.0

### Instalation

```bash
$> git clone https://github.com/katolikyan/QCSimulator.git
$> pip3 install QCSimulator/
```

### Usage 
[**Basic QCSimulator API tutorial**](https://colab.research.google.com/drive/12jgkrVgxTZbmyJRl114j_J5ePNu2W9ey?usp=sharing)

> The detailed documentation for the library is comming soon.

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
### Available gates in this build:
* `i`  — Identity gate.
* `x` — Pauli-X (NOT) gate.
* `y` — Pauli-Y gate
* `z` — Pauli-Z gate
* `h` — H (Hadamard) gate
* `t` — T gate
* `ci` — control-identity. *(just a connection of 2 qubits)*
* `cx` — CNOT gate
* `cz` — CZ gate
* `cy` — CY gate
* `ch` — CH gate
* `rx` — rotation through angle θ (radians) around the x-axis
* `ry` — rotation through angle θ (radians) around the y-axis
* `rz` — rotation through angle θ (radians) around the z-axis 
* `rot` — Phase rotaion through angle θ (radians) gate 
* `swap` — SWAP gate swaps the state of the two qubits 
* `crot` — controlled phase shift with angle θ (radians)


### Available auto-builder functions:
* `cirquit.qft()`
* `cirquit.qft_rev()` 

Check out colab explaining the QFT functions:  
[**QFT Tutorial**](https://colab.research.google.com/drive/1gknkMQ_SJGFRyMLqZ82w6Tb2sJpujCCS?usp=sharing)

### Getting some data after execution
All the probabilities are returned in little-endian by default. 
To swap to big endian just call 
```python
qcs.set_global_endian("big-endian")
```
*I recommend to work on little end only*

```python
# Executing the circuit returns a class that contains all the data we need.
result = circuit.execute()

result.get_state_vector() # returns state vector
result.get_state_tensor() # returns state tensor

#returns all possible bitstring probabilities
result.get_all_probabilities() 

# returns specific bitstring probability
result.get_bitstr_probability("10")
# if the bitstr function doesn't recive a bitstring -> random bitstring probability is returned
result.get_bitstr_probability() # returns rundom bitstring probability.
```
### There are more functionality in the lib. 
You can find some examples in the `examples` folder or check out the colab versions:
* [**Basic QCSimulator API tutorial**](https://colab.research.google.com/drive/12jgkrVgxTZbmyJRl114j_J5ePNu2W9ey?usp=sharing)
* [**Deutsch's algorithm**](https://colab.research.google.com/drive/1cedqh4uTv6Qr_DJ48wA7KpwRgt29_hcq?usp=sharing)
* [**QFT Tutorial**](https://colab.research.google.com/drive/1gknkMQ_SJGFRyMLqZ82w6Tb2sJpujCCS?usp=sharing)
* [**QAOA**](https://colab.research.google.com/drive/150-AAp2wv7bMIW7WgPg7fOuVVv_hiUaT?usp=sharing)

---
Do not hesitate to open an issue, contribute, leave feedback, or criticize.\
Thank you!
