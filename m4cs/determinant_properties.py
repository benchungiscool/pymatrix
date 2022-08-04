#!/usr/bin/env python3

from src.operations import *
from src.properties import *
from src.vectors import *
from tests.helper import *

#### DETERMINANT PROPERTIES ####
# det(a) == det(A^T)
def determinant_transposed(a):
	return determinant(a) == determinant(matrix_transpose(a))

# det(a) == tr(a) when a is triangular
def determinant_triangular_matrix(a):
	if not is_triangular(a):
		raise Exception("Matrix isn't triangular")
	return get_trace(a)

# if you have the determinant of a matrix a, when two rows or columns are swapped
# the determinant of the modified matrix a[s] == -det(a)
def determinant_row_swap(a):
	detA = determinant(a)
	a[0], a[1] = a[1], a[0]
	detAs = determinant(a)
	return detAs == -detA

# if two rows of a matrix are identical then the determinant = 0
def null_determinant(a):
	return determinant(a) == 0

# if you multiply a row by by a scalar f, the determinant is f*det(a)
def row_by_scalar(a):
	detA = determinant(a)
	a[0] = scalar_product(a[0], 2)
	return determinant(a) == 2 * detA

# if you multiply a matrix by by a scalar f, the determinant is f^2 * det(a)
def matrix_by_scalar(a):
	detA = determinant(a)
	a = matrix_scalar_product(a, 2)
	return determinant(a) == (2 ** dimensions(a)[1]) * detA

# det(ab) == det(a) * det(b)
def product_determinant(a):
	b = matrix_transpose(a)
	return determinant(matrix_multiplication(a, b)) == determinant(a) * determinant(b)

