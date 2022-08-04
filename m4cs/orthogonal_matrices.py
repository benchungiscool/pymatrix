#!/usr/bin/env python3

from src.operations import *
from src.properties import *
from src.vectors import *
from tests.helper import *
from m4cs.adjugate_matrices import *
from m4cs.matrix_inversion import *


#### ORTHOGONAL MATRICES ####

def is_singular(a):
  return determinant(a) == 0

def is_orthogonal(a):
  return inverse_matrix(a) == matrix_transpose(a)

if __name__ == "__main__":
  a = [
      [2, -2, 1],
      [1, 2, 2],
      [2, 1, -2],
  ]
  print(is_orthogonal(a))

