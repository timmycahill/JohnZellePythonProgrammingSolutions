# main.py
from sphere import Sphere

def main():
    printIntroduction()
    sphere = getSphere()
    outputResults(sphere)

def printIntroduction():
    print("This program calculates the surface area and volume of a sphere with a given radius.\n")

def getSphere():
    radius = eval(input("Enter the radius of the sphere: "))
    return Sphere(radius)

def outputResults(sphere):
    print("\nSurface area: {0:0.2f}".format(sphere.surfaceArea()))
    print("\nVolume: {0:0.2f}".format(sphere.volume()))

if __name__ == "__main__":
    main()
