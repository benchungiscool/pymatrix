from src.properties import get_dimensions

class Matrix:
	def __init__(self, vals):
		self.vals = vals

	def __getitem__(self, item):
		return self.vals[item]

	def __len__(self):
		return len(self.vals)

