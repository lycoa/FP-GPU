from fp_gpu import hello
from pauli_matrices import sigX, sigY, sigZ

print(hello())
print(sigX() @ sigY(), sigZ())  # Task 2c)

def matrix_multiplication(A,B):
    C = A() @ B()
    return C

a = matrix_multiplication(sigX, sigZ)
print(f"Edit Marco: {a}")