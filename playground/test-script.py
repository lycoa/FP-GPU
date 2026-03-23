from fp_gpu import hello
from pauli_matrices import sigX, sigY, sigZ

print(hello())
print(sigX() @ sigY(), sigZ())  # Task 2c)

a = sigZ @ sigX

print(f"Marcos edit {a}")