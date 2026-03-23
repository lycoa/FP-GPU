from fp_gpu import hello
from pauli_matrices import sigX, sigY, sigZ

print(hello())

print(sigX()@sigY()) # Task 2c)
