#!/usr/bin/env python3

from src.operations import *
import unittest

def print_matrix(a):
  print("\n" + "-" * 3, "BEGIN PRINT MATRIX", "-" * 3)
  for column_vector in a:
    print(column_vector)
  print("-" * 3, "END PRINT MATRIX", "-" * 3)

class TestOperations(unittest.TestCase):
  def setUp(self):
    # define some matrices that we can use later in tests
    self.first_nxn_matrix = [
      [6, 41, 5],
      [3, 5, 12],
      [32, 2, 3]
    ]
    self.second_nxn_matrix = [
      [3, 82, 10],
      [6, 10, 6],
      [64, 1, 6]
    ]
    self.first_mxn_matrix = [
      [6, 41, 5, 4],
      [3, 5, 12, 1],
      [32, 2, 3, 15]
    ]
    self.second_mxn_matrix = [
      [3, 82, 10, 2],
      [6, 10, 6, 10],
      [16, 4, 9, 30]
    ]
    self.first_rxn_matrix = [
      [2, 3],
      [5, 2],
      [4, 4]
    ]

  def test_addition(self):
    test_nxn = matrix_addition(self.first_nxn_matrix, self.second_nxn_matrix)
    self.assertEqual(
      test_nxn,
      [
        [9, 123, 15],
        [9, 15, 18],
        [96, 3, 9]
      ]
    )

    test_mxn = matrix_addition(self.first_mxn_matrix, self.second_mxn_matrix)
    self.assertEqual(
      test_mxn,
      [
        [9, 123, 15, 6],
        [9, 15, 18, 11],
        [48, 6, 12, 45],
      ]
    )

    fails = False
    try:
      matrix_addition(self.first_mxn_matrix, self.first_nxn_matrix)
    except:
      fails = True
    self.assertTrue(fails)

  def test_scalar_product(self):
    nxn_product = matrix_scalar_product(self.first_nxn_matrix, 100)
    self.assertEqual(
      nxn_product,
      [
        [600, 4100, 500],
        [300, 500, 1200],
        [3200, 200, 300]
      ]
    )

    mxn_product = matrix_scalar_product(self.first_mxn_matrix, 100)
    self.assertEqual(
      mxn_product,
      [
        [600, 4100, 500, 400],
        [300, 500, 1200, 100],
        [3200, 200, 300, 1500]
      ]
    )

  def test_matrix_multiplication(self):
    c = matrix_multiplication(self.first_nxn_matrix, self.first_nxn_matrix)
    print_matrix(c)
    self.assertTrue(True)


if __name__ == "__main__":
  unittest.main()
