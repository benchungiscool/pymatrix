from src.properties import get_dimensions
from random import randint, randrange

class Matrix:
	def __init__(self, *kwargs):
		if vals: self.fromVals(vals)
		else: self.vals = []

	def fromVals(self, vals: list):
		self.vals = vals

	def genRow(self, n, lowerBound, upperBound):
		ret = []
		for i in range(n):
			ret.append(randint(lowerBound, upperBound))
		return ret

	def fromDimensions(self, m: int, n:int, lowerBound=-1024, upperBound=1024):
		self.vals = [self.genRow(n, lowerBound, upperBound) for j in range(m)]

	def __getitem__(self, item):
		return self.vals[item]

	def __len__(self):
		return len(self.vals)

	def __str__(self):
		ret = []
		for row in self.vals:
			ret.append(str(row) + '\n')
		return "".join(ret)

	def __iter__(self):
		return self

if __name__== "__main__":
	m = Matrix().fromDimensions(3,3)
	print(m)
