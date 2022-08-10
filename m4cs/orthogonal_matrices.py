#!/usr/bin/env python3

from src.operations import *

#### ORTHOGONAL MATRICES ####

def is_singular(a):
  m,n = dimensions(a)
  if m != n:
    return False
  return determinant(a) == 0

def is_orthogonal(a):
  return is_identity_matrix(matrix_multiplication(a, matrix_transpose(a)))

