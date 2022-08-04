#!/usr/bin/env python3

from src.operations import *
from src.properties import *
from src.vectors import *
from tests.helper import *
from m4cs.adjugate_matrices import *
from m4cs.matrix_inversion import *
from math import sqrt


#### ORTHOGONAL MATRICES ####

def is_singular(a):
  return determinant(a) == 0

def is_orthogonal(a):
  return is_identity_matrix(matrix_multiplication(a, matrix_transpose(a)))
