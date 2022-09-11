from m4cs.matrix_inversion import *
from tests.helper import *

# declare a matrix
a = [
    [1, 24, 51],
    [-3, 22, 42],
    [6, 32, -100]
  ]
print_matrix(a, "Matrix a =")

# print the inverse of the matrix
print_matrix(inverse_matrix(a), "Inverse of a =")

# perform a matrix multiplication and producce the output
b = [
    [5, 12, 12],
    [64, -64, 22],
    [53, 21, 22]
  ]
print_matrix(b, "Matrix b =")
print_matrix(matrix_multiplication(a, b), "a * b =")


