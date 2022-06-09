#!/usr/bin/env python3

def same_length(a, b):
  return len(a) == len(b)

# get the cartesian product of two sets
def cartesian_product(a, b):
  ret = []
  for ai in a:
    for bi in b:
      ret.append((ai, bi))
  return ret

# get the sum of two vectors
def add_vectors(a, b):
  ret = []
  if not same_length(a, b):
    raise Exception
  for ai, bi in zip(a, b):
    ret.append(ai + bi)
  return ret

def scalar_product(vector, scalar):
    # check that the correct type of input is given
    if len(vector) <= 1 or type(scalar) != (int or float):
      raise Exception
    return list(map(lambda x: x * scalar, vector))

def vector_product(a, b):
    if not same_length(a, b):
      raise Exception
    return [a[i] * b[i] for i in range(len(a))]

