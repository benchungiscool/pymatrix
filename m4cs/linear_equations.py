from src.operations import *
from src.properties import *
from src.vectors import *
from tests.helper import *
from m4cs.matrix_inversion import *
from m4cs.orthogonal_matrices import *
from copy import deepcopy
from numpy import *

# convert a numpy array into a pymatrix one
def numpy_to_pymatrix(a, doInt=False):
  # use the numpy convert to list
  ret = a.tolist()
  
  if doInt:
    # function works on a nested list, so nest if not nested
    if any(isinstance(i, list) for i in ret):
      ret = [ret]
    # map the int() function to each row of ret
    for row in ret:
      row = list(map(lambda x: int(x), row))

  return ret

# convert a len(1) numpy array to a python list of ints
def array_to_vector(a):
  return [int(i) for i in a]

def linear_system_solve(coefficents, exit_vals):
  a = array(coefficents)
  b = array(exit_vals)
  return array_to_vector(round_(linalg.solve(a, b)))

# return the complete matrix for a system of linear equations
def complete_matrix(coefficents, exit_vals):
  ret = deepcopy(coefficents)
  for i, product in enumerate(exit_vals):
    ret[i].append(product)
  return ret

# get the coefficients of a linear system of equations from the complete one
def split_complete_matrix(a):
  return [i[:-1] for i in deepcopy(a)], [i[-1:] for i in deepcopy(a)]

# get the hybrid matrix of A_i
def hybrid_matrix(a, i):
  ret = deepcopy(a)
  # take a note of the last item in ret
  b = [i[-1] for i in ret]
  # make the replace the ith column with the nth b
  for index, row in enumerate(ret):
    row[i] = b[index]
  # remove the exit vals and return
  ret = [i[:-1] for i in ret]
  return ret

# solve a system of linear equations using cramer's system
def cramers_system(a):
  # get the determinant of the coefficients before making hybrid matrix
  detA = determinant(split_complete_matrix(a)[0])

  # for each hybrid matrix, append det(hybrid(a) / det(a)
  ret = []
  for i, item in enumerate(a):
    hybridA = hybrid_matrix(a, i)
    ret.append(determinant(hybridA) / detA)
  return ret

if __name__ == "__main__":
  coefficents = [
          [2, -1, 1],
          [1, 0, 2],
          [1, -1, 0]
        ]
  exit_vals = [3, 3, 1]
  a = complete_matrix(coefficents, exit_vals)
  print(cramers_system(a))
