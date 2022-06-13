#!/usr/bin/env python3

from src.vectors import same_length, add_vectors, scalar_product
from src.properties import get_ith_row, get_jth_column

# the same length function in three dimensions
def same_dimensions(a, b):
  return same_length(a, b) and same_length(a[0], b[0])

# perform matrix addition
def matrix_addition(a, b):
  if not same_dimensions(a, b):
    raise Exception
  c = []
  for i, j in zip(a, b):
    c.append(add_vectors(i, j))
  return c

# multiply a matrix by a scalar
def matrix_scalar_product(a, scalar):
  c = []
  for vector in a:
    c.append([element * scalar for element in vector])
  return c

# matrix multiplication
def matrix_multiplication(a, b):
  # Check that the matrices are of the requisite length
  if len(get_jth_column(a, 0)) != len(get_ith_row(b, 0)):
    raise Exception

  ret = []

  return ret
