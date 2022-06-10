#!/usr/bin/env python3

from src.matrix import *
import unittest

class MatrixPropertiesTest(unittest.TestCase):
  def test_property_methods(self):
    square_matrix = [
      [1, 2, 3],
      [17, 7, 6],
      [12, 2, 5]
    ]
    non_square_matrix = [
      [1, 2, 3, 24],
      [17, 7, 6, 16],
      [12, 2, 5, 3]
    ]
    emptymatrix = []

    # Test the empty matrix check
    self.assertFalse(empty_matrix(square_matrix))
    self.assertFalse(empty_matrix(non_square_matrix))
    self.assertTrue(empty_matrix(emptymatrix))

    # test checking if matrix is A in R_{n,n} (implicitly checks the dimensions)
    fails = False
    try:
      is_square(empty_matrix)
    except:
      fails = True
    self.assertTrue(fails)
    self.assertFalse(is_square(non_square_matrix))
    self.assertTrue(is_square(square_matrix))

  def test_null(self):
    o_matrix = [
      [0, 0, 0],
      [0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]
    ]
    not_o_matrix = [
      [12, 44],
      [22, 21]
    ]

    self.assertTrue(is_null(o_matrix))
    self.assertFalse(is_null(not_o_matrix))

  def test_get_vectors(self):
    example_matrix = [
      [1, 21, 4],
      [4, 24, 12],
      [12, 45, 41]
    ]
    self.assertEqual(get_ith_row(example_matrix, 1), [21, 24, 45])
    self.assertEqual(get_jth_column(example_matrix, 0), [1, 21, 4])
    self.assertEqual(get_diagonal(example_matrix), [1, 24, 41])

  def test_trace(self):
    example_matrix = [
      [1, 21, 4],
      [4, 24, 12],
      [12, 45, 41]
    ]
    self.assertEqual(get_trace(example_matrix), 66)

  def test_triangular(self):
    lower_triangular_matrix = [
      [1, 2, 3, 4],
      [0, 3, 4, 3],
      [0, 0, 3, 6],
      [0, 0, 0, 4]
    ]
    self.assertTrue(is_lower_triangular(lower_triangular_matrix))

    upper_triangular_matrix = [
      [1, 0, 0, 0],
      [3, 4, 0, 0],
      [7, 4, 7, 0],
      [8, 2, 1, 1],
    ]
    self.assertTrue(is_upper_triangular(upper_triangular_matrix))

  def test_identity_matrix(self):
    identity_matrix = [
      [1, 0, 0, 0],
      [0, 1, 0, 0],
      [0, 0, 1, 0],
      [0, 0, 0, 1]
    ]
    self.assertTrue(is_identity_matrix(identity_matrix))

    not_identity_matrix = [
      [1, 0, 0, 0],
      [3, 4, 0, 0],
      [7, 4, 7, 0],
      [8, 2, 1, 1],
    ]
    self.assertFalse(is_identity_matrix(not_identity_matrix))

  def test_symmetric(self):
    symmetric_matrix = [
      [1, 1, -1],
      [1, 2, 0],
      [-1, 0, 5]
    ]
    self.assertTrue(is_symmetric(symmetric_matrix))

    not_symmetric_matrix = [
      [1, 0, 0, 0],
      [3, 4, 0, 0],
      [7, 4, 7, 0],
      [8, 2, 1, 1],
    ]
    self.assertFalse(is_symmetric(not_symmetric_matrix))

if __name__ == "__main__":
  unittest.main()
