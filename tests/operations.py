#!/usr/bin/env python3

from src.operations import *
from tests.helper import *
import unittest

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
    self.first_nxr_matrix = [
      [5, 2, 11],
      [6, 7, 1]
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
    # these multiplications are not possible
    first = [
      [1, -1],
      [0, 2],
      [1, 5]
    ]
    fails = False
    try:
      matrix_multiplication(first, first)
    except:
      fails = True
    self.assertTrue(fails)

    first = [
      [1, 0, 2],
      [3, 1, 4],
      [5, 7, 2]
    ]
    second = [
      [0, 1],
      [2, 7]
    ]
    fails = False
    try:
      matrix_multiplication(first, second)
    except:
      fails = True
    self.assertTrue(fails)

    fails = False
    try:
      matrix = matrix_multiplication(self.first_mxn_matrix, self.second_mxn_matrix)
    except:
      fails = True
    self.assertTrue(fails)


    # these should work
    matrix = matrix_multiplication(self.first_nxn_matrix, self.first_nxn_matrix)
    self.assertEqual(
      matrix,
      [
        [319, 461, 537],
        [417, 172, 111],
        [294, 1328, 193]
      ]
    )

    matrix = matrix_multiplication(self.first_rxn_matrix, self.first_nxr_matrix)
    self.assertEqual(
      matrix,
      [
        [28, 25, 25],
        [37, 24, 57],
        [44, 36, 48]
      ]
    )

  def test_2x2_determinant(self):
    # test that it doesn't work for 3x3 or 4x3
    fails = False
    try:
      matrix = m2_determinant(self.first_nxn_matrix)
    except:
      fails = True
    self.assertTrue(fails)

    fails = False
    try:
      matrix = m2_determinant(self.first_mxn_matrix)
    except:
      fails = True
    self.assertTrue(fails)

    self.assertEqual(
      m2_determinant(
        [
          [4, 2],
          [21, 4]
        ]
      ),
      -26
    )

  def test_determinant(self):
    m5_matrix = [
      [6, 64, 100, 12, 2],
      [16, 4, 10, 42, 5],
      [52, 6, 6, 16, 1],
      [24, 69, 10, 22, 8],
      [32, 62, 103, 14, 76]
    ]
    m4_matrix = [
      [1,2,3,4],
      [132, 42, 21, 2],
      [214, 22, 22, 1],
      [2, 42, 6, 2]
    ]
    self.assertEqual(determinant(m5_matrix), 878372156)
    self.assertEqual(determinant(m4_matrix), -121150)

  def test_linear_combination(self):
    a = [
      [0, 1, 1],
      [3, 2, 1],
      [6, 5, 3]
    ]
    self.assertTrue(linear_combination(a, 2))

if __name__ == "__main__":
  unittest.main()
