#!/usr/bin/env python3

def empty_matrix(a):
  return len(a) == 0

def get_dimensions(a):
  if not len(a):
    return 0, 0
  return len(a), len(a[0])

def is_square(a):
  dimensions = get_dimensions(a)
  return dimensions[0] == dimensions[1] and empty_matrix(a) == False

def is_null(a):
  return len(list(filter(lambda x: x.count(0) == len(x), a))) == len(a)

# get the ith row vector
def get_ith_row(a, i):
  return [a[x][i] for x in range(len(a))]

# get the jth column vector
def get_jth_column(a, j):
  return a[j]

# get the diagonal of a matrix (has to be square)
def get_diagonal(a):
  if not is_square(a):
    raise Exception
  return [a[i][i] for i in range(len(a))]

def get_trace(a):
  return sum(get_diagonal(a))

def is_lower_triangular(a):
  below_diagonal = []
  for index, row in enumerate(a):
    reversed(row)
    below_diagonal.append(row[:index])
  return is_null(below_diagonal)

def is_upper_triangular(a):
  above_diagonal = []
  for index, row in enumerate(a):
    reversed(row)
    above_diagonal.append(row[1+index:])
  return is_null(above_diagonal)

def is_triangular(a):
	return is_upper_triangular or is_lower_triangular

def is_identity_matrix(a):
  if not is_square(a):
    return False
  all_ones = True
  for scalar in get_diagonal(a):
    if scalar != 1:
      all_ones = False
  return all_ones and is_upper_triangular(a) and is_lower_triangular(a)

def is_symmetric(a):
  # square matrices only
  if not is_square(a):
    return False
  # get the values for each triangle
  abovevalues, belowvalues = [], []
  for index, column in enumerate(a):
    reversed(column)
    for scalar in column[1+index:]:
      abovevalues.append(scalar)
    for scalar in column[:index]:
      belowvalues.append(scalar)
  # return whether the two triangles are identical
  return abovevalues == belowvalues
