from src.operations import *
from src.properties import *
from src.vectors import *
from tests.helper import *
from m4cs.matrix_rank import *
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

def linear_system_solve(coefficents, known_terms):
  a = array(coefficents)
  b = array(known_terms)
  return array_to_vector(round_(linalg.solve(a, b)))

# return the complete matrix for a system of linear equations
def complete_matrix(coefficents, known_terms):
  ret = deepcopy(coefficents)
  for i, product in enumerate(known_terms):
    ret[i].append(product)
  return ret

# get the coefficients of a linear system of equations from the complete one
def split_complete_matrix(a):
  return [i[:-1] for i in deepcopy(a)], [i[-1:] for i in deepcopy(a)]

def is_solution(a, solution):
  ret = deepcopy(a)
  incomplete_matrix, known_terms = split_complete_matrix(ret)

  # each row multiplied by solution should == 0
  solution_prod = []
  for row in ret:
    row_prod = []
    for elem, scalar in zip(row, solution):
      row_prod.append(elem * scalar)
    solution_prod.append(sum(row_prod))

  # return true if the solution mapped to a is the known terms
  return solution_prod == known_terms
    

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

  # for each hybrid matrix, append det(hybrid(a) / det(a))
  ret = []
  for i, item in enumerate(a):
    hybridA = hybrid_matrix(a, i)
    ret.append(determinant(hybridA) / detA)

  return ret

# provide complete matrix, returns true if compatible
def is_compatible(a):
  # get incomplete matrix
  incomplete_matrix, known_terms = split_complete_matrix(a)
  # is only compatible if the rank(coefficients) == rank(a)
  if rank(incomplete_matrix) == rank(a):
    return True
  return False

# returns true if no solutions for a
def is_incompatible(a):
  coefficients = split_complete_matrix(a)[0]
  return rank(coefficients)[0] < rank(a)[0]

def is_cramers_system(a):
  coefficients = split_complete_matrix(a)[0]
  m, n = dimensions(coefficients)
  return rank(coefficients)[0] == rank(a)[0] == m == n

# returns true if a row is a linear combination
def is_linear_combination(a, i):
  ret = deepcopy(a)
  target_row = ret[i]
  ret = ret[:i]
  target_vector = [0] * len(a[0])
  for i in ret:
    target_vector = add_vectors(target_vector, i)
  return target_vector == target_row

# use this for case 2, where rank(a) == rank(ac) == rank == n < m
def cancel_cramer_system(a):
  ret = deepcopy(a)
  
  # check if each row is a linear combination
  linear_combination_indices = []
  for index, i in enumerate(ret):
    if is_linear_combination(ret, index):
      linear_combination_indices.append(index)

  # pop each cancellable row
  for i in linear_combination_indices:
    ret.pop(i)

  # now return the cramer system solution
  if is_cramers_system(ret):
    return cramers_system(ret)

# returns true if conforms to rouché-capelli theorem
def is_undetermined(a):
  ret = deepcopy(a)
  m,n = dimensions(ret)
  coefficients, known_terms = split_complete_matrix(ret)

  # check the coefficient matrix is singular
  if not is_singular(coefficients):
    raise Exception("Complete matrix is not singular")

  # get the ranks of the complete/incomplete matrix
  incomplete_rank = rank(coefficients)[0]
  complete_rank = rank(ret)[0]

  # if the ranks of these are the same, and more than n, the matrix is undetermined
  return complete_rank == incomplete_rank and complete_rank < n

def is_homogenous(a):
  known_terms = split_complete_matrix(a)[1]
  return known_terms == [[0]] * len(known_terms)

def general_solution_homogenous(a):
  incomplete_matrix = split_complete_matrix(a)[0]
  return is_homogenous(a) and is_singular(incomplete_matrix)

