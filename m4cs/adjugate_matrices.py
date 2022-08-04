#!/usr/bin/env python3

from src.operations import *
from src.properties import *
from src.vectors import *
from tests.helper import *

#### ADJUGATE MATRICES ####

# return the submatrix, given the lists of rows and columns to be removed
# if you don't want to remove any rows or cols, just pass an empty list
def submatrix(a, r, s):
  # allow a user to pass ints
  if type(r) == int:
    r = [r]
  if type(s) == int:
    s = [s]

  # reverse sort so indices aren't affected by popping
  s.sort(reverse=True)

  # remove each column
  for target in s:
    for i, row in enumerate(a):
      row.pop(target)

  # remove each row
  for target in r:
    a.pop(target)

  return a

# i can't tell the difference between a major and a 3x3 determinant 
def major(a): return determinant(a)

# given a matrix and a tuple with element indices, return the complement submatrix
def complement_submatrix(a, element):
  a = deepcopy(a)
  row, col = element
  for i, r in enumerate(a):
    r.pop(col)
  a.pop(row)
  return a
  
# the determinant of the complement submatrix
def minor(a, element):
  return determinant(complement_submatrix(a, element))

def cofactor(a, element):
  return ((-1) ** sum(element)) * minor(a, element)

# the adjugate matrix is a matrix of each cofactor of a matrix
def adjugate_matrix(a):
  ret = []
  a = matrix_transpose(a)
  m, n = dimensions(a)
  if m != n:
    raise Exception("m != n")
  for i in range(m):
    cur = []
    for j in range(n):
      cur.append(cofactor(a, (i, j)))
    ret.append(cur)
  return ret


