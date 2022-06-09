#!/usr/bin/env python3

from src.pymatrix import *
import unittest

class TestVectorMethods(unittest.TestCase):
  def test_cartesian_product(self):
    a = [1,2,3]
    b = [2,3]
    correctanswer = [(1, 2), (1, 3), (2, 2), (2, 3), (3, 2), (3, 3)]
    self.assertEqual(cartesian_product(a, b), correctanswer)

  def test_add_vectors(self):
    # Test that adding vectors with differing cardinalities fails
    a = [1,2,3]
    b = [3,2]
    fails = False
    try:
      add_vectors(a,b)
    except:
      fails = True
    self.assertTrue(fails)

    # Check the result of adding two vectors of the same length
    b = [3,4,5]
    correctanswer = [4,6,8]
    self.assertEqual(add_vectors(a, b), correctanswer)

  def test_scalar_product(self):
    # Test providing the wrong values to the function
    fails = False
    try:
      scalar_product(1, [2,3,4])
    except:
      fails = True
    self.assertTrue(fails)

    # Check that when given correct input, function provides correct answer
    self.assertEqual(scalar_product([1,2,3], 10), [10, 20, 30])

  def test_vector_product(self):
    self.assertEqual(vector_product([1,2,3], [7,8,9]), [7,16,27])

if __name__ == "__main__":
    unittest.main()
