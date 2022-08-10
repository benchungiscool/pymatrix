#!/usr/bin/env python3

from src.operations import *
from src.properties import *
from src.vectors import *
from tests.helper import *
from m4cs.adjugate_matrices import *
from m4cs.matrix_inversion import *
from m4cs.orthogonal_matrices import is_singular
from copy import deepcopy

#### MATRIX RANK #### 

# thanks to user chiron on stackoverflow for these three functions
def ContinSubSeq(lst):
  size = lst
  ret = []
  for start in range(size):
    for end in range(start+1,size+1):
      ret.append([start, end])
  return ret

def submatrix_range(a, rows, cols):
  # as with the other submatrix function - make a copy to avoid touching master
  a = deepcopy(a)
  
  # get each value from input
  start_row, end_row = rows
  start_col, end_col = cols

  # make the end vals exclusive
  end_row += 1
  end_col += 1

  # combine these and make them into indices
  rows = slice(start_row, end_row)
  cols = slice(start_col, end_col)


  # reverse the lists to avoid problems associated with indices/list changes
  # rows.reverse()
  # cols.reverse()

  # i could use list slices - i dont understand why a[0:len(a)+1] works!
  """
  for row in rows:
    a.pop(row)
  """
  a = a[rows]
  ret = list(map(lambda x: x[cols], a))

  return ret

def get_submatrices(a, square=False):
  m, n = dimensions(a)
  ret = []

  # get the submatrices
  for start_row, end_row in ContinSubSeq(m):
    for start_col, end_col in ContinSubSeq(n):
      ret.append(submatrix_range(a, [start_row, end_row], [start_col, end_col]))

  # if square, filter out any mxn matrices - return this
  if square:
    return list(filter(lambda x: is_square(x), ret))

  return ret

def rank(a):
  rankmatrix = []
  submatrices = get_submatrices(a, square=True)
  non_singular_matrices = list(filter(lambda x: is_singular(x) == False, submatrices))

  largest_singular_matrix = []
  for matrix in non_singular_matrices:
    if dimensions(matrix)[0] > dimensions(largest_singular_matrix)[0]:
      largest_singular_matrix = matrix

  return len(largest_singular_matrix), largest_singular_matrix
  

def linearly_independent_rows(a):
  # get number of linearly independent rows
  ret = 0
  for i, row in enumerate(a):
    row_sum = [0] * len(row)
    # get the sum of rows - current row
    for j, second_row in enumerate(a):
      if j != i:
        row_sum = add_vectors(row_sum, second_row)
    if row_sum != row:
      ret += 1
  return ret

# the number of linearly independent rows in a == rank(a)
def rank_linear_dependency(a):
  return linearly_independent_rows(a) == rank(a)[0]

# let a = non-singular and pb be the rank of the matrix B. the rank of AB == pb
def sylvesters_lemma(a, b):
  return rank(matrix_multiplication(a, b)) == rank(b)

