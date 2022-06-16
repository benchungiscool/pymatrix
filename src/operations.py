#!/usr/bin/env python3

from src.vectors import same_length, add_vectors, scalar_product, n_tuple_product
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
  # matrix dimensions are a = (m * n) where m = len(a) and n = len(a[0])
  # Check that the matrices are of the requisite length
  if not same_length(a[0], b):
    raise Exception

  # define m and k (useful for product matrix)
  m = len(a)
  k = len(b[0])

  # get the required calculations
  # problem with get_ith_row() when m*n ??
  rotatedB = [get_ith_row(b, i) for i in range(m)]
  calculations = []
  for ai in a:
    for bi in rotatedB:
      calculations.append(list(zip(ai, bi)))

  # perform each calculation
  ret = []
  for ci in calculations:
    a = []
    for vals in ci:
      a.append(vals[0] * vals[1])
    ret.append(sum(a))

  # return the new matrix nested k times
  return [ret[i:i + k] for i in range(0, len(ret), k)]
