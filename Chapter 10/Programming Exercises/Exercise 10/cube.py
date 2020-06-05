# cube.py

class Cube:
	def __init__(self, side):
		self.side = side

	def getSideLength(self):
		return self.side

	def surfaceArea(self):
		return self.side ** 2 * 6

	def volume(self):
		return self.side ** 3