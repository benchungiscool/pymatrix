#!/usr/bin/env python3

from src.vectors import same_length, add_vectors, scalar_product, n_tuple_product
from src.properties import get_ith_row, get_jth_column
from tests.helper import *
from copy import deepcopy

# the same length function in two dimensions
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

# returns the identity matrix of a given size m
def identity_matrix(m):
  # make an mxm matrix of zeroes
  ret = [[0] * m] * m
  # make each item of the diagonal zero
  for i, row in enumerate(ret):
    print(row[i])
  return ret

# returns the A^T of A
def matrix_transpose(a):
  # special case if a is one row
  m, n = dimensions(a)
  if m == 1:
    return [[a[0][i]] for i in range(len(a[0]))]

  # otherwise return each column of the matrix
  a = deepcopy(a)
  return [get_ith_row(a, i) for i in range(len(a))]

# matrix multiplication
def matrix_multiplication(a, b):
 # matrix dimensions are a = (m * n) where m = len(a) and n = len(a[0])
  if not same_length(a[0], b):
    raise Exception("Wrong dimensions")

  # define m and k (useful for product matrix)
  m = len(a)
  k = len(b[0])

  # get the required calculations
  rotatedB = matrix_transpose(b)
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

# returns the dimensions in form (m, n)
def dimensions(a):
  if not a:
    return (0, 0)
  return (len(a), len(a[0]))

# find the determinant of a 2*2 matrix (used to find the determinant of larger matrices)
def m2_determinant(a):
  # ensure matrix is m*m
  if dimensions(a) != (2, 2):
    raise Exception

  # define each matrix value
  ad = a[0][0] * a[1][1]
  bc = a[0][1] * a[1][0]

  # return the formula for a 2*2 matrix
  return ad - bc

def m3_determinant(m):
  if dimensions(m) != (3, 3):
    raise Exception

  # give each value of matrix a variable name
  a, b, c = m[0]
  d, e, f = m[1]
  g, h, i = m[2]

  # return the formula
  return a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)

def determinant(A, total=0):
    if not same_length(A[0], A):
      raise Exception("m != n")

    if dimensions(A) == (1, 1):
      return A[0]

    if dimensions(A) == (2, 2):
      return m2_determinant(A)

    if dimensions(A) == (3, 3):
      return m3_determinant(A)

    indices = list(range(len(A)))
    for fc in indices: 
      As = deepcopy(A)
      As = As[1:]
      height = len(As)
      for i in range(height):
        As[i] = As[i][0:fc] + As[i][fc+1:]
      sign = (-1) ** (fc % 2) # F)
      sub_det = determinant(As)
      total += sign * A[0][fc] * sub_det

    return total

# returns true if a row is the weighted product of preceding rows
def linear_combination(a, index):
  weighted_product = [0 for i in range(len(a[0]))]
  for i, row in enumerate(a[:index]):
    weighted_product = add_vectors(scalar_product(row, i+1), weighted_product)
  return weighted_product == a[index]
