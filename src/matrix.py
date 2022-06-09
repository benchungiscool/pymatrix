#!/usr/bin/env python3

def empty_matrix(a):
  return len(a) == 0

def get_dimensions(a):
  if not len(a):
    raise Exception
  return len(a), len(a[0])

def is_square(a):
  dimensions = get_dimensions(a)
  return dimensions[0] == dimensions[1] & empty_matrix(a) == False

def is_null(a):
  return len(list(filter(lambda x: x.count(0) == len(x), a))) == len(a)

# get the ith row vector
def get_ith_row(a, i):
  return [a[x][i] for x in range(len(a))]

# get the jth row vector
def get_jth_row(a, j):
  return a[j]

# get the diagonal of a matrix (has to be square)
def get_diagonal(a):
  if not is_square(a):
    raise Exception
  return [a[i][i] for i in range(len(a))]

def get_trace(a):
  return sum(get_diagonal(a))
