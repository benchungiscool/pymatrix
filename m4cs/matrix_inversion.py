#!/usr/bin/env python3

from src.operations import *
from src.properties import *
from src.vectors import *
from tests.helper import *
from m4cs.adjugate_matrices import *

#### INTRO TO MATRIX INVERSION ####

# returns true if a matrix is invertible
def is_invertible(a):
  product_matrix = matrix_multiplication(a, adjugate_matrix(a))
  return is_identity_matrix(product_matrix)

# invert an m2 matrix
def m2_inverse_matrix(a):
  c, d = a[1]
  a, b = a[0]
  return [[d, -b], [-c, a]]

# invert a matrix
def inverse_matrix(a):
  # special case for when m=2
  if dimensions(a) == (2,2):
    return m2_inverse_matrix(a)
  if is_invertible(a):
    return adjugate_matrix(a)
  else:
    raise Exception("Can't invert matrix")
  
