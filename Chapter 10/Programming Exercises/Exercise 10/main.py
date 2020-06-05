# main.py
from cube import Cube

def main():
	printIntroduction()
	cube = getCube()
	outputResults(cube)

def printIntroduction():
	print("This program calculates the surface area and volume of a cube.\n")

def getCube():
	side = eval(input("Enter the side length: "))
	return Cube(side)

def outputResults(cube):
	print("\nA cube with a side length {0} has a surface area of {1} and a volume of {2}.".format(cube.getSideLength(), cube.surfaceArea(), cube.volume()))

if __name__ == "__main__":
	main()