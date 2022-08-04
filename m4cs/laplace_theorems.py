#!/usr/bin/env python3

from src.operations import *
from src.properties import *
from src.vectors import *
from tests.helper import *
from m4cs.adjugate_matrices import *

"""
He put his whole laplussy into this one
"""

#### LAPLACE THEOREMS ####

# it's much simpler to calculate the determinant of a square matrix
def first_laplace_theorem(a):
  ret = []
  m, n = dimensions(a)
  if m != n:
    raise Exception("m != n")
  for j in range(n):
    ret.append(a[0][j] * cofactor(a, (0, j))) 
  return sum(ret)

# the sum of (the element of one line * the cofactors of another) always == 0 (this one goes crazy)
def second_laplace_theorem(a):
  ret = []
  m, n = dimensions(a)
  if m != n:
    raise Exception("m != n")
  for j in range(n):
    ret.append(a[0][j] * cofactor(a, (1, j)))
  return sum(ret) == 0

