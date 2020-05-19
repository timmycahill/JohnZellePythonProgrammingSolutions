# exercise3.py
#       Write definitions for these functions:
#
#   sphereArea(radius): Returns the surface area of a sphere having the given
#       radius.
#
#   sphereVolume(radius): Returns the volume of a shpere having the given
#       radius.
#
#       Use your functions to solve Programming Exercise 1 from Chapter 3.

import math

def sphereArea(radius):
    return 4 * math.pi * radius ** 2

def sphereVolume(radius):
    return 4 / 3 * math.pi * radius ** 3

def main():
    print("This program calculates the volume and surface area of a sphere " +
          "given its radius.\n")
    
    radius = eval(input("Enter the radius of the sphere: "))

    volume = sphereVolume(radius)
    surfaceArea = sphereArea(radius)

    print("The volume of the sphere is", volume, "and the surface area is",
          surfaceArea)

main()
